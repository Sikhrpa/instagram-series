#!/usr/bin/env python3
"""
SikhRPA Instagram Auto-Poster — Official Meta Instagram Graph API Client
Zero third-party dependencies (pure Python 3 standard library).

Supports:
  - Dec 2026 Launch Series (post-01 .. post-12: Carousels, Reels MP4, Single + Stories)
  - 2027 Full-Year Weekly Series (week-01 .. week-52: 4:5 Photo + Companion 9:16 Story)
  - Both Meta Instagram Login / Unified Login (no Facebook Page required) and Facebook Login

Required Environment Variable (GitHub Repository Secret):
  IG_ACCESS_TOKEN  - Meta Access Token (Instagram Login IGAA... or Unified/Facebook EAA...)

Optional Environment Variables:
  IG_USER_ID       - Numeric Instagram Business/Creator Account ID (auto-detected if omitted)
  IG_API_BASE      - Auto-detected from token prefix if omitted:
                     IG* -> https://graph.instagram.com
                     EAA* -> https://graph.facebook.com
  IG_API_VERSION   - Default: v21.0

Examples:
  python3 scripts/auto_post.py --status
  python3 scripts/auto_post.py --verify-token
  python3 scripts/auto_post.py --dry-run --post post-01
  python3 scripts/auto_post.py --check-due --publish-stories
  python3 scripts/auto_post.py --post week-01 --publish-stories
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

API_VERSION = os.environ.get("IG_API_VERSION", "v21.0").strip("/")


class GraphAPIError(RuntimeError):
    """Raised when Meta's Instagram Graph API returns an error response."""


def resolve_api_base(token: str) -> str:
    explicit = os.environ.get("IG_API_BASE", "").strip().rstrip("/")
    if explicit:
        return explicit
    if token.startswith("IG"):
        return "https://graph.instagram.com"
    return "https://graph.facebook.com"


def load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(
            f"{MANIFEST_PATH} not found. Run `python3 scripts/build_publish_media.py` first."
        )
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


def api_request(
    method: str,
    endpoint: str,
    token: str,
    params: dict | None = None,
    *,
    api_base: str | None = None,
) -> dict:
    """Execute a GET or POST request against the Meta Instagram Graph API."""
    base = (api_base or resolve_api_base(token)).rstrip("/")
    url = f"{base}/{API_VERSION}/{endpoint.lstrip('/')}"
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


def resolve_ig_account(ig_user_id: str, token: str) -> tuple[str, str, dict]:
    """
    Resolve (ig_user_id, api_base, profile_dict) from IG_USER_ID + IG_ACCESS_TOKEN.
    Supports Instagram Login (graph.instagram.com), Unified Login, and Facebook Login.
    """
    candidates = [resolve_api_base(token)]
    other = "https://graph.instagram.com" if "facebook" in candidates[0] else "https://graph.facebook.com"
    if not os.environ.get("IG_API_BASE", "").strip():
        candidates.append(other)

    last_err: Exception | None = None

    for base in candidates:
        # 1. If IG_USER_ID was provided explicitly, verify it directly
        if ig_user_id:
            try:
                res = api_request("GET", ig_user_id, token, {"fields": "id,username,name,media_count"}, api_base=base)
                if res.get("id"):
                    return (str(res["id"]), base, res)
            except GraphAPIError as exc:
                last_err = exc

        # 2. Try /me on graph.instagram.com (Instagram Login / Unified Login)
        try:
            me = api_request("GET", "me", token, {"fields": "user_id,id,username,name,account_type"}, api_base=base)
            uid = me.get("user_id") or me.get("id")
            if uid and (me.get("username") or "instagram.com" in base):
                return (str(uid), base, me)
        except GraphAPIError as exc:
            last_err = exc

        # 3. Try /me/accounts (Facebook Login / Business Portfolio linked Page)
        if "facebook.com" in base:
            try:
                accts = api_request(
                    "GET",
                    "me/accounts",
                    token,
                    {"fields": "name,instagram_business_account{id,username,name}"},
                    api_base=base,
                )
                for page in accts.get("data", []):
                    ig = page.get("instagram_business_account")
                    if ig and ig.get("id"):
                        return (str(ig["id"]), base, ig)
            except GraphAPIError as exc:
                last_err = exc

            # 4. Try Unified Login /me/instagram_accounts or /me/assigned_instagram_accounts
            for edge in ("me/instagram_accounts", "me/assigned_instagram_accounts"):
                try:
                    ig_list = api_request("GET", edge, token, {"fields": "id,username,name"}, api_base=base)
                    data = ig_list.get("data", [])
                    if data and data[0].get("id"):
                        return (str(data[0]["id"]), base, data[0])
                except GraphAPIError as exc:
                    last_err = exc

    raise GraphAPIError(
        "Could not resolve an Instagram Business/Creator Account ID from IG_ACCESS_TOKEN. "
        "Try also setting the IG_USER_ID repository secret to your numeric Instagram Account ID. "
        f"Last API error: {last_err}"
    )


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


