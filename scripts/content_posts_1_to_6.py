"""
SikhRPA 4-Week Instagram Series — Posts 01 through 06 (Dec 1 – Dec 12, 2026)
Grounded in Sikhrpa/sikhrpa official brand guidelines, bilingual Gurmukhi copy,
California statutory citations, and Meta firearm-education policy guardrails.
"""

from __future__ import annotations

from diagrams import (
    svg_dros_timeline,
    svg_real_id_comparison,
    svg_safety_rule_icon,
    svg_storage_tier_icon,
)
from styles import get_logo_data_uri


def get_posts_1_to_6() -> list[dict]:
    logo = get_logo_data_uri()

    # =========================================================================
    # POST 01 — Tue, Dec 1, 2026 (GivingTuesday) • 11:00 AM PST • 6-Slide Carousel
    # =========================================================================
    post_01 = {
        "number": 1,
        "slug": "post-01-meet-sikhrpa-givingtuesday",
        "date_iso": "2026-12-01",
        "date_display": "Tue, Dec 1, 2026 (GivingTuesday)",
        "time_pst": "11:00 AM PST",
        "week": 1,
        "format": "Carousel (6 slides, 4:5)",
        "format_type": "carousel",
        "title": "Meet SikhRPA — 501(c)(3) Safety Education & GivingTuesday",
        "url": "https://sikhrpa.org/donate.html",
        "caption": (
            "Meet the Sikh Rifle and Pistol Association (SikhRPA) — an IRS-recognized California 501(c)(3) "
            "nonprofit public benefit corporation dedicated to firearm safety education, safe home storage, "
            "statutory compliance, and emergency trauma readiness.\n\n"
            "Everything we publish at sikhrpa.org is 100% free and accessible in both English and Gurmukhi:\n"
            "• Free 30-Question CA Firearm Safety Certificate (FSC) Practice Exam\n"
            "• California First-Time Compliance Roadmap (REAL ID, Proof of Residency & DROS)\n"
            "• Bilingual Range Trauma & Stop the Bleed First-Aid Guide\n"
            "• Interactive Pistol Shot Diagnostic & Optics Zeroing Calculators\n"
            "• Daily California Legal & Regulatory Watch Archive\n"
            "• Free Gurdwara Safe Storage Workshops & CA DOJ-Approved Cable Locks\n\n"
            "This #GivingTuesday, every tax-deductible contribution directly funds printed bilingual safety guides, "
            "free CA DOJ-approved cable locks for families, and community safety clinics across California.\n\n"
            "• $20 = 1 CA DOJ-approved cable safety lock for a local family\n"
            "• $50 = 100 pocket-sized English & Gurmukhi safety manuals\n"
            "• $150 = Certified eye & ear protection kits for 10 beginner students\n"
            "• $1,000 = Sponsors a full bilingual Gurdwara safety workshop\n\n"
            "Support public safety education at sikhrpa.org/donate.html (Link in bio)\n"
            "Zelle (0% fees): sikhrpa | Federal EIN: 42-2595402 | president@sikhrpa.org\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #GivingTuesday #FirearmSafetyEducation #SafeStorage #PublicSafetyEducation "
            "#Nonprofit501c3 #SikhCommunity #CaliforniaSikhs #PunjabiCommunity #BilingualEducation "
            "#GurdwaraOutreach #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Repost Slide 1 to your Story with a 'Link' sticker pointing to https://sikhrpa.org/donate.html "
            "and a Poll sticker: 'Have you explored SikhRPA's free bilingual safety tools?' "
            "(Options: 'Yes — super helpful!' / 'Checking them out now!')."
        ),
        "slides": [
            {
                "filename": "slide-01-cover.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "GivingTuesday • Dec 1",
                "slide_label": "01 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;">
                  <img class="cover-logo-hero" src="{logo}" alt="SikhRPA Official Logo"/>
                  <div class="eyebrow">IRS 501(c)(3) Nonprofit Public Charity</div>
                  <h1 class="h1-hero">Meet <span class="gold">SikhRPA</span></h1>
                  <p class="lead" style="max-width:820px;">
                    Advancing <strong style="color:#fff;">firearm safety education</strong>, safe home storage,
                    California statutory compliance, and bilingual community clinics.
                  </p>
                  <div class="pa-banner" style="width:100%;max-width:860px;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;">
                    <div class="pa-text-lg">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                    <div style="font-size:19px;font-weight:800;letter-spacing:0.12em;color:#cbd5e1;margin-top:4px;text-transform:uppercase;">
                      Stay Safe, Be Responsible!
                    </div>
                  </div>
                  <div class="stat-row" style="width:100%;">
                    <div class="stat-box">
                      <div class="stat-val">501(c)(3)</div>
                      <div class="stat-lbl">EIN 42-2595402</div>
                    </div>
                    <div class="stat-box">
                      <div class="stat-val">100% Free</div>
                      <div class="stat-lbl">Digital Safety Library</div>
                    </div>
                    <div class="stat-box">
                      <div class="stat-val">EN + ਪੰਜਾਬੀ</div>
                      <div class="stat-lbl">Bilingual Outreach</div>
                    </div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-02-mission.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Public Benefit Mission",
                "slide_label": "02 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Why We Exist</div>
                <h2 class="h1-lg">Three Pillars of <span class="gold">Community Safety</span></h2>
                <p class="body-text">
                  The Sikh Rifle and Pistol Association is organized exclusively for charitable and educational
                  purposes under IRC § 501(c)(3) to prevent accidents and build disciplined stewardship.
                </p>
                <div class="stack" style="margin-top:6px;">
                  <div class="card card-gold row">
                    <div class="num-badge">1</div>
                    <div class="stack-sm">
                      <div class="h3-title">Safety &amp; Safe Home Storage</div>
                      <p class="body-sm">Educating families on California safe storage mandates (PC § 25100), child safety protocols, lockbox selection, and distributing free DOJ-approved cable locks.</p>
                    </div>
                  </div>
                  <div class="card card-blue row">
                    <div class="num-badge num-badge-blue">2</div>
                    <div class="stack-sm">
                      <div class="h3-title">Disciplined Marksmanship &amp; Trauma Care</div>
                      <p class="body-sm">Structured fundamentals covering safe handling, trigger biomechanics, optic zeroing, and life-saving Stop the Bleed range trauma preparedness.</p>
                    </div>
                  </div>
                  <div class="card row">
                    <div class="num-badge">3</div>
                    <div class="stack-sm">
                      <div class="h3-title">California Statutory Awareness</div>
                      <p class="body-sm">Plain-English and Punjabi compliance checklists, free FSC study aids, and daily regulatory briefings so owners remain fully law-abiding.</p>
                    </div>
                  </div>
                </div>
                <div class="pa-banner">
                  <div class="pa-text-sm">ਸਾਡੀ ਸੰਸਥਾ ਦਾ ਮਕਸਦ ਘਰਾਂ ਵਿੱਚ ਹਾਦਸਿਆਂ ਨੂੰ ਰੋਕਣਾ, ਬੱਚਿਆਂ ਦੀ ਸੁਰੱਖਿਆ ਯਕੀਨੀ ਬਣਾਉਣਾ, ਅਤੇ ਕੈਲੀਫੋਰਨੀਆ ਦੇ ਕਾਨੂੰਨਾਂ ਦੀ ਸਹੀ ਜਾਣਕਾਰੀ ਦੇਣਾ ਹੈ।</div>
                </div>
                """,
            },
            {
                "filename": "slide-03-free-tools.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "100% Free Tools",
                "slide_label": "03 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Open Educational Library</div>
                <h2 class="h1-lg">6 Free Interactive Tools at <span class="gold">sikhrpa.org</span></h2>
                <p class="body-text">No paywalls, no accounts required — built for California families, new owners, and instructors.</p>
                <div class="grid-2" style="margin-top:4px;">
                  <div class="card card-blue stack-sm">
                    <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">01 • FSC EXAM PREP</div>
                    <div class="h3-title" style="font-size:25px;">CA FSC 30-Q Practice Test</div>
                    <p class="body-sm">Official CA DOJ model format, instant legal explanations &amp; category score breakdown.</p>
                    <div class="blue-lt" style="font-size:15px;font-weight:700;">sikhrpa.org/fsc-quiz.html</div>
                  </div>
                  <div class="card card-gold stack-sm">
                    <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">02 • COMPLIANCE GUIDE</div>
                    <div class="h3-title" style="font-size:25px;">First-Time Roadmap</div>
                    <p class="body-sm">REAL ID vs. Federal Limits Apply, handgun residency proof, DROS 240-hr timeline &amp; transport.</p>
                    <div class="gold" style="font-size:15px;font-weight:700;">sikhrpa.org/buyer-guide.html</div>
                  </div>
                  <div class="card stack-sm">
                    <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">03 • LIFE SAFETY</div>
                    <div class="h3-title" style="font-size:25px;">Bilingual Range Trauma</div>
                    <p class="body-sm">English &amp; Gurmukhi tourniquet rules, IFAK kit auditor &amp; remote GPS 911 dispatch script.</p>
                    <div class="blue-lt" style="font-size:15px;font-weight:700;">sikhrpa.org/trauma-safety.html</div>
                  </div>
                  <div class="card stack-sm">
                    <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">04 • BIOMECHANICS</div>
                    <div class="h3-title" style="font-size:25px;">Pistol Shot Diagnostic</div>
                    <p class="body-sm">8-sector clock wheel (right &amp; left-handed), trigger finger zones &amp; safe dry-fire drills.</p>
                    <div class="blue-lt" style="font-size:15px;font-weight:700;">sikhrpa.org/shot-diagnosis.html</div>
                  </div>
                  <div class="card stack-sm">
                    <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">05 • BALLISTICS</div>
                    <div class="h3-title" style="font-size:25px;">How to Zero Optics</div>
                    <p class="body-sm">5-shot group centroid triangulator, MOA/MIL click calculator &amp; height-over-bore guides.</p>
                    <div class="blue-lt" style="font-size:15px;font-weight:700;">sikhrpa.org/zero-optics.html</div>
                  </div>
                  <div class="card stack-sm">
                    <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">06 • REGULATORY BRIEF</div>
                    <div class="h3-title" style="font-size:25px;">Daily CA Legal Watch</div>
                    <p class="body-sm">Automated public archive tracking CA DOJ bulletins, legislation &amp; 9th Circuit rulings.</p>
                    <div class="blue-lt" style="font-size:15px;font-weight:700;">sikhrpa.org/news.html</div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-04-bilingual-outreach.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Bilingual Community Outreach",
                "slide_label": "04 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Serving Every Generation</div>
                <h2 class="h1-lg">Safety Education in <span class="gold">English &amp; Gurmukhi</span></h2>
                <div class="pa-banner">
                  <div class="pa-text-md">ਸਿੱਖ ਰਾਈਫਲ ਅਤੇ ਪਿਸਤੌਲ ਐਸੋਸੀਏਸ਼ਨ — ਪਰਿਵਾਰਾਂ, ਬੀਬੀਆਂ ਅਤੇ ਨਵੇਂ ਸਿੱਖਣ ਵਾਲਿਆਂ ਲਈ ਮੁਫ਼ਤ ਸੁਰੱਖਿਆ ਸਿੱਖਿਆ।</div>
                </div>
                <div class="stack" style="margin-top:4px;">
                  <div class="card row">
                    <span class="icon-ok">✓</span>
                    <div class="stack-sm">
                      <div class="h3-title" style="font-size:26px;">Free Gurdwara Safety &amp; Safe Storage Clinics</div>
                      <p class="body-sm">Certified bilingual instructors visit California Gurdwaras and community halls at zero cost to host families and elders.</p>
                    </div>
                  </div>
                  <div class="card row">
                    <span class="icon-ok">✓</span>
                    <div class="stack-sm">
                      <div class="h3-title" style="font-size:26px;">Free CA DOJ-Approved Cable Locks</div>
                      <p class="body-sm">Every seminar distributes free DOJ-approved safety cable locks so every household can secure firearms immediately.</p>
                    </div>
                  </div>
                  <div class="card row">
                    <span class="icon-ok">✓</span>
                    <div class="stack-sm">
                      <div class="h3-title" style="font-size:26px;">Printed Bilingual Handbooks &amp; Bleeding Control</div>
                      <p class="body-sm">Pocket tri-fold safety leaflets and Gurdwara bleeding-control readiness guidance written in clear, accessible Punjabi.</p>
                    </div>
                  </div>
                </div>
                <div class="card card-blue" style="text-align:center;padding:18px 24px;">
                  <div style="font-size:20px;font-weight:700;color:#dbeafe;">
                    Invite SikhRPA to your Gurdwara or community center: <span class="gold">president@sikhrpa.org</span>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-05-givingtuesday-impact.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "GivingTuesday Impact",
                "slide_label": "05 / 06",
                "footer_url": "sikhrpa.org/donate.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">GivingTuesday • December 1, 2026</div>
                <h2 class="h1-lg">Where Your <span class="gold">Tax-Deductible</span> Gift Goes</h2>
                <p class="body-text">
                  100% of contributions fund our exempt public safety mission under IRC § 170 (Federal EIN: 42-2595402).
                </p>
                <div class="grid-2" style="margin-top:6px;">
                  <div class="card card-gold stack-sm">
                    <div style="font-size:48px;font-weight:900;color:#fbbf24;line-height:1;">$20</div>
                    <div class="h3-title" style="font-size:25px;">Child-Safe Cable Lock</div>
                    <p class="body-sm">Provides <strong>1 CA DOJ-approved cable safety lock</strong> gifted free to a first-time owner or young family.</p>
                  </div>
                  <div class="card card-blue stack-sm">
                    <div style="font-size:48px;font-weight:900;color:#93c5fd;line-height:1;">$50</div>
                    <div class="h3-title" style="font-size:25px;">100 Bilingual Guides</div>
                    <p class="body-sm">Funds printing and statewide distribution of <strong>100 English &amp; Punjabi</strong> safety reference manuals.</p>
                  </div>
                  <div class="card stack-sm">
                    <div style="font-size:48px;font-weight:900;color:#34d399;line-height:1;">$150</div>
                    <div class="h3-title" style="font-size:25px;">Student Safety Gear</div>
                    <p class="body-sm">Equips <strong>10 beginner students</strong> with ANSI Z87.1 eye protection, 30+ dB ear protection &amp; targets.</p>
                  </div>
                  <div class="card card-gold stack-sm">
                    <div style="font-size:48px;font-weight:900;color:#fbbf24;line-height:1;">$1,000</div>
                    <div class="h3-title" style="font-size:25px;">Community Workshop</div>
                    <p class="body-sm">Sponsors a full in-person <strong>certified safe handling &amp; storage clinic</strong> at a California Gurdwara.</p>
                  </div>
                </div>
                <div class="pa-banner" style="padding:14px 22px;">
                  <div class="pa-text-sm">ਟੈਕਸ-ਮੁਕਤ ਦਾਨ (IRC § 170): ਤੁਹਾਡਾ ਦਸਵੰਧ ਮੁਫ਼ਤ ਪੰਜਾਬੀ ਗਾਈਡਾਂ ਅਤੇ ਪਰਿਵਾਰਾਂ ਨੂੰ ਮੁਫ਼ਤ ਕੇਬਲ ਲਾਕ ਵੰਡਣ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।</div>
                </div>
                """,
            },
            {
                "filename": "slide-06-cta.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Support Safety Education",
                "slide_label": "06 / 06",
                "footer_url": "sikhrpa.org/donate.html",
                "footer_right": "SAVE & SHARE",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:22px;">
                  <img class="brand-logo" style="width:118px;height:118px;border-width:3px;" src="{logo}" alt="SikhRPA Logo"/>
                  <div class="eyebrow">GivingTuesday Appeal</div>
                  <h2 class="h1-lg">Invest in a <span class="gold">Safer Community</span> Today</h2>
                  <div class="grid-2" style="width:100%;text-align:left;">
                    <div class="card card-emerald stack-sm">
                      <div class="emerald" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">0% TRANSACTION FEES</div>
                      <div class="h3-title" style="font-size:27px;">Zelle® Bank Transfer</div>
                      <div style="font-size:28px;font-weight:900;color:#fff;margin:4px 0;">Tag: <span class="gold">sikhrpa</span></div>
                      <p class="body-sm">Include your email in the memo for an official IRS tax receipt.</p>
                    </div>
                    <div class="card card-blue stack-sm">
                      <div class="blue-lt" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">CARDS • VENMO • PAYPAL</div>
                      <div class="h3-title" style="font-size:27px;">Online Giving Portal</div>
                      <div style="font-size:24px;font-weight:900;color:#fff;margin:4px 0;">ID: <span class="gold">#S5PAN9B85U28J</span></div>
                      <p class="body-sm">Instant electronic IRS acknowledgment • Corporate match eligible.</p>
                    </div>
                  </div>
                  <div class="url-chip">sikhrpa.org/donate.html</div>
                  <div class="card" style="width:100%;padding:16px 24px;text-align:center;">
                    <div style="font-size:18px;color:#e2e8f0;font-weight:700;">
                      Federal EIN: <span class="gold">42-2595402</span> &nbsp;•&nbsp; Inquiries &amp; Employer Match: <span class="gold">president@sikhrpa.org</span>
                    </div>
                    <div class="pa-text-sm" style="margin-top:6px;">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!</div>
                  </div>
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # POST 02 — Thu, Dec 3, 2026 • 5:30 PM PST • 6-Slide Carousel (4:5)
    # =========================================================================
    post_02 = {
        "number": 2,
        "slug": "post-02-four-universal-safety-rules",
        "date_iso": "2026-12-03",
        "date_display": "Thu, Dec 3, 2026",
        "time_pst": "5:30 PM PST",
        "week": 1,
        "format": "Carousel (6 slides, 4:5)",
        "format_type": "carousel",
        "title": "The 4 Universal Firearm Safety Rules (English & Gurmukhi)",
        "url": "https://sikhrpa.org/",
        "caption": (
            "Safe firearm handling rests on four universal rules — zero exceptions, every single time.\n\n"
            "Save and share this bilingual English & Gurmukhi reference card with family members, "
            "first-time learners, and anyone preparing for the California Firearm Safety Certificate (FSC) exam:\n\n"
            "1. Always treat every firearm as loaded.\n"
            "   ਹਮੇਸ਼ਾ ਇਹ ਮੰਨ ਕੇ ਚੱਲੋ ਕਿ ਹਥਿਆਰ ਲੋਡ ਹੈ।\n"
            "2. Never point at anything you do not wish to destroy.\n"
            "   ਬੈਰਲ ਦਾ ਮੂੰਹ ਹਮੇਸ਼ਾ ਸੁਰੱਖਿਅਤ ਦਿਸ਼ਾ ਵੱਲ ਰੱਖੋ।\n"
            "3. Keep your finger off the trigger until ready to shoot.\n"
            "   ਟਰਿੱਗਰ 'ਤੇ ਉਂਗਲ ਉਦੋਂ ਹੀ ਰੱਖੋ ਜਦੋਂ ਨਿਸ਼ਾਨਾ ਪੂਰਾ ਹੋਵੇ।\n"
            "4. Know your target and what is beyond it.\n"
            "   ਆਪਣੇ ਨਿਸ਼ਾਨੇ ਅਤੇ ਉਸਦੇ ਪਿੱਛੇ ਦੀ ਜਗ੍ਹਾ ਦਾ ਧਿਆਨ ਰੱਖੋ।\n\n"
            "Download free printable English & Gurmukhi safety handouts anytime at sikhrpa.org (Link in bio).\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #FirearmSafetyRules #FirearmSafetyEducation #BilingualSafety #Gurmukhi "
            "#PunjabiCommunity #SikhCommunity #RangeSafety #SafeHandling #CaliforniaCompliance "
            "#PublicSafetyEducation #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Share Slide 6 (the all-in-one bilingual quick reference card) to your Story with the text: "
            "'Screenshot & save this bilingual 4 Rules card for your range bag or family!' "
            "Add a Quiz sticker testing Rule #1 ('If a magazine is removed, is the firearm empty?' → 'No — always visually check the chamber!')."
        ),
        "slides": [
            {
                "filename": "slide-01-cover.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Bilingual Safety Core",
                "slide_label": "01 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">The 4 Universal Tenets • ੪ ਮੂਲ ਸੁਰੱਖਿਆ ਨਿਯਮ</div>
                <h1 class="h1-hero">The 4 Universal <span class="gold">Firearm Safety Rules</span></h1>
                <div class="pa-banner">
                  <div class="pa-text-lg">ਹਰ ਸਮੇਂ ਪਾਲਣਾ ਕਰਨ ਯੋਗ ਚਾਰ ਅਟੱਲ ਸਰਵਵਿਆਪਕ ਸੁਰੱਖਿਆ ਨਿਯਮ</div>
                </div>
                <p class="lead">
                  Every preventable firearm accident happens when one or more of these four foundational habits is broken.
                  Master them in both <strong style="color:#fff;">English</strong> and <strong style="color:#fbbf24;">Gurmukhi</strong>.
                </p>
                <div class="grid-2" style="margin-top:8px;">
                  <div class="card card-gold row" style="padding:18px 20px;">
                    <div class="num-badge">1</div>
                    <div style="font-size:21px;font-weight:800;">Treat Every Firearm as Loaded</div>
                  </div>
                  <div class="card card-gold row" style="padding:18px 20px;">
                    <div class="num-badge">2</div>
                    <div style="font-size:21px;font-weight:800;">Always Keep a Safe Muzzle Direction</div>
                  </div>
                  <div class="card card-gold row" style="padding:18px 20px;">
                    <div class="num-badge">3</div>
                    <div style="font-size:21px;font-weight:800;">Finger Off Trigger Until Ready</div>
                  </div>
                  <div class="card card-gold row" style="padding:18px 20px;">
                    <div class="num-badge">4</div>
                    <div style="font-size:21px;font-weight:800;">Know Your Target &amp; Beyond</div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-02-rule-1.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Rule 1 of 4",
                "slide_label": "02 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <div class="stack-sm">
                    <div class="eyebrow">Universal Rule 01 • ਨਿਯਮ ੧</div>
                    <h2 class="h1-lg">Always Treat Every<br/><span class="gold">Firearm as Loaded</span></h2>
                  </div>
                  {svg_safety_rule_icon(1)}
                </div>
                <div class="pa-banner">
                  <div class="pa-text-lg">ਹਮੇਸ਼ਾ ਇਹ ਮੰਨ ਕੇ ਚੱਲੋ ਕਿ ਹਥਿਆਰ ਲੋਡ ਹੈ।</div>
                  <div class="pa-text-sm" style="margin-top:8px;color:#e2e8f0;">ਕਿਸੇ ਦੇ ਕਹਿਣ 'ਤੇ ਭਰੋਸਾ ਨਾ ਕਰੋ। ਮੈਗਜ਼ੀਨ ਕੱਢ ਕੇ ਚੈਂਬਰ ਦੀ ਖੁਦ ਅੱਖੀਂ ਜਾਂਚ ਕਰੋ।</div>
                </div>
                <div class="card stack-sm">
                  <div class="h3-title" style="font-size:26px;">Why This Rule Matters</div>
                  <p class="body-text">
                    Never accept anyone's verbal assurance that a firearm is "unloaded." Personally remove the magazine,
                    lock the slide or action open, and visually &amp; physically inspect the chamber every time you pick up a firearm.
                  </p>
                </div>
                <div class="grid-2">
                  <div class="card card-red stack-sm" style="padding:18px 22px;">
                    <div class="red-lt" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">✗ DANGEROUS MYTH</div>
                    <p class="body-sm">"The magazine is out, so the firearm is empty."</p>
                  </div>
                  <div class="card card-emerald stack-sm" style="padding:18px 22px;">
                    <div class="emerald" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">✓ SAFETY REALITY</div>
                    <p class="body-sm">A live round can remain inside the chamber even with the magazine removed.</p>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-03-rule-2.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Rule 2 of 4",
                "slide_label": "03 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <div class="stack-sm">
                    <div class="eyebrow">Universal Rule 02 • ਨਿਯਮ ੨</div>
                    <h2 class="h1-lg">Never Point at Anything You<br/><span class="gold">Do Not Wish to Destroy</span></h2>
                  </div>
                  {svg_safety_rule_icon(2)}
                </div>
                <div class="pa-banner">
                  <div class="pa-text-lg">ਬੈਰਲ ਦਾ ਮੂੰਹ ਹਮੇਸ਼ਾ ਸੁਰੱਖਿਅਤ ਦਿਸ਼ਾ ਵੱਲ ਰੱਖੋ।</div>
                  <div class="pa-text-sm" style="margin-top:8px;color:#e2e8f0;">ਬੈਰਲ ਦਾ ਮੂੰਹ ਕਦੇ ਕਿਸੇ ਵਿਅਕਤੀ ਜਾਂ ਅਣਚਾਹੀ ਚੀਜ਼ ਵੱਲ ਨਾ ਕਰੋ। ਮੂੰਹ ਹਮੇਸ਼ਾ ਜ਼ਮੀਨ ਜਾਂ ਬੈਕਸਟਾਪ ਵੱਲ ਰੱਖੋ।</div>
                </div>
                <div class="card stack-sm">
                  <div class="h3-title" style="font-size:26px;">100% Muzzle Discipline</div>
                  <p class="body-text">
                    Maintain total awareness of where the muzzle points during loading, unloading, clearing malfunctions,
                    and casing or uncasing at the range. Never sweep yourself, another person, or an unsafe wall.
                  </p>
                </div>
                <div class="card card-blue" style="padding:20px 24px;">
                  <ul class="check-list">
                    <li><span class="icon-gold">→</span><span><strong>At the Range:</strong> Keep the barrel pointed strictly downrange toward the berm at all times.</span></li>
                    <li><span class="icon-gold">→</span><span><strong>At Home:</strong> Identify an intentional, solid safe direction before any administrative handling.</span></li>
                  </ul>
                </div>
                """,
            },
            {
                "filename": "slide-04-rule-3.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Rule 3 of 4",
                "slide_label": "04 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <div class="stack-sm">
                    <div class="eyebrow">Universal Rule 03 • ਨਿਯਮ ੩</div>
                    <h2 class="h1-lg">Keep Your Finger Off the<br/><span class="gold">Trigger Until Ready</span></h2>
                  </div>
                  {svg_safety_rule_icon(3)}
                </div>
                <div class="pa-banner">
                  <div class="pa-text-lg">ਟਰਿੱਗਰ 'ਤੇ ਉਂਗਲ ਉਦੋਂ ਹੀ ਰੱਖੋ ਜਦੋਂ ਨਿਸ਼ਾਨਾ ਪੂਰਾ ਹੋਵੇ।</div>
                  <div class="pa-text-sm" style="margin-top:8px;color:#e2e8f0;">ਜਦੋਂ ਤੱਕ ਗੋਲੀ ਚਲਾਉਣ ਦਾ ਫੈਸਲਾ ਨਾ ਹੋਵੇ, ਉਂਗਲ ਨੂੰ ਟਰਿੱਗਰ ਗਾਰਡ ਤੋਂ ਬਾਹਰ ਫਰੇਮ 'ਤੇ ਸਿੱਧੀ ਰੱਖੋ।</div>
                </div>
                <div class="card stack-sm">
                  <div class="h3-title" style="font-size:26px;">High Frame Index Habit</div>
                  <p class="body-text">
                    Rest your index finger straight and high along the frame — completely outside the trigger guard —
                    until your sights are aligned on target and you have made a conscious decision to fire.
                  </p>
                </div>
                <div class="card card-gold" style="padding:20px 24px;">
                  <ul class="check-list">
                    <li><span class="icon-ok">✓</span><span><strong>Prevents Startle Discharges:</strong> If you trip, slip, or get startled, an indexed finger cannot inadvertently press the trigger.</span></li>
                    <li><span class="icon-ok">✓</span><span><strong>Build Automatic Muscle Memory:</strong> Practice high register every time you pick up a firearm, reload, or move.</span></li>
                  </ul>
                </div>
                """,
            },
            {
                "filename": "slide-05-rule-4.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Rule 4 of 4",
                "slide_label": "05 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <div class="stack-sm">
                    <div class="eyebrow">Universal Rule 04 • ਨਿਯਮ ੪</div>
                    <h2 class="h1-lg">Know Your Target &amp;<br/><span class="gold">What Lies Beyond It</span></h2>
                  </div>
                  {svg_safety_rule_icon(4)}
                </div>
                <div class="pa-banner">
                  <div class="pa-text-lg">ਆਪਣੇ ਨਿਸ਼ਾਨੇ ਅਤੇ ਉਸਦੇ ਪਿੱਛੇ ਦੀ ਜਗ੍ਹਾ ਦਾ ਧਿਆਨ ਰੱਖੋ।</div>
                  <div class="pa-text-sm" style="margin-top:8px;color:#e2e8f0;">ਗੋਲੀਆਂ ਕੰਧਾਂ, ਕਾਰਾਂ ਅਤੇ ਦਰਵਾਜ਼ਿਆਂ ਦੇ ਆਰ-ਪਾਰ ਜਾ ਸਕਦੀਆਂ ਹਨ। ਪੱਕੀ ਓਟ (ਬੈਕਸਟਾਪ) ਤੋਂ ਬਿਨਾਂ ਫਾਇਰ ਨਾ ਕਰੋ।</div>
                </div>
                <div class="card stack-sm">
                  <div class="h3-title" style="font-size:26px;">You Are Accountable for Every Round</div>
                  <p class="body-text">
                    Projectiles can easily pass through drywall, wooden doors, vehicles, and paper targets.
                    Always positively identify your target and verify a solid earthen berm or rated backstop behind it.
                  </p>
                </div>
                <div class="card card-red" style="padding:20px 24px;">
                  <ul class="check-list">
                    <li><span class="icon-no">!</span><span><strong>Never Shoot at Skylines or Water:</strong> Rounds can travel over a mile or ricochet unpredictably off flat surfaces.</span></li>
                    <li><span class="icon-ok">✓</span><span><strong>Outdoor Ranges &amp; BLM Land:</strong> Always verify hills, trails, and blind roads behind your target area.</span></li>
                  </ul>
                </div>
                """,
            },
            {
                "filename": "slide-06-summary-cta.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Save & Share Reference",
                "slide_label": "06 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SAVE & SHARE",
                "body_html": """
                <div class="eyebrow">Bilingual Quick Reference Card</div>
                <h2 class="h2-title">Save the 4 Rules — <span class="gold">Share With Family</span></h2>
                <div class="stack" style="gap:12px;">
                  <div class="card row" style="padding:16px 22px;">
                    <div class="num-badge" style="width:42px;height:42px;font-size:21px;">1</div>
                    <div>
                      <div style="font-size:21px;font-weight:800;color:#fff;">Always treat every firearm as loaded.</div>
                      <div class="pa-text-sm" style="font-size:20px;">ਹਮੇਸ਼ਾ ਇਹ ਮੰਨ ਕੇ ਚੱਲੋ ਕਿ ਹਥਿਆਰ ਲੋਡ ਹੈ।</div>
                    </div>
                  </div>
                  <div class="card row" style="padding:16px 22px;">
                    <div class="num-badge" style="width:42px;height:42px;font-size:21px;">2</div>
                    <div>
                      <div style="font-size:21px;font-weight:800;color:#fff;">Never point at anything you do not wish to destroy.</div>
                      <div class="pa-text-sm" style="font-size:20px;">ਬੈਰਲ ਦਾ ਮੂੰਹ ਹਮੇਸ਼ਾ ਸੁਰੱਖਿਅਤ ਦਿਸ਼ਾ ਵੱਲ ਰੱਖੋ।</div>
                    </div>
                  </div>
                  <div class="card row" style="padding:16px 22px;">
                    <div class="num-badge" style="width:42px;height:42px;font-size:21px;">3</div>
                    <div>
                      <div style="font-size:21px;font-weight:800;color:#fff;">Keep your finger off the trigger until ready to shoot.</div>
                      <div class="pa-text-sm" style="font-size:20px;">ਟਰਿੱਗਰ 'ਤੇ ਉਂਗਲ ਉਦੋਂ ਹੀ ਰੱਖੋ ਜਦੋਂ ਨਿਸ਼ਾਨਾ ਪੂਰਾ ਹੋਵੇ।</div>
                    </div>
                  </div>
                  <div class="card row" style="padding:16px 22px;">
                    <div class="num-badge" style="width:42px;height:42px;font-size:21px;">4</div>
                    <div>
                      <div style="font-size:21px;font-weight:800;color:#fff;">Know your target and what is beyond it.</div>
                      <div class="pa-text-sm" style="font-size:20px;">ਆਪਣੇ ਨਿਸ਼ਾਨੇ ਅਤੇ ਉਸਦੇ ਪਿੱਛੇ ਦੀ ਜਗ੍ਹਾ ਦਾ ਧਿਆਨ ਰੱਖੋ।</div>
                    </div>
                  </div>
                </div>
                <div class="cta-box" style="padding:20px 26px;">
                  <div>
                    <div class="pa-text-md" style="font-size:24px;">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                    <div style="font-size:18px;font-weight:700;color:#cbd5e1;">Stay Safe, Be Responsible! • Free bilingual PDFs online</div>
                  </div>
                  <div class="url-chip" style="font-size:20px;">sikhrpa.org</div>
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # POST 03 — Sat, Dec 5, 2026 • 10:00 AM PST • Reel (9:16 Cover + 5 Frames)
    # =========================================================================
    post_03 = {
        "number": 3,
        "slug": "post-03-ca-fsc-practice-exam-reel",
        "date_iso": "2026-12-05",
        "date_display": "Sat, Dec 5, 2026",
        "time_pst": "10:00 AM PST",
        "week": 1,
        "format": "Reel (9:16 Cover + 5 Storyboard Frames)",
        "format_type": "reel",
        "title": "Free 30-Question CA FSC Practice Exam (sikhrpa.org/fsc-quiz.html)",
        "url": "https://sikhrpa.org/fsc-quiz.html",
        "caption": (
            "Preparing for your California Firearm Safety Certificate (FSC) exam? Don't walk up to the counter "
            "guessing on California Penal Code rules.\n\n"
            "SikhRPA built a 100% free, interactive 30-Question CA FSC Practice Exam aligned with official "
            "California Department of Justice guidelines:\n"
            "• Full 30-Question Exam or Quick 15-Question Study Mode\n"
            "• 75% Passing Threshold Benchmark (23/30 correct)\n"
            "• Instant Statutory Explanations after every single question\n"
            "• Category Competency Breakdown so you know exactly what to review\n"
            "• Works offline on mobile — zero login or fees required\n\n"
            "Test yourself today at sikhrpa.org/fsc-quiz.html (Link in bio).\n\n"
            "Educational Disclaimer: This practice exam is provided exclusively for public safety education. "
            "Official California FSC certification must be administered in-person at a CA DOJ-licensed dealer.\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #CaliforniaFSC #FirearmSafetyCertificate #CaliforniaCompliance "
            "#FirearmSafetyEducation #SafeStorage #PublicSafetyEducation #StudyGuide "
            "#CaliforniaSikhs #SikhCommunity #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Share this Reel to your Story with a Link sticker to https://sikhrpa.org/fsc-quiz.html "
            "and a Slider/Poll sticker: 'Could you score 75%+ on the 30-question CA FSC safety test today?' "
            "(Options: 'Easy 100%!' / 'Let me practice first!')."
        ),
        "slides": [
            {
                "filename": "reel-00-cover.png",
                "width": 1080,
                "height": 1920,
                "theme": "royal",
                "frame_variant": "reel-cover",
                "pill_text": "Reel • Free Exam Prep",
                "slide_label": "REEL COVER",
                "footer_url": "sikhrpa.org/fsc-quiz.html",
                "footer_right": "WATCH REEL ▶",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:142px;height:142px;border-width:3.5px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">CA DOJ Standard Model • 100% Free</div>
                  <h1 class="h1-hero" style="font-size:66px;">Pass the <span class="gold">CA FSC Exam</span><br/>on Your First Try</h1>
                  <p class="lead" style="font-size:28px;max-width:840px;">
                    Free 30-Question Interactive California Firearm Safety Certificate Practice Test with instant legal explanations.
                  </p>
                  <div class="stat-row" style="width:100%;margin-top:8px;">
                    <div class="stat-box">
                      <div class="stat-val">30 Qs</div>
                      <div class="stat-lbl">Full State Model</div>
                    </div>
                    <div class="stat-box">
                      <div class="stat-val">75%+</div>
                      <div class="stat-lbl">Passing Score</div>
                    </div>
                    <div class="stat-box">
                      <div class="stat-val">$0</div>
                      <div class="stat-lbl">Always Free</div>
                    </div>
                  </div>
                  <div class="url-chip" style="font-size:26px;padding:16px 32px;margin-top:8px;">sikhrpa.org/fsc-quiz.html</div>
                </div>
                """,
            },
            {
                "filename": "reel-01-hook.png",
                "width": 1080,
                "height": 1920,
                "theme": "royal",
                "pill_text": "Frame 1 • 0:00–0:04 Hook",
                "slide_label": "01 / 05",
                "footer_url": "sikhrpa.org/fsc-quiz.html",
                "footer_right": "STORYBOARD 1/5",
                "body_html": """
                <div class="eyebrow">Hook • 0:00 – 0:04</div>
                <h1 class="h1-hero" style="font-size:66px;">Taking California's <span class="gold">FSC Safety Exam</span> Soon?</h1>
                <p class="lead" style="font-size:30px;">
                  Under <strong style="color:#fff;">CA Penal Code § 31615</strong>, almost every new owner must pass a 30-question written safety exam before initiating a transfer.
                </p>
                <div class="card card-gold stack" style="padding:32px;">
                  <div class="row" style="justify-content:space-between;border-bottom:1px solid rgba(255,255,255,0.12);padding-bottom:18px;">
                    <span style="font-size:24px;font-weight:700;color:#cbd5e1;">Official State Fee</span>
                    <span style="font-size:32px;font-weight:900;color:#fbbf24;">$25</span>
                  </div>
                  <div class="row" style="justify-content:space-between;border-bottom:1px solid rgba(255,255,255,0.12);padding-bottom:18px;">
                    <span style="font-size:24px;font-weight:700;color:#cbd5e1;">Format</span>
                    <span style="font-size:28px;font-weight:900;color:#fff;">30 Multiple Choice &amp; T/F</span>
                  </div>
                  <div class="row" style="justify-content:space-between;border-bottom:1px solid rgba(255,255,255,0.12);padding-bottom:18px;">
                    <span style="font-size:24px;font-weight:700;color:#cbd5e1;">Minimum Passing Score</span>
                    <span style="font-size:30px;font-weight:900;color:#34d399;">75% (23 / 30)</span>
                  </div>
                  <div class="row" style="justify-content:space-between;">
                    <span style="font-size:24px;font-weight:700;color:#cbd5e1;">Certificate Validity</span>
                    <span style="font-size:30px;font-weight:900;color:#93c5fd;">5 Full Years</span>
                  </div>
                </div>
                <div class="pa-banner">
                  <div class="pa-text-md">ਕੈਲੀਫੋਰਨੀਆ ਫਾਇਰਆਰਮ ਸੇਫਟੀ ਸਰਟੀਫਿਕੇਟ (FSC) ਪ੍ਰੀਖਿਆ ਦੀ ਮੁਫ਼ਤ ਤਿਆਰੀ ਕਰੋ।</div>
                </div>
                """,
            },
            {
                "filename": "reel-02-problem.png",
                "width": 1080,
                "height": 1920,
                "theme": "default",
                "pill_text": "Frame 2 • 0:04–0:10",
                "slide_label": "02 / 05",
                "footer_url": "sikhrpa.org/fsc-quiz.html",
                "footer_right": "STORYBOARD 2/5",
                "body_html": """
                <div class="eyebrow">Common Pitfalls • 0:04 – 0:10</div>
                <h2 class="h1-hero" style="font-size:58px;">4 Topics That Trip Up <span class="gold">First-Time Test Takers</span></h2>
                <p class="lead">Don't fail at the counter over California-specific legal details:</p>
                <div class="stack" style="gap:20px;">
                  <div class="card card-red row" style="padding:26px;">
                    <div class="num-badge num-badge-red">1</div>
                    <div class="stack-sm">
                      <div class="h3-title">Criminal Storage Felonies (PC § 25100)</div>
                      <p class="body-text">Hiding an unlocked firearm in a closet or high shelf is NOT a legal defense when minors are present.</p>
                    </div>
                  </div>
                  <div class="card card-gold row" style="padding:26px;">
                    <div class="num-badge">2</div>
                    <div class="stack-sm">
                      <div class="h3-title">Vehicle Transport Laws (PC § 25610)</div>
                      <p class="body-text">Handguns must be unloaded in a locked container or trunk — NEVER the glovebox or center console.</p>
                    </div>
                  </div>
                  <div class="card card-blue row" style="padding:26px;">
                    <div class="num-badge num-badge-blue">3</div>
                    <div class="stack-sm">
                      <div class="h3-title">Safe Handling &amp; Clearing Steps</div>
                      <p class="body-text">Always point in a safe direction, remove magazine first, then lock slide open and check the chamber.</p>
                    </div>
                  </div>
                  <div class="card row" style="padding:26px;">
                    <div class="num-badge">4</div>
                    <div class="stack-sm">
                      <div class="h3-title">Age &amp; Waiting Period Statutes</div>
                      <p class="body-text">Understanding California's 21+ rules, exact 240-hour waiting periods, and statutory exemptions.</p>
                    </div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "reel-03-sample-question.png",
                "width": 1080,
                "height": 1920,
                "theme": "default",
                "pill_text": "Frame 3 • 0:10–0:17 Demo",
                "slide_label": "03 / 05",
                "footer_url": "sikhrpa.org/fsc-quiz.html",
                "footer_right": "STORYBOARD 3/5",
                "body_html": """
                <div class="eyebrow">Live Quiz Preview • 0:10 – 0:17</div>
                <h2 class="h1-lg">Instant <span class="gold">Statutory Feedback</span> on Every Question</h2>
                <div class="card card-blue stack" style="padding:32px;gap:20px;">
                  <div class="row" style="justify-content:space-between;">
                    <span class="pill pill-blue" style="font-size:14px;">Question 14 of 30 • Safe Storage</span>
                    <span style="font-size:18px;font-weight:800;color:#fbbf24;">Score: 13 / 13</span>
                  </div>
                  <div style="font-size:28px;font-weight:800;line-height:1.3;color:#fff;">
                    Under California Penal Code § 25100, is hiding an unloaded firearm on a high closet shelf sufficient legal protection if a child accesses it?
                  </div>
                  <div class="stack-sm" style="gap:14px;">
                    <div class="card" style="padding:18px 22px;opacity:0.6;">
                      <span style="font-size:22px;font-weight:700;">A. Yes, if the ammunition is in another drawer</span>
                    </div>
                    <div class="card card-emerald" style="padding:20px 22px;border-width:2.5px;">
                      <span style="font-size:22px;font-weight:900;color:#a7f3d0;">✓ B. No — it must be locked in a DOJ-approved container or with a certified locking device</span>
                    </div>
                    <div class="card" style="padding:18px 22px;opacity:0.6;">
                      <span style="font-size:22px;font-weight:700;">C. Yes, if the child has been warned not to touch it</span>
                    </div>
                  </div>
                  <div class="card" style="background:rgba(15,23,42,0.9);border-left:5px solid #34d399;padding:20px;">
                    <div class="emerald" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">EXPLANATION (CA PC § 25100 &amp; § 25140)</div>
                    <p class="body-sm" style="margin-top:6px;">
                      California law requires firearms in residences where minors may gain access to be secured with a DOJ-approved safety device or locked container.
                    </p>
                  </div>
                </div>
                """,
            },
            {
                "filename": "reel-04-features.png",
                "width": 1080,
                "height": 1920,
                "theme": "royal",
                "pill_text": "Frame 4 • 0:17–0:24",
                "slide_label": "04 / 05",
                "footer_url": "sikhrpa.org/fsc-quiz.html",
                "footer_right": "STORYBOARD 4/5",
                "body_html": """
                <div class="eyebrow">Built for Real Mastery • 0:17 – 0:24</div>
                <h2 class="h1-hero" style="font-size:58px;">Everything Inside Our <span class="gold">Free Study Engine</span></h2>
                <div class="stack" style="gap:20px;margin-top:8px;">
                  <div class="card card-gold row" style="padding:28px;">
                    <span class="icon-ok" style="width:42px;height:42px;font-size:22px;">✓</span>
                    <div>
                      <div class="h3-title">Full 30-Q Exam &amp; Quick 15-Q Drill</div>
                      <p class="body-text">Randomized question order every attempt so you actually learn the law — not just answer letters.</p>
                    </div>
                  </div>
                  <div class="card card-blue row" style="padding:28px;">
                    <span class="icon-ok" style="width:42px;height:42px;font-size:22px;">✓</span>
                    <div>
                      <div class="h3-title">Category Competency Breakdown</div>
                      <p class="body-text">Instantly pinpoints weak areas across Safety Rules, Storage Laws, Handling, and Penal Codes.</p>
                    </div>
                  </div>
                  <div class="card row" style="padding:28px;">
                    <span class="icon-ok" style="width:42px;height:42px;font-size:22px;">✓</span>
                    <div>
                      <div class="h3-title">Offline Mode + Local Progress History</div>
                      <p class="body-text">Study on your phone anywhere with zero ads, zero tracking, and direct access to the official CA DOJ Study Guide PDF.</p>
                    </div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "reel-05-cta.png",
                "width": 1080,
                "height": 1920,
                "theme": "royal",
                "pill_text": "Frame 5 • 0:24–0:30 CTA",
                "slide_label": "05 / 05",
                "footer_url": "sikhrpa.org/fsc-quiz.html",
                "footer_right": "LINK IN BIO",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:150px;height:150px;border-width:3.5px;" src="{logo}" alt="SikhRPA"/>
                  <div class="eyebrow">Practice Before You Go</div>
                  <h2 class="h1-hero" style="font-size:64px;">Take the Free <span class="gold">30-Q Practice Exam</span> Now</h2>
                  <p class="lead" style="font-size:29px;max-width:840px;">
                    Save this Reel, tag a friend preparing for their California FSC, and tap the link in bio.
                  </p>
                  <div class="url-chip" style="font-size:28px;padding:18px 36px;">sikhrpa.org/fsc-quiz.html</div>
                  <div class="pa-banner" style="width:100%;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;">
                    <div class="pa-text-lg">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                    <div style="font-size:20px;font-weight:800;color:#cbd5e1;margin-top:4px;">STAY SAFE, BE RESPONSIBLE!</div>
                  </div>
                  <div class="disclaimer-note" style="font-size:16px;text-align:left;">
                    <strong>Educational Disclaimer:</strong> Provided exclusively for public safety education by SikhRPA (501(c)(3), EIN 42-2595402).
                    Official California FSC certification must be administered in-person at a CA DOJ-licensed dealer.
                  </div>
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # POST 04 — Tue, Dec 8, 2026 • 12:00 PM PST • 7-Slide Carousel (4:5)
    # =========================================================================
    post_04 = {
        "number": 4,
        "slug": "post-04-ca-first-time-buyer-roadmap",
        "date_iso": "2026-12-08",
        "date_display": "Tue, Dec 8, 2026",
        "time_pst": "12:00 PM PST",
        "week": 2,
        "format": "Carousel (7 slides, 4:5)",
        "format_type": "carousel",
        "title": "California First-Time Buyer's Compliance Roadmap (REAL ID, Residency & DROS)",
        "url": "https://sikhrpa.org/buyer-guide.html",
        "caption": (
            "California has some of the most specific statutory documentation rules in the nation — and simple "
            "paperwork oversights are the #1 reason lawful first-time applicants get turned away at the counter.\n\n"
            "Swipe through SikhRPA's 5-Step California Compliance Roadmap to prepare every document properly:\n"
            "1. Primary ID (CA PC § 26845): Check the top-right corner of your CA Driver's License! If it says "
            "'FEDERAL LIMITS APPLY' instead of displaying the REAL ID Golden Bear & Star, you MUST bring an "
            "unexpired U.S. Passport, certified U.S. Birth Certificate, or valid Green Card (Form I-551).\n"
            "2. Handgun Proof of Residency (11 CCR § 4045.1): Current DMV registration, municipal utility bill "
            "(≤90 days), signed residential lease, or property deed matching your ID address. Cell phone bills, "
            "bank statements, and internet/cable bills are strictly rejected.\n"
            "3. Firearm Safety Certificate (CA PC § 31615): 30-question exam (75% passing, $25 fee, valid 5 years).\n"
            "4. Exact 10-Day (240-Hour) DROS Wait (CA PC § 26815 & § 28220): Counted to the exact second, with a "
            "hard 30-day pickup expiration window.\n"
            "5. Delivery & Legal Transport (CA PC § 26850 & § 25610): Complete the Safe Handling Demonstration, "
            "verify a DOJ-approved lock/safe affidavit, and transport unloaded inside a locked container or trunk.\n\n"
            "Use the interactive counter-readiness self-audit checklist free at sikhrpa.org/buyer-guide.html (Link in bio).\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #CaliforniaCompliance #CAFirstTimeGuide #REALID #CaliforniaLaw "
            "#FirearmSafetyEducation #SafeStorage #SafeTransport #CaliforniaSikhs "
            "#SikhCommunity #PunjabiCommunity #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Share Slide 2 (the CA 'FEDERAL LIMITS APPLY' vs. REAL ID visual comparison) to your Story "
            "with a Poll: 'Did you know about the CA Federal Limits Apply ID rule?' "
            "(Options: 'Yes, I knew!' / 'Good thing I checked!') + Link sticker to https://sikhrpa.org/buyer-guide.html."
        ),
        "slides": [
            {
                "filename": "slide-01-cover.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "CA DOJ Compliance Guide",
                "slide_label": "01 / 07",
                "footer_url": "sikhrpa.org/buyer-guide.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">California Statutory Progression</div>
                <h1 class="h1-hero">California First-Time <span class="gold">Compliance Roadmap</span></h1>
                <p class="lead">
                  The 5 sequential legal steps required under California Penal Code — avoid preventable paperwork rejections before visiting a licensed dealer.
                </p>
                <div class="pa-banner">
                  <div class="pa-text-md">ਕੈਲੀਫੋਰਨੀਆ ਕਾਨੂੰਨੀ ਦਸਤਾਵੇਜ਼ ਅਤੇ ਸੁਰੱਖਿਆ ਪਾਲਣਾ ਗਾਈਡ (REAL ID • ਰਿਹਾਇਸ਼ੀ ਸਬੂਤ • FSC • 10-ਦਿਨ DROS)</div>
                </div>
                <div class="stack-sm" style="margin-top:4px;">
                  <div class="card row" style="padding:14px 20px;"><div class="num-badge" style="width:38px;height:38px;font-size:19px;">1</div><span style="font-size:21px;font-weight:800;">REAL ID vs. "FEDERAL LIMITS APPLY" Check</span></div>
                  <div class="card row" style="padding:14px 20px;"><div class="num-badge" style="width:38px;height:38px;font-size:19px;">2</div><span style="font-size:21px;font-weight:800;">Handgun Secondary Proof of Residency (11 CCR § 4045.1)</span></div>
                  <div class="card row" style="padding:14px 20px;"><div class="num-badge" style="width:38px;height:38px;font-size:19px;">3</div><span style="font-size:21px;font-weight:800;">Firearm Safety Certificate (FSC — 30 Questions)</span></div>
                  <div class="card row" style="padding:14px 20px;"><div class="num-badge" style="width:38px;height:38px;font-size:19px;">4</div><span style="font-size:21px;font-weight:800;">DROS Screening &amp; Exact 10-Day (240-Hour) Wait</span></div>
                  <div class="card row" style="padding:14px 20px;"><div class="num-badge" style="width:38px;height:38px;font-size:19px;">5</div><span style="font-size:21px;font-weight:800;">Safe Handling Demo, DOJ Lock &amp; Legal Transport</span></div>
                </div>
                """,
            },
            {
                "filename": "slide-02-real-id-comparison.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Step 1 • CA PC § 26845",
                "slide_label": "02 / 07",
                "footer_url": "sikhrpa.org/buyer-guide.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="eyebrow">Step 1 • Primary Identity Check</div>
                <h2 class="h2-title">The CA <span class="red-lt">"Federal Limits Apply"</span> vs. <span class="emerald">REAL ID</span> Rule</h2>
                <div class="diagram-wrap" style="padding:14px;">
                  {svg_real_id_comparison()}
                </div>
                <div class="card card-gold" style="padding:18px 24px;">
                  <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;margin-bottom:8px;">
                    IF YOUR LICENSE SAYS "FEDERAL LIMITS APPLY", BRING ONE OF THESE:
                  </div>
                  <div class="grid-2" style="gap:10px;font-size:18px;font-weight:700;color:#f8fafc;">
                    <div>✓ Unexpired U.S. Passport / Card</div>
                    <div>✓ Certified U.S. Birth Certificate</div>
                    <div>✓ Valid Permanent Resident Card (I-551)</div>
                    <div>✓ Certificate of Naturalization / Citizenship</div>
                  </div>
                </div>
                <div class="pa-banner" style="padding:14px 20px;">
                  <div class="pa-text-sm">ਪੰਜਾਬੀ ਨੋਟ: ਜੇ ਤੁਹਾਡੇ ਲਾਇਸੈਂਸ 'ਤੇ "Federal Limits Apply" ਲਿਖਿਆ ਹੈ, ਤਾਂ ਅਮਰੀਕੀ ਪਾਸਪੋਰਟ, ਜਨਮ ਸਰਟੀਫਿਕੇਟ ਜਾਂ ਗ੍ਰੀਨ ਕਾਰਡ ਨਾਲ ਲੈ ਕੇ ਜਾਣਾ ਲਾਜ਼ਮੀ ਹੈ।</div>
                </div>
                """,
            },
            {
                "filename": "slide-03-proof-of-residency.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Step 2 • 11 CCR § 4045.1",
                "slide_label": "03 / 07",
                "footer_url": "sikhrpa.org/buyer-guide.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Step 2 • Handguns Mandatory</div>
                <h2 class="h1-lg">Secondary Proof of <span class="gold">CA Residency</span></h2>
                <p class="body-text">
                  Name and street address must match your California Driver's License <strong style="color:#fff;">letter-for-letter</strong>.
                </p>
                <div class="grid-2" style="margin-top:4px;">
                  <div class="card card-emerald stack" style="padding:24px;">
                    <div class="emerald" style="font-size:18px;font-weight:900;letter-spacing:0.06em;">✓ ACCEPTED BY CA DOJ</div>
                    <ul class="check-list">
                      <li><span class="icon-ok">✓</span><span><strong>Current DMV Vehicle Registration</strong> (most reliable!)</span></li>
                      <li><span class="icon-ok">✓</span><span><strong>Municipal Utility Bill</strong> (City Water, Trash, PG&amp;E, SMUD, LADWP — within 90 days)</span></li>
                      <li><span class="icon-ok">✓</span><span><strong>Signed Residential Lease</strong> (signed &amp; dated by tenant and landlord)</span></li>
                      <li><span class="icon-ok">✓</span><span><strong>Gov't Property Deed</strong> or County Property Tax Bill</span></li>
                    </ul>
                  </div>
                  <div class="card card-red stack" style="padding:24px;">
                    <div class="red-lt" style="font-size:18px;font-weight:900;letter-spacing:0.06em;">✗ STRICTLY REJECTED</div>
                    <ul class="check-list">
                      <li><span class="icon-no">✗</span><span><strong>Cell Phone Bills</strong> (Verizon, AT&amp;T, T-Mobile) — prohibited by statute</span></li>
                      <li><span class="icon-no">✗</span><span><strong>Bank or Credit Card Statements</strong> (even if stamped)</span></li>
                      <li><span class="icon-no">✗</span><span><strong>Cable TV / Home Internet Bills</strong> (Comcast, Spectrum)</span></li>
                      <li><span class="icon-no">✗</span><span><strong>Pay Stubs or W-2 Forms</strong> (not recognized under 11 CCR § 4045.1)</span></li>
                    </ul>
                  </div>
                </div>
                <div class="card card-blue" style="padding:18px 24px;">
                  <div style="font-size:18px;color:#dbeafe;line-height:1.45;">
                    <strong class="gold">Recently Moved?</strong> Update your address in the CA DMV system first and bring a current DMV printout or updated vehicle registration showing your current home address.
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-04-fsc-exam.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Step 3 • CA PC § 31615",
                "slide_label": "04 / 07",
                "footer_url": "sikhrpa.org/fsc-quiz.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Step 3 • Written Safety Certification</div>
                <h2 class="h1-lg">Firearm Safety <span class="gold">Certificate (FSC)</span></h2>
                <p class="lead">
                  Required before acquiring any firearm in California unless you hold a statutory exemption (e.g., valid CCW permit, active peace officer, or active military with ID).
                </p>
                <div class="stat-row">
                  <div class="stat-box">
                    <div class="stat-val">$25</div>
                    <div class="stat-lbl">State Exam Fee</div>
                  </div>
                  <div class="stat-box">
                    <div class="stat-val">30 Qs</div>
                    <div class="stat-lbl">75% to Pass</div>
                  </div>
                  <div class="stat-box">
                    <div class="stat-val">5 Years</div>
                    <div class="stat-lbl">Valid Duration</div>
                  </div>
                </div>
                <div class="card card-gold stack-sm" style="padding:26px;">
                  <div class="h3-title">What the Written Exam Covers</div>
                  <ul class="check-list" style="margin-top:6px;">
                    <li><span class="icon-gold">1</span><span>The 4 Universal Firearm Safety Rules &amp; safe handling mechanics</span></li>
                    <li><span class="icon-gold">2</span><span>California criminal safe storage laws (PC § 25100) &amp; child protection</span></li>
                    <li><span class="icon-gold">3</span><span>Legal vehicle transportation, age limits &amp; statutory transfers</span></li>
                  </ul>
                </div>
                <div class="cta-box" style="padding:20px 26px;">
                  <div>
                    <div style="font-size:22px;font-weight:900;color:#fff;">Practice All 30 Questions Free Before You Go</div>
                    <div style="font-size:17px;color:#cbd5e1;">Instant statutory explanations • Offline mobile ready</div>
                  </div>
                  <div class="url-chip" style="font-size:19px;">sikhrpa.org/fsc-quiz.html</div>
                </div>
                """,
            },
            {
                "filename": "slide-05-dros-timeline.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Step 4 • PC § 26815 & § 28220",
                "slide_label": "05 / 07",
                "footer_url": "sikhrpa.org/buyer-guide.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="eyebrow">Step 4 • Background Screening &amp; Statutory Wait</div>
                <h2 class="h1-lg">DROS &amp; The Exact <span class="gold">10-Day (240-Hour)</span> Timeline</h2>
                <p class="body-text">
                  California mandates ten full 24-hour periods — counted <strong style="color:#fff;">down to the exact second</strong> from your Dealer's Record of Sale (DROS) submission timestamp.
                </p>
                <div class="diagram-wrap" style="padding:16px;">
                  {svg_dros_timeline()}
                </div>
                <div class="grid-2">
                  <div class="card card-gold stack-sm" style="padding:18px 22px;">
                    <div class="gold" style="font-size:15px;font-weight:900;">VERIFY EVERY LETTER AT DAY 0</div>
                    <p class="body-sm">A misspelled street name, missing apartment number, or wrong middle initial on Form 4473 / DROS triggers a DOJ delay or rejection.</p>
                  </div>
                  <div class="card card-red stack-sm" style="padding:18px 22px;">
                    <div class="red-lt" style="font-size:15px;font-weight:900;">DON'T MISS DAY 30</div>
                    <p class="body-sm">If you do not pick up within 30 calendar days of DROS submission, the application expires by law and the full 10-day process restarts.</p>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-06-delivery-transport.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Step 5 • PC § 26850 & § 25610",
                "slide_label": "06 / 07",
                "footer_url": "sikhrpa.org/buyer-guide.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Step 5 • Delivery &amp; Going Home Legally</div>
                <h2 class="h1-lg">Safe Handling Demo, <span class="gold">DOJ Lock &amp; Transport</span></h2>
                <div class="stack">
                  <div class="card card-blue stack-sm" style="padding:22px 26px;">
                    <div class="row" style="justify-content:space-between;">
                      <div class="h3-title" style="font-size:26px;">1. Safe Handling Demonstration (PC § 26850)</div>
                      <span class="pill pill-blue" style="font-size:13px;">Inert Dummy Round</span>
                    </div>
                    <p class="body-sm">In front of a DOJ-certified instructor: verify clear &amp; lock action open → load &amp; chamber dummy round → safely eject dummy round → apply locking device.</p>
                  </div>
                  <div class="card card-gold stack-sm" style="padding:22px 26px;">
                    <div class="h3-title" style="font-size:26px;">2. Firearm Safety Device Mandate (PC § 23635)</div>
                    <p class="body-sm">Every firearm leaving a dealer must have a CA DOJ-certified locking device (usually included in box) or a signed approved Safe Affidavit verifying a compliant home safe.</p>
                  </div>
                  <div class="card card-emerald stack-sm" style="padding:22px 26px;">
                    <div class="h3-title" style="font-size:26px;">3. Legal Vehicle Transport Home (PC § 25610)</div>
                    <ul class="check-list" style="margin-top:4px;">
                      <li><span class="icon-ok">✓</span><span>Completely <strong>UNLOADED</strong> inside a fully <strong>locked container</strong> or vehicle trunk.</span></li>
                      <li><span class="icon-no">✗</span><span><strong>NEVER</strong> place a handgun in the glove compartment or center console (even if locked).</span></li>
                    </ul>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-07-checklist-cta.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Counter-Readiness Audit",
                "slide_label": "07 / 07",
                "footer_url": "sikhrpa.org/buyer-guide.html",
                "footer_right": "SAVE & SHARE",
                "body_html": """
                <div class="eyebrow">Before You Leave Home</div>
                <h2 class="h1-lg">5-Item <span class="gold">Compliance Checklist</span></h2>
                <div class="card stack" style="padding:28px;">
                  <ul class="check-list" style="gap:16px;">
                    <li><span class="icon-ok">1</span><span><strong>Unexpired CA Driver's License / ID</strong> (+ U.S. Passport, Birth Cert., or Green Card if "Federal Limits Apply")</span></li>
                    <li><span class="icon-ok">2</span><span><strong>Handgun Proof of Residency</strong> (DMV Reg, Municipal Utility Bill ≤90d, or Signed Lease — exact matching address)</span></li>
                    <li><span class="icon-ok">3</span><span><strong>Active FSC Card</strong> (or statutory exemption / ready for 30-question exam)</span></li>
                    <li><span class="icon-ok">4</span><span><strong>State DROS Screening Fee (~$37.19)</strong> &amp; calendar reminder for Day 10–30 pickup window</span></li>
                    <li><span class="icon-ok">5</span><span><strong>Locked Transport Container or Clear Trunk</strong> ready in your vehicle on pickup day</span></li>
                  </ul>
                </div>
                <div class="cta-box">
                  <div>
                    <div style="font-size:24px;font-weight:900;color:#fff;">Interactive Bilingual Checklist &amp; FAQs</div>
                    <div class="pa-text-sm" style="margin-top:4px;">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Free community legal resource</div>
                  </div>
                  <div class="url-chip" style="font-size:19px;">sikhrpa.org/buyer-guide.html</div>
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # POST 05 — Thu, Dec 10, 2026 • 6:00 PM PST • 6-Slide Carousel (4:5)
    # =========================================================================
    post_05 = {
        "number": 5,
        "slug": "post-05-holiday-safe-storage-pc25100",
        "date_iso": "2026-12-10",
        "date_display": "Thu, Dec 10, 2026",
        "time_pst": "6:00 PM PST",
        "week": 2,
        "format": "Carousel (6 slides, 4:5)",
        "format_type": "carousel",
        "title": "Holiday Safe Storage, CA Penal Code § 25100 & 3-Minute Pre-Guest Audit",
        "url": "https://sikhrpa.org/",
        "caption": (
            "Hosting family, friends, and visiting children this holiday season? Take 3 minutes to audit "
            "your home firearm storage BEFORE guests arrive.\n\n"
            "Under California Penal Code § 25100 and § 25140, criminal storage of an unsecured firearm where a "
            "minor under 18 or prohibited person gains access and causes harm is a serious felony. Hiding a firearm "
            "on a high closet shelf or inside a nightstand drawer is NOT a legal defense — and never keeps curious children safe.\n\n"
            "Swipe through for:\n"
            "• CA Penal Code § 25100 & § 25140 summary in English & Gurmukhi\n"
            "• The 3 Levels of CA DOJ-Approved Safe Storage (Cable Lock • Biometric Lockbox • Fire-Rated Steel Safe)\n"
            "• The 3-Minute Pre-Guest Home Safety Audit checklist\n"
            "• The 4 Essential Safety Rules for Kids (STOP • Don't Touch • Leave Area • Tell an Adult / ੧. ਰੁਕੋ • ੨. ਹੱਥ ਨਾ ਲਾਓ • ੩. ਦੂਰ ਹਟੋ • ੪. ਵੱਡਿਆਂ ਨੂੰ ਦੱਸੋ)\n\n"
            "Need a CA DOJ-approved cable lock? SikhRPA distributes free cable safety locks at every community workshop. "
            "Email president@sikhrpa.org or visit sikhrpa.org (Link in bio).\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #SafeStorage #HolidaySafety #ChildSafety #CaliforniaLaw #PC25100 "
            "#FirearmSafetyEducation #HomeSafety #PublicSafetyEducation #SikhCommunity "
            "#CaliforniaSikhs #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Repost Slide 4 (the 3-Minute Pre-Guest Safety Audit) to your Story with a reminder: "
            "'Hosting family this December? Screenshot this 3-minute safe storage check!' "
            "Include a Question sticker: 'Need a free CA DOJ cable lock for your household? DM or email president@sikhrpa.org.'"
        ),
        "slides": [
            {
                "filename": "slide-01-cover.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Holiday Family Safety",
                "slide_label": "01 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Holiday Hosting Safety • CA PC § 25100</div>
                <h1 class="h1-hero">Holiday Guests Visiting?<br/><span class="gold">Lock Every Firearm First.</span></h1>
                <p class="lead">
                  Family gatherings bring curious children, visiting relatives, and busy rooms.
                  Protect your loved ones with California's safe storage standard and our <strong style="color:#fff;">3-Minute Pre-Guest Audit</strong>.
                </p>
                <div class="pa-banner">
                  <div class="pa-text-lg">ਸੁਰੱਖਿਅਤ ਸਟੋਰੇਜ — ਪਰਿਵਾਰ ਅਤੇ ਬੱਚਿਆਂ ਦੀ ਸੁਰੱਖਿਆ ਸਭ ਤੋਂ ਪਹਿਲਾਂ</div>
                  <div class="pa-text-sm" style="margin-top:6px;color:#e2e8f0;">ਹਥਿਆਰ ਨੂੰ ਸਿਰਫ਼ ਉੱਚੀ ਥਾਂ ਜਾਂ ਅਲਮਾਰੀ ਵਿੱਚ ਲੁਕਾਉਣਾ ਕਾਨੂੰਨੀ ਬਚਾਅ ਨਹੀਂ ਹੈ।</div>
                </div>
                <div class="stat-row" style="margin-top:6px;">
                  <div class="stat-box">
                    <div class="stat-val">PC § 25100</div>
                    <div class="stat-lbl">CA Storage Law</div>
                  </div>
                  <div class="stat-box">
                    <div class="stat-val">3 Min</div>
                    <div class="stat-lbl">Pre-Guest Audit</div>
                  </div>
                  <div class="stat-box">
                    <div class="stat-val">Free</div>
                    <div class="stat-lbl">DOJ Cable Locks</div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-02-pc25100-law.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "California Statute",
                "slide_label": "02 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Know California Law</div>
                <h2 class="h1-lg">CA Safe Storage Law <span class="red-lt">(PC § 25100 &amp; § 25140)</span></h2>
                <div class="card card-red stack-sm" style="padding:26px;">
                  <div class="red-lt" style="font-size:16px;font-weight:900;letter-spacing:0.08em;">CRIMINAL FELONY LIABILITY</div>
                  <p class="body-text" style="color:#f8fafc;">
                    Under <strong>California Penal Code § 25100</strong>, it is a criminal felony to store an unsecured firearm
                    in a location where a child under 18 or prohibited person is likely to gain access and causes death or great bodily injury.
                  </p>
                </div>
                <div class="pa-banner">
                  <div class="pa-text-md">ਜੇਕਰ ਘਰ ਵਿੱਚ ਖੁੱਲ੍ਹਾ ਰੱਖਿਆ ਹਥਿਆਰ ਕਿਸੇ ਬੱਚੇ ਦੇ ਹੱਥ ਲੱਗ ਜਾਵੇ ਅਤੇ ਹਾਦਸਾ ਵਾਪਰੇ, ਤਾਂ ਮਾਲਕ ਵਿਰੁੱਧ ਸੰਗੀਨ ਅਪਰਾਧ (ਫੈਲੋਨੀ) ਦਰਜ ਹੁੰਦਾ ਹੈ।</div>
                </div>
                <div class="grid-2">
                  <div class="card stack-sm" style="padding:20px 22px;">
                    <div class="red-lt" style="font-size:15px;font-weight:900;">✗ NOT LEGAL STORAGE</div>
                    <p class="body-sm">Unlocked nightstand drawer, top closet shelf, under a mattress, or hidden inside luggage.</p>
                  </div>
                  <div class="card card-emerald stack-sm" style="padding:20px 22px;">
                    <div class="emerald" style="font-size:15px;font-weight:900;">✓ LEGAL COMPLIANCE</div>
                    <p class="body-sm">Secured inside a CA DOJ-certified locked container, gun safe, or with an approved locking device.</p>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-03-three-storage-levels.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "CA DOJ Approved",
                "slide_label": "03 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="eyebrow">3 Levels of Safe Home Storage • ਸਟੋਰੇਜ ਦੇ ੩ ਪੱਧਰ</div>
                <h2 class="h1-lg">Choose the Right <span class="gold">Protection Tier</span></h2>
                <div class="stack" style="gap:18px;margin-top:4px;">
                  <div class="card card-gold row" style="padding:22px 26px;">
                    {svg_storage_tier_icon(1)}
                    <div class="stack-sm">
                      <div class="row" style="gap:10px;"><span class="pill" style="font-size:13px;padding:4px 12px;">Level 1</span><span class="pa-text-sm" style="font-size:20px;">ਕੇਬਲ ਲਾਕ</span></div>
                      <div class="h3-title" style="font-size:27px;">CA DOJ Cable Lock</div>
                      <p class="body-sm">Loops directly through the open action/magwell so the firearm cannot chamber or fire. Gifted 100% free at SikhRPA clinics.</p>
                    </div>
                  </div>
                  <div class="card card-blue row" style="padding:22px 26px;">
                    {svg_storage_tier_icon(2)}
                    <div class="stack-sm">
                      <div class="row" style="gap:10px;"><span class="pill pill-blue" style="font-size:13px;padding:4px 12px;">Level 2</span><span class="pa-text-sm" style="font-size:20px;">ਤਾਲਾਬੰਦ ਬਕਸਾ</span></div>
                      <div class="h3-title" style="font-size:27px;">Quick-Access Lockbox</div>
                      <p class="body-sm">Heavy-gauge steel mechanical pushbutton or biometric bedside vault — keeps children out while allowing authorized access.</p>
                    </div>
                  </div>
                  <div class="card row" style="padding:22px 26px;border-color:rgba(245,158,11,0.4);">
                    {svg_storage_tier_icon(3)}
                    <div class="stack-sm">
                      <div class="row" style="gap:10px;"><span class="pill pill-emerald" style="font-size:13px;padding:4px 12px;">Level 3</span><span class="pa-text-sm" style="font-size:20px;">ਲੋਹੇ ਦੀ ਸੇਫ਼</span></div>
                      <div class="h3-title" style="font-size:27px;">Bolted Fire-Rated Steel Safe</div>
                      <p class="body-sm">Gold standard for multi-firearm households — bolted to floor studs, resists fire, burglary, and unauthorized access.</p>
                    </div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-04-pre-guest-audit.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "3-Minute Pre-Guest Audit",
                "slide_label": "04 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Run Before Guests Arrive</div>
                <h2 class="h1-lg">The <span class="gold">3-Minute Pre-Guest</span> Safety Audit</h2>
                <div class="card stack" style="padding:26px 28px;">
                  <ul class="check-list" style="gap:18px;">
                    <li><span class="icon-gold">1</span><span><strong>Account for Every Firearm:</strong> Physically confirm every handgun, rifle, and shotgun is inside a locked safe or DOJ lockbox.</span></li>
                    <li><span class="icon-gold">2</span><span><strong>Check Bedside &amp; Closet Spots:</strong> Zero firearms left in drawers, coat closets, or guest bedrooms where kids play hide-and-seek.</span></li>
                    <li><span class="icon-gold">3</span><span><strong>Secure Keys &amp; Backup Codes:</strong> Never leave safe keys on dressers, key hooks, or easy-to-guess combinations (like birthdays).</span></li>
                    <li><span class="icon-gold">4</span><span><strong>Lock Ammunition Separately:</strong> Store ammunition in a dedicated locked ammo can or separate locked compartment.</span></li>
                    <li><span class="icon-gold">5</span><span><strong>Inspect Vehicles &amp; Range Bags:</strong> Check gloveboxes, trunks, and range bags — never leave firearms unattended in parked cars.</span></li>
                    <li><span class="icon-gold">6</span><span><strong>Brief Visiting Parents:</strong> Confirm every adult in the home knows storage areas are locked and off-limits.</span></li>
                  </ul>
                </div>
                """,
            },
            {
                "filename": "slide-05-child-safety-rules.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Child Safety Protocol",
                "slide_label": "05 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Teach Every Child • ਬੱਚਿਆਂ ਲਈ ੪ ਜ਼ਰੂਰੀ ਨਿਯਮ</div>
                <h2 class="h1-lg">4 Simple Rules for Kids <span class="gold">If They Ever See a Gun</span></h2>
                <p class="body-text">
                  Safe storage is the adult's 100% responsibility — and teaching children these four steps adds a vital second layer of safety anywhere they visit.
                </p>
                <div class="grid-2" style="margin-top:8px;">
                  <div class="card card-red stack-sm" style="padding:26px;text-align:center;">
                    <div style="font-size:48px;font-weight:900;color:#fca5a5;">01</div>
                    <div class="h3-title">STOP</div>
                    <div class="pa-text-lg" style="font-size:30px;">੧. ਰੁਕੋ</div>
                    <p class="body-sm">Freeze immediately — don't step closer or inspect it.</p>
                  </div>
                  <div class="card card-gold stack-sm" style="padding:26px;text-align:center;">
                    <div style="font-size:48px;font-weight:900;color:#fbbf24;">02</div>
                    <div class="h3-title">DON'T TOUCH</div>
                    <div class="pa-text-lg" style="font-size:30px;">੨. ਹੱਥ ਨਾ ਲਾਓ</div>
                    <p class="body-sm">Never pick it up or let another child touch it.</p>
                  </div>
                  <div class="card card-blue stack-sm" style="padding:26px;text-align:center;">
                    <div style="font-size:48px;font-weight:900;color:#93c5fd;">03</div>
                    <div class="h3-title">LEAVE AREA</div>
                    <div class="pa-text-lg" style="font-size:30px;">੩. ਦੂਰ ਹਟੋ</div>
                    <p class="body-sm">Walk away from the room or area right away.</p>
                  </div>
                  <div class="card card-emerald stack-sm" style="padding:26px;text-align:center;">
                    <div style="font-size:48px;font-weight:900;color:#34d399;">04</div>
                    <div class="h3-title">TELL AN ADULT</div>
                    <div class="pa-text-lg" style="font-size:30px;">੪. ਵੱਡਿਆਂ ਨੂੰ ਦੱਸੋ</div>
                    <p class="body-sm">Find a parent, elder, or trusted adult immediately.</p>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-06-free-locks-cta.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Free Community Safety",
                "slide_label": "06 / 06",
                "footer_url": "sikhrpa.org",
                "footer_right": "SAVE & SHARE",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;">
                  <img class="brand-logo" style="width:128px;height:128px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="eyebrow">100% Free Public Safety Service</div>
                  <h2 class="h1-lg">Free CA DOJ Cable Locks<br/><span class="gold">For Every Family</span></h2>
                  <div class="pa-banner" style="width:100%;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;">
                    <div class="pa-text-lg">ਸਾਡੇ ਹਰ ਸੈਮੀਨਾਰ ਵਿੱਚ ਮੁਫ਼ਤ ਕੈਲੀਫੋਰਨੀਆ DOJ ਲਾਕ ਵੰਡੇ ਜਾਂਦੇ ਹਨ।</div>
                  </div>
                  <p class="lead" style="max-width:840px;">
                    Want to sponsor cable safety locks for families or host a free Safe Storage Workshop at your Gurdwara?
                  </p>
                  <div class="grid-2" style="width:100%;">
                    <div class="card card-gold stack-sm" style="padding:22px;">
                      <div class="gold" style="font-size:15px;font-weight:900;">REQUEST A WORKSHOP</div>
                      <div style="font-size:23px;font-weight:900;color:#fff;">president@sikhrpa.org</div>
                      <p class="body-sm">Free bilingual seminars for Gurdwaras &amp; community centers</p>
                    </div>
                    <div class="card card-blue stack-sm" style="padding:22px;">
                      <div class="blue-lt" style="font-size:15px;font-weight:900;">FUND A FAMILY LOCK ($20)</div>
                      <div style="font-size:23px;font-weight:900;color:#fff;">sikhrpa.org/donate.html</div>
                      <p class="body-sm">501(c)(3) tax-deductible • EIN 42-2595402</p>
                    </div>
                  </div>
                  <div style="font-size:21px;font-weight:800;color:#fef3c7;">
                    <span class="gurmukhi">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</span> &nbsp;—&nbsp; Stay Safe, Be Responsible!
                  </div>
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # POST 06 — Sat, Dec 12, 2026 • 10:00 AM PST • Editorial 4:5 + Story Q&A 9:16
    # =========================================================================
    post_06 = {
        "number": 6,
        "slug": "post-06-daily-legal-regulatory-watch",
        "date_iso": "2026-12-12",
        "date_display": "Sat, Dec 12, 2026",
        "time_pst": "10:00 AM PST",
        "week": 2,
        "format": "Single Editorial Graphic (4:5) + Story Q&A Template (9:16)",
        "format_type": "single",
        "title": "California Firearms Legal & Regulatory Watch (sikhrpa.org/news.html)",
        "url": "https://sikhrpa.org/news.html",
        "caption": (
            "California firearm statutes, court injunctions, and CA DOJ Bureau of Firearms bulletins change constantly — "
            "and staying law-abiding starts with reliable, non-sensationalized information.\n\n"
            "SikhRPA maintains a free, automated Daily California Legal & Regulatory Watch archive at "
            "sikhrpa.org/news.html tracking five public categories:\n"
            "• Chaptered California Legislation & Effective Dates\n"
            "• Federal 9th Circuit & District Court Rulings / Stays\n"
            "• Official CA DOJ Bureau of Firearms Regulatory Bulletins\n"
            "• Authoritative State Reporting\n"
            "• Community Safety & Safe Storage Advisories\n\n"
            "Have a general educational question about California safe storage, FSC preparation, or regulatory updates? "
            "Drop it in our Story Q&A box today or comment below so we can cover it in a future educational guide!\n\n"
            "Bookmark the permanent archive: sikhrpa.org/news.html (Link in bio)\n\n"
            "Educational Disclaimer: SikhRPA is an IRS-recognized 501(c)(3) educational nonprofit and does not "
            "provide legal advice or representation. Always consult a qualified California attorney or verify statutes "
            "directly with the California DOJ Bureau of Firearms.\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #CaliforniaLegalWatch #CaliforniaCompliance #RegulatoryUpdate "
            "#PublicSafetyEducation #FirearmSafetyEducation #CaliforniaLaw #CADOJ "
            "#SikhCommunity #CaliforniaSikhs #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Upload story-01-qa-template.png (9:16) to your Instagram Story! Place the native Instagram "
            "'Questions' sticker directly inside the dashed gold interactive box with prompt: "
            "'Ask a CA safety or compliance question!' and add a Link sticker to https://sikhrpa.org/news.html."
        ),
        "slides": [
            {
                "filename": "post-01-editorial.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Daily Legal Watch",
                "slide_label": "EDITORIAL BRIEF",
                "footer_url": "sikhrpa.org/news.html",
                "footer_right": "BOOKMARK & SAVE",
                "body_html": """
                <div class="eyebrow">Automated Public Intelligence • Permanent Archive</div>
                <h1 class="h1-hero" style="font-size:56px;">California Legal &amp; <span class="gold">Regulatory Watch</span></h1>
                <p class="lead">
                  California firearm laws evolve rapidly through chaptered bills, court stays, and DOJ advisories.
                  Stay informed and compliant — without social media rumors.
                </p>
                <div class="card card-blue stack" style="padding:26px;">
                  <div class="gold" style="font-size:16px;font-weight:900;letter-spacing:0.09em;">5 VERIFIED INTELLIGENCE STREAMS AT SIKHRPA.ORG/NEWS.HTML</div>
                  <div class="grid-2" style="gap:14px;">
                    <div class="card" style="padding:16px 18px;background:rgba(15,23,42,0.85);">
                      <div style="font-size:19px;font-weight:900;color:#fbbf24;">01 • Legislation</div>
                      <p class="body-sm" style="font-size:16px;margin-top:4px;">Chaptered California bills, statutory amendments &amp; effective dates.</p>
                    </div>
                    <div class="card" style="padding:16px 18px;background:rgba(15,23,42,0.85);">
                      <div style="font-size:19px;font-weight:900;color:#93c5fd;">02 • Court Rulings</div>
                      <p class="body-sm" style="font-size:16px;margin-top:4px;">9th Circuit decisions, administrative stays &amp; injunctions.</p>
                    </div>
                    <div class="card" style="padding:16px 18px;background:rgba(15,23,42,0.85);">
                      <div style="font-size:19px;font-weight:900;color:#34d399;">03 • CA DOJ Bulletins</div>
                      <p class="body-sm" style="font-size:16px;margin-top:4px;">Bureau of Firearms notices, roster &amp; DROS compliance updates.</p>
                    </div>
                    <div class="card" style="padding:16px 18px;background:rgba(15,23,42,0.85);">
                      <div style="font-size:19px;font-weight:900;color:#e2e8f0;">04 • State &amp; Safety News</div>
                      <p class="body-sm" style="font-size:16px;margin-top:4px;">Authoritative reporting &amp; community safety advisories.</p>
                    </div>
                  </div>
                </div>
                <div class="cta-box" style="padding:18px 24px;">
                  <div>
                    <div style="font-size:21px;font-weight:900;color:#fff;">Searchable Daily Regulatory Archive</div>
                    <div style="font-size:16px;color:#cbd5e1;">Free public safety education • Zero paywall</div>
                  </div>
                  <div class="url-chip" style="font-size:19px;">sikhrpa.org/news.html</div>
                </div>
                <div class="disclaimer-note">
                  <strong>Educational Notice (Not Legal Counsel):</strong> Aggregated for 501(c)(3) public education only. Always verify current statutes with the California DOJ Bureau of Firearms or consult a qualified California attorney.
                </div>
                """,
            },
            {
                "filename": "story-01-qa-template.png",
                "width": 1080,
                "height": 1920,
                "theme": "royal",
                "frame_variant": "story-frame",
                "pill_text": "Instagram Story • Q&A",
                "slide_label": "STORY Q&A",
                "footer_url": "sikhrpa.org/news.html",
                "footer_right": "TAP LINK STICKER ↑",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:120px;height:120px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">Saturday Compliance Q&amp;A</div>
                  <h1 class="h1-hero" style="font-size:62px;">California Safety &amp; <span class="gold">Compliance Q&amp;A</span></h1>
                  <p class="lead" style="font-size:27px;max-width:840px;">
                    Questions about CA safe storage (PC § 25100), FSC exam prep, REAL ID rules, or our Daily Legal Watch?
                  </p>
                  <div class="sticker-zone" style="width:100%;min-height:360px;">
                    <div style="font-size:20px;font-weight:900;letter-spacing:0.12em;color:#fbbf24;text-transform:uppercase;">
                      [ Place Instagram Question Sticker Here ]
                    </div>
                    <div style="font-size:28px;font-weight:800;color:#fff;max-width:700px;">
                      "Drop a California safety or compliance question for our next educational post!"
                    </div>
                    <div style="font-size:18px;color:#94a3b8;">
                      Educational information only — not individual legal advice
                    </div>
                  </div>
                  <div class="card card-blue" style="width:100%;padding:22px 28px;">
                    <div style="font-size:22px;font-weight:800;color:#dbeafe;">Read today's daily regulatory sweep:</div>
                    <div style="font-size:28px;font-weight:900;color:#fbbf24;margin-top:6px;">sikhrpa.org/news.html</div>
                  </div>
                  <div class="pa-text-md">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                </div>
                """,
            },
        ],
    }

    return [post_01, post_02, post_03, post_04, post_05, post_06]
