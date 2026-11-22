"""Miss Fatima's Science Universe — an interactive Streamlit learning space."""

from html import escape

import streamlit as st

st.set_page_config(
    page_title="Miss Fatima's Science Universe",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# The repository did not contain teacher-provided lesson sheets. Activity pages
# therefore remain clearly labeled templates rather than invented instructions.
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { --ink:#eef5ff; --muted:#a9bad3; --blue:#53c8ff; --cyan:#7af4ff; --panel:#101d35; }
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
footer { color:#8295af; text-align:center; padding:2.5rem 0 1rem; font-size:.85rem; }
.stButton>button { border-radius:11px; border:1px solid rgba(83,200,255,.5); }
@media (max-width: 700px) { .hero { padding:1.4rem; border-radius:18px; } .card { min-height:unset; } }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

PAGES = [
    "🏠 Home",
    "🧬 Biology",
    "🧪 Chemistry",
    "⚡ Physics",
    "💙 Thank You",
]

with st.sidebar:
    st.markdown("## 🔬 Science Universe")
    st.caption("A learning space with Miss Fatima")
    page = st.radio("Explore", PAGES, label_visibility="collapsed")
    st.divider()
    st.markdown("**Your subjects**")
    st.markdown('<span class="pill">Biology</span><span class="pill">Chemistry</span><span class="pill">Physics</span>', unsafe_allow_html=True)
    st.markdown("\n")
    st.caption("Curiosity starts with a question ✨")


def hero(kicker: str, title: str, intro: str) -> None:
    st.markdown(
        f'<section class="hero"><div class="eyebrow">{escape(kicker)}</div>'
        f'<h1>{escape(title)}</h1><p>{escape(intro)}</p></section>',
        unsafe_allow_html=True,
    )


def card(icon: str, title: str, description: str) -> None:
    st.markdown(
        f'<div class="card"><div class="icon">{icon}</div><h3>{escape(title)}</h3>'
        f'<p>{escape(description)}</p></div>',
        unsafe_allow_html=True,
    )


def source_note() -> None:
    st.markdown(
        '<div class="note"><strong>About the lesson materials:</strong> The project did not include '
        'the teacher’s activity sheets or chapter notes. The activity slots below are intentionally '
        'left as templates; no teacher-specific instructions or answers have been made up.</div>',
        unsafe_allow_html=True,
    )


def home() -> None:
    hero("WELCOME, SCIENTIST", "Miss Fatima���s Science Universe", "Explore biology, chemistry, and physics in one bright, interactive learning space. Pick a subject and let your curiosity lead the way.")
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
    st.markdown("<footer>Made for curious minds · Learn at your own pace</footer>", unsafe_allow_html=True)


def biology() -> None:
    hero("LIFE SCIENCE", "Biology", "Choose one of the requested activities, or open the Interpret Lab to organize your analysis and conclusion.")
    activity = st.selectbox("Biology activity", ["Activity 1", "Activity 2", "Activity 3", "Activity 4", "Activity 7", "Interpret Lab (Analysis + Conclusion)"])
    if activity == "Interpret Lab (Analysis + Conclusion)":
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
    else:
        st.markdown(f"### 🌱 {activity}")
        st.info(f"The instructions, topic, and answer key for {activity} were not included in the project materials. This activity slot is ready for the original class handout—no details have been invented.")
        st.markdown("**Class material**")
        st.text_area("Paste or write the teacher-provided activity prompt here for your own session.", key=f"{activity}_notes", height=150, placeholder="Teacher-provided prompt and notes…")
        st.caption("This text stays in the current app session and is not saved to the repository.")
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
    st.write("A Lewis structure is a model that shows valence electrons: shared pairs form covalent bonds, and unshared pairs are lone pairs. For the common main-group examples below, hydrogen is shown with a duet and the other atoms with an octet.")
    st.markdown("#### A useful drawing routine")
    steps = st.columns(4)
    step_text = [("01 · Count", "Add the valence electrons contributed by the atoms."), ("02 · Connect", "Choose a central atom (hydrogen is never central) and draw single bonds."), ("03 · Complete", "Give outer atoms their duet or octet, then place remaining electrons on the center."), ("04 · Check", "Check the total electron count and octets; use multiple bonds if needed." )]
    for col, (title, text) in zip(steps, step_text):
        with col: card("✦", title, text)
    st.markdown("### Worked examples")
    selected = st.selectbox("Choose a molecule", list(LEWIS_EXAMPLES))
    structure, explanation = LEWIS_EXAMPLES[selected]
    st.markdown(f'<div class="formula">{escape(structure)}</div>', unsafe_allow_html=True)
    st.write(explanation)
    with st.expander("Try a quick check"):
        st.write("In the selected example, identify the central atom (if there is one) and count its bonding pairs and lone pairs.")
        response = st.text_input("Your answer", key="lewis_answer", placeholder="For example: 2 bonding pairs and 2 lone pairs")
        if st.button("Show the check", key="lewis_check"):
            st.success(f"Use this structure to check your answer: {structure}. {explanation}")
    st.caption("These are foundational examples, not a substitute for Miss Fatima’s specific class notes or required drawing conventions.")


def physics() -> None:
    hero("PHYSICS · CHAPTER 3", "Electric Current", "A concise foundation for thinking about current, charge flow, and its measurement.")
    st.markdown("### What is electric current?")
    st.write("Electric current describes how quickly electric charge passes a point in a circuit. The conventional-current direction is the direction positive charge would move; in a metal wire, electrons drift in the opposite direction.")
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
    st.caption("This is a general introductory overview. The actual Chapter 3 notes, scope, and examples were not present in the repository; follow the class materials where they differ.")


def thank_you() -> None:
    hero("A NOTE FROM THE HEART", "Thank you, Miss Fatima", "For the patience, encouragement, and spark that make learning an adventure.")
    st.markdown("<div class=" + '"hero"' + " style=\"text-align:center;padding:3.2rem 1.5rem\"><div style=\"font-size:clamp(1.7rem,5vw,3rem);font-family:'Space Grotesk',sans-serif;color:#f2f8ff\">From your student Hadi,<br>to the best teacher ❤️</div><div style=\"color:#9ce8ff;margin-top:1rem;font-size:1.1rem\">Thank you for helping curiosity grow. ✨</div></div>", unsafe_allow_html=True)


# Persist navigation from the home-page jump selector.
if "page" in st.session_state:
    page = st.session_state.pop("page")

if page == "🏠 Home": home()
elif page == "🧬 Biology": biology()
elif page == "🧪 Chemistry": chemistry()
elif page == "⚡ Physics": physics()
else: thank_you()
