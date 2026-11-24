#!/usr/bin/env python3
"""
Render a dignified, reverent 9:16 (1080x1920) Instagram Story graphic for
Sri Guru Nanak Dev Ji's Parkash Purab (Gurpurab) for SikhRPA (@sikhrpa).
Outputs both PNG and sRGB JPEG plus a ready-to-paste caption.txt.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from styles import ROOT_DIR, get_logo_data_uri  # noqa: E402

OUT_DIR = ROOT_DIR / "posts" / "bonus-guru-nanak-gurpurab-story"


def build_gurpurab_html() -> str:
    logo = get_logo_data_uri()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, initial-scale=1.0" />
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: 1080px;
    height: 1920px;
    overflow: hidden;
    background: #090e1c;
    color: #f8fafc;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
  }}

  .canvas {{
    position: relative;
    width: 1080px;
    height: 1920px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 155px 68px 190px 68px;
    background:
      radial-gradient(circle 480px at 50% 28%, rgba(245, 158, 11, 0.28) 0%, rgba(217, 119, 6, 0.08) 45%, rgba(9, 14, 28, 0) 75%),
      radial-gradient(ellipse 90% 55% at 50% 85%, rgba(30, 58, 138, 0.45) 0%, rgba(9, 14, 28, 0) 72%),
      linear-gradient(180deg, #080d1a 0%, #0f172a 48%, #091022 100%);
    overflow: hidden;
  }}

  /* Subtle gold ornamental corner frame */
  .outer-frame {{
    position: absolute;
    inset: 38px;
    border: 2px solid rgba(217, 119, 6, 0.35);
    border-radius: 34px;
    pointer-events: none;
    z-index: 1;
  }}
  .inner-frame {{
    position: absolute;
    inset: 50px;
    border: 1px solid rgba(251, 191, 36, 0.16);
    border-radius: 26px;
    pointer-events: none;
    z-index: 1;
  }}

  .top-bar {{
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 14px;
    text-align: center;
  }}

  .greeting-pa {{
    font-family: 'Noto Serif Gurmukhi', 'Noto Sans Gurmukhi', serif;
    font-size: 28px;
    font-weight: 700;
    color: #fde68a;
    letter-spacing: 0.01em;
    line-height: 1.55;
  }}

  .center-piece {{
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 24px;
    width: 100%;
  }}

  .ikonkar-halo {{
    width: 248px;
    height: 248px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: radial-gradient(circle, rgba(245, 158, 11, 0.24) 0%, rgba(15, 23, 42, 0.85) 70%);
    border: 2.5px solid rgba(251, 191, 36, 0.65);
    box-shadow:
      0 0 0 14px rgba(217, 119, 6, 0.10),
      0 0 65px rgba(245, 158, 11, 0.30);
  }}

  .ikonkar-glyph {{
    font-family: 'Noto Serif Gurmukhi', 'Noto Sans Gurmukhi', serif;
    font-size: 138px;
    font-weight: 700;
    line-height: 1.1;
    background: linear-gradient(180deg, #fef3c7 0%, #fbbf24 52%, #d97706 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 6px 18px rgba(217, 119, 6, 0.45));
    padding-top: 8px;
  }}

  .eyebrow {{
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 9px 24px;
    border-radius: 999px;
    background: rgba(217, 119, 6, 0.18);
    border: 1px solid rgba(251, 191, 36, 0.45);
    color: #fef3c7;
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
  }}

  .title-en {{
    font-family: 'Inter Display', 'Inter', sans-serif;
    font-size: 68px;
    font-weight: 900;
    line-height: 1.08;
    letter-spacing: -0.025em;
    color: #ffffff;
  }}
  .title-en span {{
    color: #fbbf24;
  }}

  .title-pa-box {{
    width: 100%;
    background: linear-gradient(135deg, rgba(217, 119, 6, 0.16) 0%, rgba(30, 58, 138, 0.34) 100%);
    border: 1px solid rgba(251, 191, 36, 0.45);
    border-top: 4px solid #f59e0b;
    border-radius: 22px;
    padding: 24px 30px;
  }}
  .title-pa {{
    font-family: 'Noto Serif Gurmukhi', 'Noto Sans Gurmukhi', serif;
    font-size: 34px;
    font-weight: 700;
    line-height: 1.65;
    color: #fef3c7;
  }}

  .blessing {{
    font-size: 25px;
    line-height: 1.48;
    color: #cbd5e1;
    max-width: 850px;
    font-weight: 500;
  }}

  .pillars {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    width: 100%;
    margin-top: 4px;
  }}
  .pillar {{
    background: rgba(15, 23, 42, 0.78);
    border: 1px solid rgba(251, 191, 36, 0.34);
    border-radius: 20px;
    padding: 22px 14px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
  }}
  .pillar-pa {{
    font-family: 'Noto Serif Gurmukhi', 'Noto Sans Gurmukhi', serif;
    font-size: 28px;
    font-weight: 700;
    color: #fbbf24;
    line-height: 1.5;
  }}
  .pillar-en {{
    font-size: 20px;
    font-weight: 800;
    color: #ffffff;
  }}
  .pillar-sub {{
    font-size: 15px;
    color: #94a3b8;
    font-weight: 600;
  }}

  .footer-brand {{
    position: relative;
    z-index: 2;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
    padding-top: 22px;
    border-top: 1px solid rgba(255, 255, 255, 0.12);
  }}

  .brand-row {{
    display: flex;
    align-items: center;
    gap: 18px;
  }}
  .brand-row img {{
    width: 78px;
    height: 78px;
    border-radius: 50%;
    border: 2.5px solid #f59e0b;
    background: #080d1a;
    box-shadow: 0 6px 20px rgba(0,0,0,0.5);
  }}
  .brand-text {{
    text-align: left;
  }}
  .brand-title {{
    font-size: 24px;
    font-weight: 900;
    letter-spacing: 0.04em;
    color: #ffffff;
  }}
  .brand-sub {{
    font-size: 16px;
    font-weight: 700;
    color: #fbbf24;
    margin-top: 2px;
  }}
  .motto-line {{
    font-family: 'Noto Sans Gurmukhi', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #fde68a;
    line-height: 1.5;
  }}
</style>
</head>
<body>
  <div class="canvas">
    <!-- Celestial sunburst rays SVG background -->
    <svg viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0;pointer-events:none;z-index:0;" xmlns="http://www.w3.org/2000/svg">
      <g opacity="0.13" stroke="#fbbf24" stroke-width="1.5">
        <line x1="540" y1="535" x2="540" y2="90"/>
        <line x1="540" y1="535" x2="770" y2="145"/>
        <line x1="540" y1="535" x2="940" y2="310"/>
        <line x1="540" y1="535" x2="995" y2="535"/>
        <line x1="540" y1="535" x2="940" y2="760"/>
        <line x1="540" y1="535" x2="770" y2="925"/>
        <line x1="540" y1="535" x2="310" y2="145"/>
        <line x1="540" y1="535" x2="140" y2="310"/>
        <line x1="540" y1="535" x2="85" y2="535"/>
        <line x1="540" y1="535" x2="140" y2="760"/>
        <line x1="540" y1="535" x2="310" y2="925"/>
      </g>
      <circle cx="540" cy="535" r="215" fill="none" stroke="rgba(251,191,36,0.18)" stroke-width="1.5" stroke-dasharray="6 8"/>
      <circle cx="540" cy="535" r="320" fill="none" stroke="rgba(251,191,36,0.10)" stroke-width="1.5"/>
    </svg>

    <div class="outer-frame"></div>
    <div class="inner-frame"></div>

    <div class="top-bar">
      <div class="greeting-pa">ਵਾਹਿਗੁਰੂ ਜੀ ਕਾ ਖਾਲਸਾ, ਵਾਹਿਗੁਰੂ ਜੀ ਕੀ ਫਤਹਿ</div>
      <svg viewBox="0 0 420 20" width="360" height="18" xmlns="http://www.w3.org/2000/svg">
        <line x1="0" y1="10" x2="178" y2="10" stroke="rgba(251,191,36,0.55)" stroke-width="1.8"/>
        <polygon points="210,2 220,10 210,18 200,10" fill="none" stroke="#fbbf24" stroke-width="2"/>
        <circle cx="210" cy="10" r="3" fill="#fbbf24"/>
        <line x1="242" y1="10" x2="420" y2="10" stroke="rgba(251,191,36,0.55)" stroke-width="1.8"/>
      </svg>
    </div>

    <div class="center-piece">
      <div class="ikonkar-halo">
        <div class="ikonkar-glyph">ੴ</div>
      </div>

      <div class="eyebrow">Parkash Purab • Sri Guru Nanak Dev Ji</div>

      <h1 class="title-en">Happy <span>Guru Nanak</span><br/>Gurpurab</h1>

      <div class="title-pa-box">
        <div class="title-pa">ਧੰਨ ਧੰਨ ਸ੍ਰੀ ਗੁਰੂ ਨਾਨਕ ਦੇਵ ਜੀ ਦੇ ਪ੍ਰਕਾਸ਼ ਪੁਰਬ ਦੀਆਂ ਲੱਖ-ਲੱਖ ਵਧਾਈਆਂ!</div>
      </div>

      <p class="blessing">
        May the timeless teachings of Guru Nanak Dev Ji bless the entire Sangat with peace, humility, truthful living, and <strong style="color:#fef3c7;">Sarbat da Bhala</strong> — the well-being of all humanity.
      </p>

      <div class="pillars">
        <div class="pillar">
          <div class="pillar-pa">ਨਾਮ ਜਪੋ</div>
          <div class="pillar-en">Naam Japo</div>
          <div class="pillar-sub">Remember the One</div>
        </div>
        <div class="pillar">
          <div class="pillar-pa">ਕਿਰਤ ਕਰੋ</div>
          <div class="pillar-en">Kirat Karo</div>
          <div class="pillar-sub">Honest Living</div>
        </div>
        <div class="pillar">
          <div class="pillar-pa">ਵੰਡ ਛਕੋ</div>
          <div class="pillar-en">Vand Chhako</div>
          <div class="pillar-sub">Share &amp; Serve</div>
        </div>
      </div>
    </div>

    <div class="footer-brand">
      <div class="brand-row">
        <img src="{logo}" alt="SikhRPA Logo" />
        <div class="brand-text">
          <div class="brand-title">SIKH RIFLE &amp; PISTOL ASSOCIATION</div>
          <div class="brand-sub">@sikhrpa &nbsp;•&nbsp; sikhrpa.org &nbsp;•&nbsp; 501(c)(3) Public Charity</div>
        </div>
      </div>
      <div class="motto-line">ਸਰਬੱਤ ਦਾ ਭਲਾ &nbsp;•&nbsp; ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
    </div>
  </div>
</body>
</html>
"""


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    png_path = OUT_DIR / "story-guru-nanak-gurpurab.png"
    jpg_path = OUT_DIR / "story-guru-nanak-gurpurab.jpg"
    caption_path = OUT_DIR / "caption.txt"

    chrome_path = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    launch_kwargs: dict = {"args": ["--no-sandbox", "--disable-gpu", "--font-render-hinting=none"]}
    if chrome_path:
        launch_kwargs["executable_path"] = chrome_path

    with sync_playwright() as p:
        browser = p.chromium.launch(**launch_kwargs)
        page = browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        page.set_content(build_gurpurab_html(), wait_until="load")
        page.evaluate("() => document.fonts.ready")
        overflow = page.evaluate("() => document.querySelector('.canvas').scrollHeight - 1920")
        if overflow > 2:
            print(f"⚠ Overflow detected: {overflow}px")
            browser.close()
            return 2
        page.screenshot(path=str(png_path), type="png", full_page=False)
        browser.close()

    with Image.open(png_path) as img:
        img.convert("RGB").save(jpg_path, format="JPEG", quality=94, optimize=True, subsampling=0)

    caption_text = (
        "========================================================================\n"
        "BONUS STORY — Sri Guru Nanak Dev Ji Parkash Purab (Gurpurab)\n"
        "Format: 9:16 Instagram Story (1080x1920)\n"
        "========================================================================\n\n"
        "--- OPTIONAL STORY TEXT / REPOST CAPTION ---\n\n"
        "Waheguru Ji Ka Khalsa, Waheguru Ji Ki Fateh!\n\n"
        "ਧੰਨ ਧੰਨ ਸ੍ਰੀ ਗੁਰੂ ਨਾਨਕ ਦੇਵ ਜੀ ਦੇ ਪ੍ਰਕਾਸ਼ ਪੁਰਬ ਦੀਆਂ ਲੱਖ-ਲੱਖ ਵਧਾਈਆਂ!\n\n"
        "Wishing the entire Sangat a blessed and peaceful Guru Nanak Gurpurab. "
        "May the eternal teachings of Naam Japo, Kirat Karo, and Vand Chhako continue to guide "
        "our families in humility, service, and Sarbat da Bhala.\n\n"
        "ਸਰਬੱਤ ਦਾ ਭਲਾ • ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!\n"
        "— Sikh Rifle and Pistol Association (@sikhrpa | sikhrpa.org)\n\n"
        "--- HASHTAGS ---\n\n"
        "#GuruNanakGurpurab #Gurpurab #GuruNanakDevJi #ParkashPurab #SarbatDaBhala "
        "#SikhRPA #SikhCommunity #CaliforniaSikhs #Waheguru\n"
    )
    caption_path.write_text(caption_text, encoding="utf-8")
    print(f"✓ Rendered {png_path} and {jpg_path} (ZERO overflow)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
