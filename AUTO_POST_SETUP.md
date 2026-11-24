# Auto-Posting Setup Guide — SikhRPA Instagram Series

This repository is pre-configured for **100% automated posting** to Instagram (`@sikhrpa`) across all 12 scheduled slots (Dec 1 – Dec 26, 2026), including:
- **Carousels** (Posts 01, 02, 04, 05, 08, 09, 10, 12) — pre-converted to Meta-required sRGB JPEGs under `media/jpg/`
- **Reels** (Posts 03 & 07) — pre-compiled into 1080×1920 H.264/AAC MP4 videos under `media/reels/` with custom covers
- **Single Feed Posts** (Posts 06 & 11) + **Companion 9:16 Stories** (Posts 06, 11, 12)
- **Duplicate Protection** — `publish_state.json` is automatically updated and committed back to `main` after each post publishes

---

## Option A: Free Automated Publishing via GitHub Actions (Recommended)

Because `Sikhrpa/instagram-series` is a public GitHub repository, Meta's official **Instagram Graph API** fetches the JPEGs and MP4 Reels directly from `raw.githubusercontent.com` — **zero hosting fees, zero third-party SaaS subscriptions**.

### Step 1: Confirm Your Instagram Account Setup (1 minute)
1. In the Instagram app, ensure `@sikhrpa` is switched to a **Professional Account** (**Business** or **Creator**).
2. Link `@sikhrpa` to your official **SikhRPA Facebook Page** (Instagram Settings → *Account Center* / *Sharing across profiles*, or Facebook Page Settings → *Linked Accounts → Instagram*).

### Step 2: Create a Meta App & Get Your Credentials (3 minutes)
1. Go to [developers.facebook.com](https://developers.facebook.com/) → **My Apps → Create App** → choose **Other → Business** (or **Manage messaging & content on Instagram**).
2. Open the **Graph API Explorer** (`Tools → Graph API Explorer`):
   - Select your app and click **Generate Access Token** with these permissions:
     - `instagram_basic`
     - `instagram_content_publish`
     - `pages_show_list`
     - `pages_read_engagement`
3. Find your **`IG_USER_ID`**:
   - In Graph API Explorer, query `GET /me/accounts?fields=name,instagram_business_account`
   - Copy the numeric `instagram_business_account.id` (e.g., `17841400000000000`) — this is your **`IG_USER_ID`**.
4. Exchange your short-lived token for a **60-Day Long-Lived Access Token** (or generate a never-expiring System User Token in Meta Business Manager → *Business Settings → System Users*):
   - In Meta's [Access Token Debugger](https://developers.facebook.com/tools/debug/accesstoken/), click **Extend Access Token** → copy the resulting long-lived token as **`IG_ACCESS_TOKEN`**.

### Step 3: Add Two Secrets to GitHub (30 seconds)
In this repository, go to **Settings → Secrets and variables → Actions → New repository secret** and add:

| Secret Name | Value |
|---|---|
| `IG_USER_ID` | Your numeric Instagram Business/Creator Account ID |
| `IG_ACCESS_TOKEN` | Your long-lived Meta Graph API Access Token |

*(Optional: If you use Meta's direct Instagram Login API instead of Facebook Login, add a Repository Variable `IG_API_BASE` = `https://graph.instagram.com` under Settings → Secrets and variables → Actions → Variables.)*

### Step 4: Verify & Test Before Dec 1 (30 seconds)
Go to the **Actions** tab → **Auto-Post SikhRPA Instagram Series** → **Run workflow**:
1. Run `mode: verify_token` → confirms `@sikhrpa` username & API access.
2. Run `mode: dry_run` → verifies all 12 posts, captions (≤ 2,200 chars), and live HTTP 200 reachability of every JPEG & MP4 URL without posting anything.
3. Want to test or publish one post on demand? Choose `mode: single_post` and enter `post_number: 01`.

### Step 5: Hands-Off Automated Schedule
The workflow `.github/workflows/auto-post-instagram.yml` runs automatically every 30 minutes throughout December:
- Whenever current time ≥ a pending post's scheduled PST timestamp in `publish_manifest.json`, it publishes the Carousel / Reel / Photo (+ optional companion 9:16 Story) and commits the resulting Instagram Media ID into `publish_state.json`.
- **Interactive Story Stickers Note:** Meta's Graph API publishes photo Stories cleanly, but does not allow adding native interactive stickers (Questions, Polls, Link Stickers, Countdowns) via API. If you want to add interactive stickers manually on Posts 06, 11, or 12, simply set `publish_stories: false` (or edit `story_url` to `null` in `publish_manifest.json`) and upload the 9:16 PNGs from your phone!

---

## Option B: Zero-Code UI Scheduler (Meta Business Suite / Buffer / Later / Make.com)

Prefer a drag-and-drop calendar without setting up a Meta Developer App?
- **Meta Business Suite (100% Free):** Open [business.facebook.com](https://business.facebook.com) → **Planner → Create Post**, upload slides from `posts/post-XX-.../` (or MP4s from `media/reels/`), paste copy from `caption.txt` or `index.html`, and schedule each Tue/Thu/Sat PST slot.
- **Buffer / Later / Make.com / Zapier:** Import [`schedule.csv`](schedule.csv), which already includes the `ISO Timestamp (PST)`, `Graph API Type`, `Public HTTPS Media URLs` (direct GitHub Raw `.jpg` and `.mp4` links), `Companion Story URL`, and `Caption + Hashtags`.

---

## Regenerating Publish Media After Copy Edits

If you edit any slide text or captions in `scripts/content_posts_*.py`:

```bash
python3 scripts/generate_all.py          # Re-render all 65 PNGs + caption.txt + index.html
python3 scripts/build_publish_media.py   # Rebuild media/jpg/, media/reels/*.mp4, publish_manifest.json & schedule.csv
```
