#!/usr/bin/env python3
"""
SikhRPA 4-Week Instagram Series — Reproducible Master Generator
Renders all 65 production-ready PNGs (1080x1350 4:5 & 1080x1920 9:16) via
Playwright + Chrome with Inter and Noto Sans/Serif Gurmukhi fonts, writes
ready-to-paste caption.txt files, builds schedule.csv, and generates the
GitHub-Pages-ready interactive gallery (index.html).

Usage:
    python3 scripts/generate_all.py
"""

from __future__ import annotations

import csv
import html as html_lib
import json
import os
import re
import shutil
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from content_posts_1_to_6 import get_posts_1_to_6  # noqa: E402
from content_posts_7_to_12 import get_posts_7_to_12  # noqa: E402
from styles import ROOT_DIR, build_slide_html  # noqa: E402

POSTS_DIR = ROOT_DIR / "posts"

# Meta / Instagram Regulated-Goods Firearm Policy Guardrail Blocklist
FORBIDDEN_TERMS = [
    r"\bfor sale\b",
    r"\bbuy guns?\b",
    r"\bammo for sale\b",
    r"\bgiveaway\b",
    r"\braffle\b",
    r"\bdiscount code\b",
    r"\bpromo code\b",
    r"\bshop now\b",
    r"#pewpew\b",
    r"#gunsofinstagram\b",
    r"#gunsdaily\b",
    r"#2a\b",
    r"#tacticalgear\b",
    r"#firearmsforsale\b",
]


def audit_policy_guardrails(posts: list[dict]) -> list[str]:
    """Scan all captions, hashtags, Story prompts, and slide copy for policy violations."""
    issues: list[str] = []
    for post in posts:
        fields = [
            ("caption", post["caption"]),
            ("hashtags", post["hashtags"]),
            ("story_prompt", post["story_prompt"]),
        ]
        for slide in post["slides"]:
            fields.append((slide["filename"], slide["body_html"]))
        for field_name, text in fields:
            for pattern in FORBIDDEN_TERMS:
                if re.search(pattern, text, flags=re.IGNORECASE):
                    issues.append(f"Post {post['number']:02d} ({field_name}) matched forbidden term: {pattern}")
    return issues


def write_caption_file(post: dict, post_dir: Path) -> None:
    """Write ready-to-paste caption.txt inside each post directory."""
    media_list = ", ".join(s["filename"] for s in post["slides"])
    content = (
        f"========================================================================\n"
        f"POST {post['number']:02d} — {post['title']}\n"
        f"Schedule: {post['date_display']} • {post['time_pst']}\n"
        f"Format:   {post['format']}\n"
        f"Link:     {post['url']}\n"
        f"Media:    {media_list}\n"
        f"========================================================================\n\n"
        f"--- CAPTION (READY TO PASTE) ---\n\n"
        f"{post['caption']}\n\n"
        f"--- HASHTAGS (READY TO PASTE) ---\n\n"
        f"{post['hashtags']}\n\n"
        f"--- INSTAGRAM STORY PROMPT ---\n\n"
        f"{post['story_prompt']}\n"
    )
    (post_dir / "caption.txt").write_text(content, encoding="utf-8")


