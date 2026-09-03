#!/usr/bin/env python3
"""
Generator for Subject 022: AGK - Instrumentation
Volume 4: Chapters 12 to 14 (GPWS/EGPWS, TCAS II & Autopilot/Autoland)
- Chapter 12: Ground Proximity Warning Systems (GPWS Modes 1-7 & EGPWS/TAWS)
- Chapter 13: Traffic Alert & Collision Avoidance (TCAS II v7.1)
- Chapter 14: Automatic Flight Control Systems (AFCS, Autopilot & Autoland CAT I/II/III)

Fully aligned with CAE Oxford Book 5 (Instrumentation) and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/022_instrumentation"

def build_inst_ch12():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch12_gpws_egpws.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 12: GPWS & EGPWS")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        12,
        "Ground Proximity Warning Systems (GPWS & EGPWS)",
        "439-488"
    )

    pdf.add_heading_1("1. Classic GPWS Operating Modes (Modes 1 to 7)")
    pdf.add_paragraph(
        "Classic GPWS warns of impending Controlled Flight Into Terrain (CFIT). It relies on Radio Altimeter rate of change "
        "and aircraft configuration from 50 ft to 2,500 ft AGL:"
    )

    gpws_table = [
        ["Mode 1: Excessive Sink Rate", "Radio altitude sinking excessively fast.", "'SINK RATE, SINK RATE' (amber); if uncorrected: 'PULL UP' (red light + continuous aural siren)."],
        ["Mode 2: Terrain Closure Rate", "Rapidly rising terrain beneath aircraft.", "'TERRAIN, TERRAIN' (amber); if closure rate exceeds boundary: 'PULL UP, PULL UP' (red)."],
        ["Mode 3: Altitude Loss After Take-Off", "Barometric altitude sink after take-off or go-around before reaching 1,500 ft AGL.", "'DON'T SINK, DON'T SINK' (amber voice alert repeated until positive climb established)."],
        ["Mode 4: Unsafe Terrain Clearance", "Landing gear or flaps NOT in landing position at low radio altitude.", "Mode 4A (Gear up, speed < 190 kt): 'TOO LOW, GEAR'. Mode 4B (Flaps up, speed < 159 kt): 'TOO LOW, FLAPS'. At higher speeds: 'TOO LOW, TERRAIN'."],
        ["Mode 5: Below Glideslope", "Descent more than 1.3 dots below ILS glideslope beam.", "'GLIDESLOPE, GLIDESLOPE' (amber alert; volume increases as glideslope deviation deepens)."],
        ["Mode 6: Bank Angle / Callouts", "Excessive bank angle (> 35° to 45° depending on altitude); plus advisory altitude callouts.", "'BANK ANGLE, BANK ANGLE'; plus synthetic height calls ('ONE THOUSAND', 'FIVE HUNDRED', 'MINIMUMS')."],
        ["Mode 7: Windshear Detection", "Reactive windshear detected via accelerometer and air data comparison.", "Red WINDSHEAR light on PFD + two-tone siren + synthetic voice 'WINDSHEAR, WINDSHEAR, WINDSHEAR'."]
    ]
    pdf.add_table(["GPWS Warning Mode", "Aeronautical Trigger Condition", "Cockpit Visual & Synthetic Aural Warnings"], gpws_table, col_widths=[125.0, 185.0, 190.0])

    pdf.add_heading_1("2. Enhanced GPWS (EGPWS / TAWS): Forward Looking Terrain (FLTA)")
    pdf.add_paragraph(
        "Classic GPWS had a deadly limitation: its radio altimeter looked ONLY straight down, providing zero warning when flying "
        "toward a vertical cliff or rising mountain ridge (CFIT risk):"
    )
    pdf.add_bullet("EGPWS / TAWS Architecture", "Adds a worldwide digital terrain elevation database, obstacle database (towers, bridges), and high-precision GPS aircraft positioning.")
    pdf.add_bullet("Forward Looking Terrain Avoidance (FLTA)", "Projects a virtual look-ahead caution envelope (40 to 60 seconds ahead) and warning envelope (20 to 30 seconds ahead) along the aircraft's projected flight path. Issues alerts BEFORE the aircraft arrives at rising terrain!")
    pdf.add_bullet("Premature Descent Alert (PDA)", "Warns if aircraft descends significantly below the normal 3° descent profile on approach prior to reaching the runway.")
    pdf.add_bullet("ND Terrain Display Colors", "Solid Red: Terrain > 2,000 ft above aircraft; Solid Yellow: Terrain 500 ft below to 2,000 ft above; Green: Terrain 2,000 ft to 500 ft below aircraft altitude.")

    pdf.add_callout(
        "trap",
        "GPWS / EGPWS 'PULL UP' Emergency Flight Maneuver",
        "Upon receiving any RED 'PULL UP' or 'TERRAIN AHEAD PULL UP' warning in IMC or night:\n"
        "- Disconnect Autopilot and Autothrottle immediately!\n"
        "- Apply MAXIMUM TOGA THRUST!\n"
        "- Roll wings level and pitch up smoothly to the PITCH LIMIT INDICATOR (PLI) or stick shaker angle!\n"
        "- DO NOT RETRACT GEAR OR FLAPS until terrain clearance is fully assured!",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch12 = [
        ("Q1: What is the primary operational advantage of an Enhanced GPWS (EGPWS / TAWS) over a conventional classic GPWS?",
         "[A] It measures cabin differential pressure\n[B] It provides Forward Looking Terrain Avoidance (FLTA) using a worldwide terrain database and GPS, detecting rising terrain ahead before flying over it\n[C] It replaces the weather radar\n[D] It operates only in VMC",
         "CORRECT: [B]. Classic GPWS senses terrain directly downward via radio altimeter, creating blind spots against steep cliffs. EGPWS compares GPS position against a digital terrain database to warn 40-60 seconds ahead of impact."),
        ("Q2: Which GPWS mode triggers the cockpit voice warning 'DON'T SINK, DON'T SINK'?",
         "[A] Mode 1: Excessive descent rate\n[B] Mode 2: Rapid terrain closure\n[C] Mode 3: Inadvertent altitude loss after take-off or go-around\n[D] Mode 5: Below glideslope",
         "CORRECT: [C]. Mode 3 monitors barometric altitude loss following take-off or missed approach with gear/flaps not in landing configuration, alerting 'DON'T SINK'."),
        ("Q3: When the flight crew receives an authentic EGPWS 'PULL UP' warning in IMC, why must the landing gear and flaps NOT be immediately retracted?",
         "[A] Gear retraction increases parasitic drag\n[B] Retracting gear/flaps causes a momentary loss of lift (sink) and alters aircraft trim, which could result in ground impact\n[C] Regulations prohibit gear movement\n[D] The warning will cancel",
         "CORRECT: [B]. Standard CFIT escape procedures mandate leaving configuration untouched during initial pull-up to avoid aerodynamic settling or secondary stall while achieving maximum climb angle.")
    ]

    for q_text, opts, exp in questions_ch12:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 12 compiled: {pdf_path}")


def build_inst_ch13():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch13_tcas_ii.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 13: TCAS II (v7.1)")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        13,
        "Traffic Alert & Collision Avoidance (TCAS II v7.1)",
        "489-538"
    )

    pdf.add_heading_1("1. TCAS II Architecture & The Tau (Tau) Principle")
    pdf.add_paragraph(
        "TCAS II operates independently of ground Air Traffic Control radar, interrogating SSR Mode C and Mode S transponders "
        "on 1030 MHz and receiving replies on 1090 MHz within a ~30 to 50 NM surveillance range:"
    )
    pdf.add_bullet("Tau Concept (Time to CPA)", "TCAS does NOT calculate collision risk based purely on physical distance! Instead, it evaluates TAU (Tau): Time to Closest Point of Approach (CPA): Tau = Range / Closure Rate: Tau = r / (-r_dot).")
    pdf.add_bullet("Threat Classification Hierarchy", "1. Non-Threat Traffic: Open white diamond (> 6 NM or > 1,200 ft vertical); 2. Proximity Traffic: Solid white diamond (within 6 NM and 1,200 ft, but non-converging); 3. Traffic Advisory (TA): Solid amber circle; 4. Resolution Advisory (RA): Solid red square.")

    tcas_table = [
        ["Alert Level", "Tau Time Threshold (Cruise)", "Cockpit Visual & Synthetic Aural Warning", "Mandatory Pilot Action"],
        ["Traffic Advisory (TA)", "Tau = 35 to 48 Seconds", "Solid AMBER circle on ND. Synthetic voice: 'TRAFFIC, TRAFFIC'.", "Attempt visual acquisition of conflicting traffic. PREPARE for possible Resolution Advisory. DO NOT MANEUVER solely based on TA!"],
        ["Resolution Advisory (RA)", "Tau = 20 to 35 Seconds", "Solid RED square on ND. Pitch cues on PFD vertical speed tape (green fly-to arc; red avoid arc). Aural: 'CLIMB', 'DESCEND', 'LEVEL OFF'.", "FLY THE RA IMMEDIATELY within 5 SECONDS! TCAS RA commands take strict priority over all ATC clearances!"]
    ]
    pdf.add_table(["Alert Level", "Tau Time Threshold (Cruise)", "Cockpit Visual & Synthetic Aural Warning", "Mandatory Pilot Action"], tcas_table, col_widths=[105.0, 105.0, 160.0, 130.0])

    pdf.add_heading_1("2. TCAS II Version 7.1 Enhancements & Sense Reversals")
    pdf.add_paragraph(
        "Following the fatal 2002 Überlingen mid-air collision, TCAS Version 7.1 introduced vital safety modifications:"
    )
    pdf.add_bullet("'LEVEL OFF' Aural Replaces 'Adjust Vertical Speed'", "In initial RA encounters where traffic levels off, TCAS v7.1 now commands 'LEVEL OFF, LEVEL OFF', instructing pilots to reduce vertical speed to zero fpm smoothly, preventing excessive climb/descent.")
    pdf.add_bullet("Coordinated Sense Reversals", "When two TCAS II aircraft encounter each other, their Mode S transponders negotiate resolution senses automatically: one commands CLIMB while the other commands DESCEND. If one pilot fails to comply (flying opposite to RA), TCAS v7.1 detects the non-compliance and issues an immediate SENSE REVERSAL ('CLIMB, CLIMB NOW!' or 'DESCEND, DESCEND NOW!'). Reaction time for reversal RA: 2.5 SECONDS!")

    pdf.add_callout(
        "trap",
        "ATC vs TCAS RA Absolute Legal Priority",
        "- STRICT EASA / ICAO LAW: A TCAS Resolution Advisory (RA) ALWAYS TAKES PRECEDENCE over conflicting ATC instructions!\n"
        "- If ATC says 'Descend FL 350' but TCAS commands 'CLIMB, CLIMB':\n"
        "- YOU MUST CLIMB! Never follow an ATC clearance that contradicts a TCAS RA!\n"
        "- Notify ATC as soon as workload permits: '[Callsign], TCAS RA'.",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch13 = [
        ("Q1: If an air traffic controller issues a radar descent clearance that directly contradicts a TCAS Resolution Advisory (RA) commanding a climb, what must the pilot do?",
         "[A] Follow the ATC instruction because ATC has radar separation overview\n[B] Follow the TCAS RA immediately, disengaging autopilot if necessary, and advise ATC as soon as practical\n[C] Level off and ask ATC to confirm\n[D] Turn 90 degrees right",
         "CORRECT: [B]. Under international aviation regulations, a TCAS RA takes absolute legal precedence over conflicting ATC clearances. Pilots must immediately respond to the RA within 5 seconds and notify ATC."),
        ("Q2: How does TCAS II calculate the time to Closest Point of Approach (CPA) to trigger a Traffic Advisory or Resolution Advisory?",
         "[A] By measuring barometric pressure difference\n[B] Using the Tau (Tau) formula: Range divided by Closure Rate (r / r_dot)\n[C] By checking the GPS ground distance\n[D] Using the aircraft Mach number",
         "CORRECT: [B]. TCAS II evaluates collision risk using Tau (time to CPA), which is calculated as instantaneous slant range divided by closing velocity. This accounts for high closing speeds in head-on traffic."),
        ("Q3: What critical safety change was implemented in TCAS II Version 7.1 to improve pilot compliance during vertical adjustments?",
         "[A] Added horizontal steering commands\n[B] Replaced 'Adjust Vertical Speed, Adjust' with the clear synthetic voice command 'LEVEL OFF, LEVEL OFF'\n[C] Increased surveillance range to 200 NM\n[D] Inhibited all warnings below 10,000 ft",
         "CORRECT: [B]. TCAS v7.1 replaced the confusing 'Adjust Vertical Speed' command with 'LEVEL OFF, LEVEL OFF' to guide pilots smoothly to zero vertical speed, preventing overshoot into conflicting flight levels.")
    ]

    for q_text, opts, exp in questions_ch13:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 13 compiled: {pdf_path}")


def build_inst_ch14():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch14_afcs_autopilot_flight_director.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 14: AFCS & Autopilot")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        14,
        "Automatic Flight Control & Autoland (CAT I/II/III)",
        "539-600"
    )

    pdf.add_heading_1("1. Automatic Flight Control System (AFCS) Hierarchy")
    pdf.add_paragraph(
        "The AFCS integrates the Autopilot (AP), Flight Director (FD), and Autothrottle / Autothrust (A/T) into an automated flight envelope:"
    )
    pdf.add_bullet("Flight Director (FD)", "Computes steering commands displayed as crosshairs or single-cue command bars on the PFD. Indicates where the pilot MUST steer the aircraft manually to intercept and maintain the selected flight path.")
    pdf.add_bullet("Inner Loop (Stability Augmentation / Fast Loop)", "Damps aerodynamic oscillations and holds attitude. Senses angular rates from rate gyros/accelerometers and deflects control surfaces (e.g. Yaw Damper to eliminate Dutch Roll). Operates with rapid control surface movements.")
    pdf.add_bullet("Outer Loop (Guidance / Slow Loop)", "Tracks navigation paths and targets: Altitude Hold, Heading Select, VOR/LOC, LNAV, VNAV, Glide Path. Displaces control surfaces slowly to guide aircraft along flight trajectory.")
    pdf.add_bullet("Control Wheel Steering (CWS)", "A semi-automatic mode where pilot applies manual force on control yoke; autopilot follows pilot input. When yoke pressure is released, autopilot locks onto and maintains the new attitude!")

    pdf.add_heading_1("2. ICAO / CS-AWO Precision Landing Categories")
    pdf.add_paragraph(
        "All-Weather Operations (CS-AWO) categorize instrument approaches by Decision Height (DH) and Runway Visual Range (RVR):"
    )

    cat_table = [
        ["Approach Category", "Minimum Decision Height (DH)", "Minimum Runway Visual Range (RVR)", "Airborne Autoland System Architecture"],
        ["CAT I", "DH >= 200 ft (60 m)", "RVR >= 550 m (or 800 m vis)", "Standard single autopilot or manual flight with Flight Director."],
        ["CAT II", "100 ft <= DH < 200 ft", "RVR >= 300 m", "Fail-Passive autopilot or dual flight directors. Radio altimeter mandatory."],
        ["CAT IIIa", "DH < 100 ft or NO DH", "RVR >= 175 m", "Fail-Passive or Fail-Operational autoland system with automatic rollout/manual rollout."],
        ["CAT IIIb", "DH < 50 ft or NO DH", "50 m <= RVR < 175 m", "Fail-Operational autoland system with automatic rollout guidance to runway center."],
        ["CAT IIIc", "NO DH (Zero DH)", "NO RVR (Zero RVR)", "Zero-zero landing and taxi guidance. (Not commercially certified due to ground rescue limits)."]
    ]
    pdf.add_table(["Approach Category", "Minimum Decision Height (DH)", "Minimum Runway Visual Range (RVR)", "Airborne Autoland System Architecture"], cat_table, col_widths=[90.0, 130.0, 130.0, 150.0])

    pdf.add_heading_1("3. Fail-Passive vs Fail-Operational Autoland Architecture")
    pdf.add_paragraph(
        "Transport category aircraft require certified multi-channel redundancy for low-visibility autolandings:"
    )
    pdf.add_bullet("Fail-Passive System (Single-Failure Tolerant)", "In the event of an autopilot channel failure below alert height, NO OUT-OF-TRIM condition occurs, but the autopilot DISCONNECTS automatically! The pilot must immediately take manual control and execute a missed approach (go-around) if visual reference is not established. Typical for CAT II and CAT IIIa.")
    pdf.add_bullet("Fail-Operational System (Dual-Failure Tolerant)", "Features at least two independent autopilot channels operating simultaneously (duplex or triplex). If one channel fails below the Alert Height (typically 100-200 ft), the remaining channel continues the approach, flare, touchdown, and rollout AUTOMATICALLY with NO PILOT INTERVENTION! Mandatory for CAT IIIb.")

    pdf.add_callout(
        "trap",
        "Autoland Flare Mode Trigger & Transition",
        "- Below 50 ft AGL: Sensed by the Radio Altimeter!\n"
        "- The autopilot enters FLARE mode: Pitch attitude increases smoothly to reduce sink rate to ~1-2 ft/sec.\n"
        "- Autothrottle automatically retards thrust levers to IDLE (FMA annunciates 'RETARD' at ~30-20 ft).\n"
        "- At touchdown: Rollout mode tracks the ILS localizer centerline via nosewheel steering and rudder.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch14 = [
        ("Q1: In an Automatic Flight Control System (AFCS), what is the difference between an 'inner loop' and an 'outer loop'?",
         "[A] Inner loop controls engines, outer loop controls flaps\n[B] Inner loop provides rate damping and short-term stability augmentation; outer loop provides long-term path guidance (altitude hold, heading, nav tracking)\n[C] Inner loop is manual, outer loop is automatic\n[D] Inner loop operates only on the ground",
         "CORRECT: [B]. The inner loop stabilizes the aircraft about its axes using rate gyros (damping Dutch roll and pitch oscillations). The outer loop guides the aircraft along selected navigation paths (holding altitude or tracking localizer)."),
        ("Q2: What is the defining operational characteristic of a 'Fail-Operational' autoland flight guidance system?",
         "[A] Following an autopilot failure, the aircraft automatically executes a go-around\n[B] Following a single system failure below alert height, the approach, flare, and landing can be completed automatically by the remaining operating channel without pilot intervention\n[C] It requires manual landing flare\n[D] It operates on battery power only",
         "CORRECT: [B]. Fail-operational systems feature multiple redundant channels. If one channel fails below alert height, the remaining channel continues and lands the aircraft automatically with zero interruption."),
        ("Q3: What is the minimum Runway Visual Range (RVR) required for an ICAO Category II (CAT II) precision ILS approach?",
         "[A] 550 m\n[B] 300 m\n[C] 175 m\n[D] 75 m",
         "CORRECT: [B]. CAT II requires a minimum Decision Height between 100 ft and 200 ft, and an RVR of not less than 300 meters.")
    ]

    for q_text, opts, exp in questions_ch14:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 14 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_inst_ch12()
    build_inst_ch13()
    build_inst_ch14()
