#!/usr/bin/env python3
"""
SikhRPA Black Friday / Cyber Monday 2026 — Instagram Story Series (9:16)
Renders 3 affiliate-eligible Story sequences (14 total 1080x1920 frames) using
the shared SikhRPA brand system (styles.build_slide_html), writes posting
instructions + ready-to-paste Story link URLs in caption.txt, and exports
Instagram-ready sRGB JPEGs.

All Story link stickers point directly to the unlisted deals landing page:
    https://sikhrpa.org/black-friday-2026

Only products already vetted in sikhrpa/data/range-gear.json and
sikhrpa/data/ppe-products.json are featured. No firearms, ammunition, or
static dollar prices (Amazon Operating Agreement) appear anywhere.

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


def product_card(name: str, badge: str, why: str, tone: str = "") -> str:
    tone_cls = f" card-{tone}" if tone else ""
    return f"""
    <div class="card{tone_cls} stack-sm" style="padding:20px 24px;">
      <div class="row" style="gap:12px;justify-content:space-between;">
        <div class="h3-title" style="font-size:26px;">{name}</div>
        <span class="pill" style="font-size:13px;padding:4px 12px;white-space:nowrap;">{badge}</span>
      </div>
      <p class="body-sm">{why}</p>
    </div>
    """


def compact_card(name: str, badge: str, why: str, tone: str = "") -> str:
    tone_cls = f" card-{tone}" if tone else ""
    return f"""
    <div class="card{tone_cls} stack-sm" style="padding:18px 22px;">
      <div class="row" style="gap:10px;justify-content:space-between;">
        <div class="h3-title" style="font-size:23px;">{name}</div>
        <span class="pill" style="font-size:12px;padding:3px 10px;white-space:nowrap;">{badge}</span>
      </div>
      <p class="body-sm" style="font-size:18px;line-height:1.4;">{why}</p>
    </div>
    """


def sticker_box(label: str, min_height: int = 210) -> str:
    return f"""
    <div class="sticker-zone" style="width:100%;min-height:{min_height}px;">
      <div style="font-size:19px;font-weight:900;letter-spacing:0.12em;color:#fbbf24;text-transform:uppercase;">
        [ Place Instagram Link Sticker Here ]
      </div>
      <div style="font-size:28px;font-weight:800;color:#fff;">{label}</div>
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
    # BF-A — Safe Storage Is the Best Gift (Fri, Nov 27) — 5 Story Frames (9:16)
    # =========================================================================
    post_a = {
        "number": 101,
        "slug": "bf-a-safe-storage-best-gift",
        "date_display": "Fri, Nov 27, 2026 (Black Friday)",
        "time_pst": "8:00 AM PST",
        "format": "Instagram Story Sequence (5 frames, 9:16)",
        "title": "Black Friday Stories: Safe Storage Is the Best Gift",
        "url": f"{DEALS_URL}#safe-storage",
        "caption": (
            "(Instagram Stories — '#ad' and Amazon Associates disclosure are built into every frame.)\n\n"
            "Paste this URL into the Instagram Link Sticker on Frames 2, 3, 4, and 5:\n"
            f"  {DEALS_URL}#safe-storage\n"
            "Suggested sticker text: '2026 Safe Storage Deals'"
        ),
        "hashtags": "#ad #SikhRPA #SafeStorage #BlackFriday #HomeSafety #PC25100 #SikhCommunity",
        "story_prompt": (
            "Frame 1: No sticker needed (optional Poll: 'Lockbox or full safe?'). "
            f"Frames 2–5: Place a native Instagram Link Sticker inside the dashed box pointing to {DEALS_URL}#safe-storage. "
            "Save all 5 frames to a 'Black Friday' Story Highlight."
        ),
        "links": [
            ("Primary Story Link Sticker (Section 1)", f"{DEALS_URL}#safe-storage"),
            ("Full 2026 Black Friday Deals Page", DEALS_URL),
        ],
        "slides": [
            make_story(
                "story-01-cover.png",
                "#ad • Black Friday",
                "1 / 5",
                f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:130px;height:130px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">Black Friday Gift Guide • 2026</div>
                  <h1 class="h1-hero" style="font-size:70px;">The Best Gift This Year?<br/><span class="gold">A Lock.</span></h1>
                  <p class="lead" style="font-size:28px;max-width:860px;">
                    Lockboxes, transport cases &amp; storage essentials from SikhRPA's
                    <strong style="color:#fff;">vetted Safe Storage list</strong> — marked down this week.
                  </p>
                  <div class="pa-banner" style="width:100%;text-align:center;">
                    <div class="pa-text-lg">ਸੁਰੱਖਿਅਤ ਸਟੋਰੇਜ — ਪਰਿਵਾਰ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਤੋਹਫ਼ਾ</div>
                  </div>
                  <div class="stat-row" style="width:100%;">
                    <div class="stat-box"><div class="stat-val">Bedside</div><div class="stat-lbl">Quick Access</div></div>
                    <div class="stat-box"><div class="stat-val">Vehicle</div><div class="stat-lbl">PC § 25610</div></div>
                    <div class="stat-box"><div class="stat-val">Inside</div><div class="stat-lbl">The Safe</div></div>
                  </div>
                  {disclosure_bar()}
                </div>
                """,
                footer_right="TAP THROUGH →",
            ),
            make_story(
                "story-02-bedside.png",
                "#ad • Bedside",
                "2 / 5",
                f"""
                <div class="stack" style="gap:22px;">
                  <div class="eyebrow">Pick #1 • ਬਿਸਤਰੇ ਕੋਲ ਤਾਲਾਬੰਦ ਬਕਸਾ</div>
                  <h2 class="h1-lg" style="font-size:56px;">Bedside <span class="gold">Quick-Access</span></h2>
                  <p class="body-text">Fast for you. Locked for curious kids and visiting guests (CA PC § 25100).</p>
                  {product_card("Hornady RAPiD® Safe 2700KP XL", "14-Gauge Steel",
                                "RFID tag + backlit keypad + key backup. Exceeds ASTM child- and pry-resistance standards.", "blue")}
                  {product_card("Vaultek LifePod 2.0", "IP65 Sealed",
                                "Weather-sealed lockbox with keypad, key backup, and steel tether cable — bedside or travel.", "gold")}
                  <div class="card card-emerald" style="padding:18px 22px;">
                    <p class="body-sm" style="color:#f8fafc;"><strong>Tip:</strong> Never use birthdays as codes, and never leave backup keys on a dresser.</p>
                  </div>
                  {sticker_box("Check Bedside Deals →")}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-03-budget-vehicle.png",
                "#ad • Vehicle",
                "3 / 5",
                f"""
                <div class="stack" style="gap:20px;">
                  <div class="eyebrow">Pick #2 • ਗੱਡੀ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਆਵਾਜਾਈ</div>
                  <h2 class="h1-lg" style="font-size:54px;">Budget &amp; <span class="gold">Vehicle Transport</span></h2>
                  <p class="body-text">California requires handguns in a vehicle to be in a <strong style="color:#fff;">locked container</strong> or trunk (PC § 25610).</p>
                  {compact_card("SnapSafe Steel Lock Box XL", "Budget Pick",
                                "16-gauge steel with 1,500 lb tether cable. Choose steel & confirm your SKU on the CA DOJ roster.", "blue")}
                  {compact_card("Pelican Vault V300", "Crushproof",
                                "Weather-sealed hard case with stainless padlock hasps for range days & airline check-in.", "gold")}
                  {compact_card("Savior Equipment Range Bags", "Lockable Zips",
                                "Specialist 3-pistol bag & American Classic double rifle case with lockable zipper pulls.")}
                  {sticker_box("Check Vehicle & Case Deals →", min_height=190)}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-04-inside-the-safe.png",
                "#ad • In-Safe",
                "4 / 5",
                f"""
                <div class="stack" style="gap:20px;">
                  <div class="eyebrow">Pick #3 • Budget-Friendly Add-Ons</div>
                  <h2 class="h1-lg" style="font-size:54px;">Finish the Job <span class="gold">Inside the Safe</span></h2>
                  {compact_card("Eva-Dry E-333 Dehumidifier", "Cordless",
                                "Pulls moisture out of safes (up to 333 cu. ft.) to prevent rust in California humidity.", "blue")}
                  {compact_card("MTM AC50C Lockable Can", "Padlock Tabs",
                                "O-ring sealed ammo can with dual padlock tabs — store ammunition locked separately.", "gold")}
                  {compact_card("Master Lock 120Q (4-Pack)", "Keyed Alike",
                                "Slim brass padlocks for case hasps and soft-bag zippers — one key opens all four.")}
                  <div class="pa-banner" style="padding:18px 22px;">
                    <div class="pa-text-md">ਹਥਿਆਰ ਅਤੇ ਗੋਲੀ-ਸਿੱਕਾ ਹਮੇਸ਼ਾ ਵੱਖ-ਵੱਖ ਤਾਲੇ ਹੇਠ ਰੱਖੋ।</div>
                    <div class="body-sm" style="margin-top:4px;">Always lock firearms and ammunition separately.</div>
                  </div>
                  {sticker_box("Check In-Safe Deals →", min_height=180)}
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
                  <div class="eyebrow">All 25 Vetted Black Friday Picks</div>
                  <h2 class="h1-lg" style="font-size:54px;">Every Qualifying Purchase<br/><span class="gold">Funds Free Safety Clinics</span></h2>
                  <p class="lead" style="font-size:26px;max-width:860px;">
                    Tap below for our full 2026 Black Friday safety gear roundup. Prices move fast — confirm live pricing on Amazon before buying.
                  </p>
                  {sticker_box("2026 Black Friday Safety Picks →", min_height=240)}
                  <div class="card card-blue" style="width:100%;padding:20px 24px;">
                    <div class="blue-lt" style="font-size:15px;font-weight:900;">NEED A FREE CA DOJ CABLE LOCK?</div>
                    <p class="body-sm" style="margin-top:6px;color:#f8fafc;">Email <strong>president@sikhrpa.org</strong> — distributed free at every SikhRPA workshop.</p>
                  </div>
                  <div class="pa-text-md">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                  {disclosure_bar()}
                </div>
                """,
            ),
        ],
    }

    # =========================================================================
    # BF-B — Dastar & Patka-Friendly Range PPE (Sat, Nov 28) — 5 Story Frames (9:16)
    # =========================================================================
    post_b = {
        "number": 102,
        "slug": "bf-b-dastar-friendly-range-ppe",
        "date_display": "Sat, Nov 28, 2026",
        "time_pst": "10:00 AM PST",
        "format": "Instagram Story Sequence (5 frames, 9:16)",
        "title": "Black Friday Stories: Dastar & Patka-Friendly Ear and Eye Protection",
        "url": f"{DEALS_URL}#range-ppe",
        "caption": (
            "(Instagram Stories — '#ad' and Amazon Associates disclosure are built into every frame.)\n\n"
            "Paste this URL into the Instagram Link Sticker on Frames 2, 3, 4, and 5:\n"
            f"  {DEALS_URL}#range-ppe\n"
            "Suggested sticker text: 'Dastar-Friendly PPE Deals'"
        ),
        "hashtags": "#ad #SikhRPA #HearingProtection #EyeProtection #Dastar #Patka #BlackFriday #SikhCommunity",
        "story_prompt": (
            "Frame 1: No sticker needed (optional Poll: 'Earbuds or neckband muffs?'). "
            f"Frames 2–5: Place a native Instagram Link Sticker inside the dashed box pointing to {DEALS_URL}#range-ppe. "
            "Save to your 'Black Friday' Story Highlight."
        ),
        "links": [
            ("Primary Story Link Sticker (Section 2)", f"{DEALS_URL}#range-ppe"),
            ("Full 2026 Black Friday Deals Page", DEALS_URL),
        ],
        "slides": [
            make_story(
                "story-01-cover.png",
                "#ad • Black Friday",
                "1 / 5",
                f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:130px;height:130px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">Dastar &amp; Patka-Friendly PPE</div>
                  <h1 class="h1-hero" style="font-size:68px;">Muffs Don't Seal<br/><span class="gold">Over a Dastar.</span></h1>
                  <p class="lead" style="font-size:28px;max-width:860px;">
                    A broken seal means permanent hearing damage. These vetted ear &amp; eye picks fit
                    <strong style="color:#fff;">with</strong> Sikh headwear — check Black Friday pricing inside.
                  </p>
                  <div class="pa-banner" style="width:100%;text-align:center;">
                    <div class="pa-text-lg">ਦਸਤਾਰ ਅਤੇ ਪਟਕੇ ਨਾਲ ਕੰਨਾਂ ਅਤੇ ਅੱਖਾਂ ਦੀ ਸੁਰੱਖਿਆ</div>
                  </div>
                  <div class="stat-row" style="width:100%;">
                    <div class="stat-box"><div class="stat-val">In-Ear</div><div class="stat-lbl">Zero Contact</div></div>
                    <div class="stat-box"><div class="stat-val">Neckband</div><div class="stat-lbl">Behind Head</div></div>
                    <div class="stat-box"><div class="stat-val">Z87.1+</div><div class="stat-lbl">Thin Temples</div></div>
                  </div>
                  {disclosure_bar()}
                </div>
                """,
                footer_right="TAP THROUGH →",
            ),
            make_story(
                "story-02-electronic-earbuds.png",
                "#ad • Electronic",
                "2 / 5",
                f"""
                <div class="stack" style="gap:18px;">
                  <div class="eyebrow">Pick #1 • Hear Commands, Block Gunshots</div>
                  <h2 class="h1-lg" style="font-size:54px;">Electronic <span class="gold">Earbuds</span></h2>
                  <div class="grid-2" style="gap:14px;">
                    {compact_card("ISOtunes ADVANCE BT", "NRR 26",
                                  "Tactical Sound Control, IP67, neck tether so you never drop a bud.", "blue")}
                    {compact_card("ISOtunes CALIBER BT", "NRR 25",
                                  "True wireless with pocket charging case. Zero bulk under a Dastar.", "gold")}
                    {compact_card("Walker's Disrupter", "NRR 24",
                                  "360° mics & impulse suppression. Always use the foam tips on the line.")}
                    {compact_card("3M PELTOR EEP-100", "NRR 23–30",
                                  "Simple one-button workhorse, 16-hour battery, IP54.")}
                  </div>
                  {sticker_box("Check Electronic Earbud Deals →", min_height=200)}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-03-plugs-neckband.png",
                "#ad • Plugs & Neckband",
                "3 / 5",
                f"""
                <div class="stack" style="gap:18px;">
                  <div class="eyebrow">Pick #2 • Reusable &amp; Double-Up Layers</div>
                  <h2 class="h1-lg" style="font-size:52px;">Plugs &amp; <span class="gold">Neckband Muffs</span></h2>
                  {compact_card("Sordin Supreme Pro-X (Neckband)", "Behind Head",
                                "Electronic muffs with band behind the head — fits a Patka or ears-exposed Keski.", "gold")}
                  {compact_card("Decibullz Custom Molded", "NRR 31",
                                "Boil-and-shape earpieces that lock into your exact ear contour in 5 minutes.", "blue")}
                  {compact_card("3M E-A-Rsoft FX &amp; Mack's Ultra Soft", "NRR 33",
                                "Max-NRR soft foam plugs — great standalone or as the inner layer indoors.")}
                  <div class="card card-emerald" style="padding:16px 22px;">
                    <p class="body-sm" style="color:#f8fafc;"><strong>Indoor range?</strong> Double up: foam plugs + electronic protection.</p>
                  </div>
                  {sticker_box("Check Plugs & Neckband Deals →", min_height=180)}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-04-eyewear.png",
                "#ad • Eyewear",
                "4 / 5",
                f"""
                <div class="stack" style="gap:18px;">
                  <div class="eyebrow">Pick #3 • ਅੱਖਾਂ ਦੀ ਸੁਰੱਖਿਆ (ANSI Z87.1+)</div>
                  <h2 class="h1-lg" style="font-size:52px;">Thin-Temple <span class="gold">Range Eyewear</span></h2>
                  <div class="grid-2" style="gap:14px;">
                    {compact_card("ESS Crossbow Suppressor", "Z87.1+ MIL",
                                  "Wafer-thin temples slide cleanly along a Dastar without hot spots.", "blue")}
                    {compact_card("Wiley X Saber Advanced", "3-Lens Kit",
                                  "Clear, Smoke & Rust ballistic lenses + adjustable temples.", "gold")}
                    {compact_card("3M SecureFit 400", "Budget Pick",
                                  "Flat flexible temples — ideal starter pair & spares for guests.")}
                    {compact_card("NoCry OverSpecs", "Over Rx",
                                  "Wraparound Z87.1+ shield that fits over everyday glasses.")}
                  </div>
                  {sticker_box("Check Range Eyewear Deals →", min_height=200)}
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
                  <div class="eyebrow">Dastar &amp; Patka PPE Deals</div>
                  <h2 class="h1-lg" style="font-size:54px;">Protect Your Hearing —<br/><span class="gold">It Never Comes Back.</span></h2>
                  <div class="pa-banner" style="width:100%;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;">
                    <div class="pa-text-lg">ਆਪਣੀ ਸੁਣਨ ਸ਼ਕਤੀ ਦੀ ਰੱਖਿਆ ਕਰੋ — ਇਹ ਮੁੜ ਵਾਪਸ ਨਹੀਂ ਆਉਂਦੀ।</div>
                  </div>
                  {sticker_box("Dastar-Friendly PPE Deals →", min_height=240)}
                  <p class="body-sm" style="max-width:820px;">
                    Black Friday prices change hourly — check current pricing on Amazon. Every qualifying purchase helps fund SikhRPA's free 501(c)(3) education.
                  </p>
                  {disclosure_bar()}
                </div>
                """,
            ),
        ],
    }

    # =========================================================================
    # BF-C — Cyber Monday Safety Stocking Stuffers (Mon, Nov 30) — 4 Story Frames
    # =========================================================================
    post_c = {
        "number": 103,
        "slug": "bf-c-cyber-monday-stocking-stuffers",
        "date_display": "Mon, Nov 30, 2026 (Cyber Monday)",
        "time_pst": "9:00 AM PST (stagger frames through the day)",
        "format": "Instagram Story Sequence (4 frames, 9:16)",
        "title": "Cyber Monday Stories: Safety Stocking Stuffers",
        "url": f"{DEALS_URL}#stocking-stuffers",
        "caption": (
            "(Instagram Stories — '#ad' and Amazon Associates disclosure are built into every frame.)\n\n"
            "Paste this URL into the Instagram Link Sticker on Frames 2, 3, and 4:\n"
            f"  {DEALS_URL}#stocking-stuffers\n"
            "Suggested sticker text: 'Cyber Monday Stocking Stuffers'"
        ),
        "hashtags": "#ad #SikhRPA #CyberMonday #StockingStuffers #RangeSafety #HomeSafety #SikhCommunity",
        "story_prompt": (
            "Frame 1: No sticker needed (optional Countdown sticker to Cyber Monday midnight). "
            f"Frames 2–4: Place a native Instagram Link Sticker inside the dashed box pointing to {DEALS_URL}#stocking-stuffers. "
            "Save to your 'Black Friday' Story Highlight."
        ),
        "links": [
            ("Primary Story Link Sticker (Section 3)", f"{DEALS_URL}#stocking-stuffers"),
            ("Full 2026 Black Friday Deals Page", DEALS_URL),
        ],
        "slides": [
            make_story(
                "story-01-cover.png",
                "#ad • Cyber Monday",
                "1 / 4",
                f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:30px;">
                  <img class="brand-logo" style="width:130px;height:130px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">Cyber Monday • Last Call</div>
                  <h1 class="h1-hero" style="font-size:72px;">Safety<br/><span class="gold">Stocking Stuffers</span></h1>
                  <p class="lead" style="font-size:30px;max-width:860px;">
                    Budget-friendly safety essentials every range bag needs. Tap through →
                  </p>
                  <div class="pa-banner" style="width:100%;text-align:center;">
                    <div class="pa-text-lg">ਛੋਟੇ ਤੋਹਫ਼ੇ, ਵੱਡੀ ਸੁਰੱਖਿਆ</div>
                    <div class="body-sm" style="margin-top:6px;">Small gifts, big safety</div>
                  </div>
                  {disclosure_bar()}
                </div>
                """,
                footer_right="TAP THROUGH →",
            ),
            make_story(
                "story-02-ears-locks.png",
                "#ad • Cyber Monday",
                "2 / 4",
                f"""
                <div class="stack" style="gap:24px;">
                  <div class="eyebrow">Stuffer #1 &amp; #2</div>
                  <h2 class="h1-lg" style="font-size:58px;">Ears &amp; <span class="gold">Locks</span></h2>
                  {product_card("Mack's / 3M E-A-Rsoft Foam Plugs", "NRR 33",
                                "Zero Dastar contact. Toss a bulk pack in every range bag and car.", "blue")}
                  {product_card("Master Lock 120Q (4-Pack)", "Keyed Alike",
                                "Lock range-bag zippers and case hasps — one key opens all four.", "gold")}
                  {sticker_box("Check Stocking Stuffer Deals →", min_height=220)}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-03-after-range.png",
                "#ad • Cyber Monday",
                "3 / 4",
                f"""
                <div class="stack" style="gap:24px;">
                  <div class="eyebrow">Stuffer #3 &amp; #4</div>
                  <h2 class="h1-lg" style="font-size:58px;">After the <span class="gold">Range</span></h2>
                  {product_card("ESCA Tech D-Wipe Towels", "Lead Removal",
                                "Wipe lead residue off hands &amp; face before driving home or hugging the kids.", "emerald")}
                  {product_card("Break-Free CLP + Hoppe's BoreSnake", "Clean &amp; Protect",
                                "Quick post-range cleaning and a rust-inhibiting film before storage.", "blue")}
                  {sticker_box("Check Range Care Deals →", min_height=220)}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
            make_story(
                "story-04-in-the-safe.png",
                "#ad • Cyber Monday",
                "4 / 4",
                f"""
                <div class="stack" style="gap:20px;">
                  <div class="eyebrow">Stuffer #5 &amp; #6</div>
                  <h2 class="h1-lg" style="font-size:54px;">Safe &amp; <span class="gold">Dry-Fire</span></h2>
                  {compact_card("Eva-Dry E-333 + MTM AC50C Can", "Dry &amp; Locked",
                                "Rechargeable dehumidifier prevents rust; lockable can keeps ammo stored separately.", "blue")}
                  {compact_card("Tipton Snap Caps", "Dry-Fire Practice",
                                "Inert dummy rounds for safe at-home trigger practice and malfunction drills.", "gold")}
                  <div class="card card-emerald" style="padding:18px 22px;">
                    <p class="body-sm" style="color:#f8fafc;">
                      <strong>Need a free cable lock?</strong> Email <strong>president@sikhrpa.org</strong>.
                    </p>
                  </div>
                  {sticker_box("All 2026 Black Friday Picks →", min_height=200)}
                  {disclosure_bar()}
                </div>
                """,
                theme="default",
            ),
        ],
    }

    return [post_a, post_b, post_c]


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
        "--- OPTIONAL HASHTAGS (if adding a text tag) ---\n\n"
        f"{post['hashtags']}\n\n"
        "--- UNLISTED DEALS PAGE URLS (Amazon tag: sikhrpa01-20 built in) ---\n\n"
        f"{links}\n\n"
        "--- BEFORE POSTING ---\n"
        "• Open https://sikhrpa.org/black-friday-2026 and check a few items on Amazon to confirm deals are active.\n"
        "• Place Instagram's native Link Sticker inside the dashed box on each Story frame.\n"
        "• Do not add dollar prices for Amazon items (Amazon Operating Agreement).\n"
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
            if out_dir.exists():
                shutil.rmtree(out_dir)
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
    print("\n✓ All 14 Black Friday Story graphics rendered with zero overflow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
