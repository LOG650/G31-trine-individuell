# Rapport: Optimalt lagernivå i TRN Ankomst

**Forfatter:** Trine Østengen  
**Dato:** April 2026  
**Emne:** LOG650 Forskningsprosjekt  
**Oppdragsgiver:** Høgskulen på Vestlandet  

## Sammendrag

Dette forskningsprosjektet undersøker hvordan min–maks-parametere påvirker varetilgjengelighet i TRN Ankomst, Oslo Lufthavn. Gjennom en systematisk tilnærming som inkluderer litteraturstudier, problemformulering og kvantitativ simulering viser resultatene at små økninger i min–maks-nivåer kan redusere tom-hylle-rate betydelig, samtidig som lagerbinding holdes innenfor akseptable grenser. Rapporten anbefaler en moderat økning i min–maks-nivåer for å forbedre kundetilfredshet og muliggjøre salgsfremmende tiltak.

Prosjektet har vært gjennomført i henhold til LOG650s krav til vitenskapelig forskningsrapport, med fokus på praktisk relevans for retail-logistikk og bruk av simulerte data for å unngå konfidensialitetsproblemer.

## Innledning

### Bakgrunn og kontekst
I retail-sektoren er lagerstyring en kritisk suksessfaktor for kundetilfredshet og lønnsomhet. Min–maks-styring er en vanlig metode for automatisk etterfylling, hvor nye bestillinger utløses når beholdning faller under et minimumsnivå, og påfyll skjer opp til et maksimumsnivå. I praksis balanseres dette mot leveringstider, etterspørselsvariasjoner og lagerkostnader.

TRN Ankomst på Oslo Lufthavn representerer et spesielt case: høyt trafikkvolum med varierende etterspørsel, begrenset lagringskapasitet, og leveringsrestriksjoner (ingen mottak på tirsdager). Butikken opererer med svært lave min–maks-nivåer for å minimere lagerbinding, men dette fører til hyppige tom-hylle-situasjoner som påvirker kundeopplevelsen negativt.

### Problemstilling
Hvilke min–maks-parametere gir lavest tom-hylle-rate og lav-hylle-rate for utvalgte skjønnhetsprodukter i TRN Ankomst, og hva er konsekvensen av alternative min–maks-nivåer for lagerbinding?

### Formål og forskningsspørsmål
Formålet med prosjektet er å identifisere optimale min–maks-nivåer som balanserer tilgjengelighet mot lagerkostnader, basert på en kvantitativ analyse av simulerte driftsforhold.

Forskningsspørsmål:
1. Hvordan påvirker forskjellige min–maks-nivåer tom-hylle-rate og lav-hylle-rate?
2. Hva er trade-off mellom forbedret tilgjengelighet og økt lagerbinding?
3. Hvilke praktiske anbefalinger kan gis for TRN Ankomst?

### Avgrensninger
- Omfang: TRN Ankomst, 7 skjønnhetsprodukter, min–maks per plassering
- Metode: Kvantitativ simulering med simulerte data
- Tid: 90 dager simulering
- Utelukket: Reelle bedriftsdata, sesongvariasjoner, prisendringer, kampanjer

## Teoretisk rammeverk

### Min–maks-styring i retail
Min–maks-styring er en reorder point-metode hvor:
- Min = Sikkerhetslager + forbruk i lead time
- Maks = Min + økonomisk ordrekvantum

I praksis justeres disse basert på erfaring, og de påvirker:
- **Service level:** Andel av etterspørsel som kan dekkes umiddelbart
- **Lagerkostnader:** Binding av kapital i beholdning
- **Ordrefrekvens:** Hyppighet av bestillinger

### Relevante teorier
- **Inventory Theory:** Economic Order Quantity (EOQ) og Safety Stock-beregninger
- **Service Level Management:** Trade-off mellom tilgjengelighet og kostnader
- **Retail Operations:** Butikkdrift med begrenset plass og høyt volum

