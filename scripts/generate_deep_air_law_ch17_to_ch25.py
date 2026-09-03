#!/usr/bin/env python3
"""
Deep Comprehensive Generator for 010 Air Law (Chapters 17 to 25).
Designed for 100% self-contained study without textbooks.
Includes:
- Chapter 17: AIS & AIRAC System (2 pages)
- Chapter 18: Aerodromes - Physical Characteristics & OLS (3 pages)
- Chapter 19: Aerodromes - Visual Aids, Markings & Signs (3 pages)
- Chapter 20: Aerodrome Lighting (Calvert, PAPI) (2 pages)
- Chapter 21: Obstacles & Aerodrome Services (RFFS Foam/Response) (2 pages)
- Chapter 22: Facilitation (Annex 9) (2 pages)
- Chapter 23: Search and Rescue (SAR Patterns & Codes) (2 pages)
- Chapter 24: Security (Annex 17) (2 pages)
- Chapter 25: Accident & Incident Investigation (Annex 13) (2 pages)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

# ==============================================================================
# CHAPTER 17: AIS & AIRAC
# ==============================================================================
def build_ch17():
    pdf_path = os.path.join(BASE_DIR, "010_ch17_ais.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 17: Aeronautical Information Service (AIS)")
    pdf.add_title_banner("Air Law", 17, "AIS, AIP & AIRAC System", "357-374")

    pdf.add_heading_1("1. The Integrated Aeronautical Information Package (IAIP)")
    pdf.add_bullet("AIP (Aeronautical Information Publication)", "Basic permanent regulatory document. Divided into 3 PARTS: GEN (General - laws, tables, units, services), ENR (En-route - airspace, ATS routes, navaids), AD (Aerodromes - runways, visual aids, procedures).")
    pdf.add_bullet("AIP Amendments (AIP AMDT)", "Permanent changes to the AIP. Regular or AIRAC.")
    pdf.add_bullet("AIP Supplements (AIP SUP)", "Temporary changes of long duration (3 MONTHS OR LONGER) or changes with extensive text/graphics. Published on YELLOW paper.")
    pdf.add_bullet("NOTAM & PIB", "Notice to Airmen (max validity 3 MONTHS) and Pre-flight Information Bulletins.")
    pdf.add_bullet("AIC (Aeronautical Information Circulars)", "Administrative, technical, or advisory notices: White (Admin), Yellow (Operational / ATC), Pink (Flight Safety), Mauve (Airspace restrictions).")

    pdf.add_heading_1("2. The AIRAC System (AviationExam Core)")
    pdf.add_callout(
        "trap",
        "AIRAC Publication & Implementation Timelines",
        "• Standard Cycle: Published on predetermined dates based on a 28-DAY INTERVAL.\n"
        "• Publication Lead Time: Must be dispatched at least 42 DAYS in advance of effective date.\n"
        "• Major Operational Changes: Must be dispatched at least 56 DAYS in advance (e.g. major airspace redesign, new runway).",
        max_chars=86
    )

    pdf.add_heading_1("3. Special NOTAM Formats: SNOWTAM & ASHTAM")
    pdf.add_bullet("SNOWTAM", "Special series NOTAM notifying presence or removal of hazardous snow, slush, ice, or standing water on runways. Maximum validity is 8 HOURS (or 24 hours). A new SNOWTAM must be issued whenever there is a significant change.")
    pdf.add_bullet("ASHTAM", "Special series NOTAM notifying operationally significant changes in volcanic activity, volcanic ash clouds, or contamination. Maximum validity is 24 HOURS.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Standard AIRAC cycle duration? -> 28 days.")
    pdf.add_bullet("Q2", "Advance notice required for major AIRAC changes? -> 56 days (standard: 42 days).")
    pdf.add_bullet("Q3", "Maximum validity period of a standard NOTAM? -> 3 months.")
    pdf.add_bullet("Q4", "Color of AIP Supplements? -> Yellow paper.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 17 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 18: AERODROMES - PHYSICAL CHARACTERISTICS & OLS
# ==============================================================================
def build_ch18():
    pdf_path = os.path.join(BASE_DIR, "010_ch18_aerodromes_characteristics.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 18: Aerodromes - Characteristics & OLS")
    pdf.add_title_banner("Air Law", 18, "Aerodrome Design & OLS Surfaces", "375-398")

    pdf.add_heading_1("1. Aerodrome Reference Code (Annex 14)")
    code_data = [
        ["Code 1", "Field Length < 800 m", "Code A", "Wingspan < 15 m (Gear span < 4.5 m)"],
        ["Code 2", "Field Length 800 m to < 1,200 m", "Code B", "Wingspan 15 m to < 24 m (Gear span 4.5 to < 6 m)"],
        ["Code 3", "Field Length 1,200 m to < 1,800 m", "Code C", "Wingspan 24 m to < 36 m (Gear span 6 to < 9 m) [A320, B737]"],
        ["Code 4", "Field Length >= 1,800 m", "Code D", "Wingspan 36 m to < 52 m (Gear span 9 to < 14 m) [B767]"],
        ["—", "—", "Code E", "Wingspan 52 m to < 65 m (Gear span 9 to < 14 m) [B777, A350]"],
        ["—", "—", "Code F", "Wingspan 65 m to < 80 m (Gear span 14 to < 16 m) [A380, B747-8]"]
    ]
    pdf.add_table(["Code No.", "Reference Field Length", "Code Letter", "Wingspan & Outer Main Gear Wheel Span"], code_data, col_widths=[65.0, 175.0, 80.0, 190.0])

    pdf.add_heading_1("2. Declared Distances (TORA, TODA, ASDA, LDA)")
    pdf.add_bullet("TORA (Take-Off Run Available)", "Length of runway suitable for ground run on take-off.")
    pdf.add_bullet("TODA (Take-Off Distance Available)", "TORA + Clearway. (Max allowable clearway length = 0.5 x TORA).")
    pdf.add_bullet("ASDA (Accelerate-Stop Distance Available)", "TORA + Stopway.")
    pdf.add_bullet("LDA (Landing Distance Available)", "Length of runway available for ground run on landing. Measured from threshold.")
    pdf.add_bullet("Displaced Threshold", "When threshold is displaced, LDA is REDUCED by displacement. Area before displaced threshold may be used for take-off in either direction, but NOT for landing.")

    pdf.add_heading_1("3. Runway End Safety Area (RESA)")
    pdf.add_paragraph(
        "A RESA is an area symmetrical about extended centerline intended to reduce risk of damage to aircraft "
        "undershooting or overrunning runway. For Code 3 and 4 runways: minimum length is 90 m (recommended 240 m); "
        "width must be at least TWICE the runway width.",
        max_chars=92
    )

    pdf.add_heading_1("4. Obstacle Limitation Surfaces (OLS)")
    pdf.add_paragraph(
        "Airspace around aerodromes is protected by defined obstacle limitation surfaces:",
        max_chars=92
    )
    pdf.add_bullet("Approach Surface", "Inclined plane preceding threshold. Slope varies from 2.0% to 3.3% based on code.")
    pdf.add_bullet("Transitional Surface", "Slopes upward and outward from runway strip edges to the inner horizontal surface. Standard slope: 14.3% (1:7) for Code 3/4 runways.")
    pdf.add_bullet("Inner Horizontal Surface", "Circular plane located 45 m above aerodrome elevation (radius 4,000 m for Code 4).")
    pdf.add_bullet("Conical Surface", "Extends upward and outward from perimeter of inner horizontal surface at a 5% slope.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Reference code for runway >= 1,800 m? -> Code 4.")
    pdf.add_bullet("Q2", "Code letter for A320/B737? -> Code C.")
    pdf.add_bullet("Q3", "Standard minimum length of a RESA? -> 90 m (recommended 240 m).")
    pdf.add_bullet("Q4", "Height of the Inner Horizontal Surface? -> 45 m above aerodrome elevation.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 18 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 19: VISUAL AIDS - MARKINGS AND SIGNS
# ==============================================================================
def build_ch19():
    pdf_path = os.path.join(BASE_DIR, "010_ch19_visual_aids_markings.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 19: Visual Aids, Markings & Signs")
    pdf.add_title_banner("Air Law", 19, "Aerodrome Markings & Signage", "399-424")

    pdf.add_heading_1("1. Runway Markings (White)")
    stripes_data = [
        ["18 m runway width", "4 stripes"],
        ["23 m runway width", "6 stripes"],
        ["30 m runway width", "8 stripes"],
        ["45 m runway width", "12 stripes (Standard transport runway)"],
        ["60 m runway width", "16 stripes"]
    ]
    pdf.add_table(["Runway Width", "Number of Runway Threshold Stripes (Piano Keys)"], stripes_data, col_widths=[240.0, 270.0])

    pdf.add_bullet("Aiming Point", "Two conspicuous white rectangular stripes located 400 m from threshold on runways >= 2,400 m.")
    pdf.add_bullet("Touchdown Zone", "Pairs of rectangular stripes arranged symmetrically about centerline at 150 m intervals.")

    pdf.add_heading_1("2. Taxiway Markings & Holding Positions (Yellow)")
    pdf.add_bullet("Pattern A Holding Position", "Two solid yellow lines and two dashed yellow lines across taxiway. Solid lines on taxiway side; dashed lines on runway side. Aircraft MUST NOT cross solid lines towards runway without clearance.")
    pdf.add_bullet("Pattern B Holding Position", "Ladder pattern ('railway tracks'). Critical area holding point for Category II / III operations. Aircraft holds here in Low Visibility Procedures (LVP).")

    pdf.add_heading_1("3. Aerodrome Signs: Mandatory vs Information")
    signs_data = [
        ["Mandatory Instruction Sign", "WHITE letters on RED background", "Identifies entrance to runway, critical area, or prohibited zone (e.g. '09-27', 'NO ENTRY', 'CAT II/III'). Must not be crossed without ATC clearance."],
        ["Location Sign", "YELLOW letters on BLACK background", "Identifies the taxiway or runway where the aircraft is currently located ('Black square, you are there')."],
        ["Direction / Destination Sign", "BLACK letters on YELLOW background", "Indicates designation and direction of intersecting taxiways ('Yellow lead you to the fellow')."]
    ]
    pdf.add_table(["Sign Type", "Color Scheme", "Operational Meaning & Mnemonic"], signs_data, col_widths=[135.0, 165.0, 210.0])

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Color of runway markings vs taxiway markings? -> Runway: White; Taxiway: Yellow.")
    pdf.add_bullet("Q2", "Number of threshold stripes on a 45 m wide runway? -> 12 stripes.")
    pdf.add_bullet("Q3", "Color of Mandatory Instruction signs? -> White letters on Red background.")
    pdf.add_bullet("Q4", "Color of Location signs? -> Yellow letters on Black background.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 19 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 20: AERODROME LIGHTING
# ==============================================================================
def build_ch20():
    pdf_path = os.path.join(BASE_DIR, "010_ch20_aerodrome_lighting.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 20: Aerodrome Lighting Systems")
    pdf.add_title_banner("Air Law", 20, "Aerodrome Lighting & PAPI Systems", "425-446")

    pdf.add_heading_1("1. Runway Lighting Colors (Master Rule)")
    lights_data = [
        ["Runway Edge Lights", "Variable WHITE", "White, EXCEPT that on instrument runways the last 600 m (or 1/3, whichever is less) are YELLOW / AMBER to warn of runway end."],
        ["Runway Threshold Lights", "GREEN", "Unbroken transverse line of green lights showing in direction of approach."],
        ["Runway End Lights", "RED", "Unbroken transverse line of red lights showing in direction of take-off / rollout."],
        ["Runway Centerline Lights", "WHITE, RED/WHITE, RED", "White from threshold to 900 m from end; Alternating RED and WHITE from 900 m to 300 m from end; RED for the final 300 m."],
        ["Touchdown Zone (TDZ) Lights", "WHITE barrettes", "Extends from threshold for 900 m (or midpoint). Transverse rows of white barrettes."],
        ["Taxiway Edge / Centerline", "BLUE edge / GREEN centerline", "Taxiway edge lights are BLUE; Centerline lights are GREEN (flashing or alternate yellow/green in runway lead-on)."]
    ]
    pdf.add_table(["Lighting System", "Color(s)", "Location & Warning Progression"], lights_data, col_widths=[125.0, 115.0, 270.0])

    pdf.add_heading_1("2. Precision Approach Path Indicator (PAPI)")
    pdf.add_paragraph(
        "PAPI consists of a wing bar of 4 multi-lamp units on the left side of the runway. Standard glidepath: 3.0°:",
        max_chars=92
    )
    pdf.add_bullet("4 White Lights", "High (above 3° 30').")
    pdf.add_bullet("3 White, 1 Red", "Slightly High (3° 10').")
    pdf.add_bullet("2 White, 2 Red", "ON GLIDEPATH (3° 00' - 'Two red, two white, you're all right').")
    pdf.add_bullet("1 White, 3 Red", "Slightly Low (2° 50').")
    pdf.add_bullet("4 Red Lights", "Low (below 2° 30' - 'All red, you're dead').")

    pdf.add_heading_1("3. Approach Lighting Systems (ALS)")
    pdf.add_bullet("Simple Approach Lighting System", "Single row of lights extending at least 420 m from threshold with a 30 m crossbar at 300 m.")
    pdf.add_bullet("Precision Approach Lighting (Calvert)", "Extends 900 m from threshold with 5 crossbars at 150 m intervals. Centerline lights and side row barrettes.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Color of runway edge lights in last 600 m of instrument runway? -> Yellow / Amber.")
    pdf.add_bullet("Q2", "Color of runway centerline lights in final 300 m? -> Red.")
    pdf.add_bullet("Q3", "PAPI indication when on glidepath? -> 2 White, 2 Red.")
    pdf.add_bullet("Q4", "Color of taxiway edge lights? -> Blue.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 20 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 21: OBSTACLES & AERODROME SERVICES (RFFS)
# ==============================================================================
def build_ch21():
    pdf_path = os.path.join(BASE_DIR, "010_ch21_obstacle_marking_services.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 21: Obstacles & Aerodrome Services")
    pdf.add_title_banner("Air Law", 21, "Obstacles & Rescue Services (RFFS)", "447-460")

    pdf.add_heading_1("1. Rescue and Fire Fighting Services (RFFS Categories 1 to 10)")
    rffs_data = [
        ["Category 1", "0 m up to 9 m", "2 m", "Very light singles (C152, PA-28)"],
        ["Category 5", "24 m up to 28 m", "4 m", "Regional turboprops (ATR-42)"],
        ["Category 6", "28 m up to 39 m", "5 m", "Regional jets (CRJ-900, E190)"],
        ["Category 7", "39 m up to 49 m", "5 m", "Single-aisle airliners (A320, B737-800)"],
        ["Category 8", "49 m up to 61 m", "7 m", "Wide-body twin-aisle (B767, B787, A330)"],
        ["Category 9", "61 m up to 76 m", "8 m", "Heavy airliners (B777, B747, A350)"],
        ["Category 10", "76 m up to 90 m", "8 m", "Very heavy airliners (Airbus A380-800)"]
    ]
    pdf.add_table(["RFFS Category", "Aircraft Overall Length", "Max Fuselage Width", "Representative Types"], rffs_data, col_widths=[90.0, 130.0, 115.0, 175.0])

    pdf.add_callout(
        "trap",
        "RFFS Mandatory Response Times",
        "The operational objective of the RFFS is to achieve a response time of:\n"
        "• Optimum: Not exceeding 2 MINUTES to the end of each operational runway.\n"
        "• Maximum: Not exceeding 3 MINUTES to any point of each operational runway in optimum visibility.",
        max_chars=86
    )

    pdf.add_heading_1("2. Extinguishing Agents: Principal vs Complementary")
    pdf.add_bullet("Principal Agents", "Water and foam meeting performance level A, B, or C. Provides permanent fire suppression.")
    pdf.add_bullet("Complementary Agents", "Dry chemical powders or CO2. Rapid knock-down capability.")

    pdf.add_heading_1("3. Obstacle Lighting Classification")
    pdf.add_bullet("Low-Intensity", "Fixed RED lights for obstacles with height less than 45 m.")
    pdf.add_bullet("Medium-Intensity", "Flashing RED or flashing WHITE lights for obstacles between 45 m and 150 m.")
    pdf.add_bullet("High-Intensity", "Flashing WHITE lights for obstacles exceeding 150 m height (active day and night).")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "RFFS Category for A320/B737? -> Category 7.")
    pdf.add_bullet("Q2", "RFFS Category for A380? -> Category 10.")
    pdf.add_bullet("Q3", "Maximum allowable RFFS response time? -> 3 minutes (optimum 2 minutes).")
    pdf.add_bullet("Q4", "Obstacle lights for obstacles > 150 m? -> High-intensity flashing white.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 21 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 22: FACILITATION (ANNEX 9)
# ==============================================================================
def build_ch22():
    pdf_path = os.path.join(BASE_DIR, "010_ch22_facilitation.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 22: Facilitation (Annex 9)")
    pdf.add_title_banner("Air Law", 22, "Facilitation (ICAO Annex 9)", "461-470")

    pdf.add_heading_1("1. Purpose of ICAO Annex 9")
    pdf.add_paragraph(
        "Annex 9 aims to prevent unnecessary delays to aircraft, crew, passengers, and cargo, especially in customs, "
        "immigration, quarantine, and public health clearance procedures.",
        max_chars=92
    )

    pdf.add_heading_1("2. Required Flight Documentation")
    pdf.add_bullet("General Declaration", "Signed by pilot-in-command or authorized agent. Details aircraft registration, flight number, routing, declaration of health, and passenger/cargo numbers.")
    pdf.add_bullet("Crew Member Certificate (CMC)", "Issued by State of Registry. Enables visa-free temporary entry for flight crew for operational and duty purposes.")
    pdf.add_bullet("Transit Passengers", "States shall not require visas or disembarkation cards for transit passengers remaining in the airport transit area.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which Annex deals with Facilitation? -> Annex 9.")
    pdf.add_bullet("Q2", "Who signs the General Declaration? -> Pilot-in-Command or authorized agent.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 22 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 23: SEARCH AND RESCUE (ANNEX 12)
# ==============================================================================
def build_ch23():
    pdf_path = os.path.join(BASE_DIR, "010_ch23_sar.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 23: Search and Rescue (SAR)")
    pdf.add_title_banner("Air Law", 23, "Search and Rescue (ICAO Annex 12)", "471-480")

    pdf.add_heading_1("1. SAR Organization: RCC & RSC")
    pdf.add_bullet("Rescue Coordination Centre (RCC)", "Operational unit responsible for promoting efficient SAR organization and coordinating SAR operations within a SAR region.")
    pdf.add_bullet("Rescue Sub-centre (RSC)", "Subordinate unit complementing an RCC within a specific sub-region.")

    pdf.add_heading_1("2. Ground-to-Air Visual Signal Codes (Survivors / Searchers)")
    sar_data = [
        ["V", "Require assistance"],
        ["X", "Require medical assistance"],
        ["N", "NO or Negative"],
        ["Y", "YES or Affirmative"],
        ["-> (Arrow)", "Proceeding in this direction"],
        ["LL", "All well (used by search parties)"]
    ]
    pdf.add_table(["Symbol", "Official Meaning / Requirement"], sar_data, col_widths=[140.0, 370.0])

    pdf.add_callout(
        "trap",
        "Aircraft Acknowledgement of Ground Signals",
        "• Day: Rocking wings (alternately banking left and right) = 'Signal understood'.\n"
        "• Night: Flashing landing lights or navigation lights twice = 'Signal understood'.\n"
        "• Making a complete 360° turn to the right or yawing = 'Signal NOT understood'.",
        max_chars=86
    )

    pdf.add_heading_1("3. Standard Search Patterns")
    pdf.add_bullet("Track Crawl / Route Search", "Aircraft searches along the intended flight path.")
    pdf.add_bullet("Parallel Sweep Search", "Used when search area is large and terrain is flat. Aircraft fly parallel tracks.")
    pdf.add_bullet("Expanding Square Search", "Used when the location of the distress is known within close limits (concentric expanding squares).")
    pdf.add_bullet("Sector Search", "Used when the position of the target is known with high precision (star-shaped sector pattern).")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Ground symbol 'V'? -> Require assistance.")
    pdf.add_bullet("Q2", "Ground symbol 'X'? -> Require medical assistance.")
    pdf.add_bullet("Q3", "Day acknowledgement signal from aircraft? -> Rocking wings.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 23 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 24: SECURITY (ANNEX 17)
# ==============================================================================
def build_ch24():
    pdf_path = os.path.join(BASE_DIR, "010_ch24_security.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 24: Aviation Security (Annex 17)")
    pdf.add_title_banner("Air Law", 24, "Aviation Security (Annex 17)", "481-494")

    pdf.add_heading_1("1. Objectives of Aviation Security")
    pdf.add_paragraph(
        "Annex 17 aims to safeguard international civil aviation against acts of unlawful interference. "
        "The primary objective is the safety of passengers, crew, ground personnel, and the general public.",
        max_chars=92
    )

    pdf.add_heading_1("2. Flight Crew Compartment Security")
    pdf.add_bullet("Door Construction", "Passenger aircraft over 45,500 kg MTOM (or carrying > 60 passengers) must have a cockpit door resistant to small arms fire and grenade shrapnel.")
    pdf.add_bullet("Door Locking Protocol", "Must be capable of being locked/unlocked from either pilot seat. Must remain closed and locked from the moment all external doors are closed following embarkation until any door is opened for disembarkation.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which Annex deals with Security? -> Annex 17.")
    pdf.add_bullet("Q2", "When must cockpit door be locked? -> From doors closed after embarkation until disembarkation.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 24 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 25: ACCIDENT & INCIDENT INVESTIGATION (ANNEX 13)
# ==============================================================================
def build_ch25():
    pdf_path = os.path.join(BASE_DIR, "010_ch25_accident_investigation.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 25: Accident Investigation (Annex 13)")
    pdf.add_title_banner("Air Law", 25, "Accident Investigation (Annex 13)", "495-504")

    pdf.add_heading_1("1. Official Definition of an ACCIDENT (Annex 13)")
    pdf.add_callout(
        "definition",
        "Definition of an Accident",
        "An occurrence associated with the operation of an aircraft between the time any person boards with the "
        "intention of flight until such time as all persons have disembarked, in which:\n"
        "1. A person is FATALLY or SERIOUSLY INJURED (except self-inflicted, natural causes, or stowaways);\n"
        "2. The aircraft sustains DAMAGE OR STRUCTURAL FAILURE adversely affecting strength, performance, or "
        "flight characteristics, requiring major repair; OR\n"
        "3. The aircraft is MISSING or completely inaccessible.",
        max_chars=86
    )

    pdf.add_bullet("Serious Incident", "An incident involving circumstances indicating that there was a high probability of an accident (e.g. near collision, runway incursion, multiple engine failure).")
    pdf.add_bullet("Incident", "An occurrence other than an accident which affects or could affect the safety of operation.")

    pdf.add_heading_1("2. Sole Objective of Investigation (Absolute Exam Core)")
    pdf.add_callout(
        "trap",
        "Sole Objective: Prevention of Accidents (NOT Blame)",
        "The sole objective of the investigation of an accident or incident under Annex 13 shall be the "
        "PREVENTION of accidents and incidents. It is explicitly NOT the purpose of this activity to "
        "apportion blame or liability.",
        max_chars=86
    )

    pdf.add_heading_1("3. State Responsibilities & Final Report")
    pdf.add_bullet("Investigation Responsibility", "The State of OCCURRENCE institutes the inquiry.")
    pdf.add_bullet("Accredited Representatives", "State of Registry, State of Operator, State of Design, and State of Manufacture are entitled to appoint an Accredited Representative.")
    pdf.add_bullet("Final Report Target", "Shall release the Final Report as soon as possible, ideally within 12 MONTHS.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which Annex covers Accident Investigation? -> Annex 13.")
    pdf.add_bullet("Q2", "Sole objective of an accident investigation? -> Prevention of accidents (NOT blame or liability).")
    pdf.add_bullet("Q3", "Target deadline for publishing final report? -> Within 12 months.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 25 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch17()
    build_ch18()
    build_ch19()
    build_ch20()
    build_ch21()
    build_ch22()
    build_ch23()
    build_ch24()
    build_ch25()
