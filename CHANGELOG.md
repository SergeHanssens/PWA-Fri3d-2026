# Wijzigingen

## 1.2.5 — augustus 2026

- **Het app-icoon klopt nu met het echte logo.** De iconen waren nagetekend, en
  dat zag je: de oren stonden anders en de lijnen waren dikker. Ze zijn nu
  rechtstreeks uit `fri3d-logo.png` gemaakt — de PNG's als uitsnede, de SVG
  overgetrokken tot vectorpaden. De achtergrond is de navy van de app in plaats
  van zwart.
- De offline cache kreeg een nieuw nummer, zodat het oude icoon er zeker uit gaat.

## 1.2.4 — augustus 2026

Namen uit de groep kwamen nog steeds niet op je scherm. Twee oorzaken:

- **De naam werd alleen overgenomen als de planning in de database nieuwer was
  dan die op het toestel.** Dat is ze niet wanneer beide van dezelfde bewerking
  afstammen — dan is ze even oud, en bleef de ingebouwde naam staan. Toont een
  toestel voor een persoon nog de fabrieksnaam, dan wint de naam uit de groep nu
  altijd.
- **Een gewijzigde naam werd wel bewaard, maar het scherm niet vernieuwd.** Je
  zag ze dus pas na een herlaadbeurt. De app tekent nu ook opnieuw wanneer enkel
  een naam of avatar veranderde.

## 1.2.3 — augustus 2026

- **Een potloodje bij elke persoon.** Tot nu kon je alleen bewerken wie je op dat
  moment zélf was: om je kind te hernoemen moest je eerst je kind worden. In het
  scherm *Wie ben je?* staat nu bij elke persoon een potloodje dat rechtstreeks
  naam en avatar opent, zonder van identiteit te wisselen. Na het bewaren kom je
  terug in de lijst, zodat je ze na elkaar kan afgaan.
- Onderaan staat het **versienummer**. Zonder dat is niet na te gaan of een
  toestel de nieuwste versie al binnen heeft.

## 1.2.2 — augustus 2026

Namen en avatars komen eindelijk mee met de synchronisatie.

- **Namen die je op één toestel aanpaste, kwamen nooit bij de rest terecht.** Ze
  werden wél netjes weggeschreven naar je eigen Supabase, maar bij het ophalen
  vroeg de app alleen `person, add, rm, ts` op — dus zonder `label`, `avatar` en
  `deleted`. Die drie kolommen worden nu mee opgehaald. Bestond je groep al vóór
  1.1.0, dan verschijnen je eigen namen en avatars vanzelf weer, ook al staan ze
  in de database nog onder de oude persoonssleutels.
- Om dezelfde reden stond een persoon die je op één toestel verwijderde er op het
  volgende gewoon weer bij. Ook opgelost.

## 1.2.1 — augustus 2026

Herstel: lege lijsten na de hernoeming van 1.1.0.

- **Wie de app al eens geopend had, zag al zijn lijsten op nul staan.** De
  sessies worden lokaal bewaard om programmawijzigingen bij te houden, en de
  labels die er bij het bouwen aan hingen bleven daarin bevroren op de oude
  persoonssleutels. Labels, leeftijd en de praktische velden komen nu altijd
  opnieuw uit de ingebouwde data. Er ging niets verloren: de planningen stonden
  er nog, ze werden alleen nergens meer aan gekoppeld.
- Het vossenlogo in de voettekst stond in kampvuurmodus op een crèmekleurige
  plaat, waardoor het bijna onzichtbaar werd. Die plaat is nu in beide standen
  even donker.
- De tien onderdelen van het tabblad Info zijn **uitklapbaar**: je krijgt eerst
  het overzicht, en klapt open wat je wil lezen. Het luidsprekertje staat in de
  titelbalk, zodat je een onderdeel kan laten voorlezen zonder het te openen —
  wie laat voorlezen scrollt niet graag. Tijdens het voorlezen klapt het blok
  vanzelf open om mee te lezen.

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
- Bovenaan het tabblad staat tot wanneer de informatie loopt en waarop ze
  gebaseerd is, met de melding dat een nieuwere mail altijd voorgaat. Dezelfde
  datum hoor je in de gesproken inleiding.

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