### Litteraturstudie
Gjennomgang av relevant litteratur viser at:
- Min–maks er effektiv for stabile produkter, men utfordrende ved variabel etterspørsel
- Service level >95% er vanlig mål i retail, men krever høy lagerbinding
- Simulering er egnet metode når reelle data ikke er tilgjengelig

## Metode

### Forskningsdesign
Prosjektet følger en kvantitativ tilnærming med simuleringsbasert eksperimentell design:

1. **Problemidentifikasjon** (Fase 1): Utvikling av problemstilling basert på praktisk erfaring
2. **Planlegging** (Fase 2): Utvikling av prosjektplan, WBS og risikovurdering
3. **Gjennomføring** (Fase 3): Implementering av simulering og datainnsamling
4. **Analyse og rapportering** (Fase 4): Resultatanalyse og anbefalinger

### Datainnsamling og datagrunnlag
Siden konfidensielle bedriftsdata ikke var tilgjengelig, ble simulerte data brukt:

- **Produkter:** 7 skjønnhetsprodukter med realistiske min–maks-nivåer
- **Etterspørsel:** Poisson-fordelt (λ=3 normalt, λ=8 ved kampanje)
- **Lead time:** 1-3 døgn (realistisk fordeling)
- **Leveringskalender:** Alle dager unntatt tirsdag
- **Bestillingsregler:** Multipler av 3, automatisk når ≤ min

### Simuleringsmodell
Python-basert diskret-hendelses-simulering som modellerer:
- Daglig etterspørsel og lagerbevegelser
- Bestillingsutløsning og leveringsforsinkelser
- KPI-beregning per produkt og totalt

### Testede scenarier
- **Baseline:** Dagens min–maks-nivåer
- **Variant A:** +1 til min og maks
- **Variant B:** +2 til min og maks

### KPI-er og målemetoder
- **Tom-hylle-rate:** % dager med 0 stk
- **Lav-hylle-rate:** % dager med <2 stk
- **Gjennomsnittlig binding:** Gj.snitt beholdning
- **Tapt etterspørsel:** Totalt antall usolgte enheter

### Validitet og reliabilitet
- **Interne validitet:** Samme etterspørselsserie for alle scenarier
- **Eksterne validitet:** Parametere basert på kjent drift
- **Reliabilitet:** Deterministisk random seed for reproduserbarhet

## Resultater

### Simuleringsresultater

#### Oversikt over scenarier
| Scenario | Gj.snitt tom-hylle-rate | Gj.snitt lav-hylle-rate | Gj.snitt binding | Total tapt etterspørsel |
|----------|------------------------|-------------------------|------------------|-------------------------|
| Baseline | 18.7% | 22.4% | 2.7 | 867 av 2519 (34.4%) |
| Variant A | 13.3% | 16.2% | 3.8 | 644 av 2519 (25.6%) |
| Variant B | 8.7% | 11.5% | 4.8 | 567 av 2519 (22.5%) |

#### Detaljerte resultater per produkt

##### Baseline
| Produkt | Tom% | Lav% | Binding | Tapt | Etterspørsel |
|---------|------|------|---------|------|--------------|
| Maskara | 14.4 | 18.9 | 4.1 | 130 | 408 |
| Dagkrem | 17.8 | 23.3 | 3.5 | 102 | 343 |
| Håndkrem | 18.9 | 20.0 | 3.5 | 111 | 354 |
| Parfyme | 23.3 | 26.7 | 1.2 | 211 | 385 |
| Eyeliner | 24.4 | 28.9 | 1.0 | 145 | 340 |
| Leppestift | 21.1 | 22.2 | 3.3 | 96 | 352 |
| Leppepomade | 11.1 | 16.7 | 3.4 | 72 | 337 |

##### Variant A (+1 til min og maks)
| Produkt | Tom% | Lav% | Binding | Tapt | Etterspørsel |
|---------|------|------|---------|------|--------------|
| Maskara | 11.1 | 16.7 | 3.5 | 105 | 408 |
| Dagkrem | 6.7 | 11.1 | 3.6 | 71 | 343 |
| Håndkrem | 15.6 | 17.8 | 4.0 | 77 | 354 |
| Parfyme | 18.9 | 21.1 | 4.2 | 143 | 385 |
| Eyeliner | 18.9 | 22.2 | 3.8 | 103 | 340 |
| Leppestift | 12.2 | 14.4 | 3.4 | 83 | 352 |
| Leppepomade | 10.0 | 13.3 | 5.1 | 62 | 337 |

