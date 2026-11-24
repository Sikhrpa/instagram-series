#!/usr/bin/env python3
"""
SikhRPA Instagram Auto-Poster — Official Meta Instagram Graph API Client
Zero third-party dependencies (pure Python 3 standard library).

Supports:
  - Carousels (Posts 01, 02, 04, 05, 08, 09, 10, 12)
  - Reels MP4 + Cover (Posts 03, 07)
  - Single Feed Posts (Posts 06, 11)
  - Companion 9:16 Photo Stories (Posts 06, 11, 12)

Required Environment Variables (set as GitHub Repository Secrets):
  IG_USER_ID       - Instagram Business / Creator Account ID
  IG_ACCESS_TOKEN  - Long-lived Meta Access Token with instagram_basic &
                     instagram_content_publish permissions

Optional Environment Variables:
  IG_API_BASE      - Default: https://graph.facebook.com
                     (or https://graph.instagram.com for Instagram Login API)
  IG_API_VERSION   - Default: v21.0

Examples:
  python3 scripts/auto_post.py --status
  python3 scripts/auto_post.py --verify-token
  python3 scripts/auto_post.py --dry-run --post 01
  python3 scripts/auto_post.py --check-due --publish-stories
  python3 scripts/auto_post.py --post 01 --publish-stories
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT_DIR / "publish_manifest.json"
STATE_PATH = ROOT_DIR / "publish_state.json"

API_BASE = os.environ.get("IG_API_BASE", "https://graph.facebook.com").rstrip("/")
API_VERSION = os.environ.get("IG_API_VERSION", "v21.0").strip("/")


class GraphAPIError(RuntimeError):
    """Raised when Meta's Instagram Graph API returns an error response."""


def load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(
            f"{MANIFEST_PATH} not found. Run `python3 scripts/build_publish_media.py` first."
        )
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def load_state(manifest: dict) -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {
        p["post_id"]: {
            "slug": p["slug"],
            "scheduled_at_iso": p["scheduled_at_iso"],
            "status": "pending",
            "published_at": None,
            "ig_media_id": None,
            "story_media_id": None,
        }
        for p in manifest["posts"]
    }


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def api_request(method: str, endpoint: str, token: str, params: dict | None = None) -> dict:
    """Execute a GET or POST request against the Meta Instagram Graph API."""
    url = f"{API_BASE}/{API_VERSION}/{endpoint.lstrip('/')}"
    payload = dict(params or {})
    payload["access_token"] = token

    if method.upper() == "GET":
        qs = urllib.parse.urlencode(payload)
        req = urllib.request.Request(f"{url}?{qs}", method="GET")
    else:
        data = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data,
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise GraphAPIError(f"HTTP {exc.code} on {method} {endpoint}: {body}") from exc
    except urllib.error.URLError as exc:
        raise GraphAPIError(f"Network error on {method} {endpoint}: {exc}") from exc


def check_media_url_reachable(url: str) -> tuple[bool, str]:
    """Verify public HTTPS URL is reachable (HTTP 200) before sending to Meta."""
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "SikhRPA-AutoPoster/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            ctype = resp.headers.get("Content-Type", "unknown")
            clen = resp.headers.get("Content-Length", "?")
            return (resp.status == 200, f"HTTP {resp.status} ({ctype}, {clen} bytes)")
    except urllib.error.HTTPError as exc:
        return (False, f"HTTP {exc.code}")
    except urllib.error.URLError as exc:
        return (False, str(exc))


