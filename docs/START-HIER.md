# Start hier

Deze handleiding gaat ervan uit dat je **nog nooit** een website online hebt
gezet en dat woorden als "repo", "deployen" of "PWA" je niets zeggen. Dat hoeft
ook niet. Je hebt geen programmeerkennis nodig en je moet niets installeren op
je computer.

Reken op **twintig minuten**. Neem gerust een tas koffie.

---

## Wat ga je precies doen?

Je zet een klein programmaatje online, zodat jij en je gezin het op de gsm
kunnen openen. Meer is het niet. In drie stappen:

1. **De app online zetten** — 5 minuten. Hierna heb jij een webadres.
2. **De app op je gsm zetten** — 2 minuten per toestel.
3. *(Optioneel)* **Zorgen dat de gsm's elkaars planning zien** — 15 minuten.

Stap 3 mag je gerust overslaan. Zonder die stap werkt alles gewoon, alleen
houdt elke gsm dan zijn eigen lijstje bij.

---

## Woordenlijst

Je komt onderweg een paar termen tegen. Hier zijn ze, in gewone taal.

**App / PWA** — Een PWA is een website die zich gedraagt als een app: hij komt
met een eigen icoontje op je startscherm en werkt ook zonder internet. Je moet
er niets voor downloaden uit de Play Store of App Store.

**Netlify** — Een bedrijf dat gratis websites host. "Hosten" wil zeggen: jouw
bestanden op een computer zetten die altijd aanstaat, zodat anderen ze kunnen
openen. Vercel doet hetzelfde; je hebt er maar één nodig.

**Deployen** — Het online zetten van je bestanden. Bij Netlify is dat letterlijk
een map naar je browser slepen.

**Supabase** — Een gratis dienst die een klein stukje geheugen op het internet
voor je bijhoudt. Wij gebruiken het alleen om de planningen van de gsm's gelijk
te houden. Alleen nodig bij stap 3.

**Repo (repository)** — De map met alle bestanden van dit project. Je kan hem
downloaden als één zip-bestand; daar begint stap 1 mee.

**Zip-bestand** — Een map die is samengeperst tot één bestand. Dubbelklikken
volstaat om hem weer uit te pakken.

---

## Stap 1 — De app online zetten

**1.1 Haal de bestanden op.**
Download het zip-bestand van het project en pak het uit door erop te
dubbelklikken. Je krijgt een map met daarin onder meer een map die
**`public`** heet.

**1.2 Open de map `public`.**
Dubbelklik erop. Je ziet een tiental bestanden staan: `index.html`, `sw.js`,
`manifest.json`, enkele afbeeldingen en een map `fonts`.

> ⚠️ **Dit is de stap waar het meestal misgaat.** Straks moet je de **inhoud**
> van deze map online zetten, niet de map zelf. Denk aan een verhuisdoos: je
> zet de spullen in de kast, niet de doos.

