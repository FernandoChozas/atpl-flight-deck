#!/usr/bin/env python3
"""
Generator for Subject 070: Operational Procedures
Volume 1: Chapters 1 to 5
- Chapter 1: International & European Regulatory Framework (EASA AIR-OPS)
- Chapter 2: Crew Composition & Flight Duty Time Limitations (FTL Limits)
- Chapter 3: Aerodrome Operating Minima (AOM) & Low Visibility Operations (LVO)
- Chapter 4: PANS-OPS Instrument Flight Procedures (Departures & Circling)
- Chapter 5: Long-Range Approvals: ETOPS / EDTO Operations & Diversion Limits

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Operational Procedures and EASA AIR-OPS (Regulation EU 965/2012).
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/070_operational_procedures"

def build_ops_ch01():
    pdf_path = os.path.join(OUTPUT_DIR, "070_ch01_easa_airops_framework.pdf")
    pdf = PDFBuilder("Operational Procedures", "070", "Chapter 1: EASA AIR-OPS Framework")

    pdf.add_title_banner(
        "Operational Procedures",
        1,
        "International & European Framework (EASA AIR-OPS)",
        "1-36"
    )

    pdf.add_heading_1("1. The ICAO & EASA Regulatory Architecture")
    pdf.add_paragraph(
        "Commercial flight operations in Europe are governed by EASA Regulation (EU) No 965/2012 (AIR-OPS), transposing ICAO Annex 6 standards:"
    )

    ops_table = [
        ["EASA AIR-OPS Part", "Full Official Title", "Scope & Regulatory Application"],
        ["Part-GEN", "General Requirements", "Definitions, acronyms, and common rules across all flight operations."],
        ["Part-ARO", "Authority Requirements", "Requirements for National Aviation Authorities (e.g. AESA) issuing certificates."],
        ["Part-ORO", "Organisation Requirements", "Management systems, safety management (SMS), and Air Operator Certificates (AOC)."],
        ["Part-CAT", "Commercial Air Transport", "Mandatory operating rules for commercial airlines carrying passengers or cargo."],
        ["Part-SPA", "Specific Approvals", "Operations requiring special authorization: ETOPS, RVSM, LVO, PBN, Dangerous Goods."],
        ["Part-NCC / Part-NCO", "Non-Commercial Operations", "Complex motor-powered (NCC) and other-than-complex (NCO) private flights."]
    ]
    pdf.add_table(["EASA AIR-OPS Part", "Full Official Title", "Scope & Regulatory Application"], ops_table, col_widths=[110.0, 185.0, 200.0])

    pdf.add_heading_1("2. The Operations Manual (OM Parts A, B, C, D)")
    pdf.add_paragraph(
        "An Air Operator Certificate (AOC) holder must maintain an Operations Manual divided into 4 mandatory parts:"
    )
    pdf.add_bullet("OM Part A (General / Basic)", "Company policies, safety management, crew responsibilities, standard operating procedures (SOP), fuel policy, and flight duty limits (FTL).")
    pdf.add_bullet("OM Part B (Aeroplane Operating Matters)", "Type-specific aircraft technical systems, limitations, checklist procedures, and AFM performance tables.")
    pdf.add_bullet("OM Part C (Route and Aerodrome Instructions)", "Route guides, terminal charts, airport operating minima, and escape routes.")
    pdf.add_bullet("OM Part D (Training)", "Training syllabi, simulator checks, and proficiency checking for flight crew and cabin crew.")

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: In which part of an airline's Operations Manual (OM) are TYPE-SPECIFIC aircraft operating procedures and performance tables published?",
         "[A] OM Part A\n[B] OM PART B (Aeroplane Operating Matters)\n[C] OM Part C\n[D] OM Part D",
         "CORRECT: [B]. Under EASA ORO.MLR.100, OM-B contains all aircraft type-specific data, systems operating procedures, checklists, and performance limitations."),
        ("Q2: Which EASA AIR-OPS Annex sets out mandatory rules for operators conducting COMMERCIAL AIR TRANSPORT with aeroplanes?",
         "[A] Part-NCO\n[B] PART-CAT (Annex IV: Commercial Air Transport Operations)\n[C] Part-SPO\n[D] Part-MED",
         "CORRECT: [B]. Part-CAT applies to all commercial revenue flights carrying passengers, cargo, or mail."),
        ("Q3: Who holds the final legal authority for the safety and operation of the aircraft during flight?",
         "[A] The airline Chief Pilot\n[B] THE COMMANDER (Pilot-in-Command)\n[C] Air Traffic Control\n[D] The dispatcher",
         "CORRECT: [B]. Under ICAO Annex 6 and EASA CAT.GEN.MPA.105, the Commander has complete authority over the aircraft and all persons on board.")
    ]

    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Operational Procedures Chapter 1 compiled: {pdf_path}")


def build_ops_ch02():
    pdf_path = os.path.join(OUTPUT_DIR, "070_ch02_crew_composition_ftl_limits.pdf")
    pdf = PDFBuilder("Operational Procedures", "070", "Chapter 2: Crew & FTL Limits")

    pdf.add_title_banner(
        "Operational Procedures",
        2,
        "Crew Composition & Flight Duty Limitations (FTL)",
        "37-76"
    )

    pdf.add_heading_1("1. EASA Flight and Duty Time Limitations (FTL)")
    pdf.add_paragraph(
        "EASA Subpart-FTL (ORO.FTL) establishes mandatory limits to prevent crew fatigue from compromising safety:"
    )
    pdf.add_bullet("Flight Duty Period (FDP)", "Time from when a crew member is required to report for duty (typically 45 to 60 min before departure) until engine shutdown at the end of the last sector.")
    pdf.add_bullet("Maximum Daily FDP", "Ranges from 9 to 13 hours, depending on report time (circadian rhythm) and number of flight sectors (e.g. 1 to 2 sectors reporting between 06:00 and 13:29 allows 13.0 hours FDP; reporting between 02:00 and 04:59 drops to 9.0 hours!).")
    pdf.add_bullet("Minimum Rest Period", "Mandatory rest before duty must be AT LEAST 12 HOURS, or equal to the duration of the preceding duty period (whichever is GREATER!). If away from home base: at least 10 hours including an 8-hour sleep opportunity.")

    pdf.add_heading_1("2. Cumulative Duty & Flight Time Caps")
    pdf.add_bullet("Maximum Cumulative Duty Hours", "60 duty hours in 7 consecutive days; 110 duty hours in 14 consecutive days; 190 duty hours in 28 consecutive days.")
    pdf.add_bullet("Maximum Cumulative Flight Hours (Block Time)", "100 flight hours in any 28 consecutive days; 900 flight hours in a calendar year; 1,000 flight hours in any 12 consecutive months.")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Minimum Rest Period after Heavy Duty",
        "SCENARIO (EASA Flight Crew Rostering Drill):\n"
        "A commercial airline crew reports for duty at home base at 06:00 local time:\n"
        "- They operate a multi-sector European schedule\n"
        "- The duty finishes at 20:30 local time (Total duty period = 14.5 hours)\n"
        "QUESTION: What is the MINIMUM REST PERIOD required before the crew can report for their next duty?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Recall the EASA Home Base Rest Rule:\n"
        "  - Rule: Minimum rest at home base = The GREATER of:\n"
        "    * (A) 12 hours standard baseline, OR\n"
        "    * (B) The exact duration of the preceding duty period!\n\n"
        "Step 2: Compare the two values:\n"
        "  - Standard Baseline = 12.0 hours\n"
        "  - Preceding Duty Period = 14.5 hours\n"
        "  - The greater value is 14.5 hours!\n\n"
        "Step 3: Calculate the Earliest Allowable Next Report Time:\n"
        "  - Duty finished at 20:30.\n"
        "  - Add 14.5 hours of rest:\n"
        "  - 20:30 + 14h 30m = 11:00 the following morning!\n\n"
        "FINAL ANSWER: Minimum mandatory rest period is 14.5 hours (14 hours 30 minutes). Earliest next report is 11:00.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Rest Away from Base vs Home Base Trap",
        "- At HOME BASE: Rest = Greater of 12 hours OR length of duty.\n"
        "- AWAY FROM BASE: Rest = Greater of 10 hours OR length of duty (must include an 8-hour sleep opportunity).\n"
        "- Never assign 10 hours rest at home base; that is an illegal roster violation!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: Under EASA FTL regulations, what is the maximum cumulative FLIGHT TIME (block hours) permitted in any 28 consecutive days?",
         "[A] 60 hours\n[B] 100 FLIGHT HOURS\n[C] 110 hours\n[D] 900 hours",
         "CORRECT: [B]. EASA ORO.FTL.210 sets maximum cumulative flight time at 100 hours in 28 consecutive days, 900 hours in a calendar year, and 1,000 hours in 12 months."),
        ("Q2: What is the maximum cumulative DUTY TIME permitted in any 7 consecutive days?",
         "[A] 40 hours\n[B] 60 DUTY HOURS\n[C] 70 hours\n[D] 100 hours",
         "CORRECT: [B]. Total duty periods must not exceed 60 hours in 7 consecutive days, 110 hours in 14 days, and 190 hours in 28 days."),
        ("Q3: What is the minimum required rest period at home base following a duty period of 10 hours?",
         "[A] 10 hours\n[B] AT LEAST 12 HOURS (the baseline minimum)\n[C] 8 hours\n[D] 24 hours",
         "CORRECT: [B]. At home base, rest must be at least 12 hours, or the length of the preceding duty if longer. Since 10h < 12h, the 12-hour minimum applies.")
    ]

    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Operational Procedures Chapter 2 compiled: {pdf_path}")


def build_ops_ch03():
    pdf_path = os.path.join(OUTPUT_DIR, "070_ch03_aom_lvo_all_weather_ops.pdf")
    pdf = PDFBuilder("Operational Procedures", "070", "Chapter 3: AOM & Low Visibility")

    pdf.add_title_banner(
        "Operational Procedures",
        3,
        "Aerodrome Operating Minima (AOM) & LVO",
        "77-116"
    )

    pdf.add_heading_1("1. All-Weather Precision Approach Categories")
    pdf.add_paragraph(
        "Under EASA AIR-OPS (CAT.OP.MPA.110), aerodrome operating minima establish legal limits for take-off and landing:"
    )

    cat_table = [
        ["ILS Approach Category", "Decision Height (DH)", "Runway Visual Range (RVR) Minimum"],
        ["Category I (CAT I)", "DH >= 200 ft (60 m)", "RVR >= 550 meters (or 800 m for manual landing without HUD)."],
        ["Category II (CAT II)", "DH: 100 ft to < 200 ft (30 to 60 m)", "RVR >= 300 meters (requires autoland or HUD guidance)."],
        ["Category IIIa (CAT IIIa)", "DH: < 100 ft (or NO DH)", "RVR >= 175 meters (requires fail-passive autoland)."],
        ["Category IIIb (CAT IIIb)", "DH: < 50 ft (or NO DH)", "RVR: 75 to < 175 meters (requires fail-operational autoland and rollout)."],
        ["Category IIIc (CAT IIIc)", "NO Decision Height (0 ft)", "NO RVR limitation (Zero visibility landing and rollout - not operational)."]
    ]
    pdf.add_table(["ILS Approach Category", "Decision Height (DH)", "Runway Visual Range (RVR) Minimum"], cat_table, col_widths=[120.0, 185.0, 195.0])

    pdf.add_heading_1("2. Low Visibility Take-Off (LVTO)")
    pdf.add_paragraph(
        "A take-off conducted with RVR < 400 meters is an LVTO operation requiring Specific Approval (Part-SPA.LVO). Absolute minimum RVR for commercial jets: 125 meters with runway centerline lights and markings (or 150 m for Cat C/D)."
    )

    pdf.add_heading_1("3. The Approach Ban Rule")
    pdf.add_paragraph(
        "The flight crew may begin an instrument approach regardless of reported RVR. However:"
    )
    pdf.add_bullet("The 1,000 ft Ban Point", "If the reported RVR is LESS than the published minimum, THE APPROACH MUST NOT BE CONTINUED BEYOND: The Outer Marker (OM), or an altitude of 1,000 ft above aerodrome elevation in the final approach segment!")
    pdf.add_bullet("Ban Exemption After 1,000 ft", "If the aircraft is ALREADY BELOW 1,000 ft AGL and RVR deteriorates below minima, the crew MAY CONTINUE to the Decision Height (DH). If visual references are acquired at DH, landing is permitted!")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: Under EASA regulations, what are the Decision Height (DH) and minimum RVR limits for an ILS CATEGORY II approach?",
         "[A] DH >= 200 ft, RVR >= 550 m\n[B] DH between 100 ft and < 200 ft, and RVR NOT LESS THAN 300 METERS\n[C] DH < 50 ft, RVR 75 m\n[D] Zero DH",
         "CORRECT: [B]. Cat II precision approach is defined by a DH between 100 and 199 ft, and a minimum RVR of 300 m."),
        ("Q2: According to the 'APPROACH BAN' rule, past which point is an aircraft prohibited from continuing an approach if reported RVR is below minima?",
         "[A] Top of descent\n[B] The 1,000 FT AGL POINT (or Outer Marker) in the final approach segment\n[C] Initial approach fix\n[D] Touchdown",
         "CORRECT: [B]. If RVR drops below legal minima before passing 1,000 ft AGL (or the outer marker), continuing the approach is illegal; a missed approach must be initiated."),
        ("Q3: What special equipment is required on the runway for a commercial jet Low Visibility Take-Off (LVTO) with an RVR of 150 meters?",
         "[A] Only edge lights\n[B] High-intensity RUNWAY CENTERLINE LIGHTS and runway markings\n[C] Sodium flares\n[D] Ground radar only",
         "CORRECT: [B]. LVTO below 400 m requires illuminated runway centerline lights and markings to provide continuous lateral visual tracking.")
    ]

    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Operational Procedures Chapter 3 compiled: {pdf_path}")


def build_ops_ch04():
    pdf_path = os.path.join(OUTPUT_DIR, "070_ch04_pans_ops_departures_circling.pdf")
    pdf = PDFBuilder("Operational Procedures", "070", "Chapter 4: PANS-OPS & Circling")

    pdf.add_title_banner(
        "Operational Procedures",
        4,
        "PANS-OPS Instrument Procedures & Circling",
        "117-156"
    )

    pdf.add_heading_1("1. PANS-OPS Instrument Departure Criteria")
    pdf.add_paragraph(
        "ICAO Doc 8168 (PANS-OPS) establishes standard criteria for protected airspace design:"
    )
    pdf.add_bullet("Design Climb Gradient (PDG)", "Standard departure climb gradient is 3.3% (200 ft/NM), comprising 2.5% net obstacle clearance + 0.8% safety buffer.")
    pdf.add_bullet("Minimum Turn Altitude", "No turn may be initiated on departure below 120 METERS (400 FT) ABOVE AERODROME ELEVATION!")

    pdf.add_heading_1("2. Visual Manoeuvring (Circling Approach)")
    pdf.add_paragraph(
        "A visual circling approach is used when landing runway does not align with the instrument approach (alignment > 30° off runway centerline, or descent gradient exceeds 6.5%):"
    )
    pdf.add_bullet("Protected Circling Radii", "Cat A = 1.68 NM; Cat B = 2.66 NM; Cat C = 4.20 NM; Cat D = 5.28 NM from all runway thresholds.")
    pdf.add_bullet("Action on Loss of Visual Reference", "IF VISUAL CONTACT WITH THE RUNWAY IS LOST DURING CIRCLING: Initiate an IMMEDIATE CLIMBING TURN TOWARDS THE LANDING RUNWAY, establish overhead the aerodrome, and follow the missed approach procedure of the INSTRUMENT RUNWAY originally flown!")

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: Under PANS-OPS design rules, what is the MINIMUM altitude above aerodrome level before an aircraft may initiate a turn on an instrument departure?",
         "[A] 200 ft\n[B] 120 METERS (400 FEET) AGL\n[C] 1,000 ft\n[D] 500 ft",
         "CORRECT: [B]. PANS-OPS prohibits turns below 120 m (400 ft) above aerodrome elevation to guarantee obstacle clearance during straight acceleration."),
        ("Q2: If visual reference is LOST while conducting a visual circling manoeuvre to land, what is the mandatory pilot action?",
         "[A] Descend 500 ft to find the ground\n[B] Initiate an IMMEDIATE CLIMBING TURN TOWARDS THE LANDING RUNWAY, climb overhead, and fly the missed approach of the instrument approach runway\n[C] Turn 90° away from airport\n[D] Land immediately",
         "CORRECT: [B]. Turning towards the runway keeps the aircraft within the protected circling obstacle area while climbing to safety in the instrument missed approach."),
        ("Q3: What is the radius of the protected obstacle clearance area for a CATEGORY C aircraft conducting a circling approach?",
         "[A] 1.68 NM\n[B] 4.20 NAUTICAL MILES from the runway threshold\n[C] 2.66 NM\n[D] 5.28 NM",
         "CORRECT: [B]. PANS-OPS assigns Cat C aircraft a circling area radius of 4.20 NM based on a maximum circling speed of 180 kt.")
    ]

    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Operational Procedures Chapter 4 compiled: {pdf_path}")


def build_ops_ch05():
    pdf_path = os.path.join(OUTPUT_DIR, "070_ch05_etops_edto_regulations.pdf")
    pdf = PDFBuilder("Operational Procedures", "070", "Chapter 5: ETOPS / EDTO Operations")

    pdf.add_title_banner(
        "Operational Procedures",
        5,
        "Extended Diversion Time Operations (ETOPS / EDTO)",
        "157-196"
    )

    pdf.add_heading_1("1. The ETOPS Regulatory Concept")
    pdf.add_paragraph(
        "ETOPS (Extended-range Twin-engine Operational Performance Standards) / EDTO permits twin-engine aircraft to fly long-range routes across oceans and deserts:"
    )
    pdf.add_bullet("The 60-Minute Threshold", "Without ETOPS approval, a twin-jet must remain within 60 MINUTES FLYING TIME at One-Engine-Inoperative (OEI) cruise speed in still air from an adequate aerodrome.")
    pdf.add_bullet("ETOPS Approval Ratings", "ETOPS 120 min, 180 min, or 240+ min. The approved diversion time defines a circle around en-route alternates: Radius (NM) = Approved ETOPS Time (hours) x Approved OEI Cruise TAS (knots)!")

    pdf.add_heading_1("2. Adequate vs Suitable Aerodrome")
    pdf.add_bullet("Adequate Aerodrome", "Physically capable: Runway length, strength, emergency services (RFFS), and lighting meet aircraft requirements.")
    pdf.add_bullet("Suitable Aerodrome (ETOPS En-Route Alternate)", "An adequate aerodrome whose FORECAST WEATHER AT EXPECTED TIME OF ARRIVAL (ETA) is AT OR ABOVE ETOPS DISPATCH MINIMA (which includes safety buffers above normal landing minima)!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating ETOPS 120-Minute Maximum Diversion Range",
        "SCENARIO (Transatlantic Route Planning Drill):\n"
        "An Airbus A330 operator has ETOPS 120-minute approval:\n"
        "- Approved One-Engine Inoperative (OEI) cruise speed in still air = 420 knots TAS\n"
        "QUESTION: What is the maximum allowable diversion distance (radius of ETOPS circle) in Nautical Miles from an en-route alternate aerodrome?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Identify Approved Diversion Time and OEI Speed:\n"
        "  - ETOPS Time = 120 minutes = 2.0 hours.\n"
        "  - Approved OEI Speed = 420 knots TAS.\n\n"
        "Step 2: Recall the ETOPS Maximum Diversion Distance Formula:\n"
        "  - Rule: ETOPS distance is calculated strictly in STILL AIR (zero wind credit/penalty)!\n"
        "  - Formula: Maximum Range (NM) = Diversion Time (hours) x OEI TAS\n\n"
        "Step 3: Calculate the Maximum Range:\n"
        "  - Range = 2.0 hours x 420 knots = 840 Nautical Miles!\n\n"
        "Step 4: Operational Meaning for Dummies:\n"
        "  - The aircraft must never be further than 840 NM from a suitable ETOPS alternate at any point along the ocean route!\n\n"
        "FINAL ANSWER: Maximum allowable diversion distance is exactly 840 Nautical Miles.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Still Air ETOPS Distance Trap",
        "- The maximum ETOPS diversion distance is calculated in STILL AIR (zero wind)!\n"
        "- Even if there is a 100 knot jet stream tailwind, you CANNOT stretch the 840 NM circle!\n"
        "- The circle radius is fixed by: Approved Hours x OEI TAS in still air.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: What is the baseline threshold diversion time for twin-turbine aeroplanes beyond which ETOPS / EDTO approval is MANDATORY?",
         "[A] 30 minutes\n[B] 60 MINUTES at one-engine-inoperative cruise speed in still air\n[C] 120 minutes\n[D] 180 minutes",
         "CORRECT: [B]. Any twin-engine commercial flight route that exceeds 60 minutes diversion time to an adequate aerodrome is classified as an extended diversion time operation (ETOPS)."),
        ("Q2: In ETOPS dispatch regulations, what distinguishes a 'SUITABLE AERODROME' from an 'ADEQUATE AERODROME'?",
         "[A] Only runway length\n[B] A suitable aerodrome must have forecast weather at ETA meeting or exceeding higher ETOPS DISPATCH MINIMA\n[C] Suitable aerodromes must be military\n[D] There is no difference",
         "CORRECT: [B]. An adequate aerodrome meets physical criteria; a suitable aerodrome also has confirmed weather forecasts meeting strict ETOPS dispatch buffers during the arrival window."),
        ("Q3: An operator has 180-minute ETOPS approval. If their approved OEI cruise speed is 400 kt TAS in still air, what is the maximum permissible distance from an alternate?",
         "[A] 800 NM\n[B] 1,200 NAUTICAL MILES (3.0 hours x 400 kt = 1,200 NM)\n[C] 400 NM\n[D] 1,800 NM",
         "CORRECT: [B]. 180 minutes = 3 hours. 3 hours x 400 knots = 1,200 NM maximum distance from an en-route alternate.")
    ]

    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Operational Procedures Chapter 5 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_ops_ch01()
    build_ops_ch02()
    build_ops_ch03()
    build_ops_ch04()
    build_ops_ch05()
