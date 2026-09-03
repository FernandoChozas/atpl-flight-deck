#!/usr/bin/env python3
"""
Full-Depth Study Manual Generator - Volume 4 (Chapters 19 to 25).
Designed for 100% self-contained study.
Target: ~18 to 22 pages total across Chapters 19 to 25.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

# ==============================================================================
# CHAPTER 19: VISUAL AIDS - MARKINGS AND SIGNS (~3 pages)
# ==============================================================================
def build_ch19():
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

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch19 = [
        ("Q1: How many stripes are displayed on a runway threshold marking for a 45 m wide runway?",
         "[A] 8\n[B] 12\n[C] 16\n[D] 6",
         "CORRECT: [B]. A 45 m runway has 12 stripes (30 m has 8; 60 m has 16). Formula: Stripes = Width x 4 / 15."),
        ("Q2: What visual appearance designates a mandatory instruction sign at an aerodrome?",
         "[A] Yellow inscription on black background\n[B] Black inscription on yellow background\n[C] White inscription on red background\n[D] White inscription on green background",
         "CORRECT: [C]. Mandatory instruction signs (e.g. STOP, NO ENTRY, runway designations) have WHITE text on a RED background."),
        ("Q3: What marking identifies an unserviceable portion of a runway or taxiway?",
         "[A] A single yellow diagonal line\n[B] A white or yellow cross (X)\n[C] A red circle\n[D] A dashed white box",
         "CORRECT: [B]. Unserviceable areas are marked with crosses (white on runways, yellow on taxiways)."),
        ("Q4: What color is used for taxiway centerline markings?",
         "[A] White\n[B] Yellow\n[C] Red\n[D] Blue",
         "CORRECT: [B]. All taxiway markings, holding lines, and guidance lines are YELLOW (runway markings are white)."),
        ("Q5: What visual appearance designates a location sign (identifying the taxiway or runway on which the aircraft is located)?",
         "[A] Yellow text on black background with yellow border\n[B] Black text on yellow background\n[C] White text on red background\n[D] White text on green background",
         "CORRECT: [A]. Location signs display YELLOW text on a BLACK background with a yellow border ('Yellow on black is where you're at; Black on yellow is where to go')."),
        ("Q6: What is the meaning of a runway-holding position marking consisting of two continuous yellow lines and two dashed yellow lines (Pattern A)?",
         "[A] Intermediate holding position on apron\n[B] Mandatory runway-holding position: when approaching from continuous lines, MUST NOT cross without ATC clearance\n[C] Road-holding position for ground vehicles\n[D] De-icing entry line",
         "CORRECT: [B]. Pattern 'A' runway-holding position consists of two continuous lines on taxiway side and two dashed lines on runway side. An aircraft approaching from the continuous side must stop.")
    ]
    for q_text, opts, exp in questions_ch19:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 19 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 20: AERODROME LIGHTING (~3 pages)
# ==============================================================================
def build_ch20():
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

    pdf.add_heading_1("3. Visual Approach Slope Indicators (VASIS & 3-BAR VASIS)")
    vasis_data = [
        ["Standard VASIS (2-Bar)", "Upwind and downwind bars. Standard 3° glidepath. Red over White = On slope; Red over Red = Low; White over White = High."],
        ["3-Bar VASIS", "Developed for wide-body aircraft with large eye-to-wheel height (e.g. B747). Uses middle bar as common bar. Flight crew of large aircraft fly upper glidepath (Bar 2 and 3)."],
        ["T-VASIS", "T-shaped light arrays on both sides of runway. Inverted 'T' indicates fly down (high); upright 'T' indicates fly up (low)."]
    ]
    pdf.add_table(["System Type", "Visual Display Geometry & Pilot Guidance"], vasis_data, col_widths=[140.0, 370.0])

    pdf.add_heading_1("4. Approach Lighting Systems (ALS)")
    pdf.add_bullet("Simple Approach Lighting System (SALS)", "Single row of lights extending at least 420 m from threshold with a 30 m crossbar at 300 m.")
    pdf.add_bullet("Calvert Precision Approach System", "Extends 900 m from threshold with 5 crossbars at 150 m intervals. Centerline lights and side row barrettes.")
    pdf.add_bullet("Stop Bars", "Unidirectional red lights embedded across taxiway at runway holding positions. Extinguished when ATC clearance is given.")
    pdf.add_bullet("Runway Guard Lights", "Pair of flashing yellow lights (wig-wags) located at taxiway/runway intersection to warn of approaching runway.")

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch20 = [
        ("Q1: What color are runway centerline lights in the final 300 m of the runway?",
         "[A] Alternate red and white\n[B] White\n[C] Red\n[D] Yellow",
         "CORRECT: [C]. Centerline lights are white to 900 m, alternate red/white from 900 m to 300 m, and all RED for the final 300 m."),
        ("Q2: What is the PAPI indication for an aircraft on the correct glidepath?",
         "[A] 3 white and 1 red\n[B] 2 white and 2 red\n[C] 4 white\n[D] 1 white and 3 red",
         "CORRECT: [B]. Two red and two white indicates the aircraft is on the 3.0° glidepath."),
        ("Q3: What color are runway edge lights in the last 600 m of a precision instrument runway?",
         "[A] Red\n[B] Yellow / Amber\n[C] Green\n[D] Blue",
         "CORRECT: [B]. The last 600 m (or one third of runway length) of edge lights are yellow to warn of approaching runway end."),
        ("Q4: What color are taxiway edge lights and taxiway centerline lights?",
         "[A] White edge and green centerline\n[B] Blue edge and green centerline\n[C] Yellow edge and blue centerline\n[D] Green edge and white centerline",
         "CORRECT: [B]. Under Annex 14, taxiway edge lights are blue and centerline lights are green."),
        ("Q5: What does a red stop bar light embedded across a taxiway indicate to a pilot?",
         "[A] Proceed with caution\n[B] Runway holding position: MUST NOT CROSS until light is extinguished by ATC\n[C] Rapid exit taxiway\n[D] De-icing pad entrance",
         "CORRECT: [B]. An illuminated red stop bar is an absolute stop signal. Never cross an active red stop bar, even if verbal clearance was received."),
        ("Q6: On a precision instrument runway, what color are Touchdown Zone (TDZ) lights and how far do they extend?",
         "[A] Green lights extending 300 m\n[B] White barrettes extending from threshold for 900 m (or midpoint of runway)\n[C] Alternating yellow and red lights for 600 m\n[D] Blue lights for 1,200 m",
         "CORRECT: [B]. TDZ lights consist of white barrettes extending from the threshold for 900 m (or to runway midpoint, whichever is less).")
    ]
    for q_text, opts, exp in questions_ch20:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 20 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 21: OBSTACLES & AERODROME SERVICES (RFFS) (~3 pages)
# ==============================================================================
def build_ch21():
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
        "RFFS Operational Response Time (AviationExam Core)",
        "• Operational Objective: The operational objective of the RFFS is to achieve a response time of TWO (2) MINUTES "
        "to any point of each operational runway, and not exceeding THREE (3) MINUTES to any other part of the movement area.\n"
        "• Response Time Definition: The time between the initial call to the RFFS and the first responding vehicle(s) "
        "applying foam at the required rate.",
        max_chars=86
    )

    pdf.add_heading_1("2. Extinguishing Agent Quantities & Discharge Rates")
    pdf.add_paragraph(
        "Annex 14 specifies minimum amounts of usable water for foam production and discharge rates:\n"
        "• Category 6: 7,900 liters of water (Level B foam), discharge rate 4,000 L/min, complementary agent 225 kg.\n"
        "• Category 7: 12,100 liters of water (Level B foam), discharge rate 5,300 L/min, complementary agent 225 kg.\n"
        "• Category 9: 24,300 liters of water (Level B foam), discharge rate 9,000 L/min, complementary agent 450 kg.",
        max_chars=92
    )

    pdf.add_heading_1("3. Obstacle Marking & Lighting Standards")
    pdf.add_bullet("Marking Colors", "Fixed obstacles must be colored in a chequered pattern (orange/white or red/white) or alternating contrasting horizontal bands (at least 7 bands of orange/white or red/white).")
    pdf.add_bullet("Low-Intensity Lights", "Fixed red lights used for obstacles with height less than 45 m.")
    pdf.add_bullet("Medium-Intensity Lights", "Flashing red or flashing white lights used for obstacles between 45 m and 150 m.")
    pdf.add_bullet("High-Intensity Lights", "Flashing white lights (up to 200,000 cd day, 2,000 cd night) used for obstacles exceeding 150 m height (e.g. broadcast masts, tall cooling towers).")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch21 = [
        ("Q1: What is the maximum acceptable RFFS response time to any point of an operational runway in optimum conditions?",
         "[A] 1 minute\n[B] 2 minutes (not exceeding 3 minutes to other movement areas)\n[C] 4 minutes\n[D] 5 minutes",
         "CORRECT: [B]. The operational objective is 2 minutes to runway points, and max 3 minutes to any movement area."),
        ("Q2: Which RFFS category applies to an Airbus A320 with an overall length of 37.6 m and fuselage width of 3.95 m?",
         "[A] Category 5\n[B] Category 6\n[C] Category 7\n[D] Category 8",
         "CORRECT: [B]. Length 28 to 39 m with width up to 5 m corresponds to RFFS Category 6 (B737-800 is Cat 7 if length exceeds 39 m)."),
        ("Q3: What type of lighting is required on obstacles exceeding 150 m in height?",
         "[A] Low-intensity fixed red lights\n[B] Medium-intensity flashing red lights\n[C] High-intensity flashing white lights\n[D] Green strobe lights",
         "CORRECT: [C]. Annex 14 mandates high-intensity flashing white lights for obstacles taller than 150 m."),
        ("Q4: What is the principal extinguishing agent required for aerodrome rescue and fire fighting?",
         "[A] CO2 gas\n[B] Dry chemical powder\n[C] Water with foam-producing chemical (AFFF)\n[D] Halon 1301",
         "CORRECT: [C]. Foam produced from water and film-forming fluoroprotein or aqueous film-forming foam (AFFF) is the primary agent."),
        ("Q5: What minimum amount of complementary dry chemical powder is required for RFFS Category 7?",
         "[A] 100 kg\n[B] 225 kg\n[C] 450 kg\n[D] 900 kg",
         "CORRECT: [B]. Under Annex 14, Category 6 and 7 aerodromes require at least 225 kg of complementary dry chemical powder or gaseous agent."),
        ("Q6: What visual markings are required on service vehicles authorized to operate on aerodrome movement areas?",
         "[A] Conspicuous single yellow or orange color, or display flashing yellow beacons\n[B] Plain white with red stripes\n[C] Military camouflage\n[D] Blue flashing lights only",
         "CORRECT: [A]. Movement area service vehicles must be colored conspicuously (yellow/orange) and display flashing yellow obstacle beacons.")
    ]
    for q_text, opts, exp in questions_ch21:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 21 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 22: FACILITATION (ANNEX 9) (~2 pages)
# ==============================================================================
def build_ch22():
    pdf_path = os.path.join(BASE_DIR, "010_ch22_facilitation.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 22: Facilitation (ICAO Annex 9)")
    pdf.add_title_banner("Air Law", 22, "Facilitation (Annex 9)", "461-470")

    pdf.add_heading_1("1. Purpose & Core Documents (Annex 9)")
    pdf.add_paragraph(
        "Annex 9 aims to prevent unnecessary delays to aircraft, crews, passengers, and cargo, especially in the "
        "administration of customs, immigration, quarantine, and health clearance procedures.",
        max_chars=92
    )

    pdf.add_bullet("General Declaration (GenDec)", "The basic document of entry and departure for an aircraft, signed by pilot-in-command or authorized agent, reporting aircraft registration, flight routing, number of crew and passengers, and public health declaration.")
    pdf.add_bullet("Passenger Manifest", "List of passenger names, embarkation points, and disembarkation points. Contracting States shall not require passenger manifests where automated systems exist.")
    pdf.add_bullet("Cargo Manifest", "Commercial document detailing air waybill numbers, nature of goods, packages, and destination.")
    pdf.add_bullet("Crew Member Certificate (CMC)", "Standardized identification card issued to operating crew members to facilitate entry without visa during layover.")

    pdf.add_heading_1("2. Inadmissible Persons vs Deportees")
    pdf.add_bullet("Inadmissible Person", "A person who is or will be refused admission to a State by its authorities (e.g. expired visa, fraudulent passport). The OPERATOR that transported the person is legally responsible for their custody and return transportation to their point of embarkation.")
    pdf.add_bullet("Deportee", "A person who had legally entered a State but is formally ordered to leave by government authorities. The State ordering deportation is responsible for custody and arranging transit.")

    pdf.add_heading_1("3. Aircraft Disinsection & Public Health")
    pdf.add_paragraph(
        "Disinsection of aircraft cabins and flight decks is carried out to prevent the spread of mosquito-borne diseases "
        "(e.g. malaria, dengue). Permitted methods under WHO/ICAO include disinsection on arrival, pre-flight and top-of-descent "
        "spraying, or residual insecticide treatment.",
        max_chars=92
    )

    pdf.add_heading_1("4. Facilitation of Air Cargo & Transit Passengers")
    pdf.add_bullet("Direct Transit", "Contracting States shall ensure that passengers in direct airside transit without leaving the airport international transit area are not required to hold transit visas, except under special national security declarations.")
    pdf.add_bullet("Air Cargo Clearance", "Customs clearance for standard air cargo shall be completed as soon as possible and in any event within 4 hours of arrival, utilizing electronic data interchange (EDI).")

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch22 = [
        ("Q1: Who is financially and operationally responsible for removing an inadmissible passenger from a State?",
         "[A] The passenger's country of nationality\n[B] The State of destination\n[C] The aircraft operator that carried the passenger\n[D] ICAO Facilitation Fund",
         "CORRECT: [C]. Under Annex 9, the operator that transported an inadmissible person is responsible for transporting them back to point of origin."),
        ("Q2: What is the primary purpose of the General Declaration (GenDec)?",
         "[A] Flight plan filing with ATC\n[B] Aircraft entry and clearance document for customs, immigration, and public health\n[C] Weight and balance calculation\n[D] Continuing airworthiness tracking",
         "CORRECT: [B]. The GenDec is the official clearance document for customs, immigration, and public health."),
        ("Q3: What document permits operating flight crew members visa-free temporary entry during international layovers?",
         "[A] Student pilot licence\n[B] Crew Member Certificate (CMC)\n[C] Part-MED certificate\n[D] Operator flight release",
         "CORRECT: [B]. The Crew Member Certificate (CMC) facilitates temporary visa-free entry for active crew during layovers."),
        ("Q4: Are transit passengers remaining in the airport international transit area required to obtain transit visas under standard ICAO facilitation rules?",
         "[A] Yes, always\n[B] No, Contracting States shall not require transit visas for direct transit passengers\n[C] Only for stays exceeding 2 hours\n[D] Yes, if arriving from outside Europe",
         "CORRECT: [B]. Under Annex 9, direct transit passengers remaining airside do not require visas."),
        ("Q5: What is the primary purpose of the Health section in the General Declaration?",
         "[A] Reporting crew duty time\n[B] Declaring on-board health conditions, disinsection, and any illness before landing\n[C] Verifying passenger vaccine records only\n[D] Registering dangerous goods cargo",
         "CORRECT: [B]. The health section of the GenDec reports details of any illness on board and disinsection carried out during flight."),
        ("Q6: How long may an operating flight crew member stay in a State without a visa using a Crew Member Certificate (CMC)?",
         "[A] 24 hours only\n[B] For the duration of the scheduled layover / turn-around\n[C] 30 days\n[D] Visas are always required for flight crew",
         "CORRECT: [B]. The CMC allows operating crew to remain visa-free for the scheduled layover period until their next departure flight.")
    ]
    for q_text, opts, exp in questions_ch22:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 22 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 23: SEARCH AND RESCUE (ANNEX 12) (~3 pages)
# ==============================================================================
def build_ch23():
    pdf_path = os.path.join(BASE_DIR, "010_ch23_sar.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 23: Search and Rescue (ICAO Annex 12)")
    pdf.add_title_banner("Air Law", 23, "Search and Rescue (Annex 12)", "471-482")

    pdf.add_heading_1("1. SAR Organization & Rescue Coordination Centres (RCC)")
    pdf.add_paragraph(
        "ICAO Annex 12 mandates that Contracting States establish Search and Rescue Services on a 24-hour basis. "
        "A Rescue Coordination Centre (RCC) is established in each Search and Rescue Region (SRR) to direct SAR operations.",
        max_chars=92
    )

    pdf.add_heading_1("2. Ground-Air Visual Signal Code for Survivors")
    pdf.add_paragraph(
        "Ground signals made by survivors to search aircraft using fabric strips, wood, or trodden snow:",
        max_chars=92
    )

    signals_data = [
        ["V", "Require assistance"],
        ["X", "Require medical assistance"],
        ["N", "NO or Negative"],
        ["Y", "YES or Affirmative"],
        ["-> (Arrow)", "Proceeding in this direction"],
        ["LL", "All well / All survivors located"],
        ["JL", "Operation completed"]
    ]
    pdf.add_table(["Visual Symbol", "Meaning to Search Aircraft (Annex 12 Appendix 1)"], signals_data, col_widths=[140.0, 370.0])

    pdf.add_callout(
        "trap",
        "Search Aircraft Acknowledgment Signals",
        "When a search aircraft observes survivor ground signals:\n"
        "• DAY: Rocking wings (for aeroplanes) or flashing landing lights twice (for helicopters).\n"
        "• NIGHT: Flashing landing lights or navigation lights TWICE.\n"
        "• If signal NOT understood: Aeroplane completes a 360° turn to the right, or displays red pyrotechnics.",
        max_chars=86
    )

    pdf.add_heading_1("3. Droppable Emergency Equipment Color Streamers")
    pdf.add_paragraph(
        "Containers or packages containing survival equipment dropped to survivors are indicated by colored streamers:\n"
        "• RED: Medical supplies and first aid equipment.\n"
        "• BLUE: Food and water.\n"
        "• YELLOW: Blankets and protective clothing.\n"
        "• BLACK: Miscellaneous survival equipment (knives, compasses, cooking equipment).",
        max_chars=92
    )

    pdf.add_heading_1("4. Emergency Locator Transmitter (ELT) Frequencies")
    pdf.add_paragraph(
        "• 406.0 MHz: Digital satellite frequency monitored by COSPAS-SARSAT satellite constellation. Transmits unique 24-bit aircraft hex code for instant identification.\n"
        "• 121.5 MHz: VHF civilian emergency frequency used for terminal acoustic/radio homing by rescue aircraft.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch23 = [
        ("Q1: What does the ground-air survivor symbol 'X' signify to search aircraft?",
         "[A] Require assistance\n[B] Require medical assistance\n[C] No or Negative\n[D] Aircraft destroyed",
         "CORRECT: [B]. The single 'V' means 'Require assistance'; the 'X' means 'Require medical assistance'."),
        ("Q2: How does a search aeroplane acknowledge that survivor ground signals have been seen and understood during daylight?",
         "[A] Firing a red flare\n[B] Rocking wings\n[C] Circling to the right 360°\n[D] Pitching nose up and down",
         "CORRECT: [B]. Rocking wings by day (or flashing lights twice at night) confirms signals are understood."),
        ("Q3: Which satellite frequency is used by modern ELTs for global satellite alerting through COSPAS-SARSAT?",
         "[A] 121.5 MHz\n[B] 243.0 MHz\n[C] 406.0 MHz\n[D] 1090 MHz",
         "CORRECT: [C]. 406.0 MHz is the digital satellite beacon frequency (121.5 MHz is for VHF homing)."),
        ("Q4: What color streamer indicates that a dropped survival package contains food and water?",
         "[A] Red\n[B] Blue\n[C] Yellow\n[D] Black",
         "CORRECT: [B]. Under Annex 12, Blue denotes food and water (Red = medical, Yellow = blankets/clothing, Black = miscellaneous)."),
        ("Q5: What does the ground-air visual signal 'LL' signify?",
         "[A] Require food and water\n[B] All well\n[C] Land here\n[D] Lost direction",
         "CORRECT: [B]. 'LL' indicates 'All well'."),
        ("Q6: What is the international military UHF aeronautical emergency frequency monitored by SAR units?",
         "[A] 121.5 MHz\n[B] 243.0 MHz\n[C] 406.0 MHz\n[D] 1090 MHz",
         "CORRECT: [B]. 243.0 MHz is the international UHF military aeronautical emergency frequency."),
        ("Q7: What does the ground-air survivor visual symbol 'V' signify to search aircraft?",
         "[A] Require medical assistance\n[B] Require assistance\n[C] All well\n[D] Operation completed",
         "CORRECT: [B]. Single 'V' signifies 'Require assistance' ('X' is require medical assistance; 'LL' is all well).")
    ]
    for q_text, opts, exp in questions_ch23:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 23 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 24: SECURITY (ICAO ANNEX 17) (~3 pages)
# ==============================================================================
def build_ch24():
    pdf_path = os.path.join(BASE_DIR, "010_ch24_security.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 24: Aviation Security (ICAO Annex 17)")
    pdf.add_title_banner("Air Law", 24, "Security & Unlawful Interference", "483-492")

    pdf.add_heading_1("1. Security Architecture & Objectives")
    pdf.add_paragraph(
        "Annex 17 establishes Standards and Recommended Practices to safeguard international civil aviation against "
        "acts of unlawful interference. Each Contracting State must designate an appropriate authority for civil aviation security.",
        max_chars=92
    )

    pdf.add_bullet("Security Restricted Area (SRA)", "Airside areas where access is controlled to ensure civil aviation security (e.g. passenger boarding areas, baggage sorting areas, aprons). All persons and vehicles are screened 100%.")
    pdf.add_bullet("100% Hold Baggage Screening", "All originating hold baggage must be screened prior to being loaded onto commercial aircraft.")
    pdf.add_bullet("Flight Deck Security Door", "On commercial aeroplanes with MTOM > 54,000 kg or passenger seating > 19, the flight crew compartment door must be capable of being locked from the inside and resist small arms fire and grenade shrapnel.")

    pdf.add_heading_1("2. Unruly Passenger Threat Levels (ICAO Doc 9811)")
    pdf.add_bullet("Level 1: Disruptive Behavior", "Verbal abuse, failure to follow crew instructions, non-violent disruptive conduct.")
    pdf.add_bullet("Level 2: Physically Abusive Behavior", "Physical contact, pushing, shoving, kicking, damage to cabin property.")
    pdf.add_bullet("Level 3: Life-Threatening Behavior", "Display or threat of weapons, credible terroristic threat, direct physical injury.")
    pdf.add_bullet("Level 4: Attempted / Actual Flight Deck Breach", "Attempt to force cockpit entry, hijack attempt, sabotage.")

    pdf.add_heading_1("3. In-Flight Security Officers (Sky Marshals)")
    pdf.add_paragraph(
        "Under Annex 17, the deployment of In-Flight Security Officers (IFSOs) shall be subject to bilateral agreement "
        "between the States involved. When deployed, IFSOs are government personnel authorized to carry firearms on board. "
        "The Pilot-in-Command retains ultimate command of the aircraft, but the IFSO operates in accordance with their national mandate.",
        max_chars=92
    )

    pdf.add_heading_1("4. Regulated Agents & Air Cargo Security")
    pdf.add_paragraph(
        "A Regulated Agent (RA) is an agent, freight forwarder, or entity that conducts business with an operator "
        "and applies security controls accepted by the competent authority. Cargo from a regulated agent or known consignor "
        "maintains secure chain of custody and may be loaded without duplicate screening.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch24 = [
        ("Q1: Which aircraft are required to have an armored, lockable flight deck security door under Annex 6/17?",
         "[A] All commercial aircraft without exception\n[B] Aeroplanes with MTOM > 5,700 kg only\n[C] Passenger aeroplanes with MTOM > 54,000 kg or seating capacity > 19 passengers\n[D] Multi-engine turboprops only",
         "CORRECT: [C]. Armored, bullet-resistant lockable cockpit doors are required on passenger aeroplanes exceeding 54,000 kg MTOM or more than 19 passenger seats."),
        ("Q2: Under ICAO threat classifications, what level corresponds to an attempted cockpit breach?",
         "[A] Level 1\n[B] Level 2\n[C] Level 3\n[D] Level 4",
         "CORRECT: [D]. Level 4 is the highest threat level, denoting an attempted or actual breach of the flight crew compartment."),
        ("Q3: What transponder code must be squawked in the event of unlawful interference (hijack)?",
         "[A] 7000\n[B] 7500\n[C] 7600\n[D] 7700",
         "CORRECT: [B]. Squawk Mode A Code 7500 denotes hijacking / unlawful interference."),
        ("Q4: What is the legal status of In-Flight Security Officers (IFSOs) on international commercial flights?",
         "[A] Permitted on all flights without prior notification\n[B] Permitted only with mutual agreement between the State of the Operator and the State of destination\n[C] Strictly prohibited by ICAO\n[D] Mandatory on all flights over 5 hours",
         "CORRECT: [B]. Annex 17 mandates that deployment of armed security officers is subject to bilateral agreement between States."),
        ("Q5: What is a 'Regulated Agent' in the context of aviation security under Annex 17?",
         "[A] An armed police officer at the airport\n[B] An agent, freight forwarder, or entity that conducts business with an operator and applies security controls accepted by the competent authority\n[C] A customs broker\n[D] An airline ticketing manager",
         "CORRECT: [B]. A Regulated Agent is an entity authorized to apply approved security screening and chain-of-custody controls to air cargo."),
        ("Q6: Which international convention was the first to address offenses and certain other acts committed on board aircraft?",
         "[A] Tokyo Convention (1963)\n[B] Hague Convention (1970)\n[C] Montreal Convention (1971)\n[D] Rome Convention (1952)",
         "CORRECT: [A]. The Tokyo Convention of 1963 was the first international convention establishing jurisdiction and powers of the aircraft commander over offenses on board."),
        ("Q7: What is the primary focus of the 1971 Montreal Convention regarding aviation safety?",
         "[A] Economic regulation of air fares\n[B] Suppression of unlawful acts against the safety of civil aviation (sabotage, explosive devices, and damaging facilities)\n[C] Suppression of unlawful seizure of aircraft (hijacking)\n[D] Carrier liability for lost baggage",
         "CORRECT: [B]. The Montreal Convention of 1971 covers acts of sabotage, damage to air navigation facilities, and placing destructive devices (the Hague Convention of 1970 covers hijacking).")
    ]
    for q_text, opts, exp in questions_ch24:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 24 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 25: AIRCRAFT ACCIDENT & INCIDENT INVESTIGATION (~3 pages)
# ==============================================================================
def build_ch25():
    pdf_path = os.path.join(BASE_DIR, "010_ch25_accident_investigation.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 25: Aircraft Accident Investigation")
    pdf.add_title_banner("Air Law", 25, "Accident Investigation (Annex 13)", "493-506")

    pdf.add_heading_1("1. Accident vs Serious Incident vs Incident (Annex 13)")
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
    pdf.add_bullet("Fatal Injury", "An injury resulting in death within 30 DAYS of the date of the accident.")
    pdf.add_bullet("Serious Injury", "An injury requiring hospitalization > 48 hours within 7 days; fracture of bone (except simple fingers/toes/nose); lacerations causing severe hemorrhage; internal organ damage; or 2nd/3rd degree burns over > 5% of body surface.")
    pdf.add_bullet("Serious Incident", "An incident involving circumstances indicating that there was a high probability of an accident (e.g. near collision requiring evasive maneuver, landing on taxiway, uncontained engine failure).")

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

    pdf.add_heading_1("4. Flight Data & Cockpit Voice Recorders (Preservation)")
    pdf.add_paragraph(
        "• Flight Data Recorder (FDR): Must record parameters for at least the preceding 25 HOURS of operation.\n"
        "• Cockpit Voice Recorder (CVR): Must retain information recorded during at least the last 2 HOURS (increased to 25 hours for newly manufactured large aeroplanes).\n"
        "• In the event of an accident or serious incident, the operator must PRESERVE all original recorded data without erasure.",
        max_chars=92
    )

    pdf.add_heading_1("5. Mandatory Occurrence Reporting (EU No 376/2014)")
    pdf.add_paragraph(
        "Under Regulation (EU) No 376/2014, any occurrence which may represent a significant risk to aviation safety "
        "must be reported by the flight crew, operator, or ATS provider to the competent authority within 72 HOURS "
        "of becoming aware of the occurrence.",
        max_chars=92
    )

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch25 = [
        ("Q1: What is the sole objective of an aircraft accident investigation under ICAO Annex 13?",
         "[A] To determine who is legally liable\n[B] The prevention of accidents and incidents\n[C] To assist insurance claims settlement\n[D] To penalize regulatory violations",
         "CORRECT: [B]. The sole objective under Annex 13 is explicitly the prevention of accidents and incidents, NOT to apportion blame or liability."),
        ("Q2: Under Annex 13, a fatal injury is defined as an injury resulting in death within how many days?",
         "[A] 7 days\n[B] 14 days\n[C] 30 days\n[D] 60 days",
         "CORRECT: [C]. A fatal injury is one resulting in death within 30 days of the accident."),
        ("Q3: Are Cockpit Voice Recorder (CVR) recordings allowed to be used for criminal prosecution of the crew?",
         "[A] Yes, without restriction\n[B] NO, CVR recordings are strictly protected from disclosure for non-investigative purposes\n[C] Only if requested by the airline\n[D] Only in fatal accidents",
         "CORRECT: [B]. Annex 13 strictly protects CVR recordings from disclosure for purposes other than accident investigation."),
        ("Q4: What is the minimum recording duration of a Flight Data Recorder (FDR) on commercial air transport aeroplanes?",
         "[A] 2 hours\n[B] 10 hours\n[C] 25 hours\n[D] 60 days",
         "CORRECT: [C]. Under ICAO Annex 6 and Part-CAT, modern FDRs must retain data for at least 25 hours."),
        ("Q5: Under Regulation (EU) No 376/2014, within how many hours must a mandatory safety occurrence report be submitted?",
         "[A] 24 hours\n[B] 48 hours\n[C] 72 hours\n[D] 7 days",
         "CORRECT: [C]. Mandatory safety occurrences must be reported within 72 hours of becoming aware of the occurrence."),
        ("Q6: Which State has the primary responsibility to institute and conduct an aircraft accident investigation under Annex 13?",
         "[A] The State of Registry\n[B] The State of the Operator\n[C] The State of Occurrence\n[D] The State of Manufacture",
         "CORRECT: [C]. Under Annex 13, the State of Occurrence is responsible for instituting and conducting the investigation.")
    ]
    for q_text, opts, exp in questions_ch25:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 25 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch19()
    build_ch20()
    build_ch21()
    build_ch22()
    build_ch23()
    build_ch24()
    build_ch25()