def wait_for_container(container_id: str, token: str, *, is_video: bool = False) -> None:
    """Poll Meta media container until status_code is FINISHED (or PUBLISHED)."""
    max_wait = 240 if is_video else 90
    interval = 6 if is_video else 3
    deadline = time.time() + max_wait

    while time.time() < deadline:
        res = api_request("GET", container_id, token, {"fields": "status_code,status"})
        code = (res.get("status_code") or "").upper()
        if code in ("FINISHED", "PUBLISHED"):
            return
        if code in ("ERROR", "EXPIRED"):
            raise GraphAPIError(f"Container {container_id} failed with status={res}")
        print(f"    ⏳ Container {container_id} status={code or 'IN_PROGRESS'}... waiting {interval}s")
        time.sleep(interval)

    raise GraphAPIError(f"Timed out after {max_wait}s waiting for container {container_id} to finish.")


def publish_container(ig_user_id: str, creation_id: str, token: str) -> str:
    res = api_request("POST", f"{ig_user_id}/media_publish", token, {"creation_id": creation_id})
    media_id = res.get("id")
    if not media_id:
        raise GraphAPIError(f"media_publish returned unexpected response: {res}")
    return str(media_id)


def publish_post(
    post: dict,
    ig_user_id: str,
    token: str,
    *,
    publish_stories: bool = True,
    dry_run: bool = False,
) -> tuple[str | None, str | None]:
    """Publish a single Post (carousel, reel, or single + optional Story)."""
    ptype = post["publish_type"]
    caption = post["caption_full"]
    print(f"\n▶ Post {post['post_number']:02d} [{ptype.upper()}] — {post['title']}")
    print(f"  Scheduled: {post['date_display']} {post['time_pst']} ({post['scheduled_at_iso']})")
    print(f"  Caption length: {len(caption)} / 2200 chars")

    # Pre-flight URL verification
    urls_to_check = list(post["media_urls"])
    if post.get("cover_url"):
        urls_to_check.append(post["cover_url"])
    if publish_stories and post.get("story_url"):
        urls_to_check.append(post["story_url"])

    all_ok = True
    for u in urls_to_check:
        ok, detail = check_media_url_reachable(u)
        mark = "✓" if ok else "✗"
        print(f"  [{mark}] URL check: {u.split('/')[-1]} -> {detail}")
        if not ok:
            all_ok = False

    if dry_run:
        print("  [DRY RUN] Payload validated — skipping live Instagram Graph API publish.")
        if not all_ok:
            print("  ⚠ Note: Push media/jpg and media/reels to GitHub main so raw URLs return HTTP 200.")
        return ("DRY_RUN_MEDIA_ID", "DRY_RUN_STORY_ID" if (publish_stories and post.get("story_url")) else None)

    if not all_ok:
        raise GraphAPIError(
            "One or more public media URLs are not reachable (HTTP 200). "
            "Ensure the latest media/jpg and media/reels files are pushed to GitHub main."
        )

    # 1. Publish main feed post (Carousel / Reel / Single)
    if ptype == "carousel":
        child_ids: list[str] = []
        for idx, img_url in enumerate(post["media_urls"], start=1):
            print(f"  Creating carousel item {idx}/{len(post['media_urls'])}: {img_url.split('/')[-1]}")
            c_res = api_request(
                "POST",
                f"{ig_user_id}/media",
                token,
                {"image_url": img_url, "is_carousel_item": "true"},
            )
            cid = str(c_res["id"])
            wait_for_container(cid, token, is_video=False)
            child_ids.append(cid)

        print(f"  Creating parent CAROUSEL container ({len(child_ids)} items)...")
        parent_res = api_request(
            "POST",
            f"{ig_user_id}/media",
            token,
            {
                "media_type": "CAROUSEL",
                "children": ",".join(child_ids),
                "caption": caption,
            },
        )
        parent_id = str(parent_res["id"])
        wait_for_container(parent_id, token, is_video=False)
        media_id = publish_container(ig_user_id, parent_id, token)
        print(f"  ✓ Published Carousel! IG Media ID: {media_id}")

    elif ptype == "reel":
        print(f"  Creating REELS container ({post['video_url'].split('/')[-1]})...")
        params = {
            "media_type": "REELS",
            "video_url": post["video_url"],
            "caption": caption,
            "share_to_feed": "true",
        }
        if post.get("cover_url"):
            params["cover_url"] = post["cover_url"]
        r_res = api_request("POST", f"{ig_user_id}/media", token, params)
        rid = str(r_res["id"])
        wait_for_container(rid, token, is_video=True)
        media_id = publish_container(ig_user_id, rid, token)
        print(f"  ✓ Published Reel! IG Media ID: {media_id}")

    elif ptype == "single":
        img_url = post["media_urls"][0]
        print(f"  Creating single photo container ({img_url.split('/')[-1]})...")
        s_res = api_request(
            "POST",
            f"{ig_user_id}/media",
            token,
            {"image_url": img_url, "caption": caption},
        )
        sid = str(s_res["id"])
        wait_for_container(sid, token, is_video=False)
        media_id = publish_container(ig_user_id, sid, token)
        print(f"  ✓ Published Photo Post! IG Media ID: {media_id}")
    else:
        raise ValueError(f"Unsupported publish_type: {ptype}")

    # 2. Publish companion 9:16 Story if configured
    story_media_id: str | None = None
    if publish_stories and post.get("story_url"):
        story_url = post["story_url"]
        print(f"  Creating companion 9:16 STORIES container ({story_url.split('/')[-1]})...")
        st_res = api_request(
            "POST",
            f"{ig_user_id}/media",
            token,
            {"media_type": "STORIES", "image_url": story_url},
        )
        stid = str(st_res["id"])
        wait_for_container(stid, token, is_video=False)
        story_media_id = publish_container(ig_user_id, stid, token)
        print(f"  ✓ Published Companion Story! IG Story ID: {story_media_id}")

    return (media_id, story_media_id)


