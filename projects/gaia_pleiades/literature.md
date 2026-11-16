# 01 Gaia Pleiades: literature step

Last updated: 2026-11-15. Written before any code (phase 0). BibTeX keys refer to `docs/literature/references.bib`.

Reading limits: most entries below were read as abstracts, arXiv listing pages or open-access excerpts. Items marked **[check]** are decisive for our method and should be read in full by the user. Items marked **[secondhand]** were taken from another paper's summary, not from the original.

## 1. Question and why the Pleiades

The Pleiades (M45, Melotte 22) are the classic benchmark open cluster: young (about 100 to 130 Myr), nearby (about 135 pc), rich (over a thousand known members) and lightly reddened. This topic uses them as a test with a known answer. If our pipeline (Gaia query, quality cuts, membership, distance, age) reproduces the literature values, it can be trusted for genuinely open questions later. The first notebook does not touch the Pleiades yet: it builds the HR diagram of the solar neighborhood within 100 pc, which trains the same steps on a simpler sample.

## 2. Data: Gaia DR3 and its known problems

**Content.** Gaia DR3 is based on 34 months of data. Positions, parallaxes, proper motions and G, BP, RP photometry are identical to EDR3; DR3 added radial velocities for more than 33 million stars, astrophysical parameters, variability and non-single-star solutions (`Vallenari2023`).

**Photometry.** Median G uncertainty is 0.2 mmag at G = 10 to 14, 0.8 mmag at G about 17 and 2.6 mmag at G about 19. BP and RP fluxes can be contaminated in crowded fields or for faint sources; the paper defines a *corrected flux excess factor* C\* to flag this (`Riello2021`) **[check: coefficients of C\* and its scatter, used in notebook 1]**.

**Parallax zero point.** EDR3/DR3 parallaxes are biased: quasars show a median parallax of about −17 µas instead of zero, and the bias depends on magnitude, colour and ecliptic latitude. Lindegren et al. give tentative correction formulas, to be used at the researcher's discretion (`Lindegren2021zp`) **[check]**. Cluster-based studies find small residuals for G > 13 but larger ones for bright, blue stars, and propose refinements (`MaizApellaniz2021`). Relevance: at the Pleiades (parallax about 7.4 mas) a 0.02 to 0.04 mas offset shifts the distance by roughly 0.4 to 0.8 pc, comparable to the statistical error of the cluster mean. At 100 pc (parallax ≥ 10 mas) it is negligible for an HR diagram.

**RUWE and binaries.** RUWE (renormalised unit weight error) is about 1 for well-behaved single-star solutions. RUWE > 1.4 is the common threshold for problematic solutions and a strong binary indicator; for DR3 a stricter 1.25 has also been proposed (`ElBadry2025ruwe` summarising Lindegren 2018 and Penoyre et al. 2022). In the 100 pc catalogue, 17 % of sources have RUWE > 1.4. Caveat: cutting on RUWE removes many unresolved binaries, which changes the cluster sequence and the binary fraction we can measure.

**Distances.** Inverting a parallax is only safe when the fractional error is small; for poor parallaxes a probabilistic distance with a Galactic prior is better. Bailer-Jones et al. provide geometric and photogeometric distances for 1.47 billion EDR3 sources (`BailerJones2021`). For our cuts (parallax_over_error ≥ 10) simple inversion is acceptable; for the Pleiades the cluster distance should be inferred from the ensemble, not from individual inverted parallaxes.

**100 pc reference sample.** The Gaia Catalogue of Nearby Stars (GCNS) contains 331 312 objects and is estimated to include at least 92 % of stars of spectral type M9 or earlier within 100 pc; about 9 % probably lie beyond 100 pc (`Smart2021`). This is the reference against which notebook 1 can check completeness.

**HR diagram reference.** Gaia Collaboration (Babusiaux et al. 2018) is the showcase of Gaia HR diagrams: field and cluster samples, the split of the white dwarf sequence into hydrogen and helium white dwarfs, and membership lists for nearby clusters including the Pleiades (`Babusiaux2018`).

