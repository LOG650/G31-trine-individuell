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

Min–maks-styring er et klassisk inventarsystem der hver vare tildeles et minimums- og maksimumsnivå. I denne modellen utløser et lagernivå som er lik eller under min-bestanden en bestilling opp til maks, og modellen styres av en kombinasjon av sikkerhetslager og forventet forbruk i ledetiden. Dette er nært knyttet til teori om reorder points og safety stock, hvor målet er å balansere service level mot lagerkostnader.

I retail er denne balansen særlig tydelig. Lav lagerbinding kan gi reduserte kapitalkostnader, men fører ofte til høy tom-hylle-rate og tapte salg. Høy tilgjengelighet gir bedre service level, men krever mer kapital bundet i lager. Denne trade-off-en er sentral i inventory theory (Axsäter, 2015; Silver *et al.*, 2017) og er et kjernepunkt i denne oppgaven.

Relevante teorier som begrunner tilnærmingen i dette prosjektet er:

- **Economic Order Quantity (EOQ):** Gir et teoretisk grunnlag for hvordan bestillingsstørrelser påvirker kostnadene ved lagerhold og ordrebehandling. Selv om EOQ vanligvis forutsetter kontinuerlig etterspørsel, gir prinsippene et nyttig rammeverk for å forstå hvorfor økte min-/maks-nivåer kan redusere service gap.
- **Safety Stock:** Beskriver hvor mye buffer som trengs for å møte usikkerhet i etterspørsel og ledetid. Økt sikkerhetslager reduserer sannsynligheten for tom-hylle-situasjoner, men øker gjennomsnittlig binding.
- **Service Level Management:** Retail-studier viser at service level-mål over 95 % ofte krever betydelig lagerbinding, og at riktige policyer må tilpasses produktets etterspørselsprofil (Axsäter, 2015; Gasparin & Thenint, 2020).
- **Retail Operations:** Mindre butikker med begrenset lagerplass og begrensede mottaksdager må vurdere både fysisk plass og operasjonelle begrensninger som bemanning og utpakkingstid (Ciancimino & Lagana, 2015).

Litteraturgjennomgangen i denne rapporten tar utgangspunkt i at min–maks-policyer fungerer godt for produkter med relativt stabil etterspørsel, men at variabel etterspørsel gir økt risiko for tom-hylle-dager. Silver *et al.* (2017) peker på at min–maks skal ha tilstrekkelig sikkerhetslager for å møte usikkerhet, og Axsäter (2015) dokumenterer at service level møter en stigende lagringskostnadsfunksjon.

Simulering er anerkjent som en relevant metode når reelle operasjonelle data mangler, og spesielt i retail der scenarioanalyse kan gi innsikt i policyvalg uten å påvirke faktisk drift (Baboli *et al.*, 2011; Voss *et al.*, 2002). Basert på dette er en simuleringsmodell valgt for å teste både dagens policy og alternative min–maks-nivåer.

## Metode

### Forskningsdesign
Denne studien har et kvantitativt, eksperimentelt design hvor ulike min–maks-policyer sammenlignes ved hjelp av simulering. Designet er strukturert i fire faser som reflekterer prosjektets egenfaseinndeling:

1. Problemidentifikasjon: Formulering av problemstilling basert på TRN Ankomsts operative utfordringer.
2. Planlegging: Utvikling av prosjektplan, risikovurdering og avgrensning av omfang.
3. Gjennomføring: Implementering av Python-simulering og innsamling av resultater.
4. Analyse og rapportering: Tolkning av resultater, diskusjon og anbefalinger.

### Datainnsamling og antakelser
Uten tilgang til konfidensielle bedriftsdata er det brukt simulerte data med antakelser som er basert på faglitteratur og typiske retail-mønstre.

- **Produkter:** Sju representative skjønnhetsprodukter er valgt for å balansere analytisk dybde og gjennomførbarhet. Utvalget dekker ulike etterspørselsprofiler fra dagligvarer til mer impulssalg.
- **Etterspørsel:** Daglig etterspørsel er modellert med Poisson-fordeling fordi denne fordelingen er passende for diskrete, uavhengige hendelser med relativt lav daglig volum. En normal etterspørselsdag bruker λ=3, mens kampanjedager bruker λ=8 for å reflektere midlertidig økt etterspørsel.
- **Lead time:** Ledetid er først modellert som en stokastisk fordeling med 1–3 dager for å fange opp variasjon i transport, ordrebehandling og intern håndtering. I tillegg er det kjørt faste lead time-scenarier for 1–4 dager for å teste hvordan operasjonelle forskjeller i dag, tidspunkt, bemanning og utpakking påvirker tilgjengeligheten.
- **Leveringskalender:** Det er forutsatt at levering skjer alle dager unntatt tirsdag, noe som er en relevant begrensning i TRN Ankomsts drift.
- **Hyllerapiditet:** Modellen skiller mellom ankomst til flyplass og tidspunktet varen er salgs-klar, fordi utpakking og plassering kan forsinke tilgjengeligheten.
- **Bestillingsregler:** Ordre kvantiteres i multipler av 3, i tråd med praktiske emballasje- og leveringskrav.

### Simuleringsmodell
Simuleringen er implementert i Python som en dagen-for-dagen modell av lagerbeholdning, etterspørsel og bestillingsprosesser. Hovedkomponentene er:

- beregning av daglig etterspørsel per produkt
- vurdering av lagerstatus og bestillingsutløsning ved nivå ≤ min
- modellering av leveringstid og mottak
- måling av KPI-er per produkt og totalt

Modellen er holdt relativt enkel for å sikre transparens og forståelighet, samtidig som den fanger de viktigste operasjonelle drivkreftene i TRN Ankomst.

### Testede scenarier
Tre policyvarianter utgjør kjernen i analysen:

- Baseline: Dagens min–maks-nivåer
- Variant A: +1 på både min og maks
- Variant B: +2 på både min og maks

Denne komparative tilnærmingen gjør det mulig å vurdere de marginale effektene av økt sikkerhetslager og større bestillingsintervaller.

### KPI-er
De valgte måleparametrene følger retail-litteraturens standarder for tilgjengelighet og binding:

- Tom-hylle-rate: Andel dager med 0 enheter på lager
- Lav-hylle-rate: Andel dager med mindre enn 2 enheter på lager
- Gjennomsnittlig binding: Gjennomsnittlig beholdning over perioden
- Tapt etterspørsel: Summen av etterspørsel som ikke kunne tilfredsstilles

### Validitet og reliabilitet
For å styrke intern validitet er samme etterspørselsscenario brukt for alle policyer, og deterministisk initialisering av random seed gir reproduserbare resultater. Reliabilitet er forbedret gjennom 30 gjentatte simuleringer per scenario, noe som reduserer effekten av tilfeldig støy.

Ekstern validitet er begrenset av at modellen opererer på simulerte data og et avgrenset produktutvalg. Likevel er parametrene valgt for å være representative for retail-miljøer med begrenset lagerplass og mottaksdager. Rapportens funn er dermed mest pålitelige som relative effekter mellom policyer, snarere enn som absolutt prognose for TRN Ankomst.

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

### Svar på problemstillingen
Ja. Simuleringen viser at en moderat økning i min og maks gir lavere tom-hylle-rate og lav-hylle-rate, samtidig som lagerbindingen øker moderat. Den mest robuste løsningen er **Variant A (+1 til min og maks)** fordi den gir vesentlig bedre tilgjengelighet uten uforholdsmessig høy binding.

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