import json, re, html

RAW = json.load(open('schedule-snapshot.json'))

# title-substring -> tags
TAG = {
 # --- Serge ---
 "Fri3d Badge - Hardware":            ["ouder-a","badge"],
 "MicroPythonOS":                     ["ouder-a","badge"],
 "BadgeHub":                          ["ouder-a","badge"],
 "Meet the Mosfet":                   ["ouder-a","badge"],
 "MeshCore dat je vergeten":          ["ouder-a","radio"],
 "PCB art, SAO":                      ["ouder-a","badge","esthetiek"],
 "Op vossenjacht met je badge":       ["ouder-a","tiener","radio","badge"],
 "Make an app or game with AI":       ["ouder-a","badge","leren"],
 "Self-hosting with docker":          ["ouder-a","selfhost"],
 "Taking back control":               ["ouder-a","radio","security"],
 "Smart Home Engineering":            ["ouder-a","selfhost","badge"],
 "Geen batterij, toch slim":          ["ouder-a","selfhost"],
 "Opname podcast Home Assistant":     ["ouder-a","selfhost"],
 "Capaciteitstarief beperken":        ["ouder-a","selfhost"],
 "Fri3d Badge - Achter de schermen":  ["ouder-a","badge"],
 "Mijn data is van mij":              ["ouder-a","selfhost","security"],
 "RF Hacking":                        ["ouder-a","radio"],
 "Aurora project":                    ["ouder-a","radio","weten"],
 "Nerdland Talk":                     ["ouder-a","weten"],
 "Vibe Code a game":                  ["ouder-a","leren"],
 "PCB reverse-engineering":           ["ouder-a","badge"],
 "IPv6 adoption":                     ["ouder-a","selfhost"],
 "PCB versie van een Neodome":        ["ouder-a","badge","esthetiek"],
 "rtl_433":                           ["ouder-a","radio"],
 "Hoe herstel je oude computers":     ["ouder-a","badge"],
 "OpenStreetmap voor beginners":      ["ouder-a","selfhost"],
 "Cryptography":                      ["ouder-a","security"],
 "Cyberveiligheid in 2026":           ["ouder-a","security"],
 "False sense of":                    ["ouder-a","security"],
 "Hacking for fun and convenience":   ["ouder-a","security"],
 "Netwerkbeheer is als moederschap":  ["ouder-a","selfhost"],
 "Hoeveel kost elektriciteit":        ["ouder-a","selfhost"],
 "WTF\u203d PDF":                      ["ouder-a","security"],
 "Start to Program Your Badge":       ["ouder-a","tiener","badge","leren"],
 "Programmeer je badge (intro)":      ["badge","leren"],
 "Programmeer je badge (advanced)":   ["tiener","badge","leren"],
 "Fri3dPBX":                          ["ouder-a","doorlopend","radio"],
 "Radioactiviteit":                   ["ouder-a","weten"],
 "Een geautomatiseerd huis zonder":   ["ouder-a","selfhost"],
 "We flikkeren samen Discord":        ["ouder-a","security"],
 "Lego Mario Hacking":                ["tiener","badge"],

 # --- Serge's eigen sessies ---
 "Pok\u00e9mon & Yu-Gi-Oh":            ["ouder-a","tiener","eigen","games"],
 "Van leerkracht tot vibe coder":     ["ouder-a","ouder-b","eigen","leren"],
 "AI in de klas \u00e9n thuis":        ["ouder-a","ouder-b","eigen","leren"],

 # --- Kathy ---
 "hoe weet ik wat mijn talent is":    ["ouder-b","kind","leren"],
 "Veilig (spelen) rond de sporen":    ["ouder-b","weten"],
 "naai je eigen camera beanbag":      ["ouder-b","handen"],
 "Haken met de corner to corner":     ["ouder-b","handen"],
 "T-shirt bewerken met javel":        ["ouder-b","kind","handen"],
 "Verf je eigen wol":                 ["ouder-b","handen"],
 "De magie van paddenstoelen":        ["ouder-b","weten"],
 "Handtassen maken van oude":         ["ouder-b","kind","handen"],
 "Juwelen maken":                     ["ouder-b","kind","handen"],
 "wol spinnen met een Turkse":        ["ouder-b","kind","handen","esthetiek"],
 "Prutsen mag":                       ["ouder-b","kind","leren"],
 "Vinyl tekst":                       ["ouder-b","kind","handen"],
 "Kracht van feedback":               ["ouder-b","leren"],
 "Reflectie via Journalling":         ["ouder-b","leren"],
 "Sensory overload":                  ["ouder-b","weten","leren"],
 "Tawashi":                           ["ouder-b","handen"],
 "Werken met Hars":                   ["ouder-b","kind","handen"],
 "leuke lapjes haken":                ["ouder-b","handen"],
 "Bloemetjes haken":                  ["ouder-b","handen"],
 "Strandbloemen maken":               ["ouder-b","handen"],
 "Ontdek hoe Will-e":                 ["ouder-b","weten"],

 # --- Jago ---
 "Blender voor dummies":              ["tiener","esthetiek"],
 "Dungeons & Dragons":                ["tiener","kind","games"],
 "Maak een arcade game met GBStudio": ["tiener","badge","games"],
 "Laat je badge bewegen":             ["tiener","badge"],
 "Wifi bestuurde":                    ["tiener","weten"],
 "Jongleer balletjes":                ["tiener","handen"],
 "DIY flipperkast":                   ["tiener","games","handen"],
 "Maak een DJ controller":            ["tiener","kind","avond","badge"],
 "Fri3d Laser night":                 ["tiener","kind","games","avond"],
 "Modelraket bouwen":                 ["tiener","weten","handen"],
 "cyborg) katrobot":                  ["tiener","handen"],
 "Cardboard marble labyrinth":        ["tiener","handen"],
 "Snake!":                            ["tiener","doorlopend","games"],
 "WiFi Robot timer parcours":         ["tiener","doorlopend","games"],
 "WiFi robot bouwen":                 ["tiener","doorlopend","handen"],
 "Fission Impossible":                ["tiener","kind","doorlopend","games"],
 "Vossenjacht \U0001f98a Foxhunt":     ["tiener","kind","ouder-a","doorlopend","radio","games"],
 "Waterraketten":                     ["weten","handen"],
 "Bouw je eigen DIY drumcomputer":    ["tiener","kind","avond","handen"],
 "Programmeren met BBC Micro:bit":    ["leren"],
 "Scratch voor beginners":            ["leren"],
 "AI in actie: programmeer een":      ["tiener","leren"],

 # --- Mala ---
 "Analoge fotografie":                ["kind","esthetiek","handen"],
 "Realtime kunst":                    ["kind","esthetiek"],
 "Nerdkunst":                         ["kind","esthetiek"],
 "Lasercut leftover upcycling":       ["kind","doorlopend","esthetiek"],
 "Glasgraveren":                      ["kind","handen"],
 "Making Beats from Freedom":         ["kind","avond"],
 "Brixel Rave Cave":                  ["kind","avond"],
 "Singalong":                         ["kind","avond"],
 "Aanschouw het heelal":              ["kind","avond","weten"],
 "Tabletop RPG avontuur":             ["kind","games","avond"],
 "Blood on the Clocktower":           ["kind","games","avond"],
 "Lucifer-domino":                    ["kind","avond","handen"],
 "Sjorren":                           ["kind","handen"],
 "Fri3d Zine Factory":                ["kind","esthetiek","handen"],
 "Pins maken met afval":              ["kind","handen"],

 # --- rest ---
 "Hacker Jeopardy":                   ["ouder-a","kind","games","avond"],
 "Openingsceremonie":                 ["ouder-a","ouder-b","tiener","kind"],
 "Slotceremonie":                     ["ouder-a","ouder-b","tiener","kind"],
 "Fri3d Post":                        ["doorlopend"],
 "Geheim feestje":                    ["doorlopend","avond"],
 "Limosjiene":                        ["doorlopend"],
 "Morse":                             ["ouder-a","doorlopend","radio"],
 "Briljante Benny":                   ["weten"],
 "Steampunk creaturen":               ["handen"],
 "Binair naam-armbandje":             ["handen"],
 "Maak van je oude LP":               ["handen","esthetiek"],
 "Ballonplooien":                     ["handen"],
 "zelf slijm maken":                  ["weten"],
 "Om ter schuimst":                   ["weten"],
 "Papieren vliegtuigen":              ["handen","weten"],
 "Jagen op Aziatische hoornaars":     ["weten"],
 "DIY RC Auto":                       ["tiener","handen"],
 "BirdNET-PI":                        ["ouder-a","weten","selfhost"],
 "Self-hosting zelfhulpgroep":        ["ouder-a","selfhost"],
 "Workshop schattig kuikentje":       ["handen"],
 "inkscape voor beginnende":          ["esthetiek","handen"],
 "Mars rovers":                       ["tiener","handen","badge"],
 "Solder your own solar lantern":     ["tiener","handen","badge"],
}

