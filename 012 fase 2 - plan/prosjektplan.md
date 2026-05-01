# Prosjektstyringsplan for Optimalt lagernivå TRN Ankomst

**Dato:** 2026-03-17

**Utarbeidet av:**
Trine Østengen

**Autorisert av:**
[Sponsor]

## Innhold

- Sammendrag
- Behov
- Sponsor
- Kunde
- Forretningscase
- Alternativer
- Forutsetninger
- Gevinster
- Kostnader
- Analyse
- Omfang
- Mål
- Krav
- Løsning
- Arbeidsnedbrytningsstruktur
- Omfangsverifikasjon
- Fremdrift
- Avhengighetsdiagram
- Gantt-plan
- Kritisk linje
- Milepæler
- Budsjett
- Kostnadsfordeling per leveranse
- Ressurskostnader
- Kostnadskurve
- Risiko
- Prosess for risikostyring
- Risikoregister
- Endringskontrollprosess

## Sammendrag

Dette dokumentet utgjør prosjektstyringsplanen for prosjektet «Optimalt lagernivå i TRN Ankomst». Planen beskriver hvordan prosjektet skal gjennomføres, inkludert baselines for omfang, fremdrift og risiko. Prosjektet gjennomføres som et studentprosjekt og bygger på en kvantitativ simulering av min–maks-styrt etterfylling.

Prosjektet er planlagt slik at det kan gjennomføres uten konfidensielle bedriftsdata ved å bruke simulerte data basert på kjente driftsforhold (bestillingskvant i multipler av 3, leveringskalender uten mottak på tirsdag, og total etterfyllingstid 1–4 døgn som scenarier).

Dette er et levende dokument og kan oppdateres ved behov gjennom prosjektperioden, for eksempel dersom det blir nødvendig å justere omfang, antakelser eller tidsplan.

## Behov

Prosjektet svarer på et praktisk behov knyttet til varetilgjengelighet i butikk når min–maks-nivåer er satt lavt samtidig som etterfyllingstiden er flere døgn. I slike situasjoner øker risikoen for tom hylle og lav hylle, noe som kan begrense salg og redusere muligheten for salgsøkende tiltak (for eksempel ekstra fronting og flere plasseringer). Formålet er å undersøke hvilke endringer i min–maks som kan redusere tom-hylle-rate og lav-hylle-rate uten uforholdsmessig økning i lagerbinding.

## Sponsor

Prosjektet er et studentprosjekt. Faglærer/emneansvarlig fungerer som formell godkjenner av prosjektplan og leveranser i emnet. Jeg (Trine Østengen) er prosjektleder og ansvarlig for planlegging, gjennomføring og leveranser.

## Kunde

Kunde/sluttbruker forstås som prosjektets mottaker i emnesammenheng (LOG650). Resultatene er ment å være relevante for butikkdrift i TRN Ankomst, men prosjektet gjennomføres uten involvering fra bedriften og uten bruk av konfidensielle bedriftsdata.

## Forretningscase

Forretningscaset i dette prosjektet handler om å undersøke en konkret trade-off i lagerstyring: lavere tom-hylle-rate og lav-hylle-rate krever ofte høyere beholdning, som igjen øker lagerbinding. Prosjektet er begrunnet fordi selv små forbedringer i tilgjengelighet kan ha tydelig effekt i butikkdrift, både ved å redusere perioder uten vare på hylle og ved å gjøre det mulig å gjennomføre salgsaktiviteter som fronting og ekstra plasseringer. Siden prosjektet gjennomføres med simulerte data, er kostnaden i hovedsak tidsbruk, og risikoen knyttet til konfidensialitet er lav.

## Alternativer

Følgende alternativer ble vurdert:

