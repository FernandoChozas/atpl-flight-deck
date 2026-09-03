#!/usr/bin/env python3
"""
Generator for Subject 022: AGK - Instrumentation
Volume 3: Chapters 09 to 11 (EFIS, FMS & Stall Protection)
- Chapter 09: Electronic Flight Instrument Systems (EFIS: PFD & ND)
- Chapter 10: Flight Management Systems (FMS, CDU & Cost Index)
- Chapter 11: Angle of Attack & Stall Warning/Protection (Stick Shaker/Pusher)

Fully aligned with CAE Oxford Book 5 (Instrumentation) and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/022_instrumentation"

def build_inst_ch09():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch09_electronic_flight_displays_efis.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 9: EFIS (PFD & ND)")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        9,
        "Electronic Flight Instrument Systems (PFD & ND)",
        "299-348"
    )

    pdf.add_heading_1("1. EFIS Architecture: Display Units & Symbol Generators")
    pdf.add_paragraph(
        "Electronic Flight Instrument Systems (EFIS) replace electromechanical gauges with high-resolution digital screens "
        "driven by central graphic processing computers (Display Computers / Symbol Generators - SG):"
    )
    pdf.add_bullet("Screen Types", "Older airliners use Cathode Ray Tubes (CRT). Modern aircraft use Active Matrix Liquid Crystal Displays (AMLCD) providing wider viewing angles, lower power consumption, and daylight readability.")
    pdf.add_bullet("Display Redundancy & Reversion", "Each pilot seat has a Primary Flight Display (PFD) and a Navigation Display (ND). If a PFD screen burns out or fails, an EFIS display transfer switch moves the entire PFD image automatically or manually onto the adjacent ND screen!")

    pdf.add_heading_1("2. Standard EFIS Color Code Philosophy")
    pdf.add_paragraph(
        "EASA CS-25 certification standardizes EFIS color usage across all manufacturers to prevent pilot misinterpretation:"
    )

    color_table = [
        ["RED", "Warnings, immediate flight hazards, flight envelope red line limits (e.g. V_NE, V_MO / M_MO barber pole, stick shaker speed band, TCAS RA red blocks)."],
        ["AMBER / YELLOW", "Cautions, abnormal conditions, armed limit ranges, airspeed caution range (yellow arc), TCAS TA advisory circles."],
        ["GREEN", "Engaged active autopilot/flight director modes on the FMA, active navigation tracking (VOR/ILS course line), normal system status."],
        ["MAGENTA", "Active flight guidance targets! Flight Director steering command bars, active FMS route flight plan, active target altitude, active waypoint name, VNAV descent path."],
        ["CYAN (LIGHT BLUE)", "Armed autopilot modes on the FMA (waiting for capture), pre-selected bug values, secondary flight routes, tuned navigation aids."],
        ["WHITE", "Current active numerical flight data, instrument dials and scales, non-active flight plan waypoints, system baseline borders."]
    ]
    pdf.add_table(["EFIS Color Standard", "Aeronautical Meaning & Cockpit Applications"], color_table, col_widths=[140.0, 360.0])

    pdf.add_heading_1("3. Primary Flight Display (PFD) & Navigation Display (ND) Modes")
    pdf.add_paragraph(
        "The PFD centralizes the classic 'Basic T' instruments on a single screen, topped by the Flight Mode Annunciator (FMA):"
    )
    pdf.add_bullet("Flight Mode Annunciator (FMA)", "Divided into 5 columns across the top of the PFD: 1. Autothrottle status; 2. Vertical mode (engaged green / armed cyan); 3. Lateral mode (engaged green / armed cyan); 4. Approach capability (CAT I, II, III DUAL); 5. Autopilot / Flight Director engagement status. ANY MODE CHANGE is highlighted by a flashing white box for 10 seconds!")
    pdf.add_bullet("Speed Trend Vector", "A vertical magenta or green trend vector arrow on the airspeed tape. The tip indicates what the airspeed will be in exactly 10 SECONDS based on current longitudinal acceleration!")
    pdf.add_bullet("ND Modes", "1. ROSE NAV / VOR / ILS: Full 360° compass rose centered on aircraft; 2. ARC MODE: 90° expanded forward sector, track-up oriented, displays active route, weather radar, TCAS and terrain overlays; 3. PLAN MODE: True North-up, centered on selected route waypoints, used for flight plan verification (aircraft symbol is not shown at center).")

    pdf.add_callout(
        "trap",
        "Navigation Display (ND) Radar Overlay in PLAN Mode",
        "- CRITICAL EXAM RULE: Weather Radar (WXR) returns and Terrain (GPWS) returns CANNOT BE DISPLAYED in PLAN mode!\n"
        "- Reason: PLAN mode is oriented TRUE NORTH UP, whereas the weather radar antenna scans relative to the aircraft heading/track!\n"
        "- Weather radar overlay is available ONLY in ARC mode and ROSE mode.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch09 = [
        ("Q1: Under standard EASA EFIS color coding rules, what color is used on the PFD and ND to represent the active Flight Director command bars and active FMS guidance targets?",
         "[A] Green\n[B] Cyan\n[C] MAGENTA\n[D] Yellow",
         "CORRECT: [C]. Under CS-25 conventions, MAGENTA is strictly reserved for commanded flight director guidance targets, active waypoints, and FMS lateral/vertical profiles. (Green indicates engaged modes or raw data)."),
        ("Q2: What does the 'Speed Trend Vector' on a modern PFD airspeed tape indicate?",
         "[A] The target cruise speed\n[B] The predicted airspeed in exactly 10 SECONDS at the current rate of acceleration or deceleration\n[C] The maximum flap extend speed\n[D] The windspeed component",
         "CORRECT: [B]. The speed trend vector arrow projects aircraft acceleration. The tip of the vector indicates the airspeed that will be reached in 10 seconds if current acceleration remains constant."),
        ("Q3: Why can weather radar (WXR) returns NOT be displayed on the Navigation Display when PLAN mode is selected?",
         "[A] Radar transmitter powers off in PLAN mode\n[B] PLAN mode is oriented True North up, which cannot be synchronized with the heading-referenced radar antenna scan\n[C] Screen resolution is insufficient\n[D] TCAS overrides radar",
         "CORRECT: [B]. The weather radar scans relative to the aircraft's physical nose (heading/track). PLAN mode shows a static map oriented True North up, making radar overlay geometrically incompatible.")
    ]

    for q_text, opts, exp in questions_ch09:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 9 compiled: {pdf_path}")


def build_inst_ch10():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch10_flight_management_system_fms.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 10: FMS & Cost Index")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        10,
        "Flight Management Systems (FMS & Cost Index)",
        "349-398"
    )

    pdf.add_heading_1("1. FMS System Architecture & Dual Databases")
    pdf.add_paragraph(
        "The Flight Management System (FMS) is the brain of modern navigation, integrating lateral routing (LNAV), "
        "vertical profile optimization (VNAV), and performance calculations:"
    )
    pdf.add_bullet("Hardware Layout", "Consists of two redundant Flight Management Computers (FMCs) cross-talking over ARINC 429/AFDX buses, controlled via pilot Multifunction Control Display Units (MCDU) or Touchscreen Control Units.")
    pdf.add_bullet("Navigation Database (NDB)", "A certified, READ-ONLY database updated internationally every 28 DAYS according to the ICAO AIRAC cycle. Contains worldwide airports, runways, waypoints, airways, radio aids, SIDs, STARs, and published instrument approaches. The flight crew CANNOT overwrite or alter stored airway points.")
    pdf.add_bullet("Performance Database (PDB)", "Contains manufacturer aerodynamic drag polars, engine fuel burn curves, weight limits, and flight envelope speeds for the specific airframe/engine type.")

    pdf.add_heading_1("2. Cost Index (CI) & Speed Optimization")
    pdf.add_paragraph(
        "The FMS computes the most economical cruising speed and climb/descent profiles based on airline Cost Index (CI):"
    )
    pdf.add_bullet("Cost Index Formula", "Cost Index = Cost of Time ($ per hour) / Cost of Fuel (cents per pound or kg). CI balances flight crew/maintenance hourly operational costs against fuel expenses.")
    pdf.add_bullet("Cost Index = 0", "Represents ZERO cost of time! The FMS commands MAXIMUM RANGE CRUISE (MRC) speed: burns minimum possible fuel per nautical mile, resulting in the slowest cruise speed and longest flight duration.")
    pdf.add_bullet("Cost Index = 999 (Maximum CI)", "Time cost is infinitely more important than fuel! The FMS commands the maximum authorized cruising speed (V_MO / M_MO), minimizing flight time regardless of high fuel consumption.")
    pdf.add_bullet("Long Range Cruise (LRC)", "A speed schedule flown at 99% of Maximum Range Cruise efficiency, providing ~3% to 5% higher speed for only 1% extra fuel burn.")

    cost_table = [
        ["Cost Index Value", "Aeronautical Optimization Objective", "Flight Performance Result"],
        ["CI = 0 (Minimum Fuel)", "Minimum fuel consumption per nautical mile (Zero time cost).", "Maximum Range Cruise (MRC). Lowest cruise speed; maximum flight time; greatest fuel economy."],
        ["Intermediate CI (Typical 20-80)", "Standard airline operating balance between schedule and fuel burn.", "Econ climb, Econ cruise, and Econ descent speeds calculated dynamically."],
        ["Maximum CI (e.g. 999)", "Minimum flight duration (Time is critical, fuel cost ignored).", "Flies at maximum certified speed (V_MO / M_MO). Highest fuel burn; shortest flight time."]
    ]
    pdf.add_table(["Cost Index Value", "Aeronautical Optimization Objective", "Flight Performance Result"], cost_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_callout(
        "trap",
        "Cost Index Effect on Speeds and Profiles Summary",
        "- INCREASING Cost Index: Increases Climb Speed, Cruise Speed/Mach, and Descent Speed; steepens descent path; shortens flight time!\n"
        "- DECREASING Cost Index: Decreases Climb/Cruise/Descent speeds; flattens descent path; saves fuel!\n"
        "- CI = 0 ALWAYS corresponds to MAXIMUM RANGE (Minimum Fuel)!",
        max_chars=86
    )

    pdf.add_heading_1("3. Required Navigation Performance (RNP) vs Actual (ANP)")
    pdf.add_paragraph(
        "Modern RNAV routes are certified under Performance-Based Navigation (PBN) standards:"
    )
    pdf.add_bullet("Required Navigation Performance (RNP)", "The lateral accuracy containment standard in nautical miles that the aircraft must maintain for at least 95% of total flight time (e.g. RNP 4 for oceanic, RNP 1 for terminal SIDs/STARs, RNP 0.3 for RNAV/RNP final approaches).")
    pdf.add_bullet("Actual Navigation Performance (ANP / EPE)", "The current real-time estimated navigation error computed by the FMS from multi-sensor blending (GPS + DME/DME + IRS). If ANP exceeds RNP: ANP > RNP, an 'UNABLE RNP' caution illuminates on the PFD/ND, requiring an immediate missed approach or ATC notification!")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch10 = [
        ("Q1: What is the operational effect of entering a Cost Index (CI) of ZERO into the Flight Management Computer?",
         "[A] The FMC commands maximum certified airspeed\n[B] The FMC commands Maximum Range Cruise (MRC) speed, resulting in minimum fuel burn per nautical mile\n[C] The autopilot disconnects\n[D] The FMS switches to manual navigation",
         "CORRECT: [B]. When CI = 0, time cost is treated as zero. The computer optimizes purely for fuel economy, flying at Maximum Range Cruise (MRC) speed."),
        ("Q2: How often is the worldwide aeronautical Navigation Database (NDB) within an aircraft FMS updated?",
         "[A] Every 7 days\n[B] Every 28 DAYS in accordance with the international ICAO AIRAC cycle\n[C] Annually on January 1st\n[D] Whenever the aircraft undergoes a C-check",
         "CORRECT: [B]. International aeronautical navigation data is published and synchronized on a strict 28-day cycle known as the AIRAC (Aeronautical Information Regulation And Control) cycle."),
        ("Q3: What occurs if the Actual Navigation Performance (ANP) computed by the FMS becomes LARGER than the Required Navigation Performance (RNP) on an RNP approach?",
         "[A] The autopilot increases speed\n[B] An 'UNABLE RNP' alert is annunciated and the flight crew must execute a missed approach or notify ATC\n[C] The FMC switches automatically to VOR tracking\n[D] Fuel is dumped",
         "CORRECT: [B]. When ANP exceeds RNP, the aircraft can no longer guarantee the required obstacle clearance boundary. Flight crew procedures mandate executing an immediate go-around.")
    ]

    for q_text, opts, exp in questions_ch10:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 10 compiled: {pdf_path}")


def build_inst_ch11():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch11_aerodynamic_stall_warning.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 11: Stall Warning & AOA")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        11,
        "Stall Warning & Angle of Attack Systems",
        "399-438"
    )

    pdf.add_heading_1("1. Angle of Attack (AOA) Aerodynamics & Sensor Types")
    pdf.add_paragraph(
        "An airfoil stalls when airflow separates from the upper surface at the Critical Angle of Attack (Alpha_crit, typically 14° to 18°). "
        "An aircraft stalls at the EXACT SAME CRITICAL AOA regardless of weight, airspeed, bank angle, or altitude:"
    )
    pdf.add_bullet("Pivoting Aerodynamic Vanes", "Mounted on the left and right forward fuselage. A counterweighted, aerodynamically balanced wedge vane rotates freely to align with the local oncoming relative airflow. Electrically heated to prevent ice accumulation.")
    pdf.add_bullet("Conical / Slotted Probes (Rosemount)", "A fixed cylindrical/conical probe projecting into the airstream with two longitudinal slots. Differential pressure between the two slots is measured by a internal transducer, providing AOA measurement with no external moving parts.")

    pdf.add_heading_1("2. Stall Warning & Prevention Devices: Stick Shaker vs Stick Pusher")
    pdf.add_paragraph(
        "CS-25 transport certification requires clear, unmistakable aerodynamic warning prior to stall entry:"
    )

    stall_table = [
        ["System Component", "Physical Mechanism & Trigger Point", "Certification Rule & Aircraft Protection"],
        ["Aerodynamic Buffet", "Natural turbulent wake from stalled wing root buffeting horizontal stabilizer.", "Light aircraft and low-wing jets. Some swept-wing jets lack natural pre-stall buffet, requiring artificial warning devices!"],
        ["Stick Shaker (Artificial Warning)", "Eccentric unbalanced electric motors mounted on the control columns vibrate the yoke vigorously at ~15 to 30 Hz with a loud clattering noise.", "MANDATORY CS-25 requirement: Must activate at least 5 KNOTS OR 5% ABOVE the stall speed (V_S) to allow pilot recovery before the actual aerodynamic stall."],
        ["Stick Pusher (Artificial Prevention)", "Pneumatic or hydraulic actuator ram connected to the elevator control linkage. Pushes the yoke violently FORWARD with 30 to 40 kg (60-80 lb) of force!", "MANDATORY on T-tail swept-wing aircraft (e.g. CRJ, bizjets) susceptible to DEEP STALL (Super-Stall) where stalled wing wake blankets the T-tail elevator, making recovery aerodynamic impossible! Pushes nose down before critical AOA."]
    ]
    pdf.add_table(["System Component", "Physical Mechanism & Trigger Point", "Certification Rule & Aircraft Protection"], stall_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_callout(
        "trap",
        "Deep Stall (Super-Stall) & Stick Pusher Role",
        "- Deep Stall Risk: Swept-wing aircraft with T-tail empennage and rear-fuselage engines.\n"
        "- Phenomenon: At high angles of attack, wingtip stall causes center of lift to shift forward, pitching the nose UP further! The turbulent separated wake of the stalled wing blankets the high T-tail elevator, completely neutralizing pitch control!\n"
        "- Solution: The STICK PUSHER detects rapid approach to critical AOA and forcibly drives the elevator DOWN before deep stall can ever be entered!",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch11 = [
        ("Q1: Under EASA CS-25 certification requirements, at what speed margin must the artificial stall warning (stick shaker) activate?",
         "[A] Exactly at the aerodynamic stall speed\n[B] At least 5 KNOTS or 5% ABOVE the stall speed (V_S)\n[C] 20 knots above stall speed\n[D] Only when the landing gear is retracted",
         "CORRECT: [B]. CS-25 mandates that clear artificial or natural stall warning must begin at least 5 knots or 5% above the stall speed, providing sufficient reaction time for flight crew recovery."),
        ("Q2: Why are T-tail jet transport aircraft equipped with a mandatory STICK PUSHER system?",
         "[A] To help the pilot trim the aircraft during take-off\n[B] To prevent the aircraft from entering a catastrophic DEEP STALL, where the stalled wing wake blankets the T-tail, rendering elevators aerodynamically ineffective\n[C] To retract the flaps automatically\n[D] To prevent overspeed",
         "CORRECT: [B]. In T-tail aircraft, wing wake washes over the elevated horizontal stabilizer at high angles of attack, causing complete loss of elevator pitch-down authority (deep stall). A stick pusher forcibly lowers the nose before this occurs."),
        ("Q3: Does an aircraft's critical stalling Angle of Attack change with increases in aircraft gross mass?",
         "[A] Yes, critical AOA increases with mass\n[B] No, the critical stalling Angle of Attack remains CONSTANT regardless of aircraft mass, bank angle, or altitude\n[C] Yes, critical AOA decreases with mass\n[D] It changes only with flap extension",
         "CORRECT: [B]. An airfoil stalls when the critical angle of attack is reached (airflow separation). While the stall SPEED increases with mass and load factor, the critical stalling ANGLE OF ATTACK is aerodynamically constant.")
    ]

    for q_text, opts, exp in questions_ch11:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 11 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_inst_ch09()
    build_inst_ch10()
    build_inst_ch11()
