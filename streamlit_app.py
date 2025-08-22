#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os
import time
from dataclasses import dataclass
from typing import Optional, Tuple

import streamlit as st


# -----------------------------
# Page setup
# -----------------------------

st.set_page_config(
    page_title="Truthlens — Misinformation Scanner",
    page_icon="🔎",
    layout="wide",
)

# Custom CSS to approximate the neon dark theme
st.markdown(
    """
    <style>
    :root {
      --bg-900: #0B0F14;
      --bg-800: #0F1622;
      --text-100: #E6F0FF;
      --text-300: #9BB3C9;
      --line-700: #1B2A3B;
      --blue: #00D4FF;
      --fuchsia: #FF2BD1;
      --green: #39FF88;
      --red: #FF5C5C;
      --radius-lg: 16px;
      --radius-md: 12px;
      --radius-sm: 8px;
      --shadow-glow-blue: 0 0 24px rgba(0, 212, 255, 0.35);
      --shadow-glow-green: 0 0 24px rgba(57, 255, 136, 0.35);
      --shadow-glow-red: 0 0 24px rgba(255, 92, 92, 0.35);
    }

    .truthlens-panel {
      background: var(--bg-800);
      border: 1px solid var(--line-700);
      border-radius: var(--radius-lg);
      padding: 24px;
      color: var(--text-100);
    }
    .truthlens-title {
      font-weight: 700;
      font-size: 22px;
      margin-bottom: 12px;
    }
    .hint { color: var(--text-300); }
    .tab-underline {
      height: 3px;
      border-radius: 2px;
      background: linear-gradient(90deg, var(--blue), var(--fuchsia));
      box-shadow: var(--shadow-glow-blue);
      margin-top: 8px;
      margin-bottom: 2px;
    }
    .dropzone {
      border: 2px dashed var(--line-700);
      border-radius: var(--radius-lg);
      padding: 28px;
      text-align: center;
      color: var(--text-300);
      background: var(--bg-900);
    }
    .verdict-good { color: var(--green); font-weight: 800; font-size: 22px; }
    .verdict-bad { color: var(--red); font-weight: 800; font-size: 22px; }
    .card { background: var(--bg-900); border: 1px solid var(--line-700); border-radius: 12px; padding: 12px; }
    .card-label { color: var(--text-300); font-size: 12px; letter-spacing: 0.04em; }
    .card-value { color: var(--text-100); font-size: 16px; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Utilities
# -----------------------------

@dataclass
class AnalysisResult:
    is_ai_generated: bool
    confidence_pct: int
    resolution: str
    aspect_ratio: str
    file_type: str
    video_length: Optional[str] = None


def deterministic_score(seed: str) -> float:
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    value = int(digest[:8], 16) / 0xFFFFFFFF
    return value


def guess_resolution_and_ratio(source: str) -> Tuple[str, str]:
    lower = source.lower()
    if any(k in lower for k in ["tiktok", "shorts", "reels"]):
        return "1080 × 1920", "9:16"
    if any(k in lower for k in ["instagram", "stories"]):
        return "1080 × 1350", "4:5"
    return "1920 × 1080", "16:9"


def guess_video_length(source: str) -> str:
    score = deterministic_score(source)
    total_secs = 10 + int(score * 160)
    m, s = divmod(total_secs, 60)
    return f"{m:02d}:{s:02d}"


def simulate_analysis_and_results(source: str) -> AnalysisResult:
    res, ratio = guess_resolution_and_ratio(source)
    ext = os.path.splitext(source)[1].lower()
    score = deterministic_score(source)
    confidence = 72 + int(score * 27)
    is_ai = score >= 0.5
    file_type = ext if ext else (".mp4" if "http" in source else ".jpg")
    video_len = guess_video_length(source) if ext in {".mp4", ".mov", ".avi", ".mkv", ".webm"} or ("tiktok" in source.lower() or "youtube" in source.lower()) else None
    return AnalysisResult(
        is_ai_generated=is_ai,
        confidence_pct=confidence,
        resolution=res,
        aspect_ratio=ratio,
        file_type=file_type,
        video_length=video_len,
    )


# -----------------------------
# App Header
# -----------------------------

st.markdown("<div class='truthlens-title'>Truthlens</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='truthlens-panel'>", unsafe_allow_html=True)

    tabs = st.tabs(["URL (Default)", "Media Upload"])

    # URL Tab
    with tabs[0]:
        url_col1, url_col2 = st.columns([6, 1])
        with url_col1:
            url_input = st.text_input(
                "",
                placeholder="Paste any media URL, including links from social media like TikTok, Instagram, and YouTube...",
                label_visibility="collapsed",
            )
            st.caption("Resolving media source…")
        with url_col2:
            submit_url = st.button("Analyze", type="primary", use_container_width=True)

        if submit_url and not url_input:
            st.warning("We couldn’t read that link. Check the URL and try again.")

    # Upload Tab
    with tabs[1]:
        st.markdown("<div class='dropzone'>Drag & Drop a file here or Click to browse.</div>", unsafe_allow_html=True)
        uploaded = st.file_uploader("Upload media", type=["jpg","jpeg","png","webp","bmp","gif","mp4","mov","avi","mkv","webm"], label_visibility="collapsed")
        submit_upload = st.button("Analyze Upload", use_container_width=True)

    st.markdown("<div class='tab-underline'></div>", unsafe_allow_html=True)

    # Trigger analysis
    source: Optional[str] = None
    if submit_url and url_input:
        source = url_input
    elif submit_upload and uploaded is not None:
        # We use the filename as deterministic seed; in real app, save and analyze file bytes
        source = uploaded.name

    # Scan & Analysis simulation
    if source:
        st.divider()
        msg_slot = st.empty()
        progress = st.progress(0, text="Initializing…")
        steps = [
            "Analyzing pixel integrity…",
            "Scanning for artifact patterns…",
            "Cross-referencing data points…",
            "Evaluating compression signatures…",
            "Measuring sensor noise consistency…",
            "Aggregating model inferences…",
        ]
        for i, msg in enumerate(steps, start=1):
            msg_slot.markdown(f"<span class='hint'>{msg}</span>", unsafe_allow_html=True)
            progress.progress(int(i / len(steps) * 100), text=msg)
            time.sleep(0.9)
        msg_slot.empty()

        # Results
        result = simulate_analysis_and_results(source)
        st.success("Analysis complete")

        # Verdict
        verdict_class = "verdict-bad" if result.is_ai_generated else "verdict-good"
        verdict_text = "Likely AI-Generated" if result.is_ai_generated else "Likely Human-Created"
        st.markdown(f"<div class='{verdict_class}'>{verdict_text}</div>", unsafe_allow_html=True)
        st.caption("This is a probabilistic assessment, not an absolute determination.")

        # Data Summary cards
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown("<div class='card'><div class='card-label'>Resolution</div><div class='card-value'>%s</div></div>" % result.resolution, unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='card'><div class='card-label'>Aspect Ratio</div><div class='card-value'>%s</div></div>" % result.aspect_ratio, unsafe_allow_html=True)
        with c3:
            st.markdown("<div class='card'><div class='card-label'>File Type</div><div class='card-value'>%s</div></div>" % result.file_type, unsafe_allow_html=True)
        with c4:
            if result.video_length:
                st.markdown("<div class='card'><div class='card-label'>Video Length</div><div class='card-value'>%s</div></div>" % result.video_length, unsafe_allow_html=True)
            else:
                st.markdown("<div class='card'><div class='card-label'>Video Length</div><div class='card-value'>—</div></div>", unsafe_allow_html=True)

        # Confidence meter
        st.write("Confidence Score")
        conf_bar = st.progress(result.confidence_pct)
        st.write(f"{result.confidence_pct}% likely {'AI-Generated' if result.is_ai_generated else 'Human-Created'}")

    st.markdown("</div>", unsafe_allow_html=True)