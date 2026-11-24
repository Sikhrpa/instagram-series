"""
SikhRPA Instagram Content Series — Shared Brand Tokens & HTML/CSS Templates
Brand Colors:
  - Primary Navy:  #0f172a
  - Heritage Gold: #d97706 (highlight #f59e0b, soft tint #fef3c7)
  - Royal Blue:    #1e3a8a (highlight #3b82f6)
Typography:
  - English:  Inter (Display / UI)
  - Gurmukhi: Noto Sans Gurmukhi / Noto Serif Gurmukhi
"""

from __future__ import annotations

import base64
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
LOGO_PATH = ROOT_DIR / "assets" / "srpa-logo.png"

_LOGO_DATA_URI: str | None = None


def get_logo_data_uri() -> str:
    global _LOGO_DATA_URI
    if _LOGO_DATA_URI is None:
        raw = LOGO_PATH.read_bytes()
        b64 = base64.b64encode(raw).decode("ascii")
        _LOGO_DATA_URI = f"data:image/png;base64,{b64}"
    return _LOGO_DATA_URI


BASE_CSS = """
@charset "UTF-8";
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --navy-950: #090e1a;
  --navy-900: #0f172a;
  --navy-800: #16223a;
  --navy-700: #1e293b;
  --blue-900: #1e3a8a;
  --blue-600: #2563eb;
  --blue-400: #60a5fa;
  --gold-600: #d97706;
  --gold-500: #f59e0b;
  --gold-400: #fbbf24;
  --gold-100: #fef3c7;
  --emerald-500: #10b981;
  --emerald-400: #34d399;
  --red-500: #ef4444;
  --red-400: #f87171;
  --slate-50: #f8fafc;
  --slate-200: #e2e8f0;
  --slate-300: #cbd5e1;
  --slate-400: #94a3b8;
  --border-subtle: rgba(255, 255, 255, 0.11);
  --border-gold: rgba(217, 119, 6, 0.45);
}

html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: var(--navy-900);
  color: var(--slate-50);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-rendering: geometricPrecision;
}

.gurmukhi {
  font-family: 'Noto Sans Gurmukhi', 'Noto Sans Gurmukhi UI', sans-serif;
  line-height: 1.62;
  letter-spacing: 0;
}

.gurmukhi-serif {
  font-family: 'Noto Serif Gurmukhi', 'Noto Sans Gurmukhi', serif;
  line-height: 1.7;
  letter-spacing: 0;
}

.canvas {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background:
    radial-gradient(ellipse 85% 55% at 88% 8%, rgba(30, 58, 138, 0.42) 0%, rgba(15, 23, 42, 0) 68%),
    radial-gradient(ellipse 70% 50% at 10% 92%, rgba(217, 119, 6, 0.16) 0%, rgba(15, 23, 42, 0) 65%),
    linear-gradient(165deg, #0f172a 0%, #0b1222 55%, #0f172a 100%);
  overflow: hidden;
}

.canvas.theme-royal {
  background:
    radial-gradient(ellipse 90% 60% at 50% 0%, rgba(30, 58, 138, 0.58) 0%, rgba(15, 23, 42, 0) 72%),
    radial-gradient(ellipse 65% 45% at 85% 95%, rgba(217, 119, 6, 0.2) 0%, rgba(15, 23, 42, 0) 65%),
    linear-gradient(170deg, #0f172a 0%, #101b36 52%, #0c1324 100%);
}

.canvas.theme-trauma {
  background:
    radial-gradient(ellipse 80% 50% at 88% 6%, rgba(185, 28, 28, 0.26) 0%, rgba(15, 23, 42, 0) 65%),
    radial-gradient(ellipse 70% 50% at 10% 94%, rgba(30, 58, 138, 0.35) 0%, rgba(15, 23, 42, 0) 65%),
    linear-gradient(165deg, #0f172a 0%, #0c1220 60%, #111827 100%);
}

.canvas.theme-shaheedi {
  background:
    radial-gradient(ellipse 80% 50% at 50% 10%, rgba(217, 119, 6, 0.18) 0%, rgba(11, 17, 32, 0) 68%),
    radial-gradient(ellipse 70% 45% at 50% 92%, rgba(30, 58, 138, 0.28) 0%, rgba(11, 17, 32, 0) 65%),
    linear-gradient(180deg, #0a101f 0%, #0f172a 55%, #090d19 100%);
}

/* Subtle precision architectural grid */
.canvas::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.024) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.024) 1px, transparent 1px);
  background-size: 54px 54px;
  pointer-events: none;
  z-index: 0;
}

.top-accent-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 8px;
  background: linear-gradient(90deg, #1e3a8a 0%, #d97706 48%, #f59e0b 72%, #1e3a8a 100%);
  z-index: 5;
}

.canvas.theme-trauma .top-accent-bar {
  background: linear-gradient(90deg, #dc2626 0%, #d97706 55%, #1e3a8a 100%);
}

.canvas.theme-shaheedi .top-accent-bar {
  background: linear-gradient(90deg, #92400e 0%, #d97706 50%, #92400e 100%);
}

.frame-4x5 {
  padding: 46px 56px 40px 56px;
}

.frame-9x16 {
  padding: 155px 60px 215px 60px;
}

.frame-9x16.reel-cover {
  padding: 250px 60px 250px 60px;
}

.frame-9x16.story-frame {
  padding: 160px 60px 180px 60px;
}

.slide-header,
.slide-body,
.slide-footer {
  position: relative;
  z-index: 2;
}

/* Header bar */
.slide-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding-bottom: 18px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.brand-lockup {
  display: flex;
  align-items: center;
  gap: 14px;
}

.brand-logo {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  object-fit: contain;
  background: #0b1222;
  border: 2px solid rgba(217, 119, 6, 0.65);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.45);
}

.brand-meta {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.brand-name {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: 0.06em;
  color: #f8fafc;
  text-transform: uppercase;
}

.brand-sub {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: #fbbf24;
  text-transform: uppercase;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 18px;
  border-radius: 999px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  border: 1px solid var(--border-gold);
  background: rgba(217, 119, 6, 0.16);
  color: #fde68a;
}

.pill-blue {
  border-color: rgba(96, 165, 250, 0.4);
  background: rgba(30, 58, 138, 0.55);
  color: #dbeafe;
}

.pill-red {
  border-color: rgba(248, 113, 113, 0.45);
  background: rgba(185, 28, 28, 0.28);
  color: #fecaca;
}

.pill-emerald {
  border-color: rgba(52, 211, 153, 0.45);
  background: rgba(6, 95, 70, 0.35);
  color: #a7f3d0;
}

.slide-counter {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: #94a3b8;
  padding: 7px 14px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.09);
}

.slide-counter span {
  color: #fbbf24;
}

/* Main Body */
.slide-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 22px;
  padding: 22px 0;
  min-height: 0;
}

.slide-body.top-align {
  justify-content: flex-start;
  padding-top: 24px;
}

/* Typography */
.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-size: 17px;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #f59e0b;
}

.eyebrow::before {
  content: "";
  width: 28px;
  height: 3px;
  border-radius: 2px;
  background: #f59e0b;
}

.h1-hero {
  font-family: 'Inter Display', 'Inter', sans-serif;
  font-size: 62px;
  font-weight: 900;
  line-height: 1.07;
  letter-spacing: -0.025em;
  color: #ffffff;
}

.h1-lg {
  font-family: 'Inter Display', 'Inter', sans-serif;
  font-size: 52px;
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -0.022em;
  color: #ffffff;
}

.h2-title {
  font-family: 'Inter Display', 'Inter', sans-serif;
  font-size: 42px;
  font-weight: 800;
  line-height: 1.14;
  letter-spacing: -0.02em;
  color: #ffffff;
}

.h3-title {
  font-family: 'Inter Display', 'Inter', sans-serif;
  font-size: 30px;
  font-weight: 800;
  line-height: 1.2;
  letter-spacing: -0.015em;
  color: #ffffff;
}

.gold { color: #fbbf24; }
.gold-deep { color: #f59e0b; }
.blue-lt { color: #93c5fd; }
.emerald { color: #34d399; }
.red-lt { color: #fca5a5; }
.muted { color: #94a3b8; }

.lead {
  font-size: 25px;
  line-height: 1.44;
  color: #cbd5e1;
  font-weight: 400;
}

.body-text {
  font-size: 21px;
  line-height: 1.44;
  color: #cbd5e1;
}

.body-sm {
  font-size: 18px;
  line-height: 1.42;
  color: #cbd5e1;
}

.pa-banner {
  background: linear-gradient(135deg, rgba(217, 119, 6, 0.16) 0%, rgba(30, 58, 138, 0.28) 100%);
  border: 1px solid rgba(245, 158, 11, 0.42);
  border-left: 6px solid #f59e0b;
  border-radius: 16px;
  padding: 18px 24px;
}

.pa-text-lg {
  font-family: 'Noto Sans Gurmukhi', sans-serif;
  font-size: 29px;
  font-weight: 700;
  line-height: 1.58;
  color: #fef3c7;
}

.pa-text-md {
  font-family: 'Noto Sans Gurmukhi', sans-serif;
  font-size: 23px;
  font-weight: 600;
  line-height: 1.6;
  color: #fde68a;
}

.pa-text-sm {
  font-family: 'Noto Sans Gurmukhi', sans-serif;
  font-size: 19px;
  font-weight: 500;
  line-height: 1.6;
  color: #fde68a;
}

/* Cards & Grids */
.card {
  background: rgba(22, 34, 58, 0.78);
  border: 1px solid var(--border-subtle);
  border-radius: 20px;
  padding: 24px 26px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.28);
}

.card-gold {
  background: linear-gradient(155deg, rgba(217, 119, 6, 0.15) 0%, rgba(22, 34, 58, 0.88) 65%);
  border: 1px solid rgba(245, 158, 11, 0.42);
}

.card-blue {
  background: linear-gradient(155deg, rgba(30, 58, 138, 0.45) 0%, rgba(15, 23, 42, 0.9) 75%);
  border: 1px solid rgba(96, 165, 250, 0.32);
}

.card-emerald {
  background: linear-gradient(155deg, rgba(16, 185, 129, 0.14) 0%, rgba(15, 23, 42, 0.9) 75%);
  border: 1px solid rgba(52, 211, 153, 0.38);
}

.card-red {
  background: linear-gradient(155deg, rgba(239, 68, 68, 0.16) 0%, rgba(15, 23, 42, 0.9) 75%);
  border: 1px solid rgba(248, 113, 113, 0.38);
}

.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.stack {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.stack-sm {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.row {
  display: flex;
  align-items: center;
  gap: 16px;
}

.num-badge {
  flex-shrink: 0;
  width: 48px;
  height: 48px;
  border-radius: 14px;
  background: linear-gradient(135deg, #d97706 0%, #f59e0b 100%);
  color: #0f172a;
  font-size: 24px;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 18px rgba(217, 119, 6, 0.35);
}

.num-badge-blue {
  background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
  color: #ffffff;
  box-shadow: 0 6px 18px rgba(30, 58, 138, 0.45);
}

.num-badge-red {
  background: linear-gradient(135deg, #b91c1c 0%, #ef4444 100%);
  color: #ffffff;
}

.stat-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.stat-box {
  background: rgba(15, 23, 42, 0.72);
  border: 1px solid rgba(245, 158, 11, 0.3);
  border-radius: 16px;
  padding: 18px 16px;
  text-align: center;
}

.stat-val {
  font-family: 'Inter Display', 'Inter', sans-serif;
  font-size: 36px;
  font-weight: 900;
  color: #fbbf24;
  line-height: 1.1;
}

.stat-lbl {
  margin-top: 6px;
  font-size: 15px;
  font-weight: 600;
  color: #cbd5e1;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.check-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.check-list li {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  font-size: 20px;
  line-height: 1.38;
  color: #e2e8f0;
}

.icon-ok, .icon-no, .icon-gold {
  flex-shrink: 0;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 17px;
  margin-top: 2px;
}

.icon-ok { background: rgba(16, 185, 129, 0.22); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.5); }
.icon-no { background: rgba(239, 68, 68, 0.22); color: #f87171; border: 1px solid rgba(248, 113, 113, 0.5); }
.icon-gold { background: rgba(217, 119, 6, 0.24); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.5); }

.diagram-wrap {
  background: rgba(9, 14, 26, 0.72);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 20px;
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.cta-box {
  background: linear-gradient(135deg, #1e3a8a 0%, #172554 60%, #0f172a 100%);
  border: 2px solid #f59e0b;
  border-radius: 20px;
  padding: 24px 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35);
}

.url-chip {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: #f59e0b;
  color: #0f172a;
  font-size: 22px;
  font-weight: 900;
  padding: 13px 24px;
  border-radius: 14px;
  letter-spacing: -0.01em;
}

.disclaimer-note {
  font-size: 14px;
  line-height: 1.42;
  color: #94a3b8;
  background: rgba(15, 23, 42, 0.65);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 11px 16px;
}

/* Footer bar */
.slide-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 16px;
  color: #94a3b8;
}

.footer-left {
  display: flex;
  align-items: center;
  gap: 14px;
  font-weight: 600;
}

.footer-url {
  color: #fbbf24;
  font-weight: 800;
}

.footer-swipe {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 800;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: #f8fafc;
  background: rgba(217, 119, 6, 0.22);
  border: 1px solid rgba(245, 158, 11, 0.45);
  padding: 7px 16px;
  border-radius: 999px;
}

/* Cover-specific hero emblem */
.cover-logo-hero {
  width: 175px;
  height: 175px;
  border-radius: 50%;
  border: 4px solid rgba(245, 158, 11, 0.85);
  box-shadow: 0 0 0 12px rgba(217, 119, 6, 0.14), 0 18px 44px rgba(0, 0, 0, 0.55);
  background: #090e1a;
}

.divider-gold {
  width: 96px;
  height: 5px;
  border-radius: 3px;
  background: linear-gradient(90deg, #f59e0b 0%, #d97706 100%);
}

/* Table styling */
.tech-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 19px;
}

.tech-table th {
  text-align: left;
  padding: 13px 16px;
  background: rgba(30, 58, 138, 0.55);
  color: #fef3c7;
  font-weight: 800;
  font-size: 16px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 2px solid rgba(245, 158, 11, 0.5);
}

.tech-table td {
  padding: 13px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  color: #e2e8f0;
  font-weight: 600;
}

.tech-table tr:nth-child(even) td {
  background: rgba(255, 255, 255, 0.025);
}

/* Story interactive sticker zone */
.sticker-zone {
  border: 2.5px dashed rgba(251, 191, 36, 0.72);
  border-radius: 26px;
  background: rgba(15, 23, 42, 0.72);
  padding: 36px 28px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
}

.reel-badge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 10px 22px;
  border-radius: 999px;
  background: rgba(217, 119, 6, 0.22);
  border: 1.5px solid #f59e0b;
  color: #fef3c7;
  font-size: 18px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
"""


