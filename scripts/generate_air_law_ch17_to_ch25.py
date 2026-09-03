#!/usr/bin/env python3
"""
Generator for 010 Air Law - Final Block (Chapters 17 to 25):
- Chapter 17: Aeronautical Information Service (AIS, AIP, AIRAC, NOTAM, SNOWTAM, ASHTAM, AIC)
- Chapter 18: Aerodromes - Physical Characteristics (Annex 14, Reference codes 1-4 & A-F, TORA/TODA/ASDA/LDA, RESA)
- Chapter 19: Aerodromes - Visual Aids, Markings & Signs (Threshold stripes, Pattern A/B, Mandatory vs Info signs)
- Chapter 20: Aerodrome Lighting (Approach systems, Runway edge/centerline/end lights, PAPI colors & angles)
- Chapter 21: Obstacle Marking & Aerodrome Services (RFFS categories 1-10, Response times 2/3 min)
- Chapter 22: Facilitation (Annex 9, General Declaration, Entry/Departure, Customs)
- Chapter 23: Search and Rescue (Annex 12, RCC, Emergency phases, Ground-Air signals V, X, N, Y)
- Chapter 24: Security (Annex 17, Flight deck door, Unlawful interference, Screening)
- Chapter 25: Aircraft Accident & Incident Investigation (Annex 13, Accident definition, 12-month report, Sole objective)

Generates publication-grade, study-friendly PDFs and companion Markdown files.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

# ==============================================================================
# CHAPTER 17: AIS
# ==============================================================================
def build_ch17():
    pdf_path = os.path.join(BASE_DIR, "010_ch17_ais.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch17_ais.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 17: Aeronautical Information Service (AIS)")
    pdf.add_title_banner("Air Law", 17, "Aeronautical Information Service", "357-374")

    pdf.add_heading_1("1. The Integrated Aeronautical Information Package (IAIP)")
    pdf.add_paragraph(
        "Governed by ICAO Annex 15, the IAIP ensures the timely flow of aeronautical information necessary for "
        "the safety, regularity, and efficiency of international air navigation. It consists of:",
        max_chars=92
    )
    pdf.add_bullet("AIP (Aeronautical Information Publication)", "Basic permanent regulatory document. Divided into 3 PARTS: GEN (General), ENR (En-route), and AD (Aerodromes).")
    pdf.add_bullet("AIP Amendments (AIP AMDT)", "Permanent changes to the AIP. Regular or AIRAC.")
    pdf.add_bullet("AIP Supplements (AIP SUP)", "Temporary changes of long duration (3 months or longer) or changes with extensive text/graphics. Published on yellow paper.")
    pdf.add_bullet("NOTAM & PIB", "Notice to Airmen and Pre-flight Information Bulletins (operational urgency).")
    pdf.add_bullet("AIC (Aeronautical Information Circulars)", "Information of administrative, technical, or advisory nature not qualifying for AIP or NOTAM.")

    pdf.add_callout(
        "trap",
        "The AIRAC System (AviationExam Core)",
        "• AIRAC (Aeronautical Information Regulation and Control) governs operationally significant changes.\n"
        "• Standard Cycle: Published on predetermined dates based on a 28-DAY CYCLE.\n"
        "• Publication lead time: Must be sent at least 42 DAYS in advance of effective date.\n"
        "• Major changes (e.g. airspace redesign): Must be sent at least 56 DAYS in advance.",
        max_chars=86
    )

    pdf.add_heading_1("2. NOTAM, SNOWTAM & ASHTAM")
    pdf.add_bullet("NOTAM Validity", "A NOTAM has a maximum validity of 3 MONTHS. If the condition continues beyond 3 months, a replacing NOTAM must be issued or an AIP supplement published.")
    pdf.add_bullet("SNOWTAM", "Special series NOTAM notifying presence of snow, slush, ice, or standing water on runways. Maximum validity is 8 HOURS (or 24 hours). Issued whenever there is a significant change.")
    pdf.add_bullet("ASHTAM", "Special series NOTAM notifying operationally significant changes in volcanic ash activity or contamination. Maximum validity is 24 HOURS.")
    pdf.add_bullet("AIC Color Coding", "White: Administrative. Yellow: Operational (ATC, navigation). Pink: Safety (flight safety awareness). Mauve: National airspace restrictions."),

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Standard AIRAC cycle duration? -> 28 days.")
    pdf.add_bullet("Q2", "Advance notice for major AIRAC changes? -> 56 days (standard: 42 days).")
    pdf.add_bullet("Q3", "Three parts of the AIP? -> GEN, ENR, AD.")
    pdf.add_bullet("Q4", "Maximum validity period of a NOTAM? -> 3 months.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 010 Air Law | Chapter 17: Aeronautical Information Service (AIS)\n\n"
                "Syllabus: Annex 15, AIP 3 parts (GEN, ENR, AD), AIRAC 28-day cycle, NOTAM (max 3 months), SNOWTAM, ASHTAM, AIC colors.\n")
    print(f"Generated Ch 17: {pdf_path}")

# ==============================================================================
# CHAPTER 18: AERODROMES - PHYSICAL CHARACTERISTICS
# ==============================================================================
def build_ch18():
    pdf_path = os.path.join(BASE_DIR, "010_ch18_aerodromes_characteristics.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch18_aerodromes_characteristics.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 18: Aerodromes - Physical Characteristics")
    pdf.add_title_banner("Air Law", 18, "Aerodrome Characteristics & Distances", "375-398")

    pdf.add_heading_1("1. Aerodrome Reference Code (Annex 14)")
    pdf.add_paragraph(
        "Annex 14 classifies aerodrome facilities using a two-element reference code based on critical aircraft design:",
        max_chars=92
    )

    code_table = [
        ["Code 1", "Reference Field Length < 800 m", "Code A", "Wingspan < 15 m (Gear span < 4.5 m)"],
        ["Code 2", "Field Length 800 m to < 1,200 m", "Code B", "Wingspan 15 m to < 24 m (Gear span 4.5 to < 6 m)"],
        ["Code 3", "Field Length 1,200 m to < 1,800 m", "Code C", "Wingspan 24 m to < 36 m (Gear span 6 to < 9 m) [A320, B737]"],
        ["Code 4", "Field Length >= 1,800 m", "Code D", "Wingspan 36 m to < 52 m (Gear span 9 to < 14 m) [B767]"],
        ["—", "—", "Code E", "Wingspan 52 m to < 65 m (Gear span 9 to < 14 m) [B777, A350]"],
        ["—", "—", "Code F", "Wingspan 65 m to < 80 m (Gear span 14 to < 16 m) [A380, B747-8]"]
    ]
    pdf.add_table(
        ["Element 1 (Number)", "Airplane Reference Field Length", "Element 2 (Letter)", "Wingspan & Outer Main Gear Span"],
        code_table,
        col_widths=[105.0, 150.0, 100.0, 150.0]
    )

    pdf.add_heading_1("2. Declared Distances: TORA, TODA, ASDA, LDA")
    pdf.add_bullet("TORA (Take-Off Run Available)", "Length of runway declared available and suitable for the ground run of an aeroplane taking off.")
    pdf.add_bullet("TODA (Take-Off Distance Available)", "TORA plus length of Clearway (if available). (Max clearway length = 0.5 x TORA).")
    pdf.add_bullet("ASDA (Accelerate-Stop Distance Available)", "TORA plus length of Stopway (if available).")
    pdf.add_bullet("LDA (Landing Distance Available)", "Length of runway declared available and suitable for the ground run of an aeroplane landing. Measured from the threshold.")

    pdf.add_callout(
        "trap",
        "Displaced Threshold & Declared Distances",
        "When a threshold is displaced (moved down the runway):\n"
        "• LDA is REDUCED by the distance of the displacement.\n"
        "• TORA, TODA, and ASDA are NOT reduced for take-off in the opposite direction.\n"
        "• The area before a displaced threshold can be used for take-off, but NOT for landing.",
        max_chars=86
    )

    pdf.add_heading_1("3. Runway End Safety Area (RESA)")
    pdf.add_paragraph(
        "A RESA is an area symmetrical about the extended runway centerline intended to reduce damage to an "
        "aircraft undershooting or overrunning the runway. For Code 3 and 4 runways: minimum length is 90 m "
        "(recommended 240 m); width is at least TWICE the runway width.",
        max_chars=92
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Reference code for runway length >= 1,800 m? -> Code 4.")
    pdf.add_bullet("Q2", "Reference code letter for A320/B737 (wingspan 24-36 m)? -> Code C.")
    pdf.add_bullet("Q3", "Formula for TODA? -> TORA + Clearway.")
    pdf.add_bullet("Q4", "Formula for ASDA? -> TORA + Stopway.")
    pdf.add_bullet("Q5", "Standard minimum length of a RESA for code 3/4? -> 90 m (recommended 240 m).")

    pdf.compile_pdf(pdf_path)

    # Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 010 Air Law | Chapter 18: Aerodromes - Physical Characteristics\n\n"
                "Syllabus: Annex 14 Reference Code 1-4 and A-F, TORA/TODA/ASDA/LDA, Clearway/Stopway, RESA (90m/240m).\n")
    print(f"Generated Ch 18: {pdf_path}")

# ==============================================================================
# CHAPTER 19: VISUAL AIDS - MARKINGS AND SIGNS
# ==============================================================================
def build_ch19():
    pdf_path = os.path.join(BASE_DIR, "010_ch19_visual_aids_markings.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch19_visual_aids_markings.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 19: Visual Aids, Markings & Signs")
    pdf.add_title_banner("Air Law", 19, "Aerodrome Markings and Signs", "399-424")

    pdf.add_heading_1("1. Runway Markings (White)")
    pdf.add_paragraph(
        "All runway markings are WHITE (except yellow for displaced threshold arrows/chevrons and runway lead-in lines):",
        max_chars=92
    )

    stripes_table = [
        ["18 m runway width", "4 stripes"],
        ["23 m runway width", "6 stripes"],
        ["30 m runway width", "8 stripes"],
        ["45 m runway width", "12 stripes (Standard for large runways)"],
        ["60 m runway width", "16 stripes"]
    ]
    pdf.add_table(
        ["Runway Width", "Number of Runway Threshold Stripes (Piano Keys)"],
        stripes_table,
        col_widths=[240.0, 265.0]
    )

    pdf.add_bullet("Aiming Point Marking", "Two conspicuous white rectangular stripes located 400 m from threshold on runways >= 2,400 m.")
    pdf.add_bullet("Touchdown Zone Markings", "Pairs of rectangular stripes symmetrically arranged about the runway centerline at 150 m intervals.")

    pdf.add_heading_1("2. Taxiway Markings & Holding Positions (Yellow)")
    pdf.add_bullet("Taxiway Centerline & Edges", "Taxiway markings are YELLOW. Centerline is a continuous yellow line.")
    pdf.add_bullet("Pattern A Holding Position", "Two solid yellow lines and two dashed yellow lines across taxiway. Located at runway intersection. Aircraft MUST NOT cross the solid lines towards the runway without ATC clearance.")
    pdf.add_bullet("Pattern B Holding Position", "Ladder pattern ('railway tracks'). Critical area holding point for Category II / III operations. Aircraft holds here when low visibility procedures are in force.")

    pdf.add_heading_1("3. Aerodrome Signs: Mandatory vs Information")
    pdf.add_paragraph(
        "Signs are strictly divided into two legal categories by color:",
        max_chars=92
    )

    signs_table = [
        ["Mandatory Instruction Sign", "WHITE inscription on RED background", "Identifies entrance to runway, critical area, or prohibited area (e.g. '09-27', 'NO ENTRY', 'CAT II/III'). MUST NOT be passed without ATC clearance."],
        ["Location Sign", "YELLOW inscription on BLACK background", "Identifies the taxiway or runway where the aircraft is currently located (e.g. 'B' - 'Black square, you are there')."],
        ["Direction / Destination Sign", "BLACK inscription on YELLOW background", "Indicates designation and direction of intersecting taxiways (e.g. '-> A' - 'Yellow lead you to the fellow')."]
    ]
    pdf.add_table(
        ["Sign Type", "Color Scheme", "Operational Meaning & Mnemonic"],
        signs_table,
        col_widths=[140.0, 160.0, 205.0]
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Color of runway markings vs taxiway markings? -> Runway: White; Taxiway: Yellow.")
    pdf.add_bullet("Q2", "Number of threshold stripes on a 45 m wide runway? -> 12 stripes.")
    pdf.add_bullet("Q3", "Color of Mandatory Instruction signs? -> White letters on Red background.")
    pdf.add_bullet("Q4", "Color of Location signs? -> Yellow letters on Black background.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 010 Air Law | Chapter 19: Aerodromes - Visual Aids, Markings and Signs\n\n"
                "Syllabus: Runway markings (45m = 12 stripes), Pattern A vs B holding positions, Mandatory vs Info signs.\n")
    print(f"Generated Ch 19: {pdf_path}")

# ==============================================================================
# CHAPTER 20: AERODROME LIGHTING
# ==============================================================================
def build_ch20():
    pdf_path = os.path.join(BASE_DIR, "010_ch20_aerodrome_lighting.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch20_aerodrome_lighting.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 20: Aerodrome Lighting")
    pdf.add_title_banner("Air Law", 20, "Aerodrome Lighting Systems", "425-446")

    pdf.add_heading_1("1. Runway Lighting Colors (Master Rule)")
    pdf.add_paragraph(
        "Runway lights follow a strict color code tested extensively in EASA examinations:",
        max_chars=92
    )

    lights_table = [
        ["Runway Edge Lights", "Variable WHITE", "White, EXCEPT that on instrument runways the last 600 m (or 1/3, whichever is less) are YELLOW / AMBER to warn of runway end."],
        ["Runway Threshold Lights", "GREEN", "Unbroken transverse line of green lights showing in direction of approach."],
        ["Runway End Lights", "RED", "Unbroken line of red lights showing in direction of take-off / rollout."],
        ["Runway Centerline Lights", "WHITE, RED/WHITE, RED", "White from threshold to 900 m from end; Alternating RED and WHITE from 900 m to 300 m from end; RED for the final 300 m."],
        ["Touchdown Zone (TDZ) Lights", "WHITE barrettes", "Extends from threshold for 900 m (or midpoint). Transverse rows of white barrettes."],
        ["Taxiway Edge / Centerline", "BLUE edge / GREEN centerline", "Taxiway edge lights are BLUE; Centerline lights are GREEN (flashing or alternate yellow/green in runway lead-on)."]
    ]
    pdf.add_table(
        ["Lighting System", "Color(s)", "Location & Warning Progression"],
        lights_table,
        col_widths=[125.0, 115.0, 265.0]
    )

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

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Color of runway threshold lights? -> Green.")
    pdf.add_bullet("Q2", "Color of runway end lights? -> Red.")
    pdf.add_bullet("Q3", "Color of runway centerline lights in the last 300 m? -> Red.")
    pdf.add_bullet("Q4", "PAPI indication when on the correct glidepath? -> 2 White, 2 Red.")
    pdf.add_bullet("Q5", "Color of taxiway edge lights? -> Blue.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 010 Air Law | Chapter 20: Aerodrome Lighting\n\n"
                "Syllabus: Runway edge (last 600m yellow), centerline (white -> red/white -> red in last 300m), PAPI 4 units.\n")
    print(f"Generated Ch 20: {pdf_path}")

# ==============================================================================
# CHAPTER 21: OBSTACLE MARKING & AERODROME SERVICES (RFFS)
# ==============================================================================
def build_ch21():
    pdf_path = os.path.join(BASE_DIR, "010_ch21_obstacle_marking_services.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch21_obstacle_marking_services.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 21: Obstacles & Aerodrome Services (RFFS)")
    pdf.add_title_banner("Air Law", 21, "Obstacles and Rescue Services (RFFS)", "447-460")

    pdf.add_heading_1("1. Rescue and Fire Fighting Services (RFFS Categories 1 to 10)")
    pdf.add_paragraph(
        "Aerodrome RFFS category is determined by the overall length of the longest aeroplane normally using "
        "the aerodrome and its maximum fuselage width:",
        max_chars=92
    )

    rffs_table = [
        ["Category 1", "0 m up to 9 m", "2 m", "Very light singles (C152, PA-28)"],
        ["Category 5", "24 m up to 28 m", "4 m", "Regional turboprops (ATR-42)"],
        ["Category 6", "28 m up to 39 m", "5 m", "Regional jets (CRJ-900, E190)"],
        ["Category 7", "39 m up to 49 m", "5 m", "Single-aisle airliners (A320, B737-800)"],
        ["Category 8", "49 m up to 61 m", "7 m", "Wide-body twin-aisle (B767, B787, A330)"],
        ["Category 9", "61 m up to 76 m", "8 m", "Heavy airliners (B777, B747, A350)"],
        ["Category 10", "76 m up to 90 m", "8 m", "Very heavy airliners (Airbus A380-800)"]
    ]
    pdf.add_table(
        ["RFFS Category", "Aircraft Overall Length", "Max Fuselage Width", "Typical Aircraft Types"],
        rffs_table,
        col_widths=[90.0, 130.0, 115.0, 170.0]
    )

    pdf.add_callout(
        "trap",
        "RFFS Mandatory Response Times (Very Frequently Examined)",
        "The operational objective of the RFFS is to achieve a response time of:\n"
        "• Optimum: Not exceeding 2 MINUTES to the end of each operational runway.\n"
        "• Maximum: Not exceeding 3 MINUTES to any point of each operational runway in optimum visibility.",
        max_chars=86
    )

    pdf.add_heading_1("2. Obstacle Lighting & Marking")
    pdf.add_bullet("Marking Colors", "Orange and white or red and white in alternating bands on conspicuous obstacles (masts, towers, chimneys).")
    pdf.add_bullet("Low-Intensity Lights", "Fixed RED lights used for obstacles with height less than 45 m.")
    pdf.add_bullet("Medium-Intensity Lights", "Flashing RED or flashing WHITE lights used for obstacles between 45 m and 150 m.")
    pdf.add_bullet("High-Intensity Lights", "Flashing WHITE lights used for obstacles exceeding 150 m height (active day and night).")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "RFFS Category for A320/B737? -> Category 7.")
    pdf.add_bullet("Q2", "RFFS Category for Airbus A380? -> Category 10.")
    pdf.add_bullet("Q3", "Maximum allowable RFFS response time? -> 3 minutes (optimum 2 minutes).")
    pdf.add_bullet("Q4", "Obstacle light color for obstacles below 45 m? -> Fixed red.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 010 Air Law | Chapter 21: Obstacle Marking and Aerodrome Services\n\n"
                "Syllabus: RFFS Categories 1 to 10 (A320 = Cat 7, A380 = Cat 10), response times (2 min / 3 min), obstacle lights.\n")
    print(f"Generated Ch 21: {pdf_path}")

# ==============================================================================
# CHAPTER 22: FACILITATION (ANNEX 9)
# ==============================================================================
def build_ch22():
    pdf_path = os.path.join(BASE_DIR, "010_ch22_facilitation.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch22_facilitation.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 22: Facilitation (Annex 9)")
    pdf.add_title_banner("Air Law", 22, "Facilitation (ICAO Annex 9)", "461-470")

    pdf.add_heading_1("1. Objectives of Facilitation")
    pdf.add_paragraph(
        "Annex 9 aims to prevent unnecessary delays to aircraft, crews, passengers, and cargo, especially in "
        "the administration of laws relating to customs, immigration, quarantine, and clearance.",
        max_chars=92
    )

    pdf.add_heading_1("2. Required Entry & Departure Documents")
    pdf.add_bullet("General Declaration", "Signed by pilot-in-command or authorized agent. Details aircraft registration, flight number, routing, declaration of health, and crew/passenger manifests.")
    pdf.add_bullet("Crew Member Certificate (CMC)", "Issued by the State of Registry to flight crew. Enables visa-free temporary entry for duty and relief purposes.")
    pdf.add_bullet("Disembarkation Cards", "Contracting States shall not require disembarkation/embarkation cards from citizens or from transit passengers who do not leave the airport transit area.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which ICAO Annex deals with Facilitation? -> Annex 9.")
    pdf.add_bullet("Q2", "Who signs the General Declaration? -> Pilot-in-Command or designated agent.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 010 Air Law | Chapter 22: Facilitation (Annex 9)\n\n"
                "Syllabus: Annex 9, General Declaration, Crew Member Certificate (CMC), transit procedures.\n")
    print(f"Generated Ch 22: {pdf_path}")

# ==============================================================================
# CHAPTER 23: SEARCH AND RESCUE (ANNEX 12)
# ==============================================================================
def build_ch23():
    pdf_path = os.path.join(BASE_DIR, "010_ch23_sar.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch23_sar.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 23: Search and Rescue (SAR)")
    pdf.add_title_banner("Air Law", 23, "Search and Rescue (ICAO Annex 12)", "471-480")

    pdf.add_heading_1("1. SAR Organization: RCC and RSC")
    pdf.add_bullet("Rescue Coordination Centre (RCC)", "A unit responsible for promoting efficient organization of search and rescue services and for coordinating the conduct of SAR operations within a SAR region.")
    pdf.add_bullet("Rescue Sub-centre (RSC)", "A unit subordinate to an RCC established to complement the latter within a specified sub-region.")

    pdf.add_heading_1("2. Ground-to-Air Visual Signal Codes (Survivors / Searchers)")
    pdf.add_paragraph(
        "Symbols used by survivors or ground parties to signal searching aircraft (Annex 12 Appendix 1):",
        max_chars=92
    )

    sar_table = [
        ["V", "Require assistance"],
        ["X", "Require medical assistance"],
        ["N", "NO or Negative"],
        ["Y", "YES or Affirmative"],
        ["-> (Arrow)", "Proceeding in this direction"],
        ["LL", "All well (used by search parties)"]
    ]
    pdf.add_table(
        ["Visual Ground Symbol", "Meaning / Requirement"],
        sar_table,
        col_widths=[150.0, 355.0]
    )

    pdf.add_callout(
        "trap",
        "Aircraft Acknowledgement Signals",
        "• Day: Rocking wings (bank left and right) = 'Signal understood'.\n"
        "• Night: Flashing landing lights or navigation lights twice = 'Signal understood'.\n"
        "• Making a complete 360° right-hand turn or yawing = 'Signal NOT understood'.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which ICAO Annex covers SAR? -> Annex 12.")
    pdf.add_bullet("Q2", "Ground symbol 'V'? -> Require assistance.")
    pdf.add_bullet("Q3", "Ground symbol 'X'? -> Require medical assistance.")
    pdf.add_bullet("Q4", "How does an aircraft acknowledge a ground signal by day? -> Rocking wings.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 010 Air Law | Chapter 23: Search and Rescue (Annex 12)\n\n"
                "Syllabus: Annex 12, RCC/RSC, Ground-to-air signals (V, X, N, Y), aircraft acknowledgement.\n")
    print(f"Generated Ch 23: {pdf_path}")

# ==============================================================================
# CHAPTER 24: SECURITY (ANNEX 17)
# ==============================================================================
def build_ch24():
    pdf_path = os.path.join(BASE_DIR, "010_ch24_security.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch24_security.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 24: Security (Annex 17)")
    pdf.add_title_banner("Air Law", 24, "Aviation Security (Annex 17)", "481-494")

    pdf.add_heading_1("1. Objectives of Aviation Security")
    pdf.add_paragraph(
        "Annex 17 aims to safeguard international civil aviation against acts of unlawful interference. "
        "The primary objective of each Contracting State is the safety of passengers, crew, ground personnel, and the public.",
        max_chars=92
    )

    pdf.add_heading_1("2. Flight Crew Compartment Security")
    pdf.add_bullet("Door Construction", "All passenger aircraft over 45,500 kg MTOM (or carrying > 60 passengers) must have a flight deck door resistant to penetration by small arms fire and grenade shrapnel.")
    pdf.add_bullet("Door Operation", "Must be capable of being locked and unlocked from either pilot's station. Must remain closed and locked from the moment all external doors are closed following embarkation until any door is opened for disembarkation.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which ICAO Annex deals with Security? -> Annex 17.")
    pdf.add_bullet("Q2", "When must the cockpit door be locked? -> From engine start / doors closed until disembarkation.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 010 Air Law | Chapter 24: Security (Annex 17)\n\n"
                "Syllabus: Annex 17, Flight deck door security, unruly passengers, screening requirements.\n")
    print(f"Generated Ch 24: {pdf_path}")

# ==============================================================================
# CHAPTER 25: ACCIDENT AND INCIDENT INVESTIGATION (ANNEX 13)
# ==============================================================================
def build_ch25():
    pdf_path = os.path.join(BASE_DIR, "010_ch25_accident_investigation.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch25_accident_investigation.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 25: Accident Investigation")
    pdf.add_title_banner("Air Law", 25, "Accident Investigation (Annex 13)", "495-504")

    pdf.add_heading_1("1. Definitions: Accident vs Serious Incident vs Incident")
    pdf.add_callout(
        "definition",
        "Official Definition of an ACCIDENT (Annex 13)",
        "An occurrence associated with the operation of an aircraft between the time any person boards the "
        "aircraft with the intention of flight until such time as all persons have disembarked, in which:\n"
        "1. A person is FATALLY or SERIOUSLY INJURED (except self-inflicted, natural causes, or stowaways);\n"
        "2. The aircraft sustains DAMAGE OR STRUCTURAL FAILURE adversely affecting strength, performance, or "
        "flight characteristics, requiring major repair; OR\n"
        "3. The aircraft is MISSING or completely inaccessible.",
        max_chars=86
    )

    pdf.add_bullet("Serious Incident", "An incident involving circumstances indicating that there was a high probability of an accident (e.g. near-collision, runway incursion, multiple engine failure, uncontained engine fire).")
    pdf.add_bullet("Incident", "An occurrence other than an accident, associated with the operation of an aircraft, which affects or could affect the safety of operation.")

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
    pdf.add_bullet("Investigation Responsibility", "The State of OCCURRENCE shall institute an inquiry into the circumstances of the accident.")
    pdf.add_bullet("Entitled States", "State of Registry, State of Operator, State of Design, and State of Manufacture are entitled to appoint an Accredited Representative to participate in the investigation.")
    pdf.add_bullet("Final Report Release", "The State conducting the investigation shall release the Final Report as soon as possible, ideally within 12 MONTHS of the date of the occurrence.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which ICAO Annex covers Accident Investigation? -> Annex 13.")
    pdf.add_bullet("Q2", "What is the sole objective of an accident investigation? -> Prevention of accidents (NOT blame or liability).")
    pdf.add_bullet("Q3", "Who institutes the investigation? -> The State of Occurrence.")
    pdf.add_bullet("Q4", "Target deadline for publishing the final accident report? -> Within 12 months.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 010 Air Law | Chapter 25: Aircraft Accident and Incident Investigation\n\n"
                "Syllabus: Annex 13, Accident definition, Serious Incident, State of Occurrence, 12-month report, Sole objective = Prevention.\n")
    print(f"Generated Ch 25: {pdf_path}")

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
