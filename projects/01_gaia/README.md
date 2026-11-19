# 01 Gaia (notebooks 01 to 04, then DR4 repeat)

Status: in progress (literature step, notebook 1 and sub-notebook 1.1 done). Last updated: 2026-11-19. The state of notebook 2 is not covered by this update.

Topic 01. Notebooks are numbered within this topic (01, 02, ...); figures start with the notebook number. New files in `data/` and commit messages use `01-NN` (for example `data/raw/01-02_pleiades_cone_dr3.adql`, commit `01-02: ...`). Rules: `docs/NAMING.md`.

## Question
1. What does the HR diagram of the solar neighborhood (within 100 pc) look like in Gaia DR3, and how complete is a simple, quality-cut sample?
2. Can we recover the Pleiades from Gaia DR3 astrometry alone, and reproduce the literature distance (about 136 pc) and age (about 100 to 130 Myr)?

This is a benchmark with a known answer. It validates the pipeline before genuinely open questions are tackled. The full analysis is repeated with Gaia DR4 (released 2 December 2026).

## Scientific background (who, what, why)
- **Gaia** (ESA, launched 2013) measures positions, parallaxes, proper motions and photometry for about 1.8 billion sources (DR3). DR4 adds 66 months of data and time series.
- **The Pleiades** are the reference young open cluster. Their distance was disputed for almost two decades (Hipparcos 120 pc vs. 133 to 136 pc from other methods) until VLBI radio parallaxes gave 136.2 ± 1.2 pc (Melis et al. 2014) and Gaia confirmed it.
- **Age** is the harder problem: lithium depletion boundary ages cluster around 112 to 130 Myr, isochrone ages around 100 to 125 Myr, and models with magnetic activity shift young-cluster ages upward. The absolute age scale of young clusters is still debated.
- **Membership** depends on method: compact cores (about 1000 to 1250 stars), coronae and tidal tails (about 2000 stars over > 200 pc) and the recently proposed Greater Pleiades Complex (about 3000 stars over about 600 pc).

Details, numbers and references: `literature.md`.

## Method (planned)
- Data: Gaia DR3 via ADQL (pyvo), ESA Gaia archive first, Gaia partner data centres (ARI Heidelberg, AIP Potsdam) as automatic fallback, filtered on the server. Raw query results cached in `data/raw/` with the ADQL text next to them.
- Quality cuts: parallax_over_error ≥ 10, RUWE < 1.4, photometric S/N (G > 50, BP and RP > 20), corrected BP/RP flux excess |C\*| < 3σ (Riello et al. 2021).
- Membership: HDBSCAN (scikit-learn) in proper-motion and parallax space; comparison with Hunt & Reffert (2023) and Lodieu et al. (2019).
- Distance: ensemble mean parallax with and without zero-point correction (Lindegren et al. 2021).
- Age: PARSEC (optionally MIST) isochrones with an explicit likelihood; comparison with lithium ages.

## Steps
- [x] Literature step (`literature.md`, `docs/literature/references.bib`)
- [x] Notebook 1: HR diagram within 100 pc, completeness, RUWE test, spurious sources, Hyades check (`notebooks/01_neighborhood_hrd.ipynb`), run on real data
- [x] Notebook 1.1: re-evaluation of the five open questions of notebook 1 (`notebooks/01.1_neighborhood_reevaluation.ipynb`), run on real data
- [ ] Notebook 2: Pleiades query and HDBSCAN membership
- [ ] Notebook 3: Pleiades distance and parallax zero point
- [ ] Notebook 4: isochrone age
- [ ] Repeat 2 to 4 with Gaia DR4 (as notebooks 05 ff.)

## Files
- `literature.md`: state of knowledge, methods, data problems, open questions
- `notebooks/01_neighborhood_hrd.ipynb`: Gaia DR3 query within 100 pc, quality cuts, HR diagram, completeness, sky map, vector point diagram, three follow-up checks (section 8)
- `notebooks/01.1_neighborhood_reevaluation.ipynb`: sub-notebook of 01. Each check states competing hypotheses and a prediction before the code. Uses the GCNS, Hipparcos and Hunt & Reffert (2024) as external references
- `figures/`: PNG output of the notebooks (prefix = notebook number)
- Shared helpers: `shared/gaia_tools.py` (cached Gaia queries, quality-cut helpers)

## Results
Notebook 1 (2026-11-15, Gaia DR3 via AIP Potsdam):
- 372,226 sources with parallax >= 10 mas and parallax_over_error >= 10; 201,458 remain after the cuts (about 60 % of the 331,312 GCNS objects: pure but incomplete). Removed in sequence: RUWE 28.4 %, G S/N 0.9 %, BP/RP S/N 20.5 %, C* 4.1 %.
- HRD: main sequence, binary sequence, giants with red clump and white dwarf sequence visible.
- Completeness: M_G > 13 falls below 90 % beyond 40.5 pc (BP S/N cut). Without a RUWE cut, M_G 5 to 13 is complete to 100 pc. RUWE depletes nearby mid-M dwarfs (failure 21 % at 15 to 30 pc vs 5 % at 75 to 100 pc, a test-power effect); RUWE < 1.2 is too strict. The rise of the bright class (M_G < 5) was first attributed to the Gaia bright limit; sub-notebook 1.1 shows that this is only half of the explanation (see below).
- Spurious sources below the white dwarfs: 86.5 % at |b| < 15 deg (uniform: 26 %), mostly blends; colour cuts catch them (BP/RP 96 %, C* 90 %), RUWE 58 %.
- Hyades recovered with a window search: 285 stars vs 54 expected from the field (excess about 230), median 47.4 pc, depth 3.1 pc, narrow main sequence. The off-centre clump of section 7 was the field.
- Decisions for notebook 2: no RUWE cut for membership (flag high-RUWE stars as probable binaries), keep colour cuts for HRDs, validate against Hunt & Reffert 2023.