AGES = [
 ("lft-kleuter",  "Vanaf 4 tot 6"),
 ("lft-kind",     "Vanaf 7 tot 9"),
 ("lft-tiener",   "Vanaf 10 tot 12"),
 ("lft-13",       "Vanaf 13"),
 ("lft-junior",   "Junior hackers & CoderDojo"),
 ("lft-begeleid", "Begeleiding gevraagd"),
]
PREP = [
 ("prep-mee",    "Iets meebrengen"),
 ("prep-kost",   "Kost iets"),
 ("prep-laptop", "Laptop nodig"),
]
THEMES = [
 ("badge",     "Badge & embedded"),
 ("radio",     "Radio, mesh & morse"),
 ("leren",     "Onderwijs & vibe coding"),
 ("selfhost",  "Self-hosting & slim huis"),
 ("security",  "Security & privacy"),
 ("esthetiek", "Waar de esthetiek zit"),
 ("avond",     "Muziek en avond"),
 ("handen",    "Maken met je handen"),
 ("games",     "Games & rollenspel"),
 ("weten",     "Wetenschap & natuur"),
 ("doorlopend","Doorlopend op het terrein"),
]
THEMES = THEMES + PREP
PEOPLE = [("ouder-a","Ouder A"),("ouder-b","Ouder B"),("tiener","Tiener"),("kind","Kind")]