**Gaia DR4.** Planned for 2 December 2026, based on 66 months of data, with time series for all sources and about 2.8 billion sources (ESA Gaia pages, see Sources). Expected precision gain over DR3: about √2 for parallaxes and about 2√2 for proper motions (`Brown2025`). Consequences for us: a new parallax zero-point calibration will be needed (do not reuse the DR3 formulas on DR4), epoch astrometry will allow better binary handling, and internal cluster kinematics become measurable for more stars. Plan: run project 01 on DR3 now and repeat it on DR4.

## 3. Pleiades distance: a solved controversy, useful as a check

Hipparcos gave 120.2 ± 1.5 pc, in conflict with 133.5 ± 1.2 pc from other methods. VLBI radio parallaxes of Pleiades stars gave 136.2 ± 1.2 pc and ruled out the Hipparcos value (`Melis2014`). Gaia data releases confirmed the longer distance (summarised in `Heyl2021`). Our DR3 mean parallax, with and without zero-point correction, should land near the VLBI value. A clear deviation would point to a problem in our membership or our zero-point handling.

## 4. Membership: how clusters are separated from the field

| Approach | Example | Notes |
|---|---|---|
| Kinematic + statistical parallax/proper-motion selection | `Lodieu2019`: 1248 Pleiades members inside the tidal radius (Gaia DR2); stream around the Pleiades out to 40 pc | Classic, transparent |
| Unsupervised membership (UPMASK) + neural-network ages | `CantatGaudin2020`: parameters for 1867 clusters | Basis of many age catalogues |
| HDBSCAN on astrometry, all-sky | `HuntReffert2023`: 7167 clusters from 729 million DR3 sources; membership lists often include tidal tails **[check: quality cuts and HDBSCAN settings]** | Current standard; HDBSCAN is in our scikit-learn |
| DBSCAN + Bayesian proper-motion model | `Alfonso2023`: Pleiades, Praesepe, Blanco 1 with DR3 | Close to what we will do |
| Bound vs unbound via Jacobi radius | `HuntReffert2024`: only 79 % of catalogue clusters compatible with bound clusters, 11 % within 250 pc | Tells us where the "cluster" ends |
| Coronae | `Meingast2021`: coeval, comoving coronae extending ≳ 100 pc around 10 nearby clusters; the coronae are unbound but hold most of the stellar mass | Membership depends strongly on the method |
| Tidal tails | `Risbud2025`: 2029 stars associated with the Pleiades and its tails, tip-to-tip extent > 200 pc | Convergent-point method |
| Rotation + kinematics | `Boyle2025`: Greater Pleiades Complex, 3091 stars, bound core of a coeval structure spread over about 600 pc | Uses TESS rotation as an age tag |

The Hyades (about 47 pc, inside the 100 pc sample of notebook 1) were the first open cluster with detected tidal tails, found independently in Gaia DR2 (`Roeser2019`, `MeingastAlves2019`).

Takeaway: "membership" is not unique. A compact core sample is right for the age and distance benchmark; extended structures are a separate (and open) question. The sizes of member lists differ by a factor of two to three between methods.

## 5. Age: methods and the current values

| Method | Pleiades age | Source |
|---|---|---|
| Lithium depletion boundary (LDB), Keck spectra | 125 to 130 Myr | `Stauffer1998` |
| LDB, model sensitivity study | 148 ± 19 Myr (base case), 126 ± 11 Myr with a bolometric-correction shift | `Burke2004` |
| LDB, near-infrared, revised | 112 ± 5 Myr; about 100 Myr if magnetic activity is accounted for | `Dahm2015` |
| LDB, homogeneous re-analysis with Gaia DR2 | 118 (+6/−10) Myr **[secondhand, via `Jeffries2023`]** | `GalindoGuil2022` |
| Empirical lithium isochrones (EAGLES) | 93 (+9/−10) Myr from literature data | `Jeffries2023` |
| Empirical lithium isochrones, LAMOST spectra | 118 ± 6 Myr | `Frasca2025` |
| Bayesian hierarchical lithium model (preprint, 2026) | 124.5 (+3.3/−2.7) Myr | `GonzalezRamirez2026` |
| Isochrone fitting (literature compilation) | centred on 100 to 125 Myr | `Brandner2023` |
| White dwarf cooling | firm lower limit 60 Myr | `Heyl2021` |

