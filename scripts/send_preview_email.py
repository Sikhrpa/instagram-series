#!/usr/bin/env python3
"""
SikhRPA Instagram 2-Day Advance Preview Emailer
Zero third-party dependencies (pure Python 3 standard library).

Checks publish_manifest.json + publish_state.json for any pending Instagram post
scheduled within the next ~48-60 hours (2 days ahead) whose preview email has
not yet been sent, and emails a rich HTML preview (slides, Story, full caption,
and direct GitHub edit/pause links) to tarun@sikhrpa.org.

Supports two delivery backends (configure one via GitHub Secrets):
  1. Gmail / Google Workspace SMTP (recommended, free):
       SMTP_USERNAME  - e.g. tarun@sikhrpa.org (or president@sikhrpa.org)
       SMTP_PASSWORD  - 16-char Google App Password
       SMTP_HOST      - optional (default: smtp.gmail.com)
       SMTP_PORT      - optional (default: 465)
  2. Resend API (alternative):
       RESEND_API_KEY - Resend API key
       RESEND_FROM    - optional (default: SikhRPA Auto-Poster <noreply@sikhrpa.org>)

Optional:
  PREVIEW_TO_EMAIL     - default: tarun@sikhrpa.org

Usage:
  python3 scripts/send_preview_email.py --check-due
  python3 scripts/send_preview_email.py --post post-01
  python3 scripts/send_preview_email.py --post post-01 --dry-run
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import os
import smtplib
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT_DIR / "publish_manifest.json"
STATE_PATH = ROOT_DIR / "publish_state.json"
REPO_WEB_BASE = "https://github.com/Sikhrpa/instagram-series"
DEFAULT_TO_EMAIL = "tarun@sikhrpa.org"


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def load_state(manifest: dict) -> dict:
    existing = {}
    if STATE_PATH.exists():
        existing = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    for p in manifest["posts"]:
        pid = p["post_id"]
        if pid not in existing:
            existing[pid] = {
                "slug": p["slug"],
                "scheduled_at_iso": p["scheduled_at_iso"],
                "status": "pending",
                "published_at": None,
                "ig_media_id": None,
                "story_media_id": None,
            }
    return existing


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def find_post(manifest: dict, selector: str) -> dict | None:
    sel = selector.strip().lower()
    for p in manifest["posts"]:
        if p["post_id"].lower() == sel or p["slug"].lower() == sel:
            return p
    if sel.isdigit():
        num = int(sel)
        for p in manifest["posts"]:
            if p.get("post_number") == num and p["post_id"].startswith("post-"):
                return p
    return None


def build_email_content(post: dict) -> tuple[str, str, str]:
    """Return (subject, plain_text, html_body) for a scheduled post preview."""
    pid = post["post_id"]
    title = post["title"]
    when = f"{post['date_display']} • {post['time_pst']}"
    ptype = post["publish_type"].upper()
    caption = post["caption_full"]
    bio_url = post.get("link_in_bio") or "https://sikhrpa.org/"

    subject = f"[SikhRPA IG Preview • 2 Days Ahead] {pid.upper()}: {title} ({post['date_display']})"

    edit_manifest_url = f"{REPO_WEB_BASE}/edit/main/publish_manifest.json"
    pause_state_url = f"{REPO_WEB_BASE}/edit/main/publish_state.json"
    actions_url = f"{REPO_WEB_BASE}/actions/workflows/auto-post-instagram.yml"

    media_urls = list(post.get("media_urls") or [])
    cover_url = post.get("cover_url")
    story_url = post.get("story_url")

    # Plain-text fallback
    media_lines = "\n".join(f"  - {u}" for u in media_urls)
    if cover_url:
        media_lines += f"\n  - Cover: {cover_url}"
    if story_url:
        media_lines += f"\n  - Companion 9:16 Story: {story_url}"

    plain_text = (
        f"SikhRPA Instagram Auto-Post Preview (Scheduled in ~2 Days)\n"
        f"==========================================================\n"
        f"Post ID:   {pid}\n"
        f"Title:     {title}\n"
        f"Scheduled: {when} ({post['scheduled_at_iso']})\n"
        f"Format:    {post['format']} [{ptype}]\n"
        f"Link URL:  {bio_url}\n\n"
        f"MEDIA FILES:\n{media_lines}\n\n"
        f"CAPTION + HASHTAGS ({len(caption)} / 2200 chars):\n"
        f"----------------------------------------------------------\n"
        f"{caption}\n"
        f"----------------------------------------------------------\n\n"
        f"NEED TO EDIT OR PAUSE BEFORE IT GOES LIVE?\n"
        f"- Edit caption/schedule: {edit_manifest_url}\n"
        f"- Pause/skip this post (change status from 'pending' to 'paused'): {pause_state_url}\n"
        f"- Workflow dashboard: {actions_url}\n"
    )

    # Rich HTML email
    esc = html_lib.escape
    media_blocks = []
    if ptype == "REEL":
        if cover_url:
            media_blocks.append(
                f'<div style="margin-bottom:12px;">'
                f'<div style="font-size:12px;font-weight:700;color:#94a3b8;margin-bottom:6px;">REEL COVER</div>'
                f'<img src="{esc(cover_url)}" alt="Reel Cover" style="max-width:260px;width:100%;border-radius:10px;border:1px solid #334155;" />'
                f'</div>'
            )
        if media_urls:
            media_blocks.append(
                f'<p style="margin:8px 0;"><a href="{esc(media_urls[0])}" '
                f'style="display:inline-block;background:#1e3a8a;color:#ffffff;text-decoration:none;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px;">'
                f'Download / Preview Compiled MP4 Reel ↗</a></p>'
            )
    else:
        for idx, u in enumerate(media_urls, start=1):
            label = f"Slide {idx} of {len(media_urls)}" if len(media_urls) > 1 else "Feed Graphic (4:5)"
            media_blocks.append(
                f'<div style="display:inline-block;vertical-align:top;width:240px;margin:0 10px 14px 0;">'
                f'<div style="font-size:11px;font-weight:700;color:#94a3b8;margin-bottom:4px;">{esc(label)}</div>'
                f'<a href="{esc(u)}" target="_blank">'
                f'<img src="{esc(u)}" alt="{esc(label)}" style="width:240px;max-width:100%;border-radius:10px;border:1px solid #334155;display:block;" />'
                f'</a></div>'
            )

    if story_url:
        media_blocks.append(
            f'<div style="display:inline-block;vertical-align:top;width:180px;margin:0 10px 14px 0;">'
            f'<div style="font-size:11px;font-weight:700;color:#fbbf24;margin-bottom:4px;">Companion 9:16 Story</div>'
            f'<a href="{esc(story_url)}" target="_blank">'
            f'<img src="{esc(story_url)}" alt="Companion Story" style="width:180px;max-width:100%;border-radius:10px;border:1px solid #d97706;display:block;" />'
            f'</a></div>'
        )

    caption_html = esc(caption).replace("\n", "<br/>")
    html_body = f"""<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background:#0b1120;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Roboto,sans-serif;color:#f8fafc;">
  <div style="max-width:680px;margin:0 auto;padding:24px 16px;">
    <div style="background:#0f172a;border:1px solid #334155;border-top:4px solid #f59e0b;border-radius:14px;overflow:hidden;">
      <div style="padding:22px 24px;background:linear-gradient(135deg,#0f172a 0%,#172554 100%);border-bottom:1px solid #1e293b;">
        <div style="font-size:11px;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;color:#fbbf24;">
          SikhRPA Instagram Auto-Poster • 2-Day Review Preview
        </div>
        <h1 style="margin:8px 0 6px 0;font-size:22px;line-height:1.3;color:#ffffff;">
          {esc(pid.upper())} — {esc(title)}
        </h1>
        <div style="font-size:14px;color:#cbd5e1;">
          <strong style="color:#fbbf24;">Scheduled:</strong> {esc(when)} &nbsp;•&nbsp; <strong>Format:</strong> {esc(post['format'])}
        </div>
      </div>

      <div style="padding:22px 24px;">
        <div style="margin-bottom:20px;">
          <a href="{esc(edit_manifest_url)}" style="display:inline-block;background:#f59e0b;color:#0f172a;text-decoration:none;padding:10px 16px;border-radius:8px;font-weight:800;font-size:13px;margin:0 8px 8px 0;">
            Edit Caption / Schedule
          </a>
          <a href="{esc(pause_state_url)}" style="display:inline-block;background:#334155;color:#ffffff;text-decoration:none;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px;margin:0 8px 8px 0;">
            Pause / Skip Post
          </a>
          <a href="{esc(actions_url)}" style="display:inline-block;background:#1e293b;color:#cbd5e1;border:1px solid #334155;text-decoration:none;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px;margin:0 8px 8px 0;">
            GitHub Actions
          </a>
        </div>

        <div style="font-size:12px;font-weight:800;letter-spacing:0.08em;text-transform:uppercase;color:#94a3b8;margin-bottom:10px;">
          Visual Preview (click any image for full size)
        </div>
        <div style="margin-bottom:18px;">
          {''.join(media_blocks)}
        </div>

        <div style="font-size:12px;font-weight:800;letter-spacing:0.08em;text-transform:uppercase;color:#94a3b8;margin-bottom:8px;">
          Caption &amp; Hashtags ({len(caption)} / 2200 chars)
        </div>
        <div style="background:#020617;border:1px solid #1e293b;border-radius:10px;padding:16px;font-size:14px;line-height:1.6;color:#e2e8f0;margin-bottom:18px;">
          {caption_html}
        </div>

        <div style="font-size:12px;color:#94a3b8;line-height:1.6;border-top:1px solid #1e293b;padding-top:14px;">
          <strong>No action needed</strong> if everything looks good — this post will publish automatically to <strong>@sikhrpa</strong> on <strong>{esc(when)}</strong>.<br/>
          To pause it, click <em>Pause / Skip Post</em> above and change <code>"{esc(pid)}"</code> status from <code>"pending"</code> to <code>"paused"</code>.
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""
    return subject, plain_text, html_body


