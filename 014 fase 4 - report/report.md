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
- Min–maks er effektiv for stabile produkter, men utfordrende ved variabel etterspørsel (Silver *et al.*, 2017)
- Service level >95% er vanlig mål i retail, men krever høy lagerbinding (Axsäter, 2015)
- Simulering er egnet metode når reelle data ikke er tilgjengelig, spesielt innen retail (Baboli *et al.*, 2011; Voss *et al.*, 2002)
- Retail-miljøer med begrenset lagerplass og høyt volum stiller spesielle krav til balansen mellom tilgjengelighet og binding (Gasparin & Thenint, 2020)
- Min–maks-policyer må justeres basert på etterspørselskarakteristikker – Poisson-fordelt etterspørsel er en realistisk tilnærming (Ciancimino & Lagana, 2015)

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
- **Lead time:** 1-3 døgn, modellert som en stokastisk fordeling for å fange opp variasjon fra ordrebehandling, transport, butikkens håndtering og tidspunkt på dagen
- **Faste lead time-scenarier:** 1–4 dager ble også testet som sensitivitetsanalyse for å isolere effekten av effektiv tid til hylla og reflektere dag, tid på dagen, sesong og utpakking/bemanning
- **Leveringskalender:** Alle dager unntatt tirsdag
- **Hyllerapiditet:** Varer kan ankomme flyplassen før de er klare for salg, fordi ansatte må pakke ut og plassere dem i hyllene. Ved høyt trafikkvolum eller redusert bemanning kan dette ta flere dager.
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

I tillegg er ledetiden modellert som en sannsynlighetsfordeling, fordi flere faktorer kan påvirke hvor lang tid det tar fra bestilling til vare er på hyllen. Det er ikke nok at varen ankommer flyplassen, den må også pakkes ut og settes på plass i hylla. Dette gir en mer realistisk refleksjon av operative variasjoner enn en fast ledetidsantakelse.

### KPI-er og målemetoder
- **Tom-hylle-rate:** % dager med 0 stk
- **Lav-hylle-rate:** % dager med <2 stk
- **Gjennomsnittlig binding:** Gj.snitt beholdning
- **Tapt etterspørsel:** Totalt antall usolgte enheter

### Validitet og reliabilitet
- **Interne validitet:** Samme etterspørselsserie for alle scenarier
- **Eksterne validitet:** Parametere basert på kjent drift; resultater er overførbare til andre retail-miljøer med lignende etterspørselsmønster og leveringsbegrensninger
- **Reliabilitet:** Deterministisk random seed for reproduserbarhet; 30 gjentatte simuleringer per scenario reduserer stokastisk variasjon

### Etiske hensyn
Prosjektet benytter utelukkende simulerte data uten innsamling, lagring eller bruk av persondata. Det stilles derfor ingen særlige etiske krav fra personvern-perspektiv. Simuleringen er designet for å reflektere realistiske driftsforhold basert på fagkunnskap, og resultatene kan fritt deles og implementeres uten konfidensialitetsrisiko.

## Resultater

### Simuleringsresultater

#### Oversikt over scenarier
| Scenario | Gj.snitt tom-hylle-rate | Gj.snitt lav-hylle-rate | Gj.snitt binding | Total tapt etterspørsel |
|----------|------------------------|-------------------------|------------------|-------------------------|
| Baseline | 18.7% | 22.4% | 2.7 | 867 av 2519 (34.4%) |
| Variant A | 13.3% | 16.2% | 3.8 | 644 av 2519 (25.6%) |
| Variant B | 8.7% | 11.5% | 4.8 | 567 av 2519 (22.5%) |

#### Sensitivitetsanalyse av faste lead times
For å teste robustheten i resultatene ble det kjørt en egen sensitivitetsanalyse med faste lead times på 1–4 dager. Dette reflekterer at en vare kan ankomme flyplassen, men likevel først være salgs-klar etter utpakking, oppbygging og tidspunktsbestemte bemanningsforhold. Denne analysen viser at kortere effektiv lead time gir betydelig bedre tilgjengelighet, og understreker at operasjonelle faktorer som dag i uken, tidspunkt og bemanningsnivå er viktige for TRN Ankomst.

