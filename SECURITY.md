# Beveiliging

## Ondersteunde versies

Enkel de laatste versie op `main` krijgt fixes. De app is één statisch bestand
zonder server, dus "updaten" betekent: de nieuwe `public/`-map deployen.

| Versie | Ondersteund |
|--------|-------------|
| 1.0.x  | ✅ |
| ouder  | ❌ |

## Een lek melden

Open **geen** publiek issue voor een beveiligingsprobleem.

Gebruik in plaats daarvan **Security → Report a vulnerability** op deze repo
(GitHub Private Vulnerability Reporting). Lukt dat niet, neem dan contact op via
het GitHub-profiel van [@SergeHanssens](https://github.com/SergeHanssens).

Zet er in ieder geval bij: wat er misgaat, hoe je het namaakt, en wat iemand er
in het slechtste geval mee kan. Je krijgt binnen een week een eerste antwoord.
Dit is een vrijetijdsproject — er staat geen beloning tegenover, wel een
vermelding als je dat wil.

## Wat je moet weten over de opzet

Deze dingen zijn **bewust** zo en gelden niet als lek:

- **De Supabase-tabel staat open voor lezen en schrijven** door iedereen met de
  publishable key en de groepscode. De groepscode is het enige geheim. Dat is
  een afweging voor een gezinsplanning; zet er niets in wat je niet aan een
  vreemde zou tonen. Zie de README voor hoe je het strakker zet.
- **Deel-links en uitnodigingslinks bevatten de groepscode.** Wie de link heeft,
  zit in de groep.
- **De publishable key hoort publiek te zijn.** De secret- of service_role-key
  hoort dat níét — die staat nergens in dit project en mag er ook nooit in.
- **Alles staat in de browser** (localStorage): namen, avatars en planningen
  blijven op het toestel. Er is geen account en geen wachtwoord.

Wél een lek: een manier om aan gegevens van een *andere* groep te komen, code
uit te voeren via de programmagegevens, of de service worker iets te laten
serveren wat er niet hoort.
