"""
SikhRPA Instagram Content Series — Technical Inline SVG Diagram Generators
All geometry is computed cleanly in Python so every graphic renders razor-sharp
at 1080px+ resolution in Chromium/Playwright.
"""

from __future__ import annotations

import math


def svg_safety_rule_icon(rule_num: int) -> str:
    """Clean minimalist technical SVG badges for the 4 Universal Safety Rules."""
    if rule_num == 1:
        # Eye + Open Chamber Check
        return """
        <svg viewBox="0 0 220 140" width="220" height="140" xmlns="http://www.w3.org/2000/svg">
          <rect x="8" y="10" width="204" height="120" rx="18" fill="#0b1326" stroke="#f59e0b" stroke-width="2.5"/>
          <path d="M36 70 Q110 18 184 70 Q110 122 36 70 Z" fill="rgba(245,158,11,0.12)" stroke="#fbbf24" stroke-width="3.5"/>
          <circle cx="110" cy="70" r="24" fill="#1e3a8a" stroke="#fbbf24" stroke-width="3"/>
          <circle cx="110" cy="70" r="10" fill="#fbbf24"/>
          <path d="M88 32 L132 32 M110 22 L110 38" stroke="#34d399" stroke-width="3" stroke-linecap="round"/>
          <text x="110" y="118" text-anchor="middle" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="11.5" font-weight="800" letter-spacing="1.0">CHECK CHAMBER CLEAR</text>
        </svg>"""
    if rule_num == 2:
        # Safe Muzzle Direction Vector (Downrange / Safe Backstop)
        return """
        <svg viewBox="0 0 220 140" width="220" height="140" xmlns="http://www.w3.org/2000/svg">
          <rect x="8" y="10" width="204" height="120" rx="18" fill="#0b1326" stroke="#f59e0b" stroke-width="2.5"/>
          <line x1="34" y1="70" x2="150" y2="70" stroke="#fbbf24" stroke-width="5" stroke-dasharray="10 7" stroke-linecap="round"/>
          <polygon points="150,58 176,70 150,82" fill="#fbbf24"/>
          <rect x="180" y="34" width="14" height="72" rx="4" fill="#34d399" opacity="0.9"/>
          <circle cx="34" cy="70" r="10" fill="#1e3a8a" stroke="#60a5fa" stroke-width="3"/>
          <text x="110" y="118" text-anchor="middle" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" font-weight="800" letter-spacing="1.2">SAFE MUZZLE VECTOR</text>
        </svg>"""
    if rule_num == 3:
        # Straight Index Finger Register Outside Guard
        return """
        <svg viewBox="0 0 220 140" width="220" height="140" xmlns="http://www.w3.org/2000/svg">
          <rect x="8" y="10" width="204" height="120" rx="18" fill="#0b1326" stroke="#f59e0b" stroke-width="2.5"/>
          <rect x="34" y="42" width="152" height="22" rx="6" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
          <path d="M88 64 L88 90 Q88 98 98 98 L136 98 Q144 98 144 90 L144 64" fill="none" stroke="#64748b" stroke-width="3"/>
          <path d="M118 68 Q114 82 119 90" fill="none" stroke="#ef4444" stroke-width="3.5" stroke-linecap="round"/>
          <!-- High straight finger along frame -->
          <rect x="78" y="46" width="88" height="14" rx="7" fill="#34d399"/>
          <circle cx="158" cy="53" r="4" fill="#064e3b"/>
          <text x="110" y="118" text-anchor="middle" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" font-weight="800" letter-spacing="1.1">FINGER HIGH ON FRAME</text>
        </svg>"""
    # Rule 4: Target + Backstop Penetration Check
    return """
    <svg viewBox="0 0 220 140" width="220" height="140" xmlns="http://www.w3.org/2000/svg">
      <rect x="8" y="10" width="204" height="120" rx="18" fill="#0b1326" stroke="#f59e0b" stroke-width="2.5"/>
      <circle cx="72" cy="64" r="28" fill="none" stroke="#60a5fa" stroke-width="3"/>
      <circle cx="72" cy="64" r="16" fill="none" stroke="#fbbf24" stroke-width="3"/>
      <circle cx="72" cy="64" r="5" fill="#fbbf24"/>
      <line x1="100" y1="64" x2="152" y2="64" stroke="#f87171" stroke-width="3.5" stroke-dasharray="6 5"/>
      <path d="M158 32 L188 32 L198 96 L148 96 Z" fill="rgba(52,211,153,0.18)" stroke="#34d399" stroke-width="3"/>
      <text x="173" y="70" text-anchor="middle" fill="#34d399" font-family="Inter,sans-serif" font-size="11" font-weight="800">BERM</text>
      <text x="110" y="118" text-anchor="middle" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" font-weight="800" letter-spacing="1.1">CONFIRM SOLID BACKSTOP</text>
    </svg>"""


