# Vedlegg 1: Prosjektplan (full versjon)

## Prosjektstyringsplan for Optimalt lagernivå TRN Ankomst

**Dato:** 2026-03-17  
**Utarbeidet av:** Trine Østengen  
**Prosjektperiode:** Januar - mai 2026  

### Sammendrag
Dette dokumentet utgjør prosjektstyringsplanen for LOG650 forskningsprosjektet «Optimalt lagernivå i TRN Ankomst». Planen beskriver hvordan prosjektet skal gjennomføres, inkludert baselines for omfang, fremdrift og risiko. Prosjektet bygger på kvantitativ simulering av min–maks-styrt etterfylling for å identifisere optimale lagerparametere.

### Behov og bakgrunn
TRN Ankomst opererer med svært lave min–maks-nivåer som fører til hyppige tom-hylle-situasjoner. Dette påvirker kundetilfredshet negativt og begrenser muligheter for salgsfremmende tiltak. Prosjektet skal identifisere balanserte min–maks-parametere som forbedrer tilgjengelighet uten uforholdsmessig lagerkostnad.

### Forretningscase
- **Problem:** Høye tom-hylle-rater (anslag 20-25%) fører til tapt salg og dårlig kundeopplevelse
- **Mulighet:** Optimalisering av lagerparametere kan forbedre service level betydelig
- **Gevinst:** Bedre kundetilfredshet, økt salgspotensial, mer effektive salgsaktiviteter

### Omfang og avgrensninger
**Inkludert:**
- 7 skjønnhetsprodukter (Maskara, Dagkrem, Håndkrem, Parfyme, Eyeliner, Leppestift, Leppepomade)
- Min–maks-styring per produkt
- Simulering over 90 dager
- Tre scenarier (baseline, +1, +2 til min-maks)

**Ekskludert:**
- Reelle bedriftsdata (bruker simulering)
- Sesongvariasjoner og kampanjer
- Prisendringer og innkjøpskostnader
- Fysiske butikkendringer eller plasseringer

### Mål og suksesskriterier
1. Identifisere min–maks-parametere som reduserer tom-hylle-rate med minst 20%
2. Dokumentere trade-off mellom tilgjengelighet og lagerbinding
3. Gi praktiske anbefalinger for TRN Ankomst
4. Levere komplett vitenskapelig rapport

### Krav
- **Funksjonelle krav:** Simulering må modellere realistisk etterspørsel og leveringsprosesser
- **Tekniske krav:** Python-basert, reproduserbare resultater
- **Kvalitetskrav:** Vitenskapelig standard, komplett dokumentasjon

### Arbeidsnedbrytningsstruktur (WBS)

```
1.0 Problemidentifikasjon og planlegging
   1.1 Litteraturstudie
   1.2 Problemformulering
   1.3 Prosjektplanlegging
   1.4 Risikoanalyse

2.0 Metodeutvikling
   2.1 Simuleringsmodell design
   2.2 Datainnsamling (simulert)
   2.3 Validering av modell

3.0 Implementering og testing
   3.1 Kodeutvikling
   3.2 Simulering kjøring
   3.3 Resultatanalyse

4.0 Rapportering og presentasjon
   4.1 Rapportskriving
   4.2 Peer review
   4.3 Endelig innlevering
```

### Fremdrift og milepæler

| Milepæl | Planlagt dato | Status |
|---------|---------------|--------|
| Fase 1: Proposal | 15. mars | Fullført |
| Fase 2: Plan | 17. mars | Fullført |
| Fase 3: Review | 30. april | Fullført |
| Fase 4: Report | 31. mai | Pågår |
| Peer review | 30.april-8.mai | Kommende |
| Endelig innlevering | 31. mai | Kommende |

### Budsjett og ressurser
- **Tidsestimat:** 120 timer totalt
- **Ressurser:** Python, VS Code, simuleringsverktøy
- **Kostnader:** Ingen (studentprosjekt)

### Risikoanalyse

#### Høy risiko
| Risiko | Sannsynlighet | Konsekvens | Tiltak |
|--------|---------------|-------------|---------|
| Utilstrekkelig datagrunnlag | Høy | Kan ikke validere resultater | Bruk realistiske simulerte data |
| Teknisk feil i simulering | Middels | Feil resultater | Grundig testing og validering |
| Manglende tilbakemelding | Middels | Svakere rapport | Planlegg peer review tidlig |

#### Risikoregister
1. **Datatilgang:** Løst ved simulering
2. **Tekniske utfordringer:** Løst ved prototyping
3. **Tidsmangel:** Løst ved detaljert planlegging

### Prosess for endringskontroll
- Alle endringer må dokumenteres
- Vurdering av påvirkning på omfang, tid og kostnad
- Godkjenning av sponsor ved større endringer

### Kommunikasjonsplan
- Ukentlige oppdateringer til veileder
- Peer review periode: 30. april - 8. mai
- Endelig presentasjon: Mai 2026

### Kvalitetssikring
- Kode review og testing
- Validering av simuleringsresultater
- Fagfellevurdering (peer review)

Dette dokumentet revideres ved behov gjennom prosjektperioden.