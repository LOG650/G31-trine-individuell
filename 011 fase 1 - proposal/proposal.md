# Proposal LOG650

**Gruppemedlemmer:**
Trine Østengen

**Område:**
Lagerstyring (inventory management) og etterfyllingsstyring i retail. Prosjektet undersøker hvordan min–maks-parametere påvirker tilgjengelighet i butikk, og bruker en enkel kvantitativ simulering for å teste forbedringer.

**Bedrift (valgbart):**
Travel Retail Norway (TRN), avgrenset til Ankomst-butikken på Oslo Lufthavn. Casebeskrivelsen bygger på kjent praksis fra drift: min–maks styrer automatisk bestilling, bestillinger kommer i multipler av 3, og total etterfyllingstid fra automatisk bestilling til vare er på hylle er normalt 1–4 døgn. Varelevering skjer alle dager unntatt tirsdag.

**Problemstilling:**
Hvilke min–maks-parametere gir lavest tom-hylle-rate og lav-hylle-rate for utvalgte skjønnhetsprodukter i TRN Ankomst, og hva er konsekvensen av alternative min–maks-nivåer for lagerbinding?

**Data:**
Reelle interne data antas å være vanskelig å hente ut i prosjektperioden på grunn av systemendringer. Prosjektet vil derfor bruke simulerte data som representerer realistisk etterspørsel og etterfyllingsflyt i TRN Ankomst. Simuleringen parameteriseres med kjente driftsforhold: bestillingskvant i multipler av 3, leveringskalender med levering alle dager unntatt tirsdag, og total etterfyllingstid 1–4 døgn (modellert som scenarier).

**Beslutningsvariabler:**
Min- og maks-nivå per vare for et avgrenset utvalg skjønnhetsprodukter (for eksempel 20–30 varer innen hudpleie og sminke).

**Målfunksjon:**
Målet er å redusere tom-hylle-rate og lav-hylle-rate (bedre tilgjengelighet) med minst mulig økning i lagerbinding. Beste løsning er den som gir lavest tom-hylle-rate og lav-hylle-rate, med minst mulig ekstra beholdning.

**Avgrensninger:**
Prosjektet avgrenses til TRN Ankomst og et begrenset utvalg skjønnhetsprodukter. Prosjektet modellerer ikke prisendringer, kampanjer, endringer i butikkplanogram eller den nye sesongmekanismen som nylig er innført. Prosjektet estimerer ikke tapt salg direkte på kundenivå, men bruker tom hylle og lav hylle som proxy for tilgjengelighetsbegrenset salg.
