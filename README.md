# Miss Fatima's Science Universe 🔬

A professional, mobile-friendly Streamlit learning space for Biology, Chemistry, and Physics.

## What's inside

- **Biology:** Activity slots for Activities 1, 2, 3, 4, and 7, plus a Biology-only Interpret Lab with separate Analysis and Conclusion writing fields.
- **Chemistry:** A Lewis structures introduction, drawing routine, worked examples (H₂, H₂O, CO₂, NH₃, and CH₄), and an interactive practice check.
- **Physics:** Chapter 3 — Electric Current, including the current relationship, units, measurement notes, and a quick concept check.
- **A thank-you page:** “From your student Hadi, to the best teacher ❤️”.
- Dark navy styling, neon-blue accents, responsive layout, and simple subject navigation.

## Lesson-material note

The repository supplied for this project contained no teacher handouts, activity instructions, answer keys, or Chapter 3 notes. To avoid inventing Miss Fatima's specific lesson details, the Biology activity pages are clearly marked as templates and the Biology Interpret Lab asks students to use their assigned observations. Chemistry and Physics pages provide foundational general-science explanations, not a claim to reproduce the teacher's lesson sheets. Add the original class materials when they are available.

## Run locally

Requires Python 3.9 or newer.

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Streamlit prints a local URL (usually `http://localhost:8501`) when the app starts.

## Deploy to Streamlit Community Cloud

1. Push this repository to GitHub (the entry point `app.py` and `requirements.txt` are in the repository root).
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) and connect GitHub if prompted.
3. Choose **Create app**, select `kahwajifawziya-dev/miss-fatima-science-universe`, select the `main` branch, and set the main file path to `app.py`.
4. Deploy. Community Cloud will install the packages listed in `requirements.txt`.

The app does not require secrets, API keys, or external data files.
