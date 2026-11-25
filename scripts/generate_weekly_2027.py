#!/usr/bin/env python3
"""
SikhRPA 2027 Full-Year 52-Week Instagram Generator (Posts + Companion Stories)
Renders 104 production-ready PNGs (52x 4:5 Feed Posts + 52x 9:16 Stories),
writes 52 ready-to-paste caption.txt files, builds schedule-2027.csv, and
upgrades index.html into a unified Campaign Gallery (Dec 2026 + 2027 52-Week + Bonus Story).

Usage:
    python3 scripts/generate_weekly_2027.py
"""

from __future__ import annotations

import csv
import html as html_lib
import json
import re
import shutil
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from content_posts_1_to_6 import get_posts_1_to_6  # noqa: E402
from content_posts_7_to_12 import get_posts_7_to_12  # noqa: E402
from diagrams import svg_dignified_divider  # noqa: E402
from generate_all import FORBIDDEN_TERMS  # noqa: E402
from styles import ROOT_DIR, build_slide_html, get_logo_data_uri  # noqa: E402
from weekly_2027_data import WEEKLY_2027_POSTS  # noqa: E402

WEEKLY_DIR = ROOT_DIR / "weekly-2027"
RAW_BASE = "https://raw.githubusercontent.com/Sikhrpa/instagram-series/main"

CATEGORY_META = {
    "holiday": {"label": "Major Sikh Holiday", "theme": "shaheedi", "pill_class": "", "accent": "#fbbf24"},
    "safety": {"label": "Safety & Safe Storage", "theme": "royal", "pill_class": "", "accent": "#fbbf24"},
    "compliance": {"label": "CA Compliance", "theme": "default", "pill_class": "pill-blue", "accent": "#93c5fd"},
    "marksmanship": {"label": "Marksmanship & Optics", "theme": "default", "pill_class": "", "accent": "#fbbf24"},
    "trauma": {"label": "Range Trauma & First Aid", "theme": "trauma", "pill_class": "pill-red", "accent": "#fca5a5"},
    "community": {"label": "Community & 501(c)(3)", "theme": "royal", "pill_class": "pill-emerald", "accent": "#34d399"},
}


