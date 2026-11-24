#!/usr/bin/env python3
"""
Build Instagram Graph API-ready publish media from the rendered PNGs:
  1. Converts all 65 PNGs -> sRGB JPEGs (quality=94) under media/jpg/<slug>/
     (Instagram Graph API strictly requires JPEG for image_url containers.)
  2. Compiles 1080x1920 H.264/AAC MP4 Reels videos for Posts 03 & 07 under
     media/reels/<slug>.mp4 with smooth crossfade transitions.
  3. Writes publish_manifest.json (single source of truth for auto_post.py),
     initializes publish_state.json (preserving existing published entries),
     and updates schedule.csv with public GitHub Raw HTTPS URLs.

Usage:
    python3 scripts/build_publish_media.py
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from content_posts_1_to_6 import get_posts_1_to_6  # noqa: E402
from content_posts_7_to_12 import get_posts_7_to_12  # noqa: E402
from styles import ROOT_DIR  # noqa: E402

RAW_BASE_URL = "https://raw.githubusercontent.com/Sikhrpa/instagram-series/main"
POSTS_DIR = ROOT_DIR / "posts"
MEDIA_JPG_DIR = ROOT_DIR / "media" / "jpg"
MEDIA_REELS_DIR = ROOT_DIR / "media" / "reels"
MANIFEST_PATH = ROOT_DIR / "publish_manifest.json"
STATE_PATH = ROOT_DIR / "publish_state.json"

TIME_MAP = {
    "10:00 AM PST": "10:00:00-08:00",
    "10:30 AM PST": "10:30:00-08:00",
    "11:00 AM PST": "11:00:00-08:00",
    "12:00 PM PST": "12:00:00-08:00",
    "4:00 PM PST": "16:00:00-08:00",
    "5:30 PM PST": "17:30:00-08:00",
    "6:00 PM PST": "18:00:00-08:00",
}


def convert_png_to_jpg(src_png: Path, dst_jpg: Path) -> None:
    dst_jpg.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src_png) as img:
        rgb = img.convert("RGB")
        rgb.save(dst_jpg, format="JPEG", quality=94, optimize=True, subsampling=0)


def compile_reel_mp4(frame_pngs: list[Path], out_mp4: Path, sec_per_frame: float = 5.0, fade: float = 0.5) -> None:
    """
    Compile 5 vertical 1080x1920 storyboard PNGs into an Instagram-Reels-compliant
    H.264 / yuv420p / 30fps MP4 with smooth crossfades and a silent AAC audio track.
    """
    out_mp4.parent.mkdir(parents=True, exist_ok=True)
    n = len(frame_pngs)
    assert n >= 2, "Need at least 2 frames to compile a Reel"

    # Total duration with n frames and (n-1) crossfades of length `fade`
    total_dur = n * sec_per_frame - (n - 1) * fade

    cmd = ["ffmpeg", "-y"]
    for png in frame_pngs:
        cmd += ["-loop", "1", "-t", f"{sec_per_frame:.2f}", "-i", str(png)]
    # Silent stereo 48kHz audio track (Instagram Reels prefers an AAC audio stream)
    cmd += ["-f", "lavfi", "-t", f"{total_dur:.2f}", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000"]

    filter_parts = []
    for i in range(n):
        filter_parts.append(f"[{i}:v]fps=30,format=yuv420p,setsar=1[v{i}]")

    prev = "v0"
    for i in range(1, n):
        offset = i * (sec_per_frame - fade)
        nxt = f"xf{i}" if i < n - 1 else "vout"
        filter_parts.append(
            f"[{prev}][v{i}]xfade=transition=fade:duration={fade:.2f}:offset={offset:.2f}[{nxt}]"
        )
        prev = nxt

    filter_complex = ";".join(filter_parts)
    cmd += [
        "-filter_complex", filter_complex,
        "-map", "[vout]",
        "-map", f"{n}:a",
        "-c:v", "libx264",
        "-profile:v", "high",
        "-level", "4.1",
        "-pix_fmt", "yuv420p",
        "-crf", "22",
        "-preset", "medium",
        "-r", "30",
        "-c:a", "aac",
        "-b:a", "128k",
        "-ar", "48000",
        "-movflags", "+faststart",
        "-shortest",
        str(out_mp4),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def build_all() -> None:
    posts = get_posts_1_to_6() + get_posts_7_to_12()
    manifest_posts = []

    # Load existing publish_state.json so we never reset already-published records
    existing_state: dict = {}
    if STATE_PATH.exists():
        existing_state = json.loads(STATE_PATH.read_text(encoding="utf-8"))

    new_state: dict = {}
    jpg_count = 0
    reel_count = 0

    for post in posts:
        slug = post["slug"]
        num = post["number"]
        post_png_dir = POSTS_DIR / slug
        post_jpg_dir = MEDIA_JPG_DIR / slug

        # 1. Convert all PNGs for this post to JPEGs
        jpg_map: dict[str, Path] = {}
        for slide in post["slides"]:
            png_name = slide["filename"]
            jpg_name = Path(png_name).with_suffix(".jpg").name
            src_png = post_png_dir / png_name
            dst_jpg = post_jpg_dir / jpg_name
            convert_png_to_jpg(src_png, dst_jpg)
            jpg_map[png_name] = dst_jpg
            jpg_count += 1

        # 2. Classify Graph API publish payload for this post
        iso_time = TIME_MAP.get(post["time_pst"], "12:00:00-08:00")
        scheduled_iso = f"{post['date_iso']}T{iso_time}"
        caption_full = f"{post['caption']}\n\n{post['hashtags']}"
        assert len(caption_full) <= 2200, (
            f"Post {num:02d} caption+hashtags exceeds Instagram's 2,200-char limit ({len(caption_full)} chars)"
        )

        entry: dict = {
            "post_number": num,
            "post_id": f"post-{num:02d}",
            "slug": slug,
            "week": post["week"],
            "title": post["title"],
            "date_display": post["date_display"],
            "time_pst": post["time_pst"],
            "scheduled_at_iso": scheduled_iso,
            "format": post["format"],
            "link_in_bio": post["url"],
            "caption_full": caption_full,
            "story_prompt": post["story_prompt"],
        }

        if post["format_type"] == "reel":
            # Compile reel-01..05 storyboard frames into MP4 + use reel-00-cover.jpg as cover_url
            story_frames = [
                post_png_dir / s["filename"]
                for s in post["slides"]
                if not s["filename"].startswith("reel-00-")
            ]
            out_mp4 = MEDIA_REELS_DIR / f"{slug}.mp4"
            print(f"  Compiling Reel MP4: {out_mp4.relative_to(ROOT_DIR)} ({len(story_frames)} frames)...")
            compile_reel_mp4(story_frames, out_mp4)
            reel_count += 1

            cover_jpg = jpg_map["reel-00-cover.jpg" if "reel-00-cover.jpg" in jpg_map else "reel-00-cover.png"]
            entry["publish_type"] = "reel"
            entry["video_url"] = f"{RAW_BASE_URL}/{out_mp4.relative_to(ROOT_DIR).as_posix()}"
            entry["cover_url"] = f"{RAW_BASE_URL}/{cover_jpg.relative_to(ROOT_DIR).as_posix()}"
            entry["media_urls"] = [entry["video_url"]]
            entry["story_url"] = None

        elif post["format_type"] == "single":
            # Feed photo (post-01-*.jpg) + companion 9:16 Story (story-01-*.jpg)
            feed_slide = next(s for s in post["slides"] if s["filename"].startswith("post-"))
            story_slide = next((s for s in post["slides"] if s["filename"].startswith("story-")), None)
            feed_jpg = jpg_map[feed_slide["filename"]]
            entry["publish_type"] = "single"
            entry["media_urls"] = [f"{RAW_BASE_URL}/{feed_jpg.relative_to(ROOT_DIR).as_posix()}"]
            entry["story_url"] = (
                f"{RAW_BASE_URL}/{jpg_map[story_slide['filename']].relative_to(ROOT_DIR).as_posix()}"
                if story_slide
                else None
            )

        else:
            # Carousel (all slide-*.jpg items; if post-12 also has reel-00-cover.png, publish it as companion Story!)
            carousel_slides = [s for s in post["slides"] if s["filename"].startswith("slide-")]
            extra_story = next((s for s in post["slides"] if s["filename"].startswith("reel-00-")), None)
            entry["publish_type"] = "carousel"
            entry["media_urls"] = [
                f"{RAW_BASE_URL}/{jpg_map[s['filename']].relative_to(ROOT_DIR).as_posix()}"
                for s in carousel_slides
            ]
            entry["story_url"] = (
                f"{RAW_BASE_URL}/{jpg_map[extra_story['filename']].relative_to(ROOT_DIR).as_posix()}"
                if extra_story
                else None
            )

        manifest_posts.append(entry)

        post_key = f"post-{num:02d}"
        if post_key in existing_state:
            new_state[post_key] = existing_state[post_key]
        else:
            new_state[post_key] = {
                "slug": slug,
                "scheduled_at_iso": scheduled_iso,
                "status": "pending",
                "published_at": None,
                "ig_media_id": None,
                "story_media_id": None,
            }

    MANIFEST_PATH.write_text(
        json.dumps({"raw_base_url": RAW_BASE_URL, "posts": manifest_posts}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    STATE_PATH.write_text(json.dumps(new_state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Update schedule.csv to include Public HTTPS Media URLs for Graph API / Buffer / Later / Make
    csv_path = ROOT_DIR / "schedule.csv"
    fieldnames = [
        "Post Number",
        "Week",
        "Scheduled Date",
        "Scheduled Time (PST)",
        "ISO Timestamp (PST)",
        "Format",
        "Graph API Type",
        "Title",
        "Post Folder",
        "Media Files",
        "Public HTTPS Media URLs",
        "Companion Story URL",
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
        for post, m in zip(posts, manifest_posts):
            media_paths = "; ".join(f"posts/{post['slug']}/{s['filename']}" for s in post["slides"])
            writer.writerow(
                {
                    "Post Number": f"{post['number']:02d}",
                    "Week": f"Week {post['week']}",
                    "Scheduled Date": post["date_display"],
                    "Scheduled Time (PST)": post["time_pst"],
                    "ISO Timestamp (PST)": m["scheduled_at_iso"],
                    "Format": post["format"],
                    "Graph API Type": m["publish_type"].upper(),
                    "Title": post["title"],
                    "Post Folder": f"posts/{post['slug']}",
                    "Media Files": media_paths,
                    "Public HTTPS Media URLs": "; ".join(m["media_urls"]),
                    "Companion Story URL": m["story_url"] or "",
                    "Slide Count": len(post["slides"]),
                    "Caption": post["caption"],
                    "Hashtags": post["hashtags"],
                    "Caption + Hashtags": m["caption_full"],
                    "Link in Bio URL": post["url"],
                    "Story Prompt": post["story_prompt"],
                }
            )

    print(f"✓ Converted {jpg_count} PNGs -> sRGB JPEGs in media/jpg/")
    print(f"✓ Compiled {reel_count} Instagram Reels MP4s in media/reels/")
    print(f"✓ Wrote {MANIFEST_PATH.name}, {STATE_PATH.name}, and updated schedule.csv")


if __name__ == "__main__":
    build_all()
