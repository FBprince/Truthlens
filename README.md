# Truthlens — Misinformation Scanner

A desktop and web (Streamlit) application concept that helps analyze images/videos to assess whether they are likely human-created or AI-generated. This project ships with:
- A Streamlit web app (`streamlit_app.py`) ready for deployment on Streamlit Community Cloud or GitHub Codespaces
- An optional PySide6 desktop app (`truthlens_app.py`) for local demos

## Features
- URL and Media Upload tabs with animated, neon-themed dark UI
- Drag & Drop file upload or click-to-browse (Streamlit’s uploader)
- Animated scanning screen with rotating analysis messages
- Results dashboard with clear verdict, data summary cards, and confidence meter
- Deterministic, offline analysis simulation (no external APIs)

## Tech
- Python 3.9+
- Streamlit (web)
- PySide6 (optional desktop)

## Install
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run — Streamlit (web)
```bash
streamlit run streamlit_app.py
```
Open the printed local URL in your browser.

## Deploy — Streamlit Community Cloud
1. Push this repo to GitHub
2. Go to Streamlit Community Cloud, create a new app
3. Select your repo and set the entry point to `streamlit_app.py`
4. Framework auto-installs from `requirements.txt`

## Optional — Run desktop (PySide6)
```bash
python truthlens_app.py
```
If running on headless CI:
```bash
QT_QPA_PLATFORM=offscreen python truthlens_app.py --smoke-test
```

## Notes
- The app simulates analysis with a progress/progress bar and rotating messages, then computes a deterministic verdict and confidence based on the input (URL string or filename). This is for demo/UI purposes only.
- To plug in a real detector: replace `simulate_analysis_and_results()` in `streamlit_app.py` and/or `truthlens_app.py` and wire your media parsing and model inference.

## Project Structure
```
requirements.txt
README.md
streamlit_app.py
truthlens_app.py  # optional desktop
```

## License
MIT