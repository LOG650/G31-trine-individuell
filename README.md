README — LOG650: TRN Ankomst

Formål

Kort: Reproduser og forstå simuleringene og rapporten i dette prosjektet.

Viktige filer

- `014 fase 4 - report/report.md` — Offisiell rapport (bruk PDF for innlevering).
- `simulate_extended_tests.py` — Hovedsimuleringsscript (kjør for å generere resultater).
- `simulate_min_max.py`, `move_phase_files.py` — hjelpe-skript brukt i arbeid.

Krav

- Python 3.8+ (ingen tredjepartsbiblioteker nødvendig for basis-simulering, ifølge prosjektnotat).

Kjøring (fra prosjektrot)

- Kjør hovedsimuleringen:

```bash
py simulate_extended_tests.py
```

- Alternativt (Linux / macOS):

```bash
python3 simulate_extended_tests.py
```

Konfigurasjon

- `BASE_SEED` og `REPEATS` settes i toppen av `simulate_extended_tests.py`. Endre disse for å gjenskape eller variere resultatstabiliteten.
- Output-filer/mapper: sjekk scriptets `output`-variabler eller README-seksjoner i hvert script.

Generer PDF av rapporten

- Anbefalt: bruk `pandoc` for å konvertere Markdown → PDF (krever Pandoc og gjerne en LaTeX-distribusjon):

```bash
pandoc "014 fase 4 - report/report.md" -o "014 fase 4 - report/report.pdf" --from markdown --toc -V geometry:margin=1in
```

- Hvis `pandoc` ikke er tilgjengelig: åpne `report.md` i VS Code og velg "Print to PDF" eller bruk en Markdown-plugin til eksport.

Reproduserbarhet

- Rapportens simuleringer er deterministiske når `BASE_SEED` er satt og `REPEATS` er brukt (se `014 fase 4 - report/report.md`, Appendix A).

Notat om sensitiv data

- Alle data i repo er simulert; ingen konfidensiell informasjon er inkludert.

Kontakt

- For spørsmål: Forfatter — Trine Østengen (se forfatterlinje i `report.md`).
