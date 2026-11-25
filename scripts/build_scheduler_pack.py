#!/usr/bin/env python3
"""
Build the Meta Business Suite Scheduling Workbench (scheduler.html) and
step-by-step checklist (META_BUSINESS_SUITE_GUIDE.md) covering:
  - Black Friday / Cyber Monday 2026 Story Sequences (Nov 27, 28, 30)
  - Dec 2026 Launch Series (Posts 01-12 from schedule.csv)
  - 2027 Weekly Series (52 weeks from schedule-2027.csv)

Usage:
    python3 scripts/build_scheduler_pack.py
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

BF_STORIES = [
    {
        "id": "bf-1",
        "badge": "BF 01",
        "tab": "bf",
        "date": "Fri, Nov 27, 2026 (Black Friday)",
        "time": "8:00 AM PST",
        "format": "Instagram Story Sequence (5 frames, 9:16)",
        "title": "Verified Home Security & Smart Lock All-Time Lows (Up to 74% Off)",
        "folder": "posts/black-friday-2026/bf-1-home-security-all-time-lows/jpg",
        "files": [
            {"path": "posts/black-friday-2026/bf-1-home-security-all-time-lows/jpg/story-01-cover.jpg", "label": "Frame 1 (Cover — no sticker needed)"},
            {"path": "posts/black-friday-2026/bf-1-home-security-all-time-lows/jpg/story-02-cameras.jpg", "label": "Frame 2 (Ring & Arlo Cameras)", "sticker_url": "https://sikhrpa.org/black-friday-2026#security", "sticker_text": "Check Camera Lows"},
            {"path": "posts/black-friday-2026/bf-1-home-security-all-time-lows/jpg/story-03-locks-solar.jpg", "label": "Frame 3 (Ultraloq, eufy & Blink)", "sticker_url": "https://sikhrpa.org/black-friday-2026#security", "sticker_text": "Lock & Solar Deals"},
            {"path": "posts/black-friday-2026/bf-1-home-security-all-time-lows/jpg/story-04-track-safe.jpg", "label": "Frame 4 (AirTag Gen 2 + Safe Guides)", "sticker_url": "https://sikhrpa.org/black-friday-2026#security", "sticker_text": "Home Security Lows"},
            {"path": "posts/black-friday-2026/bf-1-home-security-all-time-lows/jpg/story-05-cta.jpg", "label": "Frame 5 (Full List CTA)", "sticker_url": "https://sikhrpa.org/black-friday-2026#security", "sticker_text": "All 28 Verified Deals"},
        ],
        "sticker_url": "https://sikhrpa.org/black-friday-2026#security",
        "sticker_text": "Home Security Lows (Up to 74% Off)",
        "caption": "",
        "notes": "In Meta Business Suite → Create Story → upload Frames 1–5 in order → add the Link Sticker inside the dashed box on Frames 2–5 pointing to https://sikhrpa.org/black-friday-2026#security. Save to a 'Black Friday' Highlight once live.",
    },
    {
        "id": "bf-2",
        "badge": "BF 02",
        "tab": "bf",
        "date": "Sat, Nov 28, 2026",
        "time": "10:00 AM PST",
        "format": "Instagram Story Sequence (5 frames, 9:16)",
        "title": "CamelCamelCamel-Checked Flashlights, Tools & Prep Lows",
        "folder": "posts/black-friday-2026/bf-2-flashlights-tools-prep-lows/jpg",
        "files": [
            {"path": "posts/black-friday-2026/bf-2-flashlights-tools-prep-lows/jpg/story-01-cover.jpg", "label": "Frame 1 (Cover — no sticker needed)"},
            {"path": "posts/black-friday-2026/bf-2-flashlights-tools-prep-lows/jpg/story-02-flashlights.jpg", "label": "Frame 2 (Streamlight & Olight)", "sticker_url": "https://sikhrpa.org/black-friday-2026#tools", "sticker_text": "Flashlight Lows"},
            {"path": "posts/black-friday-2026/bf-2-flashlights-tools-prep-lows/jpg/story-03-tools.jpg", "label": "Frame 3 (HOTO, DEWALT, Leatherman)", "sticker_url": "https://sikhrpa.org/black-friday-2026#tools", "sticker_text": "Verified Tool Deals"},
            {"path": "posts/black-friday-2026/bf-2-flashlights-tools-prep-lows/jpg/story-04-preparedness.jpg", "label": "Frame 4 (GOOLOO, Energizer, Magpul, Power)", "sticker_url": "https://sikhrpa.org/black-friday-2026#preparedness", "sticker_text": "Prep & Range Deals"},
            {"path": "posts/black-friday-2026/bf-2-flashlights-tools-prep-lows/jpg/story-05-cta.jpg", "label": "Frame 5 (Full List CTA)", "sticker_url": "https://sikhrpa.org/black-friday-2026#tools", "sticker_text": "All 28 Verified Deals"},
        ],
        "sticker_url": "https://sikhrpa.org/black-friday-2026#tools",
        "sticker_text": "Verified Tool & Prep Lows",
        "caption": "",
        "notes": "Frames 2, 3, 5 link to #tools; Frame 4 links to #preparedness. Schedule all 5 frames together for Sat Nov 28 at 10:00 AM PST in Meta Business Suite.",
    },
    {
        "id": "bf-3",
        "badge": "BF 03",
        "tab": "bf",
        "date": "Mon, Nov 30, 2026 (Cyber Monday)",
        "time": "9:00 AM PST",
        "format": "Instagram Story Sequence (4 frames, 9:16)",
        "title": "Cyber Monday Last Call & Bonus All-Time Lows",
        "folder": "posts/black-friday-2026/bf-3-cyber-monday-all-time-lows/jpg",
        "files": [
            {"path": "posts/black-friday-2026/bf-3-cyber-monday-all-time-lows/jpg/story-01-cover.jpg", "label": "Frame 1 (Cover — optional Countdown sticker)"},
            {"path": "posts/black-friday-2026/bf-3-cyber-monday-all-time-lows/jpg/story-02-prep-comms.jpg", "label": "Frame 2 (UGREEN, Midland, Kershaw, First Aid)", "sticker_url": "https://sikhrpa.org/black-friday-2026#preparedness", "sticker_text": "Readiness Deals"},
            {"path": "posts/black-friday-2026/bf-3-cyber-monday-all-time-lows/jpg/story-03-bonus-tech.jpg", "label": "Frame 3 (AirPods Pro 3, Sony, Kindle, YETI)", "sticker_url": "https://sikhrpa.org/black-friday-2026#bonus", "sticker_text": "Bonus All-Time Lows"},
            {"path": "posts/black-friday-2026/bf-3-cyber-monday-all-time-lows/jpg/story-04-cta.jpg", "label": "Frame 4 (Support SikhRPA CTA)", "sticker_url": "https://sikhrpa.org/black-friday-2026", "sticker_text": "2026 Black Friday Deals"},
        ],
        "sticker_url": "https://sikhrpa.org/black-friday-2026#bonus",
        "sticker_text": "Cyber Monday All-Time Lows",
        "caption": "",
        "notes": "Frame 2 links to #preparedness, Frame 3 links to #bonus, Frame 4 links to the main page https://sikhrpa.org/black-friday-2026.",
    },
]


def load_dec_posts() -> list[dict]:
    items = []
    with (ROOT_DIR / "schedule.csv").open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            num = row["Post Number"].strip()
            slug = Path(row["Post Folder"]).name
            api_type = row["Graph API Type"].strip().upper()
            files = []
            if api_type == "REEL":
                mp4 = f"media/reels/{slug}.mp4"
                files.append({"path": mp4, "label": "Compiled MP4 Reel (upload this file!)"})
                cover = f"media/jpg/{slug}/reel-00-cover.jpg"
                if (ROOT_DIR / cover).exists():
                    files.append({"path": cover, "label": "Reel Cover Image (optional)"})
            else:
                for p in [x.strip() for x in row["Media Files"].split(";") if x.strip()]:
                    # Prefer sRGB JPEG if available in media/jpg
                    rel_jpg = f"media/jpg/{slug}/{Path(p).stem}.jpg"
                    chosen = rel_jpg if (ROOT_DIR / rel_jpg).exists() else p
                    files.append({"path": chosen, "label": Path(chosen).name})

            items.append({
                "id": f"dec-{num}",
                "badge": f"Post {num}",
                "tab": "dec",
                "date": row["Scheduled Date"].strip(),
                "time": row["Scheduled Time (PST)"].strip(),
                "format": row["Format"].strip(),
                "title": row["Title"].strip(),
                "folder": row["Post Folder"].strip(),
                "files": files,
                "sticker_url": row["Link in Bio URL"].strip(),
                "sticker_text": "",
                "caption": row["Caption + Hashtags"].strip(),
                "notes": row["Story Prompt"].strip(),
            })
    return items


def load_2027_posts() -> list[dict]:
    items = []
    with (ROOT_DIR / "schedule-2027.csv").open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            wk = row["Week"].strip()
            num = wk.replace("Week ", "").strip()
            holiday = row["Major Sikh Holiday"].strip()
            title = row["Title"].strip()
            if holiday and holiday.lower() != "no":
                title = f"{title} ({holiday})"
            items.append({
                "id": f"w2027-{num}",
                "badge": f"W{num}",
                "tab": "y2027",
                "date": row["Date"].strip(),
                "time": row["Time"].strip(),
                "format": f"4:5 Feed Post + 9:16 Story • {row['Quarter'].strip()}",
                "title": title,
                "folder": row["Folder"].strip(),
                "files": [
                    {"path": row["Post PNG"].strip(), "label": "4:5 Feed Post (post.png)"},
                    {"path": row["Story PNG"].strip(), "label": "9:16 Companion Story (story.png)"},
                ],
                "sticker_url": row["Link in Bio URL"].strip(),
                "sticker_text": "",
                "caption": row["Caption + Hashtags"].strip(),
                "notes": row["Story Prompt"].strip(),
            })
    return items


def write_guide_md(dec_posts: list[dict], posts_2027: list[dict]) -> None:
    dec_rows = []
    for p in dec_posts:
        upload_hint = p["files"][0]["path"] if len(p["files"]) == 1 else f"`{p['folder']}/` ({len(p['files'])} files)"
        if "MP4" in p["files"][0]["label"]:
            upload_hint = f"`{p['files'][0]['path']}` (MP4 Reel)"
        dec_rows.append(f"| [ ] | **{p['badge']}** | {p['date']} • {p['time']} | {p['format']} | {p['title']} | {upload_hint} |")

    md = f"""# Meta Business Suite — Scheduling Guide & Master Checklist

