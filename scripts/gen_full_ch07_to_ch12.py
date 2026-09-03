#!/usr/bin/env python3
"""
Full-Depth Study Manual Generator - Volume 2 (Chapters 7 to 12).
Designed for 100% self-contained study.
Target: ~18 to 20 pages total across Chapters 7 to 12.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

# ==============================================================================
# CHAPTER 7: APPROACH PROCEDURES & ILS MINIMA (~5 pages)
# ==============================================================================
def build_ch07():
    pdf_path = os.path.join(BASE_DIR, "010_ch07_approach_procedures.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 7: Approach Procedures (PANS-OPS)")
    pdf.add_title_banner("Air Law", 7, "Approach Procedures & ILS Minima", "173-206")

    pdf.add_heading_1("1. The Five Approach Segments")
    pdf.add_paragraph(
        "Under ICAO Doc 8168 (PANS-OPS), an instrument approach procedure is divided into up to five distinct segments. "
        "Each segment begins and ends at designated fixes, with specific obstacle clearance margins (MOC):",
        max_chars=92
    )

    seg_data = [
        ["1. Arrival Segment", "En-route airway to Initial Approach Fix (IAF)", "Transitions aircraft from en-route ATS route to the terminal area. Often defined by a Standard Terminal Arrival (STAR). MOC conforms to en-route criteria."],
        ["2. Initial Segment", "IAF to Intermediate Fix (IF)", "Provides initial descent and maneuvering to align with the intermediate approach. MOC is at least 300 m (984 ft) in the primary area. Reversal or racetrack procedures occur in this segment."],
        ["3. Intermediate Segment", "IF to Final Approach Fix (FAF / FAP)", "The segment where aircraft configuration and speed are adjusted for final approach. Optimum descent gradient is FLAT (max gradient 5.2% / 3.0°). MOC tapers from 300 m down to 150 m (492 ft)."],
        ["4. Final Approach Segment", "FAF / FAP to Runway Threshold or MAPt", "Precision Approach: Guided by ILS/MLS glidepath to Decision Altitude/Height (DA/H).\nNon-Precision: Guided by VOR/NDB/LOC to Minimum Descent Altitude/Height (MDA/H)."],
        ["5. Missed Approach Segment", "MAPt or DA/H to holding fix or en-route", "Executed if visual reference is not established. Divided into 3 PHASES: Initial (no turn permitted), Intermediate (climb at 2.5% gradient, MOC 30 m), and Final (climb to safe level, MOC 50 m)."]
    ]
    pdf.add_table(["Approach Segment", "Fix Boundaries", "Operational Purpose & Minimum Obstacle Clearance (MOC)"], seg_data, col_widths=[110.0, 130.0, 270.0])

    pdf.add_heading_1("2. Aircraft Approach Categories (A, B, C, D, E)")
    pdf.add_paragraph(
        "Aircraft categories are determined by Vat, which is the indicated airspeed at the runway threshold. "
        "Vat equals the stall speed in landing configuration (Vso) multiplied by 1.3, or 1.23 x Vs1g, at maximum certified landing mass:",
        max_chars=92
    )

    cat_data = [
        ["Category A", "Less than 91 kt", "Light singles and twins (Cessna 172, Piper PA-28, DA-42)"],
        ["Category B", "91 kt to 120 kt", "Heavy twins, regional turboprops (King Air, ATR-42, ATR-72, Dash-8)"],
        ["Category C", "121 kt to 140 kt", "Medium commercial airliners (Airbus A320, Boeing 737, Embraer 190)"],
        ["Category D", "141 kt to 165 kt", "Heavy wide-body airliners (Boeing 777, 747, 787, Airbus A330, A350)"],
        ["Category E", "166 kt to 210 kt", "Special high-performance military and experimental aircraft"]
    ]
    pdf.add_table(["Category", "Vat Threshold Speed Range", "Representative Aircraft Models"], cat_data, col_widths=[85.0, 160.0, 265.0])

    pdf.add_heading_1("3. Reversal & Racetrack Maneuvers")
    pdf.add_bullet("45°/180° Procedure Turn", "Fly outbound on reversal track, turn 45° off track, fly for 1 MINUTE (Categories A and B) or 1 MIN 15 SEC (Categories C, D, and E), then execute a 180° turn in the opposite direction to intercept inbound track.")
    pdf.add_bullet("80°/260° Procedure Turn", "Fly outbound on reversal track, turn 80° off track, immediately followed by a 260° turn in the opposite direction to intercept the inbound track.")
    pdf.add_bullet("Base Turn", "Aircraft flies outbound on a specified radial or dead reckoning track, then executes a turn to intercept the final approach track.")
    pdf.add_bullet("Racetrack Procedure", "Aircraft flies outbound parallel to inbound track for a specified time (1 to 3 minutes), then makes a turn to intercept the inbound track.")

    pdf.add_heading_1("4. Exhaustive ILS Precision Approach Minima (Cat I to Cat IIIC)")
    pdf.add_paragraph(
        "Precision approaches provide continuous electronic glidepath and azimuth guidance. Official EASA minima:",
        max_chars=92
    )

    ils_data = [
        ["Category I (Cat I)", "Not lower than 200 ft (60 m)", "Not less than 550 m RVR (or 800 m visibility without RVR)"],
        ["Category II (Cat II)", "Lower than 200 ft but not lower than 100 ft (30 m)", "Not less than 300 m RVR"],
        ["Category IIIA (Cat IIIA)", "Lower than 100 ft or NO Decision Height", "Not less than 175 m RVR"],
        ["Category IIIB (Cat IIIB)", "Lower than 50 ft or NO Decision Height", "Less than 175 m but not less than 50 m RVR"],
        ["Category IIIC (Cat IIIC)", "NO Decision Height", "NO Runway Visual Range limitations (Zero-Zero)"]
    ]
    pdf.add_table(["ILS Category", "Decision Height (DH)", "Minimum Runway Visual Range (RVR)"], ils_data, col_widths=[125.0, 210.0, 175.0])

    pdf.add_callout(
        "trap",
        "DA/H vs MDA/H and the Missed Approach Initiation",
        "• Decision Altitude/Height (DA/H): Used in PRECISION approaches. If visual reference is not established upon "
        "reaching DA/H, an IMMEDIATE MISSED APPROACH must be initiated. The aircraft may dip slightly below DA/H during the go-around.\n"
        "• Minimum Descent Altitude/Height (MDA/H): Used in NON-PRECISION approaches. The aircraft MUST NEVER descend below "
        "MDA/H without visual reference. Level flight at MDA is permitted until reaching the Missed Approach Point (MAPt).",
        max_chars=86
    )

    pdf.add_heading_1("5. Continuous Descent Final Approach (CDFA)")
    pdf.add_paragraph(
        "CDFA is a technique for flying the final approach segment of a non-precision instrument approach procedure as a "
        "continuous descent, without level-offs, from an altitude/height at or above the FAF to a point approximately "
        "15 m (50 ft) above the landing runway threshold or to the point where the missed approach is initiated. "
        "Under EASA Air Operations (Part-CAT), CDFA is mandatory for non-precision approaches unless approved otherwise.",
        max_chars=92
    )

    pdf.add_heading_1("6. AviationExam Real Exam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: What is the minimum Runway Visual Range (RVR) for an ILS Category I approach?",
         "[A] 300 m\n[B] 550 m\n[C] 800 m\n[D] 175 m",
         "CORRECT: [B]. Under EASA CS-AWO and Part-CAT, the standard minimum RVR for an ILS Category I precision approach is 550 m (or 800 m flight visibility if no RVR system is available)."),
        ("Q2: In a precision approach, what must be done if visual reference is not established at the Decision Altitude/Height (DA/H)?",
         "[A] Level off and fly to the MAPt before executing go-around.\n[B] Initiate an immediate missed approach.\n[C] Descend an additional 50 ft to search for approach lights.\n[D] Revert to localizer-only non-precision minimums.",
         "CORRECT: [B]. At DA/H on a precision approach, an immediate go-around must be initiated without delay if visual reference is not established. Level flight at DA/H is strictly prohibited."),
        ("Q3: What Vat speed range corresponds to Aircraft Category C?",
         "[A] Less than 91 kt\n[B] 91 kt to 120 kt\n[C] 121 kt to 140 kt\n[D] 141 kt to 165 kt",
         "CORRECT: [C]. Category C Vat is 121 to 140 kt (representative of Airbus A320 and Boeing 737 at maximum landing mass)."),
        ("Q4: What is the Minimum Obstacle Clearance (MOC) provided in the intermediate approach segment?",
         "[A] 300 m (984 ft)\n[B] 150 m (492 ft)\n[C] 90 m (295 ft)\n[D] 50 m (164 ft)",
         "CORRECT: [B]. In the intermediate segment, MOC is 150 m in the primary area, reducing from the 300 m MOC of the initial approach segment."),
        ("Q5: During a 45°/180° procedure turn for a Category C aeroplane, how long must the outbound leg be flown after turning 45°?",
         "[A] 1 minute\n[B] 1 minute 15 seconds\n[C] 1 minute 30 seconds\n[D] 2 minutes",
         "CORRECT: [B]. PANS-OPS specifies 1 min for Categories A and B, and 1 min 15 sec for Categories C, D, and E."),
        ("Q6: What is the standard design climb gradient for the intermediate and final phases of a missed approach?",
         "[A] 2.0%\n[B] 2.5%\n[C] 3.3%\n[D] 5.0%",
         "CORRECT: [B]. Standard missed approach design climb gradient under PANS-OPS is 2.5%."),
        ("Q7: Under Category II ILS operations, what is the allowable Decision Height range?",
         "[A] 200 ft to 150 ft\n[B] Lower than 200 ft but not lower than 100 ft\n[C] Lower than 100 ft but not lower than 50 ft\n[D] No Decision Height",
         "CORRECT: [B]. Category II Decision Height is between 100 ft and 200 ft (RVR not less than 300 m).")
    ]
    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 7 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 8: CIRCLING APPROACH (~3 pages)
# ==============================================================================
def build_ch08():
    pdf_path = os.path.join(BASE_DIR, "010_ch08_circling_approach.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 8: Circling Approach Procedures")
    pdf.add_title_banner("Air Law", 8, "Circling Approach Procedures", "207-214")

    pdf.add_heading_1("1. Definition & Operational Criteria")
    pdf.add_paragraph(
        "A circling approach is the visual phase of an instrument approach to bring an aircraft into position for "
        "landing on a runway which is not suitably located for a straight-in approach. A straight-in approach is "
        "considered unacceptable if the final approach track alignment differs from the runway centerline by MORE THAN 30°, "
        "or if the final descent gradient exceeds standard criteria (6.5% for Cat A/B, 6.1% for Cat C/D).",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "Visual Reference Requirement in Circling",
        "Visual reference to the runway environment (threshold, runway markings, or lights) must be MAINTAINED "
        "CONTINUOUSLY throughout the circling maneuver. The aircraft must remain at or above the circling MDA/H "
        "until positioned to make a normal landing on the intended runway.",
        max_chars=86
    )

    pdf.add_heading_1("2. Circling Area Radii & Obstacle Clearance (MOC)")
    pdf.add_paragraph(
        "The circling area is constructed by drawing arcs from the threshold of each usable runway. "
        "The radius of the arc depends on the aircraft category speed (bank angle 20° or rate 3°/s):",
        max_chars=92
    )

    circling_data = [
        ["Cat A", "100 kt", "1.68 NM (3.11 km)", "90 m (295 ft)"],
        ["Cat B", "135 kt", "2.66 NM (4.93 km)", "90 m (295 ft)"],
        ["Cat C", "180 kt", "4.20 NM (7.78 km)", "120 m (394 ft)"],
        ["Cat D", "205 kt", "5.28 NM (9.78 km)", "120 m (394 ft)"],
        ["Cat E", "240 kt", "6.94 NM (12.85 km)", "150 m (492 ft)"]
    ]
    pdf.add_table(["Category", "Max Circling Speed", "Circling Radius from Thresholds", "Minimum Obstacle Clearance (MOC)"], circling_data, col_widths=[75.0, 115.0, 155.0, 165.0])

    pdf.add_heading_1("3. Descent Below Circling MDA/H & Missed Approach")
    pdf.add_paragraph(
        "Descent below circling MDA/H is permitted ONLY when:\n"
        "1. Required visual reference to the runway environment is established and maintained;\n"
        "2. The runway threshold is in sight to the pilot;\n"
        "3. The aircraft is in a position from which a normal descent to landing can be made on the runway using normal maneuvers.",
        max_chars=92
    )

    pdf.add_callout(
        "trap",
        "Loss of Visual Reference While Circling (Guaranteed Exam Question)",
        "If visual reference is lost at any time while circling to land:\n"
        "1. The pilot must initiate an IMMEDIATE CLIMBING TURN TOWARDS THE LANDING RUNWAY.\n"
        "2. Establish the aircraft overhead the aerodrome to ensure terrain clearance.\n"
        "3. Join and follow the published missed approach procedure for the INSTRUMENT RUNWAY initially used.",
        max_chars=86
    )

    pdf.add_heading_1("4. Prohibited Circling Sectors & Terrain Buffers")
    pdf.add_paragraph(
        "Where prominent obstacles or terrain exist in a specific sector around an aerodrome, visual maneuvering "
        "may be prohibited in that sector (e.g. 'Circling prohibited North of RWY 09/27').\n"
        "• The pilot must strictly contain all circling flight within the permitted visual sector.\n"
        "• If cleared to circle, turning into a prohibited sector constitutes an immediate breach of ATC clearance and terrain clearance.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: When is an instrument approach classified as a circling approach?",
         "[A] Whenever the wind on landing runway exceeds 15 kt.\n[B] When final approach track alignment differs by more than 30° from runway centerline.\n[C] Whenever the pilot requests a visual traffic circuit.\n[D] Only when the cloud base is below 1,000 ft.",
         "CORRECT: [B]. Under PANS-OPS, if final approach track differs by > 30° from runway centerline, only circling minima are authorized."),
        ("Q2: What is the circling area radius for a Category C aircraft?",
         "[A] 1.68 NM\n[B] 2.66 NM\n[C] 4.20 NM\n[D] 5.28 NM",
         "CORRECT: [C]. Cat C circling radius is 4.20 NM from runway thresholds (based on 180 kt max speed)."),
        ("Q3: What is the Minimum Obstacle Clearance (MOC) provided in a Category C circling area?",
         "[A] 90 m (295 ft)\n[B] 120 m (394 ft)\n[C] 150 m (492 ft)\n[D] 300 m (984 ft)",
         "CORRECT: [B]. Cat A and B have 90 m MOC; Cat C and D have 120 m MOC; Cat E has 150 m MOC."),
        ("Q4: If visual reference is lost while circling to land on runway 27 after an instrument approach on runway 09, what must the pilot do?",
         "[A] Turn immediately towards runway 09 and descend.\n[B] Make an immediate climbing turn towards runway 27 and join the missed approach for runway 09.\n[C] Continue visually on downwind and attempt landing.\n[D] Climb straight ahead on present heading to MSA.",
         "CORRECT: [B]. The pilot must make an immediate climbing turn towards the landing runway (rwy 27) and establish overhead before following the missed approach for runway 09."),
        ("Q5: May a pilot descend below the circling MDA/H while still on the downwind leg?",
         "[A] Yes, if the runway lights are visible\n[B] NO, the aircraft must remain at or above circling MDA/H until aligned and in a normal descent position\n[C] Yes, if cleared by ATC\n[D] Only in daylight VMC",
         "CORRECT: [B]. Descent below circling MDA/H is prohibited until the aircraft is in a position from which a normal descent to landing can be executed.")
    ]
    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 8 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 9: HOLDING PROCEDURES (~4 pages)
# ==============================================================================
def build_ch09():
    pdf_path = os.path.join(BASE_DIR, "010_ch09_holding_procedures.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 9: Holding Procedures (PANS-OPS)")
    pdf.add_title_banner("Air Law", 9, "Holding Procedures & Standards", "215-226")

    pdf.add_heading_1("1. Holding Pattern Geometry & Standards")
    pdf.add_bullet("Standard Pattern", "Racetrack pattern using RIGHT-HAND turns (non-standard pattern uses left-hand turns).")
    pdf.add_bullet("Rate of Turn", "3° per second (Rate 1 turn) or 25° bank angle, whichever requires less bank.")
    pdf.add_bullet("Outbound Timing", "1 MINUTE at or below 14,000 ft (4,250 m). 1.5 MINUTES above 14,000 ft.")
    pdf.add_bullet("Timing Point", "Outbound timing begins over or abeam the holding fix, whichever occurs later (or on wings level if abeam point cannot be identified).")

    pdf.add_heading_1("2. Maximum Holding Speeds (PANS-OPS / EASA)")
    speeds_data = [
        ["Up to 14,000 ft", "230 kt (Cat A & B: 170 kt)", "280 kt (or 0.8 Mach whichever is less)"],
        ["Above 14,000 ft up to 20,000 ft", "240 kt", "280 kt (or 0.8 Mach whichever is less)"],
        ["Above 20,000 ft up to 34,000 ft", "265 kt", "280 kt (or 0.8 Mach whichever is less)"],
        ["Above 34,000 ft", "0.83 Mach", "0.83 Mach"]
    ]
    pdf.add_table(["Altitude Band", "Normal Maximum Holding Speed", "Turbulence Conditions"], speeds_data, col_widths=[150.0, 175.0, 185.0])

    pdf.add_heading_1("3. The Three Entry Sectors (with 5° Buffer)")
    pdf.add_paragraph(
        "Entry is determined by the aircraft heading relative to the 3 entry sectors with a 5° flexibility buffer:",
        max_chars=92
    )
    pdf.add_bullet("Sector 1 (Parallel Entry - 110° sector)", "Fly to fix, turn to parallel outbound track on reciprocal heading, fly for 1 (or 1.5) min, turn left towards holding side to intercept inbound track.")
    pdf.add_bullet("Sector 2 (Offset / Teardrop Entry - 70° sector)", "Fly to fix, turn to a heading 30° to the holding side, fly for 1 (or 1.5) min, turn right to intercept inbound track.")
    pdf.add_bullet("Sector 3 (Direct Entry - 180° sector)", "Fly to fix, turn directly right to follow the holding pattern.")

    pdf.add_heading_1("4. Holding in Mountainous Terrain & Wind Drift")
    pdf.add_callout(
        "trap",
        "Triple Drift Rule & Mountainous MOC",
        "1. Triple Drift Rule: On the outbound leg, apply THREE TIMES (3x) the inbound drift angle in the opposite direction.\n"
        "2. Mountainous Terrain MOC: Standard MOC in the primary holding area is 300 m (984 ft / 1,000 ft). In designated "
        "mountainous areas, the Minimum Obstacle Clearance is doubled to at least 600 m (2,000 ft).",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch09 = [
        ("Q1: What is the maximum holding speed under PANS-OPS up to 14,000 ft in normal conditions?",
         "[A] 210 kt\n[B] 230 kt\n[C] 240 kt\n[D] 250 kt",
         "CORRECT: [B]. Under PANS-OPS, normal max holding speed up to 14,000 ft is 230 kt (170 kt for Cat A/B)."),
        ("Q2: When does outbound timing begin in a holding pattern if the abeam position cannot be determined?",
         "[A] Passing 90° to the holding track.\n[B] Immediately upon wings level on outbound heading.\n[C] 30 seconds after initiating the turn.\n[D] When crossing the holding radial on DME.",
         "CORRECT: [B]. Outbound timing begins over or abeam the fix, or upon wings level if the abeam position cannot be identified."),
        ("Q3: What angular size corresponds to Sector 2 (Offset / Teardrop entry)?",
         "[A] 70°\n[B] 110°\n[C] 180°\n[D] 90°",
         "CORRECT: [A]. Sector 1 (Parallel) is 110°; Sector 2 (Offset) is 70°; Sector 3 (Direct) is 180°."),
        ("Q4: If an aircraft applies 4° left drift correction on the inbound leg, what drift correction should be applied on the outbound leg?",
         "[A] 4° right\n[B] 8° right\n[C] 12° right\n[D] 16° right",
         "CORRECT: [C]. Under the triple drift rule, outbound drift is 3 x inbound drift = 3 x 4° = 12° in the opposite direction (right)."),
        ("Q5: What is the maximum holding speed above 14,000 ft up to 20,000 ft under PANS-OPS in turbulence?",
         "[A] 240 kt\n[B] 280 kt (or 0.8 Mach whichever is less)\n[C] 300 kt\n[D] 265 kt",
         "CORRECT: [B]. In turbulence, maximum holding speed is 280 kt or 0.8 Mach (whichever is less) up to FL 340."),
        ("Q6: What is the width of the buffer area extending beyond the boundary of the primary holding area under PANS-OPS?",
         "[A] 2.5 NM\n[B] 5.0 NM\n[C] 8.0 NM\n[D] 10.0 NM",
         "CORRECT: [B]. The buffer area extends 5.0 NM beyond the primary holding area boundary; obstacle clearance tapers to zero at the outer edge."),
        ("Q7: What is the maximum holding speed under PANS-OPS above 34,000 ft in all flight conditions?",
         "[A] 265 kt\n[B] 280 kt\n[C] 0.83 Mach\n[D] 0.88 Mach",
         "CORRECT: [C]. Under PANS-OPS, the maximum holding speed above FL 340 is 0.83 Mach.")
    ]
    for q_text, opts, exp in questions_ch09:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 9 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 10: ALTIMETER SETTING PROCEDURES (~3 pages)
# ==============================================================================
def build_ch10():
    pdf_path = os.path.join(BASE_DIR, "010_ch10_altimeter_setting.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 10: Altimeter Setting Procedures")
    pdf.add_title_banner("Air Law", 10, "Altimeter Setting & Temperature Error", "227-238")

    pdf.add_heading_1("1. Pressure Settings: QNH, QFE, Standard")
    pdf.add_bullet("QNH (Altimeter setting)", "Station pressure reduced to MSL according to ISA. Indicates ALTITUDE above MSL. On the ground at the aerodrome, it indicates aerodrome elevation.")
    pdf.add_bullet("QFE", "Atmospheric pressure at aerodrome elevation (or runway threshold). Indicates HEIGHT above aerodrome datum. On the ground, it reads ZERO.")
    pdf.add_bullet("Standard Setting (1013.25 hPa / 29.92 inHg)", "Used for vertical separation en-route. Indicates FLIGHT LEVEL (FL).")

    pdf.add_heading_1("2. Transition Altitude, Level & Layer")
    trans_data = [
        ["Transition Altitude (TA)", "Published on instrument charts (Fixed)", "Altitude at or below which vertical position is controlled by reference to ALTITUDES (QNH)."],
        ["Transition Level (TRL)", "Calculated and issued by ATC (Variable)", "Lowest available FLIGHT LEVEL above the TA. Controlled by reference to Standard (1013.25). Varies with actual QNH."],
        ["Transition Layer", "Airspace between TA and TRL", "Airspace between TA and TRL (at least 1,000 ft thick). LEVEL CRUISING FLIGHT IN THIS LAYER IS STRICTLY PROHIBITED."]
    ]
    pdf.add_table(["Element", "Authority / Publication", "Operational Rule & Altimeter Reference"], trans_data, col_widths=[125.0, 145.0, 240.0])

    pdf.add_callout(
        "trap",
        "Altimeter Changeover Point",
        "• In CLIMB: Altimeter is changed from QNH to STANDARD (1013.25 hPa) when PASSING THE TRANSITION ALTITUDE (TA).\n"
        "• In DESCENT: Altimeter is changed from STANDARD (1013.25) to QNH when PASSING THE TRANSITION LEVEL (TRL).",
        max_chars=86
    )

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_paragraph(
        "Pressure altimeters are calibrated to the International Standard Atmosphere (ISA). In temperatures colder than "
        "ISA, the true altitude is LOWER than the indicated altitude ('High to low or hot to cold, look out below!'):",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Altimeter Temperature Error and Terrain Clearance Correction",
        "SCENARIO (PANS-OPS / EASA Cold Weather Altimetry Correction):\n"
        "• Aerodrome elevation: 2,000 ft. Published Minimum Safe Altitude (MSA): 6,000 ft.\n"
        "• Reported ambient temperature at aerodrome: -15°C.\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate Standard ISA Temperature at Aerodrome Elevation (2,000 ft):\n"
        "  - ISA Temp = 15°C - (2°C x 2) = +11°C.\n"
        "Step 2: Calculate ISA Deviation (Delta-ISA):\n"
        "  - Delta-ISA = Actual (-15°C) - Standard (+11°C) = -26°C (Colder than ISA!).\n"
        "Step 3: Calculate Height Above Altimeter Source (Datum):\n"
        "  - Height = 6,000 ft (MSA) - 2,000 ft (Elevation) = 4,000 ft (4 units of 1,000 ft).\n"
        "Step 4: Apply the 4 ft per 1,000 ft Rule of Thumb:\n"
        "  - Error = 4 ft x 4 x 26 = 416 ft.\n"
        "  - Because air is colder than standard, True Altitude is 416 ft LOWER than indicated!\n\n"
        "FINAL ANSWER: To maintain the published 6,000 ft true clearance over obstacles, the pilot MUST fly an indicated altitude of at least 6,416 ft (6,000 + 416 ft)!",
        max_chars=86
    )

    pdf.add_heading_1("4. Lowest Usable Flight Level Under Low Pressure")
    pdf.add_paragraph(
        "When atmospheric pressure drops below 1013.25 hPa, Flight Levels sink closer to terrain. "
        "For example, at QNH 980 hPa (33 hPa below standard):\n"
        "• 33 hPa x 27 ft/hPa = ~891 ft loss of true clearance.\n"
        "• ATC must raise the Transition Level and lowest usable Flight Level by 1,000 ft to preserve safety margins.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch10 = [
        ("Q1: In climb, when does the altimeter subscale setting change from QNH to Standard 1013.25?",
         "[A] At the Transition Level (TRL)\n[B] Passing the Transition Altitude (TA)\n[C] Leaving controlled airspace\n[D] At 10,000 ft",
         "CORRECT: [B]. In climb, altimeters are set to 1013.25 upon passing the Transition Altitude (TA)."),
        ("Q2: In air colder than ISA, does the altimeter overread or underread?",
         "[A] It underreads (true altitude is higher than indicated).\n[B] It overreads (true altitude is lower than indicated).\n[C] It indicates correctly because pressure remains unchanged.\n[D] It only errors when climbing above FL 100.",
         "CORRECT: [B]. In cold air, air columns shrink; pressure levels drop closer to ground. The altimeter overreads (shows higher than actual true altitude)."),
        ("Q3: Is level cruising flight permitted within the Transition Layer?",
         "[A] Yes, if authorized by ATC.\n[B] Yes, under VFR only.\n[C] NO, level flight within the transition layer is strictly prohibited.\n[D] Only during holding procedures.",
         "CORRECT: [C]. Cruising in level flight within the Transition Layer is strictly prohibited."),
        ("Q4: If QNH is 980 hPa (substantially below standard), what happens to the lowest usable Flight Level?",
         "[A] It is lower than usual\n[B] It is higher than usual to guarantee minimum obstacle clearance\n[C] It is unaffected\n[D] Flight Levels are suspended",
         "CORRECT: [B]. Low atmospheric pressure compresses pressure levels towards the surface, requiring ATC to raise the lowest usable Flight Level to maintain terrain clearance."),
        ("Q5: If an aircraft flies from an area of high pressure into an area of low pressure without adjusting altimeter setting, what is the hazard?",
         "[A] The altimeter will underread and aircraft will climb\n[B] The altimeter will overread and true altitude will be dangerously lower than indicated\n[C] Airspeed indicator will fail\n[D] Autopilot will disconnect automatically",
         "CORRECT: [B]. 'High to low, look out below!' The altimeter registers the lower ambient pressure as higher altitude, causing the pilot or autopilot to fly closer to terrain than indicated."),
        ("Q6: What is the maximum permitted tolerance when checking a primary altimeter against aerodrome elevation on the ground?",
         "[A] +/- 20 ft\n[B] +/- 60 ft (to +/- 75 ft depending on test conditions)\n[C] +/- 150 ft\n[D] +/- 250 ft",
         "CORRECT: [B]. Under PANS-OPS, the pre-flight ground altimeter check tolerance is +/- 60 to 75 ft of the published aerodrome/runway elevation.")
    ]
    for q_text, opts, exp in questions_ch10:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 10 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 11: PARALLEL RUNWAY OPERATIONS (~3 pages)
# ==============================================================================
def build_ch11():
    pdf_path = os.path.join(BASE_DIR, "010_ch11_parallel_runways.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 11: Parallel Runway Operations")
    pdf.add_title_banner("Air Law", 11, "Parallel Runway Operations", "239-252")

    pdf.add_heading_1("1. Modes of Operation & Minimum Centerline Spacing")
    pdf.add_paragraph(
        "Simultaneous operations on parallel or near-parallel runways are governed by ICAO Doc 4444 (PANS-ATM) "
        "and Doc 8168. Minimum centerline separation distances are strictly tested:",
        max_chars=92
    )

    rwy_data = [
        ["Independent Parallel Approaches", "At least 1,035 m (3,400 ft)", "Simultaneous approaches where radar separation between aircraft on adjacent ILS localizers is NOT required. Requires dedicated radar monitor controllers."],
        ["Dependent Parallel Approaches", "At least 915 m (3,000 ft)", "Simultaneous approaches where radar separation minima (stagger) between aircraft on adjacent extended centerlines IS required (usually 1.5 or 2.0 NM)."],
        ["Independent Parallel Departures", "At least 1,035 m (3,400 ft)", "Simultaneous departures where departure tracks diverge immediately by at least 15° after take-off."],
        ["Segregated Parallel Operations", "At least 760 m (2,500 ft)", "One runway is used exclusively for departures, and the other runway is used exclusively for arrivals."]
    ]
    pdf.add_table(["Operational Mode", "Min. Centerline Spacing", "Operational Criteria & Stagger Requirements"], rwy_data, col_widths=[115.0, 115.0, 280.0])

    pdf.add_heading_1("2. Protected Zones: NOZ and NTZ")
    pdf.add_bullet("Normal Operating Zone (NOZ)", "An airspace corridor extending from runway threshold to point where aircraft intercepts ILS, within which aircraft are expected to maneuver.")
    pdf.add_bullet("No Transgression Zone (NTZ)", "A non-maneuvering corridor of at least 610 m (2,000 ft) width located centrally between the two extended runway centerlines. Penetration by an aircraft requires immediate controller breakout instructions.")

    pdf.add_callout(
        "trap",
        "NTZ Penetration & Breakout Instructions",
        "When an aircraft is observed penetrating the NTZ, the radar controller immediately instructs the "
        "threatened aircraft on the adjacent localizer to execute a BREAKOUT MANEUVER (e.g. 'Turn left immediately "
        "heading 270, climb to 3,000 ft'). The pilot must execute the breakout without delay.",
        max_chars=86
    )

    pdf.add_heading_1("3. Precision Runway Monitor (PRM) Systems")
    pdf.add_paragraph(
        "PRM radar systems provide fast radar updates (<= 2.5 seconds) and high-resolution displays. "
        "When PRM is in use, independent parallel approaches can be conducted on runways with centerline "
        "spacing as close as 1,035 m without staggered separation.",
        max_chars=92
    )

    pdf.add_heading_1("4. Intersecting & Converging Runway Operations")
    pdf.add_paragraph(
        "For operations on intersecting or converging runways, take-off and landing clearances are coordinated "
        "so that aircraft flight paths never cross simultaneously. When wake turbulence from an intersecting departure "
        "crosses the arrival path, a full 2-minute (or 3-minute for intermediate intersection) separation is applied.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch11 = [
        ("Q1: What is the minimum runway centerline spacing for independent parallel instrument approaches?",
         "[A] 760 m (2,500 ft)\n[B] 915 m (3,000 ft)\n[C] 1,035 m (3,400 ft)\n[D] 1,500 m (5,000 ft)",
         "CORRECT: [C]. Independent parallel approaches require at least 1,035 m (3,400 ft) centerline spacing."),
        ("Q2: What is the minimum width of the No Transgression Zone (NTZ) between parallel runway centerlines?",
         "[A] 300 m\n[B] 610 m (2,000 ft)\n[C] 915 m\n[D] 1,035 m",
         "CORRECT: [B]. The NTZ must be at least 610 m (2,000 ft) wide and located midway between the two extended runway centerlines."),
        ("Q3: For independent parallel departures, what is the minimum track divergence required immediately after take-off?",
         "[A] 10°\n[B] 15°\n[C] 30°\n[D] 45°",
         "CORRECT: [B]. Tracks must diverge by at least 15° immediately after take-off for independent parallel departures."),
        ("Q4: What is the minimum runway centerline spacing for segregated parallel operations?",
         "[A] 610 m\n[B] 760 m (2,500 ft)\n[C] 915 m\n[D] 1,035 m",
         "CORRECT: [B]. Segregated parallel operations (one runway arrival, one runway departure) require at least 760 m spacing."),
        ("Q5: What is the required radar stagger distance between aircraft on adjacent parallel ILS localizers during dependent parallel approaches?",
         "[A] 1.0 NM\n[B] 1.5 NM to 2.0 NM\n[C] 3.0 NM\n[D] 5.0 NM",
         "CORRECT: [B]. Dependent parallel approaches require a radar stagger of 1.5 NM (or 2.0 NM) between successive arrivals on parallel localizers."),
        ("Q6: During independent parallel approaches, what immediate action is required from an aircraft instructed to execute a breakout maneuver?",
         "[A] Request reason from ATC before turning\n[B] Disconnect autopilot and comply immediately with heading and climb/descent instructions without delay\n[C] Continue on localizer until visual contact is made\n[D] Squawk 7600",
         "CORRECT: [B]. A breakout instruction is issued when another aircraft penetrates the No Transgression Zone (NTZ). The pilot must comply immediately."),
        ("Q7: Under PANS-ATM, what is the maximum convergence or divergence angle for two runways to be classified as near-parallel?",
         "[A] 5°\n[B] 10°\n[C] 15°\n[D] 30°",
         "CORRECT: [C]. Non-intersecting runways whose extended centerlines have an angle of convergence or divergence of 15° or less are classified as near-parallel runways.")
    ]
    for q_text, opts, exp in questions_ch11:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 11 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 12: SSR AND ACAS (~3 pages)
# ==============================================================================
def build_ch12():
    pdf_path = os.path.join(BASE_DIR, "010_ch12_ssr_acas.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 12: SSR and ACAS (TCAS II)")
    pdf.add_title_banner("Air Law", 12, "SSR and ACAS (TCAS II)", "253-262")

    pdf.add_heading_1("1. Secondary Surveillance Radar (SSR) Modes")
    pdf.add_bullet("Mode A", "4-digit octal code (4,096 combinations) for aircraft identification assigned by ATC.")
    pdf.add_bullet("Mode C", "Transmits automated pressure altitude (referenced to 1013.25 hPa) in 100 ft increments.")
    pdf.add_bullet("Mode S", "Transmits unique 24-bit aircraft address; selective interrogation; enhanced surveillance parameters (Downlink Airborne Parameters - DAP: selected altitude, roll angle, IAS, Mach).")

    pdf.add_callout(
        "trap",
        "Mandatory Emergency Transponder Codes (Memorize 100%)",
        "• 7500: Unlawful Interference (Hijacking).\n"
        "• 7600: Lost Communications (Radio Failure).\n"
        "• 7700: General Emergency / Distress.\n"
        "• 7000: Standard VFR conspicuity in Europe (1200 in USA).\n"
        "• 2000: Default IFR entry code into uncontrolled airspace or oceanic control without assigned code.",
        max_chars=86
    )

    pdf.add_heading_1("2. Airborne Collision Avoidance System (ACAS II / TCAS II)")
    pdf.add_paragraph(
        "ACAS II interrogates Mode C/S transponders of nearby aircraft to provide warnings based on Time to CPA (tau):",
        max_chars=92
    )

    acas_data = [
        ["Traffic Advisory (TA)", "Amber solid circle", "20 to 48 seconds to CPA", "Audio: 'TRAFFIC, TRAFFIC'. Visual scan only. NO EVASIVE MANEUVER PERMITTED."],
        ["Resolution Advisory (RA)", "Red solid square", "15 to 35 seconds to CPA", "Audio: 'CLIMB', 'DESCEND', etc. Vertical evasive instruction. Pilot MUST disconnect autopilot and comply immediately."]
    ]
    pdf.add_table(["Warning Level", "Display Symbol", "Time to CPA (Tau)", "Cockpit Action & Pilot Response"], acas_data, col_widths=[105.0, 100.0, 100.0, 205.0])

    pdf.add_callout(
        "trap",
        "Pilot Response Time & Absolute Priority of TCAS RA",
        "1. Response Time: Pilot must initiate response within 5 SECONDS for initial RA, and within 2.5 SECONDS for "
        "an increased or reversal RA (G-load 0.25 g initial, 0.35 g reversal).\n"
        "2. RA vs ATC Clearance: TCAS RA OVERRULES ATC CLEARANCE. If an RA contradicts an ATC instruction, the pilot "
        "MUST follow the RA without hesitation, and advise ATC as soon as possible ('TCAS RA').",
        max_chars=86
    )

    pdf.add_heading_1("3. TCAS II Version 7.1 'Level Off' Modification")
    pdf.add_paragraph(
        "TCAS II Version 7.1 introduced a critical safety enhancement: the 'Adjust Vertical Speed, Adjust' RA was "
        "replaced by 'Level Off, Level Off'. This instructs the crew to reduce vertical climb/descent to zero ft/min, "
        "preventing excessive vertical excursions during crossing encounters.",
        max_chars=92
    )

    pdf.add_heading_1("4. Mode S Downlink Airborne Parameters (DAPs)")
    pdf.add_bullet("Basic DAP", "Flight status (airborne/ground), Mode A code, 24-bit aircraft address, aircraft identification (callsign).")
    pdf.add_bullet("Enhanced DAP", "Selected altitude, roll angle, true track angle, ground speed, magnetic heading, indicated airspeed (IAS) / Mach, and vertical rate (barometric or inertial).")

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch12 = [
        ("Q1: What is the transponder code for an aircraft experiencing unlawful interference (hijacking)?",
         "[A] 7700\n[B] 7600\n[C] 7500\n[D] 7000",
         "CORRECT: [C]. 7500 = hijacking; 7600 = radio failure; 7700 = general emergency."),
        ("Q2: In the event of a TCAS Resolution Advisory (RA) contradicting an ATC instruction, what action is required?",
         "[A] Follow ATC instruction and ignore TCAS.\n[B] Ask ATC for clarification before maneuvering.\n[C] Follow TCAS RA immediately and advise ATC as soon as possible.\n[D] Turn 90° horizontally to avoid conflict.",
         "CORRECT: [C]. TCAS RA takes absolute priority over ATC clearances. Comply immediately with RA."),
        ("Q3: What is the maximum pilot reaction time allowed to respond to an initial TCAS Resolution Advisory?",
         "[A] 2.5 seconds\n[B] 5.0 seconds\n[C] 10.0 seconds\n[D] 15.0 seconds",
         "CORRECT: [B]. Reaction time must be within 5 seconds for initial RA, and within 2.5 seconds for an increased or reversal RA."),
        ("Q4: Which transponder code should be set by an IFR aircraft entering an airspace region without an assigned squawk code?",
         "[A] 7000\n[B] 2000\n[C] 1200\n[D] 7700",
         "CORRECT: [B]. Mode A Code 2000 is the standard IFR code when no code has been assigned by ATC."),
        ("Q5: Under TCAS II Version 7.1, what new resolution advisory replaced 'Adjust Vertical Speed, Adjust'?",
         "[A] 'Maintain Vertical Speed'\n[B] 'Level Off, Level Off'\n[C] 'Descend Immediately'\n[D] 'Climb and Turn Left'",
         "CORRECT: [B]. TCAS II version 7.1 replaced 'Adjust Vertical Speed' with 'Level Off, Level Off' to eliminate pilot over-corrections."),
        ("Q6: What is the required pilot response time for an increased or reversal TCAS Resolution Advisory (RA)?",
         "[A] 5.0 seconds\n[B] 2.5 seconds\n[C] 1.0 second\n[D] 10.0 seconds",
         "CORRECT: [B]. Pilot reaction time for a reversal or increased rate RA is 2.5 seconds (with 0.35 g target acceleration).")
    ]
    for q_text, opts, exp in questions_ch12:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 12 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch07()
    build_ch08()
    build_ch09()
    build_ch10()
    build_ch11()
    build_ch12()


