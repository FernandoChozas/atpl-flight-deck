#!/usr/bin/env python3
"""
Deep Comprehensive Generator for 010 Air Law (Chapters 6 to 10 - PANS-OPS).
Designed for 100% self-contained study without textbooks.
Includes:
- Chapter 6: Instrument Departure Procedures (SID, NADP 1/2) (3 pages)
- Chapter 7: Approach Procedures (Segments, Cats A-E, ILS Cat I/II/III, CDFA) (4 pages)
- Chapter 8: Circling Approach Procedures (2 pages)
- Chapter 9: Holding Procedures (Geometry, Speeds, Sectors, Wind Drift) (3 pages)
- Chapter 10: Altimeter Setting Procedures (Temperature Error, Lowest Usable FL) (2 pages)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

# ==============================================================================
# CHAPTER 6: INSTRUMENT DEPARTURES & NADP
# ==============================================================================
def build_ch06():
    pdf_path = os.path.join(BASE_DIR, "010_ch06_departures.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 6: Instrument Departure Procedures")
    pdf.add_title_banner("Air Law", 6, "Instrument Departures (SID & NADP)", "157-172")

    pdf.add_heading_1("1. PANS-OPS Departure Design Gradients")
    pdf.add_paragraph(
        "Instrument departure procedures (ICAO Doc 8168 PANS-OPS) provide obstacle clearance from the end of the "
        "runway until the aircraft reaches the minimum en-route altitude (MEA). Design assumes all engines operating.",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "Procedure Design Gradient (PDG) = 3.3%",
        "The standard PANS-OPS Procedure Design Gradient (PDG) is 3.3% (~200 ft/NM).\n"
        "It consists of:\n"
        "1. Obstacle Identification Surface (OIS): 2.5%\n"
        "2. Obstacle Clearance Margin: 0.8%\n"
        "-> Total Standard PDG = 3.3%. A steeper climb gradient is published ONLY if required by obstacles or airspace.",
        max_chars=86
    )

    pdf.add_heading_1("2. Straight vs Turning Departures")
    pdf.add_bullet("Screen Height at DER", "The departure procedure assumes the aircraft crosses the Departure End of Runway (DER) at a minimum screen height of 5 m (16 ft) with wings level.")
    pdf.add_bullet("Straight Departure", "Track does not diverge by more than 15° from runway centerline heading.")
    pdf.add_bullet("Turning Departure", "Specified whenever track requires a turn of MORE THAN 15°. No turn shall be initiated below 120 m (394 ft) above aerodrome elevation (or DER).")
    pdf.add_bullet("Turn Design Parameters", "Average bank angle: 15° (max 21°). Speed limits are specified per category.")

    pdf.add_heading_1("3. Noise Abatement Departure Procedures (NADP 1 vs NADP 2)")
    pdf.add_paragraph(
        "ICAO Annex 6 and PANS-OPS define two standardized noise abatement departure procedures for jet aeroplanes:",
        max_chars=92
    )

    nadp_data = [
        ["NADP 1 (Noise Close to Aerodrome)", "Climb at V2 + 10 to 20 kt with take-off flaps to 800 ft (or higher). At 800 ft to 3,000 ft, reduce to climb thrust, maintain climb speed with flaps intact. At 3,000 ft, accelerate and retract flaps."],
        ["NADP 2 (Noise Distant from Aerodrome)", "Climb at V2 + 10 to 20 kt to 800 ft. At 800 ft, accelerate while retracting flaps on schedule, then reduce to climb thrust. Continue climb to 3,000 ft."]
    ]
    pdf.add_table(["Procedure", "Climb Profile & Flap Retraction Schedule"], nadp_data, col_widths=[150.0, 360.0])

    pdf.add_heading_1("4. Omnidirectional Departures")
    pdf.add_paragraph(
        "Used when no specific SID route is published. The aircraft climbs straight ahead to at least 120 m (394 ft) "
        "above aerodrome elevation before initiating a turn to the en-route heading. Obstacle clearance is provided in all sectors.",
        max_chars=92
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Standard PANS-OPS PDG? -> 3.3% (2.5% OIS + 0.8% margin).")
    pdf.add_bullet("Q2", "Assumed screen height at DER? -> 5 m (16 ft).")
    pdf.add_bullet("Q3", "Minimum altitude to begin a turn on departure? -> 120 m (394 ft) above aerodrome elevation.")
    pdf.add_bullet("Q4", "Which NADP alleviates noise close to the airport? -> NADP 1 (maintains flaps until 3,000 ft).")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 6 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 7: APPROACH PROCEDURES & ILS CATEGORIES
# ==============================================================================
def build_ch07():
    pdf_path = os.path.join(BASE_DIR, "010_ch07_approach_procedures.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 7: Approach Procedures (PANS-OPS)")
    pdf.add_title_banner("Air Law", 7, "Approach Procedures & ILS Minima", "173-206")

    pdf.add_heading_1("1. The Five Approach Segments")
    seg_data = [
        ["1. Arrival", "En-route to IAF", "Transitions aircraft to the Initial Approach Fix (IAF). Standard Terminal Arrival (STAR)."],
        ["2. Initial", "IAF to IF", "MOC at least 300 m (984 ft) in primary area. Reversal or racetrack procedures conducted here."],
        ["3. Intermediate", "IF to FAF / FAP", "Aircraft speed and configuration adjusted. MOC decreases from 300 m to 150 m (492 ft). Max descent gradient: 5.2% (3.0°)."],
        ["4. Final", "FAF / FAP to MAPt", "Precision: Glidepath 3.0° to Decision Altitude/Height (DA/H).\nNon-Precision: FAF to Minimum Descent Altitude/Height (MDA/H)."],
        ["5. Missed Approach", "MAPt to holding/en-route", "3 phases: Initial (MAPt to start of climb, NO TURN permitted), Intermediate (climb at 2.5% gradient, MOC 30 m), Final (climb to safe level, MOC 50 m)."]
    ]
    pdf.add_table(["Segment", "Boundaries", "Operational Purpose & Minimum Obstacle Clearance (MOC)"], seg_data, col_widths=[95.0, 105.0, 310.0])

    pdf.add_heading_1("2. Aircraft Approach Categories (A to E)")
    pdf.add_paragraph(
        "Based on Vat (indicated airspeed at runway threshold), where Vat = 1.3 x Vso (or 1.23 x Vs1g) at max landing mass:",
        max_chars=92
    )

    cat_data = [
        ["Category A", "Less than 91 kt", "Light singles and twins (C172, PA-28)"],
        ["Category B", "91 kt to 120 kt", "Heavy twins, regional turboprops (King Air, ATR-42/72)"],
        ["Category C", "121 kt to 140 kt", "Medium commercial airliners (Airbus A320, Boeing 737)"],
        ["Category D", "141 kt to 165 kt", "Heavy wide-body airliners (Boeing 777, 747, Airbus A350)"],
        ["Category E", "166 kt to 210 kt", "Special high-performance jet and military aircraft"]
    ]
    pdf.add_table(["Category", "Vat Threshold Speed Range", "Representative Aircraft Types"], cat_data, col_widths=[85.0, 160.0, 265.0])

    pdf.add_heading_1("3. Reversal & Racetrack Maneuvers")
    pdf.add_bullet("45°/180° Procedure Turn", "Turn 45° off outbound track, fly for 1 MINUTE (Cat A/B) or 1 MIN 15 SEC (Cat C/D/E), then turn 180° in opposite direction to intercept inbound.")
    pdf.add_bullet("80°/260° Procedure Turn", "Turn 80° off outbound track, immediately followed by a 260° turn in opposite direction to intercept inbound track.")
    pdf.add_bullet("Base Turn", "Aircraft flies outbound on a specified radial/track, then turns to intercept the final approach track.")
    pdf.add_bullet("Racetrack Procedure", "Aircraft flies outbound parallel to inbound track for 1 to 3 minutes, then turns to intercept inbound.")

    pdf.add_heading_1("4. Exhaustive ILS Precision Approach Categories (Cat I, II, III)")
    pdf.add_paragraph(
        "Precision approaches provide electronic glidepath and azimuth guidance. Official EASA minima:",
        max_chars=92
    )

    ils_data = [
        ["Category I (Cat I)", "Not lower than 200 ft (60 m)", "Not less than 550 m (or 800 m visibility without RVR)"],
        ["Category II (Cat II)", "Lower than 200 ft but not lower than 100 ft (30 m)", "Not less than 300 m RVR"],
        ["Category IIIA (Cat IIIA)", "Lower than 100 ft or NO Decision Height", "Not less than 175 m RVR"],
        ["Category IIIB (Cat IIIB)", "Lower than 50 ft or NO Decision Height", "Less than 175 m but not less than 50 m RVR"],
        ["Category IIIC (Cat IIIC)", "NO Decision Height", "NO Runway Visual Range limitations (Zero-Zero)"]
    ]
    pdf.add_table(["ILS Category", "Decision Height (DH)", "Minimum Runway Visual Range (RVR)"], ils_data, col_widths=[125.0, 210.0, 175.0])

    pdf.add_callout(
        "trap",
        "DA/H vs MDA/H (Precision vs Non-Precision)",
        "• Decision Altitude/Height (DA/H): Used in PRECISION approaches. If visual reference is not established upon "
        "reaching DA/H, an IMMEDIATE MISSED APPROACH must be initiated. The aircraft may dip slightly below DA/H during the go-around.\n"
        "• Minimum Descent Altitude/Height (MDA/H): Used in NON-PRECISION approaches. The aircraft MUST NEVER descend below "
        "MDA/H without visual reference. Level flight at MDA is permitted until reaching the MAPt.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Minimum RVR for an ILS Category I approach? -> 550 m.")
    pdf.add_bullet("Q2", "Minimum DH for an ILS Category II approach? -> 100 ft (RVR: 300 m).")
    pdf.add_bullet("Q3", "MOC in the Initial Approach Segment? -> 300 m (984 ft).")
    pdf.add_bullet("Q4", "Can you fly level at DA/H in a precision approach? -> NO, immediate go-around.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 7 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 8: CIRCLING APPROACH
# ==============================================================================
def build_ch08():
    pdf_path = os.path.join(BASE_DIR, "010_ch08_circling_approach.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 8: Circling Approach Procedures")
    pdf.add_title_banner("Air Law", 8, "Circling Approach Procedures", "207-214")

    pdf.add_heading_1("1. Definition & Operational Criteria")
    pdf.add_paragraph(
        "A circling approach is the visual phase of an instrument approach to bring an aircraft into position for "
        "landing on a runway which is not suitably located for a straight-in approach (runway alignment exceeds 30°, "
        "or descent gradient exceeds standard criteria).",
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
    circling_data = [
        ["Cat A", "100 kt", "1.68 NM (3.11 km)", "90 m (295 ft)"],
        ["Cat B", "135 kt", "2.66 NM (4.93 km)", "90 m (295 ft)"],
        ["Cat C", "180 kt", "4.20 NM (7.78 km)", "120 m (394 ft)"],
        ["Cat D", "205 kt", "5.28 NM (9.78 km)", "120 m (394 ft)"],
        ["Cat E", "240 kt", "6.94 NM (12.85 km)", "150 m (492 ft)"]
    ]
    pdf.add_table(["Category", "Max Circling Speed", "Circling Radius from Thresholds", "Minimum Obstacle Clearance (MOC)"], circling_data, col_widths=[75.0, 115.0, 155.0, 165.0])

    pdf.add_callout(
        "trap",
        "Loss of Visual Reference While Circling (Guaranteed Exam Question)",
        "If visual reference is lost at any time while circling to land:\n"
        "1. The pilot must initiate an IMMEDIATE CLIMBING TURN TOWARDS THE LANDING RUNWAY.\n"
        "2. Establish the aircraft overhead the aerodrome to ensure terrain clearance.\n"
        "3. Join and follow the published missed approach procedure for the INSTRUMENT RUNWAY initially used.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Circling radius for Category C aircraft? -> 4.20 NM.")
    pdf.add_bullet("Q2", "MOC for Cat C circling? -> 120 m (394 ft).")
    pdf.add_bullet("Q3", "First immediate action upon losing visual reference during circling? -> Climbing turn towards the landing runway.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 8 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 9: HOLDING PROCEDURES
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

    pdf.add_heading_1("4. Wind Drift Correction in Holding")
    pdf.add_callout(
        "trap",
        "Triple Drift Rule on Outbound Leg",
        "To compensate for crosswind in a holding pattern:\n"
        "• Apply wind correction angle on the inbound leg (e.g. 5° into wind).\n"
        "• On the outbound leg, apply THREE TIMES (3x) the inbound drift angle in the opposite direction (e.g. 15°).\n"
        "• Adjust outbound timing for headwind/tailwind to achieve exact 1 min (or 1.5 min) inbound leg.",
        max_chars=86
    )

    pdf.add_heading_1("5. Obstacle Clearance in Holding")
    pdf.add_bullet("Primary Area", "Full MOC provided throughout: at least 300 m (984 ft / 1,000 ft), or 600 m (2,000 ft) in designated mountainous areas.")
    pdf.add_bullet("Buffer Area", "Extends 5 NM beyond the primary area boundary. MOC tapers from full value at inner edge to ZERO at the outer 5 NM boundary.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Standard outbound leg time above 14,000 ft? -> 1.5 minutes (1 min at or below 14,000 ft).")
    pdf.add_bullet("Q2", "Max holding speed below 14,000 ft? -> 230 kt.")
    pdf.add_bullet("Q3", "Size of Sector 1 (Parallel entry)? -> 110° (Sector 2: 70°, Sector 3: 180°).")
    pdf.add_bullet("Q4", "Width of the holding buffer area? -> 5 NM.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 9 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 10: ALTIMETER SETTING PROCEDURES & TEMPERATURE ERROR
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

    pdf.add_heading_1("3. Altimeter Temperature Error Correction")
    pdf.add_paragraph(
        "Pressure altimeters are calibrated to the International Standard Atmosphere (ISA). In temperatures colder than "
        "ISA, the true altitude is LOWER than the indicated altitude ('High to low or hot to cold, look out below!'):",
        max_chars=92
    )

    pdf.add_bullet("Correction Rule of Thumb", "Correction = 4 ft per 1,000 ft of altitude above the altimeter setting source per °C deviation from ISA. (Always ADD correction to published minimum altitudes in cold weather).")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "When climbing, at what point do you change to 1013.25? -> Passing Transition Altitude (TA).")
    pdf.add_bullet("Q2", "In cold weather (colder than ISA), does altimeter overread or underread? -> Overreads (true altitude is lower than indicated).")
    pdf.add_bullet("Q3", "Can you cruise level in the Transition Layer? -> NO, prohibited.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 10 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch06()
    build_ch07()
    build_ch08()
    build_ch09()
    build_ch10()
