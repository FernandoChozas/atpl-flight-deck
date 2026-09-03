#!/usr/bin/env python3
"""
Generator for Subject 031: Mass and Balance
Volume 1: Chapters 1 to 4
- Chapter 1: Mass Definitions & Allowable Limits (BEM, DOM, ZFM, TOM, LM)
- Chapter 2: Center of Gravity Theory, Datums & Law of the Lever
- Chapter 3: Calculation of CG & % MAC (LEMAC, TEMAC)
- Chapter 4: Mass Shifts, Load Changes & Ballast Calculations

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Mass & Balance and EASA AIR-OPS (CAT.POL.MAB).
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_3/031_mass_and_balance"

def build_mb_ch01():
    pdf_path = os.path.join(OUTPUT_DIR, "031_ch01_definitions_mass_limits.pdf")
    pdf = PDFBuilder("Mass and Balance", "031", "Chapter 1: Mass Definitions & Limits")

    pdf.add_title_banner(
        "Mass and Balance",
        1,
        "Mass Definitions & Structural Limits",
        "1-22"
    )

    pdf.add_heading_1("1. The Core Mass Definitions Hierarchy")
    pdf.add_paragraph(
        "In aviation, aircraft mass is divided into precise regulatory categories. Understanding the sequence of additions is vital:"
    )

    mass_table = [
        ["Basic Empty Mass (BEM)", "Airframe structure, engines, unusable fuel, full engine oil, hydraulic fluid and permanent standard equipment.", "Starting point of aircraft mass; manufacturer weighed."],
        ["Dry Operating Mass (DOM)", "BEM + Flight Crew & Cabin Crew (+ their baggage) + Catering / Pantry + Removable emergency equipment.", "DOM = BEM + Crew + Pantry. Mass of aircraft ready to fly without payload or fuel."],
        ["Operating Mass (OM)", "DOM + Total Take-Off Fuel.", "OM = DOM + Fuel. Does NOT include any passengers or cargo."],
        ["Zero Fuel Mass (ZFM)", "DOM + Traffic Load (Payload: passengers + baggage + cargo).", "ZFM = DOM + Traffic Load. The entire mass of aircraft excluding fuel!"],
        ["Take-Off Mass (TOM)", "ZFM + Total Take-Off Fuel, OR: DOM + Traffic Load + Take-Off Fuel.", "TOM = ZFM + Fuel. Mass at brake release on the runway."],
        ["Landing Mass (LM)", "TOM minus Trip Fuel consumed in flight.", "LM = TOM - Trip Fuel."],
        ["Ramp / Taxi Mass", "TOM + Taxi Fuel (allowance burned during taxi to runway).", "Taxi Mass = TOM + Taxi Fuel (max allowable mass at gate)."]
    ]
    pdf.add_table(["Mass Term", "Definition & Constituent Components", "Master Equation & Significance"], mass_table, col_widths=[110.0, 220.0, 170.0])

    pdf.add_heading_1("2. Payload Concepts: Traffic Load vs Useful Load")
    pdf.add_bullet("Traffic Load (Payload)", "The total mass of revenue-earning items: Passengers + Baggage + Cargo + Mail. Formula: Traffic Load = ZFM - DOM.")
    pdf.add_bullet("Useful Load", "The total mass of everything that can be loaded into an empty operating aircraft: Traffic Load + Usable Fuel. Formula: Useful Load = TOM - DOM.")

    pdf.add_heading_1("3. Structural Limits vs Performance Limits")
    pdf.add_paragraph(
        "An aircraft is governed by two distinct sets of mass limits:"
    )
    pdf.add_bullet("Structural Limits (Maximum Certified)", "Permanent physical limits established by the manufacturer (MTOM, MZFM, MLM, MTXM). Exceeding these limits risks structural airframe failure (e.g. wing root bending overload at MZFM).")
    pdf.add_bullet("Performance Limits (Variable / Regulated)", "Limits calculated for specific runway and environmental conditions (Runway Length Limited TOM, Climb Gradient Limited TOM, Obstacle Limited TOM).")
    pdf.add_bullet("Golden Rule of Mass Planning", "Actual TOM MUST NOT EXCEED the LOWEST of: (1) Structural MTOM, (2) Regulated Performance MTOM, (3) MZFM + Fuel, (4) MLM + Trip Fuel!")

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Finding Maximum Allowable Take-Off Mass (MTOM)",
        "SCENARIO (Typical AviationExam Drill):\n"
        "Given the following aircraft data:\n"
        "- Dry Operating Mass (DOM): 35,000 kg\n"
        "- Maximum Structural Take-Off Mass (MTOM): 65,000 kg\n"
        "- Maximum Structural Landing Mass (MLM): 56,000 kg\n"
        "- Maximum Structural Zero Fuel Mass (MZFM): 51,000 kg\n"
        "- Performance Limited TOM for Runway 09: 63,500 kg\n"
        "- Planned Fuel on board at Take-Off: 11,000 kg\n"
        "- Estimated Trip Fuel burn to destination: 4,000 kg\n"
        "QUESTION: What is the MAXIMUM ALLOWABLE TAKE-OFF MASS that respects all limits?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Check the Direct Take-Off Mass Limits:\n"
        "  - Structural MTOM = 65,000 kg\n"
        "  - Performance MTOM = 63,500 kg -> (This restricts us to 63,500 kg max directly).\n\n"
        "Step 2: Check the Zero Fuel Mass Limit constraint on TOM:\n"
        "  - Max TOM = MZFM + Take-Off Fuel = 51,000 + 11,000 = 62,000 kg!\n"
        "  - (If we took off at 63,500 kg with 11,000 kg of fuel, our ZFM would be 52,500 kg, which EXCEEDS the structural MZFM of 51,000 kg!).\n\n"
        "Step 3: Check the Landing Mass Limit constraint on TOM:\n"
        "  - Max TOM = MLM + Trip Fuel = 56,000 + 4,000 = 60,000 kg!\n"
        "  - (If we took off heavier than 60,000 kg, after burning 4,000 kg of trip fuel we would land above the 56,000 kg landing limit!).\n\n"
        "Step 4: Compare all 3 constrained Take-Off Masses:\n"
        "  - Direct Take-off Limit: 63,500 kg\n"
        "  - ZFM-Constrained Limit: 62,000 kg\n"
        "  - Landing-Constrained Limit: 60,000 kg\n"
        "FINAL ANSWER: The Maximum Allowable Take-Off Mass is 60,000 kg! (Limited by Landing Mass).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Wing-Root Bending / MZFM Exam Trap",
        "- Why does MZFM exist? All payload is carried inside the fuselage, while fuel is carried inside the wings. In flight, wing fuel provides an upward relieving moment. When fuel burns down to zero, the entire heavy fuselage load is supported exclusively by the wing roots! Exceeding MZFM breaks the wing roots, even if you are well below MTOM!",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: What is the official definition of DRY OPERATING MASS (DOM)?",
         "[A] The mass of the airplane empty of all fuel and oil\n[B] Basic Empty Mass (BEM) PLUS crew, crew baggage, catering/pantry, and removable emergency equipment\n[C] Zero Fuel Mass minus payload\n[D] Maximum Take-Off Mass minus fuel",
         "CORRECT: [B]. DOM is the total mass of the aircraft ready for a specific type of operation, including all crew, their personal baggage, and catering, but excluding all usable fuel and traffic load (payload)."),
        ("Q2: If an aircraft's Maximum Zero Fuel Mass (MZFM) is 45,000 kg, Dry Operating Mass is 28,000 kg, and planned take-off fuel is 8,000 kg, what is the MAXIMUM TRAFFIC LOAD that can be legally carried?",
         "[A] 25,000 kg\n[B] 17,000 kg\n[C] 9,000 kg\n[D] 12,000 kg",
         "CORRECT: [B]. Traffic Load = ZFM - DOM. The maximum possible ZFM is MZFM (45,000 kg). Therefore: Max Traffic Load = 45,000 - 28,000 = 17,000 kg."),
        ("Q3: Which component is included in the BASIC EMPTY MASS (BEM) of an aircraft?",
         "[A] Flight crew baggage\n[B] Usable fuel in the wing tanks\n[C] Unusable fuel, engine oil, hydraulic fluid, and standard permanent equipment\n[D] Passenger catering supplies",
         "CORRECT: [C]. Basic Empty Mass includes the complete structural airframe, engines, standard fixed equipment, plus unusable fuel and full operating fluids (engine oil and hydraulic systems). Crew and catering are added to BEM to form DOM.")
    ]

    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"M&B Chapter 1 compiled: {pdf_path}")


def build_mb_ch02():
    pdf_path = os.path.join(OUTPUT_DIR, "031_ch02_cg_datum_moments.pdf")
    pdf = PDFBuilder("Mass and Balance", "031", "Chapter 2: CG Theory, Datums & Moments")

    pdf.add_title_banner(
        "Mass and Balance",
        2,
        "Center of Gravity Theory, Datums & Law of the Lever",
        "23-42"
    )

    pdf.add_heading_1("1. Center of Gravity (CG) Physical Concept")
    pdf.add_paragraph(
        "The Center of Gravity (CG) is the single imaginary point through which the resultant force of gravity acts on the entire aircraft. "
        "If suspended by a cable attached precisely to its CG, the aircraft would remain in perfect horizontal equilibrium in any attitude."
    )

    pdf.add_heading_1("2. The Datum & Arm Sign Conventions")
    pdf.add_paragraph(
        "To calculate where the CG is located, all physical positions are measured from an arbitrary reference plane called the DATUM:"
    )
    pdf.add_bullet("The Datum", "A vertical reference plane perpendicular to the longitudinal axis, chosen by the aircraft designer. Common locations: (1) Aircraft nose tip, (2) Engine firewall, (3) Wing leading edge.")
    pdf.add_bullet("The Arm (Lever Arm)", "The horizontal distance from the datum to the center of gravity of an individual item (passenger seat row, cargo compartment, fuel tank).")
    pdf.add_bullet("Sign Convention", "By universal convention: Distance BEHIND (aft of) the datum is POSITIVE (+). Distance IN FRONT of (forward of) the datum is NEGATIVE (-).")
    pdf.add_bullet("The Moment Equation", "Moment = Mass x Arm. Expressed in kg.m, kg.mm, or lb.in.")

    pdf.add_heading_1("3. The Law of the Lever & Center of Gravity Formula")
    pdf.add_paragraph(
        "The total moment of an aircraft about the datum is equal to the algebraic sum of the individual moments of all items loaded onto it:"
    )
    pdf.add_bullet("Master CG Equation", "Aircraft CG Location = (Total Moment) / (Total Mass) = Sum(Mass_i x Arm_i) / Sum(Mass_i).")

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Finding Aircraft Center of Gravity from Loading Table",
        "SCENARIO (Classic EASA Exam Question):\n"
        "An aircraft has the following loading schedule with the Datum located at the Engine Firewall:\n"
        "- Basic Empty Mass: 1,200 kg with an Arm of +1.50 m\n"
        "- Pilot and Copilot: 160 kg with an Arm of +1.10 m\n"
        "- Rear Passengers: 150 kg with an Arm of +2.20 m\n"
        "- Baggage in Nose Compartment: 40 kg with an Arm of -0.80 m (AHEAD of firewall!)\n"
        "- Fuel (in wings): 180 kg with an Arm of +1.60 m\n"
        "QUESTION: Calculate the exact position of the aircraft's Center of Gravity relative to the Datum.\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Build the Mass x Arm = Moment Table:\n"
        "  - Item 1 (BEM):      1,200 kg x (+1.50 m) = +1,800.0 kg.m\n"
        "  - Item 2 (Front):      160 kg x (+1.10 m) =   +176.0 kg.m\n"
        "  - Item 3 (Rear):       150 kg x (+2.20 m) =   +330.0 kg.m\n"
        "  - Item 4 (Nose Bag):    40 kg x (-0.80 m) =    -32.0 kg.m  [NOTE: NEGATIVE MOMENT!]\n"
        "  - Item 5 (Fuel):       180 kg x (+1.60 m) =   +288.0 kg.m\n\n"
        "Step 2: Sum the Total Mass:\n"
        "  - Total Mass = 1,200 + 160 + 150 + 40 + 180 = 1,730 kg.\n\n"
        "Step 3: Sum the Algebraic Moments (be careful with the negative sign!):\n"
        "  - Total Moment = 1,800.0 + 176.0 + 330.0 - 32.0 + 288.0 = +2,562.0 kg.m.\n\n"
        "Step 4: Divide Total Moment by Total Mass:\n"
        "  - CG = Total Moment / Total Mass = +2,562.0 kg.m / 1,730 kg = +1.4809 m.\n"
        "FINAL ANSWER: The Center of Gravity is located at +1.48 m (1.48 meters aft of the firewall).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Forward Datum / Negative Arm Trap",
        "- If an item is placed IN FRONT of the datum, its arm is NEGATIVE (-).\n"
        "- Its moment is therefore NEGATIVE! (Mass x (-Arm) = -Moment).\n"
        "- In the total moment sum, you MUST SUBTRACT this negative moment, but you MUST STILL ADD its mass to the total mass!",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: What is the definition of the 'ARM' of a load in mass and balance calculations?",
         "[A] The vertical height of the item above the cabin floor\n[B] The horizontal distance from the reference DATUM to the center of gravity of the item\n[C] The length of the fuselage\n[D] The structural thickness of the wing spar",
         "CORRECT: [B]. The arm is the physical distance along the longitudinal axis from the established reference datum to the center of gravity of the specific item."),
        ("Q2: If an aircraft has a total mass of 2,000 kg and a total moment of 6,000 kg.m about the datum, where is the Center of Gravity located?",
         "[A] 4.0 m aft of datum\n[B] 3.0 m aft of datum\n[C] 0.33 m aft of datum\n[D] At the datum",
         "CORRECT: [B]. CG = Total Moment / Total Mass = 6,000 kg.m / 2,000 kg = 3.0 meters aft of the datum."),
        ("Q3: If a designer chooses the aircraft nose as the Datum, what sign will all arms of items loaded inside the aircraft have?",
         "[A] Negative\n[B] Positive (+), because all loaded items are located aft of the nose tip\n[C] Zero\n[D] Variable depending on flight speed",
         "CORRECT: [B]. When the datum is placed at the extreme front tip (nose), all positions in the cabin, wings, and empennage lie aft of the datum, meaning all arms and moments are positive (+), eliminating negative numbers.")
    ]

    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"M&B Chapter 2 compiled: {pdf_path}")


def build_mb_ch03():
    pdf_path = os.path.join(OUTPUT_DIR, "031_ch03_cg_mac_calculations.pdf")
    pdf = PDFBuilder("Mass and Balance", "031", "Chapter 3: Calculation of CG & % MAC")

    pdf.add_title_banner(
        "Mass and Balance",
        3,
        "Calculation of CG & % MAC (Mean Aerodynamic Chord)",
        "43-66"
    )

    pdf.add_heading_1("1. The Mean Aerodynamic Chord (MAC) Concept")
    pdf.add_paragraph(
        "Because modern aircraft have swept, tapered wings, the aerodynamic chord varies along the wingspan. "
        "The Mean Aerodynamic Chord (MAC / c_bar) is the chord of an equivalent rectangular wing that has the identical pitching moment and aerodynamic characteristics as the actual wing!"
    )
    pdf.add_bullet("LEMAC", "Leading Edge of the Mean Aerodynamic Chord. The distance from the reference Datum to the front edge of the MAC.")
    pdf.add_bullet("TEMAC", "Trailing Edge of the Mean Aerodynamic Chord. LEMAC + Length of MAC = TEMAC.")
    pdf.add_bullet("Why Express CG as % MAC?", "Expressing CG as a percentage of MAC allows pilots to understand the aerodynamic stability and trim of an aircraft immediately, regardless of whether the aircraft is a small trainer or a heavy Boeing 777!")

    pdf.add_heading_1("2. The Master Conversion Formulas: Distance <-> % MAC")
    pdf.add_bullet("Formula 1: Converting CG Distance into % MAC", "% MAC = ((CG Distance from Datum - LEMAC) / Length of MAC) x 100")
    pdf.add_bullet("Formula 2: Converting % MAC into CG Distance from Datum", "CG Distance from Datum = LEMAC + (% MAC / 100) x Length of MAC")

    pdf.add_heading_1("3. Stability & Controllability Trade-off at the Limits")
    mac_limits_table = [
        ["CG Position Regime", "Aerodynamic Pitch Stability & Stick Forces", "Flight Control Authority & Fuel Performance"],
        ["Forward CG Limit", "MAXIMUM static longitudinal stability. Very heavy stick forces (high stick force per g).", "Landing flare authority severely limited! High downward tailplane force -> high induced trim drag and higher fuel burn."],
        ["Aft CG Limit", "MINIMUM static stability. Light, sensitive stick forces. Danger of over-controlling.", "Lower tailplane downforce -> LOWER TRIM DRAG, lower fuel burn. Must NOT exceed Neutral Point (neutral/unstable!)."]
    ]
    pdf.add_table(["CG Position Regime", "Aerodynamic Pitch Stability & Stick Forces", "Flight Control Authority & Fuel Performance"], mac_limits_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Converting CG Position to % MAC and Vice Versa",
        "SCENARIO 1 (Finding % MAC):\n"
        "Given the following aircraft technical data:\n"
        "- LEMAC is located at: 14.0 meters aft of datum\n"
        "- Length of the MAC: 4.0 meters\n"
        "- Actual aircraft CG calculated from loading sheet: 15.2 meters aft of datum\n"
        "QUESTION: What is the aircraft's Center of Gravity expressed as a percentage of MAC (% MAC)?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the distance from LEMAC to the CG:\n"
        "  - Distance from LEMAC = CG - LEMAC = 15.2 m - 14.0 m = 1.2 meters.\n\n"
        "Step 2: Divide this distance by the total length of the MAC:\n"
        "  - Fraction of MAC = 1.2 m / 4.0 m = 0.30.\n\n"
        "Step 3: Multiply by 100 to get a percentage:\n"
        "  - % MAC = 0.30 x 100 = 30.0% MAC.\n"
        "FINAL ANSWER: CG = 30.0% MAC.\n\n"
        "-----------------------------------------------------------------------\n"
        "SCENARIO 2 (Finding Physical CG Distance from % MAC):\n"
        "QUESTION: If the certified forward limit is 18% MAC, at what distance from the datum is the forward limit located?\n\n"
        "SOLUTION PASO A PASO:\n"
        "Step 1: Convert percentage to decimal: 18% = 0.18.\n"
        "Step 2: Multiply decimal by MAC length: 0.18 x 4.0 m = 0.72 meters aft of LEMAC.\n"
        "Step 3: Add this distance to LEMAC: 14.0 m + 0.72 m = 14.72 meters.\n"
        "FINAL ANSWER: Forward CG Limit is at 14.72 m aft of Datum.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "TEMAC and MAC Length Trap",
        "- If an exam question gives you LEMAC and TEMAC instead of MAC length:\n"
        "- Formula: Length of MAC = TEMAC - LEMAC!\n"
        "- E.g. If LEMAC = 500 inches and TEMAC = 700 inches, the MAC length is 200 inches.",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: If LEMAC is at station 20 m and TEMAC is at station 25 m, what is the length of the Mean Aerodynamic Chord (MAC)?",
         "[A] 45 m\n[B] 5 m\n[C] 22.5 m\n[D] 10 m",
         "CORRECT: [B]. MAC Length = TEMAC - LEMAC = 25 m - 20 m = 5 meters."),
        ("Q2: An aircraft has LEMAC at 1,000 inches and MAC length of 150 inches. If the CG is at 26% MAC, what is the CG station distance from datum?",
         "[A] 1,039 inches\n[B] 1,026 inches\n[C] 1,150 inches\n[D] 1,015 inches",
         "CORRECT: [A]. CG = LEMAC + (% MAC / 100 x MAC) = 1,000 + (0.26 x 150) = 1,000 + 39 = 1,039 inches."),
        ("Q3: Why does flying with a Center of Gravity at the AFT limit result in lower fuel consumption than at the FORWARD limit?",
         "[A] The engines produce more thrust\n[B] Less tailplane download is required to balance the aircraft, which reduces total lift required and lowers induced trim drag\n[C] The aircraft flies at lower TAS\n[D] Air density increases",
         "CORRECT: [B]. At an aft CG, the nose-down pitching moment is small, requiring a smaller downward balancing force from the horizontal stabilizer. Lower total lift required means lower induced trim drag, saving fuel.")
    ]

    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"M&B Chapter 3 compiled: {pdf_path}")


def build_mb_ch04():
    pdf_path = os.path.join(OUTPUT_DIR, "031_ch04_mass_shifts_additions.pdf")
    pdf = PDFBuilder("Mass and Balance", "031", "Chapter 4: Mass Shifts & Ballast")

    pdf.add_title_banner(
        "Mass and Balance",
        4,
        "Mass Shifts, Load Changes & Ballast Calculations",
        "67-88"
    )

    pdf.add_heading_1("1. The Fundamental Mass Shift Formula")
    pdf.add_paragraph(
        "When an item of mass already on board is moved from one compartment to another, the aircraft's Total Mass DOES NOT CHANGE, "
        "but the Center of Gravity shifts in the direction of the movement!"
    )
    pdf.add_bullet("The Universal Mass Shift Formula", "(Mass Shifted (m)) / (Total Aircraft Mass (M)) = (Change in CG (Delta CG)) / (Distance Shifted (d))")
    pdf.add_bullet("Solving for Delta CG", "Delta CG = (m x d) / M")
    pdf.add_bullet("Solving for Mass to Shift (m)", "m = (M x Delta CG) / d")
    pdf.add_bullet("Solving for Distance to Shift (d)", "d = (M x Delta CG) / m")

    pdf.add_heading_1("2. Adding or Removing Mass")
    pdf.add_paragraph(
        "When mass is added or removed, Total Mass CHANGES. Use the Moment equation:"
    )
    pdf.add_bullet("New CG Equation", "New CG = (Old Total Moment +- Added/Removed Moment) / (Old Total Mass +- Added/Removed Mass)")

    pdf.add_heading_1("3. Ballast Calculations (Correcting Out-of-Limits CG)")
    pdf.add_paragraph(
        "If an empty or lightly loaded ferry flight has a CG aft of the aft limit, ballast mass must be loaded into a forward cargo bay to bring the CG exactly onto the limit:"
    )
    pdf.add_bullet("Ballast Formula", "Ballast Mass (m_b) = (Total Mass x (Current CG - Desired Limit CG)) / (Desired Limit CG - Ballast Arm)")

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Cargo Shift to Bring CG to Forward Limit",
        "SCENARIO (Extremely Common AviationExam Question):\n"
        "An aircraft has:\n"
        "- Total Mass (M): 60,000 kg\n"
        "- Current CG position: 22.0 meters aft of datum\n"
        "- Certified Aft CG Limit: 21.6 meters aft of datum (The aircraft is 0.4 m OUT OF LIMITS!)\n"
        "- Forward Cargo Hold is at: 10.0 meters aft of datum\n"
        "- Aft Cargo Hold is at: 30.0 meters aft of datum\n"
        "QUESTION: How much cargo mass must be shifted from the Aft Cargo Hold to the Forward Cargo Hold to bring the CG to the Aft Limit of 21.6 m?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Identify all known variables:\n"
        "  - Total Mass (M) = 60,000 kg\n"
        "  - Desired change in CG (Delta CG) = Current CG - Target CG = 22.0 m - 21.6 m = 0.40 meters.\n"
        "  - Distance of shift (d) = Distance from Aft Hold to Fwd Hold = 30.0 m - 10.0 m = 20.0 meters.\n\n"
        "Step 2: Recall the Master Shift Formula:\n"
        "  - m / M = Delta CG / d  ->  m = (M x Delta CG) / d\n\n"
        "Step 3: Plug in the numbers and calculate:\n"
        "  - m = (60,000 kg x 0.40 m) / 20.0 m\n"
        "  - m = 24,000 / 20.0 = 1,200 kg.\n\n"
        "FINAL ANSWER: You must shift exactly 1,200 kg of cargo from the Aft Hold to the Forward Hold!",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Direction of Shift Trap",
        "- Shifting mass FORWARD moves the aircraft CG FORWARD (decreases CG distance from nose).\n"
        "- Shifting mass AFT moves the aircraft CG REARWARD (increases CG distance from nose).\n"
        "- Distance of shift (d) is ALWAYS the positive physical distance between the two compartments: d = |Hold_A - Hold_B|.",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: An aircraft has a gross mass of 5,000 kg and CG at station 120 inches. If 100 kg of baggage is shifted from station 150 inches to station 50 inches, what is the new CG position?",
         "[A] 118 inches\n[B] 115 inches\n[C] 122 inches\n[D] 110 inches",
         "CORRECT: [A]. Shift distance d = 150 - 50 = 100 inches (forward). Delta CG = (m x d) / M = (100 kg x 100 in) / 5,000 kg = 10,000 / 5,000 = 2.0 inches forward. New CG = 120 - 2.0 = 118 inches."),
        ("Q2: In mass shift calculations, what happens to the total mass of the aircraft?",
         "[A] It increases by the amount of mass moved\n[B] It decreases\n[C] It remains EXACTLY CONSTANT\n[D] It shifts by Delta CG",
         "CORRECT: [C]. Moving an object from one cabin location to another redistributes internal forces but does not add or subtract mass. Total aircraft mass M remains constant."),
        ("Q3: If 500 kg of cargo is REMOVED from a cargo bay located forward of the aircraft's current CG, what will happen to the CG position?",
         "[A] It will move forward\n[B] It will move REARWARD (aft)\n[C] It will remain stationary\n[D] It becomes negative",
         "CORRECT: [B]. Removing mass from in front of the CG takes away forward weight, causing the remaining balance to tilt backwards (CG moves aft).")
    ]

    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"M&B Chapter 4 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_mb_ch01()
    build_mb_ch02()
    build_mb_ch03()
    build_mb_ch04()