def print_status(manifest: dict, state: dict) -> None:
    now_utc = datetime.now(timezone.utc)
    print(f"\nSikhRPA Instagram Auto-Post Schedule (Current UTC: {now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')})")
    print("-" * 108)
    print(f"{'Post':<8} {'Scheduled (PST)':<26} {'Type':<10} {'Story':<6} {'Status':<11} {'IG Media ID'}")
    print("-" * 108)
    for p in manifest["posts"]:
        st = state.get(p["post_id"], {})
        status = st.get("status", "pending")
        due_dt = datetime.fromisoformat(p["scheduled_at_iso"]).astimezone(timezone.utc)
        due_flag = " (DUE)" if (status != "published" and now_utc >= due_dt) else ""
        has_story = "Yes" if p.get("story_url") else "No"
        mid = st.get("ig_media_id") or "-"
        print(
            f"{p['post_id']:<8} {p['scheduled_at_iso']:<26} {p['publish_type'].upper():<10} "
            f"{has_story:<6} {(status + due_flag):<11} {mid}"
        )
    print("-" * 108)


def verify_token(ig_user_id: str, token: str) -> int:
    print(f"Verifying credentials against {API_BASE}/{API_VERSION}/{ig_user_id} ...")
    res = api_request("GET", ig_user_id, token, {"fields": "id,username,name,followers_count,media_count"})
    print("✓ Instagram Graph API credentials verified!")
    print(json.dumps(res, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="SikhRPA Instagram Graph API Auto-Poster")
    parser.add_argument("--status", action="store_true", help="Show publish status of all 12 posts")
    parser.add_argument("--verify-token", action="store_true", help="Verify IG_USER_ID and IG_ACCESS_TOKEN")
    parser.add_argument("--check-due", action="store_true", help="Publish all pending posts whose scheduled time has arrived")
    parser.add_argument("--post", type=str, default="", help="Publish a specific post number (e.g. 01 or 1)")
    parser.add_argument("--dry-run", action="store_true", help="Validate URLs & payloads without publishing")
    parser.add_argument("--publish-stories", action="store_true", help="Also auto-publish companion 9:16 Stories")
    parser.add_argument("--force", action="store_true", help="Allow re-publishing a post already marked published")
    args = parser.parse_args()

    manifest = load_manifest()
    state = load_state(manifest)

    if args.status:
        print_status(manifest, state)
        return 0

    ig_user_id = os.environ.get("IG_USER_ID", "").strip()
    token = os.environ.get("IG_ACCESS_TOKEN", "").strip()

    if args.verify_token:
        if not ig_user_id or not token:
            print("✗ Missing IG_USER_ID or IG_ACCESS_TOKEN environment variables.")
            return 1
        return verify_token(ig_user_id, token)

    if args.post:
        target_num = int(args.post.strip().lstrip("0") or "0")
        matches = [p for p in manifest["posts"] if p["post_number"] == target_num]
        if not matches:
            print(f"✗ Post {args.post} not found in publish_manifest.json (valid: 01–12).")
            return 1
        post = matches[0]
        pid = post["post_id"]
        if state.get(pid, {}).get("status") == "published" and not args.force and not args.dry_run:
            print(f"ℹ {pid} is already marked published (IG Media ID: {state[pid].get('ig_media_id')}). Pass --force to re-publish.")
            return 0
        if not args.dry_run and (not ig_user_id or not token):
            print("✗ Missing IG_USER_ID or IG_ACCESS_TOKEN. See AUTO_POST_SETUP.md.")
            return 1
        media_id, story_id = publish_post(
            post, ig_user_id, token, publish_stories=args.publish_stories, dry_run=args.dry_run
        )
        if not args.dry_run:
            state[pid] = {
                "slug": post["slug"],
                "scheduled_at_iso": post["scheduled_at_iso"],
                "status": "published",
                "published_at": datetime.now(timezone.utc).isoformat(),
                "ig_media_id": media_id,
                "story_media_id": story_id,
            }
            save_state(state)
        return 0

    if args.check_due:
        now_utc = datetime.now(timezone.utc)
        due_posts = []
        for p in manifest["posts"]:
            pid = p["post_id"]
            if state.get(pid, {}).get("status") == "published":
                continue
            sched_dt = datetime.fromisoformat(p["scheduled_at_iso"]).astimezone(timezone.utc)
            if now_utc >= sched_dt:
                due_posts.append(p)

        if not due_posts:
            print(f"✓ No posts due right now ({now_utc.strftime('%Y-%m-%d %H:%M UTC')}). Next pending post:")
            for p in manifest["posts"]:
                if state.get(p["post_id"], {}).get("status") != "published":
                    print(f"  -> {p['post_id']} ({p['date_display']} • {p['time_pst']}): {p['title']}")
                    break
            return 0

        if not args.dry_run and (not ig_user_id or not token):
            print(
                "⚠ Posts are due, but IG_USER_ID / IG_ACCESS_TOKEN secrets are not configured yet.\n"
                "  Add IG_USER_ID and IG_ACCESS_TOKEN in GitHub Repo Settings -> Secrets -> Actions.\n"
                "  See AUTO_POST_SETUP.md for the 5-minute setup guide."
            )
            return 0

        for post in due_posts:
            pid = post["post_id"]
            media_id, story_id = publish_post(
                post, ig_user_id, token, publish_stories=args.publish_stories, dry_run=args.dry_run
            )
            if not args.dry_run:
                state[pid] = {
                    "slug": post["slug"],
                    "scheduled_at_iso": post["scheduled_at_iso"],
                    "status": "published",
                    "published_at": datetime.now(timezone.utc).isoformat(),
                    "ig_media_id": media_id,
                    "story_media_id": story_id,
                }
                save_state(state)
                # Brief pause between posts if multiple caught up at once
                time.sleep(5)
        return 0

    if args.dry_run:
        # Validate all 12 posts in dry-run mode
        for post in manifest["posts"]:
            publish_post(post, ig_user_id, token, publish_stories=args.publish_stories, dry_run=True)
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
