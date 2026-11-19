# Glossary

Created 2026-11-15 (notebook 01), extended 2026-11-19 (notebook 01.1). Terms in alphabetical order. Where it helps, an analogy to population genetics is given in *italics*. Analogies are aids for intuition, not exact equivalences.

**Ascertainment (selection) bias.** Distortion of a sample because the selection rule favours some objects over others. Every quality cut has one: the RUWE cut removes binaries, the BP S/N cut removes very red faint stars. *Same issue as choosing SNPs on a chip designed in one population.*

**Absolute magnitude (M_G).** The magnitude a star would have at 10 pc. From apparent magnitude G and parallax ϖ in mas: M_G = G + 5 log10(ϖ) − 10 (no extinction). Lets stars at different distances be compared. *Like normalising read counts by library size before comparing samples.*

**ADQL / TAP.** Astronomical Data Query Language (SQL dialect with sky functions) and Table Access Protocol (the web service that runs it). Used to filter Gaia on the server so only the needed rows are downloaded. *Like querying a sequence database with filters instead of downloading the whole database.*

**Apparent magnitude.** Logarithmic brightness as seen from Earth; larger numbers are fainter. A difference of 5 magnitudes is a factor of 100 in flux.

**Blend (spurious solution).** A source whose measurement is contaminated by a neighbour, giving a wrong parallax, colour or flux. Typical in crowded fields (Galactic plane). Precision is not accuracy: such sources can have a tiny formal error. *Like reads from a repeat region mapped to the wrong place with high mapping quality.*

**Bright limit (Gaia).** The very brightest stars saturate Gaia's detectors, so their measurements are poorer or missing and some nearby bright stars are absent from the catalogue. The effect distorts completeness curves of bright classes, but it is not the only cause of a rise (quality cuts add to it, notebook 01.1). *Like a detector saturating on the most abundant taxon.*

**BP, RP, G.** Gaia's three broad photometric bands: G (white light), BP (blue photometer), RP (red photometer).

**BP−RP (colour index).** Difference of BP and RP magnitudes. Small or negative: hot, blue star. Large: cool, red star. Proxy for surface temperature.

**Colour-magnitude diagram (CMD) / Hertzsprung-Russell diagram (HRD).** Plot of absolute magnitude against colour. Stars fall on distinct sequences (main sequence, giants, white dwarfs) that reflect their evolutionary state. Strictly, an HRD uses luminosity and temperature; with Gaia data the CMD is called an "observational HRD". *Like a PCA plot in which populations separate along axes that reflect underlying biology.*

**Completeness.** Fraction of real objects in a volume that are actually in the sample. Faint stars drop out first at larger distances. *Like detection limits in amplicon sequencing: rare taxa vanish as depth decreases.*

**Corona (of a cluster).** Extended, unbound but co-moving and coeval halo of stars around a compact cluster core, reaching ≳ 100 pc.

**Corrected flux excess factor (C\*).** Gaia quality metric comparing BP+RP flux to G flux, corrected for colour. Large |C\*| signals contaminated BP/RP photometry (blends, crowding, faint sources). *Like a chimera or contamination flag in sequencing QC.*

**Cross-match table gap.** A cross-match table between two catalogues (for example `hipparcos2_best_neighbour`) can lack entries for real stars. Absence from the table does not mean absence from the other catalogue; a position search closes the gap. *Like a mapping table that lists only part of the reads that actually map.*

**Double peak (ipd_frac_multi_peak).** Gaia column giving the share of observations in which the image fit found more than one peak. High values point to a resolved or nearly resolved companion.

**Ecliptic latitude.** Angle of a position above or below the plane of Earth's orbit. Gaia's scanning pattern gives a number of visits per star that depends mainly on it, which is why it serves as a control variable for sky position.

**Extinction / reddening.** Dimming (extinction, A_G) and colour shift (reddening, E(BP−RP)) caused by interstellar dust. Negligible within about 100 pc of the Sun (we sit in a dust-poor region, the Local Bubble), small but patchy toward the Pleiades.

**GCNS (Gaia Catalogue of Nearby Stars).** Catalogue of stars within about 100 pc built from Gaia with a classifier instead of hard cuts. In notebook 01.1 it is the reference for counting stars: it keeps real stars that our hard cuts reject.

**Hipparcos.** ESA astrometry satellite predating Gaia. Its bright stars serve as an external check of what Gaia lacks. *Like an older reference collection used to test a new survey.*

**Isochrone.** Model curve in the CMD showing where stars of all masses lie at one fixed age and composition. Fitting isochrones to a cluster CMD gives its age. *Like fitting the expected site-frequency spectrum under a demographic model with a given divergence time.*

**Jacobi (tidal) radius.** Radius within which a cluster's own gravity dominates over the Galactic tidal field. Stars outside it are not bound. *Like the boundary of a breeding population beyond which individuals effectively belong to another deme.*

