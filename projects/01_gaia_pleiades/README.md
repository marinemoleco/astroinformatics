# Project 01: Gaia Pleiades

Status: in progress (literature step and notebook 1 done, notebook 2 next). Last updated: 2026-11-15.

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
- [ ] Notebook 2: Pleiades query and HDBSCAN membership
- [ ] Notebook 3: Pleiades distance and parallax zero point
- [ ] Notebook 4: isochrone age
- [ ] Repeat 2 to 4 with Gaia DR4

## Files
- `literature.md`: state of knowledge, methods, data problems, open questions
- `notebooks/01_neighborhood_hrd.ipynb`: Gaia DR3 query within 100 pc, quality cuts, HR diagram, completeness, sky map, vector point diagram, three follow-up checks (section 8)
- `figures/`: PNG output of the notebooks (prefix = notebook number)
- Shared helpers: `shared/gaia_tools.py` (cached Gaia queries, quality-cut helpers)

## Results
Notebook 1 (2026-11-15, Gaia DR3 via AIP Potsdam):
- 372,226 sources with parallax >= 10 mas and parallax_over_error >= 10; 201,458 remain after the cuts (about 60 % of the 331,312 GCNS objects: pure but incomplete). Removed in sequence: RUWE 28.4 %, G S/N 0.9 %, BP/RP S/N 20.5 %, C* 4.1 %.
- HRD: main sequence, binary sequence, giants with red clump and white dwarf sequence visible.
- Completeness: M_G > 13 falls below 90 % beyond 40.5 pc (BP S/N cut). Without a RUWE cut, M_G 5 to 13 is complete to 100 pc. RUWE depletes nearby mid-M dwarfs (failure 21 % at 15 to 30 pc vs 5 % at 75 to 100 pc, a test-power effect); RUWE < 1.2 is too strict. The rise of the bright class (M_G < 5) is a Gaia bright-limit effect.
- Spurious sources below the white dwarfs: 86.5 % at |b| < 15 deg (uniform: 26 %), mostly blends; colour cuts catch them (BP/RP 96 %, C* 90 %), RUWE 58 %.
- Hyades recovered with a window search: 285 stars vs 54 expected from the field (excess about 230), median 47.4 pc, depth 3.1 pc, narrow main sequence. The off-centre clump of section 7 was the field.
- Decisions for notebook 2: no RUWE cut for membership (flag high-RUWE stars as probable binaries), keep colour cuts for HRDs, validate against Hunt & Reffert 2023.

## Open points
- Read in full before notebook 2 and 3: Hunt & Reffert 2023 (quality cuts, HDBSCAN settings), Lindegren et al. 2021 (zero-point recipe), Riello et al. 2021 (C\* coefficients, used already in notebook 1).
- Decide whether to install `gaiadr3-zeropoint` (official zero-point implementation) for notebook 3; it would be a new package in `requirements.txt`.
- Isochrone source for notebook 4: PARSEC web interface (CMD) download vs. a Python client. To be decided.
