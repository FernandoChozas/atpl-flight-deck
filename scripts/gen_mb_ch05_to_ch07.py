#!/usr/bin/env python3
"""
Generator for Subject 031: Mass and Balance
Volume 2: Chapters 5 to 7
- Chapter 5: Fuel Load Planning & Non-Linear CG Movement
- Chapter 6: Standard Masses & Cargo Compartment Limits (Floor / Running Load)
- Chapter 7: Load and Trim Sheet Execution & STAB TRIM Setting

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Mass & Balance and EASA AIR-OPS (CAT.POL.MAB).
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_3/031_mass_and_balance"

def build_mb_ch05():
    pdf_path = os.path.join(OUTPUT_DIR, "031_ch05_fuel_management_cg.pdf")
    pdf = PDFBuilder("Mass and Balance", "031", "Chapter 5: Fuel Planning & CG Movement")

    pdf.add_title_banner(
        "Mass and Balance",
        5,
        "Fuel Planning & Non-Linear CG Movement",
        "89-106"
    )

    pdf.add_heading_1("1. Fuel Tanks Geometry & CG Shift in Flight")
    pdf.add_paragraph(
        "Unlike passenger mass or cargo which remain stationary in flight, fuel mass decreases continuously throughout the trip. "
        "Because fuel tanks have complex 3D shapes across swept wings, fuel consumption causes non-linear Center of Gravity movement:"
    )
    pdf.add_bullet("Swept-Wing Fuel Tank Arm", "As wings sweep backwards, wingtip tanks are located significantly further AFT than the wing root center tank. Burning fuel from different tanks dramatically moves the aircraft CG forward or aft!")
    pdf.add_bullet("Wing Bending Relief & Standard Burn Sequence", "To minimize structural wing root bending moments, commercial jets burn fuel in a strict sequence: CENTER TANK FIRST, WING TANKS LAST! Burning the fuselage center tank first relieves wing-root stress because fuel weight inside the wings counteracts aerodynamic upward wing lift.")
    pdf.add_bullet("Unusable Fuel (Trapped Fuel)", "Fuel remaining in pipework, pumps, and tank bottoms that cannot be drained into engines during flight. REGULATION: Unusable fuel is legally part of BASIC EMPTY MASS (BEM)! It is NEVER counted as usable trip fuel.")

    pdf.add_heading_1("2. In-Flight Fuel Jettison (Fuel Dumping)")
    pdf.add_paragraph(
        "If a heavy aircraft experiences an emergency immediately after take-off, it may be above its Maximum Structural Landing Mass (MLM):"
    )
    pdf.add_bullet("Fuel Jettison System", "Dumps fuel overboard through wingtip nozzles to reduce aircraft mass down to MLM. Jettison valves close automatically to preserve reserve fuel (minimum holding fuel to land).")
    pdf.add_bullet("CG Impact of Jettisoning", "Because jettisoning typically empties center tanks and outer wing tanks rapidly, the flight crew must monitor that the CG remains strictly within the certified in-flight envelope during dumping.")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Tracking CG Movement from Take-Off to Landing",
        "SCENARIO (Typical Exam Question):\n"
        "An aircraft departs with:\n"
        "- Take-Off Mass (TOM): 50,000 kg\n"
        "- Take-Off CG: 18.00 meters aft of datum\n"
        "- Total Take-Off Moment = 50,000 x 18.00 = 900,000 kg.m\n"
        "- Trip Fuel to be burned in flight: 8,000 kg\n"
        "- The average Arm of the burned fuel is: 21.00 meters aft of datum (located AFT of the CG!)\n"
        "QUESTION: Calculate the aircraft's Landing Mass (LM) and the new Landing CG position.\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate Landing Mass (LM):\n"
        "  - LM = TOM - Trip Fuel = 50,000 kg - 8,000 kg = 42,000 kg.\n\n"
        "Step 2: Calculate the Moment of the Burned Fuel:\n"
        "  - Fuel Moment = Fuel Mass x Fuel Arm = 8,000 kg x 21.00 m = 168,000 kg.m.\n\n"
        "Step 3: Subtract the burned fuel moment from the Take-Off Moment:\n"
        "  - Landing Moment = Take-Off Moment - Fuel Moment\n"
        "  - Landing Moment = 900,000 kg.m - 168,000 kg.m = 732,000 kg.m.\n\n"
        "Step 4: Divide Landing Moment by Landing Mass to find Landing CG:\n"
        "  - Landing CG = Landing Moment / Landing Mass\n"
        "  - Landing CG = 732,000 kg.m / 42,000 kg = 17.4285 m -> 17.43 meters aft of datum!\n\n"
        "PHYSICAL EXPLANATION FOR DUMMIES:\n"
        "Because the burned fuel was located at 21 m (AFT of the 18 m CG), burning it removed weight from the back of the airplane, causing the nose to tilt down and shifting the CG FORWARD from 18.00 m to 17.43 m!",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Non-Linear Fuel Curve Trap",
        "- Center tanks burn first -> CG typically moves AFT initially.\n"
        "- Wing tanks burn second -> Swept-wing fuel burn moves CG back FORWARD.\n"
        "- Exam Trap: You CANNOT assume that if Take-off CG and Landing CG are both within limits, the aircraft was in limits throughout the entire cruise! You must check the intermediate burn curve peak!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: Under EASA AIR-OPS, which category does 'UNUSABLE FUEL' belong to?",
         "[A] Trip Fuel\n[B] Contingency Fuel\n[C] BASIC EMPTY MASS (BEM)\n[D] Traffic Load",
         "CORRECT: [C]. Unusable fuel is the fuel trapped in pipes and tank sumps that cannot reach the engines. It is a permanent fluid load counted as part of the aircraft's Basic Empty Mass."),
        ("Q2: Why is fuel in commercial jet aircraft burned from the center fuselage tank before the wing tanks?",
         "[A] Center tank fuel spoils faster\n[B] Keeping fuel inside the wing tanks as long as possible provides upward inertia and wing bending relief against aerodynamic lift\n[C] The center pump has higher pressure\n[D] Wing tanks cannot be pressurized",
         "CORRECT: [B]. Wing fuel weight acts downward along the wingspan, opposing the upward aerodynamic lift, reducing wing-root bending stress. Emptying the center tank first maximizes this structural relief."),
        ("Q3: If fuel burned during cruise has an arm located AFT of the current Center of Gravity, what happens to the CG position as fuel burns?",
         "[A] The CG moves FORWARD\n[B] The CG moves rearward\n[C] The CG stays frozen\n[D] The CG becomes negative",
         "CORRECT: [A]. Removing mass from behind the pivot point causes the remaining balance to tilt forward, shifting the CG forward.")
    ]

    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"M&B Chapter 5 compiled: {pdf_path}")


def build_mb_ch06():
    pdf_path = os.path.join(OUTPUT_DIR, "031_ch06_standard_passenger_baggage_masses.pdf")
    pdf = PDFBuilder("Mass and Balance", "031", "Chapter 6: Standard Masses & Floor Limits")

    pdf.add_title_banner(
        "Mass and Balance",
        6,
        "Standard Masses, Floor Limits & Cargo Restraints",
        "107-124"
    )

    pdf.add_heading_1("1. EASA AIR-OPS Standard Passenger Masses")
    pdf.add_paragraph(
        "Commercial operators may use EASA standard passenger masses instead of weighing every individual passenger at the gate:"
    )

    pax_table = [
        ["Passenger Category", "All Flights (>= 30 Passenger Seats)", "Holiday Charter (>= 30 Seats)", "Aircraft with 1 to 19 Seats"],
        ["Male Passenger", "88 kg (including 6 kg hand luggage)", "83 kg", "96 kg (Male)"],
        ["Female Passenger", "70 kg (including 6 kg hand luggage)", "69 kg", "78 kg (Female)"],
        ["All Adults (No Gender Split)", "84 kg", "76 kg", "88 kg"],
        ["Children (2 to 11 years)", "35 kg", "35 kg", "35 kg"],
        ["Infants (Under 2 years)", "0 kg (if held on adult's lap)", "0 kg", "0 kg (Held on lap)"]
    ]
    pdf.add_table(["Passenger Category", "All Flights (>= 30 Passenger Seats)", "Holiday Charter (>= 30 Seats)", "Aircraft with 1 to 19 Seats"], pax_table, col_widths=[125.0, 140.0, 115.0, 115.0])

    pdf.add_heading_1("2. Cargo Compartment Limitations: Floor & Running Loads")
    pdf.add_paragraph(
        "Cargo holds are protected against structural collapse by two strict engineering limitations:"
    )
    pdf.add_bullet("Area Load Limit (Floor Intensity)", "Maximum allowable mass per unit surface area: kg/m^2 or lb/ft^2. Exceeding this punches through the floor panel! Formula: Load Intensity = Mass / Contact Area <= Floor Limit.")
    pdf.add_bullet("Running Load Limit (Linear Load Limit)", "Maximum allowable mass per unit length of fuselage: kg/m or lb/in. Exceeding this breaks the transverse fuselage frames! Formula: Linear Load = Mass / Length <= Running Limit.")
    pdf.add_bullet("Spreader Plates (Dunnage)", "If a dense, heavy box exceeds the floor load limit, placing rigid wooden or composite spreader plates beneath it increases the contact area, distributing the weight safely across multiple floor beams!")

    pdf.add_heading_1("3. Cargo Restraint & Tie-Down Load Factors")
    pdf.add_paragraph(
        "To prevent cargo breaking free during severe turbulence or emergency landing, lashings must restrain against design load factors (EASA CS-25): Forward: 9.0 g; Upward: 1.5 g; Sideward: 3.0 g; Aft: 1.5 g."
    )

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Checking Floor Load Limits & Spreader Sizing",
        "SCENARIO (Classic EASA Calculation Drill):\n"
        "A cargo compartment has the following certified structural limits:\n"
        "- Maximum Floor Load Limit: 600 kg/m^2\n"
        "- Maximum Running Load Limit: 400 kg/m\n"
        "A piece of industrial machinery has a mass of 1,200 kg.\n"
        "Its base dimensions are: Length = 2.0 meters, Width = 0.8 meters.\n"
        "QUESTION: Does this cargo exceed the Floor Load Limit or the Running Load Limit? If it exceeds, what is the MINIMUM contact area required using a spreader plate?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Check the Running Load Limit:\n"
        "  - Actual Linear Load = Mass / Length = 1,200 kg / 2.0 m = 600 kg/m.\n"
        "  - Certified Running Limit = 400 kg/m.\n"
        "  - VERDICT: 600 kg/m > 400 kg/m -> EXCEEDS RUNNING LOAD LIMIT by 200 kg/m!\n\n"
        "Step 2: Check the Floor Load (Area) Limit:\n"
        "  - Contact Area = Length x Width = 2.0 m x 0.8 m = 1.6 m^2.\n"
        "  - Actual Area Load Intensity = Mass / Area = 1,200 kg / 1.6 m^2 = 750 kg/m^2.\n"
        "  - Certified Floor Limit = 600 kg/m^2.\n"
        "  - VERDICT: 750 kg/m^2 > 600 kg/m^2 -> EXCEEDS FLOOR LOAD LIMIT by 150 kg/m^2!\n\n"
        "Step 3: Calculate Minimum Spreader Plate Area required:\n"
        "  - Area_min = Mass / Max Floor Limit = 1,200 kg / 600 kg/m^2 = 2.0 m^2.\n"
        "FINAL ANSWER: Both limits are exceeded! A spreader plate of AT LEAST 2.0 m^2 contact area and at least 3.0 m length (1,200/400) is mandatory.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Infant Mass & Hand Luggage Rules",
        "- Infant mass (under 2 years) is 0 kg ONLY if held on an adult's lap. If occupying an individual seat, child mass (35 kg) must be applied!\n"
        "- Hand luggage (6 kg) is ALREADY INCLUDED in the standard passenger mass (88 kg male = 82 kg person + 6 kg bag). Do not add 6 kg twice!",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: Under EASA AIR-OPS on an aircraft with 30 or more passenger seats, what is the standard mass for an adult male passenger on a normal scheduled flight?",
         "[A] 84 kg\n[B] 88 kg (including 6 kg hand luggage allowance)\n[C] 70 kg\n[D] 96 kg",
         "CORRECT: [B]. The EASA standard male passenger mass for aircraft with 30+ seats is 88 kg (82 kg body mass + 6 kg hand luggage)."),
        ("Q2: What is the primary operational purpose of placing 'SPREADER PLATES' (dunnage) under dense cargo in an aircraft hold?",
         "[A] To increase aircraft payload\n[B] To increase the effective contact surface area, reducing floor load intensity (kg/m^2) below the certified structural floor limit\n[C] To prevent fire\n[D] To move the CG forward",
         "CORRECT: [B]. Spreader plates distribute the concentrated downward weight of heavy, compact cargo across a wider surface area, ensuring local pressure does not exceed the floor structural limit."),
        ("Q3: Under CS-25 regulations, what is the forward ultimate inertia load factor that cargo tie-downs and restraints must be capable of withstanding?",
         "[A] 1.5 g\n[B] 3.0 g\n[C] 9.0 g forward\n[D] 20.0 g",
         "CORRECT: [C]. To protect occupants in an emergency landing, cargo restraints must hold cargo in place against a 9.0 g forward deceleration load factor.")
    ]

    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"M&B Chapter 6 compiled: {pdf_path}")


def build_mb_ch07():
    pdf_path = os.path.join(OUTPUT_DIR, "031_ch07_load_trim_sheet.pdf")
    pdf = PDFBuilder("Mass and Balance", "031", "Chapter 7: Load and Trim Sheet Execution")

    pdf.add_title_banner(
        "Mass and Balance",
        7,
        "Load & Trim Sheet Execution & STAB TRIM Setting",
        "125-144"
    )

    pdf.add_heading_1("1. The Architecture of the Load and Trim Sheet")
    pdf.add_paragraph(
        "The Load and Trim Sheet is the official legal document required before every commercial departure. It fulfills two vital safety functions:"
    )
    pdf.add_bullet("Mass Check (The Upper Section)", "Verifies that the aircraft does not exceed any of its 3 structural mass limits: Maximum Zero Fuel Mass (MZFM), Maximum Take-Off Mass (MTOM), and Maximum Landing Mass (MLM).")
    pdf.add_bullet("Balance & Trim Check (The Lower Section)", "Graphically plots the Center of Gravity using an 'Index Grid' (trim drop lines) to verify that the CG is inside the flight envelope and to read the Take-Off Stabilizer Trim setting (STAB TRIM in units ANU / AND).")

    pdf.add_heading_1("2. The Index System & Reduction Formula")
    pdf.add_paragraph(
        "Because raw moments on transport jets run into millions of kilogram-meters, calculations are simplified into small manageable 'Index Units':"
    )
    pdf.add_bullet("The Index Formula", "Index = ((Mass x (Arm - Reference Datum)) / Divisor (C)) + Constant (K)")
    pdf.add_bullet("Divisor (C)", "Typically 10,000 or 100,000. Reduces the large moment into a small 2 or 3 digit number.")
    pdf.add_bullet("Constant (K)", "A positive baseline offset (e.g. +50 or +100) added so that all calculated indices remain strictly positive numbers, eliminating negative calculation errors!")

    pdf.add_heading_1("3. Take-Off Stabilizer Trim (STAB TRIM Setting)")
    pdf.add_paragraph(
        "Before take-off, the trimmable horizontal stabilizer (THS) must be set to a specific pitch trim angle corresponding to the Take-Off % MAC:"
    )
    pdf.add_bullet("Aft CG -> Low Nose-Up Trim", "At an aft CG, the aircraft naturally pitches up easily. STAB TRIM is set to a low nose-up value (e.g. 3.0 units ANU).")
    pdf.add_bullet("Forward CG -> High Nose-Up Trim", "At a forward CG, heavy nose-down moments require a large nose-up stabilizer setting (e.g. 7.5 units ANU) to allow rotation at Vr without excessive pilot pull force!")

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Index & Reading Trim Sheet",
        "SCENARIO (Standard EASA Exam Trim Sheet Problem):\n"
        "An airline uses the following Index Reduction Formula for its twin-jet:\n"
        "  Index = [Mass (kg) x (Arm (m) - 15.0 m) / 1,000] + 50.0\n"
        "Given the following loading changes to the Dry Operating Index:\n"
        "- Dry Operating Mass (DOM): 32,000 kg with an Initial Index of 52.0 units\n"
        "- Cargo loaded in Compartment 1: 2,000 kg at Arm = 8.0 meters\n"
        "- Cargo loaded in Compartment 4: 1,500 kg at Arm = 22.0 meters\n"
        "QUESTION: Calculate the New Zero Fuel Mass (ZFM) and the New Zero Fuel Index!\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate New Zero Fuel Mass:\n"
        "  - ZFM = DOM + Compartment 1 + Compartment 4\n"
        "  - ZFM = 32,000 kg + 2,000 kg + 1,500 kg = 35,500 kg.\n\n"
        "Step 2: Calculate Delta Index for Compartment 1 (Arm = 8.0 m):\n"
        "  - Delta Index_1 = [Mass x (Arm - 15.0)] / 1,000\n"
        "  - Delta Index_1 = [2,000 x (8.0 - 15.0)] / 1,000 = [2,000 x (-7.0)] / 1,000 = -14.0 units!\n"
        "  - (Notice it is negative because the arm is forward of the 15.0 m reference!).\n\n"
        "Step 3: Calculate Delta Index for Compartment 4 (Arm = 22.0 m):\n"
        "  - Delta Index_4 = [Mass x (Arm - 15.0)] / 1,000\n"
        "  - Delta Index_4 = [1,500 x (22.0 - 15.0)] / 1,000 = [1,500 x (+7.0)] / 1,000 = +10.5 units!\n\n"
        "Step 4: Sum the Initial Index with both Delta Indices to find New ZFM Index:\n"
        "  - New ZFM Index = Initial Index + Delta Index_1 + Delta Index_4\n"
        "  - New ZFM Index = 52.0 + (-14.0) + (+10.5) = 48.5 units!\n\n"
        "FINAL ANSWER: New ZFM = 35,500 kg; New ZFM Index = 48.5 units. On the trim grid, enter at Index 48.5 to read % MAC.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "STAB TRIM Setting Units Trap (ANU vs AND)",
        "- ANU = Aircraft Nose Up (positive nose-up trim).\n"
        "- AND = Aircraft Nose Down.\n"
        "- Forward CG ALWAYS requires MORE ANU (higher nose-up stabilizer trim) to assist elevator rotation at Vr!",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: What is the primary purpose of using 'INDEX UNITS' instead of raw moments in aircraft load and trim sheets?",
         "[A] To convert metric units to imperial units\n[B] To reduce huge moment numbers (millions of kg.m) into manageable small numbers, preventing human calculation errors in time-critical airline turnarounds\n[C] To calculate cruise speed\n[D] To record passenger names",
         "CORRECT: [B]. Moments for transport airliners are enormous numbers. Dividing by a constant divisor (e.g. 10,000) and adding a base constant produces compact index values (e.g. 40-60) easily plotted on graphical grids."),
        ("Q2: When setting the Take-Off Stabilizer Trim (STAB TRIM) on a commercial transport jet, what setting is required if the aircraft is loaded with a FORWARD Center of Gravity?",
         "[A] Zero trim\n[B] A GREATER Aircraft Nose Up (ANU) trim setting, to counter heavy nose-down moments and ensure adequate elevator rotation authority at Vr\n[C] Full Aircraft Nose Down (AND) trim\n[D] Trim does not depend on CG",
         "CORRECT: [B]. A forward CG produces a large nose-down moment. A higher ANU (nose-up) stabilizer setting is mandatory so the pilot can rotate the nose at Vr without exceeding control column pull limits."),
        ("Q3: On a load and trim sheet, if an aircraft's Take-Off Mass is plotted and falls OUTSIDE the certified envelope boundary, what action is legally required?",
         "[A] Increase engine thrust to TOGA\n[B] Departure is STRICTLY PROHIBITED until payload or fuel is redistributed or offloaded to bring the point within the certified envelope\n[C] Notify ATC on climb out\n[D] Fly at a lower altitude",
         "CORRECT: [B]. Flying outside the M&B envelope is illegal and causes loss of control or structural overload. The flight crew must re-trim by shifting cargo, moving passengers, or offloading fuel before departure.")
    ]

    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"M&B Chapter 7 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_mb_ch05()
    build_mb_ch06()
    build_mb_ch07()
