# Truthlens — Misinformation Scanner (Desktop, PySide6)

A desktop application concept that helps analyze images/videos to assess whether they are likely human-created or AI-generated. This implementation focuses on the complete UI/UX and an analysis simulation so you can run and demo the flows end-to-end.

## Features
- URL and Media Upload tabs with animated, neon-themed dark UI
- Drag & Drop file upload or click-to-browse
- Animated scanning screen with rotating analysis messages
- Results dashboard with clear verdict, data summary cards, and confidence meter
- Keyboard accessible, with focus rings and Enter-to-submit
- Deterministic, offline analysis simulation (no external APIs)

## Tech
- Python 3.9+
- PySide6 (Qt for Python)

## Install
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run
```bash
python truthlens_app.py
```

If running on a headless machine (CI), you can launch in offscreen mode:
```bash
QT_QPA_PLATFORM=offscreen python truthlens_app.py --smoke-test
```

## Notes
- The app simulates analysis with a progress/spinner and rotating messages, then computes a deterministic verdict and confidence based on the input (URL string or file path). This is for demo/UI purposes only.
- To plug in a real detector: replace `simulate_analysis_and_results()` and wire your media parsing and model inference where indicated in comments.

## Project Structure
```
requirements.txt
README.md
truthlens_app.py
```

## License
MIT