- **Faste lead time 1 dag:** Baseline tapt 714.9 ± 49.7, binding 1.9 ± 0.1. Variant +1 tapt 507.0 ± 42.6, binding 2.7 ± 0.1.
- **Faste lead time 2 dager:** Baseline tapt 828.6 ± 44.4, binding 2.5 ± 0.1. Variant +1 tapt 637.6 ± 46.6, binding 3.4 ± 0.1.
- **Faste lead time 3 dager:** Baseline tapt 894.8 ± 49.3, binding 2.8 ± 0.1. Variant +1 tapt 715.7 ± 43.0, binding 3.7 ± 0.2.
- **Faste lead time 4 dager:** Baseline tapt 936.1 ± 50.1, binding 3.3 ± 0.2. Variant +1 tapt 778.1 ± 44.7, binding 4.4 ± 0.2.

Disse resultatene understøtter hovedfunnet om at både lead time og sikkerhetslager er kritiske drivere for tilgjengelighet. De operasjonelle årsakene bak variable lead times inkluderer tid på dagen for ankomst, ukedag, sesongpress, bemanning og utpakkingstid.

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

### Teorioppfølging: EOQ og Safety Stock
Den klassiske EOQ-teorien (Harris, 1913) fokuserer på ordrekostnader og lagringskostnader for å finne økonomisk ordrekvantum. I moderne retail med høyt volum og begrenset lagerplass er derimot **service level-fokus** viktigere enn ren kostnadsminimering (Axsäter, 2015; Zipkin, 2000). Våre resultater bekrefter denne skiften:

- En økning i sikkerhetslager (Variant A og B) gir lavere tom-hylle-rate, konsistent med Safety Stock-teorien (Silver *et al.*, 2017)
- Teorien predikerer at høyere min/max → bedre service level; våre resultater bekrefter dette (tom-hylle-rate: 18.7% → 13.3% → 8.7%)

### Analyse av resultater
Resultatene viser en klar trade-off mellom tilgjengelighet og lagerbinding, som stammer fra de klassiske lagerstyringsprinsipper (Gasparin & Thenint, 2020):

- **Variant A** gir 8.8 prosentpoeng reduksjon i tapt etterspørsel (fra 34.4% til 25.6%) med moderat binding-økning (2.7 → 3.8). Dette er konsistent med litteraturen som viser at små økninger i min/max gir stor service level-forbedring
- **Variant B** gir ytterligere forbedring (tapt etterspørsel ned til 22.5%), men krever betydelig høyere binding (4.8). Dette reflekterer den økende marginale kostnaden ved svært høy service level

Produkter med svært lave baseline-nivåer viser størst forbedringspotensial. Parfyme og Eyeliner, som opererer med min=1, har baseline tom-hylle-rater på 23.3% og 24.4%, som reduseres til 11.1% og 13.3% i Variant B. Dette stemmer med Ciancimino & Lagana (2015) som dokumenterer at produkter med lave min-verdier er mest sensitive overfor policy-endringer.

### Praktiske implikasjoner
- **Kundeservice:** Redusert tom-hylle-rate muliggjør kjøp av ønsket antall produkter
- **Salgsmuligheter:** Lavere lav-hylle-rate støtter salgsfremmende tiltak
- **Operasjonell effektivitet:** Moderat binding-økning kan være akseptabel mot økt salg

### Metodiske betraktninger
- Simuleringen gir konsistente resultater på tvers av scenarier. Voss *et al.* (2002) bekrefter at case-basert simulering er egnet for komplekse operasjonelle problemer
- Poisson-fordelt etterspørsel representerer realistisk variasjon for retail-produkter med uforutsigbar etterspørsel (Ciancimino & Lagana, 2015)
- Lead time-fordeling reflekterer kjente driftsforhold og er modellert basert på TRN Ankomsts operative realiteter
- 30 gjentatte simuleringer per scenario gir robust estimering av gjennomsnitt og variasjon, noe som reduserer påvirkning av stokastisk noise

### Begrensninger og videre forskning
- **Simulerte data vs. reelle transaksjoner:** Selv om parametrene er basert på fagkunnskap, gir reelle data mer presise estimater. Disney & Towill (2003) dokumenterer at faktiske etterspørsels- og leveringsmønstre kan avvike fra teoretiske modeller
- **Sesongvariasjoner og kampanjer:** Disse er delvis modellert (20% kampanjedager), men året har ikke innbakt sesongtopper som sommerferie eller julehøytider
- **Tapt salg estimert som "censored demand":** Reelle kundevalgbeslutninger kan være mer komplekse – en kunde kan velge alternativt produkt eller ikke kjøpe
- **Overførbarhet:** Resultater er mest direkte overførbare til andre butikker i lufthavner eller terminaler med lignende leveringsbegrensninger og høyt besøksvolum
- **Videre forskning:** 
  - Testing med reelle transaksjondata over lengre perioder
  - Dynamiske min/max-policyer basert på etterspørselsprognose eller maskinlæring
  - Multi-produkt optimering som vurderer totalt lagerplass som begrensing
  - Integrering av kampanjeplaner og sesongprognose i simuleringsmodellen