- a) Status quo: beholde dagens min–maks-nivåer og praksis. Dette ble forkastet som “løsning” fordi dagens lave min-nivåer i kombinasjon med etterfyllingstid på flere døgn øker sannsynligheten for tom og lav hylle for mange varer.
- b) Justere min–maks basert på en enkel kvantitativ modell (simulering). Dette ble valgt fordi det er gjennomførbart innenfor prosjektperioden og gir et tydelig grunnlag for å sammenligne ulike min–maks-innstillinger på KPI-er.
- c) Mer avansert løsning (for eksempel full prognosemodell med eksterne forklaringsvariabler, optimalisering på tvers av flere butikker, eller bruk av reelle interne data med tett dialog med bedriften). Dette ble vurdert som for omfattende og mindre realistisk innen tidsrammen, spesielt fordi prosjektet er avgrenset til å kunne gjennomføres uten tilgang til konfidensielle data.

## Forutsetninger

Forretningscaset bygger på følgende forutsetninger:

- Min–maks styrer automatisk etterfylling, og bestillinger kommer i multipler av 3.
- Det er ikke varelevering på tirsdager.
- Total etterfyllingstid fra automatisk bestilling til varen er på hylle er 1–4 døgn og behandles som scenarier i analysen.
- Etterspørsel representeres ved simulerte daglige uttak med variasjon og enkelte topper.
- Prosjektet bruker tom-hylle-rate og lav-hylle-rate som proxy for tilgjengelighetsbegrenset salg, og estimerer ikke tapt salg direkte på kundenivå.

## Gevinster

Forventede gevinster er:

- Økt salgsutnyttelse og redusert sannsynlighet for tapt salg som følge av tom hylle eller svært lav hylle. Når tilgjengeligheten øker, blir det enklere å gjennomføre mersalg, og å møte situasjoner der flere kunder ønsker samme vare samtidig.
- Bedre grunnlag for å planlegge og gjennomføre salgsaktiviteter, fordi hyllen i større grad kan holdes fylt gjennom perioden.
- Reduksjon i tom-hylle-rate og lav-hylle-rate for utvalgte varer (bedre tilgjengelighet/opplevd kvalitet i butikk).
- Mer treffsikre min–maks-innstillinger for varer med ujevnt uttak og risiko for utsolgt før påfyll.
- Tydeliggjøring av trade-off mellom tilgjengelighet og lagerbinding, som kan brukes til å diskutere akseptable terskler og prioritering av varer.

## Kostnader

Prosjektet gjennomføres som et studentprosjekt og har derfor ikke økonomiske kostnader for en virksomhet. Kostnaden består hovedsakelig av tidsbruk til planlegging, utvikling av simulering, gjennomføring av eksperimenter og rapportering.

## Analyse

ROI/BCR/NPV beregnes ikke fordi prosjektet ikke omfatter budsjett eller kostnadsestimering. Analysen vurderer derfor nytte basert på målbare driftsindikatorer: tom-hylle-rate, lav-hylle-rate og lagerbinding. Prosjektet anses som relevant fordi forbedret tilgjengelighet forventes å gi høyere salgsutnyttelse (redusert sannsynlighet for tapt salg) og bedre forutsetninger for salgsaktiviteter, samtidig som lagerbinding holdes innenfor en definert terskel. Leveranse og “kost” i prosjektet er i praksis knyttet til tidsfristen og gjennomføring av planlagte aktiviteter.

## Omfang

Denne seksjonen beskriver omfanget for prosjektet «Optimalt lagernivå i TRN Ankomst». Omfanget inkluderer prosjektmål, forutsetninger, begrensninger, krav og WBS. Omfangsdefinisjonen er grunnlaget for videre planlegging av fremdrift og risiko.

Prosjektet gjennomføres som et studentprosjekt uten budsjett, og omfangsstyring knyttes derfor primært til leveranser, tid og faglige krav. Endringer i omfang håndteres ved å oppdatere prosjektstyringsplanen og Gantt-planen (baseline oppdateres ved større endringer).

## Mål

Prosjektmålet er å identifisere min–maks-parametere for et avgrenset utvalg skjønnhetsprodukter i TRN Ankomst som reduserer tom-hylle-rate og lav-hylle-rate, innenfor en akseptabel terskel for lagerbinding.

