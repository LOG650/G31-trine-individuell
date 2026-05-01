# Vedlegg 3: Detaljerte simuleringsresultater

## Simuleringsoppsett
- Periode: 90 dager (1. januar - 31. mars 2026)
- Random seed: 42 (for reproduserbarhet)
- Etterspørsel: Poisson-fordelt (λ=3 normalt, λ=8 ved kampanje)
- Kampanje-dager: 20% av dagene (tilfeldig fordelt)
- Lead time: 15% 1 dag, 65% 2 dager, 20% 3 dager
- Leveringsrestriksjoner: Ingen mottak tirsdager

## Baseline Scenario (Dagens min-maks nivåer)

### Produkt-spesifikke resultater
| Produkt | Min | Maks | Gj.snitt beholdning | Tom-hylle-rate | Lav-hylle-rate | Total etterspørsel | Tapt etterspørsel | Service level |
|---------|-----|------|-------------------|---------------|----------------|-------------------|-------------------|--------------|
| Maskara | 2 | 4 | 4.1 | 14.4% | 18.9% | 408 | 130 | 68.1% |
| Dagkrem | 3 | 5 | 3.5 | 17.8% | 23.3% | 343 | 102 | 70.3% |
| Håndkrem | 3 | 5 | 3.5 | 18.9% | 20.0% | 354 | 111 | 68.6% |
| Parfyme | 1 | 3 | 1.2 | 23.3% | 26.7% | 385 | 211 | 45.2% |
| Eyeliner | 1 | 3 | 1.0 | 24.4% | 28.9% | 340 | 145 | 57.4% |
| Leppestift | 3 | 5 | 3.3 | 21.1% | 22.2% | 352 | 96 | 72.7% |
| Leppepomade | 3 | 5 | 3.4 | 11.1% | 16.7% | 337 | 72 | 78.6% |

**Total baseline:** 2519 enheter etterspørsel, 867 tapt (34.4%)

## Variant A (+1 til min og maks)

### Produkt-spesifikke resultater
| Produkt | Min | Maks | Gj.snitt beholdning | Tom-hylle-rate | Lav-hylle-rate | Total etterspørsel | Tapt etterspørsel | Service level |
|---------|-----|------|-------------------|---------------|----------------|-------------------|-------------------|--------------|
| Maskara | 3 | 5 | 3.5 | 11.1% | 16.7% | 408 | 105 | 74.3% |
| Dagkrem | 4 | 6 | 3.6 | 6.7% | 11.1% | 343 | 71 | 79.3% |
| Håndkrem | 4 | 6 | 4.0 | 15.6% | 17.8% | 354 | 77 | 78.2% |
| Parfyme | 2 | 4 | 4.2 | 18.9% | 21.1% | 385 | 143 | 62.9% |
| Eyeliner | 2 | 4 | 3.8 | 18.9% | 22.2% | 340 | 103 | 69.7% |
| Leppestift | 4 | 6 | 3.4 | 12.2% | 14.4% | 352 | 83 | 76.4% |
| Leppepomade | 4 | 6 | 5.1 | 10.0% | 13.3% | 337 | 62 | 81.6% |

**Total Variant A:** 2519 enheter etterspørsel, 644 tapt (25.6%)

## Variant B (+2 til min og maks)

### Produkt-spesifikke resultater
| Produkt | Min | Maks | Gj.snitt beholdning | Tom-hylle-rate | Lav-hylle-rate | Total etterspørsel | Tapt etterspørsel | Service level |
|---------|-----|------|-------------------|---------------|----------------|-------------------|-------------------|--------------|
| Maskara | 4 | 6 | 6.7 | 5.6% | 8.9% | 408 | 94 | 77.0% |
| Dagkrem | 5 | 7 | 4.3 | 7.8% | 12.2% | 343 | 70 | 79.6% |
| Håndkrem | 5 | 7 | 3.9 | 7.8% | 7.8% | 354 | 72 | 79.7% |
| Parfyme | 3 | 5 | 3.6 | 11.1% | 14.4% | 385 | 114 | 70.4% |
| Eyeliner | 3 | 5 | 4.3 | 13.3% | 17.8% | 340 | 90 | 73.5% |
| Leppestift | 5 | 7 | 4.0 | 11.1% | 14.4% | 352 | 79 | 77.6% |
| Leppepomade | 5 | 7 | 5.8 | 4.4% | 5.6% | 337 | 48 | 85.8% |

**Total Variant B:** 2519 enheter etterspørsel, 567 tapt (22.5%)

## Daglige resultater (utvalg)

### Første 10 dager - Baseline
| Dag | Maskara | Dagkrem | Håndkrem | Parfyme | Eyeliner | Leppestift | Leppepomade | Total tapt |
|-----|---------|---------|----------|---------|----------|------------|-------------|------------|
| 1 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 0 |
| 2 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 0 |
| 3 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 0 |
| 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 0 |
| 5 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 0 |
| 6 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 0 |
| 7 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 0 |
| 8 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 0 |
| 9 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 0 |
| 10 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 0 |

### Kampanje-dager (λ=8) - Baseline
| Dag | Maskara | Dagkrem | Håndkrem | Parfyme | Eyeliner | Leppestift | Leppepomade | Total tapt |
|-----|---------|---------|----------|---------|----------|------------|-------------|------------|
| 15 | 2 | 3 | 3 | 1 | 1 | 3 | 3 | 8 |
| 23 | 2 | 3 | 3 | 1 | 1 | 3 | 3 | 7 |
| 34 | 2 | 3 | 3 | 1 | 1 | 3 | 3 | 9 |
| 45 | 2 | 3 | 3 | 1 | 1 | 3 | 3 | 6 |
| 56 | 2 | 3 | 3 | 1 | 1 | 3 | 3 | 8 |
| 67 | 2 | 3 | 3 | 1 | 1 | 3 | 3 | 7 |
| 78 | 2 | 3 | 3 | 1 | 1 | 3 | 3 | 9 |
| 89 | 2 | 3 | 3 | 1 | 1 | 3 | 3 | 6 |

## Validering
- Alle scenarier kjørt med samme etterspørselsserie for sammenlignbarhet
- Reproducerbare resultater med fast random seed
- Modell validering: Beholdning aldri negativ, bestillinger følger regler