def build_slide_html(
    *,
    body_html: str,
    width: int = 1080,
    height: int = 1350,
    pill_text: str = "501(c)(3) Safety Education",
    pill_class: str = "",
    slide_label: str = "",
    footer_url: str = "sikhrpa.org",
    footer_right: str = "SWIPE →",
    theme: str = "default",
    frame_variant: str = "",
    body_class: str = "",
    show_header: bool = True,
    show_footer: bool = True,
) -> str:
    """Wrap slide body HTML inside the complete branded SikhRPA canvas."""
    logo = get_logo_data_uri()
    is_vertical = height > width
    frame_cls = "frame-9x16" if is_vertical else "frame-4x5"
    if frame_variant:
        frame_cls += f" {frame_variant}"

    theme_cls = f"theme-{theme}" if theme and theme != "default" else ""
    pill_cls = f"pill {pill_class}".strip()

    counter_html = ""
    if slide_label:
        if "/" in slide_label:
            parts = slide_label.split("/", 1)
            counter_html = f'<div class="slide-counter"><span>{parts[0].strip()}</span> / {parts[1].strip()}</div>'
        else:
            counter_html = f'<div class="slide-counter"><span>{slide_label}</span></div>'

    header_html = ""
    if show_header:
        header_html = f"""
        <header class="slide-header">
          <div class="brand-lockup">
            <img class="brand-logo" src="{logo}" alt="SikhRPA Crest" />
            <div class="brand-meta">
              <div class="brand-name">SIKHRPA</div>
              <div class="brand-sub">501(c)(3) Public Charity • EIN 42-2595402</div>
            </div>
          </div>
          <div class="header-right">
            <div class="{pill_cls}">{pill_text}</div>
            {counter_html}
          </div>
        </header>
        """

    footer_html = ""
    if show_footer:
        footer_html = f"""
        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-url">{footer_url}</span>
            <span>•</span>
            <span>@sikhrpa</span>
          </div>
          <div class="footer-swipe">{footer_right}</div>
        </footer>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width={width}, initial-scale=1.0" />
<style>{BASE_CSS}</style>
</head>
<body style="width:{width}px;height:{height}px;">
  <div class="canvas {theme_cls} {frame_cls}">
    <div class="top-accent-bar"></div>
    {header_html}
    <main class="slide-body {body_class}">
      {body_html}
    </main>
    {footer_html}
  </div>
</body>
</html>
"""