Prosjektets forutsetninger er:

- Prosjektet bruker simulerte data og kan gjennomføres uten konfidensielle bedriftsdata.
- Etterfylling følger min–maks-logikk med automatisk bestilling når beholdning er mindre enn eller lik min, og påfyll opp til maks.
- Bestillingskvant avrundes til multipler av 3.
- Leveringskalender: levering alle dager unntatt tirsdag.
- Total etterfyllingstid er 1–4 døgn og behandles som scenarier i analysen.
- Tom-hylle-rate og lav-hylle-rate brukes som indikatorer på tilgjengelighetsbegrenset salg.

Prosjektets begrensninger er:

- Omfanget avgrenses til TRN Ankomst på Oslo Lufthavn og et begrenset varesett innen hudpleie og sminke (for eksempel 20–30 varer).
- Prosjektet modellerer ikke kampanjer, prisendringer, planogramendringer eller ny sesongmekanisme.
- Prosjektet estimerer ikke tapt salg direkte på kundenivå, men bruker tom/lav hylle som proxy.
- Prosjektet gjennomføres innen tidsrammene i emnet, og planlagt fremdrift styres av Gantt-planen.

## Krav

Kravene beskriver hva prosjektet må oppfylle for å anses gjennomført.

### Funksjonelle krav (modell):

- Simuleringsmodellen skal implementere min–maks-etterfylling med bestillingskvant i multipler av 3.
- Modellen skal håndtere leveringskalender uten mottak på tirsdager.
- Modellen skal støtte lead time-scenarier fra 1 til 4 døgn.

### Krav til måling og rapportering:

- Modellen skal beregne tom-hylle-rate og lav-hylle-rate per vare og samlet.
- Modellen skal beregne lagerbinding som gjennomsnittlig beholdning i enheter (og eventuelt i kroner dersom enhetspris/standardkost brukes senere).
- Resultater skal presenteres slik at trade-off mellom tilgjengelighet og lagerbinding blir tydelig.

### Krav til analyse:

- Prosjektet skal sammenligne baseline (dagens min–maks-praksis) med et begrenset antall alternative min–maks-oppsett (for eksempel tre varianter).
- Analysen skal håndtere trade-off ved å innføre en terskel for akseptabel økning i lagerbinding (for eksempel maks 10 % over baseline), og deretter minimere tom-hylle-rate og lav-hylle-rate innenfor denne terskelen.

## Løsning

Løsningen som skal utvikles for å oppfylle prosjektmålet er en enkel simuleringsmodell for min–maks-styrt etterfylling i TRN Ankomst.

Modellen bruker simulerte etterspørselsdata og kjente driftsregler (bestillingskvant i multipler av 3, ingen mottak på tirsdager og total etterfyllingstid 1–4 døgn som scenarier). Løsningen skal gjøre det mulig å sammenligne dagens praksis (baseline) med et begrenset antall alternative min–maks-oppsett, og måle effekt på tom-hylle-rate, lav-hylle-rate og lagerbinding.

Løsningsdefinisjonen er beskrevet på et nivå som er tilstrekkelig for å planlegge prosjektets aktiviteter og milepæler i MS Project og gjennomføre prosjektet innenfor emnets tidsrammer. Detaljer som valg av endelige parameterverdier, utforming av etterspørselsgenerator og format for resultatpresentasjon videreutvikles i gjennomføringsfasen.

### Viktigste leveranser i løsningen:

- Simuleringsmodell (kode) som implementerer min–maks, bestillingskvant i multipler av 3, leveringskalender uten mottak på tirsdager og lead time-scenarier (1–4 døgn).
- Baseline og alternative min–maks-eksperimenter (for eksempel tre varianter) med dokumenterte antakelser.
- Resultater (tabeller/figurer) med tom-hylle-rate, lav-hylle-rate og lagerbinding, samt sammenligning mellom baseline og varianter.
- Kort analyse og anbefaling av min–maks-parametere innenfor en akseptabel terskel for lagerbinding.

