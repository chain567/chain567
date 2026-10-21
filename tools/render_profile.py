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
    b = rect(1, 1, 958, 110, "bg", 12, "line")
    b += text(24, 47, "Hi, I'm Chain.", 35, weight=700, letter_spacing="-1")
    b += rect(224, 22, 3, 29, "blue", 0, cls="cursor")
    b += text(25, 80, "Computer science student. Tools, hardware, and curiosity.", 17, "muted")
    b += path("M530 22V90", width=1)
    for x, label, value, accent in [(553, "IN CLASS", "C++", "blue"), (682, "IN PROJECTS", "Python", "green"), (813, "AFTER CLASS", "Self-learning", "orange")]:
        b += circle(x, 39, 3, accent, "pulse")
        b += text(x+10, 43, label, 10, "muted", cls="mono")
        b += text(x, 74, value, 17, weight=600)
    svg("intro", 960, 112, "Hi, I'm Chain — computer science student", "C++ coursework, Python projects and self-directed learning. Tools, hardware and curiosity.", b)


def mobile_hero():
    b = rect(1, 1, 478, 124, "bg", 12, "line")
    b += text(20, 43, "Hi, I'm Chain.", 34, weight=700, letter_spacing="-1")
    b += rect(214, 19, 3, 28, "blue", 0, cls="cursor")
    b += text(21, 72, "Computer science student.", 17, "muted")
    b += circle(24, 103, 3, "blue", "pulse")
    b += text(35, 108, "C++ coursework · Python · self-learning", 15, "muted")
    svg("intro-mobile", 480, 126, "Hi, I'm Chain — computer science student", "C++ in class, Python in projects and self-directed learning.", b)


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
