# Rapport: Optimalt lagernivå i TRN Ankomst

**Forfatter:** Trine Østengen  
**Dato:** April 2026  
**Emne:** LOG650 Forskningsprosjekt  
**Oppdragsgiver:** Høgskulen på Vestlandet  

## Sammendrag

Denne studien undersøker hvordan min–maks-policyer påvirker varetilgjengeligheten ved TRN Ankomst, Oslo Lufthavn. Ved å kombinere faglitteratur og kvantitativ simulering vurderes effektene av alternative min–maks-nivåer på tom-hylle-rate, lav-hylle-rate og lagerbinding. Resultatene peker på at et moderat økt policynivå reduserer tom-hylle-rate betydelig, med en akseptabel økning i gjennomsnittlig lagerbinding. Studien anbefaler å implementere det moderate policyløftet parallelt med tiltak for å redusere tiden fra mottak til salgsklart.

Arbeidet er gjennomført i tråd med LOG650s krav til vitenskapelig rapportering, med vekt på metodisk transparens og reproducerbarhet ved bruk av simulerte data.

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
- **Hylleparatitet:** Modellen skiller mellom ankomst til flyplass og tidspunktet varen er salgs-klar (hylleparatitet), fordi utpakking og plassering kan forsinke tilgjengeligheten.
- **Bestillingsregler:** Ordre kvantiteres i multipler av 3, i tråd med praktiske emballasje- og leveringskrav.

### Eksplisitte antakelser og hvordan de er vurdert
For tydelighet og etterprøvbarhet listes her prosjektets sentrale antakelser eksplisitt, sammen med kort hvordan hver antakelse er begrunnet eller testet. Dette bygger på kompendiets anbefalte prosess for metode- og antakelseskontroll (Pettersen & Rekdal, 2026).

- **Uavhengig daglig etterspørsel (Poisson):** Vi antar at daglig etterspørsel per produkt er uavhengig og tilnærmet Poisson-fordelt. Valget er faglig begrunnet for lave diskrete volum; vi validerer ved visuell sjekk av simulerte frekvensfordelinger og sensitivitetskjøringer mot høyere λ-verdier.
- **Stokastisk ledetid modellering:** Ledetid antas uavhengig av etterspørsel og følger den spesifiserte diskrete fordelingen (1–3 dager) i hovedscenariet. Vi isolerer ledetidseffekter gjennom faste lead time-scenarier (1–4 dager) for å teste robusthet.
- **Tapte etterspørselsantagelse (lost sales):** Etterspørsel som ikke kan oppfylles umiddelbart antas tapt (ikke backorder). Dette gir en konservativ måling av tapt salg; alternative antakelser (substitution eller forsinket kjøp) kan vurderes i videre arbeid.
- **Produkt-uavhengighet:** Produkter modelleres uten kryss-effekter (ingen substitution eller bundling). Dette forenkler tolkning av policyeffekter per produkt, men begrenser overførbarhet i situasjoner med sterk krysseeffekt.
- **Ingen eksplisitt plassbegrensning:** Modellens struktur inkluderer ikke en eksplisitt kapasitetsbegrensning for fysisk lagerplass. Binding tolkes derfor som gjennomsnitt per produkt, ikke samlet arealkapasitet.
- **Mottaks- og bemanningsmønster:** Effektiv lead time inkluderer operasjonelle forsinkelser ved utpakking og tidspunkter for bemanning. Disse faktorene er eksplisitt undersøkt i sensitivitetsanalysen for faste lead times.

For hver antakelse henvises det til Appendix A for de eksakte parameterverdiene og koden som ble brukt for validering og sensitivitetskjøringer. Der finnes også en tabell over alle sentrale parametre og hvordan `REPEATS` og `BASE_SEED` er satt for reproduserbarhet.

### Sjekk av antakelser og sensitivitetsstrategi
I tråd med kompendiets prosessanbefaling (se avsnitt i.4 i Pettersen & Rekdal, 2026) har vi implementert følgende kontroller og sensitivitetsstrategier:

- Kjøring av multiple repeterte simuleringer (30 repeter) for å vurdere resultatstabilitet.
- Sensitivitetskjøringer for etterspørselsparameter (λ), faste vs. stokastiske ledetider, og alternative policyløft (+1 / +2) for å vurdere robusthet.
- Enkel grafisk og numerisk sjekk av simulerte etterspørselsfordelinger for å bekrefte at Poisson-tilnærmelsen ikke gir systematiske avvik under de valgte parametrene.

Disse tiltakene sikrer at modellens begrensninger er synlige i analysen og at anbefalinger formuleres som relative policy-anbefalinger, slik kompendiet anbefaler for prosjekter uten full tilgang til reelle driftsdata.
### Simuleringsmodell
Simuleringen er implementert i Python som en dag-for-dag modell av lagerbeholdning, etterspørsel og bestillingsprosesser. Hovedkomponentene er:

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

### Teoretisk tolkning
Den empiriske analysen bekrefter flere sentrale poenger fra inventory theory. EOQ-fundamentet (Harris, 1913) legger vekt på kostnadsbalanse mellom ordre- og lagerhold, men i et retail-miljø med begrenset plass blir service level og kundetilgjengelighet ofte viktigere enn lavest mulig binding (Axsäter, 2015; Zipkin, 2000). Resultatene fra Variant A og Variant B illustrerer denne grunnleggende trade-off-en mellom tilgjengelighet og lagerkostnad.

Økningen i min-/maks-nivåer reduserer tom-hylle-rate og lav-hylle-rate, noe som er konsistent med Safety Stock-teori (Silver *et al.*, 2017). På samme måte viser funnene at produkter med særlig lave baseline-beholdninger (parfyme og eyeliner) har størst gevinst ved økt policynivå, noe som stemmer med Ciancimino & Lagana (2015) sin analyse av sensitivitet for lav-lagerprodukter.

### Resultatdiskusjon
Analysen viser tydelige forbedringer i tilgjengelighet ved moderate økninger i min- og maks-nivå. Variant A reduserer tapt etterspørsel med 8.8 prosentpoeng (34.4 % → 25.6 %) samtidig som gjennomsnittlig lagerbinding øker fra 2.7 til 3.8. Dette gir et bedre forhold mellom service level og kapitalbinding enn en mer aggressiv økning til Variant B, som gir marginale forbedringer i tilgjengelighet med betydelig høyere binding.

Faste lead time-scenarier understreker at ledetid er en viktig operasjonell driver. Effektiv lead time på 1 dag gir klart lavere tapt etterspørsel og lavere binding enn 3–4 dagers ledetid. For TRN Ankomst er ikke bare bestillingspolicy viktig; tiden fra ankomst til salgsklart (hylleparatitet) er også en kritisk styringsvariabel. Operasjonelle forhold som ukedag, tidspunkt for mottak, sesong og utpakking/bemanning påvirker denne effektive ledetiden.

### Praktiske implikasjoner
- Redusert tom-hylle-rate kan direkte forbedre kundetilfredshet og kjøpssjanser.
- Lavere lav-hylle-rate gir bedre driftssikkerhet for kampanjer og salgsfremmende tiltak.
- Kortere effektiv lead time har høy verdi, særlig når leveringskalenderen er begrenset av faste mottaksdager.

Dette indikerer at en helhetlig forbedring bør omfatte både justering av min-/maks-policyer og tiltak for å redusere tiden fra mottak til hyllesett.

### Metodiske vurderinger
Simuleringen er bevisst holdt oversiktlig for å balansere transparens og praktisk relevans. Bruken av Poisson-fordeling for daglig etterspørsel er faglig begrunnet for relativt lave og uavhengige salgsarrangementer, og 30 repeterte simuleringer per scenario gir robusthet mot tilfeldige variasjoner.

Samtidig innebærer modellens enkelhet noen svakheter. Modellen har ikke eksplisitt kapasitet på lagringsplass, og den antar enkelt produktfokus uten kryss-effekter mellom produkter. Dette gjør analysen mest relevant for relative policy-sammenligninger, snarere enn som en absolutt prognose for faktisk salgsvolum.