def svg_real_id_comparison() -> str:
    """Side-by-side visual comparison of CA 'FEDERAL LIMITS APPLY' vs REAL ID Driver's License."""
    return """
    <svg viewBox="0 0 920 355" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="caCardBg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#f8fafc"/>
          <stop offset="100%" stop-color="#e2e8f0"/>
        </linearGradient>
        <linearGradient id="caHeader" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#1e3a8a"/>
          <stop offset="100%" stop-color="#1d4ed8"/>
        </linearGradient>
      </defs>

      <!-- LEFT CARD: FEDERAL LIMITS APPLY -->
      <g transform="translate(8, 12)">
        <rect x="0" y="0" width="432" height="270" rx="18" fill="url(#caCardBg)" stroke="#ef4444" stroke-width="4"/>
        <path d="M0 18 Q0 0 18 0 L414 0 Q432 0 432 18 L432 62 L0 62 Z" fill="url(#caHeader)"/>
        <text x="20" y="29" fill="#ffffff" font-family="Inter,sans-serif" font-size="22" font-weight="900" letter-spacing="1.5">CALIFORNIA</text>
        <text x="20" y="49" fill="#bfdbfe" font-family="Inter,sans-serif" font-size="12" font-weight="700" letter-spacing="1">DRIVER LICENSE • USA</text>

        <!-- Highlighted FEDERAL LIMITS APPLY corner -->
        <rect x="242" y="10" width="178" height="42" rx="8" fill="#dc2626" stroke="#fef08a" stroke-width="2.5"/>
        <text x="331" y="29" text-anchor="middle" fill="#ffffff" font-family="Inter,sans-serif" font-size="11.5" font-weight="900" letter-spacing="0.5">FEDERAL LIMITS</text>
        <text x="331" y="44" text-anchor="middle" fill="#fef08a" font-family="Inter,sans-serif" font-size="11.5" font-weight="900" letter-spacing="1">APPLY</text>

        <!-- Photo silhouette -->
        <rect x="22" y="82" width="106" height="132" rx="10" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5"/>
        <circle cx="75" cy="126" r="24" fill="#64748b"/>
        <path d="M40 202 Q75 162 110 202 Z" fill="#64748b"/>

        <!-- Card fields -->
        <text x="148" y="102" fill="#dc2626" font-family="Inter,sans-serif" font-size="13" font-weight="800">DL  A1234567</text>
        <text x="148" y="124" fill="#0f172a" font-family="Inter,sans-serif" font-size="15" font-weight="800">SINGH, SAMPLE</text>
        <text x="148" y="144" fill="#475569" font-family="Inter,sans-serif" font-size="12.5" font-weight="600">1234 OAK AVE</text>
        <text x="148" y="161" fill="#475569" font-family="Inter,sans-serif" font-size="12.5" font-weight="600">SACRAMENTO, CA 95814</text>
        <rect x="148" y="180" width="256" height="68" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
        <text x="162" y="203" fill="#b91c1c" font-family="Inter,sans-serif" font-size="13" font-weight="900">COUNTER REJECTION RISK</text>
        <text x="162" y="222" fill="#7f1d1d" font-family="Inter,sans-serif" font-size="12" font-weight="700">MUST also bring U.S. Passport,</text>
        <text x="162" y="238" fill="#7f1d1d" font-family="Inter,sans-serif" font-size="12" font-weight="700">Birth Cert., or Green Card (I-551)</text>
      </g>

      <!-- Left bottom status pill -->
      <rect x="20" y="298" width="408" height="44" rx="22" fill="rgba(239,68,68,0.22)" stroke="#f87171" stroke-width="2"/>
      <text x="224" y="325" text-anchor="middle" fill="#fecaca" font-family="Inter,sans-serif" font-size="13.2" font-weight="900" letter-spacing="0.4">✗  REQUIRES SECONDARY LEGAL PRESENCE DOC</text>

      <!-- VS Divider Badge -->
      <circle cx="460" cy="148" r="24" fill="#0f172a" stroke="#f59e0b" stroke-width="3"/>
      <text x="460" y="154" text-anchor="middle" fill="#fbbf24" font-family="Inter,sans-serif" font-size="16" font-weight="900">VS</text>

      <!-- RIGHT CARD: REAL ID -->
      <g transform="translate(480, 12)">
        <rect x="0" y="0" width="432" height="270" rx="18" fill="url(#caCardBg)" stroke="#10b981" stroke-width="4"/>
        <path d="M0 18 Q0 0 18 0 L414 0 Q432 0 432 18 L432 62 L0 62 Z" fill="url(#caHeader)"/>
        <text x="20" y="29" fill="#ffffff" font-family="Inter,sans-serif" font-size="22" font-weight="900" letter-spacing="1.5">CALIFORNIA</text>
        <text x="20" y="49" fill="#bfdbfe" font-family="Inter,sans-serif" font-size="12" font-weight="700" letter-spacing="1">DRIVER LICENSE • REAL ID</text>

        <!-- Highlighted REAL ID Golden Bear + White Star corner -->
        <rect x="302" y="8" width="118" height="46" rx="10" fill="rgba(245,158,11,0.25)" stroke="#fbbf24" stroke-width="2.5"/>
        <!-- Stylized Golden Bear silhouette -->
        <g transform="translate(320, 14)">
          <path d="M12 24 C8 22 6 17 10 12 C14 7 24 6 32 7 C40 8 49 6 56 9 C62 11 66 15 65 20 C64 25 60 28 57 32 L51 32 L50 25 L36 25 L35 32 L28 32 L27 25 L19 25 L18 32 L12 32 Z" fill="#f59e0b"/>
          <circle cx="62" cy="12" r="4" fill="#f59e0b"/>
          <!-- White REAL ID star inside bear -->
          <polygon points="39,10 41,15 46,15 42,18 43.5,23 39,20 34.5,23 36,18 32,15 37,15" fill="#ffffff"/>
        </g>

        <!-- Photo silhouette -->
        <rect x="22" y="82" width="106" height="132" rx="10" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5"/>
        <circle cx="75" cy="126" r="24" fill="#64748b"/>
        <path d="M40 202 Q75 162 110 202 Z" fill="#64748b"/>

        <!-- Card fields -->
        <text x="148" y="102" fill="#1e3a8a" font-family="Inter,sans-serif" font-size="13" font-weight="800">DL  B9876543</text>
        <text x="148" y="124" fill="#0f172a" font-family="Inter,sans-serif" font-size="15" font-weight="800">KAUR, SAMPLE</text>
        <text x="148" y="144" fill="#475569" font-family="Inter,sans-serif" font-size="12.5" font-weight="600">1234 OAK AVE</text>
        <text x="148" y="161" fill="#475569" font-family="Inter,sans-serif" font-size="12.5" font-weight="600">SACRAMENTO, CA 95814</text>
        <rect x="148" y="180" width="256" height="68" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
        <text x="162" y="203" fill="#047857" font-family="Inter,sans-serif" font-size="13" font-weight="900">GOLDEN BEAR + STAR PRESENT</text>
        <text x="162" y="222" fill="#065f46" font-family="Inter,sans-serif" font-size="12" font-weight="700">Satisfies federal ID rule alone.</text>
        <text x="162" y="238" fill="#065f46" font-family="Inter,sans-serif" font-size="12" font-weight="700">(Handguns still need Proof of Residency)</text>
      </g>

      <!-- Right bottom status pill -->
      <rect x="500" y="298" width="392" height="44" rx="22" fill="rgba(16,185,129,0.2)" stroke="#34d399" stroke-width="2"/>
      <text x="696" y="326" text-anchor="middle" fill="#a7f3d0" font-family="Inter,sans-serif" font-size="15" font-weight="900" letter-spacing="0.6">✓  REAL ID COMPLIANT PRIMARY ID</text>
    </svg>"""