**Lithium depletion boundary (LDB).** In a young cluster, low-mass stars burn their lithium once their cores get hot enough; the faintest stars still keep it. The luminosity of that sharp transition moves with age and is one of the least model-dependent age indicators for clusters of about 20 to 200 Myr. *Like a molecular clock calibrated by a well-dated fixation event.*

**Main sequence.** The band in the CMD where stars burn hydrogen in their cores; most stars spend most of their lives here.

**mas, µas.** Milliarcsecond (1/3 600 000 of a degree) and microarcsecond (1/1000 mas). Gaia parallaxes and their errors are given in mas.

**Marginally resolved pair.** Binary whose two stars lie close to Gaia's resolution limit, so the image is neither one star nor two cleanly separated ones. The astrometric fit can then be disturbed and RUWE becomes high. This is a second binary regime besides the wobble of the photocentre of closer pairs.

**Membership (cluster membership).** Assignment of stars to a cluster versus the field, usually probabilistic, based on clustering in position, proper motion and parallax. *Directly analogous to population assignment (STRUCTURE, ADMIXTURE, DAPC): membership probabilities are like ancestry proportions.*

**Moving group / association.** Group of stars with common motion and often common age that is not (or no longer) gravitationally bound. *Like a dispersed population that still shares ancestry after migration.*

**Open cluster.** Gravitationally bound group of tens to thousands of stars born together from one gas cloud, hence same age and composition. *A single-cohort founder population: same "birth date", same "genetic background".*

**Purity versus completeness.** Strict cuts give a clean but incomplete sample, loose cuts a complete but contaminated one. No setting wins both. *Precision against recall, as in variant calling.* For a member list, purity is the share of listed stars that are true members and recall the share of true members that were found (notebook 01.1, question 2).

**Perspective effect (in proper motion).** Cluster members share one space velocity, but their proper motions differ with distance and position on the sky, so a fixed proper-motion circle cuts off real members. Stronger for nearby clusters like the Hyades.

**Parallax (ϖ).** Apparent annual shift of a star's position caused by Earth's orbit. Distance in parsec = 1000 / ϖ[mas] when the parallax is precise. The ratio ϖ/σ_ϖ (parallax_over_error) measures how reliable that inversion is.

**Parallax zero point.** Systematic offset of Gaia parallaxes (a few tens of µas in DR3), depending on magnitude, colour and sky position, estimated from quasars whose true parallax is zero. *A batch effect calibrated with blank controls.*

**Parsec (pc).** Distance at which 1 au subtends 1 arcsecond; 1 pc ≈ 3.26 light-years. The Pleiades are at about 135 pc.

**Partner data centre (mirror).** Institute that hosts an identical copy of the Gaia catalogue with its own query service, for example ARI Heidelberg or AIP Potsdam. Used when the ESA archive is down. *Like a mirror of a sequence database (ENA, DDBJ, GenBank exchange the same records).*

**Proper motion (µ_α\*, µ_δ).** Angular motion of a star across the sky per year (mas/yr), in right ascension (with cos δ factor, hence the asterisk) and declination. Cluster members share almost the same proper motion. *Like a shared haplotype: members cluster tightly in this space.*

**Reference zone (of a completeness curve).** The distance range (here 20 to 30 pc) to which the curve is normalised to 1. If a cut removes more stars there than farther out, the curve rises artificially.

**RUWE.** Renormalised unit weight error: goodness of fit of Gaia's single-star astrometric model. About 1 for good single stars; above about 1.4 the solution is suspect, often because of an unresolved binary. *Like excess heterozygosity flagging a mixed or contaminated sample.*

**Test power (of a quality cut).** A fixed threshold such as RUWE < 1.4 is a significance test, and its power depends on measurement precision. Bright, nearby stars are measured precisely, so their binaries are flagged more often than those of faint, distant stars. *Like a HWE test that finds deviations at n = 1000 and misses them at n = 50.*

**Visibility periods used.** Gaia column counting the separate time windows in which a star was observed. Depends mainly on position on the sky through Gaia's scanning pattern.

**Tidal tails.** Streams of stars that have escaped a cluster, leading and trailing it along its Galactic orbit. *Emigrants that still carry the source population's signature.*

**Vector point diagram (VPD).** Scatter plot of µ_α\* against µ_δ. Clusters appear as tight clumps on top of the broad field distribution.

**Window search.** Selection of cluster candidates by a box or circle in proper motion and parallax, with the field contribution estimated from a ring around it. Simple, but ignores perspective effects.

**White dwarf.** Compact remnant of a low- to intermediate-mass star after it has shed its envelope; hot but faint, forming a separate sequence below the main sequence in the CMD. Cooling ages of white dwarfs give lower limits on cluster ages.
