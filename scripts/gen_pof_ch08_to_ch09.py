#!/usr/bin/env python3
"""
Generator for Subject 081: Principles of Flight (Aerodynamics)
Volume 3: Chapters 08 to 09 (Transonic Aerodynamics & Swept Wings)
- Chapter 08: Transonic Aerodynamics, Critical Mach (Mcrit) & Shock Waves
- Chapter 09: Transonic Design Features (Swept Wings, Supercritical & Area Rule)

Fully aligned with CAE Oxford Principles of Flight and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/081_principles_of_flight"

def build_pof_ch08():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch08_transonic_mach_mcrit.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 8: Transonic Aerodynamics")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        8,
        "Transonic Aerodynamics, Critical Mach & Shock Waves",
        "265-304"
    )

    pdf.add_heading_1("1. Mach Regimes & Critical Mach Number (Mcrit)")
    pdf.add_paragraph(
        "Compressibility effects dominate high-speed flight as airspeed approaches the speed of sound (M = TAS / a):"
    )
    pdf.add_bullet("Mach Flight Regimes", "Subsonic: M < 0.75 (flow everywhere is subsonic); Transonic: 0.75 <= M < 1.20 (mixed subsonic and supersonic flow over airframe); Supersonic: 1.20 <= M < 5.0 (flow everywhere is supersonic); Hypersonic: M >= 5.0.")
    pdf.add_bullet("Critical Mach Number (Mcrit)", "The free-stream Mach number at which airflow over the point of maximum curvature on the upper wing surface first accelerates to local Mach 1.0 (local sonic speed).")
    pdf.add_bullet("Drag Divergence Mach Number (Mdd)", "The free-stream Mach number at which aerodynamic drag rises sharply (standard definition: where C_D increases by 0.0020 or 20 drag counts). Occurs slightly above Mcrit (typically Mcrit + 0.06 to 0.08).")

    pdf.add_heading_1("2. Normal Shock Wave Physics & Wave Drag")
    pdf.add_paragraph(
        "When local airflow exceeds Mach 1.0 on the wing upper surface, it decelerates back to subsonic speed through a NORMAL SHOCK WAVE:"
    )

    shock_table = [
        ["Fluid Property Across Normal Shock", "Upstream Supersonic Flow (Ahead of Shock)", "Downstream Subsonic Flow (Behind Shock)"],
        ["Flow Velocity / Mach Number", "Supersonic (M1 > 1.0)", "SUBSONIC (M2 < 1.0). Discontinuous deceleration!"],
        ["Static Pressure (p)", "Lower ambient pressure", "DISCONTINUOUS INSTANTANEOUS RISE (Compression step)!"],
        ["Air Temperature & Density", "Lower temperature and density", "DISCONTINUOUS INSTANTANEOUS RISE!"],
        ["Total Pressure & Usable Energy", "Higher stagnation pressure", "DECREASES SIGNIFICANTLY (Energy lost as heat/entropy)!"]
    ]
    pdf.add_table(["Fluid Property Across Normal Shock", "Upstream Supersonic Flow (Ahead of Shock)", "Downstream Subsonic Flow (Behind Shock)"], shock_table, col_widths=[140.0, 180.0, 180.0])

    pdf.add_bullet("Wave Drag", "The massive drag rise caused by energy dissipation across the shock wave combined with boundary layer separation triggered by the shock's adverse pressure jump (Shock-Induced Separation / Mach Buffet).")

    pdf.add_heading_1("3. Transonic Flight Instabilities: Mach Tuck & Mach Trim")
    pdf.add_paragraph(
        "As an aircraft accelerates beyond Mcrit into the transonic region, it experiences severe trim and stability changes:"
    )
    pdf.add_bullet("Mach Tuck (Nose-Down Pitching)", "Caused by: 1. Rearward shift of the Center of Pressure from 25% chord toward 50% chord as supersonic flow expands aft; 2. Loss of downwash over the horizontal stabilizer due to shock-induced boundary layer separation at the wing root. Both effects create a dangerous, uncommanded NOSE-DOWN PITCH (Mach Tuck)!")
    pdf.add_bullet("Mach Trim System", "An automatic electrical trim system commanded by the Air Data Computer. As Mach number exceeds a preset threshold (e.g. M 0.78), the Mach trim actuator applies progressive UP-ELEVATOR / NOSE-UP STABILIZER TRIM to counter Mach tuck automatically without pilot input.")

    pdf.add_callout(
        "trap",
        "Airflow Velocity Across a Normal Shock Wave Rule",
        "- CRITICAL EXAM TRAP: Airflow passing through a NORMAL shock wave ALWAYS leaves the shock at a SUBSONIC velocity (M < 1.0)!\n"
        "- Airflow passing through an OBLIQUE shock wave remains SUPERSONIC (M > 1.0)!\n"
        "- Static pressure, temperature, and density ALWAYS INCREASE across a shock wave, while total pressure ALWAYS DECREASES.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: What is the aerodynamic definition of the 'Critical Mach Number' (Mcrit)?",
         "[A] The Mach number where the aircraft enters a flat spin\n[B] The free-stream Mach number at which airflow over any part of the aircraft first reaches local Mach 1.0\n[C] The speed of sound at sea level\n[D] Maximum operating Mach (M_MO)",
         "CORRECT: [B]. Mcrit is the aircraft flight Mach number where the fastest local airflow accelerating over the wing upper surface first achieves sonic speed (local Mach 1.0)."),
        ("Q2: What happens to flow velocity, static pressure, and total pressure as air passes through a NORMAL SHOCK WAVE?",
         "[A] Velocity increases, static pressure decreases, total pressure increases\n[B] Velocity drops from supersonic to SUBSONIC, static pressure RISES abruptly, and total pressure DECREASES\n[C] All parameters remain constant\n[D] Velocity remains supersonic",
         "CORRECT: [B]. A normal shock wave causes an irreversible adiabatic compression: flow velocity decelerates to subsonic (< M 1.0), static pressure steps up sharply, and total pressure drops due to entropy generation."),
        ("Q3: What causes 'Mach Tuck' in transonic jet transport aircraft?",
         "[A] Flap extension at high speed\n[B] Rearward movement of the wing Center of Pressure and reduction of tailplane downwash due to shock formation, inducing an uncommanded nose-down pitching moment\n[C] Engine flameout\n[D] Rudder deflection",
         "CORRECT: [B]. Shock wave development moves the center of lift rearward toward 50% chord and disrupts downwash onto the tailplane, producing an uncommanded nose-down diving tendency countered by Mach trim.")
    ]

    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 8 compiled: {pdf_path}")


def build_pof_ch09():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch09_swept_wings_area_rule.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 9: Swept Wings & Area Rule")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        9,
        "Transonic Design Features: Swept Wings & Area Rule",
        "305-344"
    )

    pdf.add_heading_1("1. Wing Sweepback: The Effective Velocity Vector")
    pdf.add_paragraph(
        "Sweeping the wing rearward (sweep angle Lambda, typically 25° to 35°) is the primary design technique to increase Mcrit and Mdd:"
    )
    pdf.add_bullet("Velocity Decomposition", "The oncoming freestream airspeed (V) is resolved into two orthogonal components: 1. Normal Component (V_n = V x cos(Lambda)), perpendicular to the leading edge; 2. Spanwise Component (V_s = V x sin(Lambda)), parallel to the leading edge.")
    pdf.add_bullet("The Sweep Benefit", "ONLY THE NORMAL COMPONENT (V_n) produces aerodynamic pressure changes and accelerates over the airfoil! The spanwise component produces only minor skin friction. Because V_n = V x cos(Lambda) is significantly smaller than V, the effective Mach number sensed by the wing is REDUCED: M_effective = M x cos(Lambda)!")
    pdf.add_bullet("Result on Mcrit", "Sweeping a wing increases the aircraft's Critical Mach Number: M_crit(swept) = M_crit(straight) / cos(Lambda). Allows the aircraft to cruise at much higher speeds before shock waves form!")

    pdf.add_heading_1("2. Swept Wing Aerodynamic Disadvantages & Remedies")
    pdf.add_paragraph(
        "While wing sweep raises cruising Mach number, it introduces severe low-speed and stability penalties:"
    )

    swept_table = [
        ["Swept Wing Penalty / Problem", "Aerodynamic Physical Cause", "Engineering Solution & Cockpit Remedy"],
        ["Wingtip Stall Tendency", "Spanwise airflow boundary layer drift thickens at tips, causing wingtips to stall FIRST.", "Wing washout (twist), leading-edge stall fences, vortilons, and vortex generators."],
        ["Severe Pitch-Up at Stall", "Tip stall occurs behind CG on swept wings; loss of tip lift shifts resultant lift FORWARD!", "Stick Pusher system; low-mounted horizontal stabilizer to avoid deep stall wash."],
        ["Dutch Roll Instability", "Strong dihedral effect of swept wings produces coupled yaw-roll oscillation.", "Yaw Damper system (mandatory for flight dispatch under MEL)."],
        ["Reduced C_L_max & High Stall Speed", "Swept wings have a flatter lift curve slope (dC_L/dAlpha is lower).", "Complex multi-slotted Fowler flaps and leading-edge slats mandatory for take-off/landing."]
    ]
    pdf.add_table(["Swept Wing Penalty / Problem", "Aerodynamic Physical Cause", "Engineering Solution & Cockpit Remedy"], swept_table, col_widths=[125.0, 195.0, 180.0])

    pdf.add_heading_1("3. Supercritical Airfoils & The Whitcomb Area Rule")
    pdf.add_bullet("Supercritical Airfoil", "Features a FLATTENED upper surface (limits peak airflow acceleration, delaying and weakening shock waves), high aft camber (restores lift near the trailing edge), and a well-rounded leading edge. Allows higher cruising Mach numbers or thicker wings (saving structural weight).")
    pdf.add_bullet("Whitcomb Area Rule", "To minimize transonic wave drag, the cross-sectional area of the entire aircraft (fuselage + wings + engines) plotted along the longitudinal axis must change SMOOTHLY without abrupt steps. Achieved by 'pinching' the fuselage at the wing root (coke-bottle fuselage waist) or adding flap track canoe fairings / Küchemann carrots.")
    pdf.add_bullet("Vortex Generators", "Small, low-aspect-ratio vertical blades mounted on the wing upper surface at an angle of attack. Shed high-energy vortices that mix freestream energy into the boundary layer, preventing shock-induced flow separation.")

    pdf.add_callout(
        "trap",
        "Effective Mach Number on a Swept Wing Calculation",
        "- Formula: M_effective = M_free x cos(Sweep Angle Lambda)!\n"
        "- Example: An aircraft with 30° wing sweep flies at Mach 0.80.\n"
        "- The wing airfoil behaves as if it were flying at: M_eff = 0.80 x cos(30°) = 0.80 x 0.866 = MACH 0.69!\n"
        "- This delays shock wave formation by over 0.10 Mach!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch09 = [
        ("Q1: Why does sweeping an aircraft wing rearward increase the Critical Mach Number (Mcrit)?",
         "[A] It increases wing aspect ratio\n[B] It decomposes oncoming airflow, so that only the component PERPENDICULAR to the leading edge (V x cos(Lambda)) determines aerodynamic pressure acceleration\n[C] It eliminates induced drag\n[D] It shifts the CG forward",
         "CORRECT: [B]. The chordwise pressure distribution on a swept wing depends solely on the velocity component normal to the leading edge (V_n = V cos(sweep)). Because V_n is lower than true airspeed, Mcrit is delayed to a higher speed."),
        ("Q2: What dangerous aerodynamic stalling characteristic is inherently associated with a sweptback wing?",
         "[A] Wing root stall with severe nose-down pitch\n[B] WINGTIP STALL first, which causes loss of aileron roll control and an uncommanded violent NOSE-UP pitching moment\n[C] Inability to stall\n[D] Immediate flameout",
         "CORRECT: [B]. Swept wings suffer spanwise boundary layer flow that thickens the tip boundary layer, causing wingtips to stall first. Because swept wingtips are located well behind the CG, losing tip lift causes a strong pitch-up."),
        ("Q3: What design feature characterizes a 'Supercritical' airfoil?",
         "[A] A highly cambered upper surface\n[B] A flattened upper surface to weaken shock waves, combined with high aft camber to generate lift\n[C] A sharp knife-like leading edge\n[D] Negative sweep",
         "CORRECT: [B]. Supercritical airfoils feature a flattened upper surface that delays local supersonic acceleration and weakens shock waves, while deep underside curvature near the trailing edge restores required lift.")
    ]

    for q_text, opts, exp in questions_ch09:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 9 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_pof_ch08()
    build_pof_ch09()