**1.3 Ga naar de website van Netlify.**
Open [app.netlify.com/drop](https://app.netlify.com/drop) in je browser. Je ziet
een groot vlak met de tekst dat je hier bestanden kan neerzetten.

**1.4 Selecteer alle bestanden in `public`.**
Klik in de map `public` op één bestand en druk dan `Ctrl+A` (Windows) of
`Cmd+A` (Mac). Alles wordt blauw. Dat is goed.

**1.5 Sleep ze naar het vlak op Netlify.**
Houd de muisknop ingedrukt, sleep alles naar het vlak in je browser en laat los.
Je ziet een balkje vollopen.

**1.6 Wacht tot er "Site is live" staat.**
Na een halve minuut krijg je een webadres te zien, iets als
`https://vrolijke-otter-a1b2c3.netlify.app`. **Dat is jouw app.** Klik erop en
kijk of je het programma ziet staan.

> Zie je in de plaats een lijst met bestandsnamen? Dan sleepte je de map in
> plaats van de inhoud. Ga terug naar 1.4 en probeer opnieuw — je kan gewoon
> nogmaals slepen, het oude wordt vervangen.

**1.7 Geef het een fatsoenlijke naam (optioneel).**
Maak gratis een account aan bij Netlify om de naam te veranderen in iets als
`fri3d-familie-janssens.netlify.app`. Zonder account werkt het ook, maar dan
onthoud je dat rare adres maar moeilijk.

**Klaar.** Bewaar dat adres goed; je hebt het bij elke volgende stap nodig.

---

## Stap 2 — De app op de gsm zetten

Doe dit op elke telefoon die hem gaat gebruiken.

### Op Android

1. Open **Chrome**. Niet de browser die opent als je op een link in WhatsApp
   tikt — dat is een andere. Start Chrome zelf vanaf je startscherm.
2. Typ of plak het webadres van stap 1.6.
3. Wacht enkele seconden. Bovenaan verschijnt een groen **⤓**-knopje.
4. Tik erop en bevestig. Het icoontje met de vos staat nu op je startscherm.

Zie je dat knopje niet? Tik dan rechtsboven op de drie puntjes **⋮** en kies
**App installeren** of **Toevoegen aan startscherm**.

### Op iPhone of iPad

1. Open **Safari** (de blauwe kompasknop). Chrome werkt hier níét voor.
2. Ga naar het webadres.
3. Tik onderaan op het deelknopje — het vierkantje met het pijltje omhoog.
4. Scroll naar beneden en kies **Zet op beginscherm**.
5. Tik op **Voeg toe**.

> Op een iPhone werken de meldingen pas nadat je dit gedaan hebt. Open de app
> voortaan via het icoontje op je beginscherm, niet via Safari.

---

## Stap 3 — De gsm's elkaars planning laten zien (optioneel)

Zonder deze stap werkt alles, maar houdt elke telefoon zijn eigen lijstje bij.
Wil je dat wat jij aanduidt ook op de gsm van je partner of je kinderen
verschijnt, dan doe je dit één keer. **Alleen jij** hoeft dit te doen; de rest
krijgt straks gewoon een link.

**3.1 Maak een account bij Supabase.**
Ga naar [supabase.com](https://supabase.com) en klik op *Start your project*.
Aanmelden met je GitHub- of Google-account mag ook.

**3.2 Maak een nieuw project.**
Klik op **New project**. Je moet drie dingen invullen:

- **Name** — kies iets als `fri3d-familie`. Dit is enkel voor jezelf.
- **Database password** — hier vraagt hij een wachtwoord. **Wat moet je daarmee
  doen? Niets.** De app gebruikt het niet. Klik op het knopje dat er zelf één
  genereert, kopieer het naar je wachtwoordmanager of schrijf het op een papiertje,
  en vergeet het verder. Kwijt geraakt is geen ramp, je kan het later opnieuw
  instellen.
- **Region** — kies **Frankfurt (eu-central-1)**. Dat is het dichtst bij.

Klik op **Create new project** en wacht een minuutje of twee.

**3.3 Maak het geheugenplekje aan.**
Klik links in het menu op **SQL Editor**, en dan op **New query**. Je krijgt een
leeg tekstvak.

Open op je computer het bestand `supabase/schema.sql` uit de projectmap (met
Kladblok of TextEdit), selecteer alles, kopieer het, en plak het in dat tekstvak.
Klik rechtsonder op **Run**.

Er zou **Success** moeten verschijnen. Zo ja: goed bezig.

**3.4 Haal twee gegevens op.**
Klik links onderaan op het tandwiel (**Project Settings**) en dan op **API Keys**.

- Zie je een knop **Create new API keys**? Klik erop. Kopieer daarna de
  **Publishable key** — een lange sliert die begint met `sb_publishable_`.
- Zie je die knop niet? Ga dan naar het tabblad **Legacy API Keys** en kopieer
  de **anon** key, die begint met `eyJ`.

⚠️ Neem **nooit** de sleutel waar *secret* of *service_role* bij staat. Die
geeft volledige toegang en hoort niet in een app thuis.

Op dezelfde pagina staat ook de **Project URL**, iets als
`https://abcdefgh.supabase.co`. Kopieer die ook.

**3.5 Vul ze in de app in.**
Open de app op je gsm of computer. Tik bovenaan op het ronde knopje met de
poppetjes. Onder *Gezinssynchronisatie* klik je op **Instellen**. Plak de twee
gegevens in de juiste vakjes. De groepscode staat er al ingevuld — laat die
gerust staan.

Klik op **Testen**. Er hoort te verschijnen: *"Verbinding werkt."*

Klik dan op **Bewaren**.

**3.6 Nodig de anderen uit.**
Tik opnieuw op het poppetjesknopje en kies **Uitnodiging sturen**. Stuur die
link via WhatsApp naar de anderen. Zij openen hem één keer, kiezen hun naam, en
verder hoeven ze niets. Vanaf nu loopt alles vanzelf gelijk.

---

## Er ging iets mis

**Ik zie een lijst met bestandsnamen in plaats van de app.**
Je sleepte de map `public` in plaats van de bestanden erin. Sleep opnieuw, nu de
inhoud.

**Het ⤓-knopje verschijnt niet op Android.**
Meestal zit je in de browser van WhatsApp of Facebook. Kopieer de link, open
Chrome zelf en plak hem daar.

**Bovenaan staat "gezin ✗ 404".**
De app vindt het geheugenplekje niet. Meestal is stap 3.3 niet goed gelopen. Ga
terug naar de SQL Editor, plak de tekst opnieuw en klik op Run.

**Bovenaan staat "gezin ✗ 401".**
De sleutel klopt niet. Ga terug naar stap 3.4 en kopieer hem opnieuw — let op dat
je niets mist aan het begin of het einde.

**Ik krijg geen meldingen.**
Zet ze aan in de app onder *Meldingen* en geef toestemming wanneer je browser
het vraagt. Weet ook: zolang de app volledig afgesloten is, kan hij niets laten
horen. Wil je dat wel, gebruik dan **Agenda (.ics)** in hetzelfde scherm; dan
zetten de activiteiten zich in de agenda van je telefoon.

**Ik snap er niets meer van.**
Niet erg. Sla stap 3 over, gebruik alleen stap 1 en 2, en deel planningen met de
knop *Stuur mijn planning door*. Dat werkt zonder enige installatie.

---

## Wat kost dit?

Niets. Netlify en Supabase hebben allebei een gratis pakket dat ruim volstaat
voor een gezin. Er is geen creditcard nodig en er wordt niets automatisch
verlengd.

Eén detail: een gratis Supabase-project gaat in slaap na ongeveer een week
zonder gebruik. Het wordt vanzelf weer wakker zodra iemand de app opent; de
eerste keer duurt dat een paar seconden langer.

---

## En verder?

Als alles draait, lees dan [`GEBRUIKEN.md`](GEBRUIKEN.md) — daar staat hoe je de
app dagelijks gebruikt: sessies aanduiden, laten voorlezen, de kaart bekijken en
meldingen instellen. Die kan je gerust doorsturen naar de rest van het gezin.
