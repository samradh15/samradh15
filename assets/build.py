#!/usr/bin/env python3
"""
Generates the theme-aware SVG assets used by README.md.

One source, two themes. Tokens below are the only place colors live;
each theme gets its own step of the same hue rather than an auto-flip.
Backgrounds stay transparent so the art sits on whatever surface
GitHub is actually painting (default / dimmed / high-contrast).

    python3 assets/build.py
"""
import pathlib

OUT = pathlib.Path(__file__).parent

SANS = "'Inter','Helvetica Neue',Helvetica,-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif"
MONO = "ui-monospace,'SF Mono',SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": {
        "ACCENT":  "#D4FF4F",  # 16.4:1 on #0d1117
        "INK":     "#E6EDF3",
        "SUB":     "#9BA6B2",
        "MUTED":   "#6E7A87",
        "RULE":    "#30363D",
        "TILE_BG": "#FFFFFF", "TILE_BG_O": "0.035",
        "TILE_BR": "#FFFFFF", "TILE_BR_O": "0.11",
        "OUTLINE": "#E6EDF3",
    },
    "light": {
        "ACCENT":  "#3F5C00",  # 7.7:1 on #ffffff
        "INK":     "#0B0D10",
        "SUB":     "#5B6672",
        "MUTED":   "#6E7A87",
        "RULE":    "#D8DEE4",
        "TILE_BG": "#000000", "TILE_BG_O": "0.025",
        "TILE_BR": "#000000", "TILE_BR_O": "0.10",
        "OUTLINE": "#0B0D10",
    },
}

BASE_CSS = """
  .sans{font-family:__SANS__}
  .mono{font-family:__MONO__}
  .meta{font-family:__MONO__;font-size:10px;letter-spacing:3.4px;fill:__MUTED__}
  .rule{stroke:__RULE__;stroke-width:1}
  .ac{fill:__ACCENT__}
  text{text-rendering:geometricPrecision}
"""


def shell(w, h, label, css, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
        f'height="{h}" role="img" aria-label="{label}">\n<style>{css}</style>\n{body}\n</svg>\n'
    )


# ---------------------------------------------------------------- hero

HERO_CSS = BASE_CSS + """
  .wm{font-family:__SANS__;font-size:64px;font-weight:800;letter-spacing:-2.2px;fill:__INK__}
  .wm-out{fill:none;stroke:__OUTLINE__;stroke-width:1.25}
  .k{font-family:__MONO__;font-size:10px;letter-spacing:2px;fill:__MUTED__}
  .v{font-family:__MONO__;font-size:11.5px;fill:__SUB__}
  .v b{font-weight:600;fill:__INK__}
  .cli{font-family:__MONO__;font-size:13px;fill:__SUB__}
  .t{opacity:0;animation:cyc 18s linear infinite}
  .t2{animation-delay:4.5s}.t3{animation-delay:9s}.t4{animation-delay:13.5s}
  @keyframes cyc{0%{opacity:0}1.5%{opacity:1}23%{opacity:1}25%{opacity:0}100%{opacity:0}}
  .caret{animation:blink 1.06s steps(1,end) infinite}
  @keyframes blink{0%,50%{opacity:1}50.01%,100%{opacity:0}}
  .pulse{animation:pl 2.4s ease-out infinite}
  @keyframes pl{0%{r:3.5;opacity:.55}100%{r:11;opacity:0}}
  .sweep{animation:sw 18s linear infinite}
  @keyframes sw{0%{transform:translateX(0);opacity:0}4%{opacity:.9}
                40%{opacity:.9}55%{opacity:0}100%{transform:translateX(792px);opacity:0}}
"""

SPEC = [
    ("ROLE",   'AI Product Manager <tspan class="mono" fill="__MUTED__">— discovery to ship</tspan>'),
    ("FOCUS",  '0&#8594;1 products <tspan fill="__MUTED__">·</tspan> AI/LLM <tspan fill="__MUTED__">·</tspan> Forward Deployed'),
    ("BUILT",  'VyapGO <tspan fill="__MUTED__">·</tspan> DasetAI <tspan fill="__MUTED__">·</tspan> RelAI <tspan fill="__MUTED__">·</tspan> NotifyME'),
    ("PROOF",  '<tspan class="ac">50+</tspan> merchants live <tspan fill="__MUTED__">·</tspan> <tspan class="ac">80+</tspan> interviews'),
]

