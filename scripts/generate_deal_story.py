#!/usr/bin/env python3
"""
Reusable SikhRPA Single-Product Deal Story Generator (9:16, 1080x1920).

Generates an on-brand Instagram Story graphic featuring an official
manufacturer product photo (never Amazon-hosted imagery), discount badge,
key specs grid, Link Sticker / CTA zone, and FTC + Amazon Associates disclosure.

Outputs:
  - posts/black-friday-2026/<slug>/<filename>.png
  - posts/black-friday-2026/<slug>/jpg/<filename>.jpg
  - media/jpg/<slug>/<filename>.jpg  (for auto_post.py / raw.githubusercontent.com)

Example:
    python3 scripts/generate_deal_story.py \
      --slug bf-test-osight-se \
      --filename story-01-osight-se.png \
      --eyebrow "Black Friday Optic Deal • Subcompact RMSc" \
      --title "OSIGHT SE" \
      --subtitle "Enclosed Reflex Sight" \
      --discount "20% OFF" \
      --image "https://cdn.olightstore.com/image/se-gn-a8txty-1-lgsrmf.jpg" \
      --image-credit "Image: OSIGHT / Olight" \
      --spec "ENCLOSED EMITTER|Sealed against rain, lint & dust (IPX7)" \
      --spec "MULTI-RETICLE|2 MOA dot + 32 MOA circle, parallax-free" \
      --spec "RMSc FOOTPRINT|Direct fit for subcompact carry slides" \
      --spec "SIDE-LOAD BATTERY|Swap CR1620 without losing zero" \
      --cta-label "Check Live Deal on Amazon →" \
      --slide-label "OSIGHT SE"
"""

from __future__ import annotations

import argparse
import base64
import html
import io
import mimetypes
import shutil
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from generate_all import audit_policy_guardrails  # noqa: E402
from styles import ROOT_DIR, build_slide_html  # noqa: E402

OUT_ROOT = ROOT_DIR / "posts" / "black-friday-2026"
MEDIA_JPG_ROOT = ROOT_DIR / "media" / "jpg"
DISCLOSURE_SLIDE = (
    "Affiliate disclosure (#ad): As an Amazon Associate, SikhRPA earns from qualifying "
    "purchases at no extra cost to you. Proceeds fund free 501(c)(3) safety education."
)


def _trim_studio_margins(raw: bytes) -> tuple[bytes, str]:
    """Auto-trim excessive near-white studio padding so the product fills the card cleanly."""
    img = Image.open(io.BytesIO(raw))
    rgb = img.convert("RGB")
    bg = Image.new("RGB", rgb.size, rgb.getpixel((0, 0)))
    diff = ImageChops.difference(rgb, bg).convert("L")
    # Threshold out faint JPEG compression noise near the background color
    mask = diff.point(lambda p: 255 if p > 14 else 0)
    bbox = mask.getbbox()
    if bbox:
        x0, y0, x1, y1 = bbox
        w, h = img.size
        pad_x = int((x1 - x0) * 0.04)
        pad_y = int((y1 - y0) * 0.04)
        crop_box = (
            max(0, x0 - pad_x),
            max(0, y0 - pad_y),
            min(w, x1 + pad_x),
            min(h, y1 + pad_y),
        )
        img = img.crop(crop_box)
    out = io.BytesIO()
    fmt = "PNG" if img.mode in ("RGBA", "LA") else "JPEG"
    if fmt == "JPEG":
        img.convert("RGB").save(out, format="JPEG", quality=95)
        return out.getvalue(), "image/jpeg"
    img.save(out, format="PNG")
    return out.getvalue(), "image/png"