def svg_dros_timeline() -> str:
    """Exact 10-Day (240-Hour) + 30-Day Expiration DROS Timeline SVG."""
    return """
    <svg viewBox="0 0 920 310" width="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Track background -->
      <line x1="78" y1="120" x2="842" y2="120" stroke="#334155" stroke-width="10" stroke-linecap="round"/>
      <!-- Active 10-day segment (amber) -->
      <line x1="78" y1="120" x2="520" y2="120" stroke="#f59e0b" stroke-width="10" stroke-linecap="round"/>
      <!-- Pickup window segment (emerald) -->
      <line x1="520" y1="120" x2="842" y2="120" stroke="#10b981" stroke-width="10" stroke-linecap="round"/>

      <!-- Span bracket: 240 Hours -->
      <path d="M90 74 L90 54 L508 54 L508 74" fill="none" stroke="#fbbf24" stroke-width="2.5"/>
      <rect x="194" y="26" width="212" height="40" rx="20" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
      <text x="300" y="52" text-anchor="middle" fill="#fef3c7" font-family="Inter,sans-serif" font-size="16" font-weight="900">EXACT 240-HOUR WAIT</text>

      <!-- Span bracket: 20-day pickup window -->
      <path d="M532 74 L532 54 L832 54 L832 74" fill="none" stroke="#34d399" stroke-width="2.5"/>
      <rect x="580" y="26" width="204" height="40" rx="20" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
      <text x="682" y="52" text-anchor="middle" fill="#a7f3d0" font-family="Inter,sans-serif" font-size="15" font-weight="900">20-DAY PICKUP WINDOW</text>

      <!-- Node 1: Day 0 -->
      <circle cx="78" cy="120" r="24" fill="#1e3a8a" stroke="#fbbf24" stroke-width="4"/>
      <text x="78" y="126" text-anchor="middle" fill="#ffffff" font-family="Inter,sans-serif" font-size="16" font-weight="900">D0</text>
      <rect x="10" y="160" width="210" height="132" rx="14" fill="rgba(30,58,138,0.45)" stroke="#60a5fa" stroke-width="1.8"/>
      <text x="24" y="188" fill="#fbbf24" font-family="Inter,sans-serif" font-size="16" font-weight="900">DAY 0 • SUBMIT DROS</text>
      <text x="24" y="212" fill="#e2e8f0" font-family="Inter,sans-serif" font-size="14" font-weight="600">Example: Dec 8 • 2:15 PM</text>
      <text x="24" y="234" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5">• CA DOJ fee ~$37.19</text>
      <text x="24" y="254" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5">• Verify spelling exact</text>
      <text x="24" y="274" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5">• Timer starts to the sec</text>

      <!-- Node 2: Day 10 -->
      <circle cx="520" cy="120" r="24" fill="#059669" stroke="#a7f3d0" stroke-width="4"/>
      <text x="520" y="126" text-anchor="middle" fill="#ffffff" font-family="Inter,sans-serif" font-size="15" font-weight="900">D10</text>
      <rect x="355" y="160" width="275" height="132" rx="14" fill="rgba(6,95,70,0.38)" stroke="#34d399" stroke-width="1.8"/>
      <text x="371" y="188" fill="#34d399" font-family="Inter,sans-serif" font-size="16" font-weight="900">DAY 10 • EARLIEST RELEASE</text>
      <text x="371" y="212" fill="#e2e8f0" font-family="Inter,sans-serif" font-size="14" font-weight="600">Example: Dec 18 • 2:15:01 PM</text>
      <text x="371" y="234" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5">• Must pass full 240 hours</text>
      <text x="371" y="254" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5">• Complete Safe Handling Demo</text>
      <text x="371" y="274" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5">• DOJ Lock or Safe Affidavit</text>

      <!-- Node 3: Day 30 -->
      <circle cx="842" cy="120" r="24" fill="#b91c1c" stroke="#fca5a5" stroke-width="4"/>
      <text x="842" y="126" text-anchor="middle" fill="#ffffff" font-family="Inter,sans-serif" font-size="15" font-weight="900">D30</text>
      <rect x="652" y="160" width="258" height="132" rx="14" fill="rgba(185,28,28,0.28)" stroke="#f87171" stroke-width="1.8"/>
      <text x="668" y="188" fill="#fca5a5" font-family="Inter,sans-serif" font-size="16" font-weight="900">DAY 30 • EXPIRATION</text>
      <text x="668" y="212" fill="#e2e8f0" font-family="Inter,sans-serif" font-size="14" font-weight="600">Hard Statutory Deadline</text>
      <text x="668" y="234" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5">• Unclaimed DROS cancels</text>
      <text x="668" y="254" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5">• Must re-file &amp; repay fee</text>
      <text x="668" y="274" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5">• Restarts new 10-day wait</text>
    </svg>"""


def svg_storage_tier_icon(level: int) -> str:
    """Clean vector icons for 3 Levels of CA DOJ Safe Home Storage."""
    if level == 1:
        return """
        <svg viewBox="0 0 110 90" width="110" height="90" xmlns="http://www.w3.org/2000/svg">
          <path d="M26 42 C26 14 84 14 84 42" fill="none" stroke="#94a3b8" stroke-width="7" stroke-linecap="round"/>
          <rect x="33" y="42" width="44" height="36" rx="8" fill="#d97706" stroke="#fde68a" stroke-width="2.5"/>
          <circle cx="55" cy="57" r="5" fill="#0f172a"/>
          <rect x="53" y="59" width="4" height="10" rx="2" fill="#0f172a"/>
        </svg>"""
    if level == 2:
        return """
        <svg viewBox="0 0 110 90" width="110" height="90" xmlns="http://www.w3.org/2000/svg">
          <rect x="12" y="20" width="86" height="54" rx="10" fill="#1e3a8a" stroke="#60a5fa" stroke-width="3"/>
          <rect x="22" y="34" width="38" height="26" rx="6" fill="#0f172a" stroke="#fbbf24" stroke-width="2"/>
          <circle cx="33" cy="47" r="4" fill="#34d399"/>
          <circle cx="49" cy="47" r="4" fill="#fbbf24"/>
          <rect x="70" y="34" width="18" height="26" rx="4" fill="#0f172a" stroke="#94a3b8" stroke-width="1.8"/>
          <circle cx="79" cy="47" r="5" fill="none" stroke="#34d399" stroke-width="2"/>
        </svg>"""
    return """
    <svg viewBox="0 0 110 90" width="110" height="90" xmlns="http://www.w3.org/2000/svg">
      <rect x="18" y="8" width="74" height="74" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="3.5"/>
      <rect x="27" y="17" width="56" height="56" rx="5" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
      <circle cx="55" cy="45" r="15" fill="none" stroke="#fbbf24" stroke-width="3.5"/>
      <line x1="55" y1="30" x2="55" y2="60" stroke="#fbbf24" stroke-width="3"/>
      <line x1="40" y1="45" x2="70" y2="45" stroke="#fbbf24" stroke-width="3"/>
      <circle cx="55" cy="45" r="5" fill="#f59e0b"/>
    </svg>"""