def wait_for_container(container_id: str, token: str, *, api_base: str, is_video: bool = False) -> None:
    """Poll Meta media container until status_code is FINISHED (or PUBLISHED)."""
    max_wait = 240 if is_video else 90
    interval = 6 if is_video else 3
    deadline = time.time() + max_wait

    while time.time() < deadline:
        res = api_request("GET", container_id, token, {"fields": "status_code,status"}, api_base=api_base)
        code = (res.get("status_code") or "").upper()
        if code in ("FINISHED", "PUBLISHED"):
            return
        if code in ("ERROR", "EXPIRED"):
            raise GraphAPIError(f"Container {container_id} failed with status={res}")
        print(f"    ⏳ Container {container_id} status={code or 'IN_PROGRESS'}... waiting {interval}s")
        time.sleep(interval)

    raise GraphAPIError(f"Timed out after {max_wait}s waiting for container {container_id} to finish.")


def publish_container(ig_user_id: str, creation_id: str, token: str, *, api_base: str) -> str:
    res = api_request("POST", f"{ig_user_id}/media_publish", token, {"creation_id": creation_id}, api_base=api_base)
    media_id = res.get("id")
    if not media_id:
        raise GraphAPIError(f"media_publish returned unexpected response: {res}")
    return str(media_id)


