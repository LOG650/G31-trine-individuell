# Peer Review Utkast – LOG650 Forskningsprosjekt

**Prosjekt:** Optimalt lagernivå i TRN Ankomst  
**Forfatter:** Trine Østengen  
**Dato:** 28. april 2026  

## Sammendrag (2-3 setninger)
Dette prosjektet undersøker hvordan min–maks-parametere påvirker varetilgjengelighet i TRN Ankomst. Gjennom kvantitativ simulering viser resultatene at små økninger i min–maks-nivåer kan redusere tom-hylle-rate betydelig, samtidig som lagerbinding holdes innenfor akseptable grenser. Rapporten anbefaler en moderat økning for å forbedre kundetilfredshet og muliggjøre salgsfremmende tiltak.

## Metode (kort beskrivelse)
- Python-basert simulering av min–maks-styrt etterfylling
- 7 skjønnhetsprodukter over 90 dager
- Realistisk etterspørsel (Poisson-fordelt), lead time 1-3 døgn, ingen mottak tirsdager
- Testet baseline vs. +1/+2 til min-maks

## Nøkkelresultater (tabell/figur)
| Scenario | Tom-hylle-rate | Lav-hylle-rate | Tapt etterspørsel | Gj.snitt binding |
|----------|----------------|----------------|-------------------|------------------|
| Baseline | 18.7% | 22.4% | 34.4% | 2.7 |
| Variant A (+1) | 13.3% | 16.2% | 25.6% | 3.8 |
| Variant B (+2) | 8.7% | 11.5% | 22.5% | 4.8 |

## Diskusjon (2-3 punkter)
- Variant A gir betydelig forbedring (reduksjon 8.8% tapt etterspørsel) med moderat binding-økning
- Spesielt effektivt for produkter med lave baseline-nivåer (Parfyme, Eyeliner)
- Muliggjør bedre kundeservice og salgsaktiviteter

## Begrensninger
- Simulert etterspørsel (ikke reelle data)
- Ingen modellering av sesong/kampanjer
- Tapt salg estimert som "censored demand"

## Tilbakemeldingsområder
- Er metodebeskrivelsen tydelig nok?
- Er resultatpresentasjonen effektiv?
- Mangler det viktige aspekter i diskusjonen?
- Er anbefalingene praktisk gjennomførbare?

## Vedlegg
- Full rapport (report.md)
- Simuleringskode (simulate_min_max.py)
- Detaljerte resultater