def svg_shot_clock_dial(size: int = 580) -> str:
    """
    Crisp 8-Sector Pistol Shot Diagnostic Target Clock Dial SVG
    highlighting the #1 most common right-handed error: 7:00–8:00 Low-Left.
    """
    cx, cy = 300, 300
    r_outer = 248
    r_inner = 58

    # 8 sectors centered on 12, 1:30, 3, 4:30, 6, 7:30, 9, 10:30
    # Angles in SVG degrees (0 deg = 3 o'clock, clockwise positive; -90 = 12 o'clock)
    sectors = [
        (-112.5, -67.5, "12:00", "Breaking Wrist Up", False),
        (-67.5, -22.5, "1:00–2:00", "Heeling", False),
        (-22.5, 22.5, "3:00", "Thumb Push", False),
        (22.5, 67.5, "4:00–5:00", "Thumb Pressure", False),
        (67.5, 112.5, "6:00", "Breaking Wrist Down", False),
        (112.5, 157.5, "7:00–8:00", "LOW-LEFT (85%)", True),
        (157.5, 202.5, "9:00", "Too Little Finger", False),
        (202.5, 247.5, "10:00–11:00", "Pushing Forward", False),
    ]

    def pt(radius: float, deg: float) -> tuple[float, float]:
        rad = math.radians(deg)
        return (cx + radius * math.cos(rad), cy + radius * math.sin(rad))

    wedge_paths = []
    label_nodes = []
    for a0, a1, clock_lbl, desc_lbl, is_hl in sectors:
        x0_o, y0_o = pt(r_outer, a0)
        x1_o, y1_o = pt(r_outer, a1)
        x1_i, y1_i = pt(r_inner, a1)
        x0_i, y0_i = pt(r_inner, a0)

        d = (
            f"M {x0_i:.2f} {y0_i:.2f} "
            f"L {x0_o:.2f} {y0_o:.2f} "
            f"A {r_outer} {r_outer} 0 0 1 {x1_o:.2f} {y1_o:.2f} "
            f"L {x1_i:.2f} {y1_i:.2f} "
            f"A {r_inner} {r_inner} 0 0 0 {x0_i:.2f} {y0_i:.2f} Z"
        )
        if is_hl:
            fill = "url(#lowLeftGrad)"
            stroke = "#fbbf24"
            sw = "4"
        else:
            fill = "rgba(30, 58, 138, 0.22)"
            stroke = "rgba(148, 163, 184, 0.34)"
            sw = "1.5"
        wedge_paths.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

        mid = (a0 + a1) / 2.0
        lbl_r = 198 if is_hl else 176
        lx, ly = pt(lbl_r, mid)
        clock_color = "#fef3c7" if is_hl else "#e2e8f0"
        desc_color = "#fbbf24" if is_hl else "#94a3b8"
        clock_fs = "17.5" if is_hl else "15"
        desc_fs = "12.5" if is_hl else "11.5"
        label_nodes.append(
            f'<text x="{lx:.1f}" y="{ly - 4:.1f}" text-anchor="middle" fill="{clock_color}" '
            f'font-family="Inter,sans-serif" font-size="{clock_fs}" font-weight="900">{clock_lbl}</text>'
            f'<text x="{lx:.1f}" y="{ly + 14:.1f}" text-anchor="middle" fill="{desc_color}" '
            f'font-family="Inter,sans-serif" font-size="{desc_fs}" font-weight="800">{desc_lbl}</text>'
        )

    # Sample low-left cluster impact markers cleanly in inner portion of 7:00-8:00 sector
    impacts = [(216, 366), (235, 378), (206, 384), (228, 396), (246, 392)]
    impact_svg = "\n".join(
        f'<circle cx="{x}" cy="{y}" r="7.5" fill="#ef4444" stroke="#fef08a" stroke-width="2.2"/>'
        for x, y in impacts
    )

    return f"""
    <svg viewBox="0 0 600 600" width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="lowLeftGrad" cx="35%" cy="68%" r="65%">
          <stop offset="0%" stop-color="rgba(239,68,68,0.72)"/>
          <stop offset="60%" stop-color="rgba(217,119,6,0.52)"/>
          <stop offset="100%" stop-color="rgba(185,28,28,0.45)"/>
        </radialGradient>
      </defs>

      <!-- Outer calibration ring -->
      <circle cx="{cx}" cy="{cy}" r="276" fill="#090e1a" stroke="rgba(245,158,11,0.45)" stroke-width="2.5"/>
      <circle cx="{cx}" cy="{cy}" r="258" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5" stroke-dasharray="4 6"/>

      <!-- 8 Sectors -->
      {"".join(wedge_paths)}

      <!-- Concentric scoring rings -->
      <circle cx="{cx}" cy="{cy}" r="196" fill="none" stroke="rgba(255,255,255,0.14)" stroke-width="1.2"/>
      <circle cx="{cx}" cy="{cy}" r="134" fill="none" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
      <circle cx="{cx}" cy="{cy}" r="58" fill="rgba(16,185,129,0.22)" stroke="#34d399" stroke-width="3"/>
      <circle cx="{cx}" cy="{cy}" r="24" fill="rgba(16,185,129,0.35)" stroke="#a7f3d0" stroke-width="2"/>
      <circle cx="{cx}" cy="{cy}" r="5" fill="#a7f3d0"/>

      <!-- Crosshair axes -->
      <line x1="{cx}" y1="36" x2="{cx}" y2="564" stroke="rgba(255,255,255,0.18)" stroke-width="1.2" stroke-dasharray="5 5"/>
      <line x1="36" y1="{cy}" x2="564" y2="{cy}" stroke="rgba(255,255,255,0.18)" stroke-width="1.2" stroke-dasharray="5 5"/>

      <!-- Center bullseye label -->
      <text x="{cx}" y="{cy + 44}" text-anchor="middle" fill="#a7f3d0" font-family="Inter,sans-serif" font-size="11.5" font-weight="900" letter-spacing="1">BULLSEYE</text>

      <!-- Impact cluster in 7:00-8:00 -->
      {impact_svg}

      <!-- Labels -->
      {"".join(label_nodes)}

      <!-- Outer clock markers -->
      <text x="300" y="22" text-anchor="middle" fill="#fbbf24" font-family="Inter,sans-serif" font-size="14" font-weight="900">12</text>
      <text x="580" y="305" text-anchor="middle" fill="#94a3b8" font-family="Inter,sans-serif" font-size="14" font-weight="800">3</text>
      <text x="300" y="591" text-anchor="middle" fill="#94a3b8" font-family="Inter,sans-serif" font-size="14" font-weight="800">6</text>
      <text x="20" y="305" text-anchor="middle" fill="#94a3b8" font-family="Inter,sans-serif" font-size="14" font-weight="800">9</text>
    </svg>"""


