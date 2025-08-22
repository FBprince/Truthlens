#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import hashlib
import random
import argparse
from dataclasses import dataclass
from typing import Optional, Dict, Tuple

from PySide6.QtCore import Qt, QTimer, QSize, QPoint, QEasingCurve
from PySide6.QtGui import QIcon, QPalette, QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QFileDialog,
    QFrame,
    QProgressBar,
    QStackedWidget,
    QMessageBox,
)


# -----------------------------
# Design tokens (QSS variables)
# -----------------------------

def get_app_stylesheet() -> str:
    return (
        """
        * { font-family: 'Montserrat', 'Poppins', 'Segoe UI', 'Inter', sans-serif; }

        /* Backgrounds & Text */
        QMainWindow { background: #0B0F14; }
        QWidget#Panel { background: #0F1622; border-radius: 16px; border: 1px solid #1B2A3B; }
        QLabel, QLineEdit, QPushButton { color: #E6F0FF; }
        QLabel.hint { color: #9BB3C9; }

        /* Buttons */
        QPushButton.primary {
            background: #00D4FF; color: #0B0F14; border: none; border-radius: 10px; padding: 10px 16px;
        }
        QPushButton.primary:hover { filter: brightness(1.05); }
        QPushButton.primary:disabled { background: #1B2A3B; color: #9BB3C9; }

        /* Tab buttons */
        QPushButton.tab {
            background: transparent; border: none; color: #9BB3C9; padding: 8px 12px; font-weight: 600;
        }
        QPushButton.tab:hover { color: #E6F0FF; }
        QPushButton.tab[active="true"] { color: #E6F0FF; }

        /* Underlines for tabs */
        QFrame#TabUnderline { background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #00D4FF, stop:1 #FF2BD1); height: 3px; border-radius: 2px; }

        /* Input */
        QLineEdit.url {
            background: #0B0F14; border: 1px solid #1B2A3B; border-radius: 12px; padding: 12px 14px;
            selection-background-color: #26465e; selection-color: #E6F0FF;
        }
        QLineEdit.url:focus { border-color: #00D4FF; }

        /* Search button embedded */
        QPushButton.search {
            background: #0F1622; border: 1px solid #1B2A3B; border-left: none; border-top-right-radius: 12px; border-bottom-right-radius: 12px;
            padding: 10px 12px; min-width: 44px;
        }
        QPushButton.search:hover { border-color: #00D4FF; }

        /* Dropzone */
        QWidget#Dropzone {
            background: #0B0F14; border: 2px dashed #1B2A3B; border-radius: 16px;
        }
        QWidget#Dropzone[hover="true"] { border-color: #00D4FF; }

        /* Progress */
        QProgressBar {
            border: 1px solid #1B2A3B; border-radius: 10px; background: #0B0F14; text-align: center; color: #E6F0FF;
        }
        QProgressBar::chunk { background: #00D4FF; border-radius: 10px; }

        /* Cards */
        QFrame.card { background: #0B0F14; border: 1px solid #1B2A3B; border-radius: 12px; }
        QLabel.card-label { color: #9BB3C9; font-size: 12px; letter-spacing: 0.04em; }
        QLabel.card-value { color: #E6F0FF; font-size: 16px; font-weight: 600; }

        /* Confidence Meter */
        QProgressBar#Confidence::chunk { background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #39FF88, stop:1 #00D4FF); }

        /* Verdicts */
        QLabel.verdict-good { color: #39FF88; font-size: 24px; font-weight: 700; }
        QLabel.verdict-bad { color: #FF5C5C; font-size: 24px; font-weight: 700; }

        /* Focus cues */
        *:focus { outline: 2px solid rgba(0, 212, 255, 0.6); outline-offset: 2px; }
        """
    )


# -----------------------------
# Utilities and Data
# -----------------------------

