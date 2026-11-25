#!/usr/bin/env python3
"""
SikhRPA Black Friday / Cyber Monday 2026 — Amazon Associates Safety Gear Posts
Renders 3 affiliate-eligible posts (4:5 carousels + 9:16 Stories) using the
shared SikhRPA brand system (styles.build_slide_html), writes caption.txt
files with FTC / Amazon Associates disclosures, and exports sRGB JPEGs.

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
from urllib.parse import quote_plus

from PIL import Image
from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from generate_all import audit_policy_guardrails  # noqa: E402
from styles import ROOT_DIR, build_slide_html, get_logo_data_uri  # noqa: E402

OUT_ROOT = ROOT_DIR / "posts" / "black-friday-2026"
AMAZON_TAG = "sikhrpa01-20"
DISCLOSURE_SHORT = "#ad • As an Amazon Associate, SikhRPA earns from qualifying purchases."
DISCLOSURE_SLIDE = (
    "Affiliate disclosure: As an Amazon Associate, SikhRPA earns from qualifying purchases "
    "at no extra cost to you. Proceeds fund free 501(c)(3) safety education."
)


def amazon_link(query: str) -> str:
    """Tagged Amazon search link (same format as sikhrpa.org gear-shelf.js fallback)."""
    return f"https://www.amazon.com/s?k={quote_plus(query)}&tag={AMAZON_TAG}"


def product_card(name: str, badge: str, why: str, tone: str = "") -> str:
    tone_cls = f" card-{tone}" if tone else ""
    return f"""
    <div class="card{tone_cls} stack-sm" style="padding:22px 26px;">
      <div class="row" style="gap:12px;justify-content:space-between;">
        <div class="h3-title" style="font-size:27px;">{name}</div>
        <span class="pill" style="font-size:13px;padding:4px 12px;white-space:nowrap;">{badge}</span>
      </div>
      <p class="body-sm">{why}</p>
    </div>
    """


def disclosure_bar() -> str:
    return f"""
    <div style="font-size:15px;line-height:1.45;color:#94a3b8;text-align:center;max-width:900px;">
      {DISCLOSURE_SLIDE}
    </div>
    """


def get_posts() -> list[dict]:
    logo = get_logo_data_uri()

    # =========================================================================
    # BF-A — Safe Storage Is the Best Gift (Fri, Nov 27)
    # =========================================================================
    post_a = {
        "number": 101,
        "slug": "bf-a-safe-storage-best-gift",
        "date_display": "Fri, Nov 27, 2026 (Black Friday)",
        "time_pst": "8:00 AM PST",
        "format": "Carousel (5 slides, 4:5) + Story (9:16)",
        "title": "Black Friday: Safe Storage Is the Best Gift",
        "url": "https://sikhrpa.org/safe-storage.html",
        "caption": (
            f"{DISCLOSURE_SHORT}\n\n"
            "The best Black Friday gift for any firearm-owning household isn't another accessory — it's a lock. 🔒\n\n"
            "Many of the lockboxes and storage essentials on SikhRPA's vetted Safe Storage list are marked down "
            "this week. Swipe for our picks:\n"
            "• Bedside quick-access: Hornady RAPiD Safe 2700KP XL • Vaultek LifePod 2.0\n"
            "• Budget & vehicle transport: SnapSafe Steel Lock Box XL • Pelican Vault V300 + Master Lock 120Q\n"
            "• Inside the safe: Eva-Dry E-333 dehumidifier • MTM AC50C lockable can\n\n"
            "Why it matters: under California Penal Code § 25100, leaving a firearm where a child or prohibited "
            "person can access it can be a crime. Handguns in a vehicle must be in a locked container or trunk (PC § 25610).\n\n"
            "Full guide + links: sikhrpa.org/safe-storage.html (link in bio). Prices change fast during Black Friday — "
            "check the current price before you buy, and confirm your exact model on the CA DOJ roster of approved devices.\n\n"
            "Every qualifying purchase helps fund free bilingual safety workshops and free cable locks for families.\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#ad #SikhRPA #SafeStorage #BlackFriday #HolidayGiftIdeas #HomeSafety #ChildSafety "
            "#CaliforniaLaw #PC25100 #FirearmSafetyEducation #SikhCommunity #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Post story-01-link.png and place a LINK sticker in the dashed zone pointing to "
            "https://sikhrpa.org/safe-storage.html (sticker text: 'Safe Storage Picks'). "
            "Keep the '#ad' text visible."
        ),
        "links": [
            ("Safe Storage guide (preferred, has disclosure)", "https://sikhrpa.org/safe-storage.html"),
            ("Hornady RAPiD 2700KP XL", amazon_link("Hornady RAPiD Safe 2700KP XL")),
            ("Vaultek LifePod 2.0", amazon_link("Vaultek LifePod 2.0 pistol lockbox safe")),
            ("SnapSafe Steel Lock Box XL", amazon_link("SnapSafe Lock Box XL steel 75201")),
            ("Pelican Vault V300", amazon_link("Pelican Vault V300 large pistol case")),
            ("Master Lock 120Q (4-pack)", amazon_link("Master Lock 120Q brass padlock 4 pack keyed alike")),
            ("Eva-Dry E-333", amazon_link("Eva-Dry E-333 renewable mini dehumidifier")),
            ("MTM AC50C", amazon_link("MTM AC50C 50 caliber ammo can")),
        ],
        "slides": [
            {
                "filename": "slide-01-cover.png",
                "theme": "royal",
                "pill_text": "Black Friday • Safe Storage",
                "slide_label": "01 / 05",
                "body_html": """
                <div class="eyebrow">Black Friday Gift Guide • 2026</div>
                <h1 class="h1-hero">The Best Gift This Year?<br/><span class="gold">A Lock.</span></h1>
                <p class="lead">
                  Lockboxes and storage essentials from SikhRPA's <strong style="color:#fff;">vetted Safe Storage list</strong>
                  are marked down this week. Protect your family — and support free safety education.
                </p>
                <div class="pa-banner">
                  <div class="pa-text-lg">ਸੁਰੱਖਿਅਤ ਸਟੋਰੇਜ — ਪਰਿਵਾਰ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਤੋਹਫ਼ਾ</div>
                </div>
                <div class="stat-row" style="margin-top:6px;">
                  <div class="stat-box"><div class="stat-val">Bedside</div><div class="stat-lbl">Quick Access</div></div>
                  <div class="stat-box"><div class="stat-val">Vehicle</div><div class="stat-lbl">PC § 25610</div></div>
                  <div class="stat-box"><div class="stat-val">Inside</div><div class="stat-lbl">The Safe</div></div>
                </div>
                """,
            },
            {
                "filename": "slide-02-bedside.png",
                "theme": "default",
                "pill_text": "Bedside Quick-Access",
                "slide_label": "02 / 05",
                "body_html": f"""
                <div class="eyebrow">Pick #1 • ਬਿਸਤਰੇ ਕੋਲ ਤਾਲਾਬੰਦ ਬਕਸਾ</div>
                <h2 class="h1-lg">Bedside <span class="gold">Quick-Access</span> Lockboxes</h2>
                <p class="body-text">Fast for you. Locked for curious kids and visiting guests.</p>
                <div class="stack" style="gap:18px;">
                  {product_card("Hornady RAPiD® Safe 2700KP XL", "14-Gauge Steel",
                                "RFID tag + backlit keypad + key backup. Exceeds ASTM child-resistance and pry-resistance standards.", "blue")}
                  {product_card("Vaultek LifePod 2.0", "IP65 Sealed",
                                "Lightweight, weather-sealed lockbox with keypad, key backup, and steel tether cable — bedside or travel.", "gold")}
                </div>
                <div class="card card-emerald" style="padding:18px 24px;">
                  <p class="body-sm" style="color:#f8fafc;"><strong>Tip:</strong> Never use birthdays as codes, and never leave the backup key on a dresser.</p>
                </div>
                """,
            },
            {
                "filename": "slide-03-budget-vehicle.png",
                "theme": "default",
                "pill_text": "Budget & Vehicle",
                "slide_label": "03 / 05",
                "body_html": f"""
                <div class="eyebrow">Pick #2 • ਗੱਡੀ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਆਵਾਜਾਈ</div>
                <h2 class="h1-lg">Budget &amp; <span class="gold">Vehicle Transport</span></h2>
                <p class="body-text">California requires handguns in a vehicle to be in a <strong style="color:#fff;">locked container</strong> or trunk (PC § 25610).</p>
                <div class="stack" style="gap:18px;">
                  {product_card("SnapSafe Steel Lock Box XL", "Budget Pick",
                                "16-gauge steel with a 1,500 lb tether cable for car seats or luggage. Choose steel, and confirm your SKU on the CA DOJ roster.", "blue")}
                  {product_card("Pelican Vault V300", "Crushproof",
                                "Weather-sealed hard case with stainless padlock hasps for multi-pistol range days and airline check-in.", "gold")}
                  {product_card("Master Lock 120Q (4-Pack)", "Keyed Alike",
                                "Slim brass padlocks that fit case hasps and soft-bag zippers. One key opens all four.")}
                </div>
                """,
            },
            {
                "filename": "slide-04-inside-the-safe.png",
                "theme": "default",
                "pill_text": "Inside the Safe",
                "slide_label": "04 / 05",
                "body_html": f"""
                <div class="eyebrow">Pick #3 • Budget-Friendly Add-Ons</div>
                <h2 class="h1-lg">Finish the Job <span class="gold">Inside the Safe</span></h2>
                <div class="stack" style="gap:18px;">
                  {product_card("Eva-Dry E-333 Dehumidifier", "Cordless",
                                "Silica gel unit that pulls moisture out of safes (up to 333 cu. ft.) to prevent rust in coastal California humidity. Recharge overnight.", "blue")}
                  {product_card("MTM AC50C Lockable Can", "Padlock Tabs",
                                "O-ring sealed, stackable can with dual padlock tabs — store ammunition locked and separate from firearms.", "gold")}
                </div>
                <div class="pa-banner">
                  <div class="pa-text-md">ਹਥਿਆਰ ਅਤੇ ਗੋਲੀ-ਸਿੱਕਾ ਹਮੇਸ਼ਾ ਵੱਖ-ਵੱਖ ਤਾਲੇ ਹੇਠ ਰੱਖੋ।</div>
                  <div class="body-sm" style="margin-top:6px;">Always lock firearms and ammunition separately.</div>
                </div>
                """,
            },
            {
                "filename": "slide-05-cta.png",
                "theme": "royal",
                "pill_text": "Link in Bio",
                "slide_label": "05 / 05",
                "footer_right": "SAVE &amp; SHARE",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;">
                  <img class="brand-logo" style="width:120px;height:120px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="eyebrow">Full Guide &amp; Current Prices</div>
                  <h2 class="h1-lg">sikhrpa.org/<span class="gold">safe-storage</span></h2>
                  <p class="lead" style="max-width:840px;">
                    Tap the link in our bio for every pick, CA storage rules, and our Vehicle Transport Checker.
                    Black Friday prices change hourly — check before you buy.
                  </p>
                  <div class="grid-2" style="width:100%;">
                    <div class="card card-gold stack-sm" style="padding:22px;">
                      <div class="gold" style="font-size:15px;font-weight:900;">EVERY PURCHASE HELPS</div>
                      <p class="body-sm">Funds free bilingual workshops &amp; free CA DOJ cable locks</p>
                    </div>
                    <div class="card card-blue stack-sm" style="padding:22px;">
                      <div class="blue-lt" style="font-size:15px;font-weight:900;">FREE CABLE LOCK</div>
                      <p class="body-sm">Email president@sikhrpa.org</p>
                    </div>
                  </div>
                  {disclosure_bar()}
                  <div class="pa-text-md">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                </div>
                """,
            },
            {
                "filename": "story-01-link.png",
                "height": 1920,
                "theme": "royal",
                "frame_variant": "story-frame",
                "pill_text": "#ad • Black Friday",
                "slide_label": "STORY",
                "footer_url": "sikhrpa.org/safe-storage.html",
                "footer_right": "TAP LINK STICKER ↑",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:120px;height:120px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">Black Friday Safe Storage Picks</div>
                  <h1 class="h1-hero" style="font-size:66px;">The Best Gift?<br/><span class="gold">A Lock.</span></h1>
                  <p class="lead" style="font-size:28px;max-width:860px;">
                    Bedside lockboxes, vehicle cases &amp; in-safe essentials from our vetted list — marked down this week.
                  </p>
                  <div class="sticker-zone" style="width:100%;min-height:300px;">
                    <div style="font-size:20px;font-weight:900;letter-spacing:0.12em;color:#fbbf24;text-transform:uppercase;">
                      [ Place Link Sticker Here ]
                    </div>
                    <div style="font-size:30px;font-weight:800;color:#fff;">Safe Storage Picks →</div>
                  </div>
                  <div class="pa-text-md">ਸੁਰੱਖਿਅਤ ਸਟੋਰੇਜ — ਸਭ ਤੋਂ ਵਧੀਆ ਤੋਹਫ਼ਾ</div>
                  {disclosure_bar()}
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # BF-B — Range PPE for Dastar & Patka Wearers (Sat, Nov 28)
    # =========================================================================
    post_b = {
        "number": 102,
        "slug": "bf-b-dastar-friendly-range-ppe",
        "date_display": "Sat, Nov 28, 2026",
        "time_pst": "10:00 AM PST",
        "format": "Carousel (5 slides, 4:5) + Story (9:16)",
        "title": "Black Friday: Dastar & Patka-Friendly Ear and Eye Protection",
        "url": "https://sikhrpa.org/range-ppe.html",
        "caption": (
            f"{DISCLOSURE_SHORT}\n\n"
            "Over-the-ear muffs can't seal properly over a Dastar — and a broken seal means real hearing damage. "
            "That's why SikhRPA built a Dastar- and Patka-friendly range protection guide. 🎯👳\n\n"
            "Many of our vetted picks are marked down for Black Friday weekend. Swipe for:\n"
            "• Electronic earbuds (zero Dastar contact): ISOtunes Sport ADVANCE BT & CALIBER BT • Walker's Disrupter • 3M PELTOR EEP-100\n"
            "• Foam plugs & neckband muffs: 3M E-A-Rsoft FX • Mack's Ultra Soft • Sordin Supreme Pro-X\n"
            "• ANSI Z87.1+ eyewear with thin temples: ESS Crossbow Suppressor • 3M SecureFit 400 • NoCry OTG (over prescription glasses)\n\n"
            "Indoor range? Double up: foam plugs + electronic protection.\n\n"
            "Full guide, fit tips & links: sikhrpa.org/range-ppe.html (link in bio). Prices change fast — check the current price before you buy.\n\n"
            "Every qualifying purchase helps fund free bilingual safety education.\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#ad #SikhRPA #HearingProtection #EyeProtection #Dastar #Patka #SikhCommunity "
            "#BlackFriday #RangeSafety #FirearmSafetyEducation #CaliforniaSikhs #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Post story-01-link.png and place a LINK sticker in the dashed zone pointing to "
            "https://sikhrpa.org/range-ppe.html (sticker text: 'Dastar-Friendly PPE'). "
            "Add a Poll sticker: 'Earbuds or neckband muffs?'"
        ),
        "links": [
            ("Range PPE guide (preferred, has disclosure)", "https://sikhrpa.org/range-ppe.html"),
            ("ISOtunes Sport ADVANCE BT", amazon_link("ISOtunes Sport ADVANCE BT shooting earbuds")),
            ("ISOtunes Sport CALIBER BT", amazon_link("ISOtunes Sport CALIBER BT shooting earbuds")),
            ("Walker's Disrupter", amazon_link("Walker's Disrupter Bluetooth earbuds")),
            ("3M PELTOR EEP-100", amazon_link("3M PELTOR EEP-100 electronic earplugs")),
            ("3M E-A-Rsoft FX", amazon_link("3M E-A-Rsoft FX earplugs NRR 33")),
            ("Mack's Ultra Soft", amazon_link("Mack's Ultra Soft Foam Earplugs 33dB")),
            ("Sordin Supreme Pro-X Neckband", amazon_link("Sordin Supreme Pro-X neckband")),
            ("ESS Crossbow Suppressor", amazon_link("ESS Crossbow Suppressor safety glasses")),
            ("3M SecureFit 400", amazon_link("3M SecureFit 400 safety glasses anti-fog")),
            ("NoCry OverSpecs OTG", amazon_link("NoCry over the glasses safety glasses")),
        ],
        "slides": [
            {
                "filename": "slide-01-cover.png",
                "theme": "royal",
                "pill_text": "Black Friday • Range PPE",
                "slide_label": "01 / 05",
                "body_html": """
                <div class="eyebrow">Dastar &amp; Patka-Friendly • Black Friday Picks</div>
                <h1 class="h1-hero">Muffs Don't Seal<br/><span class="gold">Over a Dastar.</span></h1>
                <p class="lead">
                  A broken seal means real hearing damage. These vetted ear &amp; eye protection picks
                  fit <strong style="color:#fff;">with</strong> your Dastar or Patka — and many are marked down this weekend.
                </p>
                <div class="pa-banner">
                  <div class="pa-text-lg">ਦਸਤਾਰ ਅਤੇ ਪਟਕੇ ਨਾਲ ਕੰਨਾਂ ਅਤੇ ਅੱਖਾਂ ਦੀ ਸੁਰੱਖਿਆ</div>
                </div>
                <div class="stat-row" style="margin-top:6px;">
                  <div class="stat-box"><div class="stat-val">In-Ear</div><div class="stat-lbl">Zero Contact</div></div>
                  <div class="stat-box"><div class="stat-val">Neckband</div><div class="stat-lbl">Behind Head</div></div>
                  <div class="stat-box"><div class="stat-val">Z87.1+</div><div class="stat-lbl">Thin Temples</div></div>
                </div>
                """,
            },
            {
                "filename": "slide-02-electronic-earbuds.png",
                "theme": "default",
                "pill_text": "Electronic In-Ear",
                "slide_label": "02 / 05",
                "body_html": f"""
                <div class="eyebrow">Pick #1 • Hear Range Commands, Block Gunshots</div>
                <h2 class="h1-lg">Electronic <span class="gold">Earbuds</span></h2>
                <div class="grid-2" style="gap:16px;">
                  {product_card("ISOtunes ADVANCE BT", "NRR 26",
                                "Tactical Sound Control, IP67, neck tether so you never drop a bud.", "blue")}
                  {product_card("ISOtunes CALIBER BT", "NRR 25",
                                "Fully wireless with pocket charging case. Zero bulk under a Dastar.", "gold")}
                  {product_card("Walker's Disrupter", "NRR 24",
                                "360° mics and fast impulse suppression. Always use the foam tips on the line.")}
                  {product_card("3M PELTOR EEP-100", "NRR 23–30",
                                "Simple one-button workhorse, 16-hour battery, IP54.")}
                </div>
                """,
            },
            {
                "filename": "slide-03-plugs-neckband.png",
                "theme": "default",
                "pill_text": "Plugs & Neckband",
                "slide_label": "03 / 05",
                "body_html": f"""
                <div class="eyebrow">Pick #2 • Budget &amp; Double-Up Layers</div>
                <h2 class="h1-lg">Foam Plugs &amp; <span class="gold">Neckband Muffs</span></h2>
                <div class="stack" style="gap:16px;">
                  {product_card("3M E-A-Rsoft FX", "NRR 33",
                                "Soft slow-recovery foam. Great alone or as the inner layer when doubling up.", "blue")}
                  {product_card("Mack's Ultra Soft Foam", "NRR 33",
                                "Ultra-low-pressure foam — comfortable for long 2–3 hour classes.", "blue")}
                  {product_card("Sordin Supreme Pro-X (Neckband)", "Behind the Head",
                                "Electronic muffs with the band behind the head — works with a Patka or ears-exposed Keski.", "gold")}
                </div>
                <div class="card card-emerald" style="padding:18px 24px;">
                  <p class="body-sm" style="color:#f8fafc;"><strong>Indoor range?</strong> Double up: foam plugs + electronic protection.</p>
                </div>
                """,
            },
            {
                "filename": "slide-04-eyewear.png",
                "theme": "default",
                "pill_text": "ANSI Z87.1+ Eyewear",
                "slide_label": "04 / 05",
                "body_html": f"""
                <div class="eyebrow">Pick #3 • ਅੱਖਾਂ ਦੀ ਸੁਰੱਖਿਆ</div>
                <h2 class="h1-lg">Eyewear That <span class="gold">Slides Along a Dastar</span></h2>
                <div class="stack" style="gap:16px;">
                  {product_card("ESS Crossbow Suppressor", "Z87.1+ • MIL",
                                "Wafer-thin temples slide along a Dastar and under muffs without hot spots. Rx insert available.", "blue")}
                  {product_card("3M SecureFit 400", "Budget Pick",
                                "Featherweight with flat flexible temples — great starter pair and spares for guests.", "gold")}
                  {product_card("NoCry OverSpecs (OTG)", "Over Rx Glasses",
                                "Wraparound Z87.1+ shield that fits over everyday prescription frames.")}
                </div>
                """,
            },
            {
                "filename": "slide-05-cta.png",
                "theme": "royal",
                "pill_text": "Link in Bio",
                "slide_label": "05 / 05",
                "footer_right": "SAVE &amp; SHARE",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;">
                  <img class="brand-logo" style="width:120px;height:120px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="eyebrow">Full Guide &amp; Current Prices</div>
                  <h2 class="h1-lg">sikhrpa.org/<span class="gold">range-ppe</span></h2>
                  <p class="lead" style="max-width:840px;">
                    Use our <strong style="color:#fff;">Build Your Range PPE Setup</strong> tool to match protection to your Dastar,
                    Patka, or glasses. Black Friday prices change hourly — check before you buy.
                  </p>
                  <div class="pa-banner" style="width:100%;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;">
                    <div class="pa-text-lg">ਆਪਣੀ ਸੁਣਨ ਸ਼ਕਤੀ ਦੀ ਰੱਖਿਆ ਕਰੋ — ਇਹ ਮੁੜ ਵਾਪਸ ਨਹੀਂ ਆਉਂਦੀ।</div>
                    <div class="body-sm" style="margin-top:6px;">Protect your hearing — it never comes back.</div>
                  </div>
                  {disclosure_bar()}
                  <div class="pa-text-md">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                </div>
                """,
            },
            {
                "filename": "story-01-link.png",
                "height": 1920,
                "theme": "royal",
                "frame_variant": "story-frame",
                "pill_text": "#ad • Black Friday",
                "slide_label": "STORY",
                "footer_url": "sikhrpa.org/range-ppe.html",
                "footer_right": "TAP LINK STICKER ↑",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:120px;height:120px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">Dastar-Friendly Range PPE</div>
                  <h1 class="h1-hero" style="font-size:64px;">Muffs Don't Seal<br/><span class="gold">Over a Dastar.</span></h1>
                  <p class="lead" style="font-size:28px;max-width:860px;">
                    Electronic earbuds, neckband muffs &amp; thin-temple eyewear — vetted picks marked down this weekend.
                  </p>
                  <div class="sticker-zone" style="width:100%;min-height:300px;">
                    <div style="font-size:20px;font-weight:900;letter-spacing:0.12em;color:#fbbf24;text-transform:uppercase;">
                      [ Place Link Sticker Here ]
                    </div>
                    <div style="font-size:30px;font-weight:800;color:#fff;">Dastar-Friendly PPE →</div>
                  </div>
                  <div class="pa-text-md">ਦਸਤਾਰ ਅਤੇ ਪਟਕੇ ਨਾਲ ਕੰਨਾਂ ਅਤੇ ਅੱਖਾਂ ਦੀ ਸੁਰੱਖਿਆ</div>
                  {disclosure_bar()}
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # BF-C — Cyber Monday Safety Stocking Stuffers (Mon, Nov 30) — Story set
    # =========================================================================
    def story(filename: str, label: str, footer_url: str, inner: str, footer_right: str = "TAP LINK STICKER ↑") -> dict:
        return {
            "filename": filename,
            "height": 1920,
            "theme": "royal",
            "frame_variant": "story-frame",
            "pill_text": "#ad • Cyber Monday",
            "slide_label": label,
            "footer_url": footer_url,
            "footer_right": footer_right,
            "body_html": inner,
        }

    def sticker(text: str) -> str:
        return f"""
        <div class="sticker-zone" style="width:100%;min-height:220px;">
          <div style="font-size:20px;font-weight:900;letter-spacing:0.12em;color:#fbbf24;text-transform:uppercase;">
            [ Place Link Sticker Here ]
          </div>
          <div style="font-size:28px;font-weight:800;color:#fff;">{text}</div>
        </div>
        """

    post_c = {
        "number": 103,
        "slug": "bf-c-cyber-monday-stocking-stuffers",
        "date_display": "Mon, Nov 30, 2026 (Cyber Monday)",
        "time_pst": "9:00 AM PST (stagger frames through the day)",
        "format": "Story Set (4 frames, 9:16)",
        "title": "Cyber Monday: Safety Stocking Stuffers",
        "url": "https://sikhrpa.org/safe-storage.html",
        "caption": (
            "(Stories have no caption — the '#ad' disclosure is printed on every frame.)\n\n"
            "Optional feed cross-post caption:\n"
            f"{DISCLOSURE_SHORT}\n\n"
            "Last call for Cyber Monday: small safety gifts that every range bag needs — foam earplugs, "
            "keyed-alike padlocks, lead-removal wipes, and post-range cleaning basics. Links in our Story & bio.\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": "#ad #SikhRPA #CyberMonday #StockingStuffers #RangeSafety #HomeSafety #SikhCommunity",
        "story_prompt": (
            "Frame 1: no sticker needed (or a Countdown sticker to midnight). "
            "Frame 2: link → https://sikhrpa.org/range-ppe.html. "
            "Frames 3–4: link → https://sikhrpa.org/safe-storage.html. "
            "Add all 4 to a 'Gift Guide' Highlight afterwards."
        ),
        "links": [
            ("Range PPE guide", "https://sikhrpa.org/range-ppe.html"),
            ("Safe Storage guide", "https://sikhrpa.org/safe-storage.html"),
            ("Mack's Ultra Soft", amazon_link("Mack's Ultra Soft Foam Earplugs 33dB")),
            ("3M E-A-Rsoft FX", amazon_link("3M E-A-Rsoft FX earplugs NRR 33")),
            ("Master Lock 120Q (4-pack)", amazon_link("Master Lock 120Q brass padlock 4 pack keyed alike")),
            ("D-Wipe lead-removing towels", amazon_link("ESCA Tech D-Wipe lead removing towels")),
            ("Break-Free CLP", amazon_link("Break-Free CLP cleaner lubricant preservative")),
            ("Hoppe's BoreSnake", amazon_link("Hoppe's BoreSnake bore cleaner")),
            ("Eva-Dry E-333", amazon_link("Eva-Dry E-333 renewable mini dehumidifier")),
        ],
        "slides": [
            story("story-01-cover.png", "1 / 4", "sikhrpa.org", f"""
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
            """, footer_right="TAP THROUGH →"),
            story("story-02-ears-locks.png", "2 / 4", "sikhrpa.org/range-ppe.html", f"""
                <div class="stack" style="gap:24px;">
                  <div class="eyebrow">Stuffer #1 &amp; #2</div>
                  <h2 class="h1-lg" style="font-size:58px;">Ears &amp; <span class="gold">Locks</span></h2>
                  {product_card("Mack's / 3M E-A-Rsoft Foam Plugs", "NRR 33",
                                "Zero Dastar contact. Toss a bulk pack in every range bag and car.", "blue")}
                  {product_card("Master Lock 120Q (4-Pack)", "Keyed Alike",
                                "Lock range-bag zippers and case hasps — one key opens all four.", "gold")}
                  {sticker("Dastar-Friendly Ear Pro →")}
                  {disclosure_bar()}
                </div>
            """),
            story("story-03-after-range.png", "3 / 4", "sikhrpa.org/safe-storage.html", f"""
                <div class="stack" style="gap:24px;">
                  <div class="eyebrow">Stuffer #3 &amp; #4</div>
                  <h2 class="h1-lg" style="font-size:58px;">After the <span class="gold">Range</span></h2>
                  {product_card("ESCA Tech D-Wipe Towels", "Lead Removal",
                                "Wipe lead residue off hands &amp; face before driving home or hugging the kids.", "emerald")}
                  {product_card("Break-Free CLP + Hoppe's BoreSnake", "Clean &amp; Protect",
                                "Quick post-range cleaning and a rust-inhibiting film before storage.", "blue")}
                  {sticker("Range Care Essentials →")}
                  {disclosure_bar()}
                </div>
            """),
            story("story-04-in-the-safe.png", "4 / 4", "sikhrpa.org/safe-storage.html", f"""
                <div class="stack" style="gap:24px;">
                  <div class="eyebrow">Stuffer #5</div>
                  <h2 class="h1-lg" style="font-size:58px;">Inside <span class="gold">the Safe</span></h2>
                  {product_card("Eva-Dry E-333 Dehumidifier", "Cordless",
                                "Keeps safes dry in coastal California humidity. Recharge overnight, reuse for years.", "blue")}
                  <div class="card card-gold" style="padding:22px 26px;">
                    <p class="body-text" style="color:#f8fafc;">
                      <strong>No safe yet?</strong> SikhRPA gives free CA DOJ cable locks at every workshop —
                      email <strong>president@sikhrpa.org</strong>.
                    </p>
                  </div>
                  {sticker("All Safe Storage Picks →")}
                  {disclosure_bar()}
                </div>
            """),
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
        f"Link:     {post['url']} (set as link in bio)\n"
        f"Media:    {media}\n"
        "========================================================================\n\n"
        "--- CAPTION (READY TO PASTE) ---\n\n"
        f"{post['caption']}\n\n"
        "--- HASHTAGS (READY TO PASTE) ---\n\n"
        f"{post['hashtags']}\n\n"
        "--- INSTAGRAM STORY PROMPT ---\n\n"
        f"{post['story_prompt']}\n\n"
        "--- AFFILIATE LINKS (tag: sikhrpa01-20) ---\n"
        "Prefer the sikhrpa.org page (it carries the required disclosure). Direct Amazon links\n"
        "are fine in Story link stickers as long as '#ad' stays visible. Do not use third-party\n"
        "URL shorteners for Amazon links.\n\n"
        f"{links}\n\n"
        "--- BEFORE POSTING ---\n"
        "• Open each product link and confirm it is actually discounted today.\n"
        "• Do not add dollar prices for Amazon items (Amazon Operating Agreement).\n"
        "• Keep '#ad' as the first line of the caption (FTC: disclosure above the 'more' fold).\n"
    )
    (out_dir / "caption.txt").write_text(content, encoding="utf-8")


def main() -> int:
    posts = get_posts()
    # Normalise slide defaults
    for post in posts:
        for s in post["slides"]:
            s.setdefault("width", 1080)
            s.setdefault("height", 1350)
            s.setdefault("footer_url", "sikhrpa.org")
            s.setdefault("footer_right", "SWIPE →")

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
            (out_dir / "jpg").mkdir(parents=True, exist_ok=True)
            write_caption(post, out_dir)
            for s in post["slides"]:
                w, h = s["width"], s["height"]
                page.set_viewport_size({"width": w, "height": h})
                page.set_content(
                    build_slide_html(
                        body_html=s["body_html"], width=w, height=h,
                        pill_text=s.get("pill_text", ""), slide_label=s.get("slide_label", ""),
                        footer_url=s["footer_url"], footer_right=s["footer_right"],
                        theme=s.get("theme", "default"), frame_variant=s.get("frame_variant", ""),
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
                print(f"  Rendered {post['slug']}/{s['filename']}")
        browser.close()

    if warnings:
        print("\n⚠ OVERFLOW WARNINGS:")
        for w_ in warnings:
            print("  -", w_)
        return 2
    print("\n✓ All Black Friday graphics rendered with zero overflow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
