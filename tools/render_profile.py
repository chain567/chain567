"""Render the profile's self-contained light/dark SVG artwork. No dependencies."""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets" / "profile"
THEMES = {
    "light": {"bg": "#f7f6f2", "panel": "#eeede7", "ink": "#20231f", "muted": "#62675e", "line": "#d8dbd1", "blue": "#2856d8", "green": "#326844", "orange": "#b84b29", "violet": "#7550ad", "white": "#ffffff"},
    "dark": {"bg": "#171b20", "panel": "#222830", "ink": "#eff1e9", "muted": "#a3b0b7", "line": "#38434a", "blue": "#95b0ff", "green": "#a3d9ac", "orange": "#ffab86", "violet": "#c5a8f5", "white": "#171b20"},
}
STYLE = """
text{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif}
.mono{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}
.flow{stroke-dasharray:5 8;animation:flow 2.4s linear infinite}
.pulse{animation:pulse 3.6s ease-in-out infinite}
.delayed{animation-delay:1.8s}
.cursor{animation:cursor 1.2s steps(1) infinite}
.page{animation:page 5s ease-in-out infinite}
.route{animation:route 5s ease-in-out infinite}
@keyframes flow{to{stroke-dashoffset:-26}}
@keyframes pulse{0%,100%{opacity:.35}50%{opacity:1}}
@keyframes cursor{0%,48%{opacity:1}49%,100%{opacity:0}}
@keyframes page{0%,100%{transform:translateY(0)}45%,65%{transform:translateY(-5px)}}
@keyframes route{0%,100%{stroke-dashoffset:24}50%{stroke-dashoffset:0}}
@media(prefers-reduced-motion:reduce){.flow,.pulse,.cursor,.page,.route{animation:none}}
"""


def text(x, y, value, size=16, color="ink", weight=400, cls="", **attrs):
    extra = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="@{color}" font-weight="{weight}" class="{cls}" {extra}>{escape(value)}</text>'


def rect(x, y, w, h, fill="panel", radius=8, stroke=None, cls=""):
    border = f' stroke="@{stroke}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="@{fill}"{border} class="{cls}"/>'


def path(d, color="line", width=2, cls="", **attrs):
    extra = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<path d="{d}" fill="none" stroke="@{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" class="{cls}" {extra}/>'