## Arbeidsnedbrytningsstruktur

WBS utgjør baselinen for prosjektets omfang og dokumenterer alle hovedleveranser og arbeidspakker.

## Omfangsverifikasjon

Leveransene verifiseres gjennom egenkontroll og enkle, etterprøvbare tester. Siden prosjektet gjennomføres alene, erstattes formell QA-organisasjon med en strukturert verifikasjonsrutine der kravene sjekkes før leveranser regnes som ferdige.

Verifikasjon gjennomføres på følgende måter:

- Inspeksjon: gjennomgang av antakelser, parametre og KPI-definisjoner.
- Demonstrasjon: kjøre simuleringen på et lite datasett og vise at logikken oppfører seg som forventet.
- Analyse/test: sanity checks på forventede sammenhenger.

Sanity checks (minimum):

- Når min og/eller maks økes, skal tom-hylle-rate normalt gå ned.
- Når lead time økes (1 til 4 døgn), skal tom-hylle-rate normalt gå opp.
- Når “ingen mottak tirsdag” fjernes, skal tilgjengelighet normalt bli bedre enn i baseline.

En leveranse regnes som verifisert når simuleringen kjører uten feil, KPI-ene beregnes konsistent, og baseline og alternative scenarier kan reproduseres og sammenlignes på en tydelig måte. Eventuelle avvik dokumenteres og rettes før leveransen inngår i sluttmaterialet.

## Fremdrift

Denne seksjonen dokumenterer fremdriftsbaselinen for prosjektet. Arbeidet som er definert i WBS er lagt inn i Gantt og mappet mot kalenderen for å fastslå rekkefølge, varighet, milepæler og prosjektets planlagte sluttdato. Gantt-planen etableres som baseline etter godkjenning av fase 2, slik at fremdrift og avvik kan følges opp underveis.

Siden prosjektet gjennomføres som et prosjekt uten sponsor/kunde i organisasjonsforstand, følges fremdrift opp mot frister i emnet og egen plan. Status vurderes ukentlig ved å sammenligne planlagt fremdrift i Gantt med faktisk fremdrift, og eventuelle endringer håndteres ved å oppdatere planen.

## Avhengighetsdiagram

Avhengighetsdiagrammet beskriver gjennomføringslogikken i prosjektet, altså rekkefølgen mellom hovedleveransene. I dette prosjektet følger logikken en naturlig kjede fra spesifisering til utvikling, testing, eksperimenter og rapportering.

Overordnet avhengighetslogikk:

1. Oppstart og planlegging må være ferdig før videre arbeid låses som baseline.
2. Spesifisering av KPI-er, antakelser, varesett og baseline må være ferdig før datagrunnlag og modell implementeres.
3. Datagrunnlag (simulert etterspørsel) må være på plass før simuleringen kan kjøres på baseline og varianter.
4. Simuleringsmodell må implementeres før testing og verifikasjon.
5. Verifisert modell må være klar før eksperimenter og analyse gjennomføres.
6. Eksperimenter og analyse må være ferdig før rapportering og endelig levering.

## Gantt-plan

Gantt-planen legges ved i en annen fil.

## Kritisk linje

Kritisk linje er synlig i vedlagt Gantt-plan.
Siden dette er et studentprosjekt og flere varigheter i planleggingsfasen er grove estimater, kan kritisk linje endre seg når modellen utvikles og aktivitetsvarigheter blir mer realistiske. Ved oppdateringer av planen vil kritisk linje brukes som styringsverktøy ved at aktiviteter uten slakk prioriteres, og arbeid med slakk kan justeres dersom det oppstår forsinkelser på kritiske aktiviteter.

I tidlig fase vil flere aktiviteter fremstå med slakk fordi varigheter er estimert konservativt og fordi planen er lagt opp med buffer før sluttdato, men kritiske aktiviteter fremgår likevel av Gantt-planen og vil bli fulgt opp gjennom prosjektperioden.

## Milepæler

