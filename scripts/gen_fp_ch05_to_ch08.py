#!/usr/bin/env python3
"""
Generator for Subject 033: Flight Planning and Monitoring
Volume 2: Chapters 5 to 8
- Chapter 5: Jeppesen En-Route Charts, Airway Dimensions & Altitudes (MEA, MOCA, MORA)
- Chapter 6: Standard Departures (SID), Arrivals (STAR) & Holding Pattern Entries
- Chapter 7: Meteorological Planning Charts (WINTEM & SIGWX Tropopause/Jets)
- Chapter 8: In-Flight Fuel Monitoring, Bogey Curves & Decision Point Procedure (DPP)

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Flight Planning and EASA AIR-OPS regulations.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_3/033_flight_planning_monitoring"

def build_fp_ch05():
    pdf_path = os.path.join(OUTPUT_DIR, "033_ch05_jeppesen_enroute_charts_airspace.pdf")
    pdf = PDFBuilder("Flight Planning", "033", "Chapter 5: Jeppesen Charts & Airways")

    pdf.add_title_banner(
        "Flight Planning",
        5,
        "Jeppesen En-Route Charts & Airway Dimensions",
        "165-208"
    )

    pdf.add_heading_1("1. Airway Altitudes & Definitions on Jeppesen Charts")
    pdf.add_paragraph(
        "Airways on IFR en-route charts (LO and HI) are published with exact altitude constraints ensuring terrain clearance and radio reception:"
    )

    alt_table = [
        ["Altitude Type Code", "Jeppesen Representation & Meaning", "Guaranteed Protection (Terrain vs Signal)"],
        ["MEA (Minimum En-route Alt)", "Printed as bold number (e.g. 8000). Lowest published altitude between fixes.", "Guarantees BOTH acceptable navigational signal reception AND mandatory obstacle clearance."],
        ["MOCA (Min Obstacle Clr Alt)", "Printed with an asterisk * (e.g. *4500).", "Guarantees obstacle clearance along entire airway, but signal reception ONLY within 22 NM of VOR!"],
        ["MORA (Route MORA)", "Printed with an 'a' (e.g. 7200a).", "Guarantees obstacle clearance within 10 NM of airway centerline, regardless of route width."],
        ["Grid MORA", "Large bold numbers inside each latitude/longitude quadrangle (e.g. 64 = 6,400 ft).", "Clears all terrain/structures in the quadrangle by 1,000 ft (areas <= 5,000 ft) or by 2,000 ft in mountainous areas."],
        ["MAA (Max Authorized Alt)", "Prefixed by 'MAA' (e.g. MAA FL 280).", "Highest altitude allowed on the airway to prevent radio frequency interference with adjacent stations."]
    ]
    pdf.add_table(["Altitude Type Code", "Jeppesen Representation & Meaning", "Guaranteed Protection (Terrain vs Signal)"], alt_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_heading_1("2. Airway Structure & Waypoints")
    pdf.add_bullet("Airway Width", "Standard ICAO airway corridor width is 10 NM total (5 NM on either side of centerline).")
    pdf.add_bullet("Compulsory Reporting Point", "Solid filled black triangle. Aircraft MUST report position, time, and level to ATC when crossing.")
    pdf.add_bullet("On-Request Reporting Point", "Open hollow triangle. Report position only if specifically requested by ATC.")
    pdf.add_bullet("Changeover Point (COP)", "Indicates where pilots must switch NAV frequency from the behind station to the ahead station. If no COP is shown, change over occurs at the EXACT MIDPOINT of the airway leg!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Reading En-Route Altitudes & Frequency Change",
        "SCENARIO (Standard En-Route Chart Reading Drill):\n"
        "A pilot is planning an IFR flight along airway V12 between VOR Alfa and VOR Bravo:\n"
        "- Total distance between VORs = 90 NM\n"
        "- Along the airway segment, the chart displays: '7000' and '*4200'\n"
        "- No Changeover Point (COP) symbol is depicted along the route\n"
        "QUESTION 1: What do the numbers '7000' and '*4200' mean?\n"
        "QUESTION 2: At what distance from VOR Alfa must the pilot switch navigation receivers to VOR Bravo?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Decode '7000' and '*4200':\n"
        "  - '7000' without an asterisk is the MEA (Minimum En-route Altitude) = 7,000 ft.\n"
        "  - '*4200' with an asterisk is the MOCA (Minimum Obstacle Clearance Altitude) = 4,200 ft.\n"
        "  - Operational Meaning: To fly legally with reliable radio navigation, you must cruise at or above 7,000 ft (MEA). If descending in an emergency, you are guaranteed terrain clearance down to 4,200 ft (MOCA), but VOR signal is only guaranteed within 22 NM of the VOR!\n\n"
        "Step 2: Determine the Changeover Point (COP):\n"
        "  - Rule: When no COP symbol is published, the frequency changeover MUST take place at the EXACT MIDPOINT of the leg!\n"
        "  - Total distance = 90 NM\n"
        "  - Midpoint = 90 NM / 2 = 45 NM from VOR Alfa!\n\n"
        "FINAL ANSWER: 7000 = MEA; *4200 = MOCA. Switch navigation frequency to VOR Bravo at exactly 45 NM from VOR Alfa.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The MOCA 22 NM Signal Reception Trap",
        "- MOCA guarantees OBSTACLE CLEARANCE along the entire airway.\n"
        "- But MOCA guarantees NAVIGATION SIGNAL RECEPTION only within 22 NAUTICAL MILES (40 km) of the VOR transmitter! Beyond 22 NM, you may lose the VOR radial!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: On a Jeppesen en-route chart, what does an altitude preceded by an ASTERISK (*) (e.g. *3500) signify?",
         "[A] Maximum Authorized Altitude\n[B] MOCA (Minimum Obstacle Clearance Altitude)\n[C] Transition altitude\n[D] Minimum crossing altitude",
         "CORRECT: [B]. The asterisk denotes MOCA. It guarantees terrain clearance along the entire segment, but navigational signal coverage only within 22 NM of the facility."),
        ("Q2: In the absence of a published Changeover Point (COP) on an airway between two VORs, where should the pilot switch frequencies?",
         "[A] At 20 NM from the first VOR\n[B] At the EXACT MIDPOINT between the two facilities\n[C] Only upon ATC instruction\n[D] Over the next reporting point",
         "CORRECT: [B]. By standard ICAO rules, if no COP is shown on the chart, the frequency changeover must be performed halfway between the two navigational aids."),
        ("Q3: In a Grid MORA quadrangle over mountainous terrain, what vertical clearance above the highest obstacle is guaranteed?",
         "[A] 1,000 ft\n[B] At least 2,000 FT vertically\n[C] 500 ft\n[D] 35 ft",
         "CORRECT: [B]. Grid MORA provides 1,000 ft clearance in non-mountainous terrain, and at least 2,000 ft clearance in designated mountainous areas (terrain elevation above 5,000 ft).")
    ]

    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Flight Planning Chapter 5 compiled: {pdf_path}")


def build_fp_ch06():
    pdf_path = os.path.join(OUTPUT_DIR, "033_ch06_standard_departures_arrivals_sids_stars.pdf")
    pdf = PDFBuilder("Flight Planning", "033", "Chapter 6: SIDs, STARs & Holdings")

    pdf.add_title_banner(
        "Flight Planning",
        6,
        "Standard Departures (SID), STARs & Holding Entries",
        "209-248"
    )

    pdf.add_heading_1("1. Standard Instrument Departures (SID) & Transitions")
    pdf.add_paragraph(
        "A SID links the take-off runway to the en-route airway structure, ensuring safe obstacle clearance:"
    )
    pdf.add_bullet("Design Climb Gradient (PDG)", "Standard ICAO procedure design climb gradient is 3.3% (approx 200 ft/NM). If close-in obstacles exist, a steeper gradient (e.g. 5.5%) is published with an altitude up to which it must be maintained.")
    pdf.add_bullet("Altitude Restrictions", "At or Above (bar under number: _5000_), At or Below (bar over number), Mandatory Crossing Altitude (bars above and below), Altitude Window (e.g. FL 110 - FL 130).")

    pdf.add_heading_1("2. Holding Pattern Geometry & Standard Speeds")
    pdf.add_paragraph(
        "Standard holding pattern is an oval with RIGHT-HAND TURNS (non-standard is left-hand turns):"
    )
    pdf.add_bullet("Leg Timings", "Inbound leg timing: 1.0 MINUTE at or below 14,000 ft MSL; 1.5 MINUTES above 14,000 ft (FL 140).")
    pdf.add_bullet("ICAO Maximum Holding Speeds", "Up to 14,000 ft: 230 kt (turboprops 170 kt); 14,000 to 20,000 ft: 240 kt; Above FL 200: 265 kt (or 0.83 Mach).")

    pdf.add_heading_1("3. The Three Holding Entry Sectors")
    holding_table = [
        ["Entry Sector", "Angular Width & Relative Heading", "Standard Entry Maneuver Procedure"],
        ["Sector 1: Parallel Entry", "110° sector on the holding side.", "Fly to fix, turn to parallel the outbound track (heading reciprocal of inbound) on the non-holding side for 1 min, turn left toward holding side to intercept inbound track."],
        ["Sector 2: Teardrop (Offset)", "70° sector on the non-holding side.", "Fly to fix, turn outbound at 30° OFFSET into the holding area for 1 min, then turn right to intercept the inbound track."],
        ["Sector 3: Direct Entry", "180° sector (the entire remaining half).", "Fly directly to the fix, turn right onto the outbound heading, and enter the race-track pattern directly!"]
    ]
    pdf.add_table(["Entry Sector", "Angular Width & Relative Heading", "Standard Entry Maneuver Procedure"], holding_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Determining Holding Entry Sector",
        "SCENARIO (Classic ATPL Exam Question):\n"
        "An aircraft is flying on a heading of 350° toward VOR 'ZUR'.\n"
        "ATC instructs: 'Hold at ZUR on the 090° radial, inbound track 270°, right-hand turns.'\n"
        "QUESTION: What is the correct ICAO holding entry procedure?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Identify Inbound Track and Turn Direction:\n"
        "  - Inbound Track = 270°\n"
        "  - Turn direction = Standard RIGHT-HAND turns.\n"
        "  - Outbound Track = 090° (reciprocal of 270°).\n\n"
        "Step 2: Draw the 3 Entry Sectors relative to Inbound Track (270°):\n"
        "  - For standard right-hand turns:\n"
        "    * Sector 1 (Parallel - 110°): From 270° to (270° - 110°) = 270° to 160° clockwise (160° to 270°).\n"
        "    * Sector 2 (Teardrop - 70°): From 270° to (270° + 70°) = 270° to 340° (clockwise 270° to 340°).\n"
        "    * Sector 3 (Direct - 180°): From 340° to 160° (the entire remaining arc: 340° through North/360° to 160°).\n\n"
        "Step 3: Check Aircraft Inbound Heading (350°):\n"
        "  - Aircraft is arriving on heading 350°.\n"
        "  - Compare 350° with the sectors:\n"
        "    * 350° falls squarely inside Sector 3 (which spans from 340° through 360° to 160°)!\n\n"
        "FINAL ANSWER: Sector 3 (DIRECT ENTRY)! Upon reaching ZUR, the pilot turns right directly onto the outbound heading of 090°.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Right-Hand vs Left-Hand Holding Rule",
        "- For RIGHT-HAND turns: Sector 1 (Parallel) is on the left (110°); Sector 2 (Teardrop) is on the right (70°).\n"
        "- For LEFT-HAND turns: The sectors are MIRRORED! Sector 1 is 110° on the right, Sector 2 is 70° on the left!\n"
        "- Sector 3 (Direct) is always the large 180° sector opposite the entry.",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: What is the standard outbound leg TIMING for a holding pattern at or below 14,000 ft MSL?",
         "[A] 1.5 minutes\n[B] 1.0 MINUTE (60 seconds)\n[C] 2.0 minutes\n[D] 45 seconds",
         "CORRECT: [B]. Under ICAO PANS-OPS, the outbound leg is timed for 1.0 minute up to and including 14,000 ft (FL 140), and 1.5 minutes above 14,000 ft."),
        ("Q2: In a standard right-hand holding pattern, what is the angular width of SECTOR 1 (Parallel Entry)?",
         "[A] 70°\n[B] 110 DEGREES\n[C] 180°\n[D] 90°",
         "CORRECT: [B]. Sector 1 (Parallel) covers an arc of 110°; Sector 2 (Teardrop) covers 70°; Sector 3 (Direct) covers 180°."),
        ("Q3: What is the maximum ICAO holding speed for aircraft holding at 10,000 ft MSL?",
         "[A] 250 kt\n[B] 230 KNOTS (or 170 kt for normal turboprops)\n[C] 200 kt\n[D] 265 kt",
         "CORRECT: [B]. Under ICAO Doc 8168, maximum holding speed up to 14,000 ft is 230 kt for jet aircraft.")
    ]

    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Flight Planning Chapter 6 compiled: {pdf_path}")


def build_fp_ch07():
    pdf_path = os.path.join(OUTPUT_DIR, "033_ch07_meteorological_charts_wintem_sigwx.pdf")
    pdf = PDFBuilder("Flight Planning", "033", "Chapter 7: WINTEM & SIGWX Charts")

    pdf.add_title_banner(
        "Flight Planning",
        7,
        "Meteorological Planning Charts (WINTEM & SIGWX)",
        "249-290"
    )

    pdf.add_heading_1("1. Upper Wind & Temperature Charts (WINTEM)")
    pdf.add_paragraph(
        "WINTEM charts display forecast wind arrows and outside temperatures at specific flight levels (FL 050, 100, 180, 240, 300, 340, 390):"
    )
    pdf.add_bullet("Wind Arrow Decoding", "Shaft points in the direction the wind is blowing. Barb markings: Triangular pennant = 50 knots; Long barb = 10 knots; Short barb = 5 knots.")
    pdf.add_bullet("Temperature Labels", "At and above FL 240, temperatures are universally NEGATIVE; the minus sign is omitted! (e.g. '56' at FL 340 means -56°C!).")

    pdf.add_heading_1("2. Significant Weather Charts (SIGWX)")
    pdf.add_paragraph(
        "High-level SIGWX charts (FL 250 to FL 630) show critical en-route flight hazards:"
    )
    pdf.add_bullet("Jet Streams", "Represented by heavy black lines with arrows showing direction. Core speed: Double slash // indicates speed change of 20 kt. Hatching indicates CAT (Clear Air Turbulence) boundaries.")
    pdf.add_bullet("Tropopause Heights", "Printed in small rectangular boxes (e.g. '380' means tropopause is at FL 380). High tropopause = warm air mass (equatorial); Low tropopause = cold polar air mass.")
    pdf.add_bullet("Cumulonimbus (CB)", "Identified as ISOL CB (isolated), OCNL CB (occasional), or FRQ CB (frequent) embedded in layer clouds.")

    pdf.add_heading_1("3. Cold Weather Altimeter Temperature Corrections")
    pdf.add_paragraph(
        "In extreme cold temperatures, the barometric altimeter OVER-READS (indicates higher than true altitude!): 'High to low, look out below!'"
    )
    pdf.add_bullet("Master Cold Temperature Correction Formula", "Correction (ft) = 4 ft x (Height above altimeter station / 1,000 ft) x (ISA Deviation in °C below standard)")

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Cold Weather Altimeter Correction on Final Approach",
        "SCENARIO (Safety-Critical ICAO Winter Operation Drill):\n"
        "An aircraft is on an ILS approach to an airport in Scandinavia in winter:\n"
        "- Airport Elevation = 1,000 ft MSL\n"
        "- Outside Air Temperature (OAT) at the surface = -25°C\n"
        "- Decision Altitude (DA) on chart = 1,200 ft MSL (Height above runway = 200 ft)\n"
        "- Minimum Safe Altitude (MSA) = 4,000 ft MSL (Height above station = 3,000 ft)\n"
        "QUESTION: What is the true altitude of the aircraft if it levels at indicated MSA 4,000 ft? What indicated altitude must the pilot fly to maintain true MSA 4,000 ft?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate ISA Temperature at Airport Elevation (1,000 ft):\n"
        "  - ISA at Sea Level = +15°C.\n"
        "  - ISA lapse rate = -2°C per 1,000 ft.\n"
        "  - ISA at 1,000 ft = +15°C - 2°C = +13°C.\n\n"
        "Step 2: Calculate ISA Deviation (Delta ISA):\n"
        "  - Actual OAT = -25°C.\n"
        "  - Delta ISA = Actual OAT - ISA = -25°C - (+13°C) = -38°C (38°C COLDER than standard!).\n\n"
        "Step 3: Calculate Altimeter Error at MSA (Height above station = 4,000 - 1,000 = 3,000 ft):\n"
        "  - Rule: 4 ft per 1,000 ft of height per °C of cold deviation.\n"
        "  - Correction = 4 ft x (3,000 ft / 1,000 ft) x 38°C\n"
        "  - Correction = 4 ft x 3 x 38 = 12 x 38 = 456 ft error!\n\n"
        "Step 4: Determine True Altitude vs Required Indicated Altitude:\n"
        "  - Because the air is cold, the altimeter over-reads by 456 ft! If flying at indicated 4,000 ft, TRUE ALTITUDE IS ONLY 3,544 ft (456 ft dangerously closer to mountains!).\n"
        "  - To guarantee 4,000 ft of true clearance, the pilot MUST ADD 456 ft to the altimeter!\n"
        "  - Minimum Indicated Altitude to fly = 4,000 ft + 456 ft = 4,456 ft!\n\n"
        "FINAL ANSWER: True altitude is 3,544 ft without correction. Pilot must fly indicated 4,460 ft.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Cold Weather Altimeter Trap",
        "- Cold air contracts the atmospheric column: True altitude is LOWER than indicated altitude!\n"
        "- When OAT is below 0°C, temperature corrections MUST BE ADDED to published altitudes (DA, MDA, MSA) so you don't hit the ground early!",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: On an upper wind WINTEM chart at FL 340, a temperature is labeled '48' next to a wind arrow. What is the actual temperature?",
         "[A] +48°C\n[B] -48°C (minus sign is universally omitted at high flight levels)\n[C] 48 Kelvin\n[D] 48% relative humidity",
         "CORRECT: [B]. Above FL 240 in mid-latitudes, temperatures are permanently below zero. To reduce chart clutter, the negative minus sign is omitted."),
        ("Q2: In extremely cold weather (OAT substantially below ISA), how does an uncorrected pressure altimeter read relative to true altitude?",
         "[A] It reads lower than true altitude\n[B] It reads HIGHER than true altitude (the aircraft is physically lower than the altimeter indicates!)\n[C] It reads accurately\n[D] It fails completely",
         "CORRECT: [B]. Cold air is dense, causing pressure levels to compress closer to the ground. The altimeter reads higher than actual true altitude ('high to low, look out below')."),
        ("Q3: On a high-level SIGWX chart, what does a heavy black line with an arrow and a double slash // indicate?",
         "[A] A thunderstorm front\n[B] A JET STREAM, with the double slash indicating a speed change of 20 knots along the jet axis\n[C] An oceanic boundary\n[D] Volcanic ash",
         "CORRECT: [B]. Jet stream cores are depicted by heavy arrows. A double bar // represents a change in core wind speed of 20 kt.")
    ]

    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Flight Planning Chapter 7 compiled: {pdf_path}")


def build_fp_ch08():
    pdf_path = os.path.join(OUTPUT_DIR, "033_ch08_inflight_monitoring_reộng_dpp.pdf")
    pdf = PDFBuilder("Flight Planning", "033", "Chapter 8: Fuel Monitoring & DPP")

    pdf.add_title_banner(
        "Flight Planning",
        8,
        "Fuel Monitoring, Bogey Curves & Decision Point (DPP)",
        "291-340"
    )

    pdf.add_heading_1("1. In-Flight Fuel Monitoring & Bogey Curves")
    pdf.add_paragraph(
        "Under EASA AIR-OPS, flight crews must record fuel remaining at each designated en-route waypoint and compare it against the operational flight plan (OFP):"
    )
    pdf.add_bullet("Fuel Bogey Curve (Howgozit)", "A graphical chart plotting Fuel Remaining versus Distance/Time. A falling curve steeper than planned indicates higher fuel consumption, headwind increase, or fuel leak!")
    pdf.add_bullet("Minimum Fuel Declaration", "'MINIMUM FUEL' informs ATC that all planned aerodrome options have been committed to, and any unexpected delay will result in landing with less than planned final reserve fuel. (It is NOT an emergency, but priority is requested).")
    pdf.add_bullet("Mayday Fuel Declaration", "'MAYDAY MAYDAY MAYDAY FUEL' is a distress emergency declared when estimated usable fuel on landing will be less than the 30-minute final reserve fuel. ATC will clear all conflicting traffic!")

    pdf.add_heading_1("2. The Decision Point Procedure (DPP) / Predetermined Point (PDP)")
    pdf.add_paragraph(
        "On long-range flights, carrying 5% contingency fuel for the entire 10-hour trip creates a huge mass penalty. The Decision Point Procedure (DPP) solves this legally:"
    )
    pdf.add_bullet("The DPP Concept", "The flight plan is split into two co-existing plans through an en-route 'Decision Point' (DP): (1) Flight to Destination via DP, with contingency fuel calculated ONLY from the Decision Point to Destination! (2) Flight to an En-Route Alternate via DP. Because contingency fuel applies only to the short leg from DP to destination, thousands of kilograms of contingency fuel are saved at take-off!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Fuel Savings using Decision Point Procedure (DPP)",
        "SCENARIO (Long-Range Flight Fuel Optimization Drill):\n"
        "A Boeing 787 is flying from London to Tokyo:\n"
        "- Total Trip Fuel = 60,000 kg\n"
        "- A Decision Point (DP) is selected along track over Siberia\n"
        "- Trip Fuel from Departure to DP = 40,000 kg\n"
        "- Remaining Trip Fuel from DP to Tokyo Destination = 20,000 kg\n"
        "- Under standard fuel policy, Contingency Fuel is 5% of Total Trip Fuel\n"
        "- Under DPP, Contingency Fuel is 5% of Trip Fuel FROM DP TO DESTINATION!\n"
        "QUESTION: How much contingency fuel is saved at take-off by using the Decision Point Procedure?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate Standard 5% Contingency Fuel for entire flight:\n"
        "  - Standard Contingency = 5% of Total Trip Fuel (60,000 kg)\n"
        "  - Standard Contingency = 0.05 x 60,000 kg = 3,000 kg.\n\n"
        "Step 2: Calculate DPP Contingency Fuel (5% from DP to Tokyo):\n"
        "  - Trip Fuel from DP to Tokyo = 20,000 kg\n"
        "  - DPP Contingency = 5% of 20,000 kg = 0.05 x 20,000 kg = 1,000 kg!\n\n"
        "Step 3: Calculate Fuel Savings at Take-Off:\n"
        "  - Fuel Saved = Standard Contingency - DPP Contingency\n"
        "  - Fuel Saved = 3,000 kg - 1,000 kg = 2,000 kg!\n\n"
        "Step 4: Operational Benefit for Dummies:\n"
        "  - Saving 2,000 kg of contingency fuel reduces aircraft take-off mass, allowing the airline to carry 20 additional passengers or 2 tonnes of high-yield cargo, while remaining 100% compliant with EASA safety regulations!\n\n"
        "FINAL ANSWER: The Decision Point Procedure saves exactly 2,000 kg of contingency fuel at take-off.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Decision Point Action Trap",
        "- When reaching the Decision Point en-route:\n"
        "- If actual fuel remaining is AT OR ABOVE the required fuel to reach Tokyo -> CONTINUE TO DESTINATION!\n"
        "- If actual fuel remaining is BELOW the required fuel to reach Tokyo -> DIVERT TO EN-ROUTE ALTERNATE!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: What is the primary operational advantage of using the DECISION POINT PROCEDURE (DPP) under EASA fuel policy?",
         "[A] Eliminates the need for an alternate\n[B] It reduces the required CONTINGENCY FUEL at take-off by calculating 5% contingency only from the Decision Point to Destination, saving aircraft mass\n[C] Allows flying without final reserve\n[D] Permits landing in zero visibility",
         "CORRECT: [B]. Under CAT.OP.MPA.180, DPP permits basing contingency fuel only on the stage from the decision point to destination (or alternate), saving substantial fuel mass at take-off."),
        ("Q2: What is the difference between declaring 'MINIMUM FUEL' and declaring 'MAYDAY MAYDAY MAYDAY FUEL'?",
         "[A] Minimum fuel is declared after touchdown\n[B] 'MINIMUM FUEL' is an advisory to ATC that delay will compromise reserves (not an emergency); 'MAYDAY FUEL' is a formal distress emergency declared when estimated landing fuel is below 30-min final reserve\n[C] There is no difference\n[D] Minimum fuel requires immediate evacuation",
         "CORRECT: [B]. Minimum fuel warns ATC that any unexpected delay will cause a fuel emergency; it does not grant priority. Mayday fuel is an emergency declaration demanding immediate priority."),
        ("Q3: On an in-flight fuel log, what does a sudden downward divergence of the actual fuel curve below the planned flight plan curve indicate?",
         "[A] Stronger tailwind than forecast\n[B] An abnormal fuel burn caused by higher engine fuel consumption, lower cruise level, or a severe FUEL LEAK\n[C] Lighter aircraft\n[D] Cabin heating failure",
         "CORRECT: [B]. A steep drop in the fuel curve indicates fuel is being depleted faster than planned, requiring the crew to verify engine parameters and check for fuel leaks.")
    ]

    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Flight Planning Chapter 8 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_fp_ch05()
    build_fp_ch06()
    build_fp_ch07()
    build_fp_ch08()
