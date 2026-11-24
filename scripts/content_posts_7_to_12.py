"""
SikhRPA 4-Week Instagram Series — Posts 07 through 12 (Dec 15 – Dec 26, 2026)
Grounded in Sikhrpa/sikhrpa official brand guidelines, bilingual Gurmukhi copy,
technical SVG diagrams, and Meta firearm-education policy guardrails.
"""

from __future__ import annotations

from diagrams import (
    svg_centroid_triangulation,
    svg_click_scaling_cone,
    svg_dignified_divider,
    svg_height_over_bore,
    svg_moa_vs_mil,
    svg_shot_clock_dial,
    svg_tourniquet_diagram,
    svg_trigger_finger_zones,
)
from styles import get_logo_data_uri


def get_posts_7_to_12() -> list[dict]:
    logo = get_logo_data_uri()

    # =========================================================================
    # POST 07 — Tue, Dec 15, 2026 • 12:00 PM PST • Reel (9:16 Cover + 5 Frames)
    # =========================================================================
    post_07 = {
        "number": 7,
        "slug": "post-07-pistol-shot-diagnostic-reel",
        "date_iso": "2026-12-15",
        "date_display": "Tue, Dec 15, 2026",
        "time_pst": "12:00 PM PST",
        "week": 3,
        "format": "Reel (9:16 Cover + 5 Storyboard Frames)",
        "format_type": "reel",
        "title": "Interactive Pistol Shot Diagnostic — Fixing Low-Left (7–8 O'Clock)",
        "url": "https://sikhrpa.org/shot-diagnosis.html",
        "caption": (
            "Are your pistol shots consistently landing low and to the left (7:00–8:00 o'clock)? "
            "Nearly 85% of right-handed shooters experience this exact pattern — and it is almost never your sights.\n\n"
            "What's really happening biomechanically:\n"
            "1. Sympathetic Grip Squeeze: As your index finger presses the trigger, your bottom three fingers "
            "(middle, ring, pinky) clench involuntarily, pulling the muzzle downward and inward.\n"
            "2. Recoil Anticipation: Pre-emptively pushing the wrist down right before the shot breaks.\n"
            "3. Trigger Finger Placement: Hooking too deep into the 1st joint crease drags the frame left; "
            "use the center pad sweet spot and hinge straight rearward.\n\n"
            "The Fix — The 70/30 Grip Rule:\n"
            "Apply ~70% clamping pressure with your support hand and keep your dominant hand relaxed (~30%) "
            "so your trigger finger moves independently.\n\n"
            "Dry-Fire Safety Checklist (BEFORE every drill):\n"
            "✓ Visually & physically verify chamber & magwell are 100% clear\n"
            "✓ Remove ALL live ammunition from the room\n"
            "✓ Point strictly at a safe, solid backstop\n\n"
            "Try our free interactive 8-sector target wheel (with right & left-handed mirroring) and bilingual drills "
            "at sikhrpa.org/shot-diagnosis.html (Link in bio).\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #MarksmanshipFundamentals #PistolFundamentals #DryFireSafety #RangeSafety "
            "#FirearmSafetyEducation #TriggerControl #Biomechanics #SikhCommunity "
            "#CaliforniaSikhs #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Share this Reel to your Story with a Poll sticker: 'Where do your pistol groups drift most often?' "
            "(Options: '7–8 o'clock Low-Left!' / 'Dead center!') and a Link sticker to https://sikhrpa.org/shot-diagnosis.html."
        ),
        "slides": [
            {
                "filename": "reel-00-cover.png",
                "width": 1080,
                "height": 1920,
                "theme": "royal",
                "frame_variant": "reel-cover",
                "pill_text": "Reel • Marksmanship Science",
                "slide_label": "REEL COVER",
                "footer_url": "sikhrpa.org/shot-diagnosis.html",
                "footer_right": "WATCH REEL ▶",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:20px;">
                  <div class="reel-badge">Interactive 8-Sector Target Diagnostic</div>
                  <h1 class="h1-hero" style="font-size:60px;">Why Do Shots Hit <span class="gold">Low-Left?</span></h1>
                  <div class="pa-text-md" style="font-size:26px;">ਗੋਲੀ ਖੱਬੇ-ਹੇਠਾਂ ਕਿਉਂ ਲੱਗਦੀ ਹੈ? (7:00–8:00)</div>
                  <div class="diagram-wrap" style="padding:14px;border-radius:999px;background:rgba(9,14,26,0.9);border-color:rgba(245,158,11,0.45);">
                    {svg_shot_clock_dial(size=560)}
                  </div>
                  <div class="url-chip" style="font-size:24px;padding:14px 30px;">sikhrpa.org/shot-diagnosis.html</div>
                </div>
                """,
            },
            {
                "filename": "reel-01-hook.png",
                "width": 1080,
                "height": 1920,
                "theme": "default",
                "pill_text": "Frame 1 • 0:00–0:04 Hook",
                "slide_label": "01 / 05",
                "footer_url": "sikhrpa.org/shot-diagnosis.html",
                "footer_right": "STORYBOARD 1/5",
                "body_html": f"""
                <div class="eyebrow">The #1 Marksmanship Pattern • 0:00 – 0:04</div>
                <h2 class="h1-hero" style="font-size:56px;">85% of Shooters Hit <span class="red-lt">7:00–8:00 Low-Left</span></h2>
                <div class="diagram-wrap" style="padding:16px;">
                  {svg_shot_clock_dial(size=540)}
                </div>
                <div class="pa-banner">
                  <div class="pa-text-md">ਗੋਲੀ ਖੱਬੇ ਅਤੇ ਹੇਠਾਂ ਵੱਲ ਜਾਣ ਦਾ ਮੁੱਖ ਕਾਰਨ: ਟਰਿੱਗਰ ਦਬਾਉਂਦੇ ਸਮੇਂ ਹੇਠਲੀਆਂ ਤਿੰਨ ਉਂਗਲਾਂ ਨੂੰ ਜ਼ੋਰ ਨਾਲ ਘੁੱਟਣਾ ਅਤੇ ਰੀਕੋਇਲ ਤੋਂ ਡਰ ਕੇ ਹੱਥ ਨੂੰ ਹੇਠਾਂ ਝਟਕਾ ਦੇਣਾ।</div>
                </div>
                """,
            },
            {
                "filename": "reel-02-root-cause.png",
                "width": 1080,
                "height": 1920,
                "theme": "default",
                "pill_text": "Frame 2 • 0:04–0:10 Biomechanics",
                "slide_label": "02 / 05",
                "footer_url": "sikhrpa.org/shot-diagnosis.html",
                "footer_right": "STORYBOARD 2/5",
                "body_html": f"""
                <div class="eyebrow">Root Neuromuscular Causes • 0:04 – 0:10</div>
                <h2 class="h1-lg" style="font-size:52px;">It's Not Your Sights — It's <span class="gold">Grip &amp; Trigger Mechanics</span></h2>
                <div class="card card-red stack-sm" style="padding:24px;">
                  <div class="red-lt" style="font-size:17px;font-weight:900;letter-spacing:0.08em;">1. SYMPATHETIC GRIP CLENCH</div>
                  <p class="body-text">When your index finger bends to press the trigger, your pinky and ring finger reflexively clench inward — yanking the muzzle down and left.</p>
                </div>
                <div class="card card-gold stack-sm" style="padding:24px;">
                  <div class="gold" style="font-size:17px;font-weight:900;letter-spacing:0.08em;">2. RECOIL ANTICIPATION ("THE FLINCH")</div>
                  <p class="body-text">Subconsciously pushing the wrist downward milliseconds before the shot breaks to fight expected recoil.</p>
                </div>
                <div class="diagram-wrap" style="padding:18px;">
                  <div style="font-size:16px;font-weight:900;color:#fbbf24;letter-spacing:0.08em;margin-bottom:8px;">3. TRIGGER FINGER CONTACT ZONES</div>
                  {svg_trigger_finger_zones()}
                </div>
                """,
            },
            {
                "filename": "reel-03-70-30-grip.png",
                "width": 1080,
                "height": 1920,
                "theme": "royal",
                "pill_text": "Frame 3 • 0:10–0:16 The Fix",
                "slide_label": "03 / 05",
                "footer_url": "sikhrpa.org/shot-diagnosis.html",
                "footer_right": "STORYBOARD 3/5",
                "body_html": """
                <div class="eyebrow">Neuromuscular Fix • 0:10 – 0:16</div>
                <h2 class="h1-hero" style="font-size:58px;">Master the <span class="gold">70 / 30 Grip Rule</span></h2>
                <p class="lead">Decouple your trigger finger from your gripping hand so your front sight stays completely motionless through the break.</p>
                <div class="grid-2" style="gap:20px;">
                  <div class="card card-emerald stack-sm" style="padding:30px;text-align:center;">
                    <div style="font-size:74px;font-weight:900;color:#34d399;line-height:1;">70%</div>
                    <div class="h3-title">Support Hand</div>
                    <p class="body-text">Firm, high clamping pressure pressed solidly into the exposed grip panel — absorbs recoil and locks the frame.</p>
                  </div>
                  <div class="card card-gold stack-sm" style="padding:30px;text-align:center;">
                    <div style="font-size:74px;font-weight:900;color:#fbbf24;line-height:1;">30%</div>
                    <div class="h3-title">Dominant Hand</div>
                    <p class="body-text">Firm handshake only — keeps your strong forearm relaxed so your index finger hinges straight back smoothly.</p>
                  </div>
                </div>
                <div class="card card-blue stack-sm" style="padding:26px;">
                  <div class="blue-lt" style="font-size:17px;font-weight:900;letter-spacing:0.08em;">QUICK EMPTY-HAND SELF-TEST</div>
                  <p class="body-text">Hold your dominant hand up empty and curl your index finger like a trigger press. Watch your pinky and ring finger — if they twitch inward, relax your dominant grip and transfer pressure to your support hand!</p>
                </div>
                """,
            },
            {
                "filename": "reel-04-dry-fire-checklist.png",
                "width": 1080,
                "height": 1920,
                "theme": "default",
                "pill_text": "Frame 4 • 0:16–0:24 Dry-Fire Safety",
                "slide_label": "04 / 05",
                "footer_url": "sikhrpa.org/shot-diagnosis.html",
                "footer_right": "STORYBOARD 4/5",
                "body_html": """
                <div class="eyebrow">Safety First • 0:16 – 0:24</div>
                <h2 class="h1-lg" style="font-size:52px;">Mandatory <span class="red-lt">Dry-Fire Safety</span> Checklist &amp; Drills</h2>
                <div class="card card-red stack-sm" style="padding:26px;">
                  <div class="red-lt" style="font-size:17px;font-weight:900;letter-spacing:0.08em;">STRICT 4-POINT SAFETY CHECK BEFORE ANY DRY-FIRE</div>
                  <ul class="check-list" style="gap:12px;margin-top:6px;">
                    <li><span class="icon-ok">1</span><span><strong>Remove Magazine</strong> and lock slide/action fully open.</span></li>
                    <li><span class="icon-ok">2</span><span><strong>Visually &amp; Physically Inspect</strong> chamber and magazine well twice.</span></li>
                    <li><span class="icon-ok">3</span><span><strong>ZERO Live Ammunition</strong> in the room — store all live rounds in another room.</span></li>
                    <li><span class="icon-ok">4</span><span><strong>Confirm a Safe Backstop</strong> and announce clearly when starting &amp; ending practice.</span></li>
                  </ul>
                </div>
                <div class="grid-2" style="gap:16px;">
                  <div class="card card-gold stack-sm" style="padding:22px;">
                    <div class="gold" style="font-size:15px;font-weight:900;">DRILL 1 • CASING / COIN DRILL</div>
                    <p class="body-sm">Balance a spent casing or coin behind the front sight. Press smoothly — goal: <strong>10 clean breaks without dropping</strong>.</p>
                  </div>
                  <div class="card card-blue stack-sm" style="padding:22px;">
                    <div class="blue-lt" style="font-size:15px;font-weight:900;">DRILL 2 • 2-INCH WALL DRILL</div>
                    <p class="body-sm">Stand 2" from a blank wall and watch ONLY the front sight post stay motionless through the trigger break.</p>
                  </div>
                </div>
                <div class="pa-banner" style="padding:16px 22px;">
                  <div class="pa-text-sm">ਖਾਲੀ ਕਾਰਤੂਸ ਨੂੰ ਸਲਾਈਡ ਉੱਤੇ ਰੱਖ ਕੇ ਟਰਿੱਗਰ ਦਬਾਓ। ਜੇਕਰ ਕਾਰਤੂਸ ਡਿੱਗਦਾ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਝਟਕਾ ਦੇ ਰਹੇ ਹੋ।</div>
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
                "footer_url": "sikhrpa.org/shot-diagnosis.html",
                "footer_right": "LINK IN BIO",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:26px;">
                  <img class="brand-logo" style="width:146px;height:146px;border-width:3.5px;" src="{logo}" alt="SikhRPA"/>
                  <div class="eyebrow">100% Free Interactive Tool</div>
                  <h2 class="h1-hero" style="font-size:62px;">Diagnose Your Target <span class="gold">In Seconds</span></h2>
                  <p class="lead" style="font-size:28px;max-width:840px;">
                    Tap any sector on our free 8-sector target wheel — includes Right &amp; Left-Handed mirroring and bilingual Gurmukhi coaching.
                  </p>
                  <div class="url-chip" style="font-size:25px;padding:18px 34px;">sikhrpa.org/shot-diagnosis.html</div>
                  <div class="pa-banner" style="width:100%;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;">
                    <div class="pa-text-lg">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                    <div style="font-size:20px;font-weight:800;color:#cbd5e1;margin-top:4px;">STAY SAFE, BE RESPONSIBLE!</div>
                  </div>
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # POST 08 — Thu, Dec 17, 2026 • 5:30 PM PST • 6-Slide Carousel (4:5)
    # =========================================================================
    post_08 = {
        "number": 8,
        "slug": "post-08-bilingual-range-trauma-stop-the-bleed",
        "date_iso": "2026-12-17",
        "date_display": "Thu, Dec 17, 2026",
        "time_pst": "5:30 PM PST",
        "week": 3,
        "format": "Carousel (6 slides, 4:5)",
        "format_type": "carousel",
        "title": "Bilingual Range Trauma & Stop the Bleed (IFAK Audit, Tourniquet & 911 Script)",
        "url": "https://sikhrpa.org/trauma-safety.html",
        "caption": (
            "If you carry safety gear to the range, carry the training and supplies to stop life-threatening bleeding too. "
            "Severe arterial bleeding can become fatal in minutes — long before an ambulance reaches a remote outdoor range.\n\n"
            "Swipe through SikhRPA's Bilingual Range Trauma & Stop the Bleed Awareness Guide:\n"
            "• First 60 Seconds: Call 'CEASE FIRE!' & Dial 911 → Find Bleeding Source → Compress / Tourniquet\n"
            "• 4 Mandatory Tourniquet Rules in English & Gurmukhi (ਟੂਰਨੀਕੇਟ ਲਗਾਉਣ ਦੇ ੪ ਲਾਜ਼ਮੀ ਨਿਯਮ): "
            "2–3\" above wound (never on a joint), pull strap max tight, twist windlass until bleeding stops, write time (T: HH:MM) & NEVER loosen\n"
            "• Junctional Wound Packing, Vented Chest Seals (check the back for exit wounds!), & Hypothermia Prevention\n"
            "• 6-Item Range Bag IFAK Checklist (use only authentic CoTCCC-approved tourniquets like CAT Gen 7, SOFTT-W, or SAM XT)\n"
            "• Verbatim Remote Range 911 Dispatch Script with GPS coordinates & highway gate escort\n\n"
            "Read the full bilingual guide & use the interactive IFAK Auditor and GPS 911 Script Generator at "
            "sikhrpa.org/trauma-safety.html (Link in bio).\n\n"
            "Medical Disclaimer: Provided strictly for general safety awareness and does not constitute medical advice. "
            "Always dial 911 in an emergency and pursue formal hands-on training through the American College of Surgeons "
            "Stop the Bleed® program or the American Red Cross.\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #StopTheBleed #FirstAidEducation #RangeSafety #EmergencyPreparedness "
            "#IFAK #PublicSafetyEducation #BilingualSafety #Gurmukhi #SikhCommunity "
            "#CaliforniaSikhs #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Share Slide 5 (the 6-Item Range Bag IFAK Audit) to your Story with a Poll sticker: "
            "'Do you carry a stocked IFAK on the outside of your range bag?' "
            "(Options: 'Yes — 6/6 ready!' / 'Building mine this week!') + Link sticker to https://sikhrpa.org/trauma-safety.html."
        ),
        "slides": [
            {
                "filename": "slide-01-cover.png",
                "width": 1080,
                "height": 1350,
                "theme": "trauma",
                "pill_text": "Life-Saving First Aid",
                "pill_class": "pill-red",
                "slide_label": "01 / 06",
                "footer_url": "sikhrpa.org/trauma-safety.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow" style="color:#f87171;">Bilingual Range Trauma Awareness</div>
                <h1 class="h1-hero">Range Trauma &amp; <span class="gold">Stop the Bleed</span></h1>
                <div class="pa-banner">
                  <div class="pa-text-lg">ਰੇਂਜ ਟਰਾਮਾ, ਟੂਰਨੀਕੇਟ ਨਿਯਮ, IFAK ਚੈੱਕਲਿਸਟ ਅਤੇ ੯੧੧ ਐਮਰਜੈਂਸੀ ਗਾਈਡ</div>
                </div>
                <p class="lead">
                  Every responsible range participant should know how to control massive bleeding, audit an
                  <strong style="color:#fff;">Individual First Aid Kit (IFAK)</strong>, and dispatch 911 to a remote outdoor range.
                </p>
                <div class="stat-row">
                  <div class="stat-box" style="border-color:rgba(248,113,113,0.45);">
                    <div class="stat-val" style="color:#fca5a5;">911 First</div>
                    <div class="stat-lbl">Cease Fire &amp; Call</div>
                  </div>
                  <div class="stat-box">
                    <div class="stat-val">4 Rules</div>
                    <div class="stat-lbl">EN + ਪੰਜਾਬੀ TQ</div>
                  </div>
                  <div class="stat-box">
                    <div class="stat-val">6 Items</div>
                    <div class="stat-lbl">Range IFAK Audit</div>
                  </div>
                </div>
                <div class="disclaimer-note">
                  <strong>Educational Awareness Only:</strong> Not medical advice. In any emergency dial 911 immediately. Take a formal hands-on ACS Stop the Bleed® or Red Cross course.
                </div>
                """,
            },
            {
                "filename": "slide-02-three-steps.png",
                "width": 1080,
                "height": 1350,
                "theme": "trauma",
                "pill_text": "Immediate Response",
                "pill_class": "pill-red",
                "slide_label": "02 / 06",
                "footer_url": "sikhrpa.org/trauma-safety.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow" style="color:#f87171;">First 60 Seconds • Stop the Bleed ABCs</div>
                <h2 class="h1-lg">3 Immediate Steps in a <span class="gold">Range Trauma Emergency</span></h2>
                <div class="stack" style="gap:18px;margin-top:4px;">
                  <div class="card card-red row" style="padding:24px;">
                    <div class="num-badge num-badge-red">1</div>
                    <div class="stack-sm">
                      <div class="h3-title">Ensure Safety &amp; Call 911</div>
                      <div class="pa-text-sm" style="font-size:20px;">ਸਭ ਤੋਂ ਪਹਿਲਾਂ ਰੇਂਜ ਖਾਲੀ ਕਰੋ ਅਤੇ ੯੧੧ ਮਿਲਾਓ</div>
                      <p class="body-sm">Shout <strong>"CEASE FIRE!"</strong> Unload and secure all firearms before approaching. Assign one person to call 911 immediately.</p>
                    </div>
                  </div>
                  <div class="card card-gold row" style="padding:24px;">
                    <div class="num-badge">2</div>
                    <div class="stack-sm">
                      <div class="h3-title">Find the Source of Bleeding</div>
                      <div class="pa-text-sm" style="font-size:20px;">ਖੂਨ ਵਹਿਣ ਵਾਲੀ ਥਾਂ ਦੀ ਜਾਂਚ ਕਰੋ</div>
                      <p class="body-sm">Expose the wound using trauma shears. Identify bright arterial spurting, pooling blood, or rapidly blood-soaked clothing.</p>
                    </div>
                  </div>
                  <div class="card card-blue row" style="padding:24px;">
                    <div class="num-badge num-badge-blue">3</div>
                    <div class="stack-sm">
                      <div class="h3-title">Compress: Tourniquet or Wound Packing</div>
                      <div class="pa-text-sm" style="font-size:20px;">ਦਬਾਓ: ਟੂਰਨੀਕੇਟ ਜਾਂ ਗੌਜ਼ ਨਾਲ ਪੈਕਿੰਗ</div>
                      <p class="body-sm">Arms &amp; legs: apply a CoTCCC tourniquet 2–3" above wound. Neck, groin, or armpit: pack deeply with gauze &amp; hold continuous bodyweight pressure.</p>
                    </div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-03-tourniquet-rules.png",
                "width": 1080,
                "height": 1350,
                "theme": "trauma",
                "pill_text": "CoTCCC Approved",
                "pill_class": "pill-red",
                "slide_label": "03 / 06",
                "footer_url": "sikhrpa.org/trauma-safety.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="eyebrow" style="color:#f87171;">Extremity Bleeding • ਟੂਰਨੀਕੇਟ ਲਗਾਉਣ ਦੇ ੪ ਲਾਜ਼ਮੀ ਨਿਯਮ</div>
                <h2 class="h2-title">4 Mandatory <span class="gold">Tourniquet Rules</span></h2>
                <div class="diagram-wrap" style="padding:12px 16px;">
                  {svg_tourniquet_diagram()}
                </div>
                <div class="grid-2" style="gap:14px;">
                  <div class="card stack-sm" style="padding:16px 18px;">
                    <div class="gold" style="font-size:15px;font-weight:900;">1. PLACEMENT (HIGH &amp; TIGHT)</div>
                    <p class="body-sm" style="font-size:16.5px;">2–3" above wound (or highest on limb). <strong>Never over knee or elbow joint.</strong></p>
                    <div class="pa-text-sm" style="font-size:15.5px;">ਜ਼ਖ਼ਮ ਤੋਂ ੨-੩ ਇੰਚ ਉੱਪਰ ਲਗਾਓ। ਜੋੜ ਉੱਤੇ ਨਾ ਲਗਾਓ।</div>
                  </div>
                  <div class="card stack-sm" style="padding:16px 18px;">
                    <div class="gold" style="font-size:15px;font-weight:900;">2. PULL STRAP MAX TIGHT</div>
                    <p class="body-sm" style="font-size:16.5px;">Pull Velcro fully tight <strong>before</strong> twisting windlass — slack straps fail.</p>
                    <div class="pa-text-sm" style="font-size:15.5px;">ਰੌਡ ਘੁਮਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਬੈਲਟ ਪੂਰੀ ਤਾਕਤ ਨਾਲ ਕੱਸੋ।</div>
                  </div>
                  <div class="card stack-sm" style="padding:16px 18px;">
                    <div class="gold" style="font-size:15px;font-weight:900;">3. TWIST UNTIL BLEEDING STOPS</div>
                    <p class="body-sm" style="font-size:16.5px;">Twist windlass until bright spurting stops completely, then lock in clip.</p>
                    <div class="pa-text-sm" style="font-size:15.5px;">ਖੂਨ ਬੰਦ ਹੋਣ ਤੱਕ ਰੌਡ ਘੁਮਾਓ ਅਤੇ ਲਾਕ ਕਰੋ।</div>
                  </div>
                  <div class="card card-red stack-sm" style="padding:16px 18px;">
                    <div class="red-lt" style="font-size:15px;font-weight:900;">4. WRITE TIME &amp; NEVER LOOSEN</div>
                    <p class="body-sm" style="font-size:16.5px;">Mark time (e.g. T: 14:15). Only hospital doctors remove it.</p>
                    <div class="pa-text-sm" style="font-size:15.5px;">ਸਮਾਂ ਲਿਖੋ। ਕਦੇ ਵੀ ਖੁਦ ਢਿੱਲਾ ਨਾ ਕਰੋ।</div>
                  </div>
                </div>
                <div class="disclaimer-note" style="font-size:14.5px;">
                  <strong>Warning:</strong> Avoid counterfeit generic tourniquets — they snap under load. Carry authentic CoTCCC-approved brands only (CAT Gen 7, SOFTT-W, SAM XT).
                </div>
                """,
            },
            {
                "filename": "slide-04-junctional-chest-hypothermia.png",
                "width": 1080,
                "height": 1350,
                "theme": "trauma",
                "pill_text": "Beyond Extremities",
                "pill_class": "pill-red",
                "slide_label": "04 / 06",
                "footer_url": "sikhrpa.org/trauma-safety.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow" style="color:#f87171;">Complete Trauma Awareness</div>
                <h2 class="h1-lg">Junctional Packing, <span class="gold">Chest Seals &amp; Warmth</span></h2>
                <div class="stack" style="gap:16px;">
                  <div class="card card-gold stack-sm" style="padding:20px 24px;">
                    <div class="row" style="justify-content:space-between;">
                      <div class="h3-title" style="font-size:25px;">1. Junctional Wound Packing (Groin, Armpit, Neck)</div>
                      <span class="pill" style="font-size:12.5px;padding:4px 12px;">Never Pack Chest/Abdomen</span>
                    </div>
                    <p class="body-sm">Push hemostatic (QuikClot) or sterile gauze deeply against the bleeding vessel and lean continuous bodyweight pressure for <strong>3+ min (hemostatic)</strong> or <strong>10 min (plain gauze)</strong>.</p>
                    <div class="pa-text-sm" style="font-size:17px;">ਗੌਜ਼ ਨੂੰ ਜ਼ਖ਼ਮ ਦੇ ਅੰਦਰ ਤੱਕ ਭਰੋ ਅਤੇ ਸਰੀਰ ਦਾ ਪੂਰਾ ਭਾਰ ਪਾ ਕੇ ਦਬਾ ਕੇ ਰੱਖੋ।</div>
                  </div>
                  <div class="card card-blue stack-sm" style="padding:20px 24px;">
                    <div class="h3-title" style="font-size:25px;">2. Vented Chest Seals (Entry &amp; Exit Wounds)</div>
                    <p class="body-sm">Wipe blood/sweat and apply a <strong>vented chest seal</strong> (HyFin / Halo) on exhale. <strong>Always roll and check the back</strong> for an exit wound and seal it too!</p>
                    <div class="pa-text-sm" style="font-size:17px;">ਮਰੀਜ਼ ਦੀ ਪਿੱਠ ਜ਼ਰੂਰ ਚੈੱਕ ਕਰੋ! ਜੇ ਗੋਲੀ ਪਾਰ ਹੋਈ ਹੈ, ਤਾਂ ਪਿੱਛੇ ਵੀ ਦੂਜੀ ਚੈਸਟ ਸੀਲ ਲਗਾਓ।</div>
                  </div>
                  <div class="card card-red stack-sm" style="padding:20px 24px;">
                    <div class="h3-title" style="font-size:25px;">3. Prevent Hypothermia (The Lethal Triad)</div>
                    <p class="body-sm">Even a 2°F body-temp drop stops blood from clotting. Insulate the patient off cold ground and wrap in a <strong>Mylar space blanket</strong> — even on hot 90°F summer days.</p>
                    <div class="pa-text-sm" style="font-size:17px;">ਮਰੀਜ਼ ਨੂੰ ਠੰਢੀ ਜ਼ਮੀਨ ਤੋਂ ਬਚਾਓ ਅਤੇ ਐਮਰਜੈਂਸੀ ਫੋਇਲ ਸ਼ੀਟ ਨਾਲ ਪੂਰੀ ਤਰ੍ਹਾਂ ਲਪੇਟੋ।</div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-05-ifak-audit.png",
                "width": 1080,
                "height": 1350,
                "theme": "trauma",
                "pill_text": "Range Bag Readiness",
                "pill_class": "pill-red",
                "slide_label": "05 / 06",
                "footer_url": "sikhrpa.org/trauma-safety.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow" style="color:#f87171;">Equipment Audit • ਰੇਂਜ ਬੈਗ ਟਰਾਮਾ ਕਿੱਟ ਚੈੱਕਲਿਸਟ</div>
                <h2 class="h1-lg">6-Item Range Bag <span class="gold">IFAK Checklist</span></h2>
                <p class="body-sm">Mount your Individual First Aid Kit on the <strong>outside</strong> of your range bag — staged and ready for 1-handed access:</p>
                <div class="grid-2" style="gap:14px;">
                  <div class="card card-red stack-sm" style="padding:18px 20px;">
                    <div class="red-lt" style="font-size:15px;font-weight:900;">1. CoTCCC TOURNIQUET</div>
                    <p class="body-sm" style="font-size:16.5px;">Authentic CAT Gen 7 or SOFTT-W, <strong>unwrapped out of plastic</strong> &amp; pre-staged.</p>
                    <div class="pa-text-sm" style="font-size:15.5px;">ਅਸਲੀ ਟੂਰਨੀਕੇਟ (ਪਲਾਸਟਿਕ ਤੋਂ ਬਾਹਰ)</div>
                  </div>
                  <div class="card card-gold stack-sm" style="padding:18px 20px;">
                    <div class="gold" style="font-size:15px;font-weight:900;">2. HEMOSTATIC Z-FOLD GAUZE</div>
                    <p class="body-sm" style="font-size:16.5px;">QuikClot / Combat Gauze (kaolin-impregnated) for deep junctional packing.</p>
                    <div class="pa-text-sm" style="font-size:15.5px;">ਖੂਨ ਜਮਾਉਣ ਵਾਲੀ ਗੌਜ਼</div>
                  </div>
                  <div class="card card-blue stack-sm" style="padding:18px 20px;">
                    <div class="blue-lt" style="font-size:15px;font-weight:900;">3. VENTED CHEST SEAL TWIN PACK</div>
                    <p class="body-sm" style="font-size:16.5px;">HyFin or Halo twin pack (2 seals for both entry &amp; exit torso wounds).</p>
                    <div class="pa-text-sm" style="font-size:15.5px;">ਚੈਸਟ ਸੀਲ ਜੋੜਾ (ਅੱਗੇ ਤੇ ਪਿੱਛੇ ਲਈ)</div>
                  </div>
                  <div class="card stack-sm" style="padding:18px 20px;">
                    <div class="emerald" style="font-size:15px;font-weight:900;">4. PRESSURE DRESSING</div>
                    <p class="body-sm" style="font-size:16.5px;">4" or 6" Israeli / Emergency Bandage to sustain firm direct pressure.</p>
                    <div class="pa-text-sm" style="font-size:15.5px;">ਪ੍ਰੈਸ਼ਰ ਪੱਟੀ (ਇਜ਼ਰਾਈਲੀ ਬੈਂਡੇਜ)</div>
                  </div>
                  <div class="card stack-sm" style="padding:18px 20px;">
                    <div class="gold" style="font-size:15px;font-weight:900;">5. 7.25" TRAUMA SHEARS</div>
                    <p class="body-sm" style="font-size:16.5px;">Heavy-duty medical shears to rapidly cut denim, leather, and jackets.</p>
                    <div class="pa-text-sm" style="font-size:15.5px;">ਮੋਟੇ ਕੱਪੜੇ ਕੱਟਣ ਵਾਲੀ ਕੈਂਚੀ</div>
                  </div>
                  <div class="card stack-sm" style="padding:18px 20px;">
                    <div class="blue-lt" style="font-size:15px;font-weight:900;">6. MYLAR BLANKET + NITRILE GLOVES</div>
                    <p class="body-sm" style="font-size:16.5px;">Retains 90% body heat to fight shock + 2 pairs heavy nitrile gloves.</p>
                    <div class="pa-text-sm" style="font-size:15.5px;">ਐਮਰਜੈਂਸੀ ਸ਼ੀਟ ਅਤੇ ਦਸਤਾਨੇ</div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-06-911-dispatch-script.png",
                "width": 1080,
                "height": 1350,
                "theme": "trauma",
                "pill_text": "Remote Range 911 Script",
                "pill_class": "pill-red",
                "slide_label": "06 / 06",
                "footer_url": "sikhrpa.org/trauma-safety.html",
                "footer_right": "SAVE & SHARE",
                "body_html": """
                <div class="eyebrow" style="color:#f87171;">Outdoor &amp; BLM Ranges • ਦੂਰ-ਦੁਰਾਡੇ ਰੇਂਜਾਂ 'ਤੇ ੯੧੧ ਕਾਲ</div>
                <h2 class="h1-lg">Emergency <span class="gold">911 Range Dispatch Script</span></h2>
                <p class="body-sm">
                  Many California outdoor ranges and BLM sites have no street address. Write your GPS coordinates on a card BEFORE shooting:
                </p>
                <div class="card card-red" style="padding:26px 28px;border-width:2.5px;">
                  <div class="red-lt" style="font-size:15px;font-weight:900;letter-spacing:0.1em;margin-bottom:10px;">VERBATIM 911 DISPATCH SCRIPT</div>
                  <p style="font-size:23px;line-height:1.48;font-weight:700;color:#ffffff;">
                    "This is an emergency. We have a firearm trauma injury at <span class="gold">[Range Name]</span>.
                    Our exact GPS coordinates are <span class="gold">[Latitude, Longitude]</span>.
                    Gate access code is <span class="gold">[Gate Code]</span>.
                    Patient has <span class="gold">[Condition / TQ Applied]</span>.
                    Firearm is unloaded and secured. We need an ambulance and medevac on standby."
                  </p>
                </div>
                <div class="card card-gold" style="padding:18px 24px;">
                  <div style="font-size:19px;font-weight:800;color:#fef3c7;">
                    💡 Pro-Tip: Send one person immediately to the main highway entrance gate to flag down and guide paramedics directly to your firing lane.
                  </div>
                </div>
                <div class="cta-box" style="padding:18px 24px;">
                  <div>
                    <div style="font-size:21px;font-weight:900;color:#fff;">Interactive IFAK Auditor + GPS Script Tool</div>
                    <div class="pa-text-sm" style="margin-top:2px;">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                  </div>
                  <div class="url-chip" style="font-size:18px;">sikhrpa.org/trauma-safety.html</div>
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # POST 09 — Sat, Dec 19, 2026 • 10:00 AM PST • 6-Slide Carousel (4:5)
    # =========================================================================
    post_09 = {
        "number": 9,
        "slug": "post-09-how-to-zero-optics",
        "date_iso": "2026-12-19",
        "date_display": "Sat, Dec 19, 2026",
        "time_pst": "10:00 AM PST",
        "week": 3,
        "format": "Carousel (6 slides, 4:5)",
        "format_type": "carousel",
        "title": "How to Zero Optics — Centroid Triangulation, MOA vs MIL, Click Scaling & Height-Over-Bore",
        "url": "https://sikhrpa.org/zero-optics.html",
        "caption": (
            "Stop burning ammunition chasing single bullet holes on paper! Zeroing a pistol red dot or rifle scope "
            "is pure geometry once you understand four simple principles.\n\n"
            "Swipe through SikhRPA's visual technical guide to zeroing optics accurately:\n"
            "• 5-Shot Group Centroid Triangulation: Never adjust for one shot — fire a rested 3–5 shot group, "
            "find the Mean Point of Impact (MPI), and dial once.\n"
            "• MOA vs. MIL (MRAD): 1 MOA ≈ 1.047\" at 100 yds (1/4, 1/2, or 1 MOA clicks) vs. 1 MIL = 3.60\" at 100 yds "
            "(0.1 MIL = 0.36\" per click). Golden Rule: turret arrows ('UP' / 'R') move your bullet impact (POI)!\n"
            "• 25 / 50 / 100-Yard Click Scaling: Closer targets mean smaller inch-per-click shifts — so 25 yards "
            "requires 4× as many clicks per inch as 100 yards.\n"
            "• Height-Over-Bore Mechanical Offset: Because an optic sits ~2.6\" above a carbine bore (~0.8\" on pistols), "
            "close 3–7 yard shots naturally hit 1.5\"–2.5\" below your dot.\n"
            "• 5-Step Field Zeroing Protocol in English & Gurmukhi (ਸਹੀ ਜ਼ੀਰੋਇੰਗ ਲਈ ੫ ਜ਼ਰੂਰੀ ਕਦਮ)\n\n"
            "Plot your target hits and get exact turret clicks automatically — zero math required — with our free "
            "Zeroing Click Calculator at sikhrpa.org/zero-optics.html (Link in bio).\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #OpticsZeroing #MarksmanshipFundamentals #BallisticsEducation #MOAvsMIL "
            "#RangeSafety #FirearmSafetyEducation #HeightOverBore #TechnicalEducation "
            "#SikhCommunity #CaliforniaSikhs #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Share Slide 4 (the 25/50/100-Yard Click Scaling chart) to your Story with the text: "
            "'Bookmark this click scaling chart for your next range day!' and a Link sticker to "
            "https://sikhrpa.org/zero-optics.html."
        ),
        "slides": [
            {
                "filename": "slide-01-cover.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Ballistics & Optics Curriculum",
                "slide_label": "01 / 06",
                "footer_url": "sikhrpa.org/zero-optics.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Technical Marksmanship Guide</div>
                <h1 class="h1-hero">How to <span class="gold">Zero Optics</span><br/>With Zero Guesswork</h1>
                <div class="pa-banner">
                  <div class="pa-text-lg">ਓਪਟਿਕਸ ਜ਼ੀਰੋ ਕਰਨ ਦਾ ਤਰੀਕਾ, ਕਲਿੱਕ ਕੈਲਕੁਲੇਟਰ ਅਤੇ ਬੈਲਿਸਟਿਕਸ ਗਾਈਡ</div>
                </div>
                <p class="lead">
                  Master 5-shot group centroid triangulation, MOA vs. MIL math, 25/50/100-yard click scaling, and height-over-bore mechanical offset.
                </p>
                <div class="grid-2" style="margin-top:6px;">
                  <div class="card card-blue" style="padding:18px 22px;">
                    <div class="blue-lt" style="font-size:15px;font-weight:900;">SLIDE 02</div>
                    <div style="font-size:21px;font-weight:800;margin-top:4px;">5-Shot Centroid Triangulation</div>
                  </div>
                  <div class="card card-gold" style="padding:18px 22px;">
                    <div class="gold" style="font-size:15px;font-weight:900;">SLIDE 03</div>
                    <div style="font-size:21px;font-weight:800;margin-top:4px;">MOA vs. MIL &amp; Turret Rule</div>
                  </div>
                  <div class="card card-gold" style="padding:18px 22px;">
                    <div class="gold" style="font-size:15px;font-weight:900;">SLIDE 04</div>
                    <div style="font-size:21px;font-weight:800;margin-top:4px;">25 / 50 / 100-Yd Click Scaling</div>
                  </div>
                  <div class="card card-blue" style="padding:18px 22px;">
                    <div class="blue-lt" style="font-size:15px;font-weight:900;">SLIDE 05</div>
                    <div style="font-size:21px;font-weight:800;margin-top:4px;">Height-Over-Bore Offset</div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-02-centroid-triangulation.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Group Centroid Math",
                "slide_label": "02 / 06",
                "footer_url": "sikhrpa.org/zero-optics.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="eyebrow">Never Chase Single Shots</div>
                <h2 class="h1-lg">5-Shot Group <span class="gold">Centroid Triangulation</span></h2>
                <div class="diagram-wrap" style="padding:14px;">
                  {svg_centroid_triangulation()}
                </div>
                <div class="pa-banner" style="padding:15px 22px;">
                  <div class="pa-text-sm">ਇੱਕ ਗੋਲੀ ਦੇਖ ਕੇ ਕਦੇ ਵੀ ਡਾਇਲ ਨਾ ਘੁਮਾਓ। ਹਮੇਸ਼ਾ ੩ ਤੋਂ ੫ ਗੋਲੀਆਂ ਦਾ ਗਰੁੱਪ ਫਾਇਰ ਕਰੋ ਅਤੇ ਉਸ ਗਰੁੱਪ ਦੇ ਕੇਂਦਰ (MPI) ਤੋਂ ਬੁੱਲਜ਼-ਆਈ ਦੀ ਦੂਰੀ ਮਾਪੋ।</div>
                </div>
                <div class="card" style="padding:16px 22px;">
                  <p class="body-sm">
                    <strong class="gold">Why 5 Shots?</strong> Human wobble and ammunition variance scatter individual rounds. Finding the mathematical center (Mean Point of Impact) eliminates guesswork and confirms your true optical zero in 1 adjustment.
                  </p>
                </div>
                """,
            },
            {
                "filename": "slide-03-moa-vs-mil.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Angular Units",
                "slide_label": "03 / 06",
                "footer_url": "sikhrpa.org/zero-optics.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="eyebrow">Optic Turret Standards</div>
                <h2 class="h1-lg"><span class="blue-lt">MOA</span> vs. <span class="gold">MIL (MRAD)</span> Explained</h2>
                <div class="diagram-wrap" style="padding:14px;">
                  {svg_moa_vs_mil()}
                </div>
                <div class="card card-gold stack-sm" style="padding:22px 26px;">
                  <div class="gold" style="font-size:16px;font-weight:900;letter-spacing:0.08em;">THE GOLDEN RULE OF TURRET ARROWS</div>
                  <p class="body-text" style="color:#fff;">
                    The arrows marked <strong>"UP"</strong> or <strong>"R (RIGHT)"</strong> move your <strong>Point of Impact (bullet holes)</strong> on paper — NOT the crosshair in reverse!
                  </p>
                  <div class="grid-2" style="gap:12px;margin-top:6px;">
                    <div class="card" style="padding:14px 16px;background:rgba(15,23,42,0.85);">
                      <strong class="blue-lt">Hitting LOW?</strong> Dial Top Turret → <strong>UP</strong>
                    </div>
                    <div class="card" style="padding:14px 16px;background:rgba(15,23,42,0.85);">
                      <strong class="gold">Hitting LEFT?</strong> Dial Side Turret → <strong>R (RIGHT)</strong>
                    </div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-04-click-scaling.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Distance Scaling",
                "slide_label": "04 / 06",
                "footer_url": "sikhrpa.org/zero-optics.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="eyebrow">Linear Angular Geometry</div>
                <h2 class="h2-title">25 / 50 / 100-Yard <span class="gold">Click Scaling Chart</span></h2>
                <div class="diagram-wrap" style="padding:12px 14px;">
                  {svg_click_scaling_cone()}
                </div>
                <div class="card" style="padding:12px 16px;overflow:hidden;">
                  <table class="tech-table">
                    <thead>
                      <tr>
                        <th>Optic Turret Value</th>
                        <th>@ 25 Yards (Clicks/1")</th>
                        <th>@ 50 Yards (Clicks/1")</th>
                        <th>@ 100 Yards (Clicks/1")</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>1 MOA</strong> (Pistol Dot)</td>
                        <td>0.25" <span class="gold">(4 clicks)</span></td>
                        <td>0.50" <span class="emerald">(2 clicks)</span></td>
                        <td>1.00" <span class="blue-lt">(1 click)</span></td>
                      </tr>
                      <tr>
                        <td><strong>1/2 MOA</strong> (Carbine Dot)</td>
                        <td>0.125" <span class="gold">(8 clicks)</span></td>
                        <td>0.25" <span class="emerald">(4 clicks)</span></td>
                        <td>0.50" <span class="blue-lt">(2 clicks)</span></td>
                      </tr>
                      <tr>
                        <td><strong>1/4 MOA</strong> (Rifle Scope)</td>
                        <td>0.063" <span class="gold">(16 clicks)</span></td>
                        <td>0.125" <span class="emerald">(8 clicks)</span></td>
                        <td>0.25" <span class="blue-lt">(4 clicks)</span></td>
                      </tr>
                      <tr>
                        <td><strong>0.1 MIL</strong> (MRAD Scope)</td>
                        <td>0.09" <span class="gold">(11 clicks)</span></td>
                        <td>0.18" <span class="emerald">(5.6 clicks)</span></td>
                        <td>0.36" <span class="blue-lt">(2.8 clicks)</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """,
            },
            {
                "filename": "slide-05-height-over-bore.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Mechanical Offset",
                "slide_label": "05 / 06",
                "footer_url": "sikhrpa.org/zero-optics.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="eyebrow">Why Close Shots Hit Low</div>
                <h2 class="h1-lg">Height-Over-Bore <span class="gold">Mechanical Offset</span></h2>
                <div class="diagram-wrap" style="padding:14px;">
                  {svg_height_over_bore()}
                </div>
                <div class="grid-2" style="gap:16px;">
                  <div class="card card-red stack-sm" style="padding:20px 22px;">
                    <div class="red-lt" style="font-size:15px;font-weight:900;">CLOSE-RANGE OFFSET (3–7 YD)</div>
                    <p class="body-sm">Your optic sits <strong>~2.6" above a carbine bore</strong> (~0.8" on pistols). At 3–7 yards, impacts naturally land <strong>1.5"–2.5" below your dot</strong> — hold slightly high on tight targets!</p>
                  </div>
                  <div class="card card-emerald stack-sm" style="padding:20px 22px;">
                    <div class="emerald" style="font-size:15px;font-weight:900;">POPULAR PRACTICAL ZEROS</div>
                    <p class="body-sm"><strong>50/200 yd:</strong> Flattest all-around carbine zero (&lt;2" rise to 200 yd).<br/><strong>15/25 yd:</strong> Ideal practical pistol red-dot zero.<br/><strong>100 yd:</strong> Precision magnified rifles.</p>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-06-five-step-cta.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "5-Step Field Protocol",
                "slide_label": "06 / 06",
                "footer_url": "sikhrpa.org/zero-optics.html",
                "footer_right": "SAVE & SHARE",
                "body_html": """
                <div class="eyebrow">Range Protocol • ਸਹੀ ਜ਼ੀਰੋਇੰਗ ਲਈ ੫ ਜ਼ਰੂਰੀ ਕਦਮ</div>
                <h2 class="h2-title">5 Steps to a <span class="gold">Rock-Solid Zero</span></h2>
                <div class="stack" style="gap:12px;">
                  <div class="card row" style="padding:15px 20px;">
                    <div class="num-badge" style="width:40px;height:40px;font-size:20px;">1</div>
                    <div>
                      <div style="font-size:20px;font-weight:800;">Lock in on Sandbags or a Benchrest (Never Off-Hand)</div>
                      <div class="pa-text-sm" style="font-size:17px;">ਬੰਦੂਕ ਨੂੰ ਸੈਂਡਬੈਗ ਜਾਂ ਰੈਸਟ ਉੱਤੇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਸਥਿਰ ਰੱਖੋ।</div>
                    </div>
                  </div>
                  <div class="card row" style="padding:15px 20px;">
                    <div class="num-badge" style="width:40px;height:40px;font-size:20px;">2</div>
                    <div>
                      <div style="font-size:20px;font-weight:800;">Confirm Paper at 10–15 Yards First</div>
                      <div class="pa-text-sm" style="font-size:17px;">ਸਿੱਧਾ ੧੦੦ ਗਜ਼ 'ਤੇ ਸ਼ੁਰੂ ਨਾ ਕਰੋ — ਪਹਿਲਾਂ ੧੦-੧੫ ਗਜ਼ 'ਤੇ ਜਾਂਚ ਕਰੋ।</div>
                    </div>
                  </div>
                  <div class="card row" style="padding:15px 20px;">
                    <div class="num-badge" style="width:40px;height:40px;font-size:20px;">3</div>
                    <div>
                      <div style="font-size:20px;font-weight:800;">Fire a Disciplined 3–5 Shot Group</div>
                      <div class="pa-text-sm" style="font-size:17px;">ਇੱਕ ਗੋਲੀ ਦੇਖ ਕੇ ਡਾਇਲ ਨਾ ਘੁਮਾਓ — ਗਰੁੱਪ ਦੇ ਕੇਂਦਰ ਨੂੰ ਦੇਖੋ।</div>
                    </div>
                  </div>
                  <div class="card row" style="padding:15px 20px;">
                    <div class="num-badge" style="width:40px;height:40px;font-size:20px;">4</div>
                    <div>
                      <div style="font-size:20px;font-weight:800;">Plot Group Centroid &amp; Dial Exact Clicks Once</div>
                      <div class="pa-text-sm" style="font-size:17px;">ਕੇਂਦਰ ਤੋਂ ਬੁੱਲਜ਼-ਆਈ ਦੀ ਦੂਰੀ ਮਾਪ ਕੇ ਕੈਲਕੁਲੇਟਰ ਅਨੁਸਾਰ ਕਲਿੱਕ ਘੁਮਾਓ।</div>
                    </div>
                  </div>
                  <div class="card row" style="padding:15px 20px;">
                    <div class="num-badge" style="width:40px;height:40px;font-size:20px;">5</div>
                    <div>
                      <div style="font-size:20px;font-weight:800;">Fire Final 3-Shot Confirmation Group &amp; Cap Turrets</div>
                      <div class="pa-text-sm" style="font-size:17px;">ਆਖਰੀ ੩ ਗੋਲੀਆਂ ਚਲਾ ਕੇ ਪੁਸ਼ਟੀ ਕਰੋ।</div>
                    </div>
                  </div>
                </div>
                <div class="cta-box" style="padding:18px 24px;">
                  <div>
                    <div style="font-size:21px;font-weight:900;color:#fff;">Free Interactive Zeroing Click Calculator</div>
                    <div style="font-size:16px;color:#cbd5e1;">No math required • 1 MOA, 1/2 MOA, 1/4 MOA &amp; 0.1 MIL</div>
                  </div>
                  <div class="url-chip" style="font-size:18px;">sikhrpa.org/zero-optics.html</div>
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # POST 10 — Tue, Dec 22, 2026 (Shaheedi Week) • 12:00 PM PST • 6-Slide Carousel
    # =========================================================================
    post_10 = {
        "number": 10,
        "slug": "post-10-miri-piri-shaheedi-week",
        "date_iso": "2026-12-22",
        "date_display": "Tue, Dec 22, 2026 (Shaheedi Week)",
        "time_pst": "12:00 PM PST",
        "week": 4,
        "format": "Carousel (6 slides, 4:5)",
        "format_type": "carousel",
        "title": "Shaheedi Week Reflection — Miri-Piri, Sant-Sipahi & Sikh Martial Heritage",
        "url": "https://sikhrpa.org/heritage.html",
        "caption": (
            "During Shaheedi Week (Poh / late December), we bow our heads in solemn remembrance of the "
            "Chaar Sahibzaade — Baba Ajit Singh Ji, Baba Jujhar Singh Ji, Baba Zorawar Singh Ji, and Baba Fateh Singh Ji — "
            "alongside Mata Gujri Ji and the devoted Sikhs of Chamkaur Sahib and Sirhind.\n\n"
            "Their sacrifice illuminates the deepest truth of Sikh martial heritage: strength is never rooted in "
            "aggression, vanity, or dominance. It is bound to spiritual humility (Piri), moral restraint (Miri), "
            "and unwavering protection of human dignity.\n\n"
            "In the Zafarnama (Verse 22), Guru Gobind Singh Ji articulated the ethic that guides our educational "
            "mission to this day:\n"
            "ਚੁ ਕਾਰ ਅਜ਼ ਹਮਹ ਹੀਲਤੇ ਦਰ ਗੁਜ਼ਸ਼ਤ ॥\n"
            "ਹਲਾਲ ਅਸਤ ਬੁਰਦਨ ਬ ਸ਼ਮਸ਼ੀਰ ਦਸਤ ॥੨੨॥\n"
            "\"When all other peaceful avenues have been exhausted and every remedy has failed, only then is it "
            "righteous to take up the sword.\"\n\n"
            "Today, honoring that sacred covenant of Shastar reverence means exercising total discipline: "
            "de-escalation first, strict obedience to the law, safe home storage to protect every child, "
            "and humble service (Seva) to our Sangat and neighbors.\n\n"
            "Read our complete educational curriculum on Sikh Martial Heritage & Responsible Stewardship at "
            "sikhrpa.org/heritage.html (Link in bio).\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #ShaheediWeek #ChaarSahibzaade #MataGujriJi #MiriPiri #SantSipahi "
            "#SikhHeritage #SikhHistory #SikhCommunity #CaliforniaSikhs #ResponsibleStewardship "
            "#StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Share Slide 1 or Slide 5 (Zafarnama Verse 22) respectfully to your Story with minimal overlay — "
            "add a quiet Link sticker to https://sikhrpa.org/heritage.html and text: "
            "'Remembering the Chaar Sahibzaade and Mata Gujri Ji this Shaheedi Week.'"
        ),
        "slides": [
            {
                "filename": "slide-01-cover.png",
                "width": 1080,
                "height": 1350,
                "theme": "shaheedi",
                "pill_text": "Shaheedi Week • Poh",
                "slide_label": "01 / 06",
                "footer_url": "sikhrpa.org/heritage.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;">
                  <div class="eyebrow">In Solemn Remembrance • December 1704</div>
                  <h1 class="h1-hero" style="font-size:58px;">Miri-Piri &amp; <span class="gold">Sikh Martial Heritage</span></h1>
                  {svg_dignified_divider()}
                  <p class="lead" style="max-width:840px;color:#e2e8f0;">
                    Honoring the supreme sacrifice of the <strong style="color:#fef3c7;">Chaar Sahibzaade</strong> and
                    <strong style="color:#fef3c7;">Mata Gujri Ji</strong> — and reflecting on the enduring Sikh ethic of
                    spiritual humility, moral restraint, and responsible stewardship.
                  </p>
                  <div class="pa-banner" style="width:100%;max-width:860px;text-align:center;border-left-width:1px;border-top:3px solid #d97706;">
                    <div class="gurmukhi-serif" style="font-size:29px;font-weight:700;color:#fef3c7;">
                      ਚਾਰ ਸਾਹਿਬਜ਼ਾਦਿਆਂ ਅਤੇ ਮਾਤਾ ਗੁਜਰੀ ਜੀ ਦੀ ਲਾਸਾਨੀ ਸ਼ਹਾਦਤ ਨੂੰ ਕੋਟਿ-ਕੋਟਿ ਪ੍ਰਣਾਮ
                    </div>
                  </div>
                  <div style="font-size:18px;letter-spacing:0.1em;text-transform:uppercase;color:#94a3b8;font-weight:700;margin-top:8px;">
                    Educational Curriculum • IRC § 501(c)(3) Public Charity
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-02-sahibzaade-tribute.png",
                "width": 1080,
                "height": 1350,
                "theme": "shaheedi",
                "pill_text": "Shaheedi Week Tribute",
                "slide_label": "02 / 06",
                "footer_url": "sikhrpa.org/heritage.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="eyebrow">Remembering Poh 1704</div>
                <h2 class="h1-lg">The <span class="gold">Chaar Sahibzaade</span> &amp; Mata Gujri Ji</h2>
                <p class="body-text">
                  In the freezing winter of December 1704, the four young sons of Guru Gobind Singh Ji and their grandmother
                  chose truth, conscience, and compassion over submission to tyranny.
                </p>
                <div class="grid-2" style="gap:18px;margin-top:4px;">
                  <div class="card card-gold stack-sm" style="padding:26px;">
                    <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">CHAMKAUR SAHIB • VADE SAHIBZAADE</div>
                    <div class="h3-title" style="font-size:27px;">Baba Ajit Singh Ji &amp;<br/>Baba Jujhar Singh Ji</div>
                    <p class="body-sm">Stood steadfast with serene courage and selfless duty to shield the Sangats and uphold justice against overwhelming odds.</p>
                  </div>
                  <div class="card card-gold stack-sm" style="padding:26px;">
                    <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">SIRHIND • CHHOTE SAHIBZAADE</div>
                    <div class="h3-title" style="font-size:27px;">Baba Zorawar Singh Ji,<br/>Baba Fateh Singh Ji &amp; Mata Gujri Ji</div>
                    <p class="body-sm">Endured the freezing Thanda Burj with calm prayer and unshakable faith — proving true strength is moral, never cruel.</p>
                  </div>
                </div>
                <div style="display:flex;justify-content:center;margin-top:6px;">{svg_dignified_divider()}</div>
                <p class="body-sm" style="text-align:center;color:#cbd5e1;">
                  Their memory calls every generation to live with humility, discipline, and courage in defense of the vulnerable.
                </p>
                """,
            },
            {
                "filename": "slide-03-miri-piri.png",
                "width": 1080,
                "height": 1350,
                "theme": "shaheedi",
                "pill_text": "1606 CE • Foundational Principle",
                "slide_label": "03 / 06",
                "footer_url": "sikhrpa.org/heritage.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">1606 CE • Guru Hargobind Sahib Ji</div>
                <h2 class="h1-lg"><span class="gold">Miri &amp; Piri:</span> Spiritual &amp; Civic Balance</h2>
                <p class="lead">
                  Following the martyrdom of Guru Arjan Dev Ji, the Sixth Guru established the doctrine of two inseparable responsibilities:
                </p>
                <div class="grid-2" style="gap:20px;">
                  <div class="card card-blue stack-sm" style="padding:28px;">
                    <div class="blue-lt" style="font-size:16px;font-weight:900;letter-spacing:0.1em;">PIRI • SPIRITUAL SOVEREIGNTY</div>
                    <div class="h3-title">Humility &amp; Moral Clarity</div>
                    <p class="body-text">Compassion, spiritual remembrance, ethical restraint, and unwavering respect for the sanctity of every human life.</p>
                  </div>
                  <div class="card card-gold stack-sm" style="padding:28px;">
                    <div class="gold" style="font-size:16px;font-weight:900;letter-spacing:0.1em;">MIRI • TEMPORAL DUTY</div>
                    <div class="h3-title">Civic Stewardship &amp; Protection</div>
                    <p class="body-text">Active responsibility to stand up for justice, safeguard the innocent, and refuse apathy in the face of harm.</p>
                  </div>
                </div>
                <div class="card" style="padding:22px 26px;border-left:5px solid #d97706;">
                  <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">MODERN CIVIC APPLICATION</div>
                  <p class="body-text" style="margin-top:6px;">
                    Capability without moral and spiritual restraint fails its purpose. Discipline, patience, and humility must always precede strength.
                  </p>
                </div>
                """,
            },
            {
                "filename": "slide-04-sant-sipahi.png",
                "width": 1080,
                "height": 1350,
                "theme": "shaheedi",
                "pill_text": "1699 CE • Sant-Sipahi",
                "slide_label": "04 / 06",
                "footer_url": "sikhrpa.org/heritage.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">1699 CE • Guru Gobind Singh Ji</div>
                <h2 class="h1-lg">The <span class="gold">Sant-Sipahi</span> Ideal &amp; Shastar Reverence</h2>
                <div class="stack" style="gap:18px;">
                  <div class="card card-gold stack-sm" style="padding:26px;">
                    <div class="h3-title">Saint-Soldier (Sant-Sipahi)</div>
                    <p class="body-text">
                      Formalized at Vaisakhi 1699, the Saint-Soldier unites inward equanimity (<em>Sant</em>) with outward readiness (<em>Sipahi</em>).
                      Responsibility is never driven by anger, hatred, or bravado — only by disciplined duty (<em>Dharma</em>).
                    </p>
                  </div>
                  <div class="card card-blue stack-sm" style="padding:26px;">
                    <div class="h3-title">Reverence &amp; Precision (Shastar Vidya)</div>
                    <p class="body-text">
                      Sikh tradition treats instruments of defense with solemn respect. Frivolous display, reckless handling,
                      or negligent home storage contradict centuries of reverence and careful discipline.
                    </p>
                  </div>
                  <div class="card stack-sm" style="padding:22px 26px;">
                    <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">TEMPERANCE &amp; LAW</div>
                    <p class="body-sm">
                      Emotional calm, de-escalation maturity, clean maintenance, and locked storage are the authentic contemporary expressions of this heritage.
                    </p>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-05-zafarnama.png",
                "width": 1080,
                "height": 1350,
                "theme": "shaheedi",
                "pill_text": "Zafarnama • Verse 22",
                "slide_label": "05 / 06",
                "footer_url": "sikhrpa.org/heritage.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div class="eyebrow">Sri Dasam Granth • Zafarnama (Epistle of Victory)</div>
                <h2 class="h2-title">The Ethic of <span class="gold">Last Resort &amp; Restraint</span></h2>
                <div class="card card-gold" style="padding:32px 34px;text-align:center;">
                  <div class="gurmukhi-serif" style="font-size:34px;font-weight:700;color:#fef3c7;">
                    ਚੁ ਕਾਰ ਅਜ਼ ਹਮਹ ਹੀਲਤੇ ਦਰ ਗੁਜ਼ਸ਼ਤ ॥<br/>
                    ਹਲਾਲ ਅਸਤ ਬੁਰਦਨ ਬ ਸ਼ਮਸ਼ੀਰ ਦਸਤ ॥੨੨॥
                  </div>
                  <div style="font-size:19px;font-style:italic;color:#fbbf24;margin-top:16px;font-weight:600;">
                    "Chu kar az hameh heelate dar guzasht, halal ast burdan ba shamsheer dast."
                  </div>
                  <div style="display:flex;justify-content:center;margin:18px 0;">{svg_dignified_divider()}</div>
                  <p style="font-size:24px;line-height:1.45;color:#f8fafc;font-weight:600;">
                    "When all other peaceful avenues have been exhausted and every remedy has failed, only then is it righteous to take up the sword."
                  </p>
                </div>
                <div class="card card-blue" style="padding:20px 26px;">
                  <div class="blue-lt" style="font-size:15px;font-weight:900;letter-spacing:0.08em;">MODERN LEGAL PARALLEL (CALCRIM 3470 &amp; CA PC § 417)</div>
                  <p class="body-sm" style="margin-top:6px;">
                    Both timeless Sikh ethics and California law strictly uphold de-escalation first: force is never justified in anger, vanity, or personal disputes, and brandishing is a serious crime.
                  </p>
                </div>
                """,
            },
            {
                "filename": "slide-06-modern-stewardship.png",
                "width": 1080,
                "height": 1350,
                "theme": "shaheedi",
                "pill_text": "Living the Legacy",
                "slide_label": "06 / 06",
                "footer_url": "sikhrpa.org/heritage.html",
                "footer_right": "SAVE & SHARE",
                "body_html": """
                <div class="eyebrow">Bridging History &amp; Modern Stewardship</div>
                <h2 class="h1-lg">How We Honor This <span class="gold">Legacy Today</span></h2>
                <div class="stack" style="gap:16px;">
                  <div class="card card-gold row" style="padding:22px 24px;">
                    <span class="icon-gold">1</span>
                    <div>
                      <div class="h3-title" style="font-size:25px;">Protect Every Child &amp; Household</div>
                      <p class="body-sm">Securing every firearm in a CA DOJ-approved safe or lockbox (PC § 25100) honors the core duty to protect the vulnerable.</p>
                    </div>
                  </div>
                  <div class="card card-blue row" style="padding:22px 24px;">
                    <span class="icon-ok">2</span>
                    <div>
                      <div class="h3-title" style="font-size:25px;">Practice De-Escalation &amp; Humility</div>
                      <p class="body-sm">Resolve disputes with calm patience, obey all California statutes, and model exemplary civic conduct.</p>
                    </div>
                  </div>
                  <div class="card row" style="padding:22px 24px;">
                    <span class="icon-gold">3</span>
                    <div>
                      <div class="h3-title" style="font-size:25px;">Serve the Sangat Through Education</div>
                      <p class="body-sm">Share bilingual safety literacy, safe storage awareness, and Stop the Bleed skills with our wider community.</p>
                    </div>
                  </div>
                </div>
                <div class="cta-box" style="padding:20px 26px;">
                  <div>
                    <div class="pa-text-md" style="font-size:24px;">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                    <div style="font-size:17px;color:#cbd5e1;font-weight:700;">Stay Safe, Be Responsible! • Read full curriculum</div>
                  </div>
                  <div class="url-chip" style="font-size:18px;">sikhrpa.org/heritage.html</div>
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # POST 11 — Thu, Dec 24, 2026 • 4:00 PM PST • Poster 4:5 + Story 9:16
    # =========================================================================
    post_11 = {
        "number": 11,
        "slug": "post-11-host-2027-gurdwara-workshop",
        "date_iso": "2026-12-24",
        "date_display": "Thu, Dec 24, 2026",
        "time_pst": "4:00 PM PST",
        "week": 4,
        "format": "Single Community Poster (4:5) + Story Template (9:16)",
        "format_type": "single",
        "title": "Host a Free 2027 Safety & Safe Storage Workshop at Your Gurdwara",
        "url": "https://sikhrpa.org/",
        "caption": (
            "Planning your Gurdwara Sahib or Sikh community center's 2027 educational calendar? "
            "Partner with SikhRPA to host a 100% FREE bilingual Safety & Safe Storage Workshop!\n\n"
            "What SikhRPA provides at zero cost to your Gurdwara or Sangat:\n"
            "• Certified bilingual instructors presenting in Punjabi & English\n"
            "• Practical California Safe Storage education (CA Penal Code § 25100) & child safety rules\n"
            "• Welcoming, classroom-only environment open to families, women (Bibian), elders & absolute beginners\n"
            "• Optional Stop the Bleed / Gurdwara bleeding-control cabinet & Sevadaar readiness briefing\n"
            "• FREE CA DOJ-approved cable safety locks & printed bilingual safety handbooks for every attending family\n\n"
            "ਗੁਰਦੁਆਰਾ ਸਾਹਿਬ ਵਿਖੇ ਕੈਂਪ: ਆਪਣੇ ਸਥਾਨਕ ਗੁਰਦੁਆਰਾ ਸਾਹਿਬ ਵਿੱਚ ਪੰਜਾਬੀ ਵਿੱਚ ਮੁਫ਼ਤ ਸੁਰੱਖਿਆ ਸੈਮੀਨਾਰ ਕਰਵਾਉਣ "
            "ਲਈ ਸਾਨੂੰ ਈਮੇਲ ਕਰੋ: president@sikhrpa.org\n\n"
            "Reserve a 2027 date for your Bay Area, Central Valley, Sacramento, or Southern California Gurdwara:\n"
            "Email: president@sikhrpa.org | Web: sikhrpa.org | Federal EIN: 42-2595402\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #GurdwaraOutreach #SafeStorage #CommunityWorkshop #FirearmSafetyEducation "
            "#BilingualEducation #PunjabiCommunity #CaliforniaSikhs #SikhCommunity "
            "#PublicSafetyEducation #Nonprofit501c3 #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Upload story-01-workshop-share.png (9:16) to your Story! Invite followers to tag their local "
            "California Gurdwara committee or forward the Story to a Sevadaar, and add a Link sticker to "
            "https://sikhrpa.org/ with text 'Email president@sikhrpa.org for 2027 dates'."
        ),
        "slides": [
            {
                "filename": "post-01-poster.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "2027 Community Booking",
                "slide_label": "FREE SERVICE",
                "footer_url": "president@sikhrpa.org • sikhrpa.org",
                "footer_right": "SHARE WITH COMMITTEE",
                "body_html": f"""
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <div class="stack-sm">
                    <div class="eyebrow">2027 California Gurdwara Outreach</div>
                    <h1 class="h1-lg" style="font-size:50px;">Host a Free <span class="gold">Safety &amp; Safe Storage</span> Workshop</h1>
                  </div>
                  <img class="brand-logo" style="width:118px;height:118px;border-width:3px;" src="{logo}" alt="SikhRPA"/>
                </div>
                <div class="pa-banner">
                  <div class="pa-text-md">ਗੁਰਦੁਆਰਾ ਸਾਹਿਬ ਵਿਖੇ 2027 ਲਈ ਮੁਫ਼ਤ ਪੰਜਾਬੀ ਅਤੇ ਅੰਗਰੇਜ਼ੀ ਸੁਰੱਖਿਆ ਸੈਮੀਨਾਰ ਬੁੱਕ ਕਰੋ</div>
                </div>
                <div class="card card-blue stack" style="padding:24px 26px;">
                  <div class="gold" style="font-size:15px;font-weight:900;letter-spacing:0.09em;">100% FREE CLASSROOM CURRICULUM FOR YOUR SANGAT</div>
                  <ul class="check-list" style="gap:13px;">
                    <li><span class="icon-ok">✓</span><span><strong>Bilingual Certified Instructors</strong> teaching clearly in Punjabi &amp; English</span></li>
                    <li><span class="icon-ok">✓</span><span><strong>CA Safe Storage Law (PC § 25100)</strong> &amp; 4 Rules for Child Household Safety</span></li>
                    <li><span class="icon-ok">✓</span><span><strong>Open to Families, Women &amp; Beginners</strong> — respectful, classroom-only education</span></li>
                    <li><span class="icon-ok">✓</span><span><strong>Stop the Bleed &amp; Trauma Kit Readiness</strong> guidance for Gurdwara Sevadaars</span></li>
                    <li><span class="icon-ok">✓</span><span><strong>FREE CA DOJ Cable Safety Locks</strong> &amp; printed bilingual handbooks for families</span></li>
                  </ul>
                </div>
                <div class="cta-box" style="padding:22px 26px;">
                  <div>
                    <div style="font-size:16px;font-weight:800;letter-spacing:0.08em;color:#fde68a;text-transform:uppercase;">Book Your 2027 Date Today</div>
                    <div style="font-size:30px;font-weight:900;color:#ffffff;margin-top:4px;">president@sikhrpa.org</div>
                    <div style="font-size:16px;color:#cbd5e1;margin-top:2px;">Serving Bay Area • Central Valley • Sacramento • SoCal</div>
                  </div>
                  <div class="url-chip" style="font-size:20px;">100% FREE</div>
                </div>
                <div style="text-align:center;font-size:19px;font-weight:700;color:#fef3c7;">
                  <span class="gurmukhi">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</span> &nbsp;•&nbsp; IRS 501(c)(3) Nonprofit (EIN 42-2595402)
                </div>
                """,
            },
            {
                "filename": "story-01-workshop-share.png",
                "width": 1080,
                "height": 1920,
                "theme": "royal",
                "frame_variant": "story-frame",
                "pill_text": "2027 Gurdwara Seminars",
                "slide_label": "SHARE STORY",
                "footer_url": "president@sikhrpa.org",
                "footer_right": "TAG YOUR GURDWARA ↑",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:26px;">
                  <img class="brand-logo" style="width:136px;height:136px;border-width:3.5px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">2027 Calendar Now Open • 100% Free</div>
                  <h1 class="h1-hero" style="font-size:58px;">Bring a Free <span class="gold">Safety Workshop</span> to Your Gurdwara</h1>
                  <div class="pa-banner" style="width:100%;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;">
                    <div class="pa-text-md">ਸਾਡੇ ਹਰ ਸੈਮੀਨਾਰ ਵਿੱਚ ਮੁਫ਼ਤ ਕੈਲੀਫੋਰਨੀਆ DOJ ਲਾਕ ਅਤੇ ਪੰਜਾਬੀ ਗਾਈਡਾਂ ਵੰਡੀਆਂ ਜਾਂਦੀਆਂ ਹਨ।</div>
                  </div>
                  <div class="card card-blue" style="width:100%;text-align:left;padding:28px;">
                    <ul class="check-list" style="gap:16px;">
                      <li><span class="icon-ok">✓</span><span>Bilingual Safe Storage &amp; Child Safety (PC § 25100)</span></li>
                      <li><span class="icon-ok">✓</span><span>Stop the Bleed &amp; Gurdwara First-Aid Readiness</span></li>
                      <li><span class="icon-ok">✓</span><span>Free CA DOJ Cable Safety Locks for Every Family</span></li>
                    </ul>
                  </div>
                  <div class="sticker-zone" style="width:100%;min-height:220px;">
                    <div style="font-size:19px;font-weight:900;letter-spacing:0.1em;color:#fbbf24;">TAG YOUR GURDWARA COMMITTEE OR SEND TO A SEVADAAR</div>
                    <div style="font-size:32px;font-weight:900;color:#ffffff;">president@sikhrpa.org</div>
                    <div style="font-size:19px;color:#cbd5e1;">sikhrpa.org • California 501(c)(3) Nonprofit</div>
                  </div>
                  <div class="pa-text-md">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                </div>
                """,
            },
        ],
    }

    # =========================================================================
    # POST 12 — Sat, Dec 26, 2026 • 10:30 AM PST • 9:16 Reel Cover + 5-Slide Carousel
    # =========================================================================
    post_12 = {
        "number": 12,
        "slug": "post-12-year-end-501c3-giving-appeal",
        "date_iso": "2026-12-26",
        "date_display": "Sat, Dec 26, 2026",
        "time_pst": "10:30 AM PST",
        "week": 4,
        "format": "Reel Cover (9:16) + Carousel (5 slides, 4:5)",
        "format_type": "carousel",
        "title": "Year-End 501(c)(3) Tax-Deductible Giving Appeal (Before Dec 31)",
        "url": "https://sikhrpa.org/donate.html",
        "caption": (
            "Only 5 days remain to make a 2026 tax-deductible contribution before December 31 at 11:59 PM!\n\n"
            "Because the Sikh Rifle and Pistol Association (SikhRPA) is an IRS-recognized 501(c)(3) public charity "
            "(Federal EIN: 42-2595402), every dollar you give is tax-deductible under IRC § 170 and directly powers "
            "free public safety education in 2027:\n\n"
            "• $20 — Provides 1 free CA DOJ-approved cable safety lock for a California family\n"
            "• $50 — Prints and distributes 100 pocket English & Gurmukhi safety reference manuals\n"
            "• $150 — Supplies 10 beginner students with ANSI Z87.1 eye & 30+ dB ear protection\n"
            "• $1,000 — Fully sponsors an in-person bilingual Gurdwara Safety & Safe Storage Workshop\n\n"
            "Ways to Give Before Dec 31:\n"
            "1. Zelle® (0% Fees — 100% to mission): Tag 'sikhrpa' (include your email in the memo for your IRS receipt)\n"
            "2. PayPal / Card / Venmo: sikhrpa.org/donate.html (PayPal ID: #S5PAN9B85U28J)\n"
            "3. Employer Corporate Match: Search EIN 42-2595402 in Benevity or CyberGrants — double your impact!\n"
            "4. Official IRS Tax Receipt / Form W-9: Request anytime at sikhrpa.org/receipt.html or president@sikhrpa.org\n\n"
            "Thank you for standing with us to keep California families safe, informed, and compliant.\n\n"
            "ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ! — Stay Safe, Be Responsible!"
        ),
        "hashtags": (
            "#SikhRPA #YearEndGiving #Nonprofit501c3 #TaxDeductible #PublicSafetyEducation "
            "#SafeStorage #FirearmSafetyEducation #Dasvandh #SikhCommunity #CaliforniaSikhs "
            "#PunjabiCommunity #StaySafeBeResponsible"
        ),
        "story_prompt": (
            "Post reel-00-cover.png (9:16) as a Year-End Countdown Story or Reel cover! Add an Instagram "
            "'Countdown' sticker set to Dec 31, 2026 11:59 PM PST ('2026 Tax-Deductible Giving Closes') "
            "and a Link sticker directly to https://sikhrpa.org/donate.html."
        ),
        "slides": [
            {
                "filename": "reel-00-cover.png",
                "width": 1080,
                "height": 1920,
                "theme": "royal",
                "frame_variant": "reel-cover",
                "pill_text": "Year-End Giving • 5 Days Left",
                "slide_label": "REEL COVER",
                "footer_url": "sikhrpa.org/donate.html",
                "footer_right": "GIVE BEFORE DEC 31",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:28px;">
                  <img class="brand-logo" style="width:146px;height:146px;border-width:3.5px;" src="{logo}" alt="SikhRPA"/>
                  <div class="reel-badge">5 Days Left • Tax-Deductible Before Dec 31</div>
                  <h1 class="h1-hero" style="font-size:64px;">Support <span class="gold">Community Safety</span> for 2027</h1>
                  <p class="lead" style="font-size:28px;max-width:840px;">
                    Every 501(c)(3) gift funds free bilingual safety manuals, free CA DOJ cable locks, and Gurdwara workshops.
                  </p>
                  <div class="stat-row" style="width:100%;">
                    <div class="stat-box">
                      <div class="stat-val">$20</div>
                      <div class="stat-lbl">1 Family Lock</div>
                    </div>
                    <div class="stat-box">
                      <div class="stat-val">$50</div>
                      <div class="stat-lbl">100 Bilingual Guides</div>
                    </div>
                    <div class="stat-box">
                      <div class="stat-val">0% Fee</div>
                      <div class="stat-lbl">Zelle: sikhrpa</div>
                    </div>
                  </div>
                  <div class="url-chip" style="font-size:26px;padding:16px 34px;">sikhrpa.org/donate.html</div>
                  <div style="font-size:20px;font-weight:800;color:#fde68a;">IRS 501(c)(3) Public Charity • Federal EIN: 42-2595402</div>
                </div>
                """,
            },
            {
                "filename": "slide-01-cover.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Year-End 501(c)(3) Appeal",
                "slide_label": "01 / 05",
                "footer_url": "sikhrpa.org/donate.html",
                "footer_right": "SWIPE →",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:22px;">
                  <img class="cover-logo-hero" style="width:154px;height:154px;" src="{logo}" alt="SikhRPA"/>
                  <div class="eyebrow">5 Days Left for 2026 Tax Credit • IRC § 170</div>
                  <h1 class="h1-hero" style="font-size:56px;">Make Your <span class="gold">Year-End Gift</span><br/>Before December 31</h1>
                  <p class="lead" style="max-width:840px;">
                    Help expand free bilingual firearm safety education, safe storage cable locks, and Gurdwara workshops across California in 2027.
                  </p>
                  <div class="pa-banner" style="width:100%;max-width:860px;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;">
                    <div class="pa-text-md">ਟੈਕਸ-ਮੁਕਤ ਦਾਨ (IRC § 170) — ਸੁਰੱਖਿਅਤ ਪਰਿਵਾਰਾਂ ਅਤੇ ਜਾਗਰੂਕ ਸਮਾਜ ਲਈ ਯੋਗਦਾਨ ਪਾਓ</div>
                  </div>
                  <div class="stat-row" style="width:100%;">
                    <div class="stat-box">
                      <div class="stat-val">100%</div>
                      <div class="stat-lbl">Tax-Deductible</div>
                    </div>
                    <div class="stat-box">
                      <div class="stat-val">42-2595402</div>
                      <div class="stat-lbl">Federal EIN</div>
                    </div>
                    <div class="stat-box">
                      <div class="stat-val">Dec 31</div>
                      <div class="stat-lbl">2026 Deadline</div>
                    </div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-02-what-we-built.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Mission Transparency",
                "slide_label": "02 / 05",
                "footer_url": "sikhrpa.org/donate.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Your Generosity in Action</div>
                <h2 class="h1-lg">What Your Support <span class="gold">Powers in 2027</span></h2>
                <p class="body-text">
                  As a California nonprofit public benefit corporation, 100% of board-governed disbursements serve our exempt public safety mission:
                </p>
                <div class="stack" style="gap:16px;margin-top:6px;">
                  <div class="card card-gold row" style="padding:22px 24px;">
                    <div class="num-badge">1</div>
                    <div class="stack-sm">
                      <div class="h3-title" style="font-size:26px;">Free Bilingual Digital Safety Portal</div>
                      <p class="body-sm">Maintaining all 6 free tools at sikhrpa.org — FSC Practice Exam, Buyer Compliance Guide, Shot Diagnostic, Zeroing Calculator, Trauma Guide &amp; Daily Legal Watch.</p>
                    </div>
                  </div>
                  <div class="card card-blue row" style="padding:22px 24px;">
                    <div class="num-badge num-badge-blue">2</div>
                    <div class="stack-sm">
                      <div class="h3-title" style="font-size:26px;">Free CA DOJ-Approved Cable Safety Locks</div>
                      <p class="body-sm">Distributing free locking devices to California households and first-time owners to prevent tragic child accidents.</p>
                    </div>
                  </div>
                  <div class="card card-emerald row" style="padding:22px 24px;">
                    <div class="num-badge" style="background:linear-gradient(135deg,#059669,#10b981);color:#fff;">3</div>
                    <div class="stack-sm">
                      <div class="h3-title" style="font-size:26px;">Statewide Gurdwara Clinics &amp; Printed Handbooks</div>
                      <p class="body-sm">Bringing certified bilingual instructors, printed English/Gurmukhi tri-fold guides, and bleeding-control awareness to California Gurdwaras.</p>
                    </div>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-03-impact-tiers.png",
                "width": 1080,
                "height": 1350,
                "theme": "default",
                "pill_text": "Community Impact Tiers",
                "slide_label": "03 / 05",
                "footer_url": "sikhrpa.org/donate.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Every Dollar Protects Families</div>
                <h2 class="h1-lg">Choose Your <span class="gold">2026 Year-End Impact</span></h2>
                <div class="grid-2" style="gap:18px;margin-top:4px;">
                  <div class="card card-gold stack-sm" style="padding:24px;">
                    <div style="font-size:50px;font-weight:900;color:#fbbf24;line-height:1;">$20</div>
                    <div class="h3-title" style="font-size:25px;">1 CA DOJ Cable Lock</div>
                    <p class="body-sm">Gifted free to a first-time owner or young family for immediate safe home storage.</p>
                  </div>
                  <div class="card card-blue stack-sm" style="padding:24px;">
                    <div style="font-size:50px;font-weight:900;color:#93c5fd;line-height:1;">$50</div>
                    <div class="h3-title" style="font-size:25px;">100 Bilingual Manuals</div>
                    <p class="body-sm">Prints &amp; distributes 100 pocket-sized English &amp; Gurmukhi safety reference guides.</p>
                  </div>
                  <div class="card card-emerald stack-sm" style="padding:24px;">
                    <div style="font-size:50px;font-weight:900;color:#34d399;line-height:1;">$150</div>
                    <div class="h3-title" style="font-size:25px;">10 Student Safety Kits</div>
                    <p class="body-sm">Certified ANSI Z87.1 eye protection, 30+ dB hearing protection &amp; targets for beginners.</p>
                  </div>
                  <div class="card card-gold stack-sm" style="padding:24px;">
                    <div style="font-size:50px;font-weight:900;color:#fbbf24;line-height:1;">$1,000</div>
                    <div class="h3-title" style="font-size:25px;">Full Gurdwara Clinic</div>
                    <p class="body-sm">Sponsors a complete in-person bilingual safe handling &amp; storage workshop.</p>
                  </div>
                </div>
                <div class="card" style="padding:18px 24px;text-align:center;">
                  <div style="font-size:20px;font-weight:800;color:#e2e8f0;">
                    💼 <span class="gold">Employer Match Eligible!</span> Double your gift via Benevity / CyberGrants using EIN <span class="gold">42-2595402</span>.
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-04-how-to-give.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Give Before Dec 31 Midnight",
                "slide_label": "04 / 05",
                "footer_url": "sikhrpa.org/donate.html",
                "footer_right": "SWIPE →",
                "body_html": """
                <div class="eyebrow">Fast, Verified &amp; Tax-Deductible</div>
                <h2 class="h1-lg">How to Give Before <span class="gold">December 31</span></h2>
                <div class="stack" style="gap:18px;margin-top:4px;">
                  <div class="card card-emerald stack-sm" style="padding:24px 28px;">
                    <div class="row" style="justify-content:space-between;">
                      <div class="h3-title">1. Zelle® Bank Transfer (0% Fees)</div>
                      <span class="pill pill-emerald" style="font-size:13px;">100% to Mission</span>
                    </div>
                    <div style="font-size:28px;font-weight:900;color:#fff;">Official Zelle® Tag: <span class="gold">sikhrpa</span></div>
                    <p class="body-sm">Verified Entity: Sikh Rifle and Pistol Association. Add your email in the memo for your official IRS acknowledgment letter.</p>
                  </div>
                  <div class="card card-blue stack-sm" style="padding:24px 28px;">
                    <div class="row" style="justify-content:space-between;">
                      <div class="h3-title">2. PayPal, Card, or Venmo</div>
                      <span class="pill pill-blue" style="font-size:13px;">Instant Receipt</span>
                    </div>
                    <div style="font-size:26px;font-weight:900;color:#fff;">Portal: <span class="gold">sikhrpa.org/donate.html</span> &nbsp;•&nbsp; ID: <span class="blue-lt">#S5PAN9B85U28J</span></div>
                    <p class="body-sm">Instant electronic IRS tax receipt emailed automatically for your 2026 tax return.</p>
                  </div>
                  <div class="card stack-sm" style="padding:22px 28px;">
                    <div class="h3-title" style="font-size:24px;">3. Check, Corporate Match, or IRS Receipt / Form W-9</div>
                    <p class="body-sm">Request a signed IRC § 170(f)(8) tax letter anytime at <strong class="gold">sikhrpa.org/receipt.html</strong> or email <strong class="gold">president@sikhrpa.org</strong>.</p>
                  </div>
                </div>
                """,
            },
            {
                "filename": "slide-05-thank-you-cta.png",
                "width": 1080,
                "height": 1350,
                "theme": "royal",
                "pill_text": "Thank You • 2026–2027",
                "slide_label": "05 / 05",
                "footer_url": "sikhrpa.org/donate.html",
                "footer_right": "SAVE & SHARE",
                "body_html": f"""
                <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;">
                  <img class="brand-logo" style="width:136px;height:136px;border-width:3.5px;" src="{logo}" alt="SikhRPA"/>
                  <div class="eyebrow">Thank You for Standing for Safety</div>
                  <h2 class="h1-hero" style="font-size:56px;">Building a <span class="gold">Safer, Informed</span> Community Together</h2>
                  <div class="pa-banner" style="width:100%;text-align:center;border-left-width:1px;border-top:4px solid #f59e0b;">
                    <div class="pa-text-lg">ਸੁਰੱਖਿਅਤ ਰਹੋ, ਜ਼ਿੰਮੇਵਾਰ ਬਣੋ!</div>
                    <div style="font-size:20px;font-weight:800;letter-spacing:0.12em;color:#cbd5e1;margin-top:4px;">STAY SAFE, BE RESPONSIBLE!</div>
                  </div>
                  <div class="url-chip" style="font-size:26px;padding:16px 36px;">sikhrpa.org/donate.html</div>
                  <div class="card" style="width:100%;padding:20px 26px;">
                    <div style="font-size:20px;font-weight:800;color:#f8fafc;">
                      Sikh Rifle and Pistol Association • IRS 501(c)(3) Public Charity
                    </div>
                    <div style="font-size:18px;color:#cbd5e1;margin-top:6px;">
                      Federal EIN: <span class="gold" style="font-weight:800;">42-2595402</span> &nbsp;•&nbsp;
                      Zelle: <span class="gold" style="font-weight:800;">sikhrpa</span> &nbsp;•&nbsp;
                      <span class="gold" style="font-weight:800;">president@sikhrpa.org</span>
                    </div>
                  </div>
                </div>
                """,
            },
        ],
    }

    return [post_07, post_08, post_09, post_10, post_11, post_12]
