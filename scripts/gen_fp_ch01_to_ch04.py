#!/usr/bin/env python3
"""
Generator for Subject 033: Flight Planning and Monitoring
Volume 1: Chapters 1 to 4
- Chapter 1: VFR Flight Planning, Vector Triangle & Navigational Calculations
- Chapter 2: EASA IFR Fuel Policy (AIR-OPS: Taxi, Trip, Contingency, Alternate, Final)
- Chapter 3: Critical Points: Point of No Return (PNR) & Equi-Time Point (ETP)
- Chapter 4: ICAO ATS Flight Plan (FPL) Form Item-by-Item Decoding & Execution

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Flight Planning and EASA AIR-OPS (CAT.OP.MPA.180).
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_3/033_flight_planning_monitoring"

def build_fp_ch01():
    pdf_path = os.path.join(OUTPUT_DIR, "033_ch01_vfr_flight_planning_navigation.pdf")
    pdf = PDFBuilder("Flight Planning", "033", "Chapter 1: VFR Planning & Navigation")

    pdf.add_title_banner(
        "Flight Planning",
        1,
        "VFR Flight Planning & Navigational Calculations",
        "1-40"
    )

    pdf.add_heading_1("1. The Navigational Vector Triangle & Terminology")
    pdf.add_paragraph(
        "Navigation is the geometric combination of aircraft heading/airspeed with the wind vector:"
    )
    pdf.add_bullet("True Track (TR)", "The actual path over the earth's surface that the aircraft intends to follow or is tracking.")
    pdf.add_bullet("True Airspeed (TAS)", "The calibrated airspeed corrected for altitude and temperature. Represents speed through undisturbed air.")
    pdf.add_bullet("Wind Vector (W/V)", "Given as direction (degrees True) FROM WHICH the wind blows, and speed (knots).")
    pdf.add_bullet("Drift Angle & Wind Correction Angle (WCA)", "The angle between True Heading and True Track. Drift is Right (+) if wind pushes aircraft right of track. WCA opposes drift: Heading = Track - (+- Drift).")
    pdf.add_bullet("Groundspeed (GS)", "The actual speed of the aircraft across the ground: GS = TAS +- Wind Component.")
    pdf.add_bullet("Conversion Chain", "True Heading (TH) +- Magnetic Variation = Magnetic Heading (MH) +- Compass Deviation = Compass Heading (CH) ('Variation West, Magnetic Best; Variation East, Magnetic Least').")

    pdf.add_heading_1("2. ETE & Fuel Consumption Formulas")
    pdf.add_bullet("Estimated Time En Route (ETE)", "Time (hours) = Distance (NM) / Groundspeed (kt). Time (minutes) = (Distance / GS) x 60.")
    pdf.add_bullet("Leg Fuel Burn", "Fuel (liters or kg) = Time (hours) x Fuel Consumption Rate (liters/hr or kg/hr).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: VFR Leg Heading, Groundspeed, ETE & Fuel",
        "SCENARIO (Standard Navigation Flight Planning Drill):\n"
        "A pilot plans a cross-country leg:\n"
        "- True Track = 090°\n"
        "- Distance = 160 NM\n"
        "- True Airspeed (TAS) = 120 knots\n"
        "- Forecast Wind = 360° at 30 knots (Direct crosswind from the Left!)\n"
        "- Magnetic Variation = 5° West\n"
        "- Fuel Flow = 40 liters/hour\n"
        "QUESTION: Calculate (1) Wind Correction Angle & True Heading, (2) Magnetic Heading, (3) Groundspeed, (4) ETE, (5) Fuel Burned.\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate Wind Correction Angle (WCA):\n"
        "  - Wind is from 360° against a Track of 090° (Wind angle = 90° direct from Left).\n"
        "  - Crosswind component = 30 kt x sin(90°) = 30 knots.\n"
        "  - Headwind component = 30 kt x cos(90°) = 0 knots.\n"
        "  - Rule of Thumb: Drift (degrees) ~ (Crosswind kt / TAS kt) x 60\n"
        "  - Drift = (30 / 120) x 60 = 0.25 x 60 = 15° to the RIGHT.\n"
        "  - To counter a 15° Right drift, you must steer 15° to the LEFT (-15° WCA)!\n"
        "  - True Heading (TH) = Track - Drift = 090° - 15° = 075° True!\n\n"
        "Step 2: Calculate Magnetic Heading (MH) ('Variation West, Magnetic Best' -> ADD!):\n"
        "  - MH = True Heading + Var West = 075° + 5° = 080° Magnetic!\n\n"
        "Step 3: Calculate Groundspeed (GS) using Pythagoras Theorem on the vector triangle:\n"
        "  - GS = sqrt(TAS^2 - Crosswind^2) - Headwind\n"
        "  - GS = sqrt(120^2 - 30^2) - 0 = sqrt(14,400 - 900) = sqrt(13,500) = 116.2 knots.\n\n"
        "Step 4: Calculate Estimated Time En Route (ETE):\n"
        "  - Time = (Distance / GS) x 60 = (160 NM / 116.2 kt) x 60 = 1.377 hours x 60 = 82.6 minutes (1h 23 min).\n\n"
        "Step 5: Calculate Leg Fuel Burn:\n"
        "  - Fuel = Time (hours) x Fuel Flow = 1.377 hours x 40 L/hr = 55.1 liters.\n\n"
        "FINAL ANSWER: True Heading = 075°; Magnetic Heading = 080°; GS = 116 kt; ETE = 83 minutes; Fuel = 55 liters.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Variation East vs West Memory Aid",
        "- 'Variation West, Magnetic Best' -> Magnetic is BIGGER (ADD West variation to True Heading).\n"
        "- 'Variation East, Magnetic Least' -> Magnetic is SMALLER (SUBTRACT East variation from True Heading).",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: If True Track is 180°, True Airspeed is 150 kt, wind is 090°/30 kt, and variation is 10° East, what is the MAGNETIC HEADING?",
         "[A] 160°\n[B] 170°\n[C] 190°\n[D] 180°",
         "CORRECT: [A]. Wind from 090° pushes aircraft to the Right (Drift +). Crosswind = 30 kt. Drift = (30/150) x 60 = 12° Right. True Heading = 180° - 12° = 168° True. Magnetic Heading = 168° - 10° East (East is least!) = 158° (~160°)."),
        ("Q2: What is the effect of a 90° pure crosswind on aircraft Groundspeed compared to True Airspeed?",
         "[A] Groundspeed equals TAS\n[B] Groundspeed is SLIGHTLY LESS than TAS, because aircraft nose must angle into the wind\n[C] Groundspeed is higher than TAS\n[D] Groundspeed drops to zero",
         "CORRECT: [B]. Because the aircraft points into the wind to maintain track (WCA), a portion of its forward TAS vector is angled sideways, reducing the forward groundspeed vector: GS = sqrt(TAS^2 - XW^2)."),
        ("Q3: In navigational flight planning, how is 'DRIFT' defined?",
         "[A] The angle between True North and Magnetic North\n[B] The angular difference between the Heading (aircraft longitudinal axis) and the Track (actual flight path over the ground)\n[C] The climb angle\n[D] The compass error",
         "CORRECT: [B]. Drift is the angle between heading and track caused by crosswind pushing the aircraft sideways.")
    ]

    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Flight Planning Chapter 1 compiled: {pdf_path}")


def build_fp_ch02():
    pdf_path = os.path.join(OUTPUT_DIR, "033_ch02_ifr_fuel_policy_easa.pdf")
    pdf = PDFBuilder("Flight Planning", "033", "Chapter 2: EASA IFR Fuel Policy")

    pdf.add_title_banner(
        "Flight Planning",
        2,
        "EASA IFR Fuel Policy (AIR-OPS CAT.OP.MPA.180)",
        "41-82"
    )

    pdf.add_heading_1("1. The EASA Regulatory Fuel Breakdown")
    pdf.add_paragraph(
        "Under EASA AIR-OPS (CAT.OP.MPA.180), an IFR commercial flight is legally prohibited from departing without carrying minimum certified fuel reserves:"
    )

    fuel_table = [
        ["Fuel Component", "Regulatory Definition & Calculation Basis", "Operational Role & Minimum Rules"],
        ["1. Taxi Fuel", "Fuel consumed before take-off (APU burn, engine start, taxiing to runway).", "Standard allowance: typically 150 to 300 kg for twin-jets (12-15 min)."],
        ["2. Trip Fuel", "Fuel required from brake release at departure to touchdown at destination.", "Includes take-off, climb, cruise, descent, approach, and landing at destination."],
        ["3. Contingency Fuel", "Buffer for unforeseen deviations (weather, ATC routing, lower flight level).", "HIGHER OF: 5% of Trip Fuel, OR 3% with En-Route Alternate (ERA), OR 20 min flight time."],
        ["4. Destination Alternate Fuel", "Fuel required to divert from missed approach at destination to alternate.", "Missed approach + climb + cruise to alternate + descent + approach + landing."],
        ["5. Final Reserve Fuel", "Fuel to hold at 1,500 ft AGL over alternate in ISA conditions.", "MANDATORY: 30 minutes for turbine / jet aircraft (45 minutes for piston aircraft)!"],
        ["6. Additional Fuel", "Required only if aircraft must comply with depressurization or OEI drift down.", "Ensures reaching a safe airport if engine fails or cabin depressurizes at critical point."],
        ["7. Extra Fuel", "Discretionary fuel loaded at Commander's authority for anticipated delays.", "Added for holding, thunderstorm circumnavigation, or tankering."]
    ]
    pdf.add_table(["Fuel Component", "Regulatory Definition & Calculation Basis", "Operational Role & Minimum Rules"], fuel_table, col_widths=[110.0, 215.0, 175.0])

    pdf.add_heading_1("2. The Master Fuel Equations")
    pdf.add_bullet("Minimum Required Take-Off Fuel", "Take-Off Fuel = Trip Fuel + Contingency Fuel + Alternate Fuel + Final Reserve Fuel (+ Additional Fuel).")
    pdf.add_bullet("Minimum Required Block Fuel (Ramp Fuel)", "Block Fuel = Taxi Fuel + Minimum Required Take-Off Fuel (+ Extra Fuel).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Compiling an EASA IFR Fuel Plan",
        "SCENARIO (Classic ATPL Flight Planning Exam Question):\n"
        "An Airbus A320 is planned for an IFR passenger flight from Madrid to Paris:\n"
        "- Planned Taxi Fuel: 200 kg\n"
        "- Calculated Trip Fuel: 5,000 kg\n"
        "- Diversion fuel to Paris Alternate (Orly to Beauvais): 1,200 kg\n"
        "- Holding fuel consumption at 1,500 ft AGL: 2,400 kg/hour\n"
        "- No En-Route Alternate (ERA) is designated (standard 5% contingency applies)\n"
        "- Commander requests 300 kg Extra Fuel for holding\n"
        "QUESTION: Calculate (1) Contingency Fuel, (2) Final Reserve Fuel, (3) Minimum Take-Off Fuel, and (4) Total Block Fuel.\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate Contingency Fuel (Standard 5% of Trip Fuel):\n"
        "  - Contingency = 5% of 5,000 kg = 0.05 x 5,000 kg = 250 kg.\n\n"
        "Step 2: Calculate Final Reserve Fuel (30 minutes of holding for jet!):\n"
        "  - Holding fuel burn = 2,400 kg/hour.\n"
        "  - Final Reserve (30 min = 0.5 hour) = 0.5 hr x 2,400 kg/hr = 1,200 kg!\n\n"
        "Step 3: Calculate Minimum Required Take-Off Fuel:\n"
        "  - Take-Off Fuel = Trip + Contingency + Alternate + Final Reserve\n"
        "  - Take-Off Fuel = 5,000 kg + 250 kg + 1,200 kg + 1,200 kg = 7,650 kg.\n\n"
        "Step 4: Calculate Total Required Block Fuel (Add Taxi and Extra Fuel):\n"
        "  - Block Fuel = Taxi (200 kg) + Take-Off Fuel (7,650 kg) + Extra (300 kg)\n"
        "  - Block Fuel = 200 + 7,650 + 300 = 8,150 kg!\n\n"
        "FINAL ANSWER: Contingency = 250 kg; Final Reserve = 1,200 kg; Min Take-Off Fuel = 7,650 kg; Total Block Fuel = 8,150 kg.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Final Reserve: 30 Min Turbine vs 45 Min Piston Trap",
        "- For TURBINE / JET aircraft: Final Reserve is 30 MINUTES holding at 1,500 ft.\n"
        "- For PISTON aircraft: Final Reserve is 45 MINUTES holding!\n"
        "- Final Reserve is SACROSANCT: If you calculate that you will land with less than Final Reserve, you MUST DECLARE 'MAYDAY MAYDAY MAYDAY FUEL'!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: Under EASA AIR-OPS, what is the minimum duration of FINAL RESERVE FUEL required for a commercial turbojet transport aircraft?",
         "[A] 45 minutes\n[B] 30 MINUTES holding at 1,500 ft AGL above the alternate aerodrome under ISA conditions\n[C] 20 minutes\n[D] 60 minutes",
         "CORRECT: [B]. For turbine-powered aeroplanes, final reserve fuel is calculated for 30 minutes of holding at 1,500 ft (450 m) above aerodrome elevation in standard ISA conditions."),
        ("Q2: What is the standard CONTINGENCY FUEL percentage required on an IFR flight when no en-route alternate (ERA) aerodrome is selected?",
         "[A] 10% of Trip Fuel\n[B] 5% OF TRIP FUEL (or 5 minutes, whichever is greater)\n[C] 3% of Trip Fuel\n[D] 20%",
         "CORRECT: [B]. The baseline contingency fuel required by EASA CAT.OP.MPA.180 is 5% of the planned trip fuel (reduced to 3% only if an en-route alternate is nominated)."),
        ("Q3: When MUST a flight crew legally declare 'MAYDAY MAYDAY MAYDAY FUEL' to Air Traffic Control?",
         "[A] When diverting to any alternate\n[B] When the estimated usable fuel upon landing at the nearest suitable aerodrome is calculated to be LESS THAN the planned Final Reserve Fuel\n[C] When contingency fuel is exhausted\n[D] On any missed approach",
         "CORRECT: [B]. Under ICAO Annex 6 and EASA regulations, MAYDAY FUEL is an explicit declaration of emergency that must be transmitted whenever calculated fuel on touchdown is less than the mandatory 30-minute final reserve.")
    ]

    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Flight Planning Chapter 2 compiled: {pdf_path}")


def build_fp_ch03():
    pdf_path = os.path.join(OUTPUT_DIR, "033_ch03_critical_points_pnr_etp.pdf")
    pdf = PDFBuilder("Flight Planning", "033", "Chapter 3: Critical Points (PNR & ETP)")

    pdf.add_title_banner(
        "Flight Planning",
        3,
        "Critical Points: Point of No Return (PNR) & Equi-Time Point (ETP)",
        "83-120"
    )

    pdf.add_heading_1("1. Point of No Return (PNR / Point of Safe Return)")
    pdf.add_paragraph(
        "The Point of No Return (PNR) is the furthest point along track to which an aircraft can fly and still return to the departure aerodrome (or en-route base) with mandatory reserves intact:"
    )
    pdf.add_bullet("PNR Concept", "Beyond the PNR, the aircraft CANNOT RETURN to base; it is committed to flying forward. PNR depends exclusively on: (1) Safe Endurance (E), (2) Groundspeed Out (GS_out), and (3) Groundspeed Home (GS_home).")
    pdf.add_bullet("Safe Endurance (E)", "Total fuel on board MINUS (Alternate Fuel + Final Reserve Fuel + Taxi Fuel). Only usable cruise fuel can be spent flying to PNR and back.")
    pdf.add_bullet("The PNR Master Formula", "Time to PNR (T_out) = (Safe Endurance (E) x GS_home) / (GS_out + GS_home)")
    pdf.add_bullet("Distance to PNR", "Distance_PNR = Time to PNR x GS_out")

    pdf.add_heading_1("2. Equi-Time Point (ETP / Critical Point)")
    pdf.add_paragraph(
        "The Equi-Time Point (ETP) is the point along track from which it takes EQUAL FLYING TIME to continue to destination or to return to departure:"
    )
    pdf.add_bullet("ETP Concept", "In zero wind, ETP is exactly half-way (50% distance). BUT WITH WIND, ETP MOVES INTO THE WIND! (A headwind on the way out shifts ETP closer to destination; a tailwind shifts ETP closer to departure).")
    pdf.add_bullet("The ETP Master Formula", "Distance to ETP (D_ETP) = (Total Leg Distance (D) x GS_home) / (GS_out + GS_home)")
    pdf.add_bullet("Time to ETP", "Time to ETP = D_ETP / GS_out")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Finding PNR and ETP with Wind",
        "SCENARIO (Classic Exam Problem):\n"
        "An oceanic flight is planned between Airport A and Airport B:\n"
        "- Total Distance (D) = 1,200 NM\n"
        "- Aircraft TAS = 400 knots\n"
        "- En-route Wind: 50 knots direct Headwind on outbound leg (Tailwind returning home!)\n"
        "- Total Safe Endurance (E) = 4.0 hours\n"
        "QUESTION: Calculate (1) Distance to ETP from Airport A, and (2) Time and Distance to PNR.\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate Outbound and Inbound Groundspeeds:\n"
        "  - GS_out = TAS - Headwind = 400 kt - 50 kt = 350 knots.\n"
        "  - GS_home = TAS + Tailwind = 400 kt + 50 kt = 450 knots.\n"
        "  - GS_sum = GS_out + GS_home = 350 + 450 = 800 knots.\n\n"
        "Step 2: Calculate Distance to ETP (Equi-Time Point):\n"
        "  - Formula: D_ETP = (Total Distance x GS_home) / (GS_out + GS_home)\n"
        "  - D_ETP = (1,200 NM x 450 kt) / 800 kt\n"
        "  - D_ETP = 540,000 / 800 = 675 NM from Airport A!\n"
        "  - (Notice: Because of the headwind, ETP shifted forward from 600 NM to 675 NM!)\n\n"
        "Step 3: Calculate Time to PNR (Point of No Return):\n"
        "  - Safe Endurance (E) = 4.0 hours.\n"
        "  - Formula: T_out = (E x GS_home) / (GS_out + GS_home)\n"
        "  - T_out = (4.0 hrs x 450 kt) / 800 kt = 1,800 / 800 = 2.25 hours (2 hrs 15 min)!\n\n"
        "Step 4: Calculate Distance to PNR:\n"
        "  - Distance_PNR = T_out x GS_out = 2.25 hrs x 350 kt = 787.5 NM from Airport A!\n\n"
        "FINAL ANSWER: Distance to ETP = 675 NM. Time to PNR = 2.25 hours (787.5 NM).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The ETP Moves Into the Wind Trap",
        "- If you have a HEADWIND outbound: GS_home is FASTER than GS_out. Therefore, ETP shifts FORWARD (closer to destination)!\n"
        "- If you have a TAILWIND outbound: GS_home is SLOWER. Therefore, ETP shifts BACKWARD (closer to departure)!\n"
        "- Always remember: In the formula numerator, it is ALWAYS GS_home! (D_ETP = D x GS_home / Sum_GS).",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: In the formula for calculating distance to the Equi-Time Point (ETP), which groundspeed appears in the NUMERATOR?",
         "[A] GS outbound\n[B] GS HOME (return groundspeed)\n[C] Average TAS\n[D] Crosswind component",
         "CORRECT: [B]. The formula is: Distance to ETP = (Total Distance x GS_home) / (GS_out + GS_home). GS_home is in the numerator."),
        ("Q2: On an oceanic flight with a strong HEADWIND on the outbound leg, where will the Equi-Time Point (ETP) be located?",
         "[A] Exactly at the midpoint of the route\n[B] Displaced TOWARDS THE DESTINATION (into the wind)\n[C] Displaced towards departure\n[D] ETP ceases to exist",
         "CORRECT: [B]. Because returning home has a tailwind (faster GS), you can fly further towards destination before reaching the point where flying forward takes the same time as flying back."),
        ("Q3: What single factor determines the location of the POINT OF NO RETURN (PNR) for a given aircraft and wind?",
         "[A] Only aircraft mass\n[B] The SAFE ENDURANCE of the aircraft (usable fuel available to return)\n[C] Runway length\n[D] Flap angle",
         "CORRECT: [B]. PNR is purely fuel-limited. It is the furthest point from which the aircraft can return with mandatory reserve fuel intact: T = (E x GS_home) / (GS_out + GS_home).")
    ]

    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Flight Planning Chapter 3 compiled: {pdf_path}")


def build_fp_ch04():
    pdf_path = os.path.join(OUTPUT_DIR, "033_ch04_icao_ats_flight_plan_form.pdf")
    pdf = PDFBuilder("Flight Planning", "033", "Chapter 4: ICAO ATS Flight Plan Form")

    pdf.add_title_banner(
        "Flight Planning",
        4,
        "ICAO ATS Flight Plan (FPL) Form Item-by-Item",
        "121-164"
    )

    pdf.add_heading_1("1. The ICAO Model Flight Plan Form Structure")
    pdf.add_paragraph(
        "The standard ICAO Flight Plan Form is used globally for Air Traffic Control coordination. Every item must be encoded precisely:"
    )

    fpl_table = [
        ["Item Number & Title", "Regulatory Code Formats & Allowed Entries", "Operational Significance & Rules"],
        ["Item 7: Aircraft ID", "Max 7 alphanumeric characters (e.g. IBE3412 or EC-MZZ).", "Exact callsign matching radio communication."],
        ["Item 8: Flight Rules & Type", "Rules: I (IFR), V (VFR), Y (IFR changing to VFR), Z (VFR changing to IFR). Type: S (Scheduled), N (Non-scheduled), G (General), M (Military), X (Other).", "Y and Z flights require specifying the changeover point in Item 15!"],
        ["Item 9: Type & Wake Cat", "Number + 4-letter ICAO type (e.g. A320, B738). Wake turbulence: L (<7,000 kg), M (7,000 to 136,000 kg), H (>=136,000 kg), J (Super A380).", "Dictates ATC wake separation intervals!"],
        ["Item 10: Equipment & Cap", "10a COM/NAV (S for standard VHF/VOR/ILS, D, G for GNSS, R for PBN approved). 10b SSR (Mode S, ADS-B).", "R requires PBN/ specification in Item 18!"],
        ["Item 13: DEP & EOBT", "4-letter ICAO departure aerodrome (e.g. LEMD) + 4-digit Estimated Off-Block Time (UTC).", "If no ICAO code, enter ZZZZ and specify in Item 18 DEP/."],
        ["Item 15: Speed, Level & Route", "Speed: N (knots, 4 digits, e.g. N0450) or M (Mach, 3 digits, e.g. M078). Level: F (Flight Level, 3 digits, e.g. F350) or A (Altitude in 100s ft). Route: ATS airways and waypoints.", "Speed must be initial true airspeed (TAS)."],
        ["Item 16: DEST, EET & Alternates", "4-letter destination (e.g. LFPG) + Total EET (hours:min, e.g. 0145) + 4-letter Alternate 1 & 2.", "Total EET is time from take-off to overhead destination."],
        ["Item 18: Other Information", "PBN/ (e.g. B1D1O1S2), DOF/ (Date of Flight YYMMDD), REG/ (Registration), EET/ (FIR boundary estimates), RVR/.", "0 (zero) indicates no special information."],
        ["Item 19: Supplementary Info", "E/ (Endurance hhmm), P/ (Persons on board), R/ (Emergency radio), S/ (Survival equipment), J/ (Jackets), D/ (Dinghy).", "Transmitted only for Search and Rescue (SAR)."]
    ]
    pdf.add_table(["Item Number & Title", "Regulatory Code Formats & Allowed Entries", "Operational Significance & Rules"], fpl_table, col_widths=[110.0, 215.0, 175.0])

    pdf.add_heading_1("2. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Filling an ICAO ATS Flight Plan",
        "SCENARIO (Standard EASA FPL Encoding Drill):\n"
        "A scheduled commercial flight is operated by Iberia:\n"
        "- Callsign: IBE6501, Aircraft: Airbus A350-900 (MTOM = 280,000 kg)\n"
        "- Flight Rules: Entirely IFR\n"
        "- Initial Cruising Speed: TAS 480 knots; Cruising Level: FL 390\n"
        "- Departure: Madrid Barajas (LEMD) at 14:30 UTC\n"
        "- Destination: New York JFK (KJFK); Total Estimated En-Route Time: 7 hours 45 minutes\n"
        "- Alternate: Boston Logan (KBOS)\n"
        "- Usable Fuel Endurance on board: 10 hours 30 minutes; Total Persons on Board: 312\n"
        "QUESTION: How are Items 7, 8, 9, 13, 15, 16, and 19 encoded?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Item 7 (Aircraft Identification) = IBE6501\n\n"
        "Step 2: Item 8 (Flight Rules & Type):\n"
        "  - Flight Rules: I (IFR)\n"
        "  - Type of Flight: S (Scheduled air service)\n"
        "  - Entry: I S\n\n"
        "Step 3: Item 9 (Number, Type & Wake Turbulence):\n"
        "  - Type: A359\n"
        "  - Wake Turbulence Category: MTOM = 280,000 kg (> 136,000 kg) -> Category H (HEAVY)!\n"
        "  - Entry: A359 / H\n\n"
        "Step 4: Item 13 (Departure Aerodrome & Time):\n"
        "  - LEMD 1430\n\n"
        "Step 5: Item 15 (Speed & Level):\n"
        "  - Speed: TAS 480 kt -> N0480 (N followed by 4 digits)\n"
        "  - Level: FL 390 -> F390 (F followed by 3 digits)\n"
        "  - Entry: N0480 F390 [Route...]\n\n"
        "Step 6: Item 16 (Destination, Total EET & Alternate):\n"
        "  - KJFK 0745 KBOS\n\n"
        "Step 7: Item 19 (Endurance & POB):\n"
        "  - E/ 1030 P/ 0312\n\n"
        "FINAL ANSWER: Encoded exactly as above! Zero errors, fully compliant with ICAO Doc 4444.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The FPL Speed & Wake Turbulence Traps",
        "- Speed Format: 'N' (Knots) MUST have 4 digits (e.g. 120 kt = N0120; 450 kt = N0450)!\n"
        "- Wake Turbulence: Heavy (H) is >= 136,000 kg (136 tonnes). Medium (M) is 7,000 to 136,000 kg. Super (J) is Airbus A380 only!\n"
        "- Flight Rules Y vs Z: Y = IFR changing to VFR. Z = VFR changing to IFR (Remember: Alphabetical order V->Z!).",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: On an ICAO Flight Plan Form, what does flight rule code 'Y' indicate?",
         "[A] Pure VFR flight\n[B] A flight planned to operate initially under IFR, followed by one or more subsequent changes of flight rules to VFR\n[C] A flight in yellow airspace\n[D] Military flight",
         "CORRECT: [B]. Code Y indicates an IFR flight that changes to VFR en-route. Code Z indicates a VFR flight that changes to IFR en-route."),
        ("Q2: In Item 9 of the ICAO Flight Plan, what is the Wake Turbulence Category for an aircraft with a Maximum Certified Take-Off Mass of 140,000 kg?",
         "[A] M (Medium)\n[B] H (HEAVY), because MTOM is greater than or equal to 136,000 kg\n[C] J (Super)\n[D] L (Light)",
         "CORRECT: [B]. The Heavy (H) wake turbulence category applies to all aircraft with an MTOM of 136,000 kg (300,000 lb) or more."),
        ("Q3: How must an initial true airspeed of 210 knots be entered into Item 15 of an ICAO Flight Plan?",
         "[A] 210K\n[B] N0210 (the letter N followed by exactly four digits)\n[C] TAS210\n[D] KT0210",
         "CORRECT: [B]. Airspeed in knots must be expressed by the letter N followed by 4 digits, padding with leading zeros if necessary (e.g. N0210).")
    ]

    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Flight Planning Chapter 4 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_fp_ch01()
    build_fp_ch02()
    build_fp_ch03()
    build_fp_ch04()
