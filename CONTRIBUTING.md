# Meedoen

Fijn dat je wil helpen. Dit project is klein, heeft geen afhankelijkheden en
wil dat graag zo houden. Hieronder staat wat je nodig hebt om iets te
veranderen zonder dat er iets stuk gaat.

## Wat we goed kunnen gebruiken

- **Andere Pretalx-evenementen.** Werkt de build voor jouw kamp, laat het weten
  of stuur de aanpassing door.
- **Betere labels.** Sessies die geen enkel label kregen, of net een verkeerd.
- **Toegankelijkheid.** Voorleesgedrag, contrast, toetsenbordnavigatie,
  schermlezers.
- **Vertalingen.** De interface is Nederlandstalig; meertaligheid mag, zolang
  het zonder framework kan.
- **Kaartcoördinaten** voor zalen die er nog niet in staan.

## Regels van het huis

1. **Vanilla JavaScript, geen afhankelijkheden.** Geen npm, geen bundler, geen
   framework. Dat is een ontwerpkeuze, geen achterstand: de app moet als één
   bestand offline werken en doorstuurbaar blijven.
2. **Bewerk `build/app.template.html`, niet `public/index.html`.**
   `public/index.html` wordt gegenereerd. Wijzigingen die je er rechtstreeks in
   maakt, zijn weg na de volgende build.
3. **Toegankelijkheid is geen extraatje.** Tikdoelen minstens 44 px,
   tekstcontrast minstens WCAG AA, zichtbare focus, `prefers-reduced-motion`
   respecteren.
4. **Nederlands in de interface en de documentatie.** Code, variabelen en
   commitberichten mogen Engels zijn, maar Nederlands mag ook.

## Aan de slag

```bash
git clone https://github.com/SergeHanssens/PWA-Fri3d-2026.git
cd PWA-Fri3d-2026

# de app lokaal bekijken (service workers vereisen https of localhost)
cd public && python3 -m http.server 8080
```

Na een wijziging aan de template of aan de labels opnieuw bouwen:

```bash
cd build && python3 build.py
```

Dat schrijft `public/index.html`. Je hebt enkel Python 3 nodig, geen pakketten.
Het script drukt af welke sessies geen enkel label kregen — kijk die lijst na
voor je een pull request opent.

## Voor je iets instuurt

- [ ] `python3 build.py` gedraaid en `public/index.html` mee gecommit.
- [ ] De app geopend in Chrome én in Safari of Firefox.
- [ ] Getest op een smal scherm (360 px breed) en met de leesbaarheidsstand aan.
- [ ] Voorlezen werkt nog, ook op de knoppen die je aanraakte.
- [ ] Geen keys, URL's van je eigen Supabase-project of persoonlijke namen in
      de code achtergelaten.
- [ ] `CHANGELOG.md` aangevuld als het iets is wat gebruikers merken.

## Commitberichten

Kort, in de gebiedende wijs, en zeg wát er verandert voor de gebruiker:

```
Kaartknop ook tonen bij sessies zonder zaalvermelding
Leeftijdslabel niet afleiden uit "16 deelnemers"
```

Prefixen als `fix:` of `feat:` mogen, maar hoeven niet.

## Pull requests

Vertel in de beschrijving wat er verandert en waaróm, en zet er een schermafbeelding
bij als het iets visueels is. Grote wijzigingen: open eerst een issue, dan
weten we of het past voor je er tijd in steekt.

## Licentie en beeldmerken

Wat je instuurt valt onder de [MIT-licentie](LICENSE). Het SHiftEDMake-logo, het
Fri3d-vossenlogo, de terreinkaart en de programmagegevens vallen daar níét onder
— zie [`NOTICE.md`](NOTICE.md). Fork je dit onder je eigen naam, vervang dan die
beeldmerken en de voettekst.

## Gedrag

Kort samengevat: doe normaal. De volledige versie staat in
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
