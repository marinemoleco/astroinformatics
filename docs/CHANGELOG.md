# Changelog

Newest entries on top. One entry per working session: what was done, what was decided, what changed in the setup.

## 2026-11-16: 01 Gaia, Neighbourhood, Blog Part 1 (renamed after the new scheme)
- Blog adapted to `docs\NAMING.md`: titles "About me and this project" and "Gaia Part 1: The neighbourhood", post folders `posts\about` and `posts\gaia-part-1-neighbourhood` (URLs without numbers), navbar link "About" updated, `index.qmd` sorts by `[date, title]` (About is listed before Gaia Part 1). `posts\_template` and `blog\README.md` ("Writing a post") follow the new scheme.
- Gaia Part 1: the Reproduce box links notebook 01 at the fixed commit 28f2881 with the path `projects/01_gaia/...`. The text and figures are unchanged. The post had been uploaded earlier today under the old URLs (`.deploy_manifest.json`).
- `blog\about.qmd` (superseded, not built, referenced nowhere) is to be deleted, as are the old post folders `posts\00-introduction` and `posts\01-gaia-neighbourhood` (Claude has no shell on the PC). A test render in Claude's workspace ran without errors; render, preview and upload are done by hand.
- `deploy.py` never deletes on the server: the old folders `posts/00-introduction` and `posts/01-gaia-neighbourhood` and the file `about.html` have to be removed there by FTP.

