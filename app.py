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
.tribute-wrap { position:relative; overflow:hidden; max-width:1050px; margin:1rem auto 2rem; padding:clamp(1.3rem,4vw,3.4rem); border:1px solid rgba(117,174,255,.25); border-radius:30px; background:radial-gradient(ellipse at 50% 0%,rgba(98,58,112,.25),transparent 43%),radial-gradient(ellipse at 12% 65%,rgba(41,107,156,.16),transparent 36%),linear-gradient(150deg,#101a31 0%,#0a1426 60%,#111a30 100%); box-shadow:0 25px 85px rgba(0,0,0,.36),inset 0 1px 0 rgba(255,255,255,.05); }
.tribute-wrap:before,.tribute-wrap:after { content:'✦'; position:absolute; color:#b9dfff; opacity:.6; text-shadow:0 0 18px #65bbff; animation:tribute-sparkle 4s ease-in-out infinite; }
.tribute-wrap:before { top:7%; left:7%; font-size:1.2rem; }.tribute-wrap:after { bottom:8%; right:8%; font-size:1rem; animation-delay:1.3s; }
.tribute-eyebrow { text-align:center; color:#a9d8ff; font-size:.74rem; font-weight:700; letter-spacing:.28em; text-transform:uppercase; }
.tribute-title { text-align:center; margin:.7rem 0 .2rem; font-family:'Space Grotesk',sans-serif; font-size:clamp(2rem,6vw,4rem); line-height:1.15; letter-spacing:-.04em; color:#f7f8ff; text-shadow:0 0 32px rgba(149,183,255,.22); }
.tribute-heart { display:block; text-align:center; font-size:clamp(4rem,11vw,7.4rem); line-height:1.2; margin:.2rem auto .5rem; filter:drop-shadow(0 0 12px rgba(255,47,75,.8)) drop-shadow(0 0 36px rgba(255,47,75,.45)); animation:tribute-heartbeat 2.2s ease-in-out infinite; }
.tribute-rule { width:min(150px,36%); height:1px; margin:1.25rem auto 1.8rem; background:linear-gradient(90deg,transparent,#9bcfff,rgba(255,116,143,.85),transparent); box-shadow:0 0 14px rgba(107,185,255,.55); }
.tribute-copy { max-width:780px; margin:0 auto; }
.tribute-copy p { margin:0 auto 1.25rem; color:#d7e1f1; font-size:clamp(1rem,2.3vw,1.18rem); line-height:1.9; text-align:center; }
.tribute-copy p:first-child { color:#f0f5ff; }
.tribute-signoff { margin-top:2rem; text-align:center; color:#bad1ec; font-size:1.05rem; line-height:1.9; }
.tribute-signature { margin:.5rem auto 0; color:#f4f6ff; font-family:'Space Grotesk',sans-serif; font-size:clamp(1.2rem,3.3vw,1.75rem); line-height:1.55; font-weight:600; }
.tribute-signature-heart { color:#ff3b55; filter:drop-shadow(0 0 10px rgba(255,47,75,.62)); }
.tribute-footer { text-align:center; margin:1.6rem 0 0; color:#92b4d7; letter-spacing:.16em; font-size:.72rem; text-transform:uppercase; }
@keyframes tribute-heartbeat { 0%,100% { transform:scale(1); } 12% { transform:scale(1.07); } 24% { transform:scale(1); } 36% { transform:scale(1.045); } 52% { transform:scale(1); } }
@keyframes tribute-sparkle { 0%,100% { opacity:.35; transform:scale(.88) rotate(0); } 50% { opacity:.9; transform:scale(1.12) rotate(18deg); } }
.card { height:100%; min-height:150px; padding:1.25rem; border:1px solid rgba(137,181,231,.16); border-radius:18px; background:linear-gradient(150deg,rgba(19,35,60,.94),rgba(13,25,44,.94)); }
.card h3 { font-size:1.1rem; margin:.45rem 0 .25rem; }
.card p,.subtle { color:var(--muted); line-height:1.65; }
.subject-card { border:1px solid rgba(83,200,255,.26); border-radius:22px; background:linear-gradient(155deg,rgba(19,42,69,.96),rgba(10,22,39,.96)); padding:1rem; height:100%; box-shadow:0 14px 35px rgba(0,0,0,.18); }
.subject-card h3 { margin:.7rem 0 .3rem; font-size:1.45rem; }
.subject-card p { color:#c4d2e6; line-height:1.6; min-height:3.3em; }
.lesson-explainer { padding:1rem 1.15rem; margin:.7rem 0 1rem; border:1px solid rgba(83,200,255,.22); border-radius:14px; background:rgba(15,35,58,.82); color:#d5e2f1; line-height:1.7; }
.lesson-explainer ul { margin:.35rem 0 0; padding-left:1.3rem; }
.lesson-explainer li { margin:.28rem 0; }
.lesson-card { height:100%; padding:1rem 1.1rem; border:1px solid rgba(83,200,255,.23); border-radius:17px; background:linear-gradient(145deg,rgba(19,42,69,.96),rgba(10,22,39,.96)); }
.lesson-card h4 { margin:0 0 .55rem; color:#b5edff; font-family:'Space Grotesk',sans-serif; font-size:1.08rem; }
.lesson-card p { margin:.35rem 0; color:#d1dfef; line-height:1.65; }
.lesson-card .formula-large { color:#83e5ff; font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:clamp(1.35rem,3vw,1.85rem); margin:.2rem 0 .55rem; }
.label-chip { display:inline-block; border:1px solid rgba(83,200,255,.25); border-radius:99px; padding:.18rem .55rem; margin:.16rem .15rem .1rem 0; color:#b8d7f2; font-size:.8rem; }
.practice { padding:1rem 1.1rem; border:1px solid rgba(117,210,255,.22); border-radius:16px; background:rgba(10,30,51,.75); }
.practice h4 { margin:0 0 .45rem; color:#8ee7ff; font-family:'Space Grotesk',sans-serif; }
.note { border-left:3px solid var(--blue); background:rgba(40,119,166,.12); border-radius:0 12px 12px 0; padding:.85rem 1rem; color:#cad9ec; }
.formula { text-align:center; font-family:'Space Grotesk',sans-serif; font-size:1.5rem; color:#8ce8ff; padding:1.1rem; border-radius:14px; background:rgba(46,125,179,.13); border:1px solid rgba(83,200,255,.22); }
.stButton>button { border-radius:11px; border:1px solid rgba(83,200,255,.5); }
[data-testid="stImage"] img { width:100%; height:auto; border-radius:14px; }
@media (max-width: 700px) { .hero { padding:1.4rem; border-radius:18px; } .card { min-height:unset; } .subject-card p { min-height:unset; } .welcome { border-radius:20px; padding:2.1rem 1.1rem; } .welcome:before { left:6%; }.welcome:after { right:7%; } .tribute-wrap { border-radius:20px; padding:1.25rem 1rem; } .tribute-copy p { line-height:1.75; margin-bottom:1.05rem; } }
@media (prefers-reduced-motion: reduce) { .welcome-heart,.tribute-heart,.tribute-wrap:before,.tribute-wrap:after { animation:none; } }
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

CHEMISTRY_LESSONS = [
    "Atomic structure", "Atomic number & mass number", "Electron shells", "Valence electrons", "Ions & ionic bonding", "Covalent bonding", "Lewis structures",
]


def chem_practice(key: str, question: str, options: list[str], correct: str, explanation_text: str) -> None:
    st.markdown('<div class="practice"><h4>Quick practice</h4></div>', unsafe_allow_html=True)
    response = st.radio(question, options, key=f"chem_{key}", horizontal=True)
    if st.button("Check answer", key=f"chem_check_{key}"):
        if response == correct:
            st.success(f"Correct! {explanation_text}")
        else:
            st.info(f"Not quite. {explanation_text}")


def chemistry() -> None:
    hero("CHEMISTRY · ATOMS AND BONDING", "Chemistry", "Build your understanding from the parts of an atom to the bonds that join atoms together.")
    lesson = st.selectbox("Choose a Chemistry lesson", CHEMISTRY_LESSONS, key="chem_lesson")

    if lesson == "Atomic structure":
        st.markdown("### 1 · Structure of the atom")
        show_image("chemistry_atom.svg", "Atomic structure: nucleus with protons and neutrons, surrounded by electrons")
        st.markdown("An atom is a tiny building block of matter. At its center is a compact **nucleus**. **Protons** have positive charge and **neutrons** have no charge. **Electrons** have negative charge and occupy regions around the nucleus called shells.")
        cols = st.columns(3)
        facts = [("PROTON", "+1 charge", "In the nucleus"), ("NEUTRON", "0 charge", "In the nucleus"), ("ELECTRON", "−1 charge", "In shells around nucleus")]
        for col, (name, charge, place) in zip(cols, facts):
            with col:
                st.markdown(f'<div class="lesson-card"><h4>{name}</h4><p><strong>{charge}</strong></p><p>{place}</p></div>', unsafe_allow_html=True)
        st.markdown("**Key rule:** In a neutral atom, the number of protons equals the number of electrons, so positive and negative charges balance.")
        st.markdown("**Worked example — neutral oxygen:** Oxygen has 8 protons. A neutral oxygen atom therefore has 8 electrons. Its common nucleus contains 8 protons and 8 neutrons.")
        chem_practice("atom", "A neutral atom has 11 protons. How many electrons does it have?", ["10", "11", "12"], "11", "In a neutral atom, proton and electron counts are equal.")

    elif lesson == "Atomic number & mass number":
        st.markdown("### 2 · Atomic number and mass number")
        show_image("chemistry_atom.svg", "Protons and neutrons in the nucleus determine atomic and mass numbers")
        st.markdown('<div class="lesson-card"><h4>Remember these definitions</h4><p><strong>Atomic number (Z)</strong> = number of protons. It identifies the element.</p><p><strong>Mass number (A)</strong> = protons + neutrons in one atom’s nucleus.</p><p><strong>Neutrons</strong> = mass number − atomic number.</p></div>', unsafe_allow_html=True)
        st.markdown("**Worked example — oxygen-16:** Atomic number 8 means 8 protons. Mass number 16 means protons + neutrons = 16. Neutrons = 16 − 8 = **8**. A neutral atom also has 8 electrons.")
        st.markdown("**Notation:** An isotope may be written as ¹⁶₈O: 16 is the mass number and 8 is the atomic number.")
        chem_practice("numbers", "An atom has Z = 11 and A = 23. How many neutrons?", ["11", "12", "23"], "12", "Neutrons = A − Z = 23 − 11 = 12.")

    elif lesson == "Electron shells":
        st.markdown("### 3 · Electron shells and distribution")
        show_image("chemistry_shells.svg", "Electron shells K, L, M, and N surrounding an atom")
        st.markdown("Electrons occupy energy levels around the nucleus. Shell names K, L, M, and N correspond to principal levels n = 1, 2, 3, and 4. A shell’s theoretical maximum capacity is **2n²**: K = 2, L = 8, M = 18, N = 32 electrons.")
        st.warning("Shell capacity is not the same as the order electrons fill. For the first 20 elements at this level, use the simple filling pattern 2, 8, 8, 2 (for example, calcium is 2,8,8,2).")
        st.markdown("**Step-by-step examples**\n\n- Hydrogen (1 electron): K¹.\n- Oxygen (8 electrons): K² L⁶, often written 2,6.\n- Sodium (11 electrons): K² L⁸ M¹, written 2,8,1.\n- Chlorine (17 electrons): K² L⁸ M⁷, written 2,8,7.\n- Calcium (20 electrons): K² L⁸ M⁸ N², written 2,8,8,2.")
        chem_practice("shells", "What is the shell distribution for an atom with 11 electrons?", ["2,7,2", "2,8,1", "8,3"], "2,8,1", "Fill the first shell with 2, the second with 8, then place the remaining 1 in the third shell.")

    elif lesson == "Valence electrons":
        st.markdown("### 4 · Valence electrons")
        show_image("chemistry_shells.svg", "The outermost occupied shell contains the valence electrons")
        st.markdown("**Valence electrons** are electrons in the outermost occupied shell. They are especially important because they take part in chemical bonding. For many main-group elements, the group number helps identify this count.")
        st.markdown("**Worked examples**\n\n- Oxygen: 2,6 → outer shell has **6** valence electrons.\n- Sodium: 2,8,1 → **1** valence electron.\n- Chlorine: 2,8,7 → **7** valence electrons.\n- Carbon: 2,4 → **4** valence electrons.")
        st.markdown("Atoms can become more stable by transferring or sharing outer electrons. The simple octet model is useful for these introductory examples, but it is not a universal rule for every element or compound.")
        chem_practice("valence", "How many valence electrons does chlorine (2,8,7) have?", ["2", "7", "17"], "7", "The last number in the shell distribution is the outer-shell electron count.")

    elif lesson == "Ions & ionic bonding":
        st.markdown("### 5 · Ions and ionic bonding")
        show_image("chemistry_ions.svg", "Electron transfer from sodium to chlorine forms oppositely charged ions")
        st.markdown("An **ion** is an atom or group of atoms with a net electric charge because it has gained or lost electrons. The nucleus does not change during ordinary ion formation.")
        st.markdown("- Losing negative electrons gives a **positive ion (cation)**. Sodium loses one electron: Na → Na⁺ + e⁻.\n- Gaining negative electrons gives a **negative ion (anion)**. Chlorine gains one electron: Cl + e⁻ → Cl⁻.\n- **Ionic bonding** is the electrostatic attraction between oppositely charged ions.")
        st.markdown("**Worked example — sodium chloride (NaCl):** Sodium has 2,8,1 and loses its outer electron to become Na⁺ (2,8). Chlorine has 2,8,7 and gains that electron to become Cl⁻ (2,8,8). The + and − ions attract; the simplest ratio is one Na⁺ to one Cl⁻, giving NaCl.")
        st.markdown("**Important:** The formula NaCl represents a 1:1 ratio in an ionic solid, not a single covalently bonded NaCl molecule.")
        chem_practice("ions", "When a chlorine atom gains one electron, what ion forms?", ["Cl⁺", "Cl⁻", "Cl²⁻"], "Cl⁻", "Adding one negative electron makes the atom’s net charge −1.")

    elif lesson == "Covalent bonding":
        st.markdown("### 6 · Covalent bonding")
        show_image("chemistry_covalent.svg", "Atoms sharing electron pairs in water and carbon dioxide")
        st.markdown("A **covalent bond** forms when atoms share one or more pairs of electrons. This is common between non-metal atoms. Shared electrons count toward the outer shells of both bonded atoms.")
        st.markdown("**Worked example — water, H₂O:** Oxygen has 6 valence electrons and needs 2 more for an octet in this simple model. Each hydrogen has 1 and needs 1 more for a duet. Oxygen shares one pair with each hydrogen: two O–H single covalent bonds. Oxygen also has two lone pairs.")
        st.markdown("**Worked example — carbon dioxide, CO₂:** Carbon has 4 valence electrons and each oxygen has 6. Carbon shares two pairs with each oxygen, making O=C=O. Each atom reaches an octet in the Lewis model.")
        chem_practice("covalent", "In a single covalent bond, how many electron pairs are shared?", ["One pair", "Two pairs", "Three pairs"], "One pair", "A single covalent bond represents one shared pair of electrons.")

    else:
        st.markdown("### 7 · Lewis structures")
        show_image("chemistry_covalent.svg", "Lewis bond examples: shared pairs in covalent molecules")
        st.markdown("Lewis structures show valence electrons as bonds (shared pairs) and lone pairs (unshared pairs). A line represents one shared pair. Hydrogen follows a duet; common second-period atoms often follow an octet in these introductory molecules.")
        st.markdown("**A step-by-step method**\n\n1. Count all valence electrons.\n2. Choose a central atom (usually the least electronegative; never H) and connect atoms with single bonds.\n3. Complete the outer atoms’ duets or octets.\n4. Place remaining electrons on the central atom.\n5. If the central atom lacks an octet, convert a lone pair on a neighbor into a multiple bond.\n6. Check the total electron count and each atom’s duet/octet.")
        with st.expander("Worked example: H₂O"):
            st.markdown("1. Count: O contributes 6 and two H contribute 2 → **8 valence electrons**.\n2. Connect H–O–H: two single bonds use 4 electrons.\n3. Put the remaining 4 electrons on O as two lone pairs.\n4. Check: each H has a duet; O has two bonds (4 shared electrons) plus two lone pairs (4 electrons), an octet.")
            st.markdown('<div class="formula">H–O–H · two lone pairs on O</div>', unsafe_allow_html=True)
        with st.expander("Worked example: CO₂"):
            st.markdown("1. Count: C contributes 4; two O contribute 12 → **16 valence electrons**.\n2. Start O–C–O and complete oxygen octets.\n3. Carbon is short of an octet, so convert one lone pair from each O into a shared pair.\n4. Final structure: **O=C=O**. Each O has two lone pairs; carbon and oxygen each have an octet.")
        with st.expander("Worked example: H and O atoms"):
            st.markdown("A single H atom has one valence electron (H·); H₂ shares one pair (H–H). An O atom has six valence electrons (six Lewis dots): two pairs and two single electrons before bonding. In H₂O, O shares one pair with each H and keeps two lone pairs.")
        chem_practice("lewis", "How many valence electrons are in one CO₂ molecule?", ["8", "12", "16"], "16", "C has 4 and each O has 6: 4 + 6 + 6 = 16.")


PHYSICS_FORMULAS = [
    {"title": "Electric current", "formula": "I = Q / t", "symbols": "I = current · Q = charge · t = time", "units": "I in amperes (A); Q in coulombs (C); t in seconds (s)", "use": "Use when charge and time are known and you need current.", "example": "12 C passes in 3 s: I = 12 / 3 = 4 A."},
    {"title": "Electric charge", "formula": "Q = I × t", "symbols": "Q = charge · I = current · t = time", "units": "Q in coulombs (C); I in amperes (A); t in seconds (s)", "use": "Use when current and time are known and you need transferred charge.", "example": "A 0.5 A current flows for 20 s: Q = 0.5 × 20 = 10 C."},
    {"title": "Time", "formula": "t = Q / I", "symbols": "t = time · Q = charge · I = current", "units": "t in seconds (s); Q in coulombs (C); I in amperes (A)", "use": "Use when charge and current are known and you need the duration.", "example": "30 C passes at 2 A: t = 30 / 2 = 15 s."},
]


def physics() -> None:
    hero("PHYSICS · CHAPTER 3", "Electric Current", "Understand current, charge, circuit meters, and the formulas that connect them.")
    st.markdown("### The idea of current")
    st.write("Electric current is the rate at which electric charge passes a point in a circuit. A complete conducting path is needed for a steady current. Current is measured in amperes (A).")
    st.markdown("### Current, charge, and time · formula cards")
    for start in range(0, len(PHYSICS_FORMULAS), 3):
        cols = st.columns(3, gap="medium")
        for col, item in zip(cols, PHYSICS_FORMULAS[start:start + 3]):
            with col:
                st.markdown(f'<div class="lesson-card"><h4>{item["title"]}</h4><div class="formula-large">{item["formula"]}</div><p><strong>Symbols:</strong> {item["symbols"]}</p><p><strong>Units:</strong> {item["units"]}</p><p><strong>When to use:</strong> {item["use"]}</p><p><strong>Example:</strong> {item["example"]}</p></div>', unsafe_allow_html=True)
    st.markdown("#### Formula triangle")
    st.markdown('<div class="formula">Q = I × t &nbsp;&nbsp; | &nbsp;&nbsp; I = Q / t &nbsp;&nbsp; | &nbsp;&nbsp; t = Q / I</div>', unsafe_allow_html=True)
    st.caption("Rearrange the relationship to find the quantity you do not know. Convert measurements to A, C, and s before calculating.")

    st.markdown("### Units and conversions")
    unit_cols = st.columns(3)
    unit_notes = [
        ("Current", "1 A = 1000 mA", "1 mA = 0.001 A"),
        ("Potential difference", "1 V = 1000 mV", "1 kV = 1000 V"),
        ("Conversion tip", "Large unit → small unit: multiply by 1000", "Small unit → large unit: divide by 1000"),
    ]
    for col, (title, first, second) in zip(unit_cols, unit_notes):
        with col:
            st.markdown(f'<div class="lesson-card"><h4>{title}</h4><p>{first}</p><p>{second}</p></div>', unsafe_allow_html=True)
    st.markdown("**Examples:** 250 mA = 0.250 A; 0.6 A = 600 mA; 4500 mV = 4.5 V; 2.4 kV = 2400 V. Voltage (V) is potential difference, not a unit of current.")

    st.markdown("### Current direction: electrons and conventional current")
    direction_a, direction_b = st.columns(2)
    with direction_a:
        st.markdown('<div class="lesson-card"><h4>Electron flow</h4><p>In a metal wire, negatively charged electrons drift from the negative terminal toward the positive terminal.</p></div>', unsafe_allow_html=True)
    with direction_b:
        st.markdown('<div class="lesson-card"><h4>Conventional current</h4><p>By convention, current direction is the direction positive charge would move: from the positive terminal toward the negative terminal through the external circuit. In metal wires it is opposite to electron drift.</p></div>', unsafe_allow_html=True)

    st.markdown("### Circuit meters · connection matters")
    show_image("physics_meter_circuits.svg", "Circuit diagrams: ammeter in series and voltmeter in parallel")
    meter_a, meter_v = st.columns(2)
    with meter_a:
        st.markdown('<div class="lesson-card"><h4>🔵 Ammeter — series</h4><p>Connect an ammeter in series: the circuit current must pass through the meter. An ideal ammeter has very low resistance.</p></div>', unsafe_allow_html=True)
    with meter_v:
        st.markdown('<div class="lesson-card"><h4>🟣 Voltmeter — parallel</h4><p>Connect a voltmeter in parallel across the component to compare the potential difference between its two ends. An ideal voltmeter has very high resistance.</p></div>', unsafe_allow_html=True)

    st.markdown("### Quick concept check")
    st.write("If 12 C of charge passes a point in 3 s, what is the current?")
    answer = st.radio("Choose an answer", ["0.25 A", "4 A", "36 A"], horizontal=True, key="current_quiz")
    if st.button("Check answer", key="current_check"):
        if answer == "4 A":
            st.success("Correct: I = Q / t = 12 C / 3 s = 4 A.")
        else:
            st.info("Use I = Q / t, with charge in coulombs and time in seconds, then try again.")
    source_note()


def thank_you() -> None:
    st.markdown('''
    <main class="tribute-wrap" aria-label="A heartfelt appreciation tribute to Miss Fatima">
      <div class="tribute-eyebrow">With deepest appreciation</div>
      <h1 class="tribute-title">To Our Wonderful<br>Miss Fatima</h1>
      <span class="tribute-heart" role="img" aria-label="Red heart">❤️</span>
      <div class="tribute-rule"></div>
      <div class="tribute-copy">
        <p>Thank you for every moment you gave us, for every lesson you explained, and for every time you patiently repeated something just to make sure we understood.</p>
        <p>Thank you for never giving up on us, for believing in our abilities, and for making even difficult scientific ideas easier to understand.</p>
        <p>Behind every lesson was your effort, behind every explanation was your patience, and behind every success was a teacher who truly cared.</p>
        <p>We may forget some lessons over time, but we will never forget the patience, kindness, and dedication you showed us.</p>
        <p>You are more than a science teacher. You are someone who inspires us to learn, discover, and become better every day.</p>
        <p>Thank you for everything, Miss Fatima. You truly deserve all our appreciation and respect.</p>
      </div>
      <div class="tribute-rule"></div>
      <div class="tribute-signoff">With love and gratitude,<div class="tribute-signature">From your student Hadi,<br>to the best teacher <span class="tribute-signature-heart">❤️</span></div></div>
      <div class="tribute-footer">A teacher remembered with gratitude · Always</div>
    </main>
    ''', unsafe_allow_html=True)


if "page" in st.session_state:
    page = st.session_state.pop("page")
if page == "🏠 Home":
    home()
elif page == "🧬 Biology":
    biology()
elif page == "🧪 Chemistry":
    chemistry()
elif page == "⚡ Physics":
    physics()
else:
    thank_you()