def load_image_data_uri(image_src: str) -> str:
    """Load a local file or official manufacturer HTTPS image URL as a base64 data URI."""
    if image_src.startswith(("http://", "https://")):
        req = urllib.request.Request(
            image_src,
            headers={"User-Agent": "Mozilla/5.0 (compatible; SikhRPA-StoryBuilder/1.0)"},
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read()
    else:
        path = Path(image_src).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Product image not found: {path}")
        raw = path.read_bytes()

    trimmed, ctype = _trim_studio_margins(raw)
    encoded = base64.b64encode(trimmed).decode("ascii")
    return f"data:{ctype};base64,{encoded}"


def build_product_story_body(
    *,
    eyebrow: str,
    title: str,
    subtitle: str,
    discount: str,
    image_data_uri: str,
    image_credit: str,
    specs: list[tuple[str, str]],
    cta_label: str,
    cta_subtext: str,
) -> str:
    spec_cards = []
    for label, detail in specs[:4]:
        spec_cards.append(
            f"""
            <div class="card" style="padding:18px 22px;display:flex;flex-direction:column;gap:5px;">
              <div style="font-size:14px;font-weight:900;letter-spacing:0.08em;color:#fbbf24;text-transform:uppercase;">
                {html.escape(label)}
              </div>
              <div style="font-size:20px;font-weight:700;line-height:1.3;color:#f1f5f9;">
                {html.escape(detail)}
              </div>
            </div>
            """
        )
    specs_grid = (
        f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;width:100%;">{"".join(spec_cards)}</div>'
        if spec_cards
        else ""
    )

    credit_html = (
        f"""
        <div style="position:absolute;bottom:14px;right:18px;font-size:13px;font-weight:700;
                    color:#64748b;background:rgba(255,255,255,0.92);padding:3px 10px;
                    border-radius:999px;border:1px solid #e2e8f0;">
          {html.escape(image_credit)}
        </div>
        """
        if image_credit
        else ""
    )

    return f"""
    <div style="display:flex;flex-direction:column;gap:22px;width:100%;">
      <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:8px;">
        <div class="eyebrow" style="font-size:18px;">{html.escape(eyebrow)}</div>
        <h1 class="h1-hero" style="font-size:60px;line-height:1.05;margin:0;">
          {html.escape(title)} <span class="gold">{html.escape(subtitle)}</span>
        </h1>
      </div>

      <div style="position:relative;width:100%;height:560px;background:#ffffff;border-radius:28px;
                  border:3px solid rgba(251,191,36,0.75);box-shadow:0 22px 48px rgba(0,0,0,0.45);
                  display:flex;align-items:center;justify-content:center;padding:34px 44px;overflow:hidden;">
        <img src="{image_data_uri}" alt="{html.escape(title)}"
             style="max-width:100%;max-height:100%;object-fit:contain;display:block;"/>
        <div style="position:absolute;top:18px;right:20px;background:#dc2626;color:#ffffff;
                    font-size:22px;font-weight:900;letter-spacing:0.06em;text-transform:uppercase;
                    padding:9px 20px;border-radius:999px;border:2px solid #fca5a5;
                    box-shadow:0 8px 20px rgba(220,38,38,0.45);">
          {html.escape(discount)}
        </div>
        {credit_html}
      </div>

      {specs_grid}

      <div class="sticker-zone" style="width:100%;min-height:142px;padding:18px 24px;gap:6px;">
        <div style="font-size:15px;font-weight:900;letter-spacing:0.12em;color:#fbbf24;text-transform:uppercase;">
          {html.escape(cta_subtext)}
        </div>
        <div style="font-size:28px;font-weight:900;color:#ffffff;">{html.escape(cta_label)}</div>
      </div>

      <div style="font-size:14px;line-height:1.4;color:#94a3b8;text-align:center;max-width:900px;margin:0 auto;">
        {DISCLOSURE_SLIDE}
      </div>
    </div>
    """


def render_deal_story(args: argparse.Namespace) -> int:
    specs: list[tuple[str, str]] = []
    for raw in args.spec or []:
        if "|" in raw:
            k, v = raw.split("|", 1)
            specs.append((k.strip(), v.strip()))
        else:
            specs.append(("HIGHLIGHT", raw.strip()))

    image_data_uri = load_image_data_uri(args.image)

    body_html = build_product_story_body(
        eyebrow=args.eyebrow,
        title=args.title,
        subtitle=args.subtitle,
        discount=args.discount,
        image_data_uri=image_data_uri,
        image_credit=args.image_credit,
        specs=specs,
        cta_label=args.cta_label,
        cta_subtext=args.cta_subtext,
    )

    # Audit visible text (without the base64 payload) against Meta policy guardrails
    audit_post = {
        "number": args.slug,
        "slug": args.slug,
        "title": f"{args.title} {args.subtitle}",
        "caption": f"{args.eyebrow} {args.cta_label} {args.cta_subtext}",
        "hashtags": "",
        "story_prompt": "",
        "slides": [
            {
                "filename": args.filename,
                "body_html": " ".join(
                    [args.eyebrow, args.title, args.subtitle, args.discount, args.cta_label]
                    + [f"{k} {v}" for k, v in specs]
                ),
            }
        ],
    }
    issues = audit_policy_guardrails([audit_post])
    if issues:
        print("POLICY GUARDRAIL FAILURES:")
        for issue in issues:
            print("  -", issue)
        return 1
    print("✓ Meta policy guardrail audit passed.")

    out_dir = OUT_ROOT / args.slug
    jpg_dir = out_dir / "jpg"
    media_dir = MEDIA_JPG_ROOT / args.slug
    jpg_dir.mkdir(parents=True, exist_ok=True)
    media_dir.mkdir(parents=True, exist_ok=True)

    full_html = build_slide_html(
        body_html=body_html,
        width=1080,
        height=1920,
        pill_text=args.pill_text,
        slide_label=args.slide_label,
        footer_url=args.footer_url,
        footer_right=args.footer_right,
        theme=args.theme,
        frame_variant="story-frame",
    )

    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    kwargs: dict = {"args": ["--no-sandbox", "--disable-gpu", "--font-render-hinting=none"]}
    if chrome:
        kwargs["executable_path"] = chrome

    with sync_playwright() as p:
        browser = p.chromium.launch(**kwargs)
        page = browser.new_context(device_scale_factor=1).new_page()
        page.set_viewport_size({"width": 1080, "height": 1920})
        page.set_content(full_html, wait_until="load")
        page.evaluate("() => document.fonts.ready")
        overflow = page.evaluate(
            """() => {
                const c = document.querySelector('.canvas');
                const b = document.querySelector('.slide-body');
                return { c: c.scrollHeight - c.clientHeight, b: b.scrollHeight - b.clientHeight };
            }"""
        )
        png_path = out_dir / args.filename
        page.screenshot(path=str(png_path), type="png")
        browser.close()

    if overflow["c"] > 2 or overflow["b"] > 2:
        print(f"⚠ OVERFLOW DETECTED: canvas={overflow['c']}px body={overflow['b']}px")
        return 2

    jpg_name = png_path.with_suffix(".jpg").name
    img_rgb = Image.open(png_path).convert("RGB")
    img_rgb.save(jpg_dir / jpg_name, quality=95)
    img_rgb.save(media_dir / jpg_name, quality=95)

    print(f"✓ Rendered PNG:       {png_path}")
    print(f"✓ Exported Story JPG: {jpg_dir / jpg_name}")
    print(f"✓ Exported Media JPG: {media_dir / jpg_name}")
    print("✓ Zero overflow confirmed.")
    return 0


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Generate a 9:16 SikhRPA product-deal Instagram Story with product photo.")
    ap.add_argument("--slug", required=True, help="Folder slug under posts/black-friday-2026/ and media/jpg/")
    ap.add_argument("--filename", required=True, help="Output PNG filename (e.g. story-01-osight-se.png)")
    ap.add_argument("--eyebrow", required=True, help="Top category/deal eyebrow text")
    ap.add_argument("--title", required=True, help="Primary product name")
    ap.add_argument("--subtitle", default="", help="Gold-accented product subtitle")
    ap.add_argument("--discount", required=True, help="Discount badge text (e.g. '20% OFF' — no static $ prices)")
    ap.add_argument("--image", required=True, help="Local path or official manufacturer HTTPS image URL")
    ap.add_argument("--image-credit", default="", help="Manufacturer image credit (e.g. 'Image: OSIGHT / Olight')")
    ap.add_argument("--spec", action="append", default=[], help="Spec item as 'LABEL|Detail' (up to 4)")
    ap.add_argument("--cta-label", default="Check Live Deal on Amazon →", help="Main CTA text")
    ap.add_argument("--cta-subtext", default="Link in Bio • sikhrpa.org/black-friday-2026", help="CTA eyebrow text")
    ap.add_argument("--pill-text", default="#ad • Black Friday Deal", help="Top-left header pill")
    ap.add_argument("--slide-label", default="DEAL ALERT", help="Top-right slide label")
    ap.add_argument("--footer-url", default="sikhrpa.org/black-friday-2026", help="Footer URL")
    ap.add_argument("--footer-right", default="TAP LINK IN BIO ↑", help="Footer right label")
    ap.add_argument("--theme", default="royal", help="Slide color theme (royal, default, gold)")
    return ap.parse_args()


if __name__ == "__main__":
    raise SystemExit(render_deal_story(parse_args()))