**Isochrone fitting** compares the observed colour-magnitude diagram to model isochrones (PARSEC: `Bressan2012`; MIST). Bayesian tools such as BASE-9 fit age, distance modulus, extinction and metallicity together (`Bossini2019`, 269 clusters). Known problem: model isochrones do not match the observed Gaia colours of low-mass stars; empirical colour corrections derived from Hyades, Pleiades and Praesepe bring isochrone ages into agreement with LDB ages (`Wang2024`).

**Magnetic activity and starspots.** Young low-mass stars are inflated and redder than standard models predict. Magnetic or starspot models give CMD ages about 1.5 to 2 times older for young low-mass stars and fit lithium depletion better (`Binks2022`, `Franciosini2022`, `Binks2021`). This is the main reason why isochrone and lithium ages of young clusters disagree.

**Expectation for our project.** A fit of standard isochrones to the upper and middle main sequence should give roughly 100 to 130 Myr. If we fit the full sequence including M dwarfs with standard models, we should expect a biased age and visible colour residuals at the red end. That is a feature to demonstrate, not a bug to hide.

## 6. Genuinely open questions (candidates for later projects)

1. **Absolute age scale of young clusters.** LDB, lithium-pattern and isochrone ages still differ by 10 to 20 % or more; the size of the magnetic correction is not settled. Literature isochrone ages for the Pleiades still span about 80 to 140 Myr (`Frasca2025`).
2. **Where does a cluster end?** Core, corona, tidal tails and the Greater Pleiades Complex are partly overlapping descriptions. Reliability of published tail catalogues is debated (`Jadhav2025`), and some tails point away from the Galactic centre, contrary to standard tidal-tail theory (`Risbud2025`).
3. **Low-mass isochrone colours.** The colour mismatch is corrected empirically, not understood physically (`Wang2024`).
4. **What DR4 changes.** Better proper motions make internal kinematics (expansion, rotation, mass segregation) and faint tail members accessible; epoch astrometry helps with binaries. A DR3 vs DR4 comparison on the same pipeline is a natural follow-up.

## 7. Plan derived from the literature

1. **Notebook 1 (this session):** HR diagram within 100 pc from Gaia DR3 with documented quality cuts (parallax_over_error ≥ 10, RUWE < 1.4, photometric S/N, corrected flux excess C\*). Completeness check N(<d) ∝ d³. Compare visually with `Babusiaux2018` and `Smart2021`.
2. **Notebook 2:** Pleiades cone query (server-side ADQL filter), HDBSCAN membership in (proper motion, parallax) space, comparison with `HuntReffert2023` and `Lodieu2019` member lists from VizieR.
3. **Notebook 3:** Cluster distance from the ensemble parallax, with and without zero-point correction (`Lindegren2021zp`), compared with 136.2 ± 1.2 pc (`Melis2014`).
4. **Notebook 4:** Isochrone age (PARSEC, optionally MIST) with an explicit likelihood; compare with the LDB values in Section 5; show the low-mass colour residuals.
5. **After 2 December 2026:** repeat notebooks 2 to 4 with DR4.

## Sources

Gaia mission pages (DR4 date and content): [Gaia Data Release scenario](https://www.cosmos.esa.int/web/gaia/release), [Gaia Bulletin archive](https://www.cosmos.esa.int/en/web/gaia/bulletin-archive). All other references (DOI, arXiv ID or ADS bibcode) in `docs/literature/references.bib`.
