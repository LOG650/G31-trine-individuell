# Vedlegg 4: Risikoanalyse og WBS

## Risikoanalyse

### Identifiserte risikoer

| Risiko ID | Beskrivelse | Kategori | Sannsynlighet | Konsekvens | Tiltak |
|-----------|-------------|----------|---------------|-------------|---------|
| R1 | Utilstrekkelig datagrunnlag for simulering | Teknisk | Høy | Kan ikke validere resultater | Bruk realistiske simulerte data basert på kjente driftsforhold |
| R2 | Teknisk feil i simuleringskode | Teknisk | Middels | Feilaktige resultater | Grundig testing, validering og kode review |
| R3 | Manglende tilbakemelding fra peer review | Prosess | Middels | Svakere endelig rapport | Planlegg peer review tidlig, send utkast 30. april |
| R4 | Tidsmangel før innlevering | Tidsmessig | Lav | Ufullstendig rapport | Detaljert tidsplan, ukentlige milepæler |
| R5 | Endringer i prosjektomfang | Omfang | Lav | Forsinkelser | Streng endringskontroll |

### Risikoregister status
- **R1:** Løst - Simuleringsmodell bruker realistiske parametere
- **R2:** Løst - Kode testet og valideres mot kjente scenarier
- **R3:** Aktiv - Krever oppfølging i peer review periode
- **R4:** Løst - Detaljert planlegging og fremdrift
- **R5:** Løst - Omfang fastsatt og godkjent

### Risikomonitorering
- Ukentlige statusoppdateringer
- Risiko vurderes på nytt ved hver faseovergang
- Escalasjonsprosedyre: Veileder kontaktes ved høy risiko

## Arbeidsnedbrytningsstruktur (WBS)

### Fase 1: Problemidentifikasjon og planlegging (15-17 mars)
```
1.0 Problemidentifikasjon og planlegging
   1.1 Litteraturstudie og teorigrunnlag
   1.2 Problemformulering og forskningsspørsmål
   1.3 Utvikling av prosjektplan og WBS
   1.4 Risikoanalyse og avgrensninger
   1.5 Milepæler og fremdriftsplan
```

### Fase 2: Metodeutvikling (18 mars - 15 april)
```
2.0 Metodeutvikling
   2.1 Design av simuleringsmodell
   2.2 Utvikling av datagrunnlag (simulert)
   2.3 Validering av modellparametere
   2.4 Testing av simuleringslogikk
```

### Fase 3: Gjennomføring og analyse (16-30 april)
```
3.0 Gjennomføring og analyse
   3.1 Implementering av simuleringskode
   3.2 Kjøring av simuleringer (3 scenarier)
   3.3 Analyse av resultater
   3.4 Validering av funn
   3.5 Forberedelse til rapportering
```

### Fase 4: Rapportering og avslutning (1-31 mai)
```
4.0 Rapportering og avslutning
   4.1 Skriving av komplett rapport
   4.2 Peer review og tilbakemeldinger
   4.3 Revisjon basert på tilbakemeldinger
   4.4 Endelig rapport og presentasjon
   4.5 Prosjektavslutning og dokumentasjon
```

### Ressursallokering per fase
- **Fase 1:** 20 timer (planlegging og research)
- **Fase 2:** 30 timer (metodeutvikling)
- **Fase 3:** 40 timer (implementering og analyse)
- **Fase 4:** 30 timer (rapportering)

### Avhengigheter
- Fase 2 avhenger av Fase 1 (godkjent plan)
- Fase 3 avhenger av Fase 2 (ferdig metode)
- Fase 4 avhenger av Fase 3 (resultater)
- Peer review (uke 18-19) er kritisk sti for Fase 4

### Kvalitetssikring per fase
- **Fase 1:** Review av veileder
- **Fase 2:** Teknisk validering
- **Fase 3:** Resultatverifisering
- **Fase 4:** Peer review og fagfellevurdering