TAGS = [
    "I think like a founder, build like an engineer, ship like a PM.",
    "Discovery over opinion. If users aren't complaining, I'm not building.",
    "Specs are cheap. Untested specs are risky — so I prototype first.",
    "AI is a feature, not a benefit. Users should forget the AI is there.",
]


def hero():
    b = []
    b.append('<text class="meta" x="44" y="42">PORTFOLIO INDEX</text>')
    b.append('<text class="meta" x="836" y="42" text-anchor="end">SAMRADH.DEV</text>')
    b.append('<line class="rule" x1="44" y1="56" x2="836" y2="56"/>')
    # sweeping accent tick riding the top rule
    b.append('<g class="sweep"><rect x="44" y="54.5" width="46" height="3" fill="__ACCENT__" rx="1.5"/></g>')

    b.append('<text class="wm" x="42" y="130">SAMRADH</text>')
    b.append('<text class="wm wm-out" x="42" y="196">AGARWAL</text>')
    b.append('<rect x="44" y="218" width="76" height="4" fill="__ACCENT__"/>')

    y = 96
    for k, v in SPEC:
        b.append(f'<text class="k" x="470" y="{y}">{k}</text>')
        b.append(f'<text class="v" x="548" y="{y}">{v}</text>')
        y += 27
    # status row with pulsing dot
    b.append(f'<text class="k" x="470" y="{y}">STATUS</text>')
    b.append(f'<circle class="pulse" cx="553" cy="{y - 4}" r="3.5" fill="__ACCENT__"/>')
    b.append(f'<circle cx="553" cy="{y - 4}" r="3.5" fill="__ACCENT__"/>')
    b.append(f'<text class="v" x="565" y="{y}"><tspan b>Open to AI PM / FDE roles</tspan></text>')

    b.append('<line class="rule" x1="44" y1="250" x2="836" y2="250"/>')
    for i, t in enumerate(TAGS, 1):
        t = t.replace("&", "&amp;")
        b.append(
            f'<text class="cli t t{i}" x="44" y="280">'
            f'<tspan class="ac">&#9656;</tspan> {t}'
            f'<tspan class="ac caret">&#9608;</tspan></text>'
        )
    return shell(880, 300, "Samradh Agarwal — AI Product Manager, open to AI PM and Forward Deployed roles",
                 HERO_CSS, "\n".join(b))


# ------------------------------------------------------------- metrics

METRIC_CSS = BASE_CSS + """
  .val{font-family:__SANS__;font-size:36px;font-weight:700;letter-spacing:-1.4px;fill:__INK__}
  .lab{font-family:__MONO__;font-size:10.5px;fill:__SUB__}
  .sub{font-family:__MONO__;font-size:9px;fill:__MUTED__}
"""

TILES = [
    ("80+",  "MSME interviews",  "Field discovery, VyapGO"),
    ("50+",  "Merchants live",   "Shipped and transacting"),
    ("+90%", "Activation lift",  "First-transaction rate"),
    ("15+",  "Clients shipped",  "IN / NZ / DXB, 1000xDev"),
]


def metrics():
    b = []
    for i, (val, lab, sub) in enumerate(TILES):
        x = 44 + i * 202
        b.append(
            f'<rect x="{x}" y="22" width="186" height="116" rx="8" '
            f'fill="__TILE_BG__" fill-opacity="__TILE_BG_O__" '
            f'stroke="__TILE_BR__" stroke-opacity="__TILE_BR_O__" stroke-width="1"/>'
        )
        b.append(f'<rect x="{x + 18}" y="44" width="26" height="3" fill="__ACCENT__"/>')
        b.append(f'<text class="val" x="{x + 18}" y="92">{val}</text>')
        b.append(f'<text class="lab" x="{x + 18}" y="112">{lab}</text>')
        b.append(f'<text class="sub" x="{x + 18}" y="127">{sub}</text>')
    return shell(880, 160, "Key outcomes: 80+ MSME interviews, 50+ merchants live, "
                           "+90% activation lift, 15+ clients shipped", METRIC_CSS, "\n".join(b))


