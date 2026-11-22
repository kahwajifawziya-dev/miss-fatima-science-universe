"""Miss Fatima's Science Universe — interactive Streamlit learning space."""

from base64 import b64encode
from html import escape
import urllib.error
import urllib.request

import streamlit as st

st.set_page_config(
    page_title="Miss Fatima's Science Universe",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { --ink:#eef5ff; --muted:#a9bad3; --blue:#53c8ff; --cyan:#7af4ff; }
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
.stApp { color:var(--ink); background:radial-gradient(ellipse at 82% 4%,#102d50 0,transparent 36%),linear-gradient(145deg,#07111f 0%,#091629 58%,#07111f 100%); }
[data-testid="stHeader"] { background:rgba(7,17,31,.65); }
[data-testid="stSidebar"] { background:linear-gradient(180deg,#0b1930,#091323); border-right:1px solid rgba(112,190,255,.16); }
[data-testid="stSidebar"] * { color:var(--ink); }
h1,h2,h3 { font-family:'Space Grotesk',sans-serif !important; color:#f2f8ff !important; letter-spacing:-.035em; }
.hero { padding:2.1rem 2rem; border:1px solid rgba(83,200,255,.27); border-radius:24px; background:linear-gradient(115deg,rgba(18,45,78,.95),rgba(12,28,51,.77)); box-shadow:0 18px 55px rgba(0,0,0,.2); margin:1rem 0 1.5rem; }
.eyebrow { color:var(--cyan); text-transform:uppercase; letter-spacing:.18em; font-size:.75rem; font-weight:700; }
.hero h1 { font-size:clamp(2rem,5vw,3.8rem); margin:.35rem 0 .4rem; }
.hero p { color:#c0d0e6; font-size:1.04rem; max-width:690px; margin:0; }
.card { height:100%; min-height:150px; padding:1.25rem; border:1px solid rgba(137,181,231,.16); border-radius:18px; background:linear-gradient(150deg,rgba(19,35,60,.94),rgba(13,25,44,.94)); }
.card .icon { font-size:1.7rem; }
.card h3 { font-size:1.1rem; margin:.45rem 0 .25rem; }
.card p,.subtle { color:var(--muted); line-height:1.65; }
.pill { display:inline-block; padding:.28rem .7rem; border:1px solid rgba(83,200,255,.35); border-radius:99px; color:#9ce8ff; font-size:.82rem; margin:.2rem .25rem .2rem 0; }
.note { border-left:3px solid var(--blue); background:rgba(40,119,166,.12); border-radius:0 12px 12px 0; padding:.85rem 1rem; color:#cad9ec; }
.formula { text-align:center; font-family:'Space Grotesk',sans-serif; font-size:1.5rem; color:#8ce8ff; padding:1.1rem; border-radius:14px; background:rgba(46,125,179,.13); border:1px solid rgba(83,200,255,.22); }
.image-caption { color:#a9bad3; text-align:center; font-size:.82rem; margin-top:-.35rem; margin-bottom:1rem; }
.stButton>button { border-radius:11px; border:1px solid rgba(83,200,255,.5); }
@media (max-width: 700px) { .hero { padding:1.4rem; border-radius:18px; } .card { min-height:unset; } }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Public Wikimedia Commons images; URL availability is checked before display.
# Each fallback is a self-contained SVG illustration so a network/image failure
# never leaves a broken image or blank image area in the app.
IMAGES = {
    "cover": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Science_collage.png",
        "source": "https://commons.wikimedia.org/wiki/File:Science_collage.png",
        "alt": "Colorful science collage representing biology, chemistry, and physics",
        "caption": "Biology · Chemistry · Physics | Science collage, Wikimedia Commons",
        "fallback": "cover",
    },
    "brain": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Location_of_cerebrum%2C_cerebellum_and_brainstem.png",
        "source": "https://commons.wikimedia.org/wiki/File:Location_of_cerebrum,_cerebellum_and_brainstem.png",
        "alt": "Labeled human brain showing cerebrum, cerebellum, and brainstem",
        "caption": "Brain anatomy: cerebrum, cerebellum, and brainstem | Wikimedia Commons",
        "fallback": "brain",
    },
    "spinal_cord": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Gray_734.png",
        "source": "https://commons.wikimedia.org/wiki/File:Gray_734.png",
        "alt": "Spinal cord cross-section showing grey and white matter",
        "caption": "Spinal cord cross-section | Gray's Anatomy, Wikimedia Commons",
        "fallback": "spinal_cord",
    },
    "neuron": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/58/Neuron_diag2.png",
        "source": "https://commons.wikimedia.org/wiki/File:Neuron_diag2.png",
        "alt": "Neuron diagram with labeled cell body, dendrites, axon, and terminals",
        "caption": "Neuron anatomy | Wikimedia Commons",
        "fallback": "neuron",
    },
    "roots": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Gray798.png",
        "source": "https://commons.wikimedia.org/wiki/File:Gray798.png",
        "alt": "Spinal nerve showing dorsal root ganglion and dorsal and ventral roots",
        "caption": "Spinal roots and dorsal root ganglion | Gray's Anatomy, Wikimedia Commons",
        "fallback": "roots",
    },
    "synapse": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Synapse_diag1.png",
        "source": "https://commons.wikimedia.org/wiki/File:Synapse_diag1.png",
        "alt": "Labeled synapse diagram showing neurotransmitter transfer between neurons",
        "caption": "Synapse diagram | Wikimedia Commons",
        "fallback": "synapse",
    },
}


def svg_art(kind: str) -> str:
    """Return a responsive dark-theme vector fallback with educational labels."""
    common = '<defs><linearGradient id="g" x2="1" y2="1"><stop stop-color="#102c4a"/><stop offset="1" stop-color="#0a1729"/></linearGradient><filter id="glow"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="1000" height="500" rx="28" fill="url(#g)"/><g fill="none" stroke="#54ccff" stroke-width="3" opacity=".8">'
    labels = '<g font-family="Arial,sans-serif" font-size="24" fill="#eaf6ff">'
    if kind == "cover":
        artwork = '<circle cx="510" cy="250" r="116" fill="#102c49" stroke="#59dbff" stroke-width="3" filter="url(#glow)"/><circle cx="510" cy="250" r="53" fill="none" stroke="#a88bff" stroke-width="4"/><ellipse cx="510" cy="250" rx="115" ry="42" transform="rotate(-28 510 250)"/><ellipse cx="510" cy="250" rx="115" ry="42" transform="rotate(50 510 250)"/><circle cx="600" cy="160" r="9" fill="#78f4ff"/><path d="M190 140 C220 85 290 100 300 160 C350 150 365 215 322 235 C345 285 290 322 258 286 C210 320 163 275 187 237 C137 211 150 158 190 140Z" fill="#123d55" stroke="#69e7b0"/><path d="M190 145 C228 178 228 250 260 285 M165 207 L315 207 M210 120 L282 290" stroke="#78f4ff" opacity=".8"/><path d="M730 115 L800 155 L800 235 L730 275 L660 235 L660 155Z" fill="#132e4a" stroke="#ffbe67"/><circle cx="730" cy="115" r="8" fill="#ffbe67"/><circle cx="800" cy="155" r="8" fill="#ffbe67"/><circle cx="800" cy="235" r="8" fill="#ffbe67"/><circle cx="730" cy="275" r="8" fill="#ffbe67"/><circle cx="660" cy="235" r="8" fill="#ffbe67"/><circle cx="660" cy="155" r="8" fill="#ffbe67"/><path d="M105 390 Q200 350 295 390 T485 390 T675 390 T865 390" stroke="#37aaff"/><path d="M500 390 l35 -58 32 110 35 -77 35 25 32 -55 35 55 38 0" stroke="#8bf5ff"/><circle cx="170" cy="90" r="3" fill="#fff"/><circle cx="860" cy="105" r="4" fill="#fff"/><circle cx="930" cy="280" r="3" fill="#fff"/>'
        text = '<text x="500" y="455" text-anchor="middle" font-size="27" letter-spacing="7">A UNIVERSE OF DISCOVERY</text>'
    elif kind == "brain":
        artwork = '<path d="M400 350 C300 340 280 250 312 190 C330 110 420 95 480 125 C550 90 640 130 650 205 C710 250 660 330 600 347Z" fill="#183d59" stroke="#77e8ff" stroke-width="5"/><path d="M410 125 Q380 190 430 220 T400 325 M490 120 Q460 180 500 215 T480 340 M570 130 Q540 180 585 210 T560 340" stroke="#a4bcff" stroke-width="4"/><path d="M580 280 C650 265 680 315 640 360 C620 390 580 380 560 352Z" fill="#3e3267" stroke="#c49aff" stroke-width="5"/><path d="M500 330 Q520 370 510 430 L550 430 Q550 375 570 340" fill="#175071" stroke="#71ddff" stroke-width="5"/><path d="M390 170 L230 125 M620 320 L790 340 M530 400 L760 425" stroke="#63dfff" stroke-width="2"/>'
        text = '<text x="55" y="120">CEREBRUM</text><text x="795" y="350">CEREBELLUM</text><text x="770" y="435">BRAINSTEM</text>'
    elif kind == "spinal_cord":
        artwork = '<circle cx="500" cy="255" r="170" fill="#f2eee7" stroke="#65dfff" stroke-width="5"/><circle cx="500" cy="255" r="145" fill="#b9d1df" stroke="#7895a8" stroke-width="3"/><path d="M500 150 C455 185 435 205 462 235 C430 262 445 287 480 292 C455 325 480 355 500 360 C520 355 545 325 520 292 C555 287 570 262 538 235 C565 205 545 185 500 150Z" fill="#5b4b70" stroke="#3f3851" stroke-width="4"/><circle cx="500" cy="255" r="8" fill="#f0c66c"/>'
        text = '<text x="55" y="185">WHITE MATTER</text><text x="55" y="220">(outer region)</text><text x="695" y="270">GRAY MATTER</text><text x="695" y="305">(central butterfly)</text><text x="420" y="470">SPINAL CORD · CROSS-SECTION</text>'
    elif kind == "neuron":
        artwork = '<circle cx="430" cy="250" r="72" fill="#173d5c" stroke="#65eaff" stroke-width="5"/><circle cx="430" cy="250" r="24" fill="#986fff"/><path d="M380 200 L320 140 L285 95 M380 225 L290 210 L235 180 M380 270 L290 300 L245 355 M390 300 L345 370 L330 415 M500 250 C600 250 650 210 760 250 S860 280 925 240" stroke="#63dfff" stroke-width="9"/><path d="M565 226 Q590 250 565 274 M665 222 Q690 250 665 278 M765 230 Q790 250 765 270" stroke="#ffbc67" stroke-width="15"/><path d="M925 240 l30 -20 M925 240 l31 15 M900 250 l25 35" stroke="#73e8b6" stroke-width="5"/><path d="M430 170 L430 100 M640 215 L650 130 M790 292 L815 365" stroke="#9db9d3" stroke-width="2"/>'
        text = '<text x="350" y="85">DENDRITES</text><text x="360" y="465">CELL BODY</text><text x="615" y="112">MYELIN SHEATH</text><text x="785" y="405">AXON</text><text x="765" y="335">AXON TERMINALS</text>'
    elif kind == "roots":
        artwork = '<path d="M500 90 L500 410" stroke="#91b2c9" stroke-width="72" stroke-linecap="round"/><path d="M465 220 C380 190 330 145 245 125 M465 255 C375 255 325 255 230 255 M465 290 C375 325 325 365 245 390" stroke="#63dfff" stroke-width="12"/><path d="M535 320 C625 340 690 350 780 370" stroke="#ffb866" stroke-width="12"/><ellipse cx="365" cy="190" rx="45" ry="28" transform="rotate(22 365 190)" fill="#603d7e" stroke="#dc9fff" stroke-width="5"/><path d="M465 220 L650 300 M535 320 L650 300 L780 370" stroke="#9cf3dd" stroke-width="7"/>'
        text = '<text x="70" y="120">DORSAL ROOT</text><text x="70" y="165">(sensory)</text><text x="250" y="115">DORSAL ROOT GANGLION</text><text x="670" y="435">VENTRAL ROOT (motor)</text><text x="390" y="465">SPINAL CORD</text>'
    else:
        artwork = '<path d="M100 160 Q250 90 440 160 L440 340 Q250 410 100 340Z" fill="#194064" stroke="#6ce8ff" stroke-width="5"/><path d="M900 160 Q750 90 560 160 L560 340 Q750 410 900 340Z" fill="#293b69" stroke="#b89bff" stroke-width="5"/><path d="M425 205 Q470 190 485 220 L515 220 Q530 190 575 205 L575 295 Q530 310 515 280 L485 280 Q470 310 425 295Z" fill="#10243d" stroke="#ffbd68" stroke-width="4"/><circle cx="492" cy="225" r="8" fill="#72f2cc"/><circle cx="510" cy="250" r="8" fill="#72f2cc"/><circle cx="492" cy="275" r="8" fill="#72f2cc"/><path d="M450 250 L490 250 M510 250 L555 250" stroke="#ffcb76" stroke-width="3" stroke-dasharray="6 7"/><path d="M300 180 L260 105 M700 180 L740 105 M500 215 L500 120" stroke="#9db9d3" stroke-width="2"/>'
        text = '<text x="80" y="80">SENDING NEURON</text><text x="680" y="80">RECEIVING NEURON</text><text x="420" y="105">SYNAPTIC CLEFT</text><text x="375" y="395">NEUROTRANSMITTERS</text><text x="435" y="450">SIGNAL →</text>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500" role="img" aria-label="Educational science diagram">{common}{artwork}</g>{labels}{text}</g></svg>'


@st.cache_data(ttl=3600, show_spinner=False)
def image_is_available(url: str) -> bool:
    """Check the public image file before passing it to Streamlit's image renderer."""
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "ScienceUniverse/1.0 educational app"})
    try:
        with urllib.request.urlopen(request, timeout=4) as response:
            return response.status == 200 and response.headers.get("Content-Type", "").startswith("image/")
    except (urllib.error.URLError, TimeoutError, ValueError):
        return False


def show_image(image_key: str, width: int | None = None) -> None:
    image = IMAGES[image_key]
    if image_is_available(image["url"]):
        st.image(image["url"], use_container_width=True, caption=image["caption"])
    else:
        svg_data = b64encode(svg_art(image["fallback"]).encode("utf-8")).decode("ascii")
        st.markdown(
            f'<img src="data:image/svg+xml;base64,{svg_data}" alt="{escape(image["alt"])}" '
            'style="display:block;width:100%;height:auto;max-height:560px;object-fit:contain;'
            'border:1px solid rgba(83,200,255,.24);border-radius:20px;background:#091629"/>',
            unsafe_allow_html=True,
        )
        st.markdown(f'<div class="image-caption">{escape(image["caption"])} · locally rendered backup illustration</div>', unsafe_allow_html=True)


PAGES = ["🏠 Home", "🧬 Biology", "🧪 Chemistry", "⚡ Physics", "💙 Thank You"]
with st.sidebar:
    st.markdown("## 🔬 Science Universe")
    st.caption("A learning space with Miss Fatima")
    page = st.radio("Explore", PAGES, label_visibility="collapsed")
    st.divider()
    st.markdown("**Your subjects**")
    st.markdown('<span class="pill">Biology</span><span class="pill">Chemistry</span><span class="pill">Physics</span>', unsafe_allow_html=True)
    st.caption("Curiosity starts with a question ✨")


def hero(kicker: str, title: str, intro: str) -> None:
    st.markdown(f'<section class="hero"><div class="eyebrow">{escape(kicker)}</div><h1>{escape(title)}</h1><p>{escape(intro)}</p></section>', unsafe_allow_html=True)


def card(icon: str, title: str, description: str) -> None:
    st.markdown(f'<div class="card"><div class="icon">{icon}</div><h3>{escape(title)}</h3><p>{escape(description)}</p></div>', unsafe_allow_html=True)


def source_note() -> None:
    st.markdown('<div class="note"><strong>About the lesson materials:</strong> The project did not include the teacher’s activity sheets or chapter notes. The activity slots below are intentionally left as templates; no teacher-specific instructions or answers have been made up.</div>', unsafe_allow_html=True)


def home() -> None:
    hero("WELCOME, SCIENTIST", "Miss Fatima’s Science Universe", "Explore biology, chemistry, and physics in one bright, interactive learning space. Pick a subject and let your curiosity lead the way.")
    show_image("cover")
    cols = st.columns(3)
    with cols[0]: card("🧬", "Biology", "Activities 1, 2, 3, 4 & 7, plus a Biology-only Interpret Lab.")
    with cols[1]: card("🧪", "Chemistry", "A Lewis structures lesson with worked molecule examples and a practice explorer.")
    with cols[2]: card("⚡", "Physics", "Chapter 3: Electric Current, with key ideas and a quick concept check.")
    st.write("")
    st.markdown("### Choose your next stop")
    chosen = st.selectbox("Jump to a subject", ["Biology", "Chemistry", "Physics", "A special thank-you"])
    if st.button("Explore →", type="primary"):
        st.session_state["page"] = {"Biology": "🧬 Biology", "Chemistry": "🧪 Chemistry", "Physics": "⚡ Physics", "A special thank-you": "💙 Thank You"}[chosen]
        st.rerun()


def biology() -> None:
    hero("LIFE SCIENCE", "Biology", "Choose one of the requested activities, or open the Interpret Lab to organize your analysis and conclusion.")
    activity = st.selectbox("Biology activity", ["Activity 1", "Activity 2", "Activity 3", "Activity 4", "Activity 7", "Interpret Lab (Analysis + Conclusion)"])
    activity_images = {
        "Activity 1": ("brain", "Human brain anatomy"),
        "Activity 2": ("spinal_cord", "Spinal cord cross-section"),
        "Activity 3": ("neuron", "Neuron anatomy"),
        "Activity 4": ("roots", "Spinal roots and dorsal root ganglion"),
        "Activity 7": ("synapse", "Synapse diagram"),
    }
    if activity in activity_images:
        image_key, label = activity_images[activity]
        st.markdown(f"### 🧠 {activity} · {label}")
        show_image(image_key)
        st.info(f"The instructions, topic, and answer key for {activity} were not included in the project materials. This activity slot is ready for the original class handout—no details have been invented.")
        st.text_area("Paste or write the teacher-provided activity prompt here for your own session.", key=f"{activity}_notes", height=150, placeholder="Teacher-provided prompt and notes…")
        st.caption("This text stays in the current app session and is not saved to the repository.")
    else:
        st.markdown("### 🔎 Interpret Lab")
        st.caption("Biology only · Use your assigned lab observations and evidence.")
        st.info("The lab-specific prompt and data were not included in the project materials. Add your own class observations below; this page will not assume what the experiment was.")
        analysis, conclusion = st.columns(2)
        with analysis:
            st.markdown("#### Analysis")
            st.text_area("Record patterns, comparisons, or evidence from your Biology lab.", key="bio_analysis", height=170, placeholder="Use evidence from your lab materials…")
        with conclusion:
            st.markdown("#### Conclusion")
            st.text_area("Write a conclusion supported by your analysis.", key="bio_conclusion", height=170, placeholder="Answer the lab question using your evidence…")
        if st.button("Review my lab writing"):
            if st.session_state.get("bio_analysis", "").strip() and st.session_state.get("bio_conclusion", "").strip():
                st.success("Both sections are ready. Check that your conclusion is supported by evidence from your lab.")
            else:
                st.warning("Add both an analysis and a conclusion before reviewing.")
    st.markdown("\n")
    source_note()


LEWIS_EXAMPLES = {
    "H₂ — hydrogen": ("H–H", "Each hydrogen shares one pair of electrons. The shared pair gives each H a filled first shell (duet)."),
    "H₂O — water": ("H–O–H", "Oxygen is the central atom. It forms two single bonds to H and has two lone pairs. Each H has a duet; O has an octet."),
    "CO₂ — carbon dioxide": ("O=C=O", "Carbon is central and forms a double bond to each oxygen. Each O has two lone pairs; C and both O atoms have octets."),
    "NH₃ — ammonia": ("Three N–H single bonds; one lone pair on N", "Nitrogen is central, with three shared pairs in N–H bonds and one lone pair. N has an octet; each H has a duet."),
    "CH₄ — methane": ("Four C–H single bonds", "Carbon is central and shares one pair with each of four hydrogen atoms. C has an octet; each H has a duet."),
}


def chemistry() -> None:
    hero("CHEMISTRY", "Lewis Structures", "See how valence electrons are represented in simple covalent molecules, then explore a worked example.")
    st.markdown("### The core idea")
    st.write("A Lewis structure is a model that shows valence electrons: shared pairs form covalent bonds, and unshared pairs are lone pairs. Hydrogen is shown with a duet and common second-period atoms with an octet.")
    st.markdown("#### A useful drawing routine")
    steps = st.columns(4)
    step_text = [("01 · Count", "Add the valence electrons contributed by the atoms."), ("02 · Connect", "Choose a central atom (hydrogen is never central) and draw single bonds."), ("03 · Complete", "Give outer atoms their duet or octet, then place remaining electrons on the center."), ("04 · Check", "Check the total electron count and octets; use multiple bonds if needed.")]
    for col, (title, text) in zip(steps, step_text):
        with col: card("✦", title, text)
    st.markdown("### Worked examples")
    selected = st.selectbox("Choose a molecule", list(LEWIS_EXAMPLES))
    structure, explanation = LEWIS_EXAMPLES[selected]
    st.markdown(f'<div class="formula">{escape(structure)}</div>', unsafe_allow_html=True)
    st.write(explanation)
    with st.expander("Try a quick check"):
        st.text_input("Identify the central atom and count its bonding pairs and lone pairs.", key="lewis_answer", placeholder="For example: 2 bonding pairs and 2 lone pairs")
        if st.button("Show the check", key="lewis_check"):
            st.success(f"Use this structure to check your answer: {structure}. {explanation}")


def physics() -> None:
    hero("PHYSICS · CHAPTER 3", "Electric Current", "A concise foundation for thinking about current, charge flow, and its measurement.")
    st.markdown("### What is electric current?")
    st.write("Electric current describes how quickly electric charge passes a point in a circuit. Conventional current is the direction positive charge would move; in a metal wire, electrons drift in the opposite direction.")
    st.markdown('<div class="formula">I = Q ÷ t</div>', unsafe_allow_html=True)
    st.write("**I** is current in amperes (A), **Q** is charge in coulombs (C), and **t** is time in seconds (s). One ampere is one coulomb of charge passing per second.")
    a, b = st.columns(2)
    with a: card("🔌", "Measure current", "An ammeter measures current and is connected in series so the circuit current passes through it.")
    with b: card("↔️", "Closed path", "Steady current in a simple circuit requires a complete conducting path and an energy source.")
    st.markdown("### Quick concept check")
    st.write("If 12 C of charge passes a point in 3 s, what is the current?")
    answer = st.radio("Choose an answer", ["0.25 A", "4 A", "36 A"], horizontal=True, key="current_quiz")
    if st.button("Check answer", key="current_check"):
        if answer == "4 A": st.success("Correct: I = Q ÷ t = 12 C ÷ 3 s = 4 A.")
        else: st.info("Use I = Q ÷ t, with charge in coulombs and time in seconds, then try again.")
    st.markdown("\n")
    source_note()
    st.caption("This is a general introductory overview. The actual Chapter 3 notes and examples were not present in the repository; follow the class materials where they differ.")


def thank_you() -> None:
    hero("A NOTE FROM THE HEART", "Thank you, Miss Fatima", "For the patience, encouragement, and spark that make learning an adventure.")
    st.markdown('<div class="hero" style="text-align:center;padding:3.2rem 1.5rem"><div style="font-size:clamp(1.7rem,5vw,3rem);font-family:\'Space Grotesk\',sans-serif;color:#f2f8ff">From your student Hadi,<br>to the best teacher ❤️</div><div style="color:#9ce8ff;margin-top:1rem;font-size:1.1rem">Thank you for helping curiosity grow. ✨</div></div>', unsafe_allow_html=True)


if "page" in st.session_state:
    page = st.session_state.pop("page")
if page == "🏠 Home": home()
elif page == "🧬 Biology": biology()
elif page == "🧪 Chemistry": chemistry()
elif page == "⚡ Physics": physics()
else: thank_you()