def svg_trigger_finger_zones() -> str:
    """Clean 3-Zone Trigger Finger Placement Anatomy SVG."""
    return """
    <svg viewBox="0 0 880 230" width="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Finger silhouette -->
      <path d="M90 60 L660 60 Q790 60 790 118 Q790 176 660 176 L90 176 Z" fill="#1e293b" stroke="#94a3b8" stroke-width="3"/>
      <!-- Joint crease divider -->
      <line x1="360" y1="62" x2="360" y2="174" stroke="#f87171" stroke-width="3" stroke-dasharray="7 5"/>
      <!-- Pad zone highlight -->
      <rect x="435" y="68" width="175" height="100" rx="18" fill="rgba(16,185,129,0.22)" stroke="#34d399" stroke-width="3"/>
      <!-- Tip zone highlight -->
      <path d="M645 68 L690 68 Q780 68 780 118 Q780 168 690 168 L645 168 Z" fill="rgba(245,158,11,0.18)" stroke="#f59e0b" stroke-width="2.5"/>
      <!-- Joint zone highlight -->
      <rect x="260" y="68" width="145" height="100" rx="14" fill="rgba(239,68,68,0.2)" stroke="#ef4444" stroke-width="2.5"/>

      <!-- Labels inside zones -->
      <text x="332" y="108" text-anchor="middle" fill="#fecaca" font-family="Inter,sans-serif" font-size="15" font-weight="900">1ST JOINT CREASE</text>
      <text x="332" y="130" text-anchor="middle" fill="#fca5a5" font-family="Inter,sans-serif" font-size="13.5" font-weight="700">Too Much Finger</text>
      <text x="332" y="152" text-anchor="middle" fill="#ef4444" font-family="Inter,sans-serif" font-size="13" font-weight="900">→ 7:00–8:00 LOW-LEFT</text>

      <text x="522" y="108" text-anchor="middle" fill="#ecfdf5" font-family="Inter,sans-serif" font-size="16" font-weight="900">CENTER PAD</text>
      <text x="522" y="130" text-anchor="middle" fill="#a7f3d0" font-family="Inter,sans-serif" font-size="13.5" font-weight="800">SWEET SPOT ✓</text>
      <text x="522" y="152" text-anchor="middle" fill="#34d399" font-family="Inter,sans-serif" font-size="13" font-weight="900">100% STRAIGHT BACK</text>

      <text x="712" y="108" text-anchor="middle" fill="#fef3c7" font-family="Inter,sans-serif" font-size="15" font-weight="900">TIP ONLY</text>
      <text x="712" y="130" text-anchor="middle" fill="#fde68a" font-family="Inter,sans-serif" font-size="13.5" font-weight="700">Too Little Finger</text>
      <text x="712" y="152" text-anchor="middle" fill="#fbbf24" font-family="Inter,sans-serif" font-size="13" font-weight="900">→ 9:00 LEFT</text>

      <text x="175" y="122" text-anchor="middle" fill="#94a3b8" font-family="Inter,sans-serif" font-size="14" font-weight="800">INDEX FINGER</text>
      <text x="440" y="212" text-anchor="middle" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="15" font-weight="700">Leave daylight between finger &amp; frame — hinge straight rearward at 90°</text>
    </svg>"""


def svg_tourniquet_diagram() -> str:
    """Clean CoTCCC Tourniquet Application Diagram (2–3" above wound, no joint, windlass, time strap)."""
    return """
    <svg viewBox="0 0 920 230" width="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Stylized limb cylinder -->
      <rect x="45" y="76" width="830" height="74" rx="37" fill="#1e293b" stroke="#64748b" stroke-width="2.5"/>

      <!-- Torso direction label -->
      <text x="52" y="54" fill="#93c5fd" font-family="Inter,sans-serif" font-size="14" font-weight="800">← CLOSER TO TORSO (HIGH &amp; TIGHT)</text>

      <!-- NO JOINT red exclusion zone -->
      <rect x="195" y="68" width="118" height="90" rx="12" fill="rgba(239,68,68,0.16)" stroke="#ef4444" stroke-width="2" stroke-dasharray="6 4"/>
      <text x="254" y="109" text-anchor="middle" fill="#fca5a5" font-family="Inter,sans-serif" font-size="13" font-weight="900">NO JOINT</text>
      <text x="254" y="128" text-anchor="middle" fill="#f87171" font-family="Inter,sans-serif" font-size="11.5" font-weight="700">(Elbow / Knee)</text>

      <!-- Tourniquet strap + windlass + time strap -->
      <rect x="385" y="64" width="112" height="98" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="4"/>
      <!-- Windlass rod -->
      <rect x="406" y="42" width="70" height="14" rx="7" fill="#fbbf24" stroke="#78350f" stroke-width="2"/>
      <line x1="441" y1="56" x2="441" y2="66" stroke="#fbbf24" stroke-width="5"/>
      <!-- White TIME strap -->
      <rect x="398" y="96" width="86" height="32" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="441" y="117" text-anchor="middle" fill="#0f172a" font-family="Inter,sans-serif" font-size="14" font-weight="900">T: 14:15</text>

      <!-- 2-3 inch gap callout -->
      <line x1="504" y1="186" x2="650" y2="186" stroke="#fbbf24" stroke-width="3"/>
      <polygon points="504,186 516,180 516,192" fill="#fbbf24"/>
      <polygon points="650,186 638,180 638,192" fill="#fbbf24"/>
      <text x="577" y="212" text-anchor="middle" fill="#fef3c7" font-family="Inter,sans-serif" font-size="15" font-weight="900">2–3 INCHES ABOVE WOUND</text>

      <!-- Wound site -->
      <ellipse cx="696" cy="113" rx="34" ry="20" fill="rgba(220,38,38,0.45)" stroke="#ef4444" stroke-width="3"/>
      <text x="696" y="118" text-anchor="middle" fill="#fecaca" font-family="Inter,sans-serif" font-size="13" font-weight="900">WOUND</text>

      <!-- Callout annotations top -->
      <text x="441" y="28" text-anchor="middle" fill="#fbbf24" font-family="Inter,sans-serif" font-size="13.5" font-weight="900">TWIST WINDLASS UNTIL BLEEDING STOPS</text>
      <text x="441" y="186" text-anchor="middle" fill="#94a3b8" font-family="Inter,sans-serif" font-size="12.5" font-weight="800">NEVER LOOSEN</text>
    </svg>"""