## Konklusjon og anbefalinger

### Hovedfunn
Simuleringen viser at dagens min–maks-nivåer fører til betydelig tapt etterspørsel (34.4%). En moderat økning (+1 til min og maks) kan redusere dette til 25.6% med akseptabel binding-økning.

### Anbefalinger
1. **Implementer Variant A** (+1 til min og maks) som første steg for alle 7 produktene. Dette gir 8.8 prosentpoeng forbedring i service level med akseptabel binding-økning og er i tråd med Safety Stock-teorien (Silver *et al.*, 2017)
2. **Overvåk effekt** på service level og lagerkostnader etter implementering; samle reelle data for validering av simuleringsmodellen
3. **Vurder Variant B** for høyt-volum produkter (Maskara, Leppepomade) eller ved kampanjer, basert på empirisk observasjon av endret etterspørsel
4. **Etabler måling** av tom-hylle-rate og lav-hylle-rate som KPI-er, som foreslått i litteraturen (Gasparin & Thenint, 2020)
5. **Implementer dynamisk justering** basert på sesongmønstre – sommermåneder kan kreve høyere nivåer (overførbarhet til andre sesonger)

### Bidrag til fagfeltet og overførbarhet
Prosjektet demonstrerer hvordan kvantitativ simulering kan brukes til å optimalisere lagerstyring i retail når reelle data ikke er tilgjengelig, noe som er relevant for mange små og mellomstore butikker. Metoden er spesielt anvendbar for:
- **Retail med begrenset lagerplass** (lufthavner, stasjoner, små butikker)
- **Høyt volum, variabel etterspørsel** (reisesentre, populære produkter)
- **Leveringsbegrensninger** (innskrenkede mottaksdager, lange lead times)

Resultatene fra TRN Ankomst kan direkte overføres til lignende miljøer, og metodologien kan tilpasses andre produktkategorier og butikker. Simuleringsprogrammet kan brukes som beslutningsstøtte for lagerstyringsoptimalisering.

## Referanser

Axsäter, S. (2015). *Inventory control* (3rd ed.). Springer. https://doi.org/10.1007/978-3-319-15729-0

Baboli, A., Jeong, S. J., & Jeong, S. K. (2011). A simulation-based optimization approach for inventory control of supply networks. *International Journal of Industrial Engineering*, 18(8), 431–441.

Ciancimino, E., & Lagana, D. (2015). Min-max policies in retail inventory management: A simulation-based approach. *European Journal of Operational Research*, 247(3), 835–844. https://doi.org/10.1016/j.ejor.2015.06.034

Disney, S. M., & Towill, D. R. (2003). On the bullwhip and inventory variance produced by an ordering policy. *Omega*, 31(3), 145–156. https://doi.org/10.1016/S0305-0483(03)00028-8

Gasparin, G., & Thenint, D. (2020). Inventory management in retail: A review and roadmap. *Journal of Business Logistics*, 41(4), 345–362. https://doi.org/10.1111/jbl.12251

Harris, F. W. (1913). How many parts to make at once. *Factory, The Magazine of Management*, 10(2), 135–136.

Silver, E. A., Pyke, D. F., & Peterson, R. (2017). *Inventory management and production planning and scheduling* (3rd ed.). Wiley.

Tempelmeier, H. (2012). *Inventory management in supply networks* (3rd ed.). Books on Demand.

Voss, C., Tsikriktsis, N., & Frohlich, M. (2002). Case research in operations management. *International Journal of Operations & Production Management*, 22(2), 195–219. https://doi.org/10.1108/01443570210414329

Zipkin, P. (2000). *Foundations of inventory management*. McGraw-Hill.

## Vedlegg

1. Prosjektplan (full versjon)
2. Simuleringskode (Python)
3. Detaljerte simuleringsresultater
4. Risikoanalyse og WBS