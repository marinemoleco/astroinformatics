# Runbook: how to work with this project

Last updated: 2026-11-16. Master copy lives here on H:. This file is updated at the end of every working session.

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
- `H:\Astronomie\projects\<topic>\` one folder per topic, without number (for example `gaia_pleiades`): `README.md`, `literature.md`, `notebooks\`, `figures\`
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
- The authoritative package list is `H:\Astronomie\requirements.txt`. The `environment.yml` of the abandoned conda plan was deleted on 2026-11-16.

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

The GitHub repository (section 10) is an additional copy of notebooks, figures, code and docs, but not of raw data or the blog. The robocopy backup stays.

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
- `git add` prints "LF will be replaced by CRLF" warnings: harmless (Windows line endings).
- `fatal: detected dubious ownership` from git on the USB drive: `git config --global --add safe.directory H:/Astronomie`.
- `git push` says "Authentication failed": the browser login was not completed. Repeat the push and log in to GitHub in the browser window. Passwords and tokens never go into the chat or into files.

## 8. Working with Claude
- One chat per notebook inside the Claude project "Astroinformatics". Chat names: "<NN> <Topic>, Notebook <N>", for example "02 Gaia Pleiades, Notebook 2". Chats numbered 00 are for setup and planning (for example "00 GitHub-Setup").
- Numbering: notebooks are numbered consecutively across all topics (01, 02, 03, ...). The same number is used for the notebook file (`02_pleiades_membership.ipynb`), the figure prefix (`02_...png`), new ADQL files, the commit message (`02: ...`), the tag (`nb02`) and the chat name. Topic folders carry no number.
- Every analysis starts with a literature step (see `docs\literature\`).
- At the end of each session Claude updates: the project README, this runbook if tools changed, `CHANGELOG.md`, and the glossary.
- Model and effort: Claude points out at phase transitions when to switch (end of its reply, one line). Rule of thumb: Opus 5.5 (optionally Fable 5.2) at high effort for the literature step, method design, interpretation and hard debugging; Sonnet 5.5 at medium effort for notebooks, plots and queries; Sonnet 5.5 or Haiku 5.5 at low effort for docs and small edits.
- At the end of each session Claude also gives the git commands (section 10) and checks the file list of `git status` before anything is pushed.
- If Claude cannot see the local folder in a new chat, the folder has to be connected again (Add folder in the Claude desktop app).

## 9. Topics
| Topic | Folder | Notebooks | Question | Status |
|-------|--------|-----------|----------|--------|
| Gaia Pleiades | `projects\gaia_pleiades` | 01 to 04 | Neighborhood HR diagram, membership and age of the Pleiades | in progress: literature and notebook 01 done, notebook 02 next |
| TESS transit | `projects\tess_transit` | from 05 | Transit fit of a known planet candidate | planned |
| Galaxies | planned | | Color versus morphology (SDSS, Galaxy Zoo) | planned |
| Visual | planned | | Color image from public FITS data | planned |

## 10. GitHub (public repository)
Repository: https://github.com/marinemoleco/astroinformatics (public, created 2026-11-16). It is one repository for everything. Each topic is a folder `projects\<topic>`. `H:\Astronomie` is the working copy.

In the repository: `projects\`, `docs\` (from `literature\` only `references.bib`), `shared\`, `data\raw\*.adql` (the exact queries), `requirements.txt`, `README.md`, `LICENSE` (MIT, code) and `LICENSE-CC-BY-4.0.md` (texts and figures).
Not in the repository (listed in `.gitignore`): `blog\` (stays local), everything in `data\` except the `.adql` files, the literature PDFs (copyright), notebook checkpoints, caches and credentials of any kind.

One-time setup (done 2026-11-16): `git config --global` for `user.name`, `user.email` (the iba-science.de address), `init.defaultBranch main` and `safe.directory H:/Astronomie`. Login to GitHub through the browser window that opens at the first push. Passwords and tokens never go into the chat or into files.

### End of every session (one commit per session)
Write the CHANGELOG entry first, so that it is part of the commit. Then:
```
cd /d H:\Astronomie
git status
git add -A
git commit -m "02: Pleiades cone query (work in progress)"
git push
```
- Read the `git status` list before `git add -A`. Nothing from `blog\`, no `.fits`, no `.pdf`, no credentials may appear. If something does, do not commit and ask Claude.
- Commit messages are in English and start with the notebook number (`02:`), or `docs:` and `shared:` for changes there.
- Undo staging of one file: `git restore --staged <file>`. Undo the last commit before the push, keeping all files: `git reset --soft HEAD~1`.

### Milestones and links from blog posts
- When a notebook is finished, mark the state with a tag, for example `git tag nb02` and then `git push origin nb02`.
- A blog post links to the notebook with the commit, not with `main`, so that the link always shows the version the post describes:
  `https://github.com/marinemoleco/astroinformatics/blob/<commit>/projects/gaia_pleiades/notebooks/<notebook>.ipynb`
  Take `<commit>` from `git log --oneline` (the 7 characters are enough). The commit must be pushed before the post is published.

### Rules
- Notebooks are saved with their outputs. Claude checks the outputs for local paths and personal data before each commit. If the repository grows beyond about 200 MB, switch to `nbstripout` and keep the figures in `figures\`.
- New ADQL files start with the number of the notebook that first uses them, for example `02_pleiades_cone_dr3.adql`. The topic README lists the queries it uses.
- Raw data (`.fits`) stay local. The notebooks download them again.
- Not set up, to be proposed first: a Zenodo DOI per release, GitHub Actions.