def svg_centroid_triangulation() -> str:
    """5-Shot Group Centroid (MPI) Triangulation SVG on a crisp 1"x1" Grid."""
    # Grid spans 6"x6" centered at (240, 210), 54px per inch
    cx, cy = 240, 210
    px_per_in = 54
    grid_lines = []
    for i in range(-3, 4):
        x = cx + i * px_per_in
        y = cy + i * px_per_in
        sw = "2" if i == 0 else "1"
        col = "rgba(255,255,255,0.28)" if i == 0 else "rgba(255,255,255,0.09)"
        grid_lines.append(f'<line x1="{x}" y1="{cy - 3*px_per_in}" x2="{x}" y2="{cy + 3*px_per_in}" stroke="{col}" stroke-width="{sw}"/>')
        grid_lines.append(f'<line x1="{cx - 3*px_per_in}" y1="{y}" x2="{cx + 3*px_per_in}" y2="{y}" stroke="{col}" stroke-width="{sw}"/>')

    # 5 shots in inches relative to bullseye, exact mean = (-1.8, -2.0) -> SVG y is inverted (+down)
    shots_in = [(-2.3, -1.7), (-1.5, -2.4), (-2.0, -2.3), (-1.4, -1.6), (-1.8, -2.0)]
    mx_in = sum(s[0] for s in shots_in) / len(shots_in)
    my_in = sum(s[1] for s in shots_in) / len(shots_in)
    mx = cx + mx_in * px_per_in
    my = cy - my_in * px_per_in  # negative my_in = LOW -> larger SVG y

    tri_lines = []
    shot_dots = []
    for idx, (sx_i, sy_i) in enumerate(shots_in, start=1):
        sx = cx + sx_i * px_per_in
        sy = cy - sy_i * px_per_in
        tri_lines.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{mx:.1f}" y2="{my:.1f}" stroke="#fbbf24" stroke-width="1.8" stroke-dasharray="4 4"/>')
        shot_dots.append(
            f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="9" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>'
            f'<text x="{sx:.1f}" y="{sy + 4:.1f}" text-anchor="middle" fill="#ffffff" font-family="Inter,sans-serif" font-size="10.5" font-weight="900">{idx}</text>'
        )

    return f"""
    <svg viewBox="0 0 900 420" width="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left Target Grid -->
      <rect x="64" y="34" width="352" height="352" rx="14" fill="#0b1326" stroke="#334155" stroke-width="2"/>
      {"".join(grid_lines)}

      <!-- Bullseye rings -->
      <circle cx="{cx}" cy="{cy}" r="54" fill="none" stroke="rgba(52,211,153,0.45)" stroke-width="2"/>
      <circle cx="{cx}" cy="{cy}" r="22" fill="rgba(16,185,129,0.28)" stroke="#34d399" stroke-width="2.5"/>
      <circle cx="{cx}" cy="{cy}" r="5" fill="#34d399"/>
      <text x="{cx + 12}" y="{cy - 10}" fill="#a7f3d0" font-family="Inter,sans-serif" font-size="12" font-weight="900">POA (0,0)</text>

      <!-- Triangulation rays & 5 shots -->
      {"".join(tri_lines)}
      {"".join(shot_dots)}

      <!-- MPI Centroid Crosshair -->
      <circle cx="{mx:.1f}" cy="{my:.1f}" r="14" fill="none" stroke="#fbbf24" stroke-width="3"/>
      <line x1="{mx-18:.1f}" y1="{my:.1f}" x2="{mx+18:.1f}" y2="{my:.1f}" stroke="#fbbf24" stroke-width="2.5"/>
      <line x1="{mx:.1f}" y1="{my-18:.1f}" x2="{mx:.1f}" y2="{my+18:.1f}" stroke="#fbbf24" stroke-width="2.5"/>

      <!-- Vector arrows from MPI to Bullseye -->
      <line x1="{mx:.1f}" y1="{my:.1f}" x2="{mx:.1f}" y2="{cy}" stroke="#60a5fa" stroke-width="3.5"/>
      <polygon points="{mx:.1f},{cy} {mx-7:.1f},{cy+13} {mx+7:.1f},{cy+13}" fill="#60a5fa"/>
      <line x1="{mx:.1f}" y1="{cy}" x2="{cx}" y2="{cy}" stroke="#fbbf24" stroke-width="3.5"/>
      <polygon points="{cx},{cy} {cx-13},{cy-7} {cx-13},{cy+7}" fill="#fbbf24"/>

      <!-- Grid scale label -->
      <text x="240" y="406" text-anchor="middle" fill="#94a3b8" font-family="Inter,sans-serif" font-size="13.5" font-weight="700">1 Grid Square = 1.0" × 1.0" at Target</text>

      <!-- Right Computation Panel -->
      <g transform="translate(450, 34)">
        <rect x="0" y="0" width="430" height="352" rx="18" fill="rgba(22,34,58,0.85)" stroke="rgba(245,158,11,0.45)" stroke-width="2"/>
        <text x="26" y="40" fill="#fbbf24" font-family="Inter,sans-serif" font-size="15" font-weight="900" letter-spacing="1">5-SHOT GROUP CENTROID (MPI)</text>
        <text x="26" y="68" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="16" font-weight="600">Mean Point of Impact at 25 Yards:</text>

        <rect x="26" y="86" width="378" height="58" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <text x="44" y="122" fill="#f8fafc" font-family="Inter,sans-serif" font-size="22" font-weight="900">1.8" LEFT  •  2.0" LOW</text>

        <text x="26" y="176" fill="#93c5fd" font-family="Inter,sans-serif" font-size="14.5" font-weight="800" letter-spacing="0.8">EXACT TURRET CORRECTION (1/2 MOA @ 25 YD)</text>

        <!-- Elevation box -->
        <rect x="26" y="192" width="378" height="62" rx="12" fill="rgba(30,58,138,0.5)" stroke="#60a5fa" stroke-width="1.8"/>
        <text x="44" y="218" fill="#bfdbfe" font-family="Inter,sans-serif" font-size="13.5" font-weight="800">TOP TURRET (ELEVATION)</text>
        <text x="44" y="242" fill="#ffffff" font-family="Inter,sans-serif" font-size="20" font-weight="900">▲ DIAL 16 CLICKS "UP" (+2.0")</text>

        <!-- Windage box -->
        <rect x="26" y="268" width="378" height="62" rx="12" fill="rgba(217,119,6,0.2)" stroke="#f59e0b" stroke-width="1.8"/>
        <text x="44" y="294" fill="#fde68a" font-family="Inter,sans-serif" font-size="13.5" font-weight="800">SIDE TURRET (WINDAGE)</text>
        <text x="44" y="318" fill="#ffffff" font-family="Inter,sans-serif" font-size="20" font-weight="900">▶ DIAL 14 CLICKS "RIGHT" (+1.8")</text>
      </g>
    </svg>"""


