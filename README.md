# Astroinformatics

Hobby astronomy with public data: short, reproducible analyses of data from telescopes, probes and
satellites, run on a single desktop PC. Focus on stars, the Milky Way, light curves, exoplanets and
galaxies. Every analysis is documented step by step, with the data release, the query date and the
software versions, so that it can be repeated.

The author is a marine microbiologist (population genetics) learning astronomy in his spare time. Many
explanations therefore use analogies to population genetics. Mistakes will happen and are documented when
found. Corrections are welcome as GitHub issues.

Selected analyses are also written up on the blog: https://astronomy.iba-science.de

## Topics and notebooks

Notebooks are numbered consecutively across all topics (01, 02, 03, ...). The number appears in the
notebook file name, the figure names, the commit message and the name of the working session, so each
notebook can be found under one number. The topic folders carry no number.

| Topic | Folder | Notebooks | Question | Status |
|-------|--------|-----------|----------|--------|
| Gaia Pleiades | `projects/gaia_pleiades` | 01 to 04 (01 done) | HR diagram of the solar neighbourhood, membership and age of the Pleiades (Gaia DR3, later DR4) | in progress |
| TESS transit | `projects/tess_transit` (planned) | from 05 | Transit fit of a known TESS planet candidate | planned |
| Galaxies | planned | | Galaxy colour versus morphology (SDSS, Galaxy Zoo) | planned |
| Visual | planned | | Colour image from public FITS data | planned |

Each topic folder has its own `README.md` (question, background, method, steps, results, open points),
a `literature.md` (state of knowledge), `notebooks/` and `figures/`.

## Repository layout

```
projects/    one folder per topic: gaia_pleiades, ...
docs/        RUNBOOK.md (how to work), CHANGELOG.md (one entry per session),
             GLOSSARY.md, literature/references.bib (shared bibliography)
shared/      reusable helpers: config.py (base path), gaia_tools.py (cached Gaia queries)
data/raw/    the ADQL query files (exact query, archive, date and row count of each download)
requirements.txt   Python packages
```

Downloaded data (FITS tables) are not part of the repository. Each notebook downloads what it needs from
the public archive with a server-side filtered ADQL query (see `shared/gaia_tools.py`), and the `.adql`
file in `data/raw/` records exactly which query was run. Notebooks are stored with their outputs, so
results and figures can be inspected without re-running them. The copyrighted publications cited in the
bibliography are not included.

## Rebuilding the environment

Tested on Windows with Python 3.10 (virtual environment, no conda). The package versions used so far are
listed in `docs/RUNBOOK.md`.

```
python -m venv astro
astro\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name astro --display-name "Astro (Python)"
jupyter lab
```

The base path of the project is set in one place, `shared/config.py` (variable `BASE`). Change it to the
folder where you cloned the repository. Then open a notebook and select the kernel "Astro (Python)".

## Data and acknowledgements

Analyses so far use data from the European Space Agency (ESA) mission Gaia
(https://www.cosmos.esa.int/gaia), processed by the Gaia Data Processing and Analysis Consortium (DPAC),
accessed through the ESA Gaia archive or the partner data centres ARI Heidelberg and AIP Potsdam.
Bibliography: `docs/literature/references.bib`.

## Licences

- Code (including the code cells of notebooks): MIT, see `LICENSE`.
- Texts and figures: CC BY 4.0, see `LICENSE-CC-BY-4.0.md`.
- Data remain under the terms of the respective archives.