**Meta Business Suite** ([business.facebook.com/latest/content_calendar](https://business.facebook.com/latest/content_calendar)) is 100% free, official from Meta, requires zero API tokens, and is the **only** scheduler that lets you attach clickable **Link Stickers** to scheduled Instagram Stories.

> **Interactive Workbench:** Open [`scheduler.html`](scheduler.html) in your browser alongside Meta Business Suite for **one-click Copy Caption**, **one-click Copy Link Sticker URL**, file thumbnails, and auto-saved checkboxes for all **67 scheduled slots** (Black Friday + Dec 2026 + all 52 weeks of 2027).

---

## One-Time Setup (2 Minutes)
1. Ensure `@sikhrpa` is set to a **Professional (Business or Creator)** Instagram account and linked to the SikhRPA Facebook Page.
2. Open [business.facebook.com/latest/content_calendar](https://business.facebook.com/latest/content_calendar) on desktop (Chrome/Safari/Edge).
3. Note Meta's scheduling window: Meta Business Suite lets you schedule Posts, Reels, and Stories up to **29 days in advance**. That means:
   - **Today (Nov 25):** Schedule **Batch 1 (Black Friday Stories)** + **Batch 2 (All 12 Dec 2026 Posts)** in ~15 minutes total!
   - **Once a month in 2027 (~5 min/month):** Schedule the next 4 Tuesday slots from `weekly-2027/`.

---

## Batch 1 — Black Friday & Cyber Monday Stories (Schedule Today • ~5 min)

In Meta Business Suite → click **Create Story** → select **Instagram** → upload the `.jpg` frames in order → click **Link** (or Sticker → Link) inside the dashed box on each frame → click **Schedule**.

| Done | Set | Date & Time (PST) | Files to Upload (in order) | Clickable Link Sticker URL |
|---|---|---|---|---|
| [ ] | **BF 01** | **Fri, Nov 27** • 8:00 AM | `posts/black-friday-2026/bf-1-home-security-all-time-lows/jpg/story-01..05.jpg` | Frames 2–5 → `https://sikhrpa.org/black-friday-2026#security` |
| [ ] | **BF 02** | **Sat, Nov 28** • 10:00 AM | `posts/black-friday-2026/bf-2-flashlights-tools-prep-lows/jpg/story-01..05.jpg` | Frames 2, 3, 5 → `#tools` • Frame 4 → `#preparedness` |
| [ ] | **BF 03** | **Mon, Nov 30** • 9:00 AM | `posts/black-friday-2026/bf-3-cyber-monday-all-time-lows/jpg/story-01..04.jpg` | Frame 2 → `#preparedness` • Frame 3 → `#bonus` • Frame 4 → `https://sikhrpa.org/black-friday-2026` |

*(After the first Story goes live on Friday, tap **Highlight** in Instagram and save all 3 sets into a `"Black Friday"` Story Highlight through Cyber Monday!)*

---

## Batch 2 — Dec 2026 Launch Series (Schedule Today • ~10 min)

In Meta Business Suite → click **Create Post** (for Carousels/Photos) or **Create Reel** (for Posts 03 & 07) → copy the ready-to-paste caption from [`scheduler.html`](scheduler.html) or each post's `caption.txt` → set the PST date & time → click **Schedule**.

| Done | Post | Scheduled Slot (PST) | Format | Topic | Media to Upload |
|---|---|---|---|---|---|
{chr(10).join(dec_rows)}

---

## Batch 3 — 2027 Full-Year Weekly Series (52 Weeks • ~5 min/month)

Because Meta Business Suite schedules up to 29 days ahead, spend 5 minutes on the **last Sunday of each month** scheduling the next 4–5 Tuesdays using the **2027 Weekly Series** tab in [`scheduler.html`](scheduler.html) (or [`schedule-2027.csv`](schedule-2027.csv)):
- Each week has a `post.png` (4:5 Feed Post) and `story.png` (9:16 Companion Story) inside `weekly-2027/week-XX-.../`.
- Every caption is pre-written in `caption.txt` and one-click copyable inside `scheduler.html`.

---

## Optional: Want 100% Hands-Off API Auto-Posting Later?
This repository also includes a GitHub Actions auto-poster ([`AUTO_POST_SETUP.md`](AUTO_POST_SETUP.md)) using the official Meta Instagram Graph API. Adding `IG_USER_ID` and `IG_ACCESS_TOKEN` in GitHub Secrets enables automatic hands-off publishing for Feed Carousels, Reels, and Photo Stories — though **Meta's API does not support clickable Link Stickers on Stories**, so Meta Business Suite remains best for affiliate Stories.
"""
    (ROOT_DIR / "META_BUSINESS_SUITE_GUIDE.md").write_text(md, encoding="utf-8")


def write_scheduler_html(all_items: list[dict]) -> None:
    data_json = json.dumps(all_items, ensure_ascii=False)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>SikhRPA Meta Business Suite Scheduler Workbench</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #0b1120;
    color: #f8fafc;
    line-height: 1.5;
    padding-bottom: 64px;
  }}
  a {{ color: #fbbf24; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .topbar {{
    position: sticky;
    top: 0;
    z-index: 20;
    background: rgba(15, 23, 42, 0.96);
    backdrop-filter: blur(8px);
    border-bottom: 2px solid #d97706;
    padding: 14px 20px;
  }}
  .topbar-inner {{
    max-width: 1180px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
  }}
  .brand {{ display: flex; align-items: center; gap: 12px; }}
  .brand img {{ width: 38px; height: 38px; border-radius: 50%; border: 2px solid #f59e0b; }}
  .brand h1 {{ font-size: 18px; font-weight: 900; letter-spacing: 0.01em; }}
  .brand p {{ font-size: 12px; color: #94a3b8; }}
  .actions {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }}
  .btn {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 9px 14px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 800;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.15s ease;
  }}
  .btn-gold {{ background: #f59e0b; color: #0f172a; }}
  .btn-gold:hover {{ background: #fbbf24; text-decoration: none; }}
  .btn-ghost {{ background: #1e293b; color: #e2e8f0; border-color: #334155; }}
  .btn-ghost:hover {{ background: #334155; text-decoration: none; }}
  .btn-copy {{ background: #1e3a8a; color: #dbeafe; border-color: #3b82f6; padding: 7px 12px; font-size: 12px; }}
  .btn-copy:hover {{ background: #1d4ed8; }}
  .btn-copy.copied {{ background: #059669; border-color: #34d399; color: #fff; }}
  .container {{ max-width: 1180px; margin: 0 auto; padding: 24px 20px; }}
  .progress-card {{
    background: linear-gradient(135deg, #0f172a 0%, #172554 100%);
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 18px 22px;
    margin-bottom: 20px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
  }}
  .bar-wrap {{ flex: 1; min-width: 240px; }}
  .bar-label {{ display: flex; justify-content: space-between; font-size: 13px; font-weight: 700; margin-bottom: 8px; color: #e2e8f0; }}
  .bar-track {{ height: 10px; background: #0b1120; border-radius: 999px; overflow: hidden; border: 1px solid #334155; }}
  .bar-fill {{ height: 100%; background: linear-gradient(90deg, #d97706, #fbbf24); width: 0%; transition: width 0.25s ease; }}
  .tabs {{ display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; }}
  .tab {{
    padding: 10px 16px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 800;
    cursor: pointer;
    background: #1e293b;
    color: #cbd5e1;
    border: 1px solid #334155;
  }}
  .tab.active {{ background: #f59e0b; color: #0f172a; border-color: #fbbf24; }}
  .grid {{ display: grid; gap: 16px; }}
  .card {{
    background: #111827;
    border: 1.5px solid #1f2937;
    border-radius: 16px;
    padding: 20px;
    transition: border-color 0.15s ease;
  }}
  .card.done {{ border-color: #059669; background: rgba(6, 78, 59, 0.14); }}
  .card-head {{
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 14px;
  }}
  .check-label {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    user-select: none;
    background: #1e293b;
    border: 1px solid #334155;
    padding: 7px 12px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: 800;
  }}
  .card.done .check-label {{ background: #065f46; border-color: #34d399; color: #ecfdf5; }}
  .check-label input {{ width: 17px; height: 17px; accent-color: #10b981; cursor: pointer; }}
  .meta-row {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-bottom: 6px; }}
  .pill {{
    display: inline-block;
    padding: 3px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    background: rgba(245, 158, 11, 0.18);
    color: #fbbf24;
    border: 1px solid rgba(245, 158, 11, 0.45);
  }}
  .pill-blue {{ background: rgba(59, 130, 246, 0.16); color: #93c5fd; border-color: rgba(59, 130, 246, 0.4); }}
  .card h2 {{ font-size: 19px; font-weight: 800; color: #fff; }}
  .files-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(175px, 1fr));
    gap: 10px;
    margin: 14px 0;
  }}
  .file-box {{
    background: #0b1120;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .file-box img {{
    width: 100%;
    height: 150px;
    object-fit: contain;
    background: #020617;
    border-radius: 8px;
  }}
  .file-name {{ font-size: 11px; font-weight: 700; color: #cbd5e1; word-break: break-word; }}
  .file-actions {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .mini-link {{
    font-size: 11px;
    font-weight: 800;
    padding: 4px 8px;
    border-radius: 6px;
    background: #1e293b;
    color: #fbbf24;
    border: 1px solid #334155;
    cursor: pointer;
  }}
  .mini-link:hover {{ background: #334155; text-decoration: none; }}
  .note-box {{
    background: #0f172a;
    border-left: 3px solid #f59e0b;
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 13px;
    color: #cbd5e1;
    margin-bottom: 12px;
  }}
  .copy-row {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }}
  details {{ margin-top: 10px; }}
  summary {{ font-size: 12px; font-weight: 700; color: #94a3b8; cursor: pointer; }}
  pre {{
    margin-top: 8px;
    white-space: pre-wrap;
    background: #020617;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 12px;
    font-size: 12px;
    color: #e2e8f0;
    font-family: inherit;
    max-height: 240px;
    overflow-y: auto;
  }}
</style>
</head>
<body>
  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand">
        <img src="assets/srpa-logo.png" alt="SikhRPA" onerror="this.style.display='none'" />
        <div>
          <h1>SikhRPA Meta Business Suite Workbench</h1>
          <p>Click-to-copy captions, Link Sticker URLs, media downloads &amp; auto-saved scheduling checklist</p>
        </div>
      </div>
      <div class="actions">
        <a class="btn btn-gold" href="https://business.facebook.com/latest/content_calendar" target="_blank" rel="noopener noreferrer">
          Open Meta Business Suite Planner ↗
        </a>
        <a class="btn btn-ghost" href="META_BUSINESS_SUITE_GUIDE.md">Read Setup Guide</a>
        <a class="btn btn-ghost" href="index.html">Visual Gallery</a>
      </div>
    </div>
  </header>

  <main class="container">
    <section class="progress-card">
      <div class="bar-wrap">
        <div class="bar-label">
          <span>Overall Scheduling Progress</span>
          <span id="progressText">0 / 0 scheduled</span>
        </div>
        <div class="bar-track"><div id="progressFill" class="bar-fill"></div></div>
      </div>
      <button type="button" class="btn btn-ghost" onclick="resetProgress()">Reset Checkboxes</button>
    </section>

    <div class="tabs" role="tablist">
      <button type="button" class="tab active" data-tab="bf">Black Friday Stories (Nov 27–30)</button>
      <button type="button" class="tab" data-tab="dec">Dec 2026 Launch Series (12 Posts)</button>
      <button type="button" class="tab" data-tab="y2027">2027 Weekly Series (52 Weeks)</button>
    </div>

    <div id="cardsGrid" class="grid"></div>
  </main>

  <script>
    const ITEMS = {data_json};
    const STORAGE_KEY = 'sikhrpa_mbs_scheduled_v1';
    let currentTab = 'bf';

    function getSaved() {{
      try {{ return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{{}}') || {{}}; }}
      catch (e) {{ return {{}}; }}
    }}

    function setSaved(state) {{
      try {{ localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); }} catch (e) {{}}
    }}

    function updateProgress() {{
      const saved = getSaved();
      const doneCount = ITEMS.filter(x => saved[x.id]).length;
      const pct = ITEMS.length ? Math.round((doneCount / ITEMS.length) * 100) : 0;
      document.getElementById('progressText').textContent = doneCount + ' / ' + ITEMS.length + ' scheduled (' + pct + '%)';
      document.getElementById('progressFill').style.width = pct + '%';
    }}

    function copyText(text, btn) {{
      navigator.clipboard.writeText(text).then(() => {{
        const prev = btn.textContent;
        btn.classList.add('copied');
        btn.textContent = '✓ Copied!';
        setTimeout(() => {{
          btn.classList.remove('copied');
          btn.textContent = prev;
        }}, 1600);
      }});
    }}

    function resetProgress() {{
      if (!confirm('Clear all scheduled checkmarks?')) return;
      setSaved({{}});
      render();
    }}

    function render() {{
      const saved = getSaved();
      updateProgress();
      const grid = document.getElementById('cardsGrid');
      grid.innerHTML = '';

      ITEMS.filter(x => x.tab === currentTab).forEach(item => {{
        const isDone = Boolean(saved[item.id]);
        const card = document.createElement('article');
        card.className = 'card' + (isDone ? ' done' : '');

        const filesHtml = item.files.map(f => {{
          const isVideo = f.path.endsWith('.mp4');
          const preview = isVideo
            ? `<div style="height:150px;display:flex;align-items:center;justify-content:center;background:#172554;border-radius:8px;font-weight:900;color:#fbbf24;font-size:14px;">MP4 REEL</div>`
            : `<img src="${{f.path}}" alt="${{f.label}}" loading="lazy" />`;
          const stickerBtn = f.sticker_url
            ? `<button type="button" class="mini-link" data-copy="${{f.sticker_url.replace(/"/g, '&quot;')}}">Copy Link</button>`
            : '';
          return `
            <div class="file-box">
              ${{preview}}
              <div class="file-name">${{f.label}}</div>
              <div class="file-actions">
                <a class="mini-link" href="${{f.path}}" download>Download</a>
                ${{stickerBtn}}
              </div>
            </div>
          `;
        }}).join('');

        const copyButtons = [];
        if (item.caption) {{
          copyButtons.push(`<button type="button" class="btn btn-copy" data-copy-caption="1">Copy Caption + Hashtags</button>`);
        }}
        if (item.sticker_url) {{
          const urlLabel = item.tab === 'bf' ? 'Copy Link Sticker URL' : 'Copy Bio / Story URL';
          copyButtons.push(`<button type="button" class="btn btn-copy" data-copy="${{item.sticker_url.replace(/"/g, '&quot;')}}">${{urlLabel}}</button>`);
        }}
        if (item.sticker_text) {{
          copyButtons.push(`<button type="button" class="btn btn-copy" data-copy="${{item.sticker_text.replace(/"/g, '&quot;')}}">Copy Sticker Text</button>`);
        }}

        const captionDetails = item.caption
          ? `<details><summary>Preview full caption &amp; hashtags</summary><pre></pre></details>`
          : '';

        card.innerHTML = `
          <div class="card-head">
            <div>
              <div class="meta-row">
                <span class="pill">${{item.badge}}</span>
                <span class="pill pill-blue">${{item.date}} • ${{item.time}}</span>
                <span style="font-size:12px;color:#94a3b8;font-weight:700;">${{item.format}}</span>
              </div>
              <h2>${{item.title}}</h2>
            </div>
            <label class="check-label">
              <input type="checkbox" ${{isDone ? 'checked' : ''}} />
              <span>${{isDone ? 'Scheduled ✓' : 'Mark Scheduled'}}</span>
            </label>
          </div>
          ${{item.notes ? `<div class="note-box">${{item.notes}}</div>` : ''}}
          <div class="files-grid">${{filesHtml}}</div>
          <div class="copy-row">${{copyButtons.join('')}}</div>
          ${{captionDetails}}
        `;

        if (item.caption) {{
          card.querySelector('pre').textContent = item.caption;
          const capBtn = card.querySelector('[data-copy-caption]');
          if (capBtn) capBtn.addEventListener('click', () => copyText(item.caption, capBtn));
        }}

        card.querySelectorAll('[data-copy]').forEach(btn => {{
          btn.addEventListener('click', () => copyText(btn.getAttribute('data-copy'), btn));
        }});

        const cb = card.querySelector('input[type="checkbox"]');
        cb.addEventListener('change', () => {{
          const next = getSaved();
          next[item.id] = cb.checked;
          setSaved(next);
          render();
        }});

        grid.appendChild(card);
      }});
    }}

    document.querySelectorAll('.tab').forEach(btn => {{
      btn.addEventListener('click', () => {{
        currentTab = btn.getAttribute('data-tab');
        document.querySelectorAll('.tab').forEach(b => b.classList.toggle('active', b === btn));
        render();
      }});
    }});

    render();
  </script>
</body>
</html>
"""
    (ROOT_DIR / "scheduler.html").write_text(html, encoding="utf-8")


def main() -> int:
    dec_posts = load_dec_posts()
    posts_2027 = load_2027_posts()
    all_items = BF_STORIES + dec_posts + posts_2027
    write_guide_md(dec_posts, posts_2027)
    write_scheduler_html(all_items)
    print(f"✓ Built META_BUSINESS_SUITE_GUIDE.md and scheduler.html ({len(all_items)} scheduled slots).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