def svg_moa_vs_mil() -> str:
    """Clean Angular Diagram contrasting MOA vs. MIL (MRAD) at 100 Yards."""
    return """
    <svg viewBox="0 0 920 265" width="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: MOA Box -->
      <rect x="8" y="10" width="440" height="245" rx="18" fill="rgba(30,58,138,0.34)" stroke="#60a5fa" stroke-width="2.2"/>
      <text x="30" y="44" fill="#93c5fd" font-family="Inter,sans-serif" font-size="22" font-weight="900">MOA (Minute of Angle)</text>
      <text x="30" y="68" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="15" font-weight="600">1/60th of 1 degree • Imperial inch standard</text>

      <!-- Angle cone MOA -->
      <circle cx="52" cy="148" r="6" fill="#60a5fa"/>
      <line x1="52" y1="148" x2="290" y2="122" stroke="#60a5fa" stroke-width="2.5"/>
      <line x1="52" y1="148" x2="290" y2="174" stroke="#60a5fa" stroke-width="2.5"/>
      <line x1="290" y1="122" x2="290" y2="174" stroke="#fbbf24" stroke-width="5"/>
      <text x="172" y="153" text-anchor="middle" fill="#94a3b8" font-family="Inter,sans-serif" font-size="13" font-weight="800">100 YARDS</text>
      <text x="306" y="144" fill="#fbbf24" font-family="Inter,sans-serif" font-size="21" font-weight="900">1.047"</text>
      <text x="306" y="166" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5" font-weight="700">(≈ 1 inch)</text>

      <rect x="28" y="196" width="400" height="42" rx="10" fill="#0f172a" stroke="rgba(96,165,250,0.4)" stroke-width="1.5"/>
      <text x="228" y="222" text-anchor="middle" fill="#e2e8f0" font-family="Inter,sans-serif" font-size="14.5" font-weight="800">1/4 MOA = 0.25" • 1/2 MOA = 0.50" • 1 MOA = 1.0"</text>

      <!-- Right: MIL Box -->
      <rect x="472" y="10" width="440" height="245" rx="18" fill="rgba(217,119,6,0.16)" stroke="#f59e0b" stroke-width="2.2"/>
      <text x="494" y="44" fill="#fbbf24" font-family="Inter,sans-serif" font-size="22" font-weight="900">MIL (Milliradian / MRAD)</text>
      <text x="494" y="68" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="15" font-weight="600">1/1000th of distance • Base-10 precision math</text>

      <!-- Angle cone MIL (wider proportional visual) -->
      <circle cx="516" cy="148" r="6" fill="#f59e0b"/>
      <line x1="516" y1="148" x2="746" y2="100" stroke="#f59e0b" stroke-width="2.5"/>
      <line x1="516" y1="148" x2="746" y2="196" stroke="#f59e0b" stroke-width="2.5"/>
      <line x1="746" y1="100" x2="746" y2="196" stroke="#34d399" stroke-width="5"/>
      <text x="634" y="153" text-anchor="middle" fill="#94a3b8" font-family="Inter,sans-serif" font-size="13" font-weight="800">100 YARDS</text>
      <text x="762" y="144" fill="#34d399" font-family="Inter,sans-serif" font-size="21" font-weight="900">3.60"</text>
      <text x="762" y="166" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="13.5" font-weight="700">(10 cm @ 100m)</text>

      <rect x="492" y="196" width="400" height="42" rx="10" fill="#0f172a" stroke="rgba(245,158,11,0.45)" stroke-width="1.5"/>
      <text x="692" y="222" text-anchor="middle" fill="#fef3c7" font-family="Inter,sans-serif" font-size="14.5" font-weight="800">0.1 MIL Click = 0.36" @ 100 yd (10 clicks/MIL)</text>
    </svg>"""


def svg_click_scaling_cone() -> str:
    """25 / 50 / 100-Yard Angular Click Scaling Cone SVG."""
    return """
    <svg viewBox="0 0 920 235" width="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Origin (Optic) -->
      <circle cx="52" cy="118" r="11" fill="#f59e0b" stroke="#fef3c7" stroke-width="3"/>
      <text x="52" y="156" text-anchor="middle" fill="#fbbf24" font-family="Inter,sans-serif" font-size="13" font-weight="900">OPTIC</text>

      <!-- Cone rays -->
      <polygon points="52,118 850,36 850,200" fill="rgba(37,99,235,0.14)"/>
      <line x1="52" y1="118" x2="850" y2="36" stroke="#60a5fa" stroke-width="2.5"/>
      <line x1="52" y1="118" x2="850" y2="200" stroke="#60a5fa" stroke-width="2.5"/>
      <line x1="52" y1="118" x2="875" y2="118" stroke="rgba(255,255,255,0.22)" stroke-width="1.5" stroke-dasharray="5 5"/>

      <!-- 25 Yards Slice -->
      <line x1="252" y1="97" x2="252" y2="139" stroke="#fbbf24" stroke-width="5"/>
      <rect x="166" y="16" width="172" height="58" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
      <text x="252" y="40" text-anchor="middle" fill="#fbbf24" font-family="Inter,sans-serif" font-size="16" font-weight="900">25 YARDS</text>
      <text x="252" y="61" text-anchor="middle" fill="#e2e8f0" font-family="Inter,sans-serif" font-size="13" font-weight="700">1/4× Value (4× Clicks)</text>

      <!-- 50 Yards Slice -->
      <line x1="452" y1="77" x2="452" y2="159" stroke="#34d399" stroke-width="5"/>
      <rect x="366" y="16" width="172" height="54" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
      <text x="452" y="39" text-anchor="middle" fill="#34d399" font-family="Inter,sans-serif" font-size="16" font-weight="900">50 YARDS</text>
      <text x="452" y="59" text-anchor="middle" fill="#e2e8f0" font-family="Inter,sans-serif" font-size="13" font-weight="700">1/2× Value (2× Clicks)</text>

      <!-- 100 Yards Slice -->
      <line x1="850" y1="36" x2="850" y2="200" stroke="#f87171" stroke-width="5"/>
      <rect x="730" y="16" width="178" height="54" rx="10" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
      <text x="819" y="39" text-anchor="middle" fill="#fca5a5" font-family="Inter,sans-serif" font-size="15.5" font-weight="900">100 YARDS (BASE)</text>
      <text x="819" y="59" text-anchor="middle" fill="#e2e8f0" font-family="Inter,sans-serif" font-size="13" font-weight="700">1× Rated Click Value</text>

      <!-- Bottom formula bar -->
      <text x="460" y="222" text-anchor="middle" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="15" font-weight="800">Closer target = smaller shift per click → MORE clicks required to move 1 inch!</text>
    </svg>"""