def publish_post(
    post: dict,
    ig_user_id: str,
    token: str,
    *,
    api_base: str,
    publish_stories: bool = True,
    dry_run: bool = False,
) -> tuple[str | None, str | None]:
    """Publish a single Post (carousel, reel, or single + optional Story)."""
    ptype = post["publish_type"]
    caption = post["caption_full"]
    print(f"\n▶ {post['post_id']} [{ptype.upper()}] — {post['title']}")
    print(f"  Scheduled: {post['date_display']} {post['time_pst']} ({post['scheduled_at_iso']})")
    print(f"  Caption length: {len(caption)} / 2200 chars")

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

    if ptype == "carousel":
        child_ids: list[str] = []
        for idx, img_url in enumerate(post["media_urls"], start=1):
            print(f"  Creating carousel item {idx}/{len(post['media_urls'])}: {img_url.split('/')[-1]}")
            c_res = api_request(
                "POST",
                f"{ig_user_id}/media",
                token,
                {"image_url": img_url, "is_carousel_item": "true"},
                api_base=api_base,
            )
            cid = str(c_res["id"])
            wait_for_container(cid, token, api_base=api_base, is_video=False)
            child_ids.append(cid)

        print(f"  Creating parent CAROUSEL container ({len(child_ids)} items)...")
        parent_res = api_request(
            "POST",
            f"{ig_user_id}/media",
            token,
            {"media_type": "CAROUSEL", "children": ",".join(child_ids), "caption": caption},
            api_base=api_base,
        )
        parent_id = str(parent_res["id"])
        wait_for_container(parent_id, token, api_base=api_base, is_video=False)
        media_id = publish_container(ig_user_id, parent_id, token, api_base=api_base)
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
        r_res = api_request("POST", f"{ig_user_id}/media", token, params, api_base=api_base)
        rid = str(r_res["id"])
        wait_for_container(rid, token, api_base=api_base, is_video=True)
        media_id = publish_container(ig_user_id, rid, token, api_base=api_base)
        print(f"  ✓ Published Reel! IG Media ID: {media_id}")

    elif ptype == "single":
        img_url = post["media_urls"][0]
        print(f"  Creating single photo container ({img_url.split('/')[-1]})...")
        s_res = api_request(
            "POST",
            f"{ig_user_id}/media",
            token,
            {"image_url": img_url, "caption": caption},
            api_base=api_base,
        )
        sid = str(s_res["id"])
        wait_for_container(sid, token, api_base=api_base, is_video=False)
        media_id = publish_container(ig_user_id, sid, token, api_base=api_base)
        print(f"  ✓ Published Photo Post! IG Media ID: {media_id}")

    elif ptype == "story":
        story_img_url = post["media_urls"][0]
        print(f"  Creating standalone 9:16 STORIES container ({story_img_url.split('/')[-1]})...")
        st_res = api_request(
            "POST",
            f"{ig_user_id}/media",
            token,
            {"media_type": "STORIES", "image_url": story_img_url},
            api_base=api_base,
        )
        stid = str(st_res["id"])
        wait_for_container(stid, token, api_base=api_base, is_video=False)
        media_id = publish_container(ig_user_id, stid, token, api_base=api_base)
        print(f"  ✓ Published Standalone Story! IG Story ID: {media_id}")
        return (media_id, media_id)
    else:
        raise ValueError(f"Unsupported publish_type: {ptype}")

    story_media_id: str | None = None
    if publish_stories and post.get("story_url"):
        story_url = post["story_url"]
        print(f"  Creating companion 9:16 STORIES container ({story_url.split('/')[-1]})...")
        st_res = api_request(
            "POST",
            f"{ig_user_id}/media",
            token,
            {"media_type": "STORIES", "image_url": story_url},
            api_base=api_base,
        )
        stid = str(st_res["id"])
        wait_for_container(stid, token, api_base=api_base, is_video=False)
        story_media_id = publish_container(ig_user_id, stid, token, api_base=api_base)
        print(f"  ✓ Published Companion Story! IG Story ID: {story_media_id}")

    return (media_id, story_media_id)


def find_post(manifest: dict, selector: str) -> dict | None:
    sel = selector.strip().lower()
    for p in manifest["posts"]:
        if p["post_id"].lower() == sel or p["slug"].lower() == sel:
            return p
    if sel.isdigit():
        target_num = int(sel)
        for p in manifest["posts"]:
            if p.get("post_number") == target_num and p["post_id"].startswith("post-"):
                return p
    return None


def print_status(manifest: dict, state: dict) -> None:
    now_utc = datetime.now(timezone.utc)
    print(f"\nSikhRPA Instagram Auto-Post Schedule ({len(manifest['posts'])} posts • UTC: {now_utc.strftime('%Y-%m-%d %H:%M UTC')})")
    print("-" * 112)
    print(f"{'Post ID':<10} {'Scheduled (PT)':<26} {'Type':<10} {'Story':<6} {'Status':<11} {'IG Media ID'}")
    print("-" * 112)
    for p in manifest["posts"]:
        st = state.get(p["post_id"], {})
        status = st.get("status", "pending")
        due_dt = datetime.fromisoformat(p["scheduled_at_iso"]).astimezone(timezone.utc)
        due_flag = " (DUE)" if (status != "published" and now_utc >= due_dt) else ""
        has_story = "Yes" if p.get("story_url") else "No"
        mid = st.get("ig_media_id") or "-"
        print(
            f"{p['post_id']:<10} {p['scheduled_at_iso']:<26} {p['publish_type'].upper():<10} "
            f"{has_story:<6} {(status + due_flag):<11} {mid}"
        )
    print("-" * 112)


