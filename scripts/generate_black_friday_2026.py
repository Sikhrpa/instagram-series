#!/usr/bin/env python3
"""
SikhRPA Black Friday / Cyber Monday 2026 — Verified Amazon Price Lows Stories (9:16)
Renders 3 Instagram Story sequences (14 total 1080x1920 frames) highlighting
the 28 verified Nov 2026 Amazon Black Friday price drops & CamelCamelCamel /
editorial all-time lows hosted on:
    https://sikhrpa.org/black-friday-2026

Exports PNG + Instagram-ready sRGB JPEG plus ready-to-paste Story Link Sticker
instructions in caption.txt. No firearms, ammunition, or static dollar prices
(Amazon Operating Agreement) appear anywhere.

Usage:
    python3 scripts/generate_black_friday_2026.py
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from generate_all import audit_policy_guardrails  # noqa: E402
from styles import ROOT_DIR, build_slide_html, get_logo_data_uri  # noqa: E402

OUT_ROOT = ROOT_DIR / "posts" / "black-friday-2026"
DEALS_URL = "https://sikhrpa.org/black-friday-2026"
DISCLOSURE_SLIDE = (
    "Affiliate disclosure: As an Amazon Associate, SikhRPA earns from qualifying purchases "
    "at no extra cost to you. Proceeds fund free 501(c)(3) safety education."
)


def deal_card(name: str, discount: str, sub_badge: str, why: str, tone: str = "") -> str:
    tone_cls = f" card-{tone}" if tone else ""
    badge_bg = (
        "background:#dc2626;border-color:#f87171;color:#fff;"
        if tone == "red"
        else "background:#f59e0b;border-color:#fbbf24;color:#0f172a;"
    )
    return f"""
    <div class="card{tone_cls} stack-sm" style="padding:18px 22px;">
      <div class="row" style="gap:10px;justify-content:space-between;align-items:flex-start;">
        <div>
          <div style="font-size:13px;font-weight:900;letter-spacing:0.08em;color:#fbbf24;text-transform:uppercase;">{sub_badge}</div>
          <div class="h3-title" style="font-size:24px;margin-top:2px;">{name}</div>
        </div>
        <span class="pill" style="font-size:13px;padding:4px 12px;white-space:nowrap;{badge_bg}">{discount}</span>
      </div>
      <p class="body-sm" style="font-size:18px;line-height:1.4;">{why}</p>
    </div>
    """


def grid_deal_card(name: str, discount: str, sub_badge: str, why: str, tone: str = "") -> str:
    tone_cls = f" card-{tone}" if tone else ""
    badge_bg = (
        "background:#dc2626;border-color:#f87171;color:#fff;"
        if tone == "red"
        else "background:#f59e0b;border-color:#fbbf24;color:#0f172a;"
    )
    return f"""
    <div class="card{tone_cls} stack-sm" style="padding:18px 20px;">
      <div class="row" style="gap:8px;justify-content:space-between;align-items:center;">
        <span style="font-size:12px;font-weight:900;letter-spacing:0.06em;color:#fbbf24;text-transform:uppercase;">{sub_badge}</span>
        <span class="pill" style="font-size:12px;padding:3px 10px;white-space:nowrap;{badge_bg}">{discount}</span>
      </div>
      <div class="h3-title" style="font-size:22px;line-height:1.25;">{name}</div>
      <p class="body-sm" style="font-size:17px;line-height:1.38;">{why}</p>
    </div>
    """


def sticker_box(label: str, min_height: int = 190) -> str:
    return f"""
    <div class="sticker-zone" style="width:100%;min-height:{min_height}px;">
      <div style="font-size:18px;font-weight:900;letter-spacing:0.12em;color:#fbbf24;text-transform:uppercase;">
        [ Place Instagram Link Sticker Here ]
      </div>
      <div style="font-size:27px;font-weight:800;color:#fff;">{label}</div>
    </div>
    """


def disclosure_bar() -> str:
    return f"""
    <div style="font-size:15px;line-height:1.45;color:#94a3b8;text-align:center;max-width:900px;margin:0 auto;">
      {DISCLOSURE_SLIDE}
    </div>
    """


def make_story(
    filename: str,
    pill_text: str,
    label: str,
    inner: str,
    *,
    theme: str = "royal",
    footer_right: str = "TAP LINK STICKER ↑",
) -> dict:
    return {
        "filename": filename,
        "width": 1080,
        "height": 1920,
        "theme": theme,
        "frame_variant": "story-frame",
        "pill_text": pill_text,
        "slide_label": label,
        "footer_url": "sikhrpa.org/black-friday-2026",
        "footer_right": footer_right,
        "body_html": inner,
    }


def get_posts() -> list[dict]:
    logo = get_logo_data_uri()

    # =========================================================================
    # BF-1 — Home Security & Smart Lock All-Time Lows (Fri, Nov 27) — 5 Stories
    # =========================================================================
    post_1 = {
        "number": 101,
        "slug": "bf-1-home-security-all-time-lows",
        "date_display": "Fri, Nov 27, 2026 (Black Friday)",
        "time_pst": "8:00 AM PST",
        "format": "Instagram Story Sequence (5 frames, 9:16)",
        "title": "Black Friday Stories: Verified Home Security & Smart Lock Lows",
        "url": f"{DEALS_URL}#security",
        "caption": (
            "(Instagram Stories — '#ad' and Amazon Associates disclosure are printed on every frame.)\n\n"
            "Paste this URL into the Instagram Link Sticker on Frames 2, 3, 4, and 5:\n"
            f"  {DEALS_URL}#security\n"
            "Suggested sticker text: 'Home Security Lows (Up to 74% Off)'"
        ),
        "hashtags": "#ad #SikhRPA #BlackFriday #HomeSecurity #SmartLocks #SafeStorage #SikhCommunity",
        "story_prompt": (
            "Frame 1: No sticker needed. "
            f"Frames 2–5: Place Instagram's native Link Sticker inside the dashed box pointing to {DEALS_URL}#security. "
            "Add to a 'Black Friday' Story Highlight."
        ),
        "links": [
            ("Home Security Deals Anchor", f"{DEALS_URL}#security"),
            ("Full 28-Deal Black Friday Page", DEALS_URL),
        ],
        "slides": [
            make_story(
                "story-01-cover.png",
                "#ad • Verified Lows",
                "1 / 5",
                f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:130px;height:130px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">Verified Amazon Price Lows • 2026</div>
                  <h1 class="h1-hero" style="font-size:68px;">Home Security<br/><span class="gold">Up to 74% Off.</span></h1>
                  <p class="lead" style="font-size:28px;max-width:860px;">
                    No fake list prices. We checked <strong style="color:#fff;">2026 Black Friday price trackers</strong>
                    for genuine all-time lows on cameras, smart locks &amp; trackers.
                  </p>
                  <div class="pa-banner" style="width:100%;text-align:center;">
                    <div class="pa-text-lg">ਘਰੇਲੂ ਸੁਰੱਖਿਆ 'ਤੇ ਅਸਲੀ ਬਲੈਕ ਫ੍ਰਾਈਡੇ ਛੋਟਾਂ</div>
                  </div>
                  <div class="stat-row" style="width:100%;">
                    <div class="stat-box"><div class="stat-val">60% Off</div><div class="stat-lbl">Ring 2K Doorbell</div></div>
                    <div class="stat-box"><div class="stat-val">74% Off</div><div class="stat-lbl">Blink 3-Cam Kit</div></div>
                    <div class="stat-box"><div class="stat-val">40% Off</div><div class="stat-lbl">Ultraloq Lock</div></div>
                  </div>
                  {disclosure_bar()}
                </div>
                """,
                footer_right="TAP THROUGH →",
            ),
            make_story(
                "story-02-cameras.png",
                "#ad • All-Time Lows",
                "2 / 5",
                f"""
                <div class="stack" style="gap:18px;">
                  <div class="eyebrow">Verified Nov 25 • PCMag &amp; CNET</div>
                  <h2 class="h1-lg" style="font-size:52px;">Doorbells &amp; <span class="gold">Cameras</span></h2>
                  {deal_card("Ring Battery Doorbell 2K (2026)", "60% OFF", "Lowest Price Ever",
                             "Wire-free 2K head-to-toe front-door monitoring with 6x zoom & two-way talk.", "red")}
                  {deal_card("Ring Floodlight Cam 2K Wired", "50% OFF", "All-Time Low",
                             "Dual 2,000-lumen motion floodlights + 2K driveway surveillance at half off.", "red")}
                  {deal_card("Arlo Essential Pan-Tilt 2K Indoor", "62% OFF", "Editors' Choice Low",
                             "360° pan / 180° tilt indoor monitoring for entryways or safe rooms.", "blue")}
                  {sticker_box("Check Live Camera Deals →")}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-03-locks-solar.png",
                "#ad • Smart Locks",
                "3 / 5",
                f"""
                <div class="stack" style="gap:18px;">
                  <div class="eyebrow">Verified Nov 25 • Zero-Fee Solar &amp; Locks</div>
                  <h2 class="h1-lg" style="font-size:50px;">Smart Locks &amp; <span class="gold">Solar Kits</span></h2>
                  {deal_card("Ultraloq Bolt Fingerprint Smart Lock", "40% OFF", "Lowest Price Ever",
                             "Built-in Wi-Fi deadbolt — 100 fingerprints, 50 temporary guest PINs, Apple/Alexa/Google.", "red")}
                  {deal_card("eufy SoloCam S340 / eufyCam 3 Kit", "43–45% OFF", "No Monthly Fees",
                             "Solar-charged 3K/4K outdoor cameras with local storage — zero required cloud fees.", "gold")}
                  {deal_card("Blink Outdoor 4 (3-Camera Kit)", "74% OFF", "Deepest Markdown",
                             "Three wire-free outdoor cameras + Sync Module at this week's steepest cut.", "red")}
                  {sticker_box("Check Lock & Solar Deals →")}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-04-track-safe.png",
                "#ad • Gear Tracking",
                "4 / 5",
                f"""
                <div class="stack" style="gap:20px;">
                  <div class="eyebrow">Verified Nov 25 • Travel &amp; Storage</div>
                  <h2 class="h1-lg" style="font-size:52px;">Track Cases &amp; <span class="gold">Lock Up</span></h2>
                  {deal_card("Apple AirTag (2nd Generation)", "38% OFF", "Black Friday Low",
                             "Slip inside locked hard cases, range bags, or luggage for instant Find My tracking.", "gold")}
                  <div class="card card-blue stack-sm" style="padding:20px 24px;">
                    <div class="blue-lt" style="font-size:14px;font-weight:900;letter-spacing:0.08em;">ALSO ON THE PAGE</div>
                    <div class="h3-title" style="font-size:25px;">CA DOJ Safe Storage &amp; Range PPE Guides</div>
                    <p class="body-sm">Direct links to our vetted lockbox, vehicle transport (PC § 25610) &amp; Dastar-friendly ear protection directories.</p>
                  </div>
                  <div class="pa-banner" style="padding:18px 22px;">
                    <div class="pa-text-md">ਸੁਰੱਖਿਅਤ ਘਰ, ਸੁਰੱਖਿਅਤ ਪਰਿਵਾਰ।</div>
                  </div>
                  {sticker_box("See All Home Security Lows →")}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-05-cta.png",
                "#ad • 28 Verified Deals",
                "5 / 5",
                f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;">
                  <img class="brand-logo" style="width:120px;height:120px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="eyebrow">28 Verified Amazon Black Friday Lows</div>
                  <h2 class="h1-lg" style="font-size:52px;">Shop Smarter &amp;<br/><span class="gold">Fund Free Safety Clinics</span></h2>
                  <p class="lead" style="font-size:26px;max-width:860px;">
                    Every qualifying purchase through our deals page supports SikhRPA's free 501(c)(3) workshops &amp; free CA DOJ cable locks.
                  </p>
                  {sticker_box("2026 Verified Black Friday Deals →", min_height=230)}
                  <div class="card card-blue" style="width:100%;padding:18px 24px;">
                    <div class="blue-lt" style="font-size:14px;font-weight:900;">NEED A FREE CA DOJ CABLE LOCK?</div>
                    <p class="body-sm" style="margin-top:4px;color:#f8fafc;">Email <strong>president@sikhrpa.org</strong></p>
                  </div>
                  {disclosure_bar()}
                </div>
                """,
            ),
        ],
    }

    # =========================================================================
    # BF-2 — CamelCamelCamel Flashlights, Tools & Prep Lows (Sat, Nov 28) — 5 Stories
    # =========================================================================
    post_2 = {
        "number": 102,
        "slug": "bf-2-flashlights-tools-prep-lows",
        "date_display": "Sat, Nov 28, 2026",
        "time_pst": "10:00 AM PST",
        "format": "Instagram Story Sequence (5 frames, 9:16)",
        "title": "Black Friday Stories: Verified Flashlight, Multitool & Prep Lows",
        "url": f"{DEALS_URL}#tools",
        "caption": (
            "(Instagram Stories — '#ad' and Amazon Associates disclosure are printed on every frame.)\n\n"
            "Paste these URLs into the Instagram Link Sticker:\n"
            f"  Frames 2, 3, 5 → {DEALS_URL}#tools\n"
            f"  Frame 4        → {DEALS_URL}#preparedness\n"
            "Suggested sticker text: 'Verified Tool & Prep Lows'"
        ),
        "hashtags": "#ad #SikhRPA #BlackFriday #EDC #Flashlights #Multitools #EmergencyPrep #SikhCommunity",
        "story_prompt": (
            "Frame 1: No sticker needed. "
            f"Frames 2, 3, 5: Link Sticker → {DEALS_URL}#tools. "
            f"Frame 4: Link Sticker → {DEALS_URL}#preparedness. "
            "Save to your 'Black Friday' Story Highlight."
        ),
        "links": [
            ("Flashlights & Multitools Anchor", f"{DEALS_URL}#tools"),
            ("Range & Emergency Prep Anchor", f"{DEALS_URL}#preparedness"),
            ("Full 28-Deal Black Friday Page", DEALS_URL),
        ],
        "slides": [
            make_story(
                "story-01-cover.png",
                "#ad • Price-Tracked",
                "1 / 5",
                f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:130px;height:130px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">CamelCamelCamel-Checked Lows</div>
                  <h1 class="h1-hero" style="font-size:66px;">Flashlights, Tools<br/><span class="gold">&amp; Emergency Prep.</span></h1>
                  <p class="lead" style="font-size:28px;max-width:860px;">
                    Real Black Friday price drops on Streamlight, Olight, Leatherman, HOTO, DEWALT &amp; emergency power — verified this week.
                  </p>
                  <div class="pa-banner" style="width:100%;text-align:center;">
                    <div class="pa-text-lg">ਫਲੈਸ਼ਲਾਈਟਾਂ, ਟੂਲਸ ਅਤੇ ਐਮਰਜੈਂਸੀ ਤਿਆਰੀ</div>
                  </div>
                  <div class="stat-row" style="width:100%;">
                    <div class="stat-box"><div class="stat-val">62% Off</div><div class="stat-lbl">Streamlight USB</div></div>
                    <div class="stat-box"><div class="stat-val">43% Off</div><div class="stat-lbl">HOTO Driver Kit</div></div>
                    <div class="stat-box"><div class="stat-val">50% Off</div><div class="stat-lbl">GOOLOO 4000A</div></div>
                  </div>
                  {disclosure_bar()}
                </div>
                """,
                footer_right="TAP THROUGH →",
            ),
            make_story(
                "story-02-flashlights.png",
                "#ad • Flashlights",
                "2 / 5",
                f"""
                <div class="stack" style="gap:18px;">
                  <div class="eyebrow">Verified via CamelCamelCamel &amp; Outdoor Life</div>
                  <h2 class="h1-lg" style="font-size:52px;">EDC <span class="gold">Flashlights</span></h2>
                  {deal_card("Streamlight 66608 MicroStream USB", "62% OFF", "Near All-Time Low",
                             "250-lumen aluminum pocket light (22,700+ reviews, 4.7★). Verify 'Sold by Amazon' at checkout.", "red")}
                  {deal_card("Olight Imini 2 Keychain Light", "40% OFF", "Lowest Price Seen",
                             "Magnetic quick-release USB light — unlock safes and range bags in the dark.", "red")}
                  {deal_card("Olight Baton Ultra &amp; ArkPro Line", "UP TO 35% OFF", "Black Friday Sale",
                             "Official Olight Amazon storefront Black Friday cuts on EDC & clip lights.", "gold")}
                  {sticker_box("Check Flashlight Lows →")}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-03-tools.png",
                "#ad • Bench & EDC Tools",
                "3 / 5",
                f"""
                <div class="stack" style="gap:16px;">
                  <div class="eyebrow">Verified via CamelCamelCamel &amp; Bob Vila</div>
                  <h2 class="h1-lg" style="font-size:50px;">Bench, Safe &amp; <span class="gold">Multitools</span></h2>
                  <div class="grid-2" style="gap:14px;">
                    {grid_deal_card("HOTO 25-Pc Electric Driver", "43% OFF", "Near Record Low",
                                    "Torx, hex & Phillips S2 bits in an aluminum case — great for optics & bench.", "red")}
                    {grid_deal_card("DEWALT 20V Drill &amp; Impact", "46% OFF", "Black Friday Cut",
                                    "Bolt steel gun safes firmly into floor joists or wall studs.", "red")}
                    {grid_deal_card("Leatherman Wave+ / Skeletool", "20% OFF", "Rare Markdown",
                                    "Outside-access blades & replaceable wire cutters — range-bag staple.", "gold")}
                    {grid_deal_card("Roxon Spark 14-in-1", "20% OFF", "Lowest Ever",
                                    "Budget multitool w/ fire starter & whistle (CamelCamelCamel low).", "red")}
                  </div>
                  {sticker_box("Check Verified Tool Deals →")}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-04-preparedness.png",
                "#ad • Range & Prep",
                "4 / 5",
                f"""
                <div class="stack" style="gap:16px;">
                  <div class="eyebrow">Verified Nov 24–25 • Car, Range &amp; Outages</div>
                  <h2 class="h1-lg" style="font-size:50px;">Range &amp; <span class="gold">Emergency Prep</span></h2>
                  <div class="grid-2" style="gap:14px;">
                    {grid_deal_card("GOOLOO A5 4000A Jump Starter", "50% OFF", "Trunk Essential",
                                    "Jump starter + tire inflator + 20,000mAh power bank in one.", "red")}
                    {grid_deal_card("Energizer 48-Pack AA/AAA", "44% OFF", "Stock-Up Low",
                                    "Fresh batteries for electronic ear pro, lockboxes & radios.", "red")}
                    {grid_deal_card("Magpul Patrol Glove 2.0", "36% OFF", "Black Friday",
                                    "Goatskin palm & touchscreen thumbs for outdoor range days.", "gold")}
                    {grid_deal_card("Anker SOLIX / EcoFlow", "UP TO 50% OFF", "Backup Power",
                                    "Silent portable power stations for CA outages & travel.", "red")}
                  </div>
                  {sticker_box("Check Preparedness Deals →")}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-05-cta.png",
                "#ad • Full List",
                "5 / 5",
                f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;">
                  <img class="brand-logo" style="width:120px;height:120px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="eyebrow">Verified Black Friday Price Lows</div>
                  <h2 class="h1-lg" style="font-size:52px;">Tap Before Flash<br/><span class="gold">Quantities Sell Out</span></h2>
                  <p class="lead" style="font-size:26px;max-width:860px;">
                    Amazon Black Friday flash quantities move quickly — check live prices through our unlisted deals page and support free 501(c)(3) education.
                  </p>
                  {sticker_box("Browse All 28 Verified Deals →", min_height=230)}
                  <div class="pa-text-md">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                  {disclosure_bar()}
                </div>
                """,
            ),
        ],
    }

    # =========================================================================
    # BF-3 — Cyber Monday Last Call & Bonus All-Time Lows (Mon, Nov 30) — 4 Stories
    # =========================================================================
    post_3 = {
        "number": 103,
        "slug": "bf-3-cyber-monday-all-time-lows",
        "date_display": "Mon, Nov 30, 2026 (Cyber Monday)",
        "time_pst": "9:00 AM PST (stagger frames through the day)",
        "format": "Instagram Story Sequence (4 frames, 9:16)",
        "title": "Cyber Monday Stories: Last Call & Bonus All-Time Lows",
        "url": f"{DEALS_URL}#bonus",
        "caption": (
            "(Instagram Stories — '#ad' and Amazon Associates disclosure are printed on every frame.)\n\n"
            "Paste these URLs into the Instagram Link Sticker:\n"
            f"  Frame 2 → {DEALS_URL}#preparedness\n"
            f"  Frame 3 → {DEALS_URL}#bonus\n"
            f"  Frame 4 → {DEALS_URL}\n"
            "Suggested sticker text: 'Cyber Monday All-Time Lows'"
        ),
        "hashtags": "#ad #SikhRPA #CyberMonday #AmazonDeals #AllTimeLow #EmergencyPrep #SikhCommunity",
        "story_prompt": (
            "Frame 1: No sticker needed (optional Countdown sticker to midnight). "
            f"Frame 2: Link Sticker → {DEALS_URL}#preparedness. "
            f"Frame 3: Link Sticker → {DEALS_URL}#bonus. "
            f"Frame 4: Link Sticker → {DEALS_URL}."
        ),
        "links": [
            ("Bonus All-Time Lows Anchor", f"{DEALS_URL}#bonus"),
            ("Range & Emergency Prep Anchor", f"{DEALS_URL}#preparedness"),
            ("Full 28-Deal Black Friday Page", DEALS_URL),
        ],
        "slides": [
            make_story(
                "story-01-cover.png",
                "#ad • Cyber Monday",
                "1 / 4",
                f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:130px;height:130px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">Cyber Monday • Final Hours</div>
                  <h1 class="h1-hero" style="font-size:68px;">Last Call:<br/><span class="gold">All-Time Lows.</span></h1>
                  <p class="lead" style="font-size:28px;max-width:860px;">
                    Emergency prep essentials + the biggest verified holiday tech lows on Amazon — tap through before midnight.
                  </p>
                  <div class="pa-banner" style="width:100%;text-align:center;">
                    <div class="pa-text-lg">ਸਾਈਬਰ ਮੰਡੇ — ਆਖ਼ਰੀ ਮੌਕਾ</div>
                  </div>
                  {disclosure_bar()}
                </div>
                """,
                footer_right="TAP THROUGH →",
            ),
            make_story(
                "story-02-prep-comms.png",
                "#ad • Comms & Prep",
                "2 / 4",
                f"""
                <div class="stack" style="gap:16px;">
                  <div class="eyebrow">Verified Nov 25 • Range &amp; Readiness</div>
                  <h2 class="h1-lg" style="font-size:50px;">Comms, Power &amp; <span class="gold">Readiness</span></h2>
                  <div class="grid-2" style="gap:14px;">
                    {grid_deal_card("UGREEN Nexode 145W Bank", "BF LOW", "Record Discount",
                                    "25,000mAh fast charger for laptops, phones & gear off-grid.", "red")}
                    {grid_deal_card("Midland T51VP3 Radios", "BF DEAL", "NOAA Weather",
                                    "License-free 2-way radios + weather alerts for remote ranges.", "gold")}
                    {grid_deal_card("Kershaw Bel Air MagnaCut", "BEST PRICE", "Lowest Online",
                                    "USA-made MagnaCut steel EDC folder — cheapest on Amazon.", "gold")}
                    {grid_deal_card("300-Pc Everyday First Aid", "21% OFF", "Cuts & Scrapes",
                                    "Booboo kit for home/car. (Buy CAT tourniquets direct from NAR!)", "emerald")}
                  </div>
                  {sticker_box("Check Readiness Deals →")}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-03-bonus-tech.png",
                "#ad • Bonus Lows",
                "3 / 4",
                f"""
                <div class="stack" style="gap:16px;">
                  <div class="eyebrow">Verified Nov 25 • Holiday Gift All-Time Lows</div>
                  <h2 class="h1-lg" style="font-size:50px;">Bonus <span class="gold">All-Time Lows</span></h2>
                  <div class="grid-2" style="gap:14px;">
                    {grid_deal_card("Apple AirPods Pro 3", "40%+ OFF", "All-Time Low",
                                    "Lowest Amazon price ever. (Everyday listening — not range ear pro.)", "red")}
                    {grid_deal_card("Sony WH-1000XM6", "24% OFF", "Record Low",
                                    "Flagship ANC travel headphones at their lowest recorded price.", "red")}
                    {grid_deal_card("Amazon Kindle Paperwhite", "35% OFF", "2026 Low",
                                    "Waterproof e-reader at its lowest price of the year.", "gold")}
                    {grid_deal_card("YETI Roadie 15 &amp; Cups", "UP TO 40% OFF", "Black Friday",
                                    "Rare Amazon markdowns on YETI coolers for hot CA range days.", "gold")}
                  </div>
                  {sticker_box("Check Bonus All-Time Lows →")}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-04-cta.png",
                "#ad • Support SikhRPA",
                "4 / 4",
                f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:26px;">
                  <img class="brand-logo" style="width:125px;height:125px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="eyebrow">No Extra Cost to You</div>
                  <h2 class="h1-lg" style="font-size:52px;">Click Before You Shop<br/><span class="gold">Cyber Monday on Amazon</span></h2>
                  <p class="lead" style="font-size:26px;max-width:860px;">
                    Qualifying purchases made after tapping our deals page help fund free bilingual safety education &amp; free CA DOJ cable locks across California.
                  </p>
                  {sticker_box("Open 2026 Black Friday Deals →", min_height=230)}
                  <div class="pa-text-md">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                  {disclosure_bar()}
                </div>
                """,
            ),
        ],
    }

    return [post_1, post_2, post_3]


def write_caption(post: dict, out_dir: Path) -> None:
    media = ", ".join(s["filename"] for s in post["slides"])
    links = "\n".join(f"• {label}: {url}" for label, url in post["links"])
    content = (
        "========================================================================\n"
        f"{post['title']}\n"
        f"Schedule: {post['date_display']} • {post['time_pst']}\n"
        f"Format:   {post['format']}\n"
        f"Link:     {post['url']}\n"
        f"Media:    {media}\n"
        "========================================================================\n\n"
        "--- STORY LINK STICKER SETUP ---\n\n"
        f"{post['caption']}\n\n"
        "--- STORY POSTING INSTRUCTIONS ---\n\n"
        f"{post['story_prompt']}\n\n"
        "--- OPTIONAL HASHTAGS ---\n\n"
        f"{post['hashtags']}\n\n"
        "--- UNLISTED DEALS PAGE URLS (Amazon tag: sikhrpa01-20 built in) ---\n\n"
        f"{links}\n\n"
        "--- BEFORE POSTING ---\n"
        "• Open https://sikhrpa.org/black-friday-2026 and spot-check live prices on Amazon.\n"
        "• Place Instagram's native Link Sticker inside the dashed box on each Story frame.\n"
        "• Do not add static dollar prices for Amazon items (Amazon Operating Agreement).\n"
    )
    (out_dir / "caption.txt").write_text(content, encoding="utf-8")


def main() -> int:
    posts = get_posts()

    issues = audit_policy_guardrails(posts)
    if issues:
        print("POLICY GUARDRAIL FAILURES:")
        for i in issues:
            print("  -", i)
        return 1
    print("✓ Meta policy guardrail audit passed.")

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    kwargs: dict = {"args": ["--no-sandbox", "--disable-gpu", "--font-render-hinting=none"]}
    if chrome:
        kwargs["executable_path"] = chrome

    warnings: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(**kwargs)
        page = browser.new_context(device_scale_factor=1).new_page()
        for post in posts:
            out_dir = OUT_ROOT / post["slug"]
            (out_dir / "jpg").mkdir(parents=True, exist_ok=True)
            write_caption(post, out_dir)
            for s in post["slides"]:
                w, h = s["width"], s["height"]
                page.set_viewport_size({"width": w, "height": h})
                page.set_content(
                    build_slide_html(
                        body_html=s["body_html"],
                        width=w,
                        height=h,
                        pill_text=s["pill_text"],
                        slide_label=s["slide_label"],
                        footer_url=s["footer_url"],
                        footer_right=s["footer_right"],
                        theme=s["theme"],
                        frame_variant=s["frame_variant"],
                    ),
                    wait_until="load",
                )
                page.evaluate("() => document.fonts.ready")
                m = page.evaluate(
                    """() => { const c=document.querySelector('.canvas'), b=document.querySelector('.slide-body');
                       return {c:c.scrollHeight-c.clientHeight, b:b.scrollHeight-b.clientHeight}; }"""
                )
                if m["c"] > 2 or m["b"] > 2:
                    warnings.append(f"{post['slug']}/{s['filename']}: overflow canvas={m['c']} body={m['b']}")
                png = out_dir / s["filename"]
                page.screenshot(path=str(png), type="png")
                Image.open(png).convert("RGB").save(out_dir / "jpg" / png.with_suffix(".jpg").name, quality=95)
                print(f"  Rendered {post['slug']}/{s['filename']} ({w}x{h})")
        browser.close()

    if warnings:
        print("\n⚠ OVERFLOW WARNINGS:")
        for w_ in warnings:
            print("  -", w_)
        return 2
    print("\n✓ All 14 verified Black Friday Story graphics rendered with zero overflow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
