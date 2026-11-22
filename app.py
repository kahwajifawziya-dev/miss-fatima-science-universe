"""Miss Fatima's Science Universe — interactive Streamlit learning space."""

from pathlib import Path
from html import escape

import streamlit as st

st.set_page_config(
    page_title="Miss Fatima's Science Universe",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

ASSET_DIR = Path(__file__).parent / "assets"

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
.welcome { position:relative; overflow:hidden; text-align:center; margin:0 0 1.6rem; padding:clamp(2rem,6vw,4.2rem) 1.5rem; border:1px solid rgba(119,193,255,.27); border-radius:28px; background:radial-gradient(ellipse at 50% 35%,rgba(55,92,151,.37),transparent 58%),linear-gradient(135deg,#101d36 0%,#0b172b 55%,#111b34 100%); box-shadow:0 18px 60px rgba(0,0,0,.28),inset 0 0 44px rgba(99,159,255,.07); }
.welcome:before,.welcome:after { content:'✦'; position:absolute; color:#a7dfff; opacity:.72; text-shadow:0 0 14px #55bfff; }
.welcome:before { top:18%; left:11%; font-size:1.15rem; }.welcome:after { bottom:18%; right:12%; font-size:.9rem; }
.welcome-kicker { color:#9bdcff; text-transform:uppercase; letter-spacing:.24em; font-size:.76rem; font-weight:700; }
.welcome-name { margin:.6rem 0 .1rem; font-family:'Space Grotesk',sans-serif; font-size:clamp(2.7rem,8vw,5.7rem); font-weight:700; letter-spacing:-.055em; line-height:1.08; color:#f6f9ff; text-shadow:0 5px 32px rgba(125,190,255,.24); }
.welcome-heart { display:inline-block; margin:.05em .12em 0; color:#ff344f; font-size:clamp(3.2rem,8vw,5.4rem); line-height:1; vertical-align:-.08em; filter:drop-shadow(0 0 10px rgba(255,47,75,.78)) drop-shadow(0 0 30px rgba(255,47,75,.38)); animation:heart-glow 2.4s ease-in-out infinite; }
.welcome-message { margin:.9rem 0 .35rem; color:#dcecff; font-family:'Space Grotesk',sans-serif; font-size:clamp(1.35rem,4vw,2.1rem); font-weight:600; }
.welcome-subtitle { margin:0 auto; max-width:620px; color:#aebfd8; font-size:1rem; line-height:1.7; }
@keyframes heart-glow { 0%,100% { transform:scale(1); } 50% { transform:scale(1.08); } }
.card { height:100%; min-height:150px; padding:1.25rem; border:1px solid rgba(137,181,231,.16); border-radius:18px; background:linear-gradient(150deg,rgba(19,35,60,.94),rgba(13,25,44,.94)); }
.card h3 { font-size:1.1rem; margin:.45rem 0 .25rem; }
.card p,.subtle { color:var(--muted); line-height:1.65; }
.subject-card { border:1px solid rgba(83,200,255,.26); border-radius:22px; background:linear-gradient(155deg,rgba(19,42,69,.96),rgba(10,22,39,.96)); padding:1rem; height:100%; box-shadow:0 14px 35px rgba(0,0,0,.18); }
.subject-card h3 { margin:.7rem 0 .3rem; font-size:1.45rem; }
.subject-card p { color:#c4d2e6; line-height:1.6; min-height:3.3em; }
.lesson-explainer { padding:1rem 1.15rem; margin:.7rem 0 1rem; border:1px solid rgba(83,200,255,.22); border-radius:14px; background:rgba(15,35,58,.82); color:#d5e2f1; line-height:1.7; }
.lesson-explainer ul { margin:.35rem 0 0; padding-left:1.3rem; }
.lesson-explainer li { margin:.28rem 0; }
.note { border-left:3px solid var(--blue); background:rgba(40,119,166,.12); border-radius:0 12px 12px 0; padding:.85rem 1rem; color:#cad9ec; }
.formula { text-align:center; font-family:'Space Grotesk',sans-serif; font-size:1.5rem; color:#8ce8ff; padding:1.1rem; border-radius:14px; background:rgba(46,125,179,.13); border:1px solid rgba(83,200,255,.22); }
.stButton>button { border-radius:11px; border:1px solid rgba(83,200,255,.5); }
[data-testid="stImage"] img { width:100%; height:auto; border-radius:14px; }
@media (max-width: 700px) { .hero { padding:1.4rem; border-radius:18px; } .card { min-height:unset; } .subject-card p { min-height:unset; } .welcome { border-radius:20px; padding:2.1rem 1.1rem; } .welcome:before { left:6%; }.welcome:after { right:7%; } }
@media (prefers-reduced-motion: reduce) { .welcome-heart { animation:none; } }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

PAGES = ["🏠 Home", "🧬 Biology", "🧪 Chemistry", "⚡ Physics", "💙 Thank You"]
with st.sidebar:
    st.markdown("## 🔬 Science Universe")
    st.caption("A learning space with Miss Fatima")
    page = st.radio("Explore", PAGES, label_visibility="collapsed")
    st.divider()
    st.markdown("**Your subjects**")
    st.markdown('<span style="color:#9ce8ff">Biology · Chemistry · Physics</span>', unsafe_allow_html=True)
    st.caption("Curiosity starts with a question ✨")


def hero(kicker: str, title: str, intro: str) -> None:
    st.markdown(f'<section class="hero"><div class="eyebrow">{escape(kicker)}</div><h1>{escape(title)}</h1><p>{escape(intro)}</p></section>', unsafe_allow_html=True)


def card(icon: str, title: str, description: str) -> None:
    st.markdown(f'<div class="card"><div style="font-size:1.7rem">{icon}</div><h3>{escape(title)}</h3><p>{escape(description)}</p></div>', unsafe_allow_html=True)


def show_image(asset_name: str, caption: str) -> None:
    """Display repository-stored SVG artwork through Streamlit's image component."""
    asset_path = ASSET_DIR / asset_name
    if not asset_path.is_file():
        st.error(f"Illustration asset is missing: {asset_name}")
        return
    svg_markup = asset_path.read_text(encoding="utf-8")
    st.image(svg_markup, caption=caption, use_container_width=True)


def explanation(paragraph: str, points: list[str] | None = None) -> None:
    items = "" if not points else "<ul>" + "".join(f"<li>{escape(item)}</li>" for item in points) + "</ul>"
    st.markdown(f'<div class="lesson-explainer"><strong>What this diagram shows</strong><br>{escape(paragraph)}{items}</div>', unsafe_allow_html=True)


def source_note() -> None:
    st.markdown('<div class="note"><strong>About the lesson materials:</strong> The project did not include the teacher’s activity sheets or chapter notes. Biology activity prompts remain templates; explanations describe the general anatomy shown in the diagrams and do not claim to reproduce missing class handouts.</div>', unsafe_allow_html=True)


def home() -> None:
    st.markdown('<section class="welcome" aria-label="Welcome to Miss Fatima"><div class="welcome-kicker">A special place for a wonderful teacher</div><div class="welcome-name">Miss Fatima <span class="welcome-heart" aria-label="red heart">❤️</span></div><div class="welcome-message">Welcome, Miss Fatima!</div><p class="welcome-subtitle">We’re delighted you’re here. May every discovery in this universe bring a little wonder, inspiration, and joy.</p></section>', unsafe_allow_html=True)
    hero("WELCOME, SCIENTIST", "Miss Fatima’s Science Universe", "Explore biology, chemistry, and physics in one bright, interactive learning space. Pick a subject and let your curiosity lead the way.")
    show_image("science_universe_cover.svg", "A universe of discovery: life, matter, energy, and the connections between them")
    st.markdown("### Explore the universe of science")
    subject_cards = [
        ("biology_subject.svg", "Biology", "Discover how living things are built and work—from cells and DNA to the nervous system."),
        ("chemistry_subject.svg", "Chemistry", "Explore atoms, molecules, chemical structures, and the colorful world of laboratory science."),
        ("physics_subject.svg", "Physics", "Investigate electricity, circuits, energy, motion, and the rules that shape our universe."),
    ]
    cols = st.columns(3, gap="large")
    for col, (asset, title, description) in zip(cols, subject_cards):
        with col:
            st.markdown('<div class="subject-card">', unsafe_allow_html=True)
            show_image(asset, f"{title} science illustration")
            st.markdown(f"### {title}")
            st.markdown(f'<p>{escape(description)}</p></div>', unsafe_allow_html=True)
    st.markdown("### Choose your next stop")
    chosen = st.selectbox("Jump to a subject", ["Biology", "Chemistry", "Physics", "A special thank-you"])
    if st.button("Explore →", type="primary"):
        st.session_state["page"] = {"Biology": "🧬 Biology", "Chemistry": "🧪 Chemistry", "Physics": "⚡ Physics", "A special thank-you": "💙 Thank You"}[chosen]
        st.rerun()


BIOLOGY_ACTIVITIES = {
    "Activity 1": {
        "asset": "biology_brain.svg", "caption": "Brain anatomy: cerebrum, cerebellum, and brainstem",
        "title": "Human brain anatomy",
        "summary": "The diagram shows a side view of the brain and identifies three major regions.",
        "points": ["Cerebrum: the largest region; it supports functions such as conscious thought, interpreting sensory information, and voluntary movement.", "Cerebellum: helps coordinate movement, balance, and posture.", "Brainstem: connects the brain with the spinal cord and helps regulate essential automatic functions."],
    },
    "Activity 2": {
        "asset": "biology_spinal_cord.svg", "caption": "Colorful spinal cord cross-section with labeled regions",
        "title": "Spinal cord cross-section",
        "summary": "The cross-section shows the central butterfly-shaped gray matter surrounded by white matter, with the central canal and spinal nerve pathways labeled.",
        "points": ["Gray matter contains many neuron cell bodies and processing connections; its horns extend toward the front and back of the cord.", "White matter surrounds the gray matter and contains nerve fibers that carry signals up and down the spinal cord.", "The central canal is a small passage within the gray matter. Dorsal pathways are associated with incoming sensory information; ventral pathways carry outgoing motor signals."],
    },
    "Activity 3": {
        "asset": "biology_neuron.svg", "caption": "Neuron anatomy: dendrites, cell body, nucleus, axon, and terminals",
        "title": "Neuron anatomy",
        "summary": "The diagram follows the main parts of a neuron, from its branching input region to the end of its long fiber.",
        "points": ["Dendrites receive signals from other cells and carry them toward the cell body.", "The cell body contains the nucleus, which holds the cell's genetic material and helps direct cell activity.", "The axon carries electrical signals away from the cell body; axon terminals pass signals to another cell at a connection."],
    },
    "Activity 4": {
        "asset": "biology_spinal_roots.svg", "caption": "Spinal nerve roots: dorsal root ganglion and ventral root",
        "title": "Spinal roots and spinal nerve",
        "summary": "The diagram shows the dorsal and ventral roots meeting to form a spinal nerve, with the dorsal root ganglion on the sensory root.",
        "points": ["The dorsal root carries sensory information toward the spinal cord; its ganglion contains sensory neuron cell bodies.", "The ventral root carries motor commands away from the spinal cord.", "After the roots join, the spinal nerve contains both sensory and motor fibers."],
    },
    "Activity 7": {
        "asset": "biology_synapse.svg", "caption": "Synapse: presynaptic terminal, synaptic cleft, and postsynaptic membrane",
        "title": "A chemical synapse",
        "summary": "The diagram shows how a signal can pass from a sending neuron to a receiving cell across a tiny gap.",
        "points": ["The presynaptic terminal is the sending side and releases chemical messengers called neurotransmitters.", "The synaptic cleft is the narrow gap between the cells; neurotransmitters cross this space.", "The postsynaptic membrane is the receiving side, where receptors respond to the neurotransmitters."],
    },
}


def biology() -> None:
    hero("LIFE SCIENCE", "Biology", "Explore the nervous system diagrams and use your assigned class materials for the activity prompt.")
    activity = st.selectbox("Biology activity", ["Activity 1", "Activity 2", "Activity 3", "Activity 4", "Activity 7", "Interpret Lab (Analysis + Conclusion)"])
    if activity in BIOLOGY_ACTIVITIES:
        lesson = BIOLOGY_ACTIVITIES[activity]
        st.markdown(f"### {activity} · {lesson['title']}")
        show_image(lesson["asset"], lesson["caption"])
        explanation(lesson["summary"], lesson["points"])
        st.info(f"The exact instructions and answer key for {activity} were not included in the repository. Use the original class handout for the assigned task; the explanation above describes the general structures shown.")
        st.text_area("Teacher-provided activity prompt or notes", key=f"{activity}_notes", height=140, placeholder="Add the prompt from your class handout…")
        st.caption("This text stays in the current app session and is not saved to the repository.")
    else:
        st.markdown("### 🔎 Interpret Lab")
        show_image("biology_interpret_lab.svg", "Biology lab: observations, evidence, and interpretation")
        explanation("A science investigation begins with observations. Organize what you recorded, look for patterns, and support a conclusion with evidence from your assigned Biology lab.", ["Analysis: describe relevant results and patterns without adding unsupported information.", "Conclusion: answer the lab question and refer to evidence from your own observations."])
        st.caption("Biology only · The specific lab prompt and data were not included in the project materials.")
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
    structure, detail = LEWIS_EXAMPLES[selected]
    st.markdown(f'<div class="formula">{escape(structure)}</div>', unsafe_allow_html=True)
    st.write(detail)
    with st.expander("Try a quick check"):
        st.text_input("Identify the central atom and count its bonding pairs and lone pairs.", key="lewis_answer", placeholder="For example: 2 bonding pairs and 2 lone pairs")
        if st.button("Show the check", key="lewis_check"):
            st.success(f"Use this structure to check your answer: {structure}. {detail}")


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