Sub-notebook 1.1 (2026-11-19, re-evaluation of the five open questions; GAVO Data Center, AIP Potsdam and VizieR as sources, see Data sources):
- Q1, rise of the bright class (M_G < 5): without any cut the curve is 1.15 at 50 pc and 1.12 at 90 pc (bootstrap interval 1.01 to 1.24, only 408 stars at 20 to 30 pc). Missing nearby bright stars (Gaia bright limit) explain this part; the corrected curve is 1.04 at 50 pc and 0.99 at 90 pc. The further rise to 1.21 (notebook 01) and 1.32 (clean sample) comes from the quality cuts, which remove more stars in the reference zone. The Hyades add about 0.03 at 50 pc; both sky hemispheres rise, so a density gradient is excluded. 607 Hipparcos stars with Hp 8 to 13 have no Gaia match in our download (untested guess: in Gaia but not in the download).
- Q2, Hyades window search: purity 0.83 (GCNS list), 0.85 (Hunt & Reffert 2024), 0.76 (their core); the ring estimate of 0.81 was right. Recall is 26 % of all GCNS Hyades members and 56 % of the core; the main losses are the RUWE cut and the fixed proper-motion circle (perspective). The 48 stars found only by us behave like field stars (54 % on the Hyades sequence, 15 % radial-velocity agreement), so the literature lists are right. Five of the 48 are white dwarfs (open observation).
- Q3, comparison with the GCNS: without cuts our download equals the GCNS for M_G < 13. Of 71,240 sources not in the GCNS, 70,150 have M_G > 13, 96 % lie in the Galactic plane and 99.5 % fail the photometric cuts. The clean sample keeps 66.7 % of the GCNS volume (by class: 72 %, 69 %, 80 %, 28 %). The "about 60 %" above divided by all GCNS objects. The hard cuts reject spurious solutions like the GCNS classifier but cost a third of the real stars: for counting use the GCNS.
- Q4, RUWE peak at M_G 5 to 10 and 30 to 50 pc: the peak is real. Hyades, resolved companions, double-peak sources, colour cuts and sky position are refuted as causes. It is an apparent-magnitude effect: stars at G of about 11 to 13 fail RUWE about twice as often. Peak distances 29, 43 and 62 pc for the slices M_G 9-10, 8-9 and 7-8; slope of the distance modulus -0.82 (three slices, restricted after the run, as documented in the notebook; -0.40 with four slices). Open: real binary detection versus single stars crossing the threshold more easily. Sky position shifts the overall failure rate by up to 4 points (Castro-Ginard et al. 2024).
- Q5, visibility periods: more observations do not cause more RUWE failures. The raw difference is mostly negative and vanishes inside bands of ecliptic latitude for M_G 5 to 10 (sky position). A negative remainder stays for M_G < 5 and for the faintest stars, cause open.
- Predictions that failed or held only in part: bright-class cause (Q1, cuts not foreseen), parallax_over_error loss for M_G > 13 (Q3, 2.6 % instead of a large share), double-peak sources as cause of the peak (Q4), sign of the raw visibility effect (Q5).
- Consequences for notebook 2: membership from Hunt & Reffert 2024, no RUWE cut before selecting members; a fixed RUWE cut removes different fractions depending on apparent magnitude and sky region.

## Data sources (sub-notebook 1.1)
Queries and services are recorded in `data/raw/01-01.1_*.adql` (the service that answered and the date are in the file header, retrieved 2026-11-18).
- GAVO Data Center, Heidelberg (https://dc.g-vo.org/tap): GCNS tables `gcns.main`, `gcns.hyacob`, `gcns.resolvedss`, `gcns.missing_10mas` and `hipparcos.main`.
- AIP Potsdam (Gaia partner data centre): `gaiadr3.hipparcos2_best_neighbour` joined with `gaiadr3.gaia_source`. This table has 99,524 rows for 117,955 Hipparcos stars, so it cannot show which stars Gaia lacks; the notebook adds a position search.
- VizieR (via astroquery): Hunt & Reffert 2024, `J/A+A/686/A42/members`, cluster Melotte 25 (Hyades), 927 stars.
- Gaia DR3 100 pc download of notebook 01, reused.

## Open points
- Read in full before notebook 2 and 3: Hunt & Reffert 2023 (quality cuts, HDBSCAN settings), Lindegren et al. 2021 (zero-point recipe), Riello et al. 2021 (C\* coefficients, used already in notebook 1).
- Decide whether to install `gaiadr3-zeropoint` (official zero-point implementation) for notebook 3; it would be a new package in `requirements.txt`.
- Isochrone source for notebook 4: PARSEC web interface (CMD) download vs. a Python client. To be decided.