def verify_token_cmd(ig_user_id: str, token: str) -> int:
    uid, base, profile = resolve_ig_account(ig_user_id, token)
    print(f"✓ Instagram API credentials verified via {base}/{API_VERSION}!")
    print(f"  Resolved IG_USER_ID: {uid}")
    print(json.dumps(profile, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="SikhRPA Instagram Graph API Auto-Poster")
    parser.add_argument("--status", action="store_true", help="Show publish status of all scheduled posts")
    parser.add_argument("--verify-token", action="store_true", help="Verify IG_ACCESS_TOKEN (and resolve IG_USER_ID)")
    parser.add_argument("--check-due", action="store_true", help="Publish all pending posts whose scheduled time has arrived")
    parser.add_argument("--post", type=str, default="", help="Publish a specific post (e.g. 01, post-01, or week-01)")
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
        if not token:
            print("✗ Missing IG_ACCESS_TOKEN environment variable.")
            return 1
        return verify_token_cmd(ig_user_id, token)

    if args.post:
        post = find_post(manifest, args.post)
        if not post:
            print(f"✗ Post '{args.post}' not found in publish_manifest.json (use 01-12, post-01..post-12, or week-01..week-52).")
            return 1
        pid = post["post_id"]
        if state.get(pid, {}).get("status") == "published" and not args.force and not args.dry_run:
            print(f"ℹ {pid} is already marked published (IG Media ID: {state[pid].get('ig_media_id')}). Pass --force to re-publish.")
            return 0
        if args.dry_run:
            publish_post(post, ig_user_id, token, api_base=resolve_api_base(token), publish_stories=args.publish_stories, dry_run=True)
            return 0
        if not token:
            print("✗ Missing IG_ACCESS_TOKEN. See AUTO_POST_SETUP.md.")
            return 1
        uid, api_base, _ = resolve_ig_account(ig_user_id, token)
        media_id, story_id = publish_post(
            post, uid, token, api_base=api_base, publish_stories=args.publish_stories, dry_run=False
        )
        prev_entry = state.get(pid, {})
        state[pid] = {
            **prev_entry,
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
            if state.get(pid, {}).get("status") in ("published", "paused", "skipped"):
                continue
            sched_dt = datetime.fromisoformat(p["scheduled_at_iso"]).astimezone(timezone.utc)
            if now_utc >= sched_dt:
                due_posts.append(p)

        if not due_posts:
            print(f"✓ No posts due right now ({now_utc.strftime('%Y-%m-%d %H:%M UTC')}). Next pending post:")
            for p in manifest["posts"]:
                if state.get(p["post_id"], {}).get("status") not in ("published", "paused", "skipped"):
                    print(f"  -> {p['post_id']} ({p['date_display']} • {p['time_pst']}): {p['title']}")
                    break
            return 0

        if not args.dry_run and not token:
            print(
                "⚠ Posts are due, but IG_ACCESS_TOKEN secret is not configured yet.\n"
                "  Add IG_ACCESS_TOKEN in GitHub Repo Settings -> Secrets -> Actions."
            )
            return 0

        uid, api_base = ig_user_id, resolve_api_base(token)
        if not args.dry_run:
            uid, api_base, _ = resolve_ig_account(ig_user_id, token)

        for post in due_posts:
            pid = post["post_id"]
            media_id, story_id = publish_post(
                post, uid, token, api_base=api_base, publish_stories=args.publish_stories, dry_run=args.dry_run
            )
            if not args.dry_run:
                prev_entry = state.get(pid, {})
                state[pid] = {
                    **prev_entry,
                    "slug": post["slug"],
                    "scheduled_at_iso": post["scheduled_at_iso"],
                    "status": "published",
                    "published_at": datetime.now(timezone.utc).isoformat(),
                    "ig_media_id": media_id,
                    "story_media_id": story_id,
                }
                save_state(state)
                time.sleep(5)
        return 0

    if args.dry_run:
        for post in manifest["posts"]:
            publish_post(post, ig_user_id, token, api_base=resolve_api_base(token), publish_stories=args.publish_stories, dry_run=True)
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
