"""Reusable helpers for Gaia analyses.

- query_gaia_cached: run an ADQL query once and cache the result as FITS in data/raw, with
  the query text and the service used saved next to it (provenance). If the ESA Gaia archive
  is not reachable, the same query is sent to a Gaia partner data centre (mirror) instead.
- Quality-cut helpers for Gaia (E)DR3 photometry and astrometry.

References: Riello et al. 2021 (A&A 649, A3) for the corrected BP/RP flux excess C*;
Lindegren et al. 2021 (A&A 649, A4) for RUWE and the parallax zero point.
"""
from __future__ import annotations

import datetime as _dt
from pathlib import Path

import numpy as np
from astropy.table import Table

# Services are tried in this order. All serve gaiadr3.gaia_source with the official column
# names, so the same ADQL works everywhere. The partner data centres are mirrors of the
# ESA archive; the data are identical.
GAIA_TAP_SERVICES = [
    ("ESA Gaia archive", "https://gea.esac.esa.int/tap-server/tap"),
    ("ARI Heidelberg (Gaia partner data centre)", "https://gaia.ari.uni-heidelberg.de/tap"),
    ("AIP Potsdam (Gaia partner data centre)", "https://gaia.aip.de/tap"),
]


def _reachable(url: str, timeout: float = 10.0) -> bool:
    """True if the server answers at all within `timeout` seconds (any HTTP status counts)."""
    import requests

    try:
        requests.get(url.rstrip("/") + "/availability", timeout=timeout)
        return True
    except requests.exceptions.RequestException:
        return False


def _run_tap_async(url: str, adql: str, maxrec: int, timeout: float) -> Table:
    """Submit an asynchronous TAP job, wait for it and return the result as an astropy Table."""
    import pyvo

    service = pyvo.dal.TAPService(url)
    job = service.submit_job(adql, maxrec=maxrec)
    job.run()
    job.wait(phases=["COMPLETED", "ERROR", "ABORTED"], timeout=timeout)
    job.raise_if_error()
    result = job.fetch_result()
    try:
        job.delete()
    except Exception:  # deleting the server-side job is a courtesy, not essential
        pass
    if getattr(result, "query_status", "OK") == "OVERFLOW":
        raise RuntimeError(
            f"The result was truncated at the row limit ({maxrec} rows requested). "
            "Narrow the query or ask for a higher limit; nothing was saved."
        )
    return result.to_table()


def query_gaia_cached(adql: str, out_path, overwrite: bool = False, services=None,
                      maxrec: int = 5_000_000, timeout: float = 3600.0) -> Table:
    """Run an ADQL query on Gaia, or load the cached result.

    The result is written to `out_path` (FITS). The ADQL text, the service that answered and
    the date are written to the same name with suffix .adql. If the file exists and overwrite
    is False, nothing is downloaded.

    services: list of (name, TAP URL); default GAIA_TAP_SERVICES (ESA first, then mirrors).
    timeout: maximum time in seconds to wait for one server to finish the job.
    """
    out_path = Path(out_path)
    if out_path.exists() and not overwrite:
        print(f"Loading cached result: {out_path}")
        return Table.read(out_path)

    services = services or GAIA_TAP_SERVICES
    errors = []
    for name, url in services:
        print(f"Trying {name} ({url}) ...")
        if not _reachable(url):
            print("  not reachable, trying the next service")
            errors.append(f"{name}: not reachable")
            continue
        print("  reachable. Job submitted, waiting for the result (can take several minutes) ...")
        try:
            table = _run_tap_async(url, adql, maxrec=maxrec, timeout=timeout)
        except Exception as exc:  # report and fall through to the next service
            print(f"  failed: {type(exc).__name__}: {exc}")
            errors.append(f"{name}: {type(exc).__name__}: {exc}")
            continue

        table.meta = {}  # server metadata can break FITS headers; provenance is stored separately
        out_path.parent.mkdir(parents=True, exist_ok=True)
        table.write(out_path, overwrite=True)
        stamp = _dt.datetime.now().isoformat(timespec="seconds")
        out_path.with_suffix(".adql").write_text(
            f"-- service: {name} ({url})\n-- retrieved: {stamp}\n-- rows: {len(table)}\n"
            + adql.strip() + "\n",
            encoding="utf-8",
        )
        print(f"Saved {len(table)} rows from {name} to {out_path}")
        return table

    raise ConnectionError("No Gaia service answered:\n  " + "\n  ".join(errors))


def bp_rp_excess_corrected(excess_factor, bp_rp):
    """Corrected BP/RP flux excess factor C* (Riello et al. 2021, Eq. 6 and Table 2).

    C* = C - f(BP-RP). C* scatters around 0 for well-behaved sources.
    Check the coefficients against the paper (they are reproduced here from it).
    """
    c = np.asarray(excess_factor, dtype=float)
    x = np.asarray(bp_rp, dtype=float)
    f = np.full_like(x, np.nan)

    blue = x < 0.5
    mid = (x >= 0.5) & (x < 4.0)
    red = x >= 4.0

    f[blue] = 1.154360 + 0.033772 * x[blue] + 0.032277 * x[blue] ** 2
    f[mid] = (1.162004 + 0.011464 * x[mid] + 0.049255 * x[mid] ** 2
              - 0.005879 * x[mid] ** 3)
    f[red] = 1.057572 + 0.140537 * x[red]
    return c - f


def sigma_c_star(g_mag):
    """1-sigma scatter of C* as a function of G (Riello et al. 2021, Eq. 18)."""
    g = np.asarray(g_mag, dtype=float)
    with np.errstate(invalid="ignore"):  # NaN or negative G gives NaN, which fails the cut
        return 0.0059898 + 8.817481e-12 * g ** 7.618399


def absolute_mag(app_mag, parallax_mas):
    """Absolute magnitude from apparent magnitude and parallax in mas (no extinction)."""
    return np.asarray(app_mag, float) + 5.0 * np.log10(np.asarray(parallax_mas, float)) - 10.0