def write_schedule_csv(posts: list[dict]) -> None:
    """Write schedule.csv formatted for Meta Business Suite / Buffer / Later."""
    csv_path = ROOT_DIR / "schedule.csv"
    # Convert 11:00 AM PST -> 24h ISO timestamp with -08:00 offset (PST in December)
    time_map = {
        "10:00 AM PST": "10:00:00-08:00",
        "10:30 AM PST": "10:30:00-08:00",
        "11:00 AM PST": "11:00:00-08:00",
        "12:00 PM PST": "12:00:00-08:00",
        "4:00 PM PST": "16:00:00-08:00",
        "5:30 PM PST": "17:30:00-08:00",
        "6:00 PM PST": "18:00:00-08:00",
    }

    fieldnames = [
        "Post Number",
        "Week",
        "Scheduled Date",
        "Scheduled Time (PST)",
        "ISO Timestamp (PST)",
        "Format",
        "Title",
        "Post Folder",
        "Media Files",
        "Slide Count",
        "Caption",
        "Hashtags",
        "Caption + Hashtags",
        "Link in Bio URL",
        "Story Prompt",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for post in posts:
            iso_time = time_map.get(post["time_pst"], "12:00:00-08:00")
            media_paths = "; ".join(f"posts/{post['slug']}/{s['filename']}" for s in post["slides"])
            full_text = f"{post['caption']}\n\n{post['hashtags']}"
            writer.writerow(
                {
                    "Post Number": f"{post['number']:02d}",
                    "Week": f"Week {post['week']}",
                    "Scheduled Date": post["date_display"],
                    "Scheduled Time (PST)": post["time_pst"],
                    "ISO Timestamp (PST)": f"{post['date_iso']}T{iso_time}",
                    "Format": post["format"],
                    "Title": post["title"],
                    "Post Folder": f"posts/{post['slug']}",
                    "Media Files": media_paths,
                    "Slide Count": len(post["slides"]),
                    "Caption": post["caption"],
                    "Hashtags": post["hashtags"],
                    "Caption + Hashtags": full_text,
                    "Link in Bio URL": post["url"],
                    "Story Prompt": post["story_prompt"],
                }
            )


def write_gallery_html(posts: list[dict]) -> None:
    """Generate interactive, GitHub-Pages-ready index.html gallery with one-click copy buttons."""
    total_pngs = sum(len(p["slides"]) for p in posts)
    gallery_data = []
    for p in posts:
        gallery_data.append(
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

    data_json = json.dumps(gallery_data, ensure_ascii=False)

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SikhRPA 4-Week Instagram Content Series Gallery | Dec 2026</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+Gurmukhi:wght@400;600;700&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --navy-950: #090e1a;
      --navy-900: #0f172a;
      --navy-800: #16223a;
      --navy-700: #1e293b;
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
      background: rgba(9, 14, 26, 0.72);
      backdrop-filter: blur(12px);
      padding: 36px 0 32px;
    }}
    .hero-top {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 18px;
    }}
    .brand img {{
      width: 72px;
      height: 72px;
      border-radius: 50%;
      border: 2.5px solid var(--gold-500);
      background: var(--navy-950);
      box-shadow: 0 6px 20px rgba(0,0,0,0.45);
    }}
    .brand h1 {{
      font-size: clamp(1.5rem, 2.8vw, 2.25rem);
      font-weight: 900;
      letter-spacing: -0.02em;
    }}
    .brand h1 span {{ color: var(--gold-400); }}
    .brand p {{ color: var(--slate-300); font-size: 0.95rem; margin-top: 3px; }}
    .hero-actions {{ display: flex; flex-wrap: wrap; gap: 10px; }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border: 1px solid rgba(255,255,255,0.14);
      background: rgba(30, 41, 59, 0.85);
      color: #fff;
      font-size: 0.88rem;
      font-weight: 700;
      padding: 10px 16px;
      border-radius: 10px;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.16s ease;
    }}
    .btn:hover {{ transform: translateY(-1px); border-color: var(--gold-500); }}
    .btn-gold {{
      background: linear-gradient(135deg, var(--gold-600), var(--gold-500));
      color: var(--navy-950);
      border-color: var(--gold-400);
    }}
    .btn-blue {{
      background: linear-gradient(135deg, var(--blue-900), #2563eb);
      border-color: rgba(96,165,250,0.45);
    }}
    .stats-bar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 14px;
      margin-top: 24px;
    }}
    .stat {{
      background: rgba(22, 34, 58, 0.72);
      border: 1px solid rgba(255,255,255,0.09);
      border-radius: 14px;
      padding: 14px 18px;
    }}
    .stat strong {{ display: block; font-size: 1.35rem; color: var(--gold-400); font-weight: 900; }}
    .stat span {{ font-size: 0.78rem; color: var(--slate-400); text-transform: uppercase; letter-spacing: 0.06em; font-weight: 700; }}

    .controls {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      margin: 28px 0 22px;
    }}
    .filter-group {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .chip {{
      border: 1px solid rgba(255,255,255,0.14);
      background: rgba(22, 34, 58, 0.75);
      color: var(--slate-300);
      font-size: 0.83rem;
      font-weight: 700;
      padding: 8px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .chip.active, .chip:hover {{
      background: rgba(217,119,6,0.22);
      border-color: var(--gold-500);
      color: #fef3c7;
    }}
    .search-input {{
      background: rgba(15, 23, 42, 0.88);
      border: 1px solid rgba(255,255,255,0.15);
      color: #fff;
      padding: 9px 16px;
      border-radius: 10px;
      font-size: 0.9rem;
      min-width: 240px;
      outline: none;
    }}
    .search-input:focus {{ border-color: var(--gold-500); }}

    .posts-grid {{
      display: flex;
      flex-direction: column;
      gap: 28px;
      padding-bottom: 64px;
    }}
    .post-card {{
      background: rgba(22, 34, 58, 0.78);
      border: 1px solid rgba(255,255,255,0.11);
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 14px 36px rgba(0,0,0,0.28);
    }}
    .post-head {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      padding: 20px 26px;
      background: rgba(9, 14, 26, 0.55);
      border-bottom: 1px solid rgba(255,255,255,0.09);
    }}
    .post-title-wrap {{ display: flex; align-items: center; gap: 14px; }}
    .post-num {{
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: linear-gradient(135deg, var(--gold-600), var(--gold-500));
      color: var(--navy-950);
      font-weight: 900;
      font-size: 1.05rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .post-title-wrap h2 {{ font-size: 1.15rem; font-weight: 800; color: #fff; }}
    .post-meta {{ font-size: 0.84rem; color: var(--slate-300); margin-top: 2px; }}
    .badges {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .badge {{
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 5px 11px;
      border-radius: 999px;
      background: rgba(30,58,138,0.55);
      border: 1px solid rgba(96,165,250,0.38);
      color: #dbeafe;
    }}
    .badge-gold {{
      background: rgba(217,119,6,0.2);
      border-color: rgba(245,158,11,0.5);
      color: #fde68a;
    }}

    .post-content {{
      display: grid;
      grid-template-columns: minmax(300px, 430px) 1fr;
      gap: 26px;
      padding: 24px 26px;
    }}
    @media (max-width: 920px) {{
      .post-content {{ grid-template-columns: 1fr; }}
    }}

    /* Carousel Stage */
    .stage-wrap {{ display: flex; flex-direction: column; gap: 12px; }}
    .stage {{
      position: relative;
      background: var(--navy-950);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 16px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 360px;
      max-height: 540px;
    }}
    .stage img {{
      max-width: 100%;
      max-height: 520px;
      object-fit: contain;
      display: block;
      cursor: zoom-in;
    }}
    .nav-btn {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      border: 1px solid rgba(255,255,255,0.22);
      background: rgba(15, 23, 42, 0.85);
      color: #fff;
      font-size: 1.15rem;
      font-weight: 800;
      cursor: pointer;
    }}
    .nav-btn:hover {{ background: var(--gold-600); color: var(--navy-950); }}
    .nav-prev {{ left: 10px; }}
    .nav-next {{ right: 10px; }}
    .slide-pill {{
      position: absolute;
      bottom: 10px;
      left: 12px;
      background: rgba(9, 14, 26, 0.86);
      border: 1px solid rgba(255,255,255,0.15);
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 0.74rem;
      font-weight: 700;
      color: #fef3c7;
    }}
    .thumbs {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
    }}
    .thumb {{
      width: 58px;
      height: 72px;
      border-radius: 8px;
      object-fit: cover;
      border: 2px solid transparent;
      cursor: pointer;
      opacity: 0.65;
      flex-shrink: 0;
      background: var(--navy-950);
    }}
    .thumb.active {{
      border-color: var(--gold-500);
      opacity: 1;
    }}

    /* Copy panel */
    .copy-panel {{ display: flex; flex-direction: column; gap: 14px; }}
    .copy-actions {{ display: flex; flex-wrap: wrap; gap: 9px; }}
    .box-label {{
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--gold-400);
      margin-bottom: 6px;
    }}
    .caption-box {{
      background: rgba(9, 14, 26, 0.72);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 12px;
      padding: 14px 16px;
      font-size: 0.89rem;
      color: #e2e8f0;
      white-space: pre-wrap;
      max-height: 255px;
      overflow-y: auto;
      font-family: 'Inter', 'Noto Sans Gurmukhi', sans-serif;
    }}
    .hashtag-box {{
      background: rgba(30, 58, 138, 0.28);
      border: 1px solid rgba(96,165,250,0.28);
      border-radius: 12px;
      padding: 11px 15px;
      font-size: 0.84rem;
      color: #bfdbfe;
      font-weight: 600;
      word-break: break-word;
    }}
    .story-box {{
      background: rgba(217, 119, 6, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.34);
      border-radius: 12px;
      padding: 12px 15px;
      font-size: 0.85rem;
      color: #fef3c7;
    }}

    /* Lightbox */
    .lightbox {{
      position: fixed;
      inset: 0;
      background: rgba(5, 8, 16, 0.92);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 999;
      padding: 24px;
    }}
    .lightbox.open {{ display: flex; }}
    .lightbox img {{
      max-width: 92vw;
      max-height: 88vh;
      border-radius: 12px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.7);
    }}
    .lb-close {{
      position: fixed;
      top: 18px;
      right: 24px;
      background: rgba(255,255,255,0.12);
      border: 1px solid rgba(255,255,255,0.25);
      color: #fff;
      font-size: 1.4rem;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      cursor: pointer;
    }}
    .lb-caption {{
      position: fixed;
      bottom: 18px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(15,23,42,0.92);
      border: 1px solid rgba(245,158,11,0.45);
      color: #fef3c7;
      padding: 8px 18px;
      border-radius: 999px;
      font-size: 0.84rem;
      font-weight: 700;
    }}

    /* Toast */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--emerald);
      color: #052e16;
      font-weight: 800;
      font-size: 0.9rem;
      padding: 12px 20px;
      border-radius: 12px;
      box-shadow: 0 12px 30px rgba(0,0,0,0.4);
      opacity: 0;
      transform: translateY(12px);
      transition: all 0.2s ease;
      pointer-events: none;
      z-index: 1000;
    }}
    .toast.show {{ opacity: 1; transform: translateY(0); }}

    footer.site-footer {{
      border-top: 1px solid rgba(255,255,255,0.1);
      padding: 28px 0 42px;
      text-align: center;
      color: var(--slate-400);
      font-size: 0.86rem;
    }}
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
            <h1>SikhRPA <span>Instagram Content Series</span></h1>
            <p>4-Week Educational &amp; Safe Storage Campaign • Dec 1 – Dec 26, 2026 (Tue / Thu / Sat • PST)</p>
          </div>
        </div>
        <div class="hero-actions">
          <a class="btn btn-gold" href="schedule.csv" download>⬇ Download schedule.csv</a>
          <a class="btn btn-blue" href="https://sikhrpa.org" target="_blank" rel="noopener">🌐 sikhrpa.org</a>
          <a class="btn" href="https://github.com/Sikhrpa/instagram-series" target="_blank" rel="noopener">GitHub Repo</a>
        </div>
      </div>

      <div class="stats-bar">
        <div class="stat"><strong>12 Posts</strong><span>4 Weeks • Tue / Thu / Sat</span></div>
        <div class="stat"><strong>{total_pngs} PNGs</strong><span>1080×1350 (4:5) &amp; 1080×1920 (9:16)</span></div>
        <div class="stat"><strong>EN + ਪੰਜਾਬੀ</strong><span>Inter &amp; Noto Sans Gurmukhi</span></div>
        <div class="stat"><strong>501(c)(3)</strong><span>EIN 42-2595402 • Policy Compliant</span></div>
      </div>
    </div>
  </header>

  <main class="container">
    <div class="controls">
      <div class="filter-group" id="weekFilters">
        <button class="chip active" data-week="all">All 4 Weeks</button>
        <button class="chip" data-week="1">Week 1 (Dec 1–5)</button>
        <button class="chip" data-week="2">Week 2 (Dec 8–12)</button>
        <button class="chip" data-week="3">Week 3 (Dec 15–19)</button>
        <button class="chip" data-week="4">Week 4 (Dec 22–26)</button>
      </div>
      <div class="filter-group" id="formatFilters">
        <button class="chip active" data-fmt="all">All Formats</button>
        <button class="chip" data-fmt="carousel">Carousels</button>
        <button class="chip" data-fmt="reel">Reels</button>
        <button class="chip" data-fmt="single">Single + Story</button>
      </div>
      <input class="search-input" id="searchInput" type="search" placeholder="Search topic, statute, hashtag..." />
    </div>

    <section class="posts-grid" id="postsGrid"></section>
  </main>

  <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
    <button class="lb-close" onclick="closeLightbox(event)" aria-label="Close">×</button>
    <img id="lbImg" src="" alt="Full resolution preview" />
    <div class="lb-caption" id="lbCaption"></div>
  </div>

  <div class="toast" id="toast">Copied to clipboard!</div>

  <footer class="site-footer">
    <div class="container">
      <div class="pa" style="color:#fde68a;font-size:1.05rem;font-weight:700;margin-bottom:6px;">
        ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!
      </div>
      <div>
        Sikh Rifle and Pistol Association (SikhRPA) • IRS-Recognized California 501(c)(3) Nonprofit Public Benefit Corporation • Federal EIN: 42-2595402
      </div>
      <div style="margin-top:6px;">
        <a href="https://sikhrpa.org">sikhrpa.org</a> • <a href="mailto:president@sikhrpa.org">president@sikhrpa.org</a> • Strictly Educational &amp; Meta Policy Compliant
      </div>
    </div>
  </footer>

  <script>
    const POSTS = {data_json};
    let activeWeek = "all";
    let activeFmt = "all";
    let searchTerm = "";
    const activeSlides = {{}};
    POSTS.forEach(p => activeSlides[p.number] = 0);

    function showToast(msg) {{
      const el = document.getElementById("toast");
      el.textContent = msg;
      el.classList.add("show");
      clearTimeout(window.__toastTimer);
      window.__toastTimer = setTimeout(() => el.classList.remove("show"), 2200);
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

    document.addEventListener("keydown", (e) => {{
      if (e.key === "Escape") document.getElementById("lightbox").classList.remove("open");
    }});

    function setSlide(postNum, idx) {{
      const post = POSTS.find(p => p.number === postNum);
      if (!post) return;
      const total = post.slides.length;
      const next = ((idx % total) + total) % total;
      activeSlides[postNum] = next;
      const s = post.slides[next];
      const img = document.getElementById("stage-img-" + postNum);
      const pill = document.getElementById("stage-pill-" + postNum);
      const dl = document.getElementById("stage-dl-" + postNum);
      if (img) {{
        img.src = s.path;
        img.onclick = () => openLightbox(s.path, `Post ${{String(postNum).padStart(2,'0')}} • ${{s.filename}} (${{s.width}}×${{s.height}} • ${{s.aspect}})`);
      }}
      if (pill) pill.textContent = `${{next + 1}} / ${{total}} • ${{s.filename}} (${{s.aspect}})`;
      if (dl) {{
        dl.href = s.path;
        dl.download = s.filename;
      }}
      document.querySelectorAll(`[data-thumb-post="${{postNum}}"]`).forEach((t, i) => {{
        t.classList.toggle("active", i === next);
      }});
    }}

    function escapeHtml(str) {{
      return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }}

    function renderPosts() {{
      const grid = document.getElementById("postsGrid");
      const filtered = POSTS.filter(p => {{
        if (activeWeek !== "all" && String(p.week) !== activeWeek) return false;
        if (activeFmt !== "all" && p.format_type !== activeFmt) return false;
        if (searchTerm) {{
          const hay = (p.title + " " + p.caption + " " + p.hashtags + " " + p.date_display).toLowerCase();
          if (!hay.includes(searchTerm)) return false;
        }}
        return true;
      }});

      if (!filtered.length) {{
        grid.innerHTML = `<div class="post-card" style="padding:40px;text-align:center;color:#94a3b8;">No posts match your current filter.</div>`;
        return;
      }}

      grid.innerHTML = filtered.map(p => {{
        const idx = activeSlides[p.number] || 0;
        const cur = p.slides[idx];
        const thumbs = p.slides.map((s, i) => `
          <img class="thumb ${{i === idx ? 'active' : ''}}"
               src="${{s.path}}"
               alt="${{s.filename}}"
               title="${{s.filename}}"
               data-thumb-post="${{p.number}}"
               onclick="setSlide(${{p.number}}, ${{i}})" />
        `).join("");

        return `
        <article class="post-card">
          <div class="post-head">
            <div class="post-title-wrap">
              <div class="post-num">${{String(p.number).padStart(2, '0')}}</div>
              <div>
                <h2>${{escapeHtml(p.title)}}</h2>
                <div class="post-meta">📅 ${{escapeHtml(p.date_display)}} &nbsp;•&nbsp; ⏰ ${{escapeHtml(p.time_pst)}} &nbsp;•&nbsp; 🔗 <a href="${{p.url}}" target="_blank" style="color:#fbbf24;text-decoration:none;font-weight:700;">${{p.url.replace('https://','')}}</a></div>
              </div>
            </div>
            <div class="badges">
              <span class="badge badge-gold">Week ${{p.week}}</span>
              <span class="badge">${{escapeHtml(p.format)}}</span>
              <span class="badge">${{p.slides.length}} PNGs</span>
            </div>
          </div>

          <div class="post-content">
            <div class="stage-wrap">
              <div class="stage">
                <img id="stage-img-${{p.number}}"
                     src="${{cur.path}}"
                     alt="${{cur.filename}}"
                     onclick="openLightbox('${{cur.path}}', 'Post ${{String(p.number).padStart(2,'0')}} • ${{cur.filename}} (${{cur.width}}×${{cur.height}} • ${{cur.aspect}})')" />
                ${{p.slides.length > 1 ? `
                  <button class="nav-btn nav-prev" onclick="setSlide(${{p.number}}, (activeSlides[${{p.number}}]||0) - 1)" aria-label="Previous slide">‹</button>
                  <button class="nav-btn nav-next" onclick="setSlide(${{p.number}}, (activeSlides[${{p.number}}]||0) + 1)" aria-label="Next slide">›</button>
                ` : ''}}
                <div class="slide-pill" id="stage-pill-${{p.number}}">${{idx + 1}} / ${{p.slides.length}} • ${{cur.filename}} (${{cur.aspect}})</div>
              </div>
              <div class="thumbs">${{thumbs}}</div>
              <div style="display:flex;gap:8px;flex-wrap:wrap;">
                <a class="btn" id="stage-dl-${{p.number}}" href="${{cur.path}}" download="${{cur.filename}}" style="font-size:0.8rem;padding:7px 12px;">⬇ Download Current PNG</a>
                <a class="btn" href="posts/${{p.slug}}/caption.txt" target="_blank" style="font-size:0.8rem;padding:7px 12px;">📄 Open caption.txt</a>
              </div>
            </div>

            <div class="copy-panel">
              <div class="copy-actions">
                <button class="btn btn-gold" onclick="copyPostAll(${{p.number}})">📋 Copy Caption + Hashtags</button>
                <button class="btn btn-blue" onclick="copyPostCaption(${{p.number}})">Copy Caption Only</button>
                <button class="btn" onclick="copyPostHashtags(${{p.number}})">Copy Hashtags</button>
                <button class="btn" onclick="copyPostStory(${{p.number}})">Copy Story Prompt</button>
              </div>

              <div>
                <div class="box-label">Ready-to-Paste Instagram Caption</div>
                <div class="caption-box">${{escapeHtml(p.caption)}}</div>
              </div>

              <div>
                <div class="box-label">Clean Educational Hashtags (Meta Policy Safe)</div>
                <div class="hashtag-box">${{escapeHtml(p.hashtags)}}</div>
              </div>

              <div>
                <div class="box-label">Companion Story Prompt</div>
                <div class="story-box">${{escapeHtml(p.story_prompt)}}</div>
              </div>
            </div>
          </div>
        </article>`;
      }}).join("");
    }}

    function copyPostAll(num) {{
      const p = POSTS.find(x => x.number === num);
      copyText(p.caption + "\\n\\n" + p.hashtags, `Post ${{String(num).padStart(2,'0')}} Caption + Hashtags`);
    }}
    function copyPostCaption(num) {{
      const p = POSTS.find(x => x.number === num);
      copyText(p.caption, `Post ${{String(num).padStart(2,'0')}} Caption`);
    }}
    function copyPostHashtags(num) {{
      const p = POSTS.find(x => x.number === num);
      copyText(p.hashtags, `Post ${{String(num).padStart(2,'0')}} Hashtags`);
    }}
    function copyPostStory(num) {{
      const p = POSTS.find(x => x.number === num);
      copyText(p.story_prompt, `Post ${{String(num).padStart(2,'0')}} Story Prompt`);
    }}

    document.querySelectorAll("#weekFilters .chip").forEach(btn => {{
      btn.addEventListener("click", () => {{
        document.querySelectorAll("#weekFilters .chip").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        activeWeek = btn.dataset.week;
        renderPosts();
      }});
    }});

    document.querySelectorAll("#formatFilters .chip").forEach(btn => {{
      btn.addEventListener("click", () => {{
        document.querySelectorAll("#formatFilters .chip").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        activeFmt = btn.dataset.fmt;
        renderPosts();
      }});
    }});

    document.getElementById("searchInput").addEventListener("input", (e) => {{
      searchTerm = e.target.value.trim().toLowerCase();
      renderPosts();
    }});

    renderPosts();
  </script>
</body>
</html>
"""
    (ROOT_DIR / "index.html").write_text(index_html, encoding="utf-8")


def main() -> int:
    posts = get_posts_1_to_6() + get_posts_7_to_12()
    total_slides = sum(len(p["slides"]) for p in posts)
    print(f"Loaded {len(posts)} posts ({total_slides} total graphics).")

    # 1. Policy Guardrail Check
    policy_issues = audit_policy_guardrails(posts)
    if policy_issues:
        print("POLICY GUARDRAIL FAILURES DETECTED:")
        for issue in policy_issues:
            print("  -", issue)
        return 1
    print("✓ Meta firearm-education policy guardrail audit passed (0 violations).")

    # 2. Launch Playwright + Chrome (prefer system google-chrome if installed)
    chrome_path = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    launch_kwargs: dict = {"args": ["--no-sandbox", "--disable-gpu", "--font-render-hinting=none"]}
    if chrome_path:
        launch_kwargs["executable_path"] = chrome_path
        print(f"Rendering via Chrome at: {chrome_path}")
    else:
        print("Rendering via Playwright bundled Chromium.")

    overflow_warnings: list[str] = []
    rendered_count = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(**launch_kwargs)
        context = browser.new_context(device_scale_factor=1)
        page = context.new_page()

        for post in posts:
            post_dir = POSTS_DIR / post["slug"]
            post_dir.mkdir(parents=True, exist_ok=True)
            write_caption_file(post, post_dir)

            for slide in post["slides"]:
                w = slide["width"]
                h = slide["height"]
                page.set_viewport_size({"width": w, "height": h})

                full_html = build_slide_html(
                    body_html=slide["body_html"],
                    width=w,
                    height=h,
                    pill_text=slide.get("pill_text", "501(c)(3) Safety Education"),
                    pill_class=slide.get("pill_class", ""),
                    slide_label=slide.get("slide_label", ""),
                    footer_url=slide.get("footer_url", "sikhrpa.org"),
                    footer_right=slide.get("footer_right", "SWIPE →"),
                    theme=slide.get("theme", "default"),
                    frame_variant=slide.get("frame_variant", ""),
                    body_class=slide.get("body_class", ""),
                    show_header=slide.get("show_header", True),
                    show_footer=slide.get("show_footer", True),
                )

                page.set_content(full_html, wait_until="load")
                page.evaluate("() => document.fonts.ready")

                # Check overflow inside .slide-body and .canvas
                metrics = page.evaluate(
                    """() => {
                      const canvas = document.querySelector('.canvas');
                      const body = document.querySelector('.slide-body');
                      return {
                        canvasOverflow: canvas.scrollHeight - canvas.clientHeight,
                        bodyOverflow: body.scrollHeight - body.clientHeight
                      };
                    }"""
                )
                if metrics["canvasOverflow"] > 2 or metrics["bodyOverflow"] > 2:
                    overflow_warnings.append(
                        f"{post['slug']}/{slide['filename']}: "
                        f"canvasOverflow={metrics['canvasOverflow']}px, bodyOverflow={metrics['bodyOverflow']}px"
                    )

                out_png = post_dir / slide["filename"]
                page.screenshot(path=str(out_png), type="png", full_page=False)
                rendered_count += 1
                print(f"  [{rendered_count:02d}/{total_slides}] Rendered {post['slug']}/{slide['filename']} ({w}x{h})")

        browser.close()

    # 3. Generate schedule.csv and index.html
    write_schedule_csv(posts)
    print("✓ Generated schedule.csv")
    write_gallery_html(posts)
    print("✓ Generated index.html")

    if overflow_warnings:
        print(f"\n⚠ {len(overflow_warnings)} OVERFLOW WARNING(S):")
        for w_msg in overflow_warnings:
            print("  -", w_msg)
        return 2

    print(f"\n✓ All {rendered_count} PNG graphics rendered with ZERO layout overflow!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