SCAN_MESSAGES = [
    "Analyzing pixel integrity...",
    "Scanning for artifact patterns...",
    "Cross-referencing data points...",
    "Evaluating compression signatures...",
    "Measuring sensor noise consistency...",
    "Aggregating model inferences...",
]

VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm"}
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif"}


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
    # Map first 8 hex chars to int, then to [0,1)
    value = int(digest[:8], 16) / 0xFFFFFFFF
    return value


def guess_resolution_and_ratio(source: str) -> Tuple[str, str]:
    # Heuristic defaults, tweak based on URL hints
    lower = source.lower()
    if any(k in lower for k in ["tiktok", "shorts", "reels"]):
        return "1080 × 1920", "9:16"
    if any(k in lower for k in ["instagram", "stories"]):
        return "1080 × 1350", "4:5"
    # default landscape
    return "1920 × 1080", "16:9"


def guess_video_length(source: str) -> str:
    # Simple deterministic pseudo-length
    score = deterministic_score(source)
    total_secs = 10 + int(score * 160)  # 10s to ~170s
    m, s = divmod(total_secs, 60)
    return f"{m:02d}:{s:02d}"


def simulate_analysis_and_results(source: str) -> AnalysisResult:
    res, ratio = guess_resolution_and_ratio(source)
    ext = os.path.splitext(source)[1].lower()

    score = deterministic_score(source)
    # Confidence tilted away from 50/50 to be more decisive for demo
    confidence = 72 + int(score * 27)  # 72–99
    is_ai = score >= 0.5

    file_type = ext if ext else (".mp4" if "http" in source else ".jpg")
    video_len = guess_video_length(source) if ext in VIDEO_EXTS or ("tiktok" in source.lower() or "youtube" in source.lower()) else None

    return AnalysisResult(
        is_ai_generated=is_ai,
        confidence_pct=confidence,
        resolution=res,
        aspect_ratio=ratio,
        file_type=file_type,
        video_length=video_len,
    )


# -----------------------------
# UI Components
# -----------------------------