##### Variant B (+2 til min og maks)
| Produkt | Tom% | Lav% | Binding | Tapt | Etterspørsel |
|---------|------|------|---------|------|--------------|
| Maskara | 5.6 | 8.9 | 6.7 | 94 | 408 |
| Dagkrem | 7.8 | 12.2 | 4.3 | 70 | 343 |
| Håndkrem | 7.8 | 7.8 | 3.9 | 72 | 354 |
| Parfyme | 11.1 | 14.4 | 3.6 | 114 | 385 |
| Eyeliner | 13.3 | 17.8 | 4.3 | 90 | 340 |
| Leppestift | 11.1 | 14.4 | 4.0 | 79 | 352 |
| Leppepomade | 4.4 | 5.6 | 5.8 | 48 | 337 |

## Diskusjon

### Analyse av resultater
Resultatene viser en klar trade-off mellom tilgjengelighet og lagerbinding:

- **Variant A** gir 8.8 prosentpoeng reduksjon i tapt etterspørsel (fra 34.4% til 25.6%) med moderat binding-økning (2.7 → 3.8)
- **Variant B** gir ytterligere forbedring (tapt etterspørsel ned til 22.5%), men krever betydelig høyere binding (4.8)

Produkter med svært lave baseline-nivåer viser størst forbedringspotensial. Parfyme og Eyeliner, som opererer med min=1, har baseline tom-hylle-rater på 23.3% og 24.4%, som reduseres til 11.1% og 13.3% i Variant B.

### Praktiske implikasjoner
- **Kundeservice:** Redusert tom-hylle-rate muliggjør kjøp av ønsket antall produkter
- **Salgsmuligheter:** Lavere lav-hylle-rate støtter salgsfremmende tiltak
- **Operasjonell effektivitet:** Moderat binding-økning kan være akseptabel mot økt salg

### Metodiske betraktninger
- Simuleringen gir konsistente resultater på tvers av scenarier
- Poisson-fordelt etterspørsel representerer realistisk variasjon
- Lead time-fordeling reflekterer kjente driftsforhold

### Begrensninger og videre forskning
- Simulerte data vs. reelle transaksjoner
- Ingen modellering av sesongvariasjoner eller kampanjer
- Tapt salg estimert som "censored demand" – reelle tap kan være høyere
- Videre forskning: Testing med reelle data, flere produkter, eller maskinlæring for dynamiske parametere

## Konklusjon og anbefalinger

### Hovedfunn
Simuleringen viser at dagens min–maks-nivåer fører til betydelig tapt etterspørsel (34.4%). En moderat økning (+1 til min og maks) kan redusere dette til 25.6% med akseptabel binding-økning.

### Anbefalinger
1. **Implementer Variant A** som første steg for alle 7 produktene
2. **Overvåk effekt** på service level og lagerkostnader etter implementering
3. **Vurder Variant B** for høyt-volum produkter eller ved kampanjer
4. **Etabler måling** av tom-hylle-rate og lav-hylle-rate som KPI-er

### Bidrag til fagfeltet
Prosjektet demonstrerer hvordan kvantitativ simulering kan brukes til å optimalisere lagerstyring i retail, spesielt når reelle data ikke er tilgjengelig. Metoden kan tilpasses andre retail-miljøer med lignende utfordringer.

## Referanser

- Prosjektplan LOG650 (2026)
- Silver, E. A., Pyke, D. F., & Peterson, R. (1998). *Inventory Management and Production Planning and Scheduling*. Wiley.
- Tempelmeier, H. (2012). *Inventory Management in Supply Networks*. Books on Demand.

## Vedlegg

1. Prosjektplan (full versjon)
2. Simuleringskode (Python)
3. Detaljerte simuleringsresultater
4. Risikoanalyse og WBS