def build_caption(item: dict) -> str:
    """Generate a rich, policy-safe ready-to-paste Instagram caption for each weekly post."""
    bullets = "\n".join(f"• {h}: {d}" for h, d in item["points"])
    disclaimer = ""
    if item["category"] == "trauma":
        disclaimer = (
            "\n\nMedical Disclaimer: Provided strictly for general safety awareness and does not constitute medical advice. "
            "Always dial 911 in an emergency and pursue hands-on training through ACS Stop the Bleed® or the Red Cross."
        )
    elif item["category"] == "compliance":
        disclaimer = (
            "\n\nEducational Disclaimer: Provided exclusively for 501(c)(3) public safety education — not legal advice. "
            "Always verify current statutes with the California DOJ Bureau of Firearms or consult a qualified California attorney."
        )

    short_url = item["url"].replace("https://", "").rstrip("/")
    if item["is_holiday"]:
        return (
            f"Waheguru Ji Ka Khalsa, Waheguru Ji Ki Fateh!\n\n"
            f"{item['pa_line']}\n\n"
            f"{item['summary']}\n\n"
            f"{bullets}\n\n"
            f"Learn more about Sikh heritage, Miri-Piri, and our free bilingual safety resources at {short_url} (Link in bio).\n\n"
            f"ਸਰਬੱਤ ਦਾ ਭਲਾ • ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        )
    return (
        f"{item['title']}\n\n"
        f"{item['pa_line']}\n\n"
        f"{item['summary']}\n\n"
        f"{bullets}\n\n"
        f"Explore 100% free English & Gurmukhi safety tools anytime at {short_url} (Link in bio).\n"
        f"Sikh Rifle and Pistol Association (SikhRPA) • California 501(c)(3) Nonprofit • EIN: 42-2595402 • president@sikhrpa.org"
        f"{disclaimer}\n\n"
        f"ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
    )


def svg_holiday_emblem(symbol: str = "ikonkar", size: int = 190) -> str:
    """Unclipped golden SVG emblem (Ik Onkar or ceremonial Khanda starlight) for Holiday posts & Stories."""
    if symbol == "khanda":
        return f"""
        <svg viewBox="0 0 240 240" width="{size}" height="{size}" overflow="visible" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="hkGold" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#fef3c7"/>
              <stop offset="50%" stop-color="#fbbf24"/>
              <stop offset="100%" stop-color="#d97706"/>
            </linearGradient>
          </defs>
          <circle cx="120" cy="120" r="108" fill="rgba(217,119,6,0.12)" stroke="rgba(251,191,36,0.6)" stroke-width="2.5"/>
          <circle cx="120" cy="120" r="94" fill="none" stroke="rgba(251,191,36,0.22)" stroke-width="1.5" stroke-dasharray="5 6"/>
          <!-- Clean dignified geometric Khanda emblem -->
          <g fill="url(#hkGold)">
            <!-- Central double-edged Khanda -->
            <path d="M120 34 L130 56 L126 168 L138 168 L138 176 L124 176 L124 198 L116 198 L116 176 L102 176 L102 168 L114 168 L110 56 Z"/>
            <!-- Chakkar ring -->
            <path d="M120 74 A42 42 0 1 0 120 158 A42 42 0 1 0 120 74 Z M120 85 A31 31 0 1 1 120 147 A31 31 0 1 1 120 85 Z"/>
            <!-- Left Kirpan arc -->
            <path d="M84 56 C46 86 48 144 92 172 L106 184 L100 192 L82 178 C36 146 34 82 78 48 Z"/>
            <!-- Right Kirpan arc -->
            <path d="M156 56 C194 86 192 144 148 172 L134 184 L140 192 L158 178 C204 146 206 82 162 48 Z"/>
          </g>
        </svg>"""
    # Default: unclipped golden Ik Onkar SVG text
    return f"""
    <svg viewBox="0 0 260 260" width="{size}" height="{size}" overflow="visible" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="ikG27" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#fef3c7"/>
          <stop offset="52%" stop-color="#fbbf24"/>
          <stop offset="100%" stop-color="#d97706"/>
        </linearGradient>
        <filter id="ikGl27" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#d97706" flood-opacity="0.45"/>
        </filter>
      </defs>
      <circle cx="130" cy="130" r="116" fill="rgba(217,119,6,0.14)" stroke="rgba(251,191,36,0.65)" stroke-width="2.5"/>
      <circle cx="130" cy="130" r="102" fill="none" stroke="rgba(251,191,36,0.22)" stroke-width="1.5" stroke-dasharray="5 6"/>
      <text x="130" y="168" text-anchor="middle" fill="url(#ikG27)" filter="url(#ikGl27)"
            font-family="'Noto Serif Gurmukhi', 'Noto Sans Gurmukhi', serif" font-size="104" font-weight="700">ੴ</text>
    </svg>"""


def build_weekly_post_html(item: dict) -> str:
    """Build 4:5 (1080x1350) feed post HTML."""
    meta = CATEGORY_META[item["category"]]
    short_url = item["url"].replace("https://", "").rstrip("/")
    week_label = f"W{item['week']:02d} • 2027"

    if item["is_holiday"]:
        emblem = svg_holiday_emblem(item.get("holiday_symbol", "ikonkar"), size=146)
        point_cards = "\n".join(
            f"""<div class="card card-gold" style="padding:15px 20px;text-align:left;">
                  <div class="gold" style="font-size:16.5px;font-weight:900;">{html_lib.escape(h)}</div>
                  <p class="body-sm" style="margin-top:3px;font-size:17px;">{html_lib.escape(d)}</p>
                </div>"""
            for h, d in item["points"]
        )
        body = f"""
        <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:14px;">
          {emblem}
          <div class="eyebrow">{html_lib.escape(item['eyebrow'])}</div>
          <h1 class="h1-lg" style="font-size:42px;max-width:920px;">{html_lib.escape(item['title'])}</h1>
          <div class="pa-banner" style="width:100%;text-align:center;border-left-width:1px;border-top:3.5px solid #f59e0b;padding:14px 22px;">
            <div class="gurmukhi-serif" style="font-size:25px;font-weight:700;color:#fef3c7;">{html_lib.escape(item['pa_line'])}</div>
          </div>
          <p class="body-sm" style="max-width:880px;font-size:19px;color:#e2e8f0;">{html_lib.escape(item['summary'])}</p>
          <div class="stack-sm" style="width:100%;gap:10px;">
            {point_cards}
          </div>
        </div>
        """
        return build_slide_html(
            body_html=body,
            width=1080,
            height=1350,
            pill_text=item["date_display"],
            pill_class="",
            slide_label=week_label,
            footer_url=short_url,
            footer_right="SAVE & SHARE",
            theme="shaheedi",
        )

    # Educational / Community / Trauma / Compliance / Marksmanship 4:5 Card
    card_cls = {
        "safety": "card-gold",
        "compliance": "card-blue",
        "marksmanship": "card",
        "trauma": "card-red",
        "community": "card-emerald",
    }.get(item["category"], "card")

    badge_cls = {
        "compliance": "num-badge num-badge-blue",
        "trauma": "num-badge num-badge-red",
    }.get(item["category"], "num-badge")

    points_html = "\n".join(
        f"""<div class="card {card_cls if idx == 0 else ''} row" style="padding:17px 22px;gap:16px;">
              <div class="{badge_cls}" style="width:42px;height:42px;font-size:20px;">{idx + 1}</div>
              <div>
                <div style="font-size:21px;font-weight:800;color:#ffffff;">{html_lib.escape(h)}</div>
                <p class="body-sm" style="font-size:17.5px;margin-top:2px;">{html_lib.escape(d)}</p>
              </div>
            </div>"""
        for idx, (h, d) in enumerate(item["points"])
    )

    disclaimer_html = ""
    if item["category"] == "trauma":
        disclaimer_html = (
            '<div class="disclaimer-note"><strong>Educational Awareness Only:</strong> Not medical advice. '
            'Always call 911 in an emergency &amp; complete hands-on ACS Stop the Bleed® training.</div>'
        )
    elif item["category"] == "compliance":
        disclaimer_html = (
            '<div class="disclaimer-note"><strong>Educational Info Only (Not Legal Advice):</strong> '
            'Verify current California statutes directly with CA DOJ or a qualified California attorney.</div>'
        )

    body = f"""
    <div class="eyebrow">{html_lib.escape(item['eyebrow'])}</div>
    <h1 class="h1-lg" style="font-size:44px;">{html_lib.escape(item['title'])}</h1>
    <div class="pa-banner" style="padding:14px 20px;">
      <div class="pa-text-sm" style="font-size:20px;">{html_lib.escape(item['pa_line'])}</div>
    </div>
    <p class="body-sm" style="font-size:19.5px;color:#cbd5e1;">{html_lib.escape(item['summary'])}</p>
    <div class="stack-sm" style="gap:11px;">
      {points_html}
    </div>
    {disclaimer_html}
    """
    return build_slide_html(
        body_html=body,
        width=1080,
        height=1350,
        pill_text=f"{meta['label']}",
        pill_class=meta["pill_class"],
        slide_label=week_label,
        footer_url=short_url,
        footer_right="SAVE & SHARE",
        theme=meta["theme"],
    )


def build_weekly_story_html(item: dict) -> str:
    """Build 9:16 (1080x1920) companion Instagram Story HTML respecting Story safe zones."""
    logo = get_logo_data_uri()
    meta = CATEGORY_META[item["category"]]
    short_url = item["url"].replace("https://", "").rstrip("/")
    week_label = f"STORY • W{item['week']:02d}"

    if item["is_holiday"]:
        emblem = svg_holiday_emblem(item.get("holiday_symbol", "ikonkar"), size=255)
        pillar_boxes = "\n".join(
            f"""<div class="card card-gold" style="padding:20px 24px;text-align:left;width:100%;">
                  <div class="gold" style="font-size:20px;font-weight:900;">{html_lib.escape(h)}</div>
                  <p class="body-sm" style="margin-top:4px;font-size:19px;">{html_lib.escape(d)}</p>
                </div>"""
            for h, d in item["points"]
        )
        body = f"""
        <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:22px;">
          <div class="gurmukhi-serif" style="font-size:26px;font-weight:700;color:#fde68a;">
            ਵਾਹਿਗੁਰੂ ਜੀ ਕਾ ਖਾਲਸਾ, ਵਾਹਿਗੁਰੂ ਜੀ ਕੀ ਫਤਹਿ
          </div>
          {svg_dignified_divider()}
          {emblem}
          <div class="reel-badge">{html_lib.escape(item['date_display'])}</div>
          <h1 class="h1-lg" style="font-size:52px;">{html_lib.escape(item['title'])}</h1>
          <div class="pa-banner" style="width:100%;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;padding:20px 26px;">
            <div class="gurmukhi-serif" style="font-size:29px;font-weight:700;color:#fef3c7;">{html_lib.escape(item['pa_line'])}</div>
          </div>
          <div class="stack-sm" style="width:100%;gap:12px;">
            {pillar_boxes}
          </div>
          <div class="pa-text-md" style="margin-top:4px;">ਸਰਬੱਤ ਦਾ ਭਲਾ &nbsp;•&nbsp; ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
        </div>
        """
        return build_slide_html(
            body_html=body,
            width=1080,
            height=1920,
            pill_text="Sikh Holiday",
            slide_label=week_label,
            footer_url=short_url,
            footer_right="SHARE WITH SANGAT",
            theme="shaheedi",
            frame_variant="story-frame",
        )

    # Interactive Educational Story (Poll / Quiz / Q&A / Checklist / Link Sticker)
    stype = item.get("story_type", "link")
    sticker_copy = {
        "poll": ("COMMUNITY POLL", "Tap below to vote — share your experience with the Sangat!"),
        "quiz": ("TEST YOUR SAFETY KNOWLEDGE", "Tap your answer below — then check the free bilingual guide!"),
        "qa": ("COMMUNITY Q&A", "Drop a safety or California compliance question below!"),
        "checklist": ("SAVE FOR LATER", "Screenshot this Story & share it with family and friends!"),
        "link": ("FREE BILINGUAL RESOURCE", "Tap the Link Sticker below to open this free SikhRPA tool!"),
    }.get(stype, ("FREE BILINGUAL RESOURCE", "Tap below to explore SikhRPA's free safety tools!"))

    top_points = "\n".join(
        f"""<li><span class="icon-ok">✓</span><span><strong>{html_lib.escape(h)}:</strong> {html_lib.escape(d)}</span></li>"""
        for h, d in item["points"][:3]
    )

    body = f"""
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;">
      <img class="brand-logo" style="width:112px;height:112px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
      <div class="reel-badge">{html_lib.escape(item['story_hook'])}</div>
      <h1 class="h1-lg" style="font-size:52px;">{html_lib.escape(item['title'])}</h1>
      <div class="pa-banner" style="width:100%;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;padding:18px 24px;">
        <div class="pa-text-md" style="font-size:24px;">{html_lib.escape(item['pa_line'])}</div>
      </div>
      <div class="card card-blue" style="width:100%;text-align:left;padding:24px 26px;">
        <ul class="check-list" style="gap:14px;">
          {top_points}
        </ul>
      </div>
      <div class="sticker-zone" style="width:100%;min-height:245px;">
        <div style="font-size:18px;font-weight:900;letter-spacing:0.12em;color:#fbbf24;">{sticker_copy[0]}</div>
        <div style="font-size:26px;font-weight:800;color:#ffffff;max-width:740px;line-height:1.38;">
          {sticker_copy[1]}
        </div>
        <div style="font-size:21px;font-weight:800;color:#93c5fd;margin-top:6px;">{short_url}</div>
      </div>
      <div class="pa-text-sm" style="font-size:21px;">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!</div>
    </div>
    """
    return build_slide_html(
        body_html=body,
        width=1080,
        height=1920,
        pill_text=meta["label"],
        pill_class=meta["pill_class"],
        slide_label=week_label,
        footer_url=short_url,
        footer_right="TAP LINK STICKER ↑",
        theme=meta["theme"],
        frame_variant="story-frame",
    )


def audit_weekly_policy() -> list[str]:
    issues: list[str] = []
    for item in WEEKLY_2027_POSTS:
        cap = build_caption(item)
        if len(f"{cap}\n\n{item['hashtags']}") > 2200:
            issues.append(f"Week {item['week']:02d} caption+hashtags exceeds 2,200 chars")
        blob = " ".join(
            [item["title"], item["summary"], item["story_prompt_box"], cap, item["hashtags"]]
            + [f"{h} {d}" for h, d in item["points"]]
        )
        for pat in FORBIDDEN_TERMS:
            if re.search(pat, blob, flags=re.IGNORECASE):
                issues.append(f"Week {item['week']:02d} matched forbidden term: {pat}")
    return issues


def write_schedule_2027_csv() -> None:
    csv_path = ROOT_DIR / "schedule-2027.csv"
    fieldnames = [
        "Week",
        "Quarter",
        "Date",
        "Time",
        "Category",
        "Major Sikh Holiday",
        "Title",
        "Folder",
        "Post PNG",
        "Story PNG",
        "Post Public URL",
        "Story Public URL",
        "Link in Bio URL",
        "Caption",
        "Hashtags",
        "Caption + Hashtags",
        "Story Prompt",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in WEEKLY_2027_POSTS:
            q = (item["week"] - 1) // 13 + 1
            cap = build_caption(item)
            folder = f"weekly-2027/{item['slug']}"
            writer.writerow(
                {
                    "Week": f"Week {item['week']:02d}",
                    "Quarter": f"Q{q}",
                    "Date": item["date_display"],
                    "Time": item["time_tz"],
                    "Category": CATEGORY_META[item["category"]]["label"],
                    "Major Sikh Holiday": "Yes" if item["is_holiday"] else "No",
                    "Title": item["title"],
                    "Folder": folder,
                    "Post PNG": f"{folder}/post.png",
                    "Story PNG": f"{folder}/story.png",
                    "Post Public URL": f"{RAW_BASE}/{folder}/post.png",
                    "Story Public URL": f"{RAW_BASE}/{folder}/story.png",
                    "Link in Bio URL": item["url"],
                    "Caption": cap,
                    "Hashtags": item["hashtags"],
                    "Caption + Hashtags": f"{cap}\n\n{item['hashtags']}",
                    "Story Prompt": item["story_prompt_box"],
                }
            )


def write_unified_gallery_html() -> None:
    """Upgrade index.html to display BOTH the Dec 2026 Launch Series and the 52-Week 2027 Series."""
    dec_posts = get_posts_1_to_6() + get_posts_7_to_12()
    dec_json_data = []
    for p in dec_posts:
        dec_json_data.append(
            {
                "number": p["number"],
                "slug": p["slug"],
                "week": p["week"],
                "date_display": p["date_display"],
                "time_pst": p["time_pst"],
                "format": p["format"],
                "format_type": p["format_type"],
                "title": p["title"],
                "url": p["url"],
                "caption": p["caption"],
                "hashtags": p["hashtags"],
                "story_prompt": p["story_prompt"],
                "slides": [
                    {
                        "filename": s["filename"],
                        "path": f"posts/{p['slug']}/{s['filename']}",
                        "width": s["width"],
                        "height": s["height"],
                        "aspect": "9:16" if s["height"] > 1500 else "4:5",
                    }
                    for s in p["slides"]
                ],
            }
        )

    weekly_json_data = []
    for item in WEEKLY_2027_POSTS:
        q = (item["week"] - 1) // 13 + 1
        cap = build_caption(item)
        folder = f"weekly-2027/{item['slug']}"
        weekly_json_data.append(
            {
                "week": item["week"],
                "quarter": q,
                "slug": item["slug"],
                "date_display": item["date_display"],
                "time_tz": item["time_tz"],
                "category": item["category"],
                "category_label": CATEGORY_META[item["category"]]["label"],
                "is_holiday": item["is_holiday"],
                "title": item["title"],
                "url": item["url"],
                "caption": cap,
                "hashtags": item["hashtags"],
                "story_prompt": item["story_prompt_box"],
                "slides": [
                    {"filename": "post.png", "path": f"{folder}/post.png", "width": 1080, "height": 1350, "aspect": "4:5 Feed Post"},
                    {"filename": "story.png", "path": f"{folder}/story.png", "width": 1080, "height": 1920, "aspect": "9:16 Story"},
                ],
            }
        )

    dec_json = json.dumps(dec_json_data, ensure_ascii=False)
    weekly_json = json.dumps(weekly_json_data, ensure_ascii=False)
    holiday_count = sum(1 for x in WEEKLY_2027_POSTS if x["is_holiday"])

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SikhRPA Instagram Content Hub — Dec 2026 + Full-Year 2027 (52 Weeks)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+Gurmukhi:wght@400;600;700&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --navy-950: #090e1a;
      --navy-900: #0f172a;
      --navy-800: #16223a;
      --blue-900: #1e3a8a;
      --gold-600: #d97706;
      --gold-500: #f59e0b;
      --gold-400: #fbbf24;
      --slate-50: #f8fafc;
      --slate-300: #cbd5e1;
      --slate-400: #94a3b8;
      --emerald: #10b981;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background:
        radial-gradient(ellipse 80% 45% at 85% 0%, rgba(30,58,138,0.35), transparent 65%),
        radial-gradient(ellipse 65% 40% at 10% 100%, rgba(217,119,6,0.14), transparent 60%),
        var(--navy-900);
      color: var(--slate-50);
      min-height: 100vh;
      line-height: 1.5;
    }}
    .pa {{ font-family: 'Noto Sans Gurmukhi', sans-serif; }}
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 24px; }}
    header.hero {{
      border-bottom: 1px solid rgba(255,255,255,0.1);
      background: rgba(9, 14, 26, 0.78);
      backdrop-filter: blur(12px);
      padding: 32px 0 28px;
    }}
    .hero-top {{ display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 20px; }}
    .brand {{ display: flex; align-items: center; gap: 16px; }}
    .brand img {{ width: 68px; height: 68px; border-radius: 50%; border: 2.5px solid var(--gold-500); background: var(--navy-950); }}
    .brand h1 {{ font-size: clamp(1.45rem, 2.6vw, 2.15rem); font-weight: 900; letter-spacing: -0.02em; }}
    .brand h1 span {{ color: var(--gold-400); }}
    .brand p {{ color: var(--slate-300); font-size: 0.92rem; margin-top: 2px; }}
    .hero-actions {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .btn {{
      display: inline-flex; align-items: center; gap: 7px;
      border: 1px solid rgba(255,255,255,0.15);
      background: rgba(30, 41, 59, 0.85); color: #fff;
      font-size: 0.85rem; font-weight: 700; padding: 9px 14px; border-radius: 10px;
      cursor: pointer; text-decoration: none; transition: all 0.15s ease;
    }}
    .btn:hover {{ transform: translateY(-1px); border-color: var(--gold-500); }}
    .btn-gold {{ background: linear-gradient(135deg, var(--gold-600), var(--gold-500)); color: var(--navy-950); border-color: var(--gold-400); }}
    .btn-blue {{ background: linear-gradient(135deg, var(--blue-900), #2563eb); border-color: rgba(96,165,250,0.45); }}
    .stats-bar {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(175px, 1fr)); gap: 12px; margin-top: 20px; }}
    .stat {{ background: rgba(22, 34, 58, 0.72); border: 1px solid rgba(255,255,255,0.09); border-radius: 14px; padding: 13px 16px; }}
    .stat strong {{ display: block; font-size: 1.3rem; color: var(--gold-400); font-weight: 900; }}
    .stat span {{ font-size: 0.75rem; color: var(--slate-400); text-transform: uppercase; letter-spacing: 0.06em; font-weight: 700; }}

    .series-tabs {{ display: flex; flex-wrap: wrap; gap: 10px; margin: 26px 0 16px; }}
    .tab-btn {{
      flex: 1; min-width: 260px; padding: 14px 20px; border-radius: 14px;
      border: 1.5px solid rgba(255,255,255,0.14); background: rgba(22,34,58,0.65);
      color: var(--slate-300); font-size: 0.96rem; font-weight: 800; cursor: pointer; text-align: left;
      transition: all 0.16s ease;
    }}
    .tab-btn span {{ display: block; font-size: 0.78rem; font-weight: 600; color: var(--slate-400); margin-top: 3px; }}
    .tab-btn.active {{ background: linear-gradient(135deg, rgba(217,119,6,0.24), rgba(30,58,138,0.45)); border-color: var(--gold-500); color: #fff; }}
    .tab-btn.active span {{ color: #fde68a; }}

    .controls {{ display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px; margin: 14px 0 22px; }}
    .filter-group {{ display: flex; flex-wrap: wrap; gap: 7px; }}
    .chip {{
      border: 1px solid rgba(255,255,255,0.14); background: rgba(22, 34, 58, 0.75);
      color: var(--slate-300); font-size: 0.81rem; font-weight: 700;
      padding: 7px 13px; border-radius: 999px; cursor: pointer;
    }}
    .chip.active, .chip:hover {{ background: rgba(217,119,6,0.22); border-color: var(--gold-500); color: #fef3c7; }}
    .search-input {{
      background: rgba(15, 23, 42, 0.88); border: 1px solid rgba(255,255,255,0.15);
      color: #fff; padding: 9px 15px; border-radius: 10px; font-size: 0.88rem; min-width: 240px; outline: none;
    }}
    .search-input:focus {{ border-color: var(--gold-500); }}

    .posts-grid {{ display: flex; flex-direction: column; gap: 24px; padding-bottom: 64px; }}
    .post-card {{ background: rgba(22, 34, 58, 0.78); border: 1px solid rgba(255,255,255,0.11); border-radius: 20px; overflow: hidden; box-shadow: 0 14px 36px rgba(0,0,0,0.28); }}
    .post-card.holiday-card {{ border-color: rgba(245,158,11,0.48); background: linear-gradient(160deg, rgba(217,119,6,0.1), rgba(15,23,42,0.9)); }}
    .post-head {{ display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px; padding: 18px 24px; background: rgba(9, 14, 26, 0.55); border-bottom: 1px solid rgba(255,255,255,0.09); }}
    .post-title-wrap {{ display: flex; align-items: center; gap: 14px; }}
    .post-num {{ width: 44px; height: 44px; border-radius: 12px; background: linear-gradient(135deg, var(--gold-600), var(--gold-500)); color: var(--navy-950); font-weight: 900; font-size: 0.95rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
    .post-title-wrap h2 {{ font-size: 1.1rem; font-weight: 800; color: #fff; }}
    .post-meta {{ font-size: 0.83rem; color: var(--slate-300); margin-top: 2px; }}
    .badges {{ display: flex; flex-wrap: wrap; gap: 7px; }}
    .badge {{ font-size: 0.73rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; padding: 5px 10px; border-radius: 999px; background: rgba(30,58,138,0.55); border: 1px solid rgba(96,165,250,0.38); color: #dbeafe; }}
    .badge-gold {{ background: rgba(217,119,6,0.22); border-color: rgba(245,158,11,0.55); color: #fde68a; }}

    .post-content {{ display: grid; grid-template-columns: minmax(300px, 430px) 1fr; gap: 24px; padding: 22px 24px; }}
    @media (max-width: 920px) {{ .post-content {{ grid-template-columns: 1fr; }} }}
    .stage-wrap {{ display: flex; flex-direction: column; gap: 10px; }}
    .stage {{ position: relative; background: var(--navy-950); border: 1px solid rgba(255,255,255,0.12); border-radius: 16px; overflow: hidden; display: flex; align-items: center; justify-content: center; min-height: 360px; max-height: 520px; }}
    .stage img {{ max-width: 100%; max-height: 500px; object-fit: contain; display: block; cursor: zoom-in; }}
    .nav-btn {{ position: absolute; top: 50%; transform: translateY(-50%); width: 38px; height: 38px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.22); background: rgba(15, 23, 42, 0.85); color: #fff; font-size: 1.15rem; font-weight: 800; cursor: pointer; }}
    .nav-btn:hover {{ background: var(--gold-600); color: var(--navy-950); }}
    .nav-prev {{ left: 10px; }}
    .nav-next {{ right: 10px; }}
    .slide-pill {{ position: absolute; bottom: 10px; left: 12px; background: rgba(9, 14, 26, 0.88); border: 1px solid rgba(255,255,255,0.15); padding: 4px 10px; border-radius: 999px; font-size: 0.74rem; font-weight: 700; color: #fef3c7; }}
    .thumbs {{ display: flex; gap: 8px; overflow-x: auto; padding-bottom: 4px; }}
    .thumb {{ width: 58px; height: 72px; border-radius: 8px; object-fit: cover; border: 2px solid transparent; cursor: pointer; opacity: 0.65; flex-shrink: 0; background: var(--navy-950); }}
    .thumb.active {{ border-color: var(--gold-500); opacity: 1; }}

    .copy-panel {{ display: flex; flex-direction: column; gap: 13px; }}
    .copy-actions {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .box-label {{ font-size: 0.74rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: var(--gold-400); margin-bottom: 5px; }}
    .caption-box {{ background: rgba(9, 14, 26, 0.72); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 13px 15px; font-size: 0.87rem; color: #e2e8f0; white-space: pre-wrap; max-height: 235px; overflow-y: auto; font-family: 'Inter', 'Noto Sans Gurmukhi', sans-serif; }}
    .hashtag-box {{ background: rgba(30, 58, 138, 0.28); border: 1px solid rgba(96,165,250,0.28); border-radius: 12px; padding: 10px 14px; font-size: 0.82rem; color: #bfdbfe; font-weight: 600; word-break: break-word; }}
    .story-box {{ background: rgba(217, 119, 6, 0.12); border: 1px solid rgba(245, 158, 11, 0.34); border-radius: 12px; padding: 11px 14px; font-size: 0.84rem; color: #fef3c7; }}

    .lightbox {{ position: fixed; inset: 0; background: rgba(5, 8, 16, 0.92); display: none; align-items: center; justify-content: center; z-index: 999; padding: 24px; }}
    .lightbox.open {{ display: flex; }}
    .lightbox img {{ max-width: 92vw; max-height: 88vh; border-radius: 12px; }}
    .lb-close {{ position: fixed; top: 18px; right: 24px; background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.25); color: #fff; font-size: 1.4rem; width: 44px; height: 44px; border-radius: 50%; cursor: pointer; }}
    .lb-caption {{ position: fixed; bottom: 18px; left: 50%; transform: translateX(-50%); background: rgba(15,23,42,0.92); border: 1px solid rgba(245,158,11,0.45); color: #fef3c7; padding: 8px 18px; border-radius: 999px; font-size: 0.84rem; font-weight: 700; }}
    .toast {{ position: fixed; bottom: 24px; right: 24px; background: var(--emerald); color: #052e16; font-weight: 800; font-size: 0.88rem; padding: 12px 20px; border-radius: 12px; opacity: 0; transform: translateY(12px); transition: all 0.2s ease; pointer-events: none; z-index: 1000; }}
    .toast.show {{ opacity: 1; transform: translateY(0); }}
    footer.site-footer {{ border-top: 1px solid rgba(255,255,255,0.1); padding: 26px 0 40px; text-align: center; color: var(--slate-400); font-size: 0.85rem; }}
    footer.site-footer a {{ color: var(--gold-400); text-decoration: none; font-weight: 700; }}
  </style>
</head>
<body>
  <header class="hero">
    <div class="container">
      <div class="hero-top">
        <div class="brand">
          <img src="assets/srpa-logo.png" alt="SikhRPA Official Logo" />
          <div>
            <h1>SikhRPA <span>Instagram Content Hub</span></h1>
            <p>Dec 2026 Launch Series (12 Posts) + Full-Year 2027 Weekly Posts &amp; Stories (52 Weeks + Major Sikh Holidays)</p>
          </div>
        </div>
        <div class="hero-actions">
          <a class="btn btn-gold" href="schedule-2027.csv" download>⬇ 2027 CSV (52 Weeks)</a>
          <a class="btn btn-blue" href="schedule.csv" download>⬇ Dec 2026 CSV</a>
          <a class="btn" href="https://sikhrpa.org" target="_blank" rel="noopener">🌐 sikhrpa.org</a>
        </div>
      </div>

      <div class="stats-bar">
        <div class="stat"><strong>64+ Posts</strong><span>12 Launch + 52 Weekly (2027)</span></div>
        <div class="stat"><strong>170 PNGs</strong><span>4:5 Posts, Reels &amp; 9:16 Stories</span></div>
        <div class="stat"><strong>{holiday_count} Sikh Holidays</strong><span>2027 Gurpurabs &amp; Major Days</span></div>
        <div class="stat"><strong>501(c)(3)</strong><span>EIN 42-2595402 • EN + ਪੰਜਾਬੀ</span></div>
      </div>
    </div>
  </header>

  <main class="container">
    <div class="series-tabs">
      <button class="tab-btn active" id="tab2027" onclick="switchTab('2027')">
        📅 2027 Full-Year Weekly Series (52 Weeks)
        <span>52 Weekly 4:5 Posts + 52 Companion 9:16 Stories • Includes {holiday_count} Major Sikh Holidays</span>
      </button>
      <button class="tab-btn" id="tab2026" onclick="switchTab('2026')">
        🚀 Dec 2026 Launch Series (12 Multi-Slide Posts)
        <span>65 Production PNGs (Carousels, Reels &amp; Stories) • Dec 1 – Dec 26, 2026</span>
      </button>
    </div>

    <div class="controls" id="controlsBar"></div>
    <section class="posts-grid" id="postsGrid"></section>
  </main>

  <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
    <button class="lb-close" onclick="closeLightbox(event)" aria-label="Close">×</button>
    <img id="lbImg" src="" alt="Preview" />
    <div class="lb-caption" id="lbCaption"></div>
  </div>
  <div class="toast" id="toast">Copied!</div>

  <footer class="site-footer">
    <div class="container">
      <div class="pa" style="color:#fde68a;font-size:1.05rem;font-weight:700;margin-bottom:6px;">
        ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!
      </div>
      <div>Sikh Rifle and Pistol Association (SikhRPA) • California 501(c)(3) Nonprofit Public Benefit Corporation • Federal EIN: 42-2595402</div>
      <div style="margin-top:6px;"><a href="https://sikhrpa.org">sikhrpa.org</a> • <a href="mailto:president@sikhrpa.org">president@sikhrpa.org</a></div>
    </div>
  </footer>

  <script>
    const DEC_2026 = {dec_json};
    const WEEKLY_2027 = {weekly_json};

    let currentTab = "2027";
    let filterPrimary = "all";
    let filterSecondary = "all";
    let searchTerm = "";
    const activeSlides = {{}};

    function showToast(msg) {{
      const el = document.getElementById("toast");
      el.textContent = msg;
      el.classList.add("show");
      clearTimeout(window.__tt);
      window.__tt = setTimeout(() => el.classList.remove("show"), 2200);
    }}

    async function copyText(text, label) {{
      try {{
        await navigator.clipboard.writeText(text);
        showToast("✓ Copied " + label);
      }} catch {{
        const ta = document.createElement("textarea");
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
        showToast("✓ Copied " + label);
      }}
    }}

    function openLightbox(src, caption) {{
      document.getElementById("lbImg").src = src;
      document.getElementById("lbCaption").textContent = caption;
      document.getElementById("lightbox").classList.add("open");
    }}
    function closeLightbox(e) {{
      if (e.target.id === "lightbox" || e.target.classList.contains("lb-close")) {{
        document.getElementById("lightbox").classList.remove("open");
      }}
    }}
    document.addEventListener("keydown", e => {{ if (e.key === "Escape") document.getElementById("lightbox").classList.remove("open"); }});

    function escapeHtml(s) {{ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }}

    function switchTab(tab) {{
      currentTab = tab;
      filterPrimary = "all";
      filterSecondary = "all";
      searchTerm = "";
      document.getElementById("tab2027").classList.toggle("active", tab === "2027");
      document.getElementById("tab2026").classList.toggle("active", tab === "2026");
      renderControls();
      renderPosts();
    }}

    function renderControls() {{
      const bar = document.getElementById("controlsBar");
      if (currentTab === "2027") {{
        bar.innerHTML = `
          <div class="filter-group">
            <button class="chip ${{filterPrimary==='all'?'active':''}}" onclick="setPrimary('all')">All 52 Weeks</button>
            <button class="chip ${{filterPrimary==='1'?'active':''}}" onclick="setPrimary('1')">Q1 (Jan–Mar)</button>
            <button class="chip ${{filterPrimary==='2'?'active':''}}" onclick="setPrimary('2')">Q2 (Apr–Jun)</button>
            <button class="chip ${{filterPrimary==='3'?'active':''}}" onclick="setPrimary('3')">Q3 (Jul–Sep)</button>
            <button class="chip ${{filterPrimary==='4'?'active':''}}" onclick="setPrimary('4')">Q4 (Oct–Dec)</button>
          </div>
          <div class="filter-group">
            <button class="chip ${{filterSecondary==='all'?'active':''}}" onclick="setSecondary('all')">All Topics</button>
            <button class="chip ${{filterSecondary==='holiday'?'active':''}}" onclick="setSecondary('holiday')">★ Sikh Holidays ({holiday_count})</button>
            <button class="chip ${{filterSecondary==='safety'?'active':''}}" onclick="setSecondary('safety')">Safety</button>
            <button class="chip ${{filterSecondary==='compliance'?'active':''}}" onclick="setSecondary('compliance')">CA Law</button>
            <button class="chip ${{filterSecondary==='marksmanship'?'active':''}}" onclick="setSecondary('marksmanship')">Marksmanship</button>
            <button class="chip ${{filterSecondary==='trauma'?'active':''}}" onclick="setSecondary('trauma')">Trauma</button>
            <button class="chip ${{filterSecondary==='community'?'active':''}}" onclick="setSecondary('community')">Community</button>
          </div>
          <input class="search-input" id="searchInput" type="search" value="${{escapeHtml(searchTerm)}}" oninput="onSearch(this.value)" placeholder="Search week, holiday, law..." />
        `;
      }} else {{
        bar.innerHTML = `
          <div class="filter-group">
            <button class="chip ${{filterPrimary==='all'?'active':''}}" onclick="setPrimary('all')">All 4 Weeks</button>
            <button class="chip ${{filterPrimary==='1'?'active':''}}" onclick="setPrimary('1')">Week 1</button>
            <button class="chip ${{filterPrimary==='2'?'active':''}}" onclick="setPrimary('2')">Week 2</button>
            <button class="chip ${{filterPrimary==='3'?'active':''}}" onclick="setPrimary('3')">Week 3</button>
            <button class="chip ${{filterPrimary==='4'?'active':''}}" onclick="setPrimary('4')">Week 4</button>
          </div>
          <div class="filter-group">
            <button class="chip ${{filterSecondary==='all'?'active':''}}" onclick="setSecondary('all')">All Formats</button>
            <button class="chip ${{filterSecondary==='carousel'?'active':''}}" onclick="setSecondary('carousel')">Carousels</button>
            <button class="chip ${{filterSecondary==='reel'?'active':''}}" onclick="setSecondary('reel')">Reels</button>
            <button class="chip ${{filterSecondary==='single'?'active':''}}" onclick="setSecondary('single')">Single + Story</button>
          </div>
          <input class="search-input" id="searchInput" type="search" value="${{escapeHtml(searchTerm)}}" oninput="onSearch(this.value)" placeholder="Search Dec 2026 posts..." />
        `;
      }}
    }}

    function setPrimary(v) {{ filterPrimary = v; renderControls(); renderPosts(); }}
    function setSecondary(v) {{ filterSecondary = v; renderControls(); renderPosts(); }}
    function onSearch(v) {{ searchTerm = v.trim().toLowerCase(); renderPosts(); }}

    function getItem(key) {{
      if (key.startsWith("2027-")) {{
        const w = Number(key.split("-")[1]);
        return WEEKLY_2027.find(x => x.week === w);
      }}
      const n = Number(key.split("-")[1]);
      return DEC_2026.find(x => x.number === n);
    }}

    function setSlide(key, idx) {{
      const item = getItem(key);
      if (!item) return;
      const total = item.slides.length;
      const next = ((idx % total) + total) % total;
      activeSlides[key] = next;
      const s = item.slides[next];
      const img = document.getElementById("img-" + key);
      const pill = document.getElementById("pill-" + key);
      const dl = document.getElementById("dl-" + key);
      if (img) {{
        img.src = s.path;
        img.onclick = () => openLightbox(s.path, `${{item.title}} • ${{s.filename}} (${{s.width}}×${{s.height}})`);
      }}
      if (pill) pill.textContent = `${{next + 1}} / ${{total}} • ${{s.filename}} (${{s.aspect}})`;
      if (dl) {{ dl.href = s.path; dl.download = `${{item.slug}}-${{s.filename}}`; }}
      document.querySelectorAll(`[data-thumb="${{key}}"]`).forEach((t, i) => t.classList.toggle("active", i === next));
    }}

    function copyItem(key, mode) {{
      const item = getItem(key);
      if (!item) return;
      if (mode === "all") copyText(item.caption + "\\n\\n" + item.hashtags, "Caption + Hashtags");
      else if (mode === "cap") copyText(item.caption, "Caption");
      else if (mode === "tags") copyText(item.hashtags, "Hashtags");
      else if (mode === "story") copyText(item.story_prompt, "Story Prompt");
    }}

    function renderPosts() {{
      const grid = document.getElementById("postsGrid");
      const list = currentTab === "2027"
        ? WEEKLY_2027.filter(p => {{
            if (filterPrimary !== "all" && String(p.quarter) !== filterPrimary) return false;
            if (filterSecondary !== "all" && p.category !== filterSecondary) return false;
            if (searchTerm && !(p.title + " " + p.caption + " " + p.hashtags + " " + p.date_display).toLowerCase().includes(searchTerm)) return false;
            return true;
          }})
        : DEC_2026.filter(p => {{
            if (filterPrimary !== "all" && String(p.week) !== filterPrimary) return false;
            if (filterSecondary !== "all" && p.format_type !== filterSecondary) return false;
            if (searchTerm && !(p.title + " " + p.caption + " " + p.hashtags + " " + p.date_display).toLowerCase().includes(searchTerm)) return false;
            return true;
          }});

      if (!list.length) {{
        grid.innerHTML = `<div class="post-card" style="padding:40px;text-align:center;color:#94a3b8;">No posts match your current filter.</div>`;
        return;
      }}

      grid.innerHTML = list.map(p => {{
        const key = currentTab === "2027" ? ("2027-" + p.week) : ("2026-" + p.number);
        const idx = activeSlides[key] || 0;
        const cur = p.slides[idx];
        const numLabel = currentTab === "2027" ? ("W" + String(p.week).padStart(2, "0")) : String(p.number).padStart(2, "0");
        const timeStr = currentTab === "2027" ? p.time_tz : p.time_pst;
        const captionTxtPath = currentTab === "2027" ? `weekly-2027/${{p.slug}}/caption.txt` : `posts/${{p.slug}}/caption.txt`;
        const isHoliday = Boolean(p.is_holiday);

        const badgesHtml = currentTab === "2027"
          ? `<span class="badge badge-gold">Q${{p.quarter}} • Week ${{String(p.week).padStart(2,'0')}}</span>
             <span class="badge ${{isHoliday ? 'badge-gold' : ''}}">${{isHoliday ? '★ ' : ''}}${{escapeHtml(p.category_label)}}</span>
             <span class="badge">4:5 Post + 9:16 Story</span>`
          : `<span class="badge badge-gold">Week ${{p.week}}</span>
             <span class="badge">${{escapeHtml(p.format)}}</span>
             <span class="badge">${{p.slides.length}} PNGs</span>`;

        const thumbs = p.slides.map((s, i) => `
          <img class="thumb ${{i===idx?'active':''}}" loading="lazy" src="${{s.path}}" alt="${{s.filename}}"
               data-thumb="${{key}}" onclick="setSlide('${{key}}', ${{i}})" />
        `).join("");

        return `
        <article class="post-card ${{isHoliday ? 'holiday-card' : ''}}">
          <div class="post-head">
            <div class="post-title-wrap">
              <div class="post-num">${{numLabel}}</div>
              <div>
                <h2>${{escapeHtml(p.title)}}</h2>
                <div class="post-meta">📅 ${{escapeHtml(p.date_display)}} &nbsp;•&nbsp; ⏰ ${{escapeHtml(timeStr)}} &nbsp;•&nbsp; 🔗 <a href="${{p.url}}" target="_blank" style="color:#fbbf24;text-decoration:none;font-weight:700;">${{p.url.replace('https://','')}}</a></div>
              </div>
            </div>
            <div class="badges">${{badgesHtml}}</div>
          </div>

          <div class="post-content">
            <div class="stage-wrap">
              <div class="stage">
                <img id="img-${{key}}" loading="lazy" src="${{cur.path}}" alt="${{cur.filename}}"
                     onclick="openLightbox('${{cur.path}}', '${{escapeHtml(p.title)}} • ${{cur.filename}}')" />
                ${{p.slides.length > 1 ? `
                  <button class="nav-btn nav-prev" onclick="setSlide('${{key}}', (activeSlides['${{key}}']||0)-1)" aria-label="Previous">‹</button>
                  <button class="nav-btn nav-next" onclick="setSlide('${{key}}', (activeSlides['${{key}}']||0)+1)" aria-label="Next">›</button>
                ` : ''}}
                <div class="slide-pill" id="pill-${{key}}">${{idx + 1}} / ${{p.slides.length}} • ${{cur.filename}} (${{cur.aspect}})</div>
              </div>
              <div class="thumbs">${{thumbs}}</div>
              <div style="display:flex;gap:8px;flex-wrap:wrap;">
                <a class="btn" id="dl-${{key}}" href="${{cur.path}}" download="${{p.slug}}-${{cur.filename}}" style="font-size:0.79rem;padding:7px 11px;">⬇ Download Current PNG</a>
                <a class="btn" href="${{captionTxtPath}}" target="_blank" style="font-size:0.79rem;padding:7px 11px;">📄 caption.txt</a>
              </div>
            </div>

            <div class="copy-panel">
              <div class="copy-actions">
                <button class="btn btn-gold" onclick="copyItem('${{key}}','all')">📋 Copy Caption + Hashtags</button>
                <button class="btn btn-blue" onclick="copyItem('${{key}}','cap')">Copy Caption</button>
                <button class="btn" onclick="copyItem('${{key}}','tags')">Copy Hashtags</button>
                <button class="btn" onclick="copyItem('${{key}}','story')">Copy Story Prompt</button>
              </div>
              <div>
                <div class="box-label">Ready-to-Paste Instagram Caption</div>
                <div class="caption-box">${{escapeHtml(p.caption)}}</div>
              </div>
              <div>
                <div class="box-label">Educational Hashtags (Meta Policy Safe)</div>
                <div class="hashtag-box">${{escapeHtml(p.hashtags)}}</div>
              </div>
              <div>
                <div class="box-label">Companion 9:16 Story Prompt</div>
                <div class="story-box">${{escapeHtml(p.story_prompt)}}</div>
              </div>
            </div>
          </div>
        </article>`;
      }}).join("");
    }}

    renderControls();
    renderPosts();
  </script>
</body>
</html>
"""
    (ROOT_DIR / "index.html").write_text(index_html, encoding="utf-8")


def main() -> int:
    assert len(WEEKLY_2027_POSTS) == 52, f"Expected 52 weeks, got {len(WEEKLY_2027_POSTS)}"
    print(f"Loaded {len(WEEKLY_2027_POSTS)} weekly 2027 posts (104 total PNGs: 52 posts + 52 stories).")

    issues = audit_weekly_policy()
    if issues:
        print("POLICY AUDIT FAILURES:")
        for i in issues:
            print("  -", i)
        return 1
    print("✓ Meta policy guardrail audit passed across all 52 weeks (0 violations).")

    chrome_path = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    launch_kwargs: dict = {"args": ["--no-sandbox", "--disable-gpu", "--font-render-hinting=none"]}
    if chrome_path:
        launch_kwargs["executable_path"] = chrome_path

    overflows: list[str] = []
    rendered = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(**launch_kwargs)
        context = browser.new_context(device_scale_factor=1)
        page = context.new_page()

        for item in WEEKLY_2027_POSTS:
            out_dir = WEEKLY_DIR / item["slug"]
            out_dir.mkdir(parents=True, exist_ok=True)

            # Write ready-to-paste caption.txt
            cap = build_caption(item)
            caption_txt = (
                f"========================================================================\n"
                f"2027 WEEK {item['week']:02d} — {item['title']}\n"
                f"Schedule: {item['date_display']} • {item['time_tz']}\n"
                f"Category: {CATEGORY_META[item['category']]['label']}"
                f"{' (MAJOR SIKH HOLIDAY)' if item['is_holiday'] else ''}\n"
                f"Link:     {item['url']}\n"
                f"Files:    post.png (1080x1350 4:5), story.png (1080x1920 9:16)\n"
                f"========================================================================\n\n"
                f"--- CAPTION (READY TO PASTE) ---\n\n"
                f"{cap}\n\n"
                f"--- HASHTAGS (READY TO PASTE) ---\n\n"
                f"{item['hashtags']}\n\n"
                f"--- COMPANION STORY PROMPT (9:16 story.png) ---\n\n"
                f"{item['story_prompt_box']}\n"
            )
            (out_dir / "caption.txt").write_text(caption_txt, encoding="utf-8")

            # Render 4:5 Feed Post + 9:16 Companion Story
            for fname, w, h, html_str in [
                ("post.png", 1080, 1350, build_weekly_post_html(item)),
                ("story.png", 1080, 1920, build_weekly_story_html(item)),
            ]:
                page.set_viewport_size({"width": w, "height": h})
                page.set_content(html_str, wait_until="load")
                page.evaluate("() => document.fonts.ready")
                metrics = page.evaluate(
                    """() => {
                      const c = document.querySelector('.canvas');
                      const b = document.querySelector('.slide-body');
                      return { c: c.scrollHeight - c.clientHeight, b: b.scrollHeight - b.clientHeight };
                    }"""
                )
                if metrics["c"] > 2 or metrics["b"] > 2:
                    overflows.append(f"{item['slug']}/{fname}: canvas={metrics['c']}px, body={metrics['b']}px")
                page.screenshot(path=str(out_dir / fname), type="png", full_page=False)
                rendered += 1

            print(f"  [Week {item['week']:02d}/52] Rendered {item['slug']} (post.png + story.png)")

        browser.close()

    write_schedule_2027_csv()
    print("✓ Generated schedule-2027.csv")
    write_unified_gallery_html()
    print("✓ Upgraded index.html (Dec 2026 + Full-Year 2027 52-Week Hub)")

    if overflows:
        print(f"\n⚠ {len(overflows)} OVERFLOW WARNING(S):")
        for o in overflows:
            print("  -", o)
        return 2

    print(f"\n✓ All {rendered} PNG graphics (52 weekly posts + 52 weekly stories) rendered with ZERO overflow!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
