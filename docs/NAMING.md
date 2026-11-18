# Naming and numbering

Decided 2026-11-16, sub-notebooks added 2026-11-18. This file is the single source for all naming rules. Other documents refer to it. This is the master copy; a mirror is kept in the Claude project "Astroinformatics" as `claude/NAMING.md`.

## Principle

Work is organised in topics. Each topic has a two-digit number `TT` and each notebook a two-digit number `NN` that counts within its topic (01, 02, 03, ...). The number of the topic is assigned when the topic starts, in the order in which topics are started. `00` is reserved for setup, infrastructure and planning.

Rule of thumb: inside a topic folder `NN` is enough, because the folder already says which topic it is. Wherever all topics come together (shared folders, git history, chat list), the full form `TT-NN` is used.

## Topics

| TT | Topic | Folder | Status |
|----|-------|--------|--------|
| 00 | Setup, infrastructure, planning | (none) | ongoing |
| 01 | Gaia | `projects/01_gaia` | in progress |
| next | TESS transit | `projects/TT_tess` when started | planned |
| later | Galaxies | assigned at start | planned |
| later | Visual | assigned at start | planned |

Planned topics get their number only when they start. A topic stays open as long as the question continues; the repeat of notebooks 02 to 04 with Gaia DR4 runs as further notebooks of topic 01 (05, 06, ...). A new question with new data or a new method family is a new topic.

## Inside a topic folder: `NN`

```
projects/
  01_gaia/
    README.md, literature.md
    notebooks/
      01_neighborhood_hrd.ipynb
      01.1_neighborhood_reevaluation.ipynb
      02_pleiades_membership.ipynb
    figures/
      01_hrd_100pc.png
      01.1_gcns_comparison.png
      02_pleiades_vpd.png
  02_tess/                        (example, not yet created)
    notebooks/
      01_transit_fit.ipynb        same "01" as in Gaia, but another folder: no conflict
```

- Topic folder: `projects/TT_shortname` (lower case, underscore).
- Notebook: `NN_short_name.ipynb`.
- Figures: `figures/NN_short_name.png`, `NN` = notebook that makes the figure.

## Sub-notebooks: `NN.n` (added 2026-11-18)

A sub-notebook follows up a finished notebook `NN`: open questions, checks, validation against reference data or an alternative approach to the same question. It gets the number of its parent plus `.n`, counted from 1: `01.1`, `01.2`, ... A new question or a new main step is a new `NN`, not a sub-notebook.

| What | Rule | Example |
|------|------|---------|
| Notebook | `NN.n_short_name.ipynb` | `notebooks/01.1_neighborhood_reevaluation.ipynb` |
| Figures | `figures/NN.n_short_name.png` | `figures/01.1_gcns_comparison.png` |
| Data files | `TT-NN.n_short_name.*` | `data/raw/01-01.1_gcns_100pc.adql` |
| Commit message | `TT-NN.n: text` | `01-01.1: GCNS comparison` |
| Tag | `TT-NN.n` | `git tag 01-01.1` |
| Claude chat | `TT Topic, Short description, Notebook NN.n` | `01 Gaia, Neighbourhood re-evaluation, Notebook 1.1` |

Note: in some file browsers `01.1_...` sorts before `01_...` (the dot sorts before the underscore). This is harmless; the number itself keeps the relation clear.

## Where all topics meet: `TT-NN`

| What | Rule | Example |
|------|------|---------|
| New ADQL and data files in `data/raw/` and `data/processed/` | `TT-NN_short_name.*` | `data/raw/01-02_pleiades_cone_dr3.adql` |
| Commit message | `TT-NN: text`, or `docs:`, `shared:` | `01-02: Pleiades cone query` |
| Tag when a notebook is finished | `TT-NN` | `git tag 01-02` |
| Claude chat for a notebook | `TT Topic, Short description, Notebook N` | `01 Gaia, Pleiades query and HDBSCAN, Notebook 2` |
| Claude chat for a blog post | `TT Topic, Short description, Blog Part K` | `01 Gaia, Neighbourhood, Blog Part 1` |
| Claude chat for setup and planning | `00 Subject` | `00 GitHub-Setup Hobby Astronomy` |

Files that existed before this rule keep their names (`data/raw/gaia_dr3_100pc_plx10_poe10.*`, `data/processed/gaia_dr3_100pc_clean.fits`).

## Blog

- Titles carry no numbers. The about page is `About me and this project`. Posts of a topic are counted as parts: `Topic Part K: Title`, for example `Gaia Part 1: The neighbourhood`, `Gaia Part 2: The Pleiades`. A part can cover several notebooks, including sub-notebooks.
- Post folders (and thus URLs) carry no numbers either: `posts/about/`, `posts/gaia-part-1-neighbourhood/`, `posts/gaia-part-2-pleiades/`.
- The post list is sorted by publication date, then title (`sort: [date, title]` in `blog/index.qmd`), because Quarto otherwise sorts alphabetically by title.
- A post links to the notebook with a fixed commit:
  `https://github.com/marinemoleco/astroinformatics/blob/<commit>/projects/01_gaia/notebooks/01_neighborhood_hrd.ipynb`

## Current chats (state 2026-11-18)

- 00 Astronomie-Hobby mit öffentlichen Daten
- 00 Blog-Plan für Webspace-Dokumentation
- 00 GitHub-Setup Hobby Astronomy
- 00 Naming and numbering
- 01 Gaia, Neighbourhood, Notebook 1
- 01 Gaia, Neighbourhood, Blog Part 1
- 01 Gaia, Pleiades query and HDBSCAN, Notebook 2
- 01 Gaia, Neighbourhood re-evaluation, Notebook 1.1

## History

- 2026-11-15: folder `projects/01_gaia_pleiades`, notebooks numbered within the project.
- 2026-11-16 (morning): notebooks numbered consecutively across all topics, folder renamed to `projects/gaia_pleiades`.
- 2026-11-16 (evening): this scheme. Folder renamed to `projects/01_gaia`, notebooks count within the topic, `TT-NN` outside the topic folder, blog titles and URLs without numbers.
- 2026-11-18: sub-notebooks `NN.n` for follow-up checks and alternative approaches to a finished notebook.
