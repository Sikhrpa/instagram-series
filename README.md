# SikhRPA 4-Week Instagram Content Series (December 2026)

Production-ready 4-week (12-post, 65-graphic) bilingual Instagram educational campaign, posting schedule, interactive web gallery, and reproducible Python/Playwright graphics generator for the **Sikh Rifle and Pistol Association (SikhRPA)** — an IRS-recognized California 501(c)(3) nonprofit public benefit corporation (`EIN: 42-2595402`).

> **ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!**
> Website: [sikhrpa.org](https://sikhrpa.org) • Contact: [president@sikhrpa.org](mailto:president@sikhrpa.org) • Source Brand Repo: [Sikhrpa/sikhrpa](https://github.com/Sikhrpa/sikhrpa)

---

## 4-Week Posting Schedule (Dec 1 – Dec 26, 2026 • Tue / Thu / Sat • PST)

| # | Date & Time (PST) | Format | Graphics | Topic & Primary Resource | Folder |
|---|---|---|---|---|---|
| **01** | **Tue, Dec 1** *(GivingTuesday)* • 11:00 AM | Carousel (6 slides, 4:5) | 6 PNGs | Meet SikhRPA — 501(c)(3) Mission, Free Tools, Bilingual Outreach & GivingTuesday ([donate.html](https://sikhrpa.org/donate.html)) | [`posts/post-01-meet-sikhrpa-givingtuesday`](posts/post-01-meet-sikhrpa-givingtuesday/) |
| **02** | **Thu, Dec 3** • 5:30 PM | Carousel (6 slides, 4:5) | 6 PNGs | The 4 Universal Firearm Safety Rules in English & Gurmukhi ([sikhrpa.org](https://sikhrpa.org/)) | [`posts/post-02-four-universal-safety-rules`](posts/post-02-four-universal-safety-rules/) |
| **03** | **Sat, Dec 5** • 10:00 AM | Reel (9:16 Cover + 5 Storyboard Frames) | 6 PNGs | Free 30-Question CA FSC Practice Exam ([fsc-quiz.html](https://sikhrpa.org/fsc-quiz.html)) | [`posts/post-03-ca-fsc-practice-exam-reel`](posts/post-03-ca-fsc-practice-exam-reel/) |
| **04** | **Tue, Dec 8** • 12:00 PM | Carousel (7 slides, 4:5) | 7 PNGs | California First-Time Buyer's Compliance Roadmap — REAL ID vs. "FEDERAL LIMITS APPLY", Proof of Residency & 10-Day (240-Hour) DROS Timeline ([buyer-guide.html](https://sikhrpa.org/buyer-guide.html)) | [`posts/post-04-ca-first-time-buyer-roadmap`](posts/post-04-ca-first-time-buyer-roadmap/) |
| **05** | **Thu, Dec 10** • 6:00 PM | Carousel (6 slides, 4:5) | 6 PNGs | Holiday Safe Storage, CA Penal Code § 25100 & 3-Minute Pre-Guest Audit ([sikhrpa.org](https://sikhrpa.org/)) | [`posts/post-05-holiday-safe-storage-pc25100`](posts/post-05-holiday-safe-storage-pc25100/) |
| **06** | **Sat, Dec 12** • 10:00 AM | Single Editorial Graphic (4:5) + Story Q&A Template (9:16) | 2 PNGs | Daily California Legal & Regulatory Watch ([news.html](https://sikhrpa.org/news.html)) | [`posts/post-06-daily-legal-regulatory-watch`](posts/post-06-daily-legal-regulatory-watch/) |
| **07** | **Tue, Dec 15** • 12:00 PM | Reel (9:16 Cover + 5 Storyboard Frames) | 6 PNGs | Interactive Pistol Shot Diagnostic — 8-Sector Target Clock Dial (Low-Left 7–8 o'clock) + Dry-Fire Safety Checklist ([shot-diagnosis.html](https://sikhrpa.org/shot-diagnosis.html)) | [`posts/post-07-pistol-shot-diagnostic-reel`](posts/post-07-pistol-shot-diagnostic-reel/) |
| **08** | **Thu, Dec 17** • 5:30 PM | Carousel (6 slides, 4:5) | 6 PNGs | Bilingual Range Trauma & Stop the Bleed — IFAK Audit, English/Gurmukhi Tourniquet Rules & 911 Dispatch Script ([trauma-safety.html](https://sikhrpa.org/trauma-safety.html)) | [`posts/post-08-bilingual-range-trauma-stop-the-bleed`](posts/post-08-bilingual-range-trauma-stop-the-bleed/) |
| **09** | **Sat, Dec 19** • 10:00 AM | Carousel (6 slides, 4:5) | 6 PNGs | How to Zero Optics — 5-Shot Centroid Triangulation, MOA vs. MIL, 25/50/100-Yd Click Scaling & Height-Over-Bore ([zero-optics.html](https://sikhrpa.org/zero-optics.html)) | [`posts/post-09-how-to-zero-optics`](posts/post-09-how-to-zero-optics/) |
| **10** | **Tue, Dec 22** *(Shaheedi Week)* • 12:00 PM | Carousel (6 slides, 4:5) | 6 PNGs | Miri-Piri & Sikh Martial Heritage — Dignified Shaheedi Week Reflection Honoring the Chaar Sahibzaade & Mata Gujri Ji ([heritage.html](https://sikhrpa.org/heritage.html)) | [`posts/post-10-miri-piri-shaheedi-week`](posts/post-10-miri-piri-shaheedi-week/) |
| **11** | **Thu, Dec 24** • 4:00 PM | Single Community Poster (4:5) + Story Template (9:16) | 2 PNGs | Host a Free 2027 Safety & Safe Storage Workshop at Your Gurdwara (`president@sikhrpa.org`) | [`posts/post-11-host-2027-gurdwara-workshop`](posts/post-11-host-2027-gurdwara-workshop/) |
| **12** | **Sat, Dec 26** • 10:30 AM | Reel Cover (9:16) + Carousel (5 slides, 4:5) | 6 PNGs | Year-End 501(c)(3) Tax-Deductible Giving Appeal Before Dec 31 ([donate.html](https://sikhrpa.org/donate.html)) | [`posts/post-12-year-end-501c3-giving-appeal`](posts/post-12-year-end-501c3-giving-appeal/) |

**Total Deliverables:** 12 complete posts • **65 production-ready PNGs** (`1080×1350` for 4:5 feed posts and `1080×1920` for 9:16 Reels & Stories) • 12 ready-to-paste `caption.txt` files • `schedule.csv` • Interactive GitHub Pages Gallery (`index.html`).

---

## Repository Structure

```text
instagram-series/
├── .github/workflows/
│   └── auto-post-instagram.yml                    # Scheduled & manual GitHub Actions Instagram publisher
├── assets/
│   └── srpa-logo.png                              # Official SikhRPA crest (from Sikhrpa/sikhrpa)
├── media/
│   ├── jpg/                                       # 65 Instagram-Graph-API-ready sRGB JPEGs
│   └── reels/                                     # 2 compiled 1080×1920 H.264/AAC MP4 Reels (Posts 03 & 07)
├── posts/
│   ├── post-01-meet-sikhrpa-givingtuesday/        # 6 PNGs (4:5) + caption.txt
│   ├── post-02-four-universal-safety-rules/       # 6 PNGs (4:5) + caption.txt
│   ├── post-03-ca-fsc-practice-exam-reel/         # 6 PNGs (9:16) + caption.txt
│   ├── post-04-ca-first-time-buyer-roadmap/       # 7 PNGs (4:5) + caption.txt
│   ├── post-05-holiday-safe-storage-pc25100/      # 6 PNGs (4:5) + caption.txt
│   ├── post-06-daily-legal-regulatory-watch/      # 2 PNGs (4:5 + 9:16) + caption.txt
│   ├── post-07-pistol-shot-diagnostic-reel/       # 6 PNGs (9:16) + caption.txt
│   ├── post-08-bilingual-range-trauma-stop-the-bleed/ # 6 PNGs (4:5) + caption.txt
│   ├── post-09-how-to-zero-optics/                # 6 PNGs (4:5) + caption.txt
│   ├── post-10-miri-piri-shaheedi-week/           # 6 PNGs (4:5) + caption.txt
│   ├── post-11-host-2027-gurdwara-workshop/       # 2 PNGs (4:5 + 9:16) + caption.txt
│   └── post-12-year-end-501c3-giving-appeal/      # 6 PNGs (9:16 + 4:5) + caption.txt
├── scripts/
│   ├── styles.py                                  # Brand colors, typography & HTML/CSS canvas frames
│   ├── diagrams.py                                # Inline SVG generators (REAL ID, DROS, Clock Dial, TQ, Optics)
│   ├── content_posts_1_to_6.py                    # Slides, captions, hashtags & Story prompts (Posts 01–06)
│   ├── content_posts_7_to_12.py                   # Slides, captions, hashtags & Story prompts (Posts 07–12)
│   ├── generate_all.py                            # Master Playwright renderer + policy/overflow validator
│   ├── build_publish_media.py                     # Converts PNGs -> JPEGs, compiles MP4 Reels & builds manifest
│   └── auto_post.py                               # Zero-dependency Instagram Graph API auto-poster
├── AUTO_POST_SETUP.md                             # 5-minute setup guide for GitHub Actions & Meta Graph API
├── publish_manifest.json                          # Structured schedule + public HTTPS media URLs
├── publish_state.json                             # Idempotent publish tracker (prevents duplicate posts)
├── index.html                                     # Interactive web gallery (GitHub Pages ready)
├── schedule.csv                                   # Import-ready schedule with public HTTPS URLs
└── README.md
```

---

## Automated Posting (Instagram Graph API + GitHub Actions)

All 12 posts — including **Carousels**, compiled **1080×1920 MP4 Reels** (Posts 03 & 07), **Single Posts**, and **Companion 9:16 Stories** — can publish automatically on schedule via **GitHub Actions** with zero third-party hosting costs:

1. Add two GitHub Repository Secrets (`IG_USER_ID` and `IG_ACCESS_TOKEN`) — see the 5-minute walkthrough in **[AUTO_POST_SETUP.md](AUTO_POST_SETUP.md)**.
2. Test in **Actions → Auto-Post SikhRPA Instagram Series → Run workflow** using `verify_token` and `dry_run`.
3. The scheduled workflow automatically publishes each pending post when its PST timestamp arrives and commits the returned Instagram Media ID to `publish_state.json` so no post is ever duplicated.

---

## Brand Identity & Typography System

- **Primary Navy:** `#0f172a`
- **Heritage Gold:** `#d97706` (highlight `#f59e0b` / `#fbbf24`)
- **Royal Blue:** `#1e3a8a`
- **Official Crest:** `assets/srpa-logo.png`
- **Fonts:** `Inter` / `Inter Display` (English) + `Noto Sans Gurmukhi` / `Noto Serif Gurmukhi` (Punjabi / Gurmukhi)
- **Organization Details:** Sikh Rifle and Pistol Association • IRS 501(c)(3) Public Charity • Federal EIN: `42-2595402` • `president@sikhrpa.org` • `sikhrpa.org`

---

## Meta / Instagram Firearm-Education Policy Guardrails

Every graphic, caption, hashtag block, and Story prompt is programmatically audited by `scripts/generate_all.py` against Meta's Regulated Goods & Firearms policies:

1. **Strictly Educational, Safety, Compliance & First-Aid Framing:** Every post focuses exclusively on accident prevention, California Penal Code compliance, safe home storage, marksmanship biomechanics, optical physics, emergency bleeding control, and Sikh ethical heritage.
2. **Zero Commerce, Sales, or Giveaway Language:** No firearm/ammunition sales, transfers, pricing, promo codes, raffles, or giveaways anywhere in copy or graphics. Free safety devices distributed at workshops are explicitly framed as *CA DOJ-approved cable safety locks*.
3. **Clean Educational Hashtags:** Uses non-commercial public-safety and community tags (`#SikhRPA`, `#FirearmSafetyEducation`, `#SafeStorage`, `#StopTheBleed`, `#CaliforniaCompliance`, `#Nonprofit501c3`, `#StaySafeBeResponsible`) and blocks commonly flagged commercial/shadowbanned hashtags.
4. **Clear Legal & Medical Disclaimers:** Educational notices are included on the FSC Practice Exam (Post 03), Legal Watch (Post 06), and Range Trauma / Stop the Bleed (Post 08) posts.

---

## Reproducing or Editing the Series

All copy, diagrams, publish media, schedules, and gallery HTML are generated reproducibly from `scripts/`:

```bash
# 1. Install English & Gurmukhi system fonts + ffmpeg (Ubuntu / Debian)
sudo apt-get update && sudo apt-get install -y fonts-inter fonts-noto-core fonts-noto-ui-core ffmpeg

# 2. Install Playwright & Pillow
pip install playwright pillow

# 3. Edit copy in scripts/content_posts_1_to_6.py or scripts/content_posts_7_to_12.py
# 4. Re-render all 65 PNGs, caption.txt files, and index.html
python3 scripts/generate_all.py

# 5. Rebuild Instagram Graph API JPEGs, MP4 Reels, publish_manifest.json & schedule.csv
python3 scripts/build_publish_media.py
```

The generator automatically runs:
- A **Meta Policy Guardrail Audit** on all copy and hashtags
- A **Layout Overflow Check** (`scrollHeight <= clientHeight`) on all 65 slides

---

## Interactive Gallery (GitHub Pages)

Open [`index.html`](index.html) locally or enable **GitHub Pages** (`Settings → Pages → Deploy from branch: main / root`) to publish a live campaign dashboard for your social media team with:
- Week and format filters + keyword search
- Interactive slide carousel previews + full-resolution lightbox zoom
- One-click **Copy Caption + Hashtags**, **Copy Caption Only**, **Copy Hashtags**, and **Copy Story Prompt** buttons
- Direct download links for every PNG and `schedule.csv`
