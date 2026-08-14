# Herkomst en rechten

## Code
De code in deze repository staat onder de **MIT-licentie** (zie `LICENSE`).
Je mag ze gebruiken, aanpassen, doorgeven en zelfs commercieel inzetten,
zolang de copyrightvermelding en de licentietekst meegaan.

## Merken en logo's — niet onder de MIT-licentie
Een softwarelicentie draagt geen merkrechten over. Dat is gebruikelijk en staat
ook zo in de licenties van grote projecten. Concreet gaat het hier om twee
verschillende merken van twee verschillende eigenaars:

**SHiftEDMake** — `public/shiftedmake-logo.png`, het woordmerk SHiftEDMake en
de baseline "van Droom naar Werkelijkheid" zijn ontworpen door en eigendom van
Serge Hanssens (SHiftEDMake).

**Fri3d Camp** — het **vossenlogo en woordmerk** (`public/fri3d-logo.png`,
`public/icon.svg`, `public/icon-*.png`) en de **terreinkaart**
(`public/kaart.png`) zijn het beeldmerk en het materiaal van Fri3d Camp, niet
van SHiftEDMake. `fri3d-logo.png` is het originele logo, enkel vrijgemaakt van
zijn zwarte achtergrond. De app-iconen zijn daar rechtstreeks uit gemaakt: de
PNG's zijn een uitsnede van het vossenkopje, en `icon.svg` is datzelfde beeld
overgetrokken tot vectorpaden zodat het op elk formaat scherp blijft. Er is dus
niets nagetekend of benaderd. Ze worden hier gebruikt met medeweten en
toestemming van de organisatie: de maker van deze app zit zelf mee in het
Fri3d-team.

Die toestemming geldt voor dit project. Fork je het voor een ander evenement,
dan staat dat daar los van — vervang in dat geval de iconen en de kaart door je
eigen beeldmateriaal.

**De vormgeving is die van SHiftEDMake, niet van Fri3d Camp.** Sinds 1.1.0
gebruikt de app geen enkele kleur of vormtaal uit de huisstijl van Fri3d meer.
Wat er van hen in zit, is beeldmateriaal en programmadata — hierboven benoemd —
en niets anders. Zo blijft duidelijk dat dit een project ernaast is en niet de
officiële app van het kamp.

Wat mag zonder te vragen:
- de app draaien, forken en aanpassen voor je eigen gezin of organisatie;
- het logo laten staan als bronvermelding, zoals het in de voettekst staat.

Wat niet mag zonder schriftelijke toestemming:
- het logo of de naam SHiftEDMake gebruiken als merk voor jouw eigen product,
  dienst of fork, of op een manier die suggereert dat SHiftEDMake jouw versie
  maakte of goedkeurde.

Fork je dit project en breng je het onder een eigen naam uit? Vervang dan
`icon.svg`, `icon-*.png` en `shiftedmake-logo.png` door je eigen beeldmerk en
pas de voettekst in `build/app.template.html` aan. Alles blijft dan werken.

## Programmagegevens
De sessiegegevens komen van **Fri3d Camp** via de publieke Pretalx-export
(`https://content.fri3d.be/`). Titels, beschrijvingen en sprekersinformatie
blijven eigendom van Fri3d Camp en de individuele sprekers. Deze app toont die
gegevens en linkt telkens terug naar de originele sessiepagina; ze vervangt de
officiële site niet en is er een aanvulling op. Voor hergebruik buiten deze
context: vraag het aan Fri3d Camp.

### Terreinkaart
`public/kaart.png` is de officiële terreinkaart van Fri3d Camp, gebruikt met
toestemming. De app toont ze ongewijzigd en kleurt alleen bij het bekijken één
icoon rood, in de browser van de gebruiker; er wordt geen aangepaste versie
verspreid.

Voor een ander evenement: vervang `kaart.png` en pas `build/mapcoords.json` aan.
Dat bestand bevat enkel coördinaten, geen beeldmateriaal.

### Schermafbeeldingen
`docs/screenshots/` bevat afbeeldingen van de app in gebruik, enkel als
illustratie bij de README en de handleiding. Daarop staan onvermijdelijk het
vossenlogo, de terreinkaart en fragmenten van het programma van Fri3d Camp; die
blijven van hen, onder dezelfde toestemming als hierboven. De getoonde namen en
planningen zijn verzonnen — er staan geen gegevens van echte deelnemers op.

## Diensten van derden
- **Supabase** — optioneel, voor synchronisatie tussen toestellen. Je gebruikt
  je eigen project; er loopt niets via SHiftEDMake.
- **AllOrigins** (`api.allorigins.win`) — enkel als noodoplossing wanneer de
  browser het programma niet rechtstreeks bij Fri3d mag ophalen. Er gaat geen
  persoonlijke informatie doorheen, alleen de publieke programma-URL.

## Lettertypen
`public/fonts/` bevat **Space Grotesk** en **Inter**, beide onder de
[SIL Open Font License 1.1](https://openfontlicense.org). Ze zijn meegeleverd
zodat de app ook offline haar uiterlijk behoudt; de OFL staat dat uitdrukkelijk
toe zolang de bestanden niet los verkocht worden.

Er zit geen tracking, geen analytics en geen advertentiecode in deze app.
