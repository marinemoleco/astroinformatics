# Runbook: how to work with this project

Last updated: 2026-11-15. Master copy lives here on H:. This file is updated at the end of every working session.

## 1. Quick start (every session)
1. Connect the USB drive and check that it is still H:.
2. Open the Windows Command Prompt (cmd).
3. Activate the environment:
   `D:\Astronomie\envs\astro\Scripts\activate`
   The prompt now starts with `(astro)`.
4. Start Jupyter:
   `jupyter lab --notebook-dir H:\Astronomie`
5. Open or create a notebook in the project folder and select the kernel "Astro (Python)" (top right).
6. Stop Jupyter with Ctrl+C in the Command Prompt window, then eject H: via "Safely remove hardware".

## 2. Where things are
- `H:\Astronomie\data\raw\` downloaded data, never modified
- `H:\Astronomie\data\processed\` cleaned tables and intermediate results
- `H:\Astronomie\projects\<NN_name>\` one folder per analysis: `README.md`, `notebooks\`, `figures\`
- `H:\Astronomie\shared\config.py` base path and helpers (change the drive letter here only)
- `H:\Astronomie\shared\gaia_tools.py` cached Gaia archive queries and Gaia quality-cut helpers
- `H:\Astronomie\docs\` this runbook, changelog, `GLOSSARY.md`, `literature\references.bib` (shared bibliography for Zotero)
- `D:\Astronomie\envs\astro\` Python virtual environment
- `D:\Astronomie\backup\` backups of notebooks, figures and docs

## 3. Software
- Windows PC, system Python 3.10.6, virtual environment `astro` (venv, no conda)
- Python packages (installed 2026-11-15): jupyterlab 4.6.6, numpy 2.2.6, scipy 1.15.3, pandas 2.3.3, matplotlib 3.10.9, seaborn 0.13.2, scikit-learn 1.7.2 (includes HDBSCAN), astropy 6.1.7, astroquery 0.4.11, pyvo 1.10.0, lightkurve 2.6.0, reproject 0.14.1
- R is installed for statistics where better suited
- Planned: TOPCAT and Aladin (interactive tables and sky maps), Siril (images), Zotero (references)
- The authoritative package list is `H:\Astronomie\requirements.txt`. `environment.yml` is unused (conda plan abandoned).

## 4. Adding or updating packages
1. Activate the environment (step 1.3).
2. `pip install <package>` or `pip install --upgrade <package>`.
3. Add the package to `requirements.txt` and write one line into `docs\CHANGELOG.md`.
4. Record the exact versions: `pip freeze > H:\Astronomie\requirements-lock.txt`

Rebuild from scratch if the environment breaks:
```
rmdir /s /q D:\Astronomie\envs\astro
python -m venv D:\Astronomie\envs\astro
D:\Astronomie\envs\astro\Scripts\activate
python -m pip install --upgrade pip
pip install -r H:\Astronomie\requirements.txt
python -m ipykernel install --user --name astro --display-name "Astro (Python)"
```

## 5. Backup
Raw data are not backed up (they can be downloaded again). Everything else is small:
```
robocopy H:\Astronomie\projects D:\Astronomie\backup\projects /E /XD .ipynb_checkpoints
robocopy H:\Astronomie\docs D:\Astronomie\backup\docs /E
robocopy H:\Astronomie\shared D:\Astronomie\backup\shared /E
```

## 6. Data downloads (Gaia archive)
- Queries run through `query_gaia_cached()` in `shared\gaia_tools.py`. It tries the ESA Gaia archive first and, if that does not answer within 10 s, the Gaia partner data centres ARI Heidelberg and AIP Potsdam (identical copies of the catalogue, same table and column names). The first run downloads and saves the result as FITS in `data\raw\` together with a `.adql` file holding the exact query, the service that answered and the date. Later runs load the file and need no internet.
- Connection test from the command prompt: `powershell Test-NetConnection gea.esac.esa.int -Port 443` (`TcpTestSucceeded : True` means reachable). Same for `gaia.ari.uni-heidelberg.de` and `gaia.aip.de`.
- After `shared\gaia_tools.py` has changed, restart the kernel (Kernel, Restart Kernel) so the notebook loads the new version.
- To force a fresh download (for example after changing the query), delete the FITS file or call the function with `overwrite=True`.
- Always filter on the server (WHERE clause), never download whole catalogues.
- Before the Gaia DR4 release on 2 December 2026 the archive expects a downtime of a few working days.

## 7. Known issues
- lightkurve prints a warning about `tpfmodel` and `oktopus` on import. Harmless, we do not use that submodule.
- `TimeoutError: [WinError 10060]` or "Status messages could not be retrieved" when querying Gaia: the ESA archive is not reachable (seen on 2026-11-15, home network fine). `query_gaia_cached()` now falls back to the partner data centres automatically.
- `FileNotFoundError: H:\Astronomie not found` from `config.py`: the drive is not connected or has another letter. Fix the letter in `shared\config.py`.
- `conda` is not installed and not needed.
- Python 3.10 no longer receives upstream security fixes. Not a concern for local analysis. A newer Python can be added later as a second venv.

## 8. Working with Claude
- One chat per analysis inside the Claude project "Hobby Astronomy". Chat names: "01 Gaia Pleiades", "02 ...".
- Every analysis starts with a literature step (see `docs\literature\`).
- At the end of each session Claude updates: the project README, this runbook if tools changed, `CHANGELOG.md`, and the glossary.
- Model and effort: Claude points out at phase transitions when to switch (end of its reply, one line). Rule of thumb: Opus 5.5 (optionally Fable 5.2) at high effort for the literature step, method design, interpretation and hard debugging; Sonnet 5.5 at medium effort for notebooks, plots and queries; Sonnet 5.5 or Haiku 5.5 at low effort for docs and small edits.
- If Claude cannot see the local folder in a new chat, the folder has to be connected again (Add folder in the Claude desktop app).

## 9. Projects
| No. | Name | Question | Status |
|-----|------|----------|--------|
| 01 | Gaia Pleiades | Neighborhood HR diagram, membership and age of the Pleiades | in progress: literature done, notebook 1 ready to run |
| 02 | TESS transit | Transit fit of a known planet candidate | planned |
| 03 | Galaxies | Color versus morphology (SDSS, Galaxy Zoo) | planned |
| 04 | Visual | Color image from public FITS data | planned |