def send_email(to_email: str, subject: str, plain_text: str, html_body: str) -> str:
    """Send email via Gmail/SMTP or Resend API. Returns backend label used."""
    smtp_user = os.environ.get("SMTP_USERNAME", "").strip()
    smtp_pass = os.environ.get("SMTP_PASSWORD", "").strip()
    resend_key = os.environ.get("RESEND_API_KEY", "").strip()

    if smtp_user and smtp_pass:
        host = os.environ.get("SMTP_HOST", "smtp.gmail.com").strip() or "smtp.gmail.com"
        port = int(os.environ.get("SMTP_PORT", "465").strip() or "465")
        from_addr = os.environ.get("SMTP_FROM", f"SikhRPA Auto-Poster <{smtp_user}>").strip()

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = from_addr
        msg["To"] = to_email
        msg.set_content(plain_text)
        msg.add_alternative(html_body, subtype="html")

        context = ssl.create_default_context()
        if port == 465:
            with smtplib.SMTP_SSL(host, port, context=context, timeout=30) as server:
                server.login(smtp_user, smtp_pass)
                server.send_message(msg)
        else:
            with smtplib.SMTP(host, port, timeout=30) as server:
                server.starttls(context=context)
                server.login(smtp_user, smtp_pass)
                server.send_message(msg)
        return f"SMTP ({host}:{port})"

    if resend_key:
        from_addr = os.environ.get("RESEND_FROM", "").strip() or "SikhRPA Auto-Poster <onboarding@resend.dev>"
        payload = json.dumps({
            "from": from_addr,
            "to": [to_email],
            "subject": subject,
            "text": plain_text,
            "html": html_body,
        }).encode("utf-8")
        req = urllib.request.Request(
            "https://api.resend.com/emails",
            data=payload,
            method="POST",
            headers={
                "Authorization": f"Bearer {resend_key}",
                "Content-Type": "application/json",
                "User-Agent": "SikhRPA-AutoPoster/1.0",
            },
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status not in (200, 201):
                raise RuntimeError(f"Resend API returned HTTP {resp.status}")
        return "Resend API"

    raise RuntimeError(
        "No email credentials configured. Add SMTP_USERNAME + SMTP_PASSWORD "
        "(Google App Password) or RESEND_API_KEY in GitHub Repository Secrets."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Send 2-day advance Instagram post preview emails")
    parser.add_argument("--check-due", action="store_true", help="Send preview emails for posts scheduled in ~2 days")
    parser.add_argument("--post", type=str, default="", help="Send a preview email for a specific post (e.g. post-01 or week-01)")
    parser.add_argument("--window-hours", type=float, default=60.0, help="Look-ahead window in hours (default: 60h ≈ 2.5 days)")
    parser.add_argument("--to", type=str, default="", help=f"Override recipient email (default: {DEFAULT_TO_EMAIL})")
    parser.add_argument("--dry-run", action="store_true", help="Render preview without sending email or modifying state")
    parser.add_argument("--force", action="store_true", help="Send even if preview_sent_at is already recorded")
    args = parser.parse_args()

    manifest = load_manifest()
    state = load_state(manifest)
    to_email = (args.to or os.environ.get("PREVIEW_TO_EMAIL") or DEFAULT_TO_EMAIL).strip()

    if args.post:
        post = find_post(manifest, args.post)
        if not post:
            print(f"✗ Post '{args.post}' not found in publish_manifest.json.")
            return 1
        subject, plain, html_body = build_email_content(post)
        print(f"▶ Preview for {post['post_id']} -> {to_email}")
        print(f"  Subject: {subject}")
        if args.dry_run:
            print(f"  [DRY RUN] HTML length={len(html_body)} chars, plain length={len(plain)} chars")
            return 0
        backend = send_email(to_email, subject, plain, html_body)
        print(f"✓ Sent preview email for {post['post_id']} to {to_email} via {backend}.")
        return 0

    if args.check_due:
        now_utc = datetime.now(timezone.utc)
        horizon = now_utc + timedelta(hours=args.window_hours)
        targets = []
        for p in manifest["posts"]:
            pid = p["post_id"]
            st = state.get(pid, {})
            if st.get("status") in ("published", "paused", "skipped"):
                continue
            if st.get("preview_sent_at") and not args.force:
                continue
            sched_dt = datetime.fromisoformat(p["scheduled_at_iso"]).astimezone(timezone.utc)
            if now_utc < sched_dt <= horizon:
                targets.append(p)

        if not targets:
            print(f"✓ No upcoming posts within next {args.window_hours:.0f}h need a preview email ({now_utc.strftime('%Y-%m-%d %H:%M UTC')}).")
            return 0

        for post in targets:
            pid = post["post_id"]
            subject, plain, html_body = build_email_content(post)
            print(f"▶ Sending 2-day preview for {pid} ({post['date_display']} {post['time_pst']}) -> {to_email}")
            if args.dry_run:
                print(f"  [DRY RUN] Would send: {subject}")
                continue
            backend = send_email(to_email, subject, plain, html_body)
            print(f"  ✓ Sent via {backend}")
            state[pid]["preview_sent_at"] = datetime.now(timezone.utc).isoformat()
            save_state(state)
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