## 2026-11-16: 00 Naming and numbering (topic-based scheme)
- Replaced the consecutive notebook numbering across topics (decided the same morning) by a topic-based scheme. New single source of rules: `docs\NAMING.md`.
- Topics carry a number `TT` (assigned at start; `00` = setup and planning). Notebooks count within their topic (`NN`). Inside the topic folder `NN` is enough (notebook files, figures); where all topics meet, `TT-NN` is used (new files in `data\`, commit messages, tags, chat names).
- Topic folder becomes `projects\01_gaia` (rename with `git mv` in the GitHub chat). Notebook 01 and its figures keep their names. TESS starts at notebook 01 of its own topic, not at 05. The DR4 repeat continues as notebooks 05 ff. of topic 01.
- Chat names: "TT Topic, Short description, Notebook N" and "TT Topic, Short description, Blog Part K".
- Blog: titles and post URLs without numbers ("About me and this project", "Gaia Part 1: The neighbourhood"), list sorted by date, then title (Quarto sorts alphabetically by title otherwise). Done in the blog chat.
- Updated: `README.md`, `docs\RUNBOOK.md` (sections 2, 8, 9, 10), topic `README.md`, `literature.md` title, `D:\Astronomie\backup\README.md`, Claude project docs. Not yet done: folder rename and path in notebook 01 (GitHub chat), blog (blog chat).
- Done in the GitHub chat: folder renamed with `git mv projects\gaia_pleiades projects\01_gaia`, the code line in notebook 01 changed from `config.project_dir("gaia_pleiades")` to `config.project_dir("01_gaia")` (the stored output of its first run keeps the old path), and the finished notebook 1 is tagged `01-01`.

## 2026-11-16: GitHub repository and documentation workflow
- Public repository `marinemoleco/astroinformatics` created and pushed (first commit 007ce59, 22 files, page checked in the browser). One repository for all projects, each analysis a folder under `projects\`.
- Decisions: the blog stays local and is not published on GitHub. In the repository: `projects`, `docs` (only `references.bib`, never the literature PDFs), `shared`, `requirements.txt`, the ADQL files in `data\raw`, README and licences. Raw and processed data stay local. Notebooks are stored with their outputs (2 MB for notebook 1); reconsider `nbstripout` beyond about 200 MB. Commit e-mail: the iba-science.de address. Licences: MIT for code, CC BY 4.0 for texts and figures (notice with link to the legal text, not the full text).
- New: `.gitignore`, `LICENSE`, `LICENSE-CC-BY-4.0.md`, public `README.md`; `environment.yml` deleted (unused). Checked beforehand for addresses, credentials and user paths in all files and in the notebook outputs: nothing found.
- Workflow for every session defined in RUNBOOK section 10: CHANGELOG entry, one commit per session with the project number, tags for finished notebooks, blog links to notebooks with a fixed commit.
- Numbering decided (same day): notebooks are numbered consecutively across all topics (01, 02, ...). The number is used in the notebook name, figure names, new ADQL file names, commit messages (`02: ...`), tags (`nb02`) and chat names. Topic folders carry no number, so `projects\01_gaia_pleiades` became `projects\gaia_pleiades` (renamed with `git mv`). Notebook 01 now calls `config.project_dir("gaia_pleiades")`; its stored output of the first run still shows the old path. Earlier entries below keep the old folder name.
- Not set up on purpose: Zenodo DOI per release, GitHub Actions (to be proposed first).
- Next: notebook 02 (Pleiades cone query, HDBSCAN). Download the Pleiades data soon, the Gaia archive has a downtime before DR4 (2 December 2026).

## 2026-11-15: 01 Gaia Pleiades, first real run of notebook 1 and section 8
- Notebook 1 ran on real data (via AIP Potsdam, ESA still unreachable): 372,226 sources downloaded, 201,458 kept. Removed in sequence: RUWE 28.4 %, G S/N 0.9 %, BP/RP S/N 20.5 %, C* 4.1 %. About 60 % of the 331,312 GCNS objects (Smart et al. 2021) remain: a pure but incomplete sample.
- Section 8 added and run: 8.1 RUWE thresholds and completeness (RUWE depletes nearby mid-M dwarfs; bright-class rise is a Gaia bright-limit effect; RUWE < 1.2 too strict), 8.2 spurious sources (blends in the Galactic plane, caught mainly by colour cuts), 8.3 Hyades recovered (excess about 230 stars, 47.4 pc, narrow main sequence). Section 7 clump was the field. Two of my predictions were wrong (bright-class cause, which cut catches blends); both are documented in the notebook and README.
- Decisions for notebook 2: no RUWE cut for the membership search (flag instead), keep colour cuts for HRDs, validate HDBSCAN against Hunt & Reffert 2023.
- Fixed mirrored longitude labels in the 8.2 sky maps (needs a re-run of that cell). Old section 8 is now section 9 (summary, filled in).
- New working standard in project doc 00: every step explained with what, why, cost, analogy, what to look for, and an exercise.
- Glossary: added ascertainment bias, blend, purity versus completeness, test power.
- Note: README, CHANGELOG and GLOSSARY on H: had been reset to an earlier state after my first update; re-applied.
- Next: notebook 2 (Pleiades cone query, HDBSCAN). Download the Pleiades data soon: Gaia archive downtime expected before DR4 (2 December 2026).

## 2026-11-15: 01 Gaia Pleiades, literature step and notebook 1
- Literature step done: `projects\01_gaia_pleiades\literature.md` (data problems of Gaia DR3, Pleiades distance, membership methods, age methods and values, open questions, plan). 36 references (DOI, arXiv ID or ADS bibcode) in the new shared `docs\literature\references.bib` (Zotero import).
- Decisions: project 01 runs on Gaia DR3 now and is repeated with DR4 (2 December 2026). Notebook 1 is the 100 pc HR diagram, the Pleiades follow in notebooks 2 to 4. Quality cuts: parallax_over_error >= 10, RUWE < 1.4, G S/N > 50, BP/RP S/N > 20, corrected flux excess |C*| < 3 sigma.
- New: `projects\01_gaia_pleiades\README.md`, `notebooks\01_neighborhood_hrd.ipynb` (written, tested by Claude on synthetic data only, not yet run on real data), `shared\gaia_tools.py` (cached Gaia queries with the ADQL text saved next to the data, C* and absolute-magnitude helpers), `docs\GLOSSARY.md` (first 30 terms with population-genetics analogies).
- No new packages. Possibly next: `gaiadr3-zeropoint` for notebook 3 (to be decided).
- First local run: ESA Gaia archive not reachable (connection timeout, also in the browser). `shared\gaia_tools.py` now uses pyvo and falls back to the Gaia partner data centres ARI Heidelberg and AIP Potsdam; the `.adql` file records which service answered. Fallback logic tested by Claude with a mock server only.
- Next: run notebook 1 locally, send the cut table, completeness table, clump line and four figures. Then notebook 2 (Pleiades membership with HDBSCAN).

## 2026-11-15: Project setup
- Decisions: all computation local, working language English, data on H: (1.26 TB free), environment and backups on D: (about 60 GB free).
- Folder structure created on H:\Astronomie and D:\Astronomie. `shared/config.py` holds the base path.
- Conda is not installed. Virtual environment `astro` created with venv at `D:\Astronomie\envs\astro` from `requirements.txt` (system Python 3.10.6).
- Packages installed: see runbook section 3. Kernel "Astro (Python)" registered.
- Smoke test passed (imports of astropy, astroquery, lightkurve, scikit-learn). Harmless lightkurve warning about `tpfmodel`.
- Documentation set up: `docs\RUNBOOK.md`, `docs\CHANGELOG.md`.
- Next: chat "01 Gaia Pleiades", starting with a literature step.