def circle(x, y, r, fill="blue", cls=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="@{fill}" class="{cls}"/>'


def svg(name, width, height, title, description, body):
    for theme, palette in THEMES.items():
        contents = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<style>{STYLE}</style>
{body}
</svg>\n'''
        for key, value in palette.items():
            contents = contents.replace("@" + key, value)
        (OUT / f"{name}-{theme}.svg").write_text(contents)


def hero():
    b = rect(1, 1, 958, 254, "bg", 16, "line")
    b += text(32, 35, "CHAIN567 / A WORK IN PROGRESS", 12, "muted", 500, "mono", letter_spacing="1.4")
    b += text(30, 105, "Hi, I'm Chain.", 57, weight=700, letter_spacing="-2")
    b += rect(354, 66, 4, 42, "blue", 0, cls="cursor")
    b += text(32, 143, "Computer science student. Curious about how things work.", 18)
    b += text(32, 172, "I make tools, connect hardware, and learn along the way.", 18, "muted")
    b += path("M32 197H928", width=1)
    for x, label in [(32, "SOFTWARE + HARDWARE"), (279, "PRACTICAL AUTOMATION"), (538, "SMALL-FORM-FACTOR PCs")]:
        b += text(x, 230, label, 11, "muted", 500, "mono", letter_spacing=".7")
    b += circle(909, 225, 4, "green", "pulse")
    # A compact learning switchboard: moving dots, no invented proficiency bars.
    for i, (label, value, accent) in enumerate([("IN CLASS", "C++", "blue"), ("IN PROJECTS", "Python", "green"), ("AFTER CLASS", "Self-learning", "orange")]):
        y = 36 + i * 45
        b += rect(706, y, 220, 37, "panel", 7)
        b += circle(720, y + 18, 3, accent, "pulse" + (" delayed" if i % 2 else ""))
        b += text(732, y + 15, label, 9, "muted", 500, "mono")
        b += text(732, y + 30, value, 14, weight=600)
    svg("intro", 960, 256, "Hi, I'm Chain — computer science student", "C++ coursework, Python projects and self-directed learning. Software, hardware, practical automation and small-form-factor PCs.", b)


def mobile_hero():
    b = rect(1, 1, 478, 286, "bg", 14, "line")
    b += text(24, 31, "CHAIN567 / A WORK IN PROGRESS", 10, "muted", 500, "mono", letter_spacing=".8")
    b += text(22, 90, "Hi, I'm Chain.", 48, weight=700, letter_spacing="-1.5")
    b += rect(298, 55, 3, 36, "blue", 0, cls="cursor")
    b += text(24, 124, "Computer science student.", 18)
    b += text(24, 151, "Tools, hardware, and a lot of curiosity.", 17, "muted")
    for i, (label, value, accent) in enumerate([("IN CLASS", "C++", "blue"), ("IN PROJECTS", "Python", "green"), ("AFTER CLASS", "Self-learning", "orange")]):
        x = 24 + i * 146
        b += rect(x, 177, 138, 62, "panel", 7)
        b += circle(x+11, 193, 3, accent, "pulse" + (" delayed" if i%2 else ""))
        b += text(x+21, 197, label, 9, "muted", cls="mono")
        b += text(x+10, 224, value, 17, weight=600)
    b += text(24, 267, "SOFTWARE + HARDWARE / PRACTICAL TOOLS", 10, "muted", cls="mono", letter_spacing=".5")
    svg("intro-mobile", 480, 288, "Hi, I'm Chain — computer science student", "C++ in class, Python in projects, self-directed learning. I enjoy tools and hands-on hardware.", b)


def card_base(number, title, label, accent):
    b = rect(1, 1, 478, 280, "bg", 14, "line")
    b += text(24, 29, number + " / " + label, 10, "muted", 500, "mono", letter_spacing="1")
    b += text(24, 65, title, 27, weight=650, letter_spacing="-.7")
    b += path("M439 25H453V39M453 25L438 40", accent, 1.7)
    b += path("M24 245H456", width=1)
    return b


def haptic():
    b = card_base("01", "VibeGuide", "SOFTWARE MEETS HARDWARE", "blue")
    b += text(24, 93, "Navigation you can feel.", 17, "muted")
    b += rect(24, 115, 432, 77)
    b += rect(47, 126, 37, 55, "bg", 7, "line")
    b += path("M57 165V146H74M66 138L74 146L66 154", "blue", 2.4)
    b += path("M100 153H260M260 153V137H330M260 153V172H389", "blue", 1.6, "flow")
    b += text(133, 143, "Bluetooth", 12, "muted", cls="mono")
    for x, y, value, cls in [(350, 137, "L", "pulse"), (408, 172, "R", "pulse delayed")]:
        b += circle(x, y, 15, "blue", cls)
        b += text(x, y + 5, value, 13, "white", 700, text_anchor="middle")
    b += text(24, 219, "Idea → feature iteration → hands-on prototype", 13)
    b += text(24, 267, "Android · Kotlin · Bluetooth · Arduino", 12, "blue", 500)
    svg("vibeguide", 480, 282, "VibeGuide: Android and Arduino haptic navigation", "Navigation you can feel. I originated the idea and led feature iteration, with hands-on hardware integration. Open the source repository.", b)


def visio():
    b = card_base("02", "Visio, minus the repetition.", "DESKTOP AUTOMATION", "green")
    b += text(24, 93, "A folder of diagrams. A batch of images.", 17, "muted")
    b += rect(24, 115, 432, 77)
    b += '<g class="page">' + rect(46, 128, 33, 44, "bg", 3, "line") + rect(54, 134, 33, 44, "bg", 3, "line") + text(59, 160, ".vsd", 9, "muted", cls="mono") + '</g>'
    b += path("M104 153H351", "green", 1.6, "flow")
    b += rect(177, 138, 110, 30, "panel", 6) + text(232, 158, "BATCH EXPORT", 10, "green", 600, "mono", text_anchor="middle")
    b += rect(367, 130, 56, 44, "bg", 4, "line")
    b += circle(407, 142, 4, "green") + path("M373 166L386 151L396 160L403 153L417 167", "green", 1.8)
    b += text(24, 219, "Folder structure kept. Progress on screen.", 13)
    b += text(24, 267, "Python · Tkinter · Windows COM", 12, "green", 500)
    svg("visio", 480, 282, "Visio batch image export", "Export folders of Visio diagrams to images, keeping folder structure and showing progress. Python, Tkinter and Windows COM. Open the repository.", b)


def av():
    b = card_base("03", "AV Operations Portal", "APPLICATION WORKFLOWS", "orange")
    b += text(24, 93, "Inventory. Roles. A clear next action.", 17, "muted")
    b += rect(24, 115, 432, 77)
    for x, label in [(43, "INVENTORY"), (188, "JSON"), (332, "AUDIT LOG")]:
        b += rect(x, 135, 104, 36, "bg", 6, "line")
        b += text(x + 52, 158, label, 10, weight=500, cls="mono", text_anchor="middle")
    b += path("M149 153H186M294 153H330", "orange", 1.7, "flow")
    b += circle(285, 135, 4, "orange", "pulse")
    b += text(24, 219, "Manager / technician views · simulated commands", 13)
    b += text(24, 267, "Python · Streamlit · Pandas · JSON", 12, "orange", 500)
    svg("av-portal", 480, 282, "AV Operations Portal: independent sample application", "Inventory and role-based workflows with JSON command preview and an audit log. Commands are simulated. Open the repository and screenshots.", b)


def notes():
    b = card_base("04", "Notes from figuring it out.", "ALGORITHMS & LEARNING", "violet")
    b += text(24, 93, "Working through the why behind the code.", 17, "muted")
    b += rect(24, 115, 432, 77)
    b += text(42, 145, "01  try an approach", 12, "muted", cls="mono")
    b += text(42, 168, "02  compare & understand", 12, cls="mono")
    b += path("M302 153H340V135H389M340 153V173H389", "violet", 1.7, "flow")
    for x, y, r, cl in [(302, 153, 5, ""), (389, 135, 6, "pulse"), (389, 173, 6, "pulse delayed")]:
        b += circle(x, y, r, "violet", cl)
    b += text(24, 219, "Approaches · edge cases · alternative solutions", 13)
    b += text(24, 267, "Python · C++ · DSA notes", 12, "violet", 500)
    svg("notebook", 480, 282, "Algorithm notebook: approaches and alternative solutions", "Python and selected C++ solutions, with notes about reasoning and edge cases. Open the learning notebook.", b)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    hero()
    mobile_hero()
    haptic()
    visio()
    av()
    notes()
    print(f"Rendered 12 light/dark SVG assets in {OUT}")
