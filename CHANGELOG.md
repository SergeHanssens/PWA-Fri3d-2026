# Wijzigingen

## 1.2.0 — augustus 2026

Een tabblad Info, zodat niemand nog in zijn mails hoeft te zoeken.

- Nieuw tabblad **Info** met tien blokken kampinformatie: aankomen en inchecken,
  brandveiligheid, stroom en daisychainen, eten en drinken, sanitair, wat je
  meeneemt, community shift, de badge, contact, en het einde op zondag.
- Elk blok heeft een eigen voorleesknop; de balk onderaan wordt *Lees info voor*
  en leest de tien blokken na elkaar, met dezelfde markering als bij de sessies.
- Vijftien links naar de echte bronnen: terreinplan, checklist, gedragscode,
  badge-documentatie, Fri3d IDE, MicroPythonOS, het volledige programma.
  Bewust géén links uit de nieuwsbrief — die lopen via een tracker en bevatten
  het e-mailadres van de ontvanger.
- De informatie zit in het bestand ingebakken, dus ze werkt ook zonder netwerk.
  Precies wanneer je ze nodig hebt: op een veld, zonder bereik.

## 1.1.0 — augustus 2026

Eigen vormgeving, en geen persoonsgegevens meer in de broncode.

- De huisstijl van Fri3d Camp is eruit. De app draagt nu enkel de vormgeving van
  SHiftEDMake: navy inkt op warm papier, paars voor selectie, teal voor
  bevestiging. Weg zijn de zwarte balken, het oranje, de mint, de diagonale
  arceringen en de harde offset-schaduw.
- De vier ingebouwde personen heten voortaan Ouder A, Ouder B, Tiener en Kind.
  De namen die je zelf invult blijven op je eigen toestel staan.
- Wie al een planning had, houdt ze: de oude persoonssleutels worden bij het
  eerste openen eenmalig omgezet, ook in de synchronisatie tussen toestellen.
- Toegankelijkheid opnieuw nagerekend en op drie plekken hersteld: de witte
  initiaal in de avatars haalde AA niet (amber bleef op 1,9:1), het rood van
  "nu bezig" zat op 4,4:1, en de kleinste labels op 3,0:1. Alles zit nu op
  minstens 4,7:1, in dagmodus én kampvuurmodus.
- Avatarinitialen komen uit alle woorden van de naam, dus Ouder A en Ouder B
  zijn uit elkaar te houden.
- Schermafbeeldingen opnieuw gemaakt in de nieuwe kleuren.

## 1.0.0 — augustus 2026
Eerste publieke versie.

- Volledig programma van Fri3d Camp 2026 (150 sessies), offline beschikbaar.
- Tabbladen per persoon, per onderwerp, per locatie, plus het volledige programma.
- Persoonlijke planning: toevoegen en weghalen per persoon, met een startvoorstel.
- Personen aanmaken, hernoemen, van avatar voorzien en verwijderen.
- Voorleesfunctie per sessie, per lijst, en optioneel voor de hele interface.
- Meldingen een instelbare tijd voor aanvang, gegroepeerd bij gelijktijdige sessies.
- Export naar `.ics` met herinneringen, voor meldingen terwijl de app dicht is.
- Uurlijkse controle op programmawijzigingen met een overzicht van wat veranderde.
- Synchronisatie tussen toestellen via een eigen Supabase-project.
- Delen zonder netwerk via een korte code of link.
- Kampvuurmodus voor 's avonds, en een leesbaarheidsstand met grotere letters.
- Handleidingen in gewone taal: `docs/START-HIER.md` om alles online te zetten
  zonder voorkennis, en `docs/GEBRUIKEN.md` voor wie de app enkel gebruikt.
- Terreinkaart die het gezochte icoon rood kleurt, op de kaart en in de legende.
- Leeftijdstabblad op basis van wat de sessies zelf vermelden.
- Apart tabblad Praktisch voor meebrengen, kosten en laptop.
- Lege lijsten zeggen nu welk filter in de weg staat, met een knop om het te wissen.
- Het Fri3d-vossenlogo opnieuw getekend na opmeting van de officiële versie, en
  daarna vervangen door het originele logo met transparante achtergrond.
- Schermafbeeldingen in de README en de gebruikershandleiding.
- Labels voor meebrengen, bijdrage en laptop, met de letterlijke zin uit de
  beschrijving en een amberkleurige rand op de kaart.
- Vormgeving die de huisstijl van Fri3d Camp en SHiftEDMake combineert;
  alle tekstcontrasten nagerekend op WCAG AA.