def svg_height_over_bore() -> str:
    """Height-Over-Bore Mechanical Offset Side-Profile SVG (Sight Line vs Bore Axis + 50/200 Arc)."""
    return """
    <svg viewBox="0 0 920 330" width="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Background grid -->
      <rect x="10" y="10" width="900" height="310" rx="18" fill="#0b1326" stroke="#334155" stroke-width="2"/>

      <!-- Optic block (top left) -->
      <rect x="38" y="108" width="92" height="30" rx="6" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2.5"/>
      <text x="84" y="128" text-anchor="middle" fill="#ffffff" font-family="Inter,sans-serif" font-size="12.5" font-weight="900">RED DOT</text>

      <!-- Barrel / Bore block (lower left) -->
      <rect x="38" y="198" width="118" height="22" rx="4" fill="#475569" stroke="#cbd5e1" stroke-width="2"/>
      <text x="95" y="213" text-anchor="middle" fill="#f8fafc" font-family="Inter,sans-serif" font-size="11.5" font-weight="900">BARREL BORE</text>

      <!-- Mechanical offset vertical bracket (2.6") -->
      <line x1="168" y1="123" x2="168" y2="209" stroke="#fbbf24" stroke-width="3"/>
      <line x1="160" y1="123" x2="176" y2="123" stroke="#fbbf24" stroke-width="2.5"/>
      <line x1="160" y1="209" x2="176" y2="209" stroke="#fbbf24" stroke-width="2.5"/>
      <!-- Clean offset callout placed above sight line with dashed leader -->
      <line x1="168" y1="84" x2="168" y2="118" stroke="#fbbf24" stroke-width="1.8" stroke-dasharray="4 3"/>
      <rect x="92" y="38" width="152" height="44" rx="10" fill="rgba(217,119,6,0.22)" stroke="#f59e0b" stroke-width="2"/>
      <text x="168" y="57" text-anchor="middle" fill="#fbbf24" font-family="Inter,sans-serif" font-size="13.5" font-weight="900">2.6" OFFSET</text>
      <text x="168" y="74" text-anchor="middle" fill="#fde68a" font-family="Inter,sans-serif" font-size="11.5" font-weight="700">(Pistol ≈ 0.8")</text>

      <!-- Line of Sight (Straight Dashed Horizontal) -->
      <line x1="130" y1="123" x2="880" y2="123" stroke="#60a5fa" stroke-width="3" stroke-dasharray="10 7"/>
      <text x="866" y="110" text-anchor="end" fill="#93c5fd" font-family="Inter,sans-serif" font-size="13.5" font-weight="800">OPTICAL LINE OF SIGHT</text>

      <!-- Ballistic Trajectory Curve (50/200 yd crossing) -->
      <path d="M 156 209 Q 520 55 876 142" fill="none" stroke="#f59e0b" stroke-width="4.5"/>

      <!-- Close range 3-7 yd drop callout -->
      <circle cx="332" cy="166" r="8" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
      <line x1="332" y1="123" x2="332" y2="166" stroke="#ef4444" stroke-width="3"/>
      <rect x="242" y="232" width="212" height="62" rx="12" fill="rgba(239,68,68,0.22)" stroke="#f87171" stroke-width="2"/>
      <text x="348" y="256" text-anchor="middle" fill="#fecaca" font-family="Inter,sans-serif" font-size="14" font-weight="900">3–7 YARDS (CLOSE RANGE)</text>
      <text x="348" y="278" text-anchor="middle" fill="#fca5a5" font-family="Inter,sans-serif" font-size="13.5" font-weight="700">Impact hits 1.5"–2.5" LOW!</text>
      <line x1="332" y1="174" x2="332" y2="232" stroke="#f87171" stroke-width="1.8" stroke-dasharray="4 4"/>

      <!-- 50-Yard First Zero Crossing -->
      <circle cx="486" cy="123" r="9" fill="#10b981" stroke="#ffffff" stroke-width="2.5"/>
      <rect x="424" y="42" width="126" height="44" rx="10" fill="rgba(16,185,129,0.24)" stroke="#34d399" stroke-width="2"/>
      <text x="487" y="61" text-anchor="middle" fill="#a7f3d0" font-family="Inter,sans-serif" font-size="14" font-weight="900">50 YD ZERO</text>
      <text x="487" y="78" text-anchor="middle" fill="#6ee7b7" font-family="Inter,sans-serif" font-size="11.5" font-weight="700">1st Crossing</text>
      <line x1="486" y1="86" x2="486" y2="114" stroke="#34d399" stroke-width="2"/>

      <!-- 120-Yard Apex (+1.8") -->
      <circle cx="645" cy="99" r="6" fill="#fbbf24"/>
      <text x="645" y="78" text-anchor="middle" fill="#fde68a" font-family="Inter,sans-serif" font-size="13" font-weight="800">~120 YD (+1.8")</text>

      <!-- 200-Yard Second Zero Crossing -->
      <circle cx="798" cy="123" r="9" fill="#10b981" stroke="#ffffff" stroke-width="2.5"/>
      <rect x="720" y="232" width="166" height="58" rx="12" fill="rgba(16,185,129,0.22)" stroke="#34d399" stroke-width="2"/>
      <text x="803" y="256" text-anchor="middle" fill="#a7f3d0" font-family="Inter,sans-serif" font-size="14.5" font-weight="900">200 YD ZERO</text>
      <text x="803" y="276" text-anchor="middle" fill="#6ee7b7" font-family="Inter,sans-serif" font-size="12.5" font-weight="700">2nd Crossing (5.56)</text>
      <line x1="798" y1="132" x2="798" y2="232" stroke="#34d399" stroke-width="1.8" stroke-dasharray="4 4"/>
    </svg>"""


def svg_dignified_divider() -> str:
    """Minimal, reverent antique-gold geometric ornament for Shaheedi Week slides."""
    return """
    <svg viewBox="0 0 600 28" width="480" height="24" xmlns="http://www.w3.org/2000/svg">
      <line x1="0" y1="14" x2="256" y2="14" stroke="rgba(217,119,6,0.55)" stroke-width="2"/>
      <polygon points="300,2 314,14 300,26 286,14" fill="none" stroke="#d97706" stroke-width="2.5"/>
      <circle cx="300" cy="14" r="4" fill="#f59e0b"/>
      <line x1="344" y1="14" x2="600" y2="14" stroke="rgba(217,119,6,0.55)" stroke-width="2"/>
    </svg>"""