Prosjektets milepæler markerer hendelser der sentrale arbeidselementer er ferdigstilt, og de brukes som styringspunkter for å følge fremdrift mot sluttdato 1. juni. I et studentprosjekt er milepælene knyttet til leveranser i emnet og til de viktigste faglige “portene” i prosjektet (plan ferdig, modell ferdig, analyse ferdig, rapport levert).

Følgende milepæler ble definert i emnet/prosjektopplegget:

- Fase 2 levert– 17. mars 2026
- Endelig levering – 31. mai 2026

Øvrige milepæler er valgt for å markere viktige oppnådde punkter i prosjektet:

- Prosjektplan godkjent
- Modell ferdig
- Modell verifisert
- Eksperimenter ferdige
- Analyse ferdig
- Rapportutkast ferdig

## Risiko

Denne seksjonen beskriver hvordan risiko håndteres i prosjektet og viser risikoregisteret som baseline. Prosjektet er et studentprosjekt uten budsjett i kroner, og risiko vurderes derfor primært med hensyn til konsekvens for tid, kvalitet og gjennomførbarhet. Eventuelle bufferbehov håndteres gjennom realistiske varighetsestimater og noe slakk frem mot sluttdato 31. mai.

## Prosess for risikostyring

Risiko identifiseres i planleggingsfasen basert på prosjektets avgrensning, antakelser og erfaring fra lignende oppgaver (modellering, datagrunnlag, tidsfrister). Risikoregisteret oppdateres ved behov gjennom prosjektperioden. Risiko gjennomgås ukentlig, og ved tegn til at en risiko er i ferd med å utløses, prioriteres tiltak først på aktiviteter som påvirker kritisk linje.

## Risikoregister

| ID | Risiko | Sannsynlighet | Konsekvens | Tiltak (forebyggende) | Beredskap (hvis det skjer) |
|---|---|---|---|---|---|
| R1 | Manglende tilgang til interne data | Høy | Høy | Bruke simulerte data og dokumenterte antakelser. Avgrense varesett og scenarier. | Forenkle etterspørselsmodell og redusere antall varianter/scenarier dersom tidsbruk øker. |
| R2 | For stort omfang (for mange varer/scenarier/varianter) | Middels | Høy | Holde fast på avgrensning (20–30 varer, tre min–maks-varianter, lead time 1–4). | Redusere til færre varer (f.eks. 10–15) eller færre varianter (f.eks. 2) uten å endre hovedpoenget. |
| R3 | Feil/bug i simuleringen gir misvisende resultater | Middels | Høy | Test på liten dataserie. Sanity checks: min/maks opp → bedre tilgjengelighet, lead time opp → dårligere tilgjengelighet. | Fryse funksjonalitet til en enklere modell (kun min–maks + ett lead time-scenario) for å sikre leverbarhet. |
| R4 | Urealistisk etterspørselsmodell (simulert data blir “for pen” eller for ekstrem) | Middels | Middels | Bruke minst to etterspørselstyper (normal + spikes). Sjekke nivå/variasjon mot rimelig butikklogikk. | Dokumentere begrensningen tydelig og fokusere på relative effekter mellom policy-varianter. |
| R5 | Tidsmangel / uforutsette forsinkelser | Høy | Høy | Prioritere fungerende baseline + få varianter. Starte rapport tidlig med fast struktur. | Kutte ekstra analyser og levere minimumsløsning med klare resultater og god dokumentasjon. |
| R6 | Uklar trade-off gjør det vanskelig å konkludere | Middels | Middels | Bruke terskeltilnærming (f.eks. maks 10 % økning i lagerbinding fra baseline) og rangere løsninger innenfor terskelen. | Presentere to anbefalinger (beste tilgjengelighet vs lavest binding) og diskutere valg/implikasjoner. |

## Endringskontrollprosess

Beslutninger om endringer i omfang, tid eller risiko dokumenteres i prosjektstyringsplanen og godkjennes av prosjektleder. Endringer vurderes på bakgrunn av konsekvens for planlagt fremdrift og målhierarki.