# ------------------------------------------------------------ pipeline

PIPE_CSS = BASE_CSS + """
  .idx{font-family:__SANS__;font-size:34px;font-weight:800;letter-spacing:-1px;
       fill:none;stroke:__OUTLINE__;stroke-width:1.1;opacity:.55}
  .st{font-family:__MONO__;font-size:11px;letter-spacing:3px;fill:__ACCENT__}
  .qt{font-family:__MONO__;font-size:11.5px;fill:__SUB__}
  .qt b{fill:__INK__;font-weight:600}
"""

STAGES = [
    ("01", "DISCOVERY", ["If users aren't complaining,", "<b>I'm not building.</b>",
                         "80+ interviews before the", "first line of spec."]),
    ("02", "EXECUTION", ["Specs are cheap, untested", "specs are risky. I prototype",
                         "in <b>Python / Next.js</b> to", "de-risk before handoff."]),
    ("03", "DELIVERY",  ["<b>AI is a feature,</b> not a", "benefit. Users should",
                         "forget the AI is there at", "all. Ship, measure, iterate."]),
]


def pipeline():
    b = []
    for i, (idx, title, lines) in enumerate(STAGES):
        x = 44 + i * 272
        b.append(f'<text class="idx" x="{x}" y="46">{idx}</text>')
        b.append(f'<text class="st" x="{x}" y="74">{title}</text>')
        b.append(f'<line class="rule" x1="{x}" y1="88" x2="{x + 248}" y2="88"/>')
        b.append(f'<rect x="{x}" y="86.5" width="34" height="3" fill="__ACCENT__"/>')
        for j, ln in enumerate(lines):
            ln = ln.replace("<b>", '<tspan b>').replace("</b>", "</tspan>")
            b.append(f'<text class="qt" x="{x}" y="{114 + j * 19}">{ln}</text>')
        if i < 2:
            cx = x + 258
            b.append(f'<path d="M{cx} 42 l6 5 -6 5" fill="none" stroke="__MUTED__" '
                     f'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>')
    return shell(880, 190, "How I work: discovery, execution, delivery", PIPE_CSS, "\n".join(b))


# ------------------------------------------------------------- buttons

BTN_CSS = BASE_CSS + """
  .bl{font-family:__MONO__;font-size:11.5px;letter-spacing:1.6px;font-weight:500;fill:__INK__}
  .ar{font-family:__MONO__;font-size:12px;fill:__MUTED__}
"""

BUTTONS = [
    ("portfolio", "PORTFOLIO"),
    ("linkedin",  "LINKEDIN"),
    ("email",     "EMAIL"),
    ("resume",    "RESUME"),
]


def button(label):
    w, h = 176, 44
    b = [
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="10" '
        f'fill="__TILE_BG__" fill-opacity="__TILE_BG_O__" '
        f'stroke="__TILE_BR__" stroke-opacity="__TILE_BR_O__" stroke-width="1"/>',
        '<rect x="18" y="19" width="6" height="6" fill="__ACCENT__"/>',
        f'<text class="bl" x="34" y="26.5">{label}</text>',
        f'<text class="ar" x="{w - 18}" y="26.5" text-anchor="end">&#8594;</text>',
    ]
    return shell(w, h, label.title(), BTN_CSS, "\n".join(b))


# ---------------------------------------------------------------- emit

def render(svg, theme):
    out = svg.replace("__SANS__", SANS).replace("__MONO__", MONO)
    for k, v in THEMES[theme].items():
        out = out.replace(f"__{k}__", v)
    # <tspan b> is shorthand the CSS child selectors key off
    return out.replace("<tspan b>", '<tspan class="em">').replace(
        "</style>", ".em{font-weight:600;fill:" + THEMES[theme]["INK"] + "}\n</style>")


jobs = [("hero", hero), ("metrics", metrics), ("pipeline", pipeline)]
jobs += [(f"btn-{slug}", (lambda l: lambda: button(l))(lab)) for slug, lab in BUTTONS]

for name, fn in jobs:
    for theme in THEMES:
        p = OUT / f"{name}-{theme}.svg"
        p.write_text(render(fn(), theme), encoding="utf-8")
        print(f"  {p.relative_to(OUT.parent)}  {p.stat().st_size:>6,}b")