### Begrensninger og videre forskning
- **Simulerte data:** Modellens parametere bygger på antakelser og fagkunnskap. Reelle driftsdata ville styrket konklusjonen, særlig for sesongvariasjoner og kampanjetrykk.
- **Sesong og kampanjer:** Kampanjedager er delvis modellert, men helårsperspektivet mangler ekstreme perioder som sommerferie og julehandel.
- **Demand censoring:** Tapte etterspørselsberegninger antar at etterspørsel som ikke tilfredsstilles, representerer direkte tap. I praksis kan kunder velge alternative varer eller utsette kjøp.
- **Overførbarhet:** Funnene er mest direkte anvendelige i lignende flyplass- og terminalmiljøer med begrenset plass og faste mottaksdager.

Videre forskning kan med fordel utforske dynamiske min-/maks-policyer basert på prognoser, multi-produkt optimering med plassbegrensning, og mer avanserte modeller for kundeadferd ved tomme hyller.

## Konklusjon og anbefalinger

### Svar på problemstillingen
Ja. Analysen viser at en moderat økning i min og maks gir lavere tom-hylle-rate og lav-hylle-rate med en akseptabel økning i lagerbinding. **Variant A (+1 til min og maks)** fremstår som det mest robuste alternativet fordi den gir betydelig tilgjengelighetsgevinst uten uforholdsmessig økt lagerbinding.

### Hovedfunn
Daglig min–maks-policy i baseline gir omfattende tapt etterspørsel (34.4 %) på grunn av hyppige tom-hylle-perioder. En moderat løft av min-/maks-nivåene reduserer dette til 25.6 % og bør vurderes som første tiltak.

### Anbefalinger
1. **Implementer Variant A** (+1 til min og maks) som første steg for de 7 produktene.
2. **Overvåk KPI-er:** mål tom-hylle-rate, lav-hylle-rate og lagerbinding for å validere modellen mot faktiske data.
3. **Vurder Variant B** for produkter med stabilt høyt volum eller ved kampanjefasede varer.
4. **Fokuser på effektiv lead time:** tiltak som raskere utpakking og mer tilgjengelig bemanning kan gi stor effekt.
5. **Utvikle dynamisk policy:** bruk data og prognoser til å justere min/max i perioder med høy etterspørsel.

### Bidrag og overførbarhet
Studien viser at kvantitativ simulering kan gi nyttige beslutningsgrunnlag i retail når reelle data er begrenset. Metoden er særlig relevant for butikker med begrenset lagerplass, høyt besøksvolum og faste mottaksdager.

Resultatene understreker at både min/max-policy og effektiv ledetid må vurderes parallelt for å oppnå en god tjenestenivåbalanse.

## Appendiks A: Reproduserbarhet og kjøring av simulering
Koden som ligger i prosjektmappen kan kjøres for å gjenskape simuleringene og statistikkene som presenteres i denne rapporten. Nedenfor er korte instruksjoner for reproduksjon og en forklaring av viktige variabler.

- Systemkrav: Python 3.8+ (ingen tredjepartsbiblioteker nødvendig).
- Kjøring (fra prosjektrot):

```bash
py simulate_extended_tests.py
```

- Beskrivelse: Scriptet kjører flere repeterte simuleringer for hvert scenario, aggregerer resultater og skriver dem til konsoll. Hovedinnstillinger finnes i toppen av `simulate_extended_tests.py`:
	- `REPEATS`: antall repeterte simuleringer
	- `PRODUCTS`: produktspesifikasjoner (min, maks)
	- `SENSITIVITY_SCENARIOS`: etterspørselsparametre for sensitivitetsanalyser

- Reproduserbarhet: scriptet bruker en deterministisk seed (`BASE_SEED`) kombinert med `REPEATS` for å sikre reproduserbare kjøringer.

Jeg kan også legge til en `README.md` i prosjektroten med disse instruksjonene hvis du ønsker.

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