WOORD = {'vier':4,'vijf':5,'zes':6,'zeven':7,'acht':8,'negen':9,'tien':10,
         'elf':11,'twaalf':12,'dertien':13,'veertien':14,'vijftien':15,'zestien':16}
AGEMIN = re.compile(
  r'(?:vanaf|minimum(?:leeftijd van)?|minstens)\s*\u00b1?\s*(\d+|[a-z]+)\s*(?:j\b|jaar)'
  r'|(\d+)\s*(?:tot|[-\u2013])\s*\d+\s*jaar'
  r'|kinderen\s*\(\+/-\s*(\d+)', re.I)
BEGELEID = re.compile(r'(jonger dan\s*\d+|onder de?\s*\d+\s*j|begeleid|onder toezicht|oudere begeleider)', re.I)

def minleeftijd(txt):
    m = AGEMIN.search(txt)
    if not m: return None
    v = next((g for g in m.groups() if g), None)
    if v is None: return None
    if str(v).isdigit(): return int(v)
    return WOORD.get(str(v).lower())

# --- Wat moet je meebrengen, en kost het iets? ---------------------------
BRING = re.compile(
  r'(?:\bmee\s?breng\w*|\bmee\s?te\s+brengen\b|\bmee\s?nem\w*|\bmee\s?te\s+nemen\b'
  r'|\bbreng\b[^.]{0,50}?\bmee\b|\bneem\b[^.]{0,50}?\bmee\b'
  r'|\bvoorzie\s+zelf\b|\bzorg\s+(?:zelf\s+)?voor\b|\bzelf\s+(?:te\s+)?voorzien\b'
  r'|\bbenodigdheden\b|\bbring\s+(?:a|an|your)\b)', re.I)
BRING_NOT = re.compile(
  r'(neem\s+ik\s+je\s+mee|neemt?\s+je\s+(?:stap voor stap\s+)?mee|nemen\s+je\s+mee'
  r'|er\s?mee\b|ermee\b|mee\s+op\s+(?:een|mijn|reis|ontdekking))', re.I)
# zinnen waarin de begeleider zelf het materiaal meebrengt
HOST = re.compile(r'^\s*(?:ik|we|wij|er)\b[^.]{0,80}?(?:breng|neem|voorzie|word[et]n?\s+voorzien)', re.I)
KOST = re.compile(r'(\u20ac\s?\d+[.,]?\d*|\b\d+[.,]?\d*\s?\u20ac|\b\d+[.,]?\d*\s?(?:euro|eur)\b'
                  r'|\bbijdrage\b(?!n)|\bkostprijs\b|\bmateriaalkost\w*|\binkom\b)', re.I)
BEDRAG = re.compile(r'(\u20ac\s?\d+(?:[.,]\d+)?|\d+(?:[.,]\d+)?\s?\u20ac|\d+(?:[.,]\d+)?\s?(?:euro|eur)\b)', re.I)
LAPTOP = re.compile(r'\blaptop\b', re.I)

AFK = (r'(?<!\bong\.)(?<!\bca\.)(?<!\bbv\.)(?<!\bnr\.)(?<!\bincl\.)'
       r'(?<!\bexcl\.)(?<!\bevt\.)(?<!\bmin\.)(?<!\bmax\.)(?<!\bnl\.)')
def zinnen(t):
    t = (t or '').replace('\r\n', '\n')
    return [z.strip() for z in re.split(AFK + r'(?<=[.!?])\s+|\n+', t) if z.strip()]

def benodigdheden(t):
    mee, kost, door_ons = [], [], []
    for z in zinnen(t):
        if len(z) > 220: continue
        if BRING.search(z) and not BRING_NOT.search(z):
            (door_ons if HOST.match(z) else mee).append(z)
        if KOST.search(z) and 'http' not in z.lower() and 'bijdragen vanuit' not in z.lower():
            kost.append(z)
    return mee[:2], kost[:2], door_ons[:1]

AGE = re.compile(
  r'(vanaf\s*\u00b1?\s*\d+\s*(?:j\b|jaar)'
  r'|minimumleeftijd van \w+'
  r'|minimum\s*\d+\s*jaar'
  r'|\d+\s*[-\u2013]\s*\d+\s*jaar'
  r'|\d+\s*tot\s*\d+\s*jaar)', re.I)

def clean(t):
    t = (t or '').replace('\r\n','\n').strip()
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    t = re.sub(r'https?://\S+', '', t)
    t = re.sub(r'[*_#`]', '', t)
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'\n{3,}', '\n\n', t).strip()

sessions = []
for day in RAW['schedule']['conference']['days']:
    for room, items in day['rooms'].items():
        for s in items:
            tags = []
            for k, v in TAG.items():
                if k.lower() in s['title'].lower():
                    tags = list(v); break
            full = (s.get('abstract') or '') + ' ' + (s.get('description') or '')
            am = AGE.search(full)
            amin = minleeftijd(full)
            mee, kost, door_ons = benodigdheden(full)
            bedrag = ""
            for z in kost:
                mb = BEDRAG.search(z)
                if mb:
                    getal = re.search(r'\d+(?:[.,]\d+)?', mb.group(0))
                    if getal: bedrag = "\u20ac" + getal.group(0).replace(".", ",")
                    break
            if mee:  tags.append("prep-mee")
            if kost: tags.append("prep-kost")
            if LAPTOP.search(full) and (mee or "workshop" in (s['type'] or "").lower()):
                tags.append("prep-laptop")
            # Leeftijdslabels, uitsluitend op basis van wat de sessie zelf zegt.
            # De twee kinderzalen tellen mee omdat die per opzet voor kinderen zijn.
            if amin is not None:
                if   amin <= 6:  tags.append("lft-kleuter")
                elif amin <= 9:  tags.append("lft-kind")
                elif amin <= 12: tags.append("lft-tiener")
                else:            tags.append("lft-13")
            if s['room'] in ("Junior hackers", "Coderdojo village"):
                if "lft-junior" not in tags: tags.append("lft-junior")
            if BEGELEID.search(full) and (amin is None or amin <= 12):
                tags.append("lft-begeleid")
            ab = clean(s.get('abstract'))
            de = clean(s.get('description'))
            body = ab if len(ab) > 40 else (de[:700] if de else ab)
            sessions.append({
                "k": f"{s['id']}-{day['date']}-{s['start']}",
                "pid": s['url'] + "|" + day['date'],
                "d": day['date'], "t": s['start'],
                "e": s['duration'], "r": s['room'],
                "n": s['title'],
                "p": ", ".join(x['public_name'] for x in s['persons']),
                "l": s['language'], "y": s['type'],
                "a": body[:900],
                "u": s['url'],
                "age": am.group(0).strip() if am else "",
                "amin": amin,
                "mee": mee, "kost": kost, "doorons": door_ons, "bedrag": bedrag,
                                "g": tags,
            })

sessions.sort(key=lambda s: (s['d'], s['t'], s['r']))
rooms = sorted({s['r'] for s in sessions if s['r'] != 'undefined (see description)'})
rooms.append('undefined (see description)')

from collections import Counter as _C
_ac = _C(g for s in sessions for g in s['g'] if g.startswith('lft-'))
print('leeftijdslabels:', dict(_ac))
_pc = _C(g for s in sessions for g in s['g'] if g.startswith('prep-'))
print('voorbereidingslabels:', dict(_pc))
untagged = [s['n'] for s in sessions
            if not [g for g in s['g'] if not g.startswith('lft-') and not g.startswith('prep-')]]
print("Zonder tag:", sorted(set(untagged)))
print("Totaal:", len(sessions))

DATA = json.dumps({"sessions": sessions, "rooms": rooms,
                   "themes": THEMES, "people": PEOPLE, "ages": AGES},
                  ensure_ascii=False, separators=(',', ':'))

MAPLOC = open('mapcoords.json', encoding='utf-8').read().strip()

tpl = open('app.template.html', encoding='utf-8').read()
out = tpl.replace('/*__DATA__*/null', DATA)
out = out.replace('/*__MAPLOC__*/{rooms:{},extra:{},size:[1226,588]}', MAPLOC)
open('../public/index.html', 'w', encoding='utf-8').write(out)
print("bytes:", len(out))
