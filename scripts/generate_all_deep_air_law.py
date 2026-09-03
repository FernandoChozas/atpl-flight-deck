#!/usr/bin/env python3
"""
Master Deep Content Generator for 010 Air Law (Chapters 1 to 25).
Replaces all short summaries with full-depth, textbook-grade, 100% self-contained study guides.
Designed to hit the target ~75 to 85 pages across all 25 chapters.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder
from scripts.generate_deep_air_law_ch01_to_ch05 import build_ch01, build_ch02, build_ch03, build_ch04, build_ch05
from scripts.generate_deep_air_law_ch06_to_ch10 import build_ch06, build_ch07, build_ch08, build_ch09, build_ch10
from scripts.generate_deep_air_law_ch11_to_ch16 import build_ch11, build_ch12, build_ch13, build_ch14, build_ch15, build_ch16
from scripts.generate_deep_air_law_ch17_to_ch25 import build_ch17, build_ch18, build_ch19, build_ch20, build_ch21, build_ch22, build_ch23, build_ch24, build_ch25

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

# ==============================================================================
# EXPANDED CHAPTERS 17 TO 25 WITH MAXIMUM DEPTH
# ==============================================================================

def build_expanded_ch17():
    pdf_path = os.path.join(BASE_DIR, "010_ch17_ais.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 17: Aeronautical Information Service (AIS)")
    pdf.add_title_banner("Air Law", 17, "AIS, AIP & AIRAC System", "357-374")

    pdf.add_heading_1("1. The Integrated Aeronautical Information Package (IAIP)")
    pdf.add_paragraph(
        "Under ICAO Annex 15, the purpose of the Aeronautical Information Service (AIS) is to ensure the flow of "
        "aeronautical data and information necessary for the safety, regularity, and efficiency of air navigation. "
        "The Integrated Aeronautical Information Package (IAIP) consists of:",
        max_chars=92
    )
    pdf.add_bullet("AIP (Aeronautical Information Publication)", "Basic permanent regulatory document for flight operations. Divided into 3 PARTS: GEN (General), ENR (En-Route), and AD (Aerodromes).")
    pdf.add_bullet("AIP Amendments (AIP AMDT)", "Permanent changes to the AIP. Regular amendments or AIRAC amendments.")
    pdf.add_bullet("AIP Supplements (AIP SUP)", "Temporary changes of long duration (3 MONTHS OR LONGER) or changes with extensive text or graphics. Published on conspicuous YELLOW paper.")
    pdf.add_bullet("NOTAM (Notice to Airmen)", "Information of urgent operational significance that cannot be published in the AIP in time. Maximum validity: 3 MONTHS.")
    pdf.add_bullet("PIB (Pre-flight Information Bulletin)", "Recapitulation of current NOTAMs and urgent information prepared for flight crews prior to departure.")
    pdf.add_bullet("AIC (Aeronautical Information Circulars)", "Notices regarding flight safety, technical, administrative, or legislative matters: White (Administrative), Yellow (Operational / ATC), Pink (Flight Safety awareness), Mauve (Airspace restrictions).")

    pdf.add_heading_1("2. The AIRAC System (AviationExam Core)")
    pdf.add_paragraph(
        "The Aeronautical Information Regulation and Control (AIRAC) system governs the publication of operationally "
        "significant changes on predetermined dates based on a 28-DAY INTERVAL:",
        max_chars=92
    )
    pdf.add_bullet("Standard AIRAC Cycle", "28 days. Effective dates are Thursdays at 00:00 UTC.")
    pdf.add_bullet("Publication Lead Time", "Information must be dispatched by AIS at least 42 DAYS prior to the effective date so as to reach recipients at least 28 days before.")
    pdf.add_bullet("Major Operational Changes", "For significant changes (e.g. major airspace restructuring, new ATS routes, new runway), information must be dispatched at least 56 DAYS in advance.")

    pdf.add_heading_1("3. NOTAM Structure & Q-Code Decoding")
    pdf.add_paragraph(
        "A NOTAM is formatted into standardized fields: Series and number, followed by the Qualifiers line (Q-code) "
        "and items A to G:",
        max_chars=92
    )
    notam_data = [
        ["Q) Line", "Contains FIR, 5-letter Q-code (e.g. QFAXX), Traffic (I/V/IV), Purpose (N/B/O/M), Scope (A/E/W), Lower/Upper FL, Coordinates & Radius."],
        ["Item A)", "ICAO 4-letter location indicator of the aerodrome or FIR (e.g. LEMD, EGLL)."],
        ["Item B)", "Ten-figure date/time group indicating start of validity (YYMMDDHHMM UTC)."],
        ["Item C)", "Ten-figure date/time group indicating end of validity, or 'PERM' for permanent changes, or 'EST' for estimated duration."],
        ["Item D)", "Daily or periodic schedule of operation (if applicable)."],
        ["Item E)", "Plain-language decoded text of the NOTAM detailing the operational condition."],
        ["Items F) & G)", "Lower and upper altitude or flight level limits (e.g. GND / FL 120)."]
    ]
    pdf.add_table(["NOTAM Item", "Operational Meaning & Contents"], notam_data, col_widths=[95.0, 415.0])

    pdf.add_heading_1("4. Special NOTAM Series: SNOWTAM & ASHTAM")
    pdf.add_bullet("SNOWTAM", "Special NOTAM notifying the presence or removal of hazardous snow, slush, ice, or standing water on aerodrome runways. Maximum validity: 8 HOURS (or 24 hours). A new SNOWTAM is issued whenever there is a significant change in runway condition.")
    pdf.add_bullet("Global Reporting Format (GRF)", "Runway Condition Code (RWYCC) ranges from 0 (Extremely slippery / nil braking) to 6 (Dry / normal braking).")
    pdf.add_bullet("ASHTAM", "Special NOTAM notifying operationally significant changes in volcanic activity, volcanic ash clouds, or contamination. Maximum validity: 24 HOURS. Uses 4-level color code: Green, Yellow, Orange, Red.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Standard AIRAC cycle duration? -> 28 days.")
    pdf.add_bullet("Q2", "Advance notice required for major AIRAC changes? -> 56 days (standard: 42 days).")
    pdf.add_bullet("Q3", "Maximum validity period of a standard NOTAM? -> 3 months.")
    pdf.add_bullet("Q4", "Color of AIP Supplements? -> Yellow paper.")
    pdf.add_bullet("Q5", "Maximum validity of an ASHTAM? -> 24 hours.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 17 compiled: {pdf_path}")

def build_expanded_ch18():
    pdf_path = os.path.join(BASE_DIR, "010_ch18_aerodromes_characteristics.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 18: Aerodromes - Physical Characteristics")
    pdf.add_title_banner("Air Law", 18, "Aerodrome Design & OLS Surfaces", "375-398")

    pdf.add_heading_1("1. Aerodrome Reference Code (Annex 14)")
    pdf.add_paragraph(
        "Annex 14 classifies aerodrome facilities using a two-element reference code based on critical aircraft design:",
        max_chars=92
    )

    code_data = [
        ["Code 1", "Reference Field Length < 800 m", "Code A", "Wingspan < 15 m (Gear span < 4.5 m)"],
        ["Code 2", "Field Length 800 m to < 1,200 m", "Code B", "Wingspan 15 m to < 24 m (Gear span 4.5 to < 6 m)"],
        ["Code 3", "Field Length 1,200 m to < 1,800 m", "Code C", "Wingspan 24 m to < 36 m (Gear span 6 to < 9 m) [A320, B737]"],
        ["Code 4", "Field Length >= 1,800 m", "Code D", "Wingspan 36 m to < 52 m (Gear span 9 to < 14 m) [B767]"],
        ["—", "—", "Code E", "Wingspan 52 m to < 65 m (Gear span 9 to < 14 m) [B777, A350]"],
        ["—", "—", "Code F", "Wingspan 65 m to < 80 m (Gear span 14 to < 16 m) [A380, B747-8]"]
    ]
    pdf.add_table(["Code No.", "Airplane Reference Field Length", "Code Letter", "Wingspan & Outer Main Gear Wheel Span"], code_data, col_widths=[65.0, 175.0, 80.0, 190.0])

    pdf.add_heading_1("2. Runway Strips, Clearways & Stopways")
    pdf.add_bullet("Runway Strip", "A defined area including runway and stopway intended: 1) To reduce damage if aircraft veers off runway, 2) To protect aircraft flying over during take-off or landing. For Code 3/4 precision runways, extends 60 m beyond each runway end, with a total width of at least 280 m (140 m each side of centerline) or 300 m (150 m each side).")
    pdf.add_bullet("Clearway", "Rectangular area on ground or water under control of aerodrome, selected or prepared as suitable area over which an aeroplane may make a portion of its initial climb to a specified height. Maximum length shall not exceed HALF THE LENGTH OF TORA (Clearway max = 0.5 x TORA). Upward slope max 1.25%.")
    pdf.add_bullet("Stopway", "Defined rectangular area on ground at end of take-off run available, prepared as suitable area in which an aircraft can be stopped in the event of an abandoned take-off. Width equal to runway.")

    pdf.add_heading_1("3. Declared Distances (TORA, TODA, ASDA, LDA)")
    pdf.add_paragraph(
        "Declared distances are the operational lengths available for aircraft performance calculations:",
        max_chars=92
    )
    dist_data = [
        ["TORA (Take-Off Run Available)", "Length of runway declared available and suitable for the ground run of an aircraft taking off."],
        ["TODA (Take-Off Distance Available)", "TORA + Clearway. (The length of TORA plus length of clearway, if provided)."],
        ["ASDA (Accelerate-Stop Distance Available)", "TORA + Stopway. (The length of TORA plus length of stopway, if provided)."],
        ["LDA (Landing Distance Available)", "Length of runway declared available and suitable for the ground run of an aeroplane landing. Measured from threshold."]
    ]
    pdf.add_table(["Declared Distance", "Calculation Formula & Operational Definition"], dist_data, col_widths=[170.0, 340.0])

    pdf.add_callout(
        "trap",
        "Displaced Threshold & Practical Calculation Exercise",
        "When a runway threshold is DISPLACED (moved down the runway):\n"
        "• Landing Distance Available (LDA) is REDUCED by the displacement distance.\n"
        "• Take-Off Run Available (TORA), TODA, and ASDA are NOT reduced for take-off in that direction.\n"
        "• The area preceding a displaced threshold is suitable for take-off and roll, but NEVER for landing.",
        max_chars=86
    )

    pdf.add_heading_1("4. Runway End Safety Area (RESA)")
    pdf.add_paragraph(
        "An area symmetrical about extended runway centerline intended to reduce risk of damage to aircraft undershooting "
        "or overrunning runway. For Code 3 and 4 runways: minimum length is 90 m (recommended 240 m); width must be at "
        "least TWICE the width of the associated runway.",
        max_chars=92
    )

    pdf.add_heading_1("5. Obstacle Limitation Surfaces (OLS)")
    ols_data = [
        ["Approach Surface", "Inclined plane preceding threshold. Slope varies from 2.0% (Code 4 precision) to 3.3%."],
        ["Transitional Surface", "Complex surface sloping upward and outward from runway strip edges to the inner horizontal surface. Standard slope: 14.3% (1:7) for Code 3/4 runways."],
        ["Inner Horizontal Surface", "Circular horizontal plane located 45 m above aerodrome elevation (radius 4,000 m for Code 4). Protects visual maneuvering area."],
        ["Conical Surface", "Surface sloping upward and outward from perimeter of inner horizontal surface at a 5% slope to a specified height (100 m for Code 4)."],
        ["Balked Landing Surface", "Inclined plane located after threshold at a specified distance protecting aircraft executing a missed approach at very low altitude."]
    ]
    pdf.add_table(["OLS Surface", "Dimensions & Operational Protection Objective"], ols_data, col_widths=[140.0, 370.0])

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Maximum permitted length of a Clearway? -> Half the length of TORA (0.5 x TORA).")
    pdf.add_bullet("Q2", "Height of the Inner Horizontal Surface? -> 45 m above aerodrome elevation.")
    pdf.add_bullet("Q3", "Standard minimum length of a RESA for Code 4? -> 90 m (recommended 240 m).")
    pdf.add_bullet("Q4", "Slope of the Transitional Surface for Code 4? -> 14.3% (1:7).")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 18 compiled: {pdf_path}")

def build_expanded_ch19():
    pdf_path = os.path.join(BASE_DIR, "010_ch19_visual_aids_markings.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 19: Visual Aids, Markings & Signs")
    pdf.add_title_banner("Air Law", 19, "Aerodrome Markings & Signage", "399-424")

    pdf.add_heading_1("1. Runway Markings (White)")
    pdf.add_paragraph(
        "Runway markings are WHITE (except yellow for displaced threshold arrows/chevrons and runway lead-in lines):",
        max_chars=92
    )

    stripes_data = [
        ["18 m runway width", "4 stripes"],
        ["23 m runway width", "6 stripes"],
        ["30 m runway width", "8 stripes"],
        ["45 m runway width", "12 stripes (Standard commercial jet runway)"],
        ["60 m runway width", "16 stripes"]
    ]
    pdf.add_table(["Runway Width", "Number of Runway Threshold Stripes (Piano Keys)"], stripes_data, col_widths=[240.0, 270.0])

    pdf.add_bullet("Aiming Point", "Two conspicuous white rectangular stripes located 400 m from threshold on runways >= 2,400 m.")
    pdf.add_bullet("Touchdown Zone Markings", "Pairs of rectangular stripes arranged symmetrically about runway centerline at 150 m intervals.")
    pdf.add_bullet("Runway Centerline Markings", "Uniformly spaced stripes and gaps: stripe length plus gap length is not less than 50 m and not more than 75 m (typically 30 m stripe and 20 m gap).")
    pdf.add_bullet("Chevrons (Yellow)", "Painted on paved areas preceding threshold (blast pads, stopways) indicating area unfit for normal taxiing, take-off, or landing.")

    pdf.add_heading_1("2. Taxiway Markings & Holding Positions (Yellow)")
    pdf.add_bullet("Pattern A Holding Position", "Two solid yellow lines and two dashed yellow lines across taxiway. Solid lines on taxiway side; dashed lines on runway side. Aircraft MUST NOT cross solid lines towards runway without ATC clearance.")
    pdf.add_bullet("Pattern B Holding Position", "Ladder pattern ('railway tracks'). Critical area holding point for Category II / III operations. Aircraft holds here in Low Visibility Procedures (LVP) to protect ILS localizer/glidepath.")
    pdf.add_bullet("Intermediate Holding Position", "Single dashed yellow line across taxiway. Aircraft holds here until cleared by ground controller.")

    pdf.add_heading_1("3. Aerodrome Signs: Mandatory vs Information")
    signs_data = [
        ["Mandatory Instruction Sign", "WHITE letters on RED background", "Identifies entrance to runway, critical area, or prohibited zone (e.g. '09-27', 'NO ENTRY', 'CAT II/III'). Must not be crossed without ATC clearance."],
        ["Location Sign", "YELLOW letters on BLACK background", "Identifies the taxiway or runway where the aircraft is currently located ('Black square, you are there'). Yellow border."],
        ["Direction / Destination Sign", "BLACK letters on YELLOW background", "Indicates designation and direction of intersecting taxiways ('Yellow lead you to the fellow'). Always includes an arrow."],
        ["Runway Exit Sign", "BLACK letters on YELLOW background", "Identifies runway exit taxiway (e.g. 'B ->'). Located on same side as exit."],
        ["Aerodrome Identification Sign", "WHITE letters on any conspicuous color", "Identifies aerodrome from air (placed on hangar roof or tower)."]
    ]
    pdf.add_table(["Sign Type", "Color Scheme", "Operational Meaning & Pilot Mnemonic"], signs_data, col_widths=[140.0, 160.0, 210.0])

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Color of runway markings vs taxiway markings? -> Runway: White; Taxiway: Yellow.")
    pdf.add_bullet("Q2", "Number of threshold stripes on a 45 m wide runway? -> 12 stripes.")
    pdf.add_bullet("Q3", "Color of Mandatory Instruction signs? -> White letters on Red background.")
    pdf.add_bullet("Q4", "Color of Location signs? -> Yellow letters on Black background.")
    pdf.add_bullet("Q5", "Pattern B holding position purpose? -> Category II / III ILS critical area protection.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 19 compiled: {pdf_path}")

def build_expanded_ch20():
    pdf_path = os.path.join(BASE_DIR, "010_ch20_aerodrome_lighting.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 20: Aerodrome Lighting Systems")
    pdf.add_title_banner("Air Law", 20, "Aerodrome Lighting & PAPI Systems", "425-446")

    pdf.add_heading_1("1. Runway Lighting Colors (Master Progression)")
    lights_data = [
        ["Runway Edge Lights", "Variable WHITE", "White, EXCEPT that on instrument runways the last 600 m (or 1/3, whichever is less) are YELLOW / AMBER to warn of runway end."],
        ["Runway Threshold Lights", "GREEN", "Unbroken transverse line of green lights showing in direction of approach. May include green wing bars."],
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
    pdf.add_bullet("Simple Approach Lighting System (SALS)", "Single row of lights extending at least 420 m from threshold with a 30 m crossbar at 300 m.")
    pdf.add_bullet("Calvert Precision Approach System", "Extends 900 m from threshold with 5 crossbars at 150 m intervals. Centerline lights and side row barrettes.")
    pdf.add_bullet("Stop Bars", "Unidirectional red lights embedded across taxiway at runway holding positions. Extinguished when ATC clearance is given.")
    pdf.add_bullet("Runway Guard Lights", "Pair of flashing yellow lights (wig-wags) located at taxiway/runway intersection to warn of approaching runway.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Color of runway edge lights in last 600 m of instrument runway? -> Yellow / Amber.")
    pdf.add_bullet("Q2", "Color of runway centerline lights in final 300 m? -> Red.")
    pdf.add_bullet("Q3", "PAPI indication when on glidepath? -> 2 White, 2 Red.")
    pdf.add_bullet("Q4", "Color of taxiway edge lights? -> Blue.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 20 compiled: {pdf_path}")

def build_expanded_ch21():
    pdf_path = os.path.join(BASE_DIR, "010_ch21_obstacle_marking_services.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 21: Obstacles & Aerodrome Services")
    pdf.add_title_banner("Air Law", 21, "Obstacles & Rescue Services (RFFS)", "447-460")

    pdf.add_heading_1("1. Rescue and Fire Fighting Services (RFFS Categories 1 to 10)")
    pdf.add_paragraph(
        "RFFS category is determined by the overall length of the longest aeroplane using the aerodrome and its maximum fuselage width:",
        max_chars=92
    )

    rffs_data = [
        ["Category 1", "0 m up to 9 m", "2 m", "Light singles (C152, PA-28)"],
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
    pdf.add_bullet("Principal Agents", "Water and foam meeting performance level A, B, or C. Level B and C foams have higher extinction efficiency.")
    pdf.add_bullet("Complementary Agents", "Dry chemical powders or CO2. Rapid knock-down capability.")

    pdf.add_heading_1("3. Obstacle Lighting Classification")
    pdf.add_bullet("Low-Intensity", "Fixed RED lights for obstacles with height less than 45 m.")
    pdf.add_bullet("Medium-Intensity", "Flashing RED or flashing WHITE lights for obstacles between 45 m and 150 m.")
    pdf.add_bullet("High-Intensity", "Flashing WHITE lights for obstacles exceeding 150 m height (operates day and night).")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "RFFS Category for A320/B737? -> Category 7.")
    pdf.add_bullet("Q2", "RFFS Category for A380? -> Category 10.")
    pdf.add_bullet("Q3", "Maximum allowable RFFS response time? -> 3 minutes (optimum 2 minutes).")
    pdf.add_bullet("Q4", "Obstacle lights for obstacles > 150 m? -> High-intensity flashing white.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 21 compiled: {pdf_path}")

def build_expanded_ch22():
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

    pdf.add_heading_1("3. Inadmissible Persons & Deportees")
    pdf.add_bullet("Inadmissible Person", "A person who is or will be refused admission to a State by its authorities. The OPERATOR that transported the person is responsible for returning them to where they boarded or to their home state.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which Annex deals with Facilitation? -> Annex 9.")
    pdf.add_bullet("Q2", "Who signs the General Declaration? -> Pilot-in-Command or authorized agent.")
    pdf.add_bullet("Q3", "Who is responsible for custody and return of inadmissible passengers? -> The operator that transported them.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 22 compiled: {pdf_path}")

def build_expanded_ch23():
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
    pdf.add_bullet("Expanding Square Search", "Used when location of distress is known within close limits (concentric expanding squares).")
    pdf.add_bullet("Sector Search", "Used when position of target is known with high precision (star-shaped sector pattern).")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Ground symbol 'V'? -> Require assistance.")
    pdf.add_bullet("Q2", "Ground symbol 'X'? -> Require medical assistance.")
    pdf.add_bullet("Q3", "Day acknowledgement signal from aircraft? -> Rocking wings.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 23 compiled: {pdf_path}")

def build_expanded_ch24():
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

    pdf.add_heading_1("3. Disruptive / Unruly Passengers (4 Levels)")
    pdf.add_bullet("Level 1 (Disruptive)", "Verbal harassment, refusal to follow crew safety instructions.")
    pdf.add_bullet("Level 2 (Physically Abusive)", "Physical contact with crew or passengers, damage to aircraft property.")
    pdf.add_bullet("Level 3 (Life-Threatening)", "Display or threat of weapon, credible threat of severe bodily harm.")
    pdf.add_bullet("Level 4 (Attempted Breach of Flight Deck)", "Attempted unauthorized entry into flight deck. Maximum emergency response.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which Annex deals with Security? -> Annex 17.")
    pdf.add_bullet("Q2", "When must cockpit door be locked? -> From doors closed after embarkation until disembarkation.")
    pdf.add_bullet("Q3", "Which level of unruly passenger involves attempted cockpit breach? -> Level 4.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 24 compiled: {pdf_path}")

def build_expanded_ch25():
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

    pdf.add_heading_1("3. State Responsibilities & Protection of Records")
    pdf.add_bullet("Investigation Responsibility", "The State of OCCURRENCE institutes the inquiry.")
    pdf.add_bullet("Accredited Representatives", "State of Registry, State of Operator, State of Design, and State of Manufacture are entitled to appoint an Accredited Representative.")
    pdf.add_bullet("Non-Disclosure of Records", "Cockpit voice recordings (CVR), witness statements, and personal medical information must NOT be made available for purposes other than accident investigation (e.g. criminal liability).")
    pdf.add_bullet("Final Report Target", "The State conducting investigation shall release Final Report as soon as possible, ideally within 12 MONTHS.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which Annex covers Accident Investigation? -> Annex 13.")
    pdf.add_bullet("Q2", "Sole objective of an accident investigation? -> Prevention of accidents (NOT blame or liability).")
    pdf.add_bullet("Q3", "Are CVR recordings admissible for criminal prosecution? -> NO, strictly protected.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 25 compiled: {pdf_path}")

def run_all_expanded():
    print("Building expanded Chapters 1 to 5...")
    build_ch01()
    build_ch02()
    build_ch03()
    build_ch04()
    build_ch05()

    print("Building expanded Chapters 6 to 10...")
    build_ch06()
    build_ch07()
    build_ch08()
    build_ch09()
    build_ch10()

    print("Building expanded Chapters 11 to 16...")
    build_ch11()
    build_ch12()
    build_ch13()
    build_ch14()
    build_ch15()
    build_ch16()

    print("Building expanded Chapters 17 to 25...")
    build_expanded_ch17()
    build_expanded_ch18()
    build_expanded_ch19()
    build_expanded_ch20()
    build_expanded_ch21()
    build_expanded_ch22()
    build_expanded_ch23()
    build_expanded_ch24()
    build_expanded_ch25()

if __name__ == "__main__":
    run_all_expanded()
