import json, re, html

RAW = json.load(open('schedule-snapshot.json'))

# title-substring -> tags
TAG = {
 # --- Serge ---
 "Fri3d Badge - Hardware":            ["serge","badge"],
 "MicroPythonOS":                     ["serge","badge"],
 "BadgeHub":                          ["serge","badge"],
 "Meet the Mosfet":                   ["serge","badge"],
 "MeshCore dat je vergeten":          ["serge","radio"],
 "PCB art, SAO":                      ["serge","badge","esthetiek"],
 "Op vossenjacht met je badge":       ["serge","jago","radio","badge"],
 "Make an app or game with AI":       ["serge","badge","leren"],
 "Self-hosting with docker":          ["serge","selfhost"],
 "Taking back control":               ["serge","radio","security"],
 "Smart Home Engineering":            ["serge","selfhost","badge"],
 "Geen batterij, toch slim":          ["serge","selfhost"],
 "Opname podcast Home Assistant":     ["serge","selfhost"],
 "Capaciteitstarief beperken":        ["serge","selfhost"],
 "Fri3d Badge - Achter de schermen":  ["serge","badge"],
 "Mijn data is van mij":              ["serge","selfhost","security"],
 "RF Hacking":                        ["serge","radio"],
 "Aurora project":                    ["serge","radio","weten"],
 "Nerdland Talk":                     ["serge","weten"],
 "Vibe Code a game":                  ["serge","leren"],
 "PCB reverse-engineering":           ["serge","badge"],
 "IPv6 adoption":                     ["serge","selfhost"],
 "PCB versie van een Neodome":        ["serge","badge","esthetiek"],
 "rtl_433":                           ["serge","radio"],
 "Hoe herstel je oude computers":     ["serge","badge"],
 "OpenStreetmap voor beginners":      ["serge","selfhost"],
 "Cryptography":                      ["serge","security"],
 "Cyberveiligheid in 2026":           ["serge","security"],
 "False sense of":                    ["serge","security"],
 "Hacking for fun and convenience":   ["serge","security"],
 "Netwerkbeheer is als moederschap":  ["serge","selfhost"],
 "Hoeveel kost elektriciteit":        ["serge","selfhost"],
 "WTF\u203d PDF":                      ["serge","security"],
 "Start to Program Your Badge":       ["serge","jago","badge","leren"],
 "Programmeer je badge (intro)":      ["badge","leren"],
 "Programmeer je badge (advanced)":   ["jago","badge","leren"],
 "Fri3dPBX":                          ["serge","doorlopend","radio"],
 "Radioactiviteit":                   ["serge","weten"],
 "Een geautomatiseerd huis zonder":   ["serge","selfhost"],
 "We flikkeren samen Discord":        ["serge","security"],
 "Lego Mario Hacking":                ["jago","badge"],

 # --- Serge's eigen sessies ---
 "Pok\u00e9mon & Yu-Gi-Oh":            ["serge","jago","eigen","games"],
 "Van leerkracht tot vibe coder":     ["serge","kathy","eigen","leren"],
 "AI in de klas \u00e9n thuis":        ["serge","kathy","eigen","leren"],

 # --- Kathy ---
 "hoe weet ik wat mijn talent is":    ["kathy","mala","leren"],
 "Veilig (spelen) rond de sporen":    ["kathy","weten"],
 "naai je eigen camera beanbag":      ["kathy","handen"],
 "Haken met de corner to corner":     ["kathy","handen"],
 "T-shirt bewerken met javel":        ["kathy","mala","handen"],
 "Verf je eigen wol":                 ["kathy","handen"],
 "De magie van paddenstoelen":        ["kathy","weten"],
 "Handtassen maken van oude":         ["kathy","mala","handen"],
 "Juwelen maken":                     ["kathy","mala","handen"],
 "wol spinnen met een Turkse":        ["kathy","mala","handen","esthetiek"],
 "Prutsen mag":                       ["kathy","mala","leren"],
 "Vinyl tekst":                       ["kathy","mala","handen"],
 "Kracht van feedback":               ["kathy","leren"],
 "Reflectie via Journalling":         ["kathy","leren"],
 "Sensory overload":                  ["kathy","weten","leren"],
 "Tawashi":                           ["kathy","handen"],
 "Werken met Hars":                   ["kathy","mala","handen"],
 "leuke lapjes haken":                ["kathy","handen"],
 "Bloemetjes haken":                  ["kathy","handen"],
 "Strandbloemen maken":               ["kathy","handen"],
 "Ontdek hoe Will-e":                 ["kathy","weten"],

 # --- Jago ---
 "Blender voor dummies":              ["jago","esthetiek"],
 "Dungeons & Dragons":                ["jago","mala","games"],
 "Maak een arcade game met GBStudio": ["jago","badge","games"],
 "Laat je badge bewegen":             ["jago","badge"],
 "Wifi bestuurde":                    ["jago","weten"],
 "Jongleer balletjes":                ["jago","handen"],
 "DIY flipperkast":                   ["jago","games","handen"],
 "Maak een DJ controller":            ["jago","mala","avond","badge"],
 "Fri3d Laser night":                 ["jago","mala","games","avond"],
 "Modelraket bouwen":                 ["jago","weten","handen"],
 "cyborg) katrobot":                  ["jago","handen"],
 "Cardboard marble labyrinth":        ["jago","handen"],
 "Snake!":                            ["jago","doorlopend","games"],
 "WiFi Robot timer parcours":         ["jago","doorlopend","games"],
 "WiFi robot bouwen":                 ["jago","doorlopend","handen"],
 "Fission Impossible":                ["jago","mala","doorlopend","games"],
 "Vossenjacht \U0001f98a Foxhunt":     ["jago","mala","serge","doorlopend","radio","games"],
 "Waterraketten":                     ["weten","handen"],
 "Bouw je eigen DIY drumcomputer":    ["jago","mala","avond","handen"],
 "Programmeren met BBC Micro:bit":    ["leren"],
 "Scratch voor beginners":            ["leren"],
 "AI in actie: programmeer een":      ["jago","leren"],

 # --- Mala ---
 "Analoge fotografie":                ["mala","esthetiek","handen"],
 "Realtime kunst":                    ["mala","esthetiek"],
 "Nerdkunst":                         ["mala","esthetiek"],
 "Lasercut leftover upcycling":       ["mala","doorlopend","esthetiek"],
 "Glasgraveren":                      ["mala","handen"],
 "Making Beats from Freedom":         ["mala","avond"],
 "Brixel Rave Cave":                  ["mala","avond"],
 "Singalong":                         ["mala","avond"],
 "Aanschouw het heelal":              ["mala","avond","weten"],
 "Tabletop RPG avontuur":             ["mala","games","avond"],
 "Blood on the Clocktower":           ["mala","games","avond"],
 "Lucifer-domino":                    ["mala","avond","handen"],
 "Sjorren":                           ["mala","handen"],
 "Fri3d Zine Factory":                ["mala","esthetiek","handen"],
 "Pins maken met afval":              ["mala","handen"],

 # --- rest ---
 "Hacker Jeopardy":                   ["serge","mala","games","avond"],
 "Openingsceremonie":                 ["serge","kathy","jago","mala"],
 "Slotceremonie":                     ["serge","kathy","jago","mala"],
 "Fri3d Post":                        ["doorlopend"],
 "Geheim feestje":                    ["doorlopend","avond"],
 "Limosjiene":                        ["doorlopend"],
 "Morse":                             ["serge","doorlopend","radio"],
 "Briljante Benny":                   ["weten"],
 "Steampunk creaturen":               ["handen"],
 "Binair naam-armbandje":             ["handen"],
 "Maak van je oude LP":               ["handen","esthetiek"],
 "Ballonplooien":                     ["handen"],
 "zelf slijm maken":                  ["weten"],
 "Om ter schuimst":                   ["weten"],
 "Papieren vliegtuigen":              ["handen","weten"],
 "Jagen op Aziatische hoornaars":     ["weten"],
 "DIY RC Auto":                       ["jago","handen"],
 "BirdNET-PI":                        ["serge","weten","selfhost"],
 "Self-hosting zelfhulpgroep":        ["serge","selfhost"],
 "Workshop schattig kuikentje":       ["handen"],
 "inkscape voor beginnende":          ["esthetiek","handen"],
 "Mars rovers":                       ["jago","handen","badge"],
 "Solder your own solar lantern":     ["jago","handen","badge"],
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
PEOPLE = [("serge","Serge"),("kathy","Kathy"),("jago","Jago"),("mala","Mala")]

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