class Header(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        title = QLabel("Truthlens")
        title.setStyleSheet("font-size: 22px; font-weight: 700; letter-spacing: 0.2px;")

        layout.addWidget(title)
        layout.addStretch(1)

        about_btn = QPushButton("About")
        about_btn.setObjectName("AboutBtn")
        about_btn.setProperty("class", "secondary")
        about_btn.clicked.connect(self._show_about)

        layout.addWidget(about_btn)

    def _show_about(self):
        QMessageBox.information(
            self, "About Truthlens",
            "Truthlens UI demo built with PySide6.\n\n"
            "This demo simulates analysis to showcase the user experience."
        )


class TabSwitcher(QWidget):
    def __init__(self, on_tab_changed, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.on_tab_changed = on_tab_changed
        self.active = "url"

        self.setContentsMargins(0, 0, 0, 0)
        wrap = QVBoxLayout(self)
        wrap.setContentsMargins(0, 0, 0, 0)
        wrap.setSpacing(6)

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(12)

        self.url_btn = QPushButton("URL (Default)")
        self.url_btn.setProperty("class", "tab")
        self.url_btn.setCheckable(True)
        self.url_btn.setChecked(True)
        self.url_btn.clicked.connect(lambda: self._activate("url"))

        self.upload_btn = QPushButton("Media Upload")
        self.upload_btn.setProperty("class", "tab")
        self.upload_btn.setCheckable(True)
        self.upload_btn.clicked.connect(lambda: self._activate("upload"))

        row.addWidget(self.url_btn)
        row.addWidget(self.upload_btn)
        row.addStretch(1)

        wrap.addLayout(row)

        # Underline container
        self.underline = QFrame()
        self.underline.setObjectName("TabUnderline")
        self.underline.setFixedHeight(3)
        wrap.addWidget(self.underline)

        self._refresh_styles()

    def _activate(self, tab_id: str):
        if self.active == tab_id:
            return
        self.active = tab_id
        self._refresh_styles()
        if self.on_tab_changed:
            self.on_tab_changed(tab_id)

    def _refresh_styles(self):
        self.url_btn.setProperty("active", str(self.active == "url").lower())
        self.upload_btn.setProperty("active", str(self.active == "upload").lower())
        self.style().unpolish(self.url_btn)
        self.style().polish(self.url_btn)
        self.style().unpolish(self.upload_btn)
        self.style().polish(self.upload_btn)
        # Move underline under the active button by setting margins
        # We approximate by aligning to left for URL and mid for Upload
        if self.active == "url":
            self.underline.setContentsMargins(10, 0, 200, 0)
        else:
            self.underline.setContentsMargins(160, 0, 50, 0)


class UrlInput(QWidget):
    def __init__(self, on_submit, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.on_submit = on_submit

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Paste any media URL, including links from social media like TikTok, Instagram, and YouTube...")
        self.input.setProperty("class", "url")
        self.input.returnPressed.connect(self._submit)

        self.search_btn = QPushButton("🔎")
        self.search_btn.setToolTip("Analyze")
        self.search_btn.setProperty("class", "search")
        self.search_btn.clicked.connect(self._submit)

        layout.addWidget(self.input, 1)
        layout.addWidget(self.search_btn, 0)

        hint = QLabel("Resolving media source…")
        hint.setProperty("class", "hint")
        hint.setContentsMargins(2, 6, 2, 0)

        wrap = QVBoxLayout()
        wrap.setContentsMargins(0, 0, 0, 0)
        wrap.setSpacing(6)
        wrap.addLayout(layout)
        wrap.addWidget(hint)
        self.setLayout(wrap)

    def _submit(self):
        text = self.input.text().strip()
        if not text:
            QMessageBox.warning(self, "Invalid URL", "We couldn’t read that link. Check the URL and try again.")
            return
        self.on_submit(text)


class Dropzone(QWidget):
    def __init__(self, on_file, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.on_file = on_file
        self.setObjectName("Dropzone")
        self.setAcceptDrops(True)
        self._hover = False

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(16, 16, 16, 16)

        icon = QLabel("⬆")
        icon.setStyleSheet("font-size: 28px;")
        text = QLabel("Drag & Drop a file here or Click to browse.")
        text.setStyleSheet("color: #9BB3C9; font-size: 14px;")

        layout.addWidget(icon, alignment=Qt.AlignHCenter)
        layout.addSpacing(8)
        layout.addWidget(text, alignment=Qt.AlignHCenter)

    def sizeHint(self) -> QSize:
        return QSize(560, 200)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            path, _ = QFileDialog.getOpenFileName(self, "Select Media", os.path.expanduser("~"),
                                                  "Media Files (*.jpg *.jpeg *.png *.webp *.bmp *.gif *.mp4 *.mov *.avi *.mkv *.webm);;All Files (*)")
            if path:
                self.on_file(path)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self._set_hover(True)
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self._set_hover(False)

    def dropEvent(self, event):
        self._set_hover(False)
        for url in event.mimeData().urls():
            local_path = url.toLocalFile()
            if local_path:
                self.on_file(local_path)
                break

    def _set_hover(self, value: bool):
        self._hover = value
        self.setProperty("hover", str(value).lower())
        self.style().unpolish(self)
        self.style().polish(self)


class ScanView(QWidget):
    def __init__(self, on_done, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.on_done = on_done

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layout.setSpacing(16)

        self.title = QLabel("Analyzing…")
        self.title.setStyleSheet("font-size: 18px; font-weight: 600;")

        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(0)  # indeterminate
        self.progress.setFixedWidth(360)

        self.message = QLabel(SCAN_MESSAGES[0])
        self.message.setProperty("class", "hint")

        layout.addWidget(self.title)
        layout.addWidget(self.progress)
        layout.addWidget(self.message)

        self._msg_index = 0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)

    def start(self):
        self._msg_index = 0
        self.message.setText(SCAN_MESSAGES[self._msg_index])
        self._timer.start(1600)
        # Simulate total duration ~7 seconds
        QTimer.singleShot(7000, self._finish)

    def _tick(self):
        self._msg_index = (self._msg_index + 1) % len(SCAN_MESSAGES)
        self.message.setText(SCAN_MESSAGES[self._msg_index])

    def _finish(self):
        self._timer.stop()
        if self.on_done:
            self.on_done()


class DataCard(QFrame):
    def __init__(self, label: str, value: str, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setProperty("class", "card")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(6)
        lab = QLabel(label)
        lab.setProperty("class", "card-label")
        val = QLabel(value)
        val.setProperty("class", "card-value")
        layout.addWidget(lab)
        layout.addWidget(val)


class ResultsView(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setSpacing(16)

        self.verdict_label = QLabel("")
        self.verdict_label.setAlignment(Qt.AlignHCenter)

        self.disclaimer = QLabel("This is a probabilistic assessment, not an absolute determination.")
        self.disclaimer.setProperty("class", "hint")
        self.disclaimer.setAlignment(Qt.AlignHCenter)

        cards_row = QHBoxLayout()
        cards_row.setSpacing(12)
        self.card_resolution = DataCard("Resolution", "–")
        self.card_ratio = DataCard("Aspect Ratio", "–")
        self.card_type = DataCard("File Type", "–")
        self.card_length = DataCard("Video Length", "–")
        cards_row.addWidget(self.card_resolution)
        cards_row.addWidget(self.card_ratio)
        cards_row.addWidget(self.card_type)
        cards_row.addWidget(self.card_length)

        # Confidence meter
        conf_wrap = QVBoxLayout()
        conf_label = QLabel("Confidence Score")
        conf_label.setProperty("class", "card-label")
        self.conf_bar = QProgressBar()
        self.conf_bar.setObjectName("Confidence")
        self.conf_bar.setMinimum(0)
        self.conf_bar.setMaximum(100)
        self.conf_bar.setFormat("%p%")

        conf_wrap.addWidget(conf_label)
        conf_wrap.addWidget(self.conf_bar)

        layout.addWidget(self.verdict_label)
        layout.addWidget(self.disclaimer)
        layout.addLayout(cards_row)
        layout.addLayout(conf_wrap)

        # Actions
        actions = QHBoxLayout()
        actions.addStretch(1)
        self.another_btn = QPushButton("Analyze another media")
        self.another_btn.setProperty("class", "primary")
        actions.addWidget(self.another_btn)
        layout.addLayout(actions)

    def set_results(self, result: AnalysisResult):
        if result.is_ai_generated:
            self.verdict_label.setText("Likely AI-Generated")
            self.verdict_label.setProperty("class", "verdict-bad")
            self.conf_bar.setStyleSheet(
                "QProgressBar#Confidence::chunk { background: qlineargradient(x1:0,y1:0,x2:1,y2:0, stop:0 #FF5C5C, stop:1 #FF2BD1); }"
            )
        else:
            self.verdict_label.setText("Likely Human-Created")
            self.verdict_label.setProperty("class", "verdict-good")
            self.conf_bar.setStyleSheet("")

        self.style().unpolish(self.verdict_label)
        self.style().polish(self.verdict_label)

        self.card_resolution.layout().itemAt(1).widget().setText(result.resolution)
        self.card_ratio.layout().itemAt(1).widget().setText(result.aspect_ratio)
        self.card_type.layout().itemAt(1).widget().setText(result.file_type)
        if result.video_length:
            self.card_length.show()
            self.card_length.layout().itemAt(1).widget().setText(result.video_length)
        else:
            self.card_length.hide()

        self.conf_bar.setValue(result.confidence_pct)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Truthlens — Misinformation Scanner")
        self.setMinimumSize(920, 640)

        container = QWidget()
        container.setObjectName("Panel")
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(24, 24, 24, 24)
        container_layout.setSpacing(18)

        self.header = Header()
        container_layout.addWidget(self.header)

        self.tabs = TabSwitcher(self._on_tab_changed)
        container_layout.addWidget(self.tabs)

        # Stacked main area
        self.stack = QStackedWidget()

        # URL view
        self.url_view = QWidget()
        v1 = QVBoxLayout(self.url_view)
        v1.setSpacing(12)
        v1.addStretch(1)
        self.url_input = UrlInput(self._submit_url)
        v1.addWidget(self.url_input)
        v1.addStretch(2)

        # Upload view
        self.upload_view = QWidget()
        v2 = QVBoxLayout(self.upload_view)
        v2.setSpacing(12)
        v2.addStretch(1)
        self.dropzone = Dropzone(self._submit_file)
        v2.addWidget(self.dropzone)
        v2.addStretch(2)

        # Scan view
        self.scan_view = ScanView(self._scan_done)

        # Results view
        self.results_view = ResultsView()
        self.results_view.another_btn.clicked.connect(self._reset_to_input)

        # Add to stack
        for w in (self.url_view, self.upload_view, self.scan_view, self.results_view):
            self.stack.addWidget(w)

        container_layout.addWidget(self.stack, 1)

        central = QWidget()
        outer = QVBoxLayout(central)
        outer.setContentsMargins(24, 24, 24, 24)
        outer.addWidget(container, 1)
        self.setCentralWidget(central)

        # State
        self._last_source: Optional[str] = None

        self._apply_styles()
        self._on_tab_changed("url")

        # Accessibility: shortcuts
        self._add_shortcuts()

    def _add_shortcuts(self):
        # Enter key submits when URL tab active
        submit_action = QAction(self)
        submit_action.setShortcut(Qt.Key_Return)
        submit_action.triggered.connect(lambda: self._submit_url(self.url_input.input.text()))
        self.addAction(submit_action)

    def _apply_styles(self):
        self.setStyleSheet(get_app_stylesheet())

    def _on_tab_changed(self, tab_id: str):
        if tab_id == "url":
            self.stack.setCurrentWidget(self.url_view)
            self.url_input.input.setFocus()
        else:
            self.stack.setCurrentWidget(self.upload_view)

    # --- Submit handlers ---
    def _submit_url(self, url: str):
        url = (url or "").strip()
        if not url:
            QMessageBox.warning(self, "Invalid URL", "We couldn’t read that link. Check the URL and try again.")
            return
        self._start_scan(url)

    def _submit_file(self, path: str):
        if not path or not os.path.exists(path):
            QMessageBox.warning(self, "Unsupported", "This format isn’t supported yet.")
            return
        self._start_scan(path)

    def _start_scan(self, source: str):
        self._last_source = source
        self.stack.setCurrentWidget(self.scan_view)
        QApplication.processEvents()
        self.scan_view.start()

    def _scan_done(self):
        # Produce results
        assert self._last_source is not None
        result = simulate_analysis_and_results(self._last_source)
        self.results_view.set_results(result)
        self.stack.setCurrentWidget(self.results_view)

    def _reset_to_input(self):
        # Reset to whichever tab is active
        if self.tabs.active == "url":
            self.stack.setCurrentWidget(self.url_view)
            self.url_input.input.setFocus()
        else:
            self.stack.setCurrentWidget(self.upload_view)


# -----------------------------
# Entrypoint
# -----------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description="Truthlens UI Demo")
    parser.add_argument("--smoke-test", action="store_true", help="Run without showing the window (CI/offscreen)")
    args = parser.parse_args(argv)

    app = QApplication(sys.argv)
    win = MainWindow()

    if args.smoke_test:
        # Do not show, just ensure widgets create without error
        QTimer.singleShot(100, app.quit)
    else:
        win.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())