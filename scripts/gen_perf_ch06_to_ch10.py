#!/usr/bin/env python3
"""
Generator for Subject 032: Performance
Volume 2: Chapters 6 to 10
- Chapter 6: Class A Take-Off Distances & Balanced Field Length
- Chapter 7: Class A Take-Off Flight Path & The 4 Climb Segments (Gross vs Net)
- Chapter 8: Class A En-Route Engine-Out Drift Down & Obstacle Clearance
- Chapter 9: Class A Landing Performance & Factored Distance Rules
- Chapter 10: Reduced Thrust (Flex Temp / Assumed Temperature) & Derated Thrust

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Performance and EASA CS-25 regulations.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_3/032_performance"

def build_perf_ch06():
    pdf_path = os.path.join(OUTPUT_DIR, "032_ch06_class_a_takeoff_distances_balanced_field.pdf")
    pdf = PDFBuilder("Performance", "032", "Chapter 6: Take-Off Distances & Balanced Field")

    pdf.add_title_banner(
        "Performance",
        6,
        "Class A Take-Off Distances & Balanced Field Length",
        "195-238"
    )

    pdf.add_heading_1("1. Declared Distances Architecture")
    pdf.add_paragraph(
        "Airport authorities declare four official runway distances that establish the take-off and landing boundaries:"
    )

    dist_table = [
        ["Declared Distance Code", "Physical Runway Components Included", "Regulatory Meaning & Usage"],
        ["TORA (Take-Off Run Available)", "Paved physical runway length suitable for normal ground run.", "Baseline distance for all wheel acceleration."],
        ["TODA (Take-Off Distance Available)", "TORA + Clearway (unobstructed water/grass area, max 50% TORA).", "Total distance to accelerate and climb to 35 ft screen height."],
        ["ASDA (Acc-Stop Distance Available)", "TORA + Stopway (load-bearing overrun strip suitable for abort).", "Total distance available to accelerate to V1 and stop completely."],
        ["LDA (Landing Distance Available)", "Paved runway from threshold to end of roll.", "Distance available for landing touch down and rollout."]
    ]
    pdf.add_table(["Declared Distance Code", "Physical Runway Components Included", "Regulatory Meaning & Usage"], dist_table, col_widths=[110.0, 210.0, 180.0])

    pdf.add_heading_1("2. The Balanced Field Length Concept")
    pdf.add_paragraph(
        "A runway is considered a 'Balanced Field' when: TODA equals ASDA (Clearway = Stopway)."
    )
    pdf.add_bullet("Balanced V1", "The unique decision speed where Accelerate-Stop Distance (reject at V1) EXACTLY EQUALS the One-Engine-Inoperative Take-off Distance (continue at V1 to 35 ft screen height)!")
    pdf.add_bullet("Variables that SHIFT V1", "Higher Mass -> Increases V1. Higher Flap Setting -> Decreases V1. Uphill Slope -> Increases V1. Headwind -> Decreases groundspeed at V1. Contaminated Runway (water/slush) -> DRATICALLY REDUCES V1 (because braking friction is degraded, you must abort earlier)!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Declared Distances & Clearway Limits",
        "SCENARIO (Standard EASA Airport Planning Drill):\n"
        "An airport publishes the following physical runway survey data:\n"
        "- Paved Runway length = 2,400 meters\n"
        "- Stopway paved overrun strip = 150 meters\n"
        "- Clearway unobstructed obstacle-free area = 1,400 meters\n"
        "QUESTION: What are the legal declared distances for TORA, ASDA, and TODA under EASA CS-25 rules?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate TORA (Take-Off Run Available):\n"
        "  - TORA is strictly the physical paved runway length = 2,400 meters.\n\n"
        "Step 2: Calculate ASDA (Accelerate-Stop Distance Available):\n"
        "  - ASDA = TORA + Stopway\n"
        "  - ASDA = 2,400 m + 150 m = 2,550 meters.\n\n"
        "Step 3: Calculate TODA (Take-Off Distance Available) with Clearway Limit Check:\n"
        "  - Rule: Clearway credit CANNOT EXCEED 50% of TORA!\n"
        "  - Maximum allowable clearway = 0.50 x 2,400 m = 1,200 meters.\n"
        "  - The physical clearway is 1,400 m, but we can ONLY LEGALLY CREDIT 1,200 meters!\n"
        "  - Legal TODA = TORA + Allowed Clearway = 2,400 m + 1,200 m = 3,600 meters!\n\n"
        "FINAL ANSWER: TORA = 2,400 m; ASDA = 2,550 m; TODA = 3,600 m (limited by the 50% clearway rule!).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Clearway 50% TORA Rule Trap",
        "- Even if an airport has 3 kilometers of open sea beyond the runway, you CANNOT add more than 50% of TORA to TODA!\n"
        "- E.g. If TORA = 2,000 m and Clearway = 1,500 m, TODA is NOT 3,500 m! TODA is capped at 2,000 + 1,000 = 3,000 m!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: What is the maximum clearway length that can legally be included in Take-Off Distance Available (TODA)?",
         "[A] Unlimited\n[B] Not more than 50% of TORA\n[C] Equal to the stopway length\n[D] 1,000 ft",
         "CORRECT: [B]. Under CS-25 and ICAO Annex 14, the length of clearway that can be credited to determine TODA must not exceed half the length of TORA."),
        ("Q2: In a 'Balanced Field Length' take-off calculation, which two distances are equal?",
         "[A] TORA and LDA\n[B] The Accelerate-Stop Distance and the One-Engine-Inoperative Take-Off Distance to 35 ft\n[C] Ground roll and climb distance\n[D] Clearway and runway length",
         "CORRECT: [B]. A balanced field exists when the distance required to accelerate to V1 and stop equals the distance required to accelerate, lose an engine at V1, and reach screen height."),
        ("Q3: How does CONTAMINATION (e.g. 5 mm standing water) affect the optimal V1 decision speed?",
         "[A] Increases V1\n[B] SUBSTANTIALLY DECREASES V1, because degraded wheel braking requires aborting earlier, and remaining runway allows continued take-off to a reduced 15 ft screen height\n[C] Has zero effect\n[D] Eliminates V1",
         "CORRECT: [B]. On contaminated runways, braking friction is severely reduced. V1 must be reduced to allow stopping within ASDA if an abort occurs; screen height for continue is lowered to 15 ft.")
    ]

    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Performance Chapter 6 compiled: {pdf_path}")


def build_perf_ch07():
    pdf_path = os.path.join(OUTPUT_DIR, "032_ch07_class_a_takeoff_climb_segments.pdf")
    pdf = PDFBuilder("Performance", "032", "Chapter 7: Take-Off Climb Segments")

    pdf.add_title_banner(
        "Performance",
        7,
        "Class A Take-Off Flight Path & 4 Climb Segments",
        "239-282"
    )

    pdf.add_heading_1("1. The Net Flight Path & The 4 Climb Segments")
    pdf.add_paragraph(
        "The take-off flight path begins at 35 ft screen height (dry) or 15 ft (wet) with one engine inoperative, continuing to 1,500 ft AGL. "
        "It is divided into four distinct aerodynamic segments:"
    )

    segments_table = [
        ["Climb Segment", "Physical Boundaries & Speeds", "Aircraft Configuration & Min Gross Gradient (Twins)"],
        ["1st Segment", "35 ft screen height to Gear Retraction fully complete. Speed = V2.", "Take-off flaps, gear extending/retracting, Take-Off Thrust (TOGA). Min Gross Gradient: Positive (>= 0.0%)."],
        ["2nd Segment (CRITICAL!)", "Gear Retracted up to Acceleration Height (min 400 ft AGL). Speed = V2.", "Take-off flaps, gear UP, TOGA thrust. Min Gross Gradient: 2.4% for twins (3.0% for quads) -- THE MOST STRINGENT!"],
        ["3rd Segment (Acceleration)", "Level acceleration flight at min 400 ft AGL. Speed accelerates from V2 to V_FTO.", "Flaps retracting sequentially, gear UP, TOGA thrust. Min Gross Gradient: Acceleration equivalent."],
        ["4th Segment (Final)", "From Acceleration Height to min 1,500 ft AGL. Speed = V_FTO (Final Take-Off Speed).", "Clean configuration (flaps UP), gear UP, Max Continuous Thrust (MCT). Min Gross Gradient: 1.2% for twins."]
    ]
    pdf.add_table(["Climb Segment", "Physical Boundaries & Speeds", "Aircraft Configuration & Min Gross Gradient (Twins)"], segments_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_heading_1("2. Gross vs Net Take-Off Flight Path")
    pdf.add_paragraph(
        "Obstacle clearance calculations are NOT based on actual test flight performance (Gross):"
    )
    pdf.add_bullet("Gross Flight Path", "The actual climb performance achieved by a skilled test pilot in a brand-new aircraft.")
    pdf.add_bullet("Net Flight Path (EASA Deduction)", "Gross flight path reduced by a mandatory regulatory penalty to account for engine wear and pilot technique: Deduct 0.8% for twin-engine jets! (Deduct 0.9% for 3-engines, 1.0% for 4-engines).")
    pdf.add_bullet("Obstacle Clearance Margins", "The Net Flight Path must clear all ground obstacles by at least: 35 ft vertically in straight flight, or 50 ft vertically during turns (max bank angle 15°)! The wings must clear terrain horizontally by at least 90 m (or 300 m if radar tracking unavailable).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Net Flight Path Obstacle Clearance",
        "SCENARIO (Classic CS-25 Obstacle Clearance Problem):\n"
        "A twin-engine jet takes off with an engine failure at V1:\n"
        "- Screen height (35 ft = 10.7 m) reached at end of TODA\n"
        "- In the 2nd segment, the aircraft achieves a Gross Climb Gradient of 2.8%\n"
        "- An obstacle of height 180 ft (55.0 m) is located 3,000 meters beyond the end of TODA\n"
        "QUESTION: What is the NET climb gradient, and what is the aircraft's NET clearance over the obstacle?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the NET Climb Gradient (Deduct 0.8% for twins!):\n"
        "  - Gross Gradient = 2.8%\n"
        "  - Net Penalty (CS-25 twin) = -0.8%\n"
        "  - Net Gradient = 2.8% - 0.8% = 2.0% (0.020).\n\n"
        "Step 2: Calculate the Net Altitude Gained over the 3,000 m distance to obstacle:\n"
        "  - Net Altitude Gained = Horizontal Distance x Net Gradient\n"
        "  - Net Altitude Gained = 3,000 m x 0.020 = 60.0 meters.\n\n"
        "Step 3: Calculate the Net Aircraft Height at the obstacle position:\n"
        "  - Net Height = Initial Screen Height (10.7 m) + Net Altitude Gained (60.0 m)\n"
        "  - Net Height = 10.7 m + 60.0 m = 70.7 meters (approx 232 ft).\n\n"
        "Step 4: Check Clearance Margin above the Obstacle:\n"
        "  - Obstacle Height = 55.0 meters (180 ft)\n"
        "  - Net Clearance = Net Aircraft Height - Obstacle Height\n"
        "  - Net Clearance = 70.7 m - 55.0 m = 15.7 meters (51.5 ft)!\n\n"
        "Step 5: Verify Legal Margin (Must be >= 35 ft):\n"
        "  - Since 51.5 ft > 35 ft, the aircraft legally clears the obstacle!\n"
        "FINAL ANSWER: Net Climb Gradient = 2.0%. Net Clearance = 15.7 m (51.5 ft), which comfortably exceeds the 35 ft legal requirement.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The 2nd Segment Gradient Trap",
        "- The 2nd segment is the MOST CRITICAL climb segment in ATPL exams!\n"
        "- Twin-engine minimum gross gradient = 2.4% (Net = 1.6%).\n"
        "- If high elevation or hot temperatures degrade climb below 2.4%, Take-Off Mass MUST be reduced, even on an infinitely long runway!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: Under CS-25, what is the mandatory Gross to Net gradient deduction for a TWIN-ENGINE transport aircraft during take-off climb?",
         "[A] 0.5%\n[B] 0.8% gradient reduction\n[C] 1.0%\n[D] 1.5%",
         "CORRECT: [B]. CS-25 mandates a gradient penalty of 0.8% for 2-engine aircraft, 0.9% for 3-engine aircraft, and 1.0% for 4-engine aircraft to convert gross flight paths into legal net flight paths."),
        ("Q2: What is the minimum required GROSS climb gradient in the SECOND SEGMENT for a twin-turbofan aircraft with one engine inoperative?",
         "[A] 0.0%\n[B] 2.4% gross climb gradient\n[C] 1.2%\n[D] 3.0%",
         "CORRECT: [B]. In the second segment (gear up, flaps take-off, V2, TOGA thrust), a twin must achieve at least a 2.4% gross climb gradient (yielding a 1.6% net gradient)."),
        ("Q3: What is the minimum vertical obstacle clearance required between the NET take-off flight path and an obstacle in straight flight?",
         "[A] 50 ft\n[B] 35 ft vertical clearance\n[C] 100 ft\n[D] Zero",
         "CORRECT: [B]. CS-25 requires the net take-off flight path to clear all obstacles by at least 35 ft vertically in wings-level flight (increased to 50 ft during turns).")
    ]

    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Performance Chapter 7 compiled: {pdf_path}")


def build_perf_ch08():
    pdf_path = os.path.join(OUTPUT_DIR, "032_ch08_class_a_enroute_engine_out_driftdown.pdf")
    pdf = PDFBuilder("Performance", "032", "Chapter 8: En-Route Drift Down")

    pdf.add_title_banner(
        "Performance",
        8,
        "Class A En-Route Engine-Out Drift Down & Obstacles",
        "283-316"
    )

    pdf.add_heading_1("1. The Engine Failure in Cruise Physics")
    pdf.add_paragraph(
        "When an engine fails during cruise at high altitude (e.g. FL 370), the aircraft cannot maintain altitude because drag at that level exceeds maximum continuous thrust (MCT) of the remaining engine:"
    )
    pdf.add_bullet("Drift Down Procedure", "The aircraft trades potential energy (altitude) for kinetic energy (airspeed), descending gradually at optimal single-engine speed (V_md / LRC speed) to maximize distance flown during descent toward the stabilizing ceiling.")
    pdf.add_bullet("Stabilizing Altitude (OEI Ceiling)", "The level altitude where remaining engine thrust at MCT exactly balances aircraft drag. As fuel burns off and the aircraft gets lighter, the stabilizing ceiling gradually climbs!")
    pdf.add_bullet("Net En-Route Flight Path (1.1% Deduction)", "Under CS-25 for twin-engine aircraft, the net en-route flight path is derived by deducting a 1.1% climb gradient penalty from gross data (1.4% for 3-engine, 1.6% for 4-engine).")

    pdf.add_heading_1("2. En-Route Obstacle Clearance Requirements")
    pdf.add_paragraph(
        "Under EASA AIR-OPS (CAT.POL.A.215), the one-engine-inoperative net drift-down flight path must clear all high terrain and obstacles within 10 NM of the route centerline by AT LEAST 2,000 FT VERTICALLY!"
    )

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Verifying Drift Down Terrain Clearance",
        "SCENARIO (Alpine Mountain Crossing Drift Down Drill):\n"
        "A twin-jet airliner is cruising at FL 350 over the Alps:\n"
        "- An engine fails at point A\n"
        "- The OEI drift-down table shows that the net flight path passes through 14,500 ft MSL at the critical ridge\n"
        "- The highest mountain peak within 10 NM of track has an elevation of 12,200 ft MSL\n"
        "QUESTION: Is the drift-down flight path legal under EASA CAT.POL.A.215 regulations?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Identify the mandatory EASA terrain clearance margin:\n"
        "  - Required Vertical Clearance = 2,000 ft above terrain within 10 NM of track.\n\n"
        "Step 2: Calculate the Minimum Allowable Net Flight Path Altitude:\n"
        "  - Min Net Altitude = Peak Elevation + Required Clearance\n"
        "  - Min Net Altitude = 12,200 ft + 2,000 ft = 14,200 ft MSL.\n\n"
        "Step 3: Compare Actual Net Altitude with Minimum Required Altitude:\n"
        "  - Aircraft Net Altitude at Ridge = 14,500 ft MSL\n"
        "  - Minimum Required Altitude = 14,200 ft MSL\n"
        "  - Actual Vertical Margin = 14,500 ft - 12,200 ft = 2,300 ft!\n\n"
        "Step 4: Check Compliance:\n"
        "  - 2,300 ft > 2,000 ft legal requirement -> COMPLIANT!\n"
        "FINAL ANSWER: Yes, the flight path is legal. The aircraft clears the peak with 2,300 ft net margin, exceeding the 2,000 ft regulatory requirement.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The 10 NM Corridor & 2,000 ft Margin Trap",
        "- Obstacle search corridor width is 10 NM ON EITHER SIDE of track (20 NM total width).\n"
        "- Clearance requirement is 2,000 ft (NOT 1,000 ft!). 1,000 ft is only permitted if the aircraft has reached its level stabilizing altitude and navigational accuracy is within 95%.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: Under EASA regulations, by what vertical margin must the OEI NET flight path clear all obstacles within 10 NM of track during en-route drift down?",
         "[A] 500 ft\n[B] At least 2,000 ft vertically\n[C] 1,000 ft\n[D] 35 ft",
         "CORRECT: [B]. CAT.POL.A.215 requires the one-engine-inoperative net flight path to have a positive slope at least 2,000 ft above all terrain within 10 NM on each side of the intended track."),
        ("Q2: What is the regulatory gradient penalty applied to gross drift down performance to obtain the NET drift down profile for a twin-engine jet?",
         "[A] 0.5%\n[B] 1.1% gradient deduction\n[C] 2.0%\n[D] Zero",
         "CORRECT: [B]. CS-25 requires deducting 1.1% from gross climb/descent gradient data for twin-engine aircraft during the en-route phase."),
        ("Q3: What speed should the flight crew fly to maximize distance traveled during an engine-out drift down?",
         "[A] Maximum operating Mach (Mmo)\n[B] The single-engine drift down speed (approx Vmd / Long Range Cruise speed)\n[C] Stall speed\n[D] Minimum clean speed",
         "CORRECT: [B]. Flying at the speed for minimum drag (Vmd) yields the maximum lift-to-drag ratio (L/D max), resulting in the shallowest glide angle and maximum distance to the OEI ceiling.")
    ]

    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Performance Chapter 8 compiled: {pdf_path}")


def build_perf_ch09():
    pdf_path = os.path.join(OUTPUT_DIR, "032_ch09_class_a_landing_performance.pdf")
    pdf = PDFBuilder("Performance", "032", "Chapter 9: Class A Landing Performance")

    pdf.add_title_banner(
        "Performance",
        9,
        "Class A Landing Performance & Factored Distance",
        "317-360"
    )

    pdf.add_heading_1("1. Class A Landing Requirements & Screen Height")
    pdf.add_paragraph(
        "Class A landing performance begins at a screen height of 50 ft above the runway threshold at target approach speed Vref:"
    )
    pdf.add_bullet("Reference Landing Speed (Vref)", "Target speed over threshold: Vref MUST BE AT LEAST 1.23 x Vsr0 (stall speed in landing configuration).")
    pdf.add_bullet("Landing Distance Available (LDA)", "The physical paved runway declared available from threshold to end of roll.")
    pdf.add_bullet("The 60% Rule (Dry Runway Factor x 1.67)", "Under EASA CAT.POL.A.230, a turbojet aircraft must be capable of landing from 50 ft to a complete stop within 60% OF THE LDA! Therefore: Required Factored Landing Distance = Actual Measured Distance / 0.60 = Actual Distance x 1.67.")
    pdf.add_bullet("Wet Runway Factor (x 1.15 of Dry = x 1.92 Total!)", "If the runway is forecast to be wet or slippery at ETA, the required landing distance is 115% OF THE FACTORED DRY DISTANCE: Required Wet Landing Distance = Actual Distance x 1.67 x 1.15 = Actual Distance x 1.92!")

    pdf.add_heading_1("2. Reverse Thrust Regulatory Credit")
    pdf.add_paragraph(
        "Under CS-25 certification for dispatch purposes, NO CREDIT is permitted for thrust reversers on dry or wet runways! "
        "The aircraft must be capable of stopping using wheel brakes and aerodynamic spoilers alone. (Reverse thrust credit is only considered in non-normal in-flight assessments or contaminated runway models).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Dispatch Landing Distance Check Dry vs Wet",
        "SCENARIO (Commercial Airline Dispatch Drill):\n"
        "A Boeing 737 is dispatching to a destination with a Landing Distance Available (LDA) of 2,200 meters:\n"
        "- Flight Manual Unfactored Landing Distance from 50 ft = 1,200 meters\n"
        "- Destination forecast: Rain showers at ETA (Runway WET!)\n"
        "QUESTION: What is the Required Dry Landing Distance? What is the Required Wet Landing Distance? Can the aircraft legally dispatch?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate Required DRY Landing Distance (The 60% Rule = x 1.67):\n"
        "  - Required Dry Distance = Actual Distance / 0.60 = 1,200 m / 0.60 = 2,000 meters.\n"
        "  - (On a dry runway, 2,000 m <= 2,200 m LDA -> Legal for dry runway).\n\n"
        "Step 2: Calculate Required WET Landing Distance (Apply 115% factor to Dry):\n"
        "  - Required Wet Distance = Required Dry Distance x 1.15\n"
        "  - Required Wet Distance = 2,000 m x 1.15 = 2,300 meters!\n"
        "  - (Notice: 1,200 m x 1.92 = 2,304 meters).\n\n"
        "Step 3: Compare Required Wet Distance with Runway LDA:\n"
        "  - Required Wet Distance = 2,300 meters\n"
        "  - Available LDA = 2,200 meters\n"
        "  - Verdict: 2,300 m > 2,200 m -> EXCEEDS AVAILABLE RUNWAY BY 100 METERS!\n\n"
        "FINAL ANSWER: The aircraft CANNOT legally dispatch! Landing mass must be reduced, or an alternate destination selected.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The 60% Rule vs 1.67 Factor Distinction Trap",
        "- Stating 'Actual distance must not exceed 60% of LDA' is mathematically identical to stating 'Required LDA must be at least Actual distance multiplied by 1.67 (1 / 0.60 = 1.667)'!\n"
        "- For Wet runways, multiply by 1.92 total! Always check whether the exam question asks for DRY or WET!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch09 = [
        ("Q1: Under EASA CS-25, what is the minimum approach speed (Vref) over the runway threshold for a commercial turbojet?",
         "[A] Vref >= 1.23 x Vsr0 (stall speed in landing configuration)\n[B] Vref = Vsr0\n[C] Vref = 1.10 x Vmca\n[D] Exactly 140 kt",
         "CORRECT: [A]. CS-25.125 requires that Vref be at least 23% above the reference stall speed in the landing configuration: Vref >= 1.23 Vsr0."),
        ("Q2: For a commercial turbojet landing on a DRY runway, what proportion of the Landing Distance Available (LDA) is the unfactored landing distance permitted to consume?",
         "[A] Exactly 50%\n[B] Not more than 60% of the LDA (factoring distance by 1.67)\n[C] 70%\n[D] 100%",
         "CORRECT: [B]. Under CAT.POL.A.230, the landing distance from 50 ft must not exceed 60% of LDA, ensuring a 40% runway safety buffer."),
        ("Q3: When calculating dispatch landing performance on a WET runway under CS-25, what additional factor is applied to the factored dry landing distance?",
         "[A] 10%\n[B] An additional 15% (giving a total factor of 1.92 times actual distance)\n[C] 30%\n[D] Zero factor",
         "CORRECT: [B]. A wet runway requires a 15% increase over the dry factored distance (Factored Dry x 1.15), reflecting reduced wet tire friction.")
    ]

    for q_text, opts, exp in questions_ch09:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Performance Chapter 9 compiled: {pdf_path}")


def build_perf_ch10():
    pdf_path = os.path.join(OUTPUT_DIR, "032_ch10_reduced_thrust_flexible_takeoff.pdf")
    pdf = PDFBuilder("Performance", "032", "Chapter 10: Reduced & Derated Thrust")

    pdf.add_title_banner(
        "Performance",
        10,
        "Reduced & Derated Take-Off Thrust (Flex Temp)",
        "361-402"
    )

    pdf.add_heading_1("1. Why Use Reduced Thrust?")
    pdf.add_paragraph(
        "Jet engines deteriorate primarily due to high Turbine Gas Temperature (EGT) during take-off at full rated power. "
        "When an aircraft is light or runway is long, taking off with reduced thrust saves substantial engine overhaul costs and increases reliability without compromising safety!"
    )

    pdf.add_heading_1("2. The Assumed Temperature Method (Flex Temp)")
    pdf.add_paragraph(
        "Modern turbofans are 'flat-rated' up to a corner point temperature (T_ref, typically ISA + 15°C / ~30°C). Above T_ref, engine thrust drops automatically to protect turbine blades from over-temperature:"
    )
    pdf.add_bullet("The Flex Principle", "The pilot enters an artificial, fictitiously HIGH outside temperature (e.g. Assumed Temp = +52°C, when actual OAT is +20°C). The FADEC commands reduced take-off N1/EPR matching performance on a hot day!")
    pdf.add_bullet("The 25% Maximum Reduction Limit", "REGULATORY LIMIT: Reduced thrust MUST NOT BE LESS than 75% of maximum rated take-off thrust! (Maximum allowable thrust reduction is 25%!).")
    pdf.add_bullet("Assumed Temp Prohibitions", "The Assumed Temperature Method is STRICTLY FORBIDDEN: (1) On contaminated runways (standing water, slush, ice), (2) When antiskid is inoperative, (3) When windshear is reported or suspected!")

    pdf.add_heading_1("3. Assumed Temperature vs Fixed Derated Thrust")
    derate_table = [
        ["Thrust Reduction Method", "Certification Status & Minimum Control Speeds", "Pilot Operating Authority in Cockpit"],
        ["Assumed Temperature (Flex)", "Certified at full rated thrust. Minimum control speeds (Vmcg, Vmca) are based on FULL RATED THRUST.", "Pilot MAY advance thrust levers to full TOGA at any time during take-off!"],
        ["Fixed Derate (Derated Thrust)", "Certified as a completely separate, lower-rated engine (e.g. 24k rating derated to 22k). Vmcg and Vmca are LOWER!", "Pilot MUST NOT push levers to full TOGA below Vmca (doing so risks violent loss of directional control)!"]
    ]
    pdf.add_table(["Thrust Reduction Method", "Certification Status & Minimum Control Speeds", "Pilot Operating Authority in Cockpit"], derate_table, col_widths=[125.0, 195.0, 180.0])

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Checking Assumed Temperature Feasibility",
        "SCENARIO (Airline Dispatch Problem):\n"
        "An Airbus A320 is operating from a 3,500 m runway:\n"
        "- Actual Outside Air Temperature (OAT): +18°C\n"
        "- Flat-rated corner temperature (T_ref): +30°C\n"
        "- Performance tables indicate aircraft can take off safely at current mass up to an assumed temperature of +54°C\n"
        "- Full rated thrust produces 120 kN per engine\n"
        "- At +54°C assumed temperature, thrust output is 93 kN per engine\n"
        "QUESTION: Can this take-off be conducted legally using Assumed Temperature? What is the percentage thrust reduction?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Check Condition 1: Is Assumed Temperature HIGHER than actual OAT?\n"
        "  - Assumed Temp (+54°C) > Actual OAT (+18°C) -> PASSED!\n"
        "  - (Assumed temperature must ALWAYS be higher than actual OAT and higher than T_ref).\n\n"
        "Step 2: Check Condition 2: Calculate Percentage Thrust Reduction:\n"
        "  - Full Rated Thrust = 120 kN\n"
        "  - Reduced Thrust at +54°C = 93 kN\n"
        "  - Actual Thrust Reduction = 120 kN - 93 kN = 27 kN.\n"
        "  - Percentage Reduction = (27 kN / 120 kN) x 100 = 22.5% reduction!\n\n"
        "Step 3: Compare with the 25% Regulatory Limit:\n"
        "  - Regulatory Maximum Reduction = 25.0%\n"
        "  - Actual Reduction = 22.5%\n"
        "  - Check: 22.5% <= 25.0% -> PASSED! The reduction is within the legal 25% limit!\n\n"
        "Step 4: Check Runway Condition:\n"
        "  - Provided the runway is NOT contaminated and antiskid is operational, the takeoff is 100% legal!\n"
        "FINAL ANSWER: Yes! The take-off is legal with Flex Temp +54°C, yielding a 22.5% thrust reduction (below the 25% legal cap).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Vmcg Difference: Flex vs Derate Trap",
        "- Under ASSUMED TEMPERATURE: Vmcg is based on FULL RATED THRUST (high Vmcg). Moving thrust to full TOGA is safe.\n"
        "- Under FIXED DERATE: Vmcg is based on the REDUCED thrust (low Vmcg). Pushing full TOGA below the full-thrust Vmcg will cause uncontrollable rudder divergence off the runway!",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch10 = [
        ("Q1: What is the maximum permissible thrust reduction when using the ASSUMED TEMPERATURE METHOD for take-off under CS-25?",
         "[A] 10%\n[B] Not more than 25% of full rated take-off thrust\n[C] 50%\n[D] Unlimited",
         "CORRECT: [B]. Under CS-25 regulations, thrust reduction using the assumed temperature method is capped at a maximum of 25% below full rated thrust (minimum 75% thrust remaining)."),
        ("Q2: Under which of the following operational conditions is the use of the ASSUMED TEMPERATURE METHOD strictly PROHIBITED?",
         "[A] At sea level\n[B] On CONTAMINATED runways (e.g. standing water, slush, or ice)\n[C] At temperatures below ISA\n[D] On runways longer than 3,000 m",
         "CORRECT: [B]. Assumed temperature take-off is banned on contaminated runways due to unpredictable tire friction and the requirement to maintain maximum acceleration and stopping margins."),
        ("Q3: What is the fundamental difference between 'Assumed Temperature' (Flex) and 'Derated Thrust' regarding minimum control speeds (Vmcg)?",
         "[A] There is no difference\n[B] Assumed temperature uses Vmcg based on FULL RATED thrust; Derated thrust establishes a certified LOWER Vmcg corresponding to the lower derated thrust rating\n[C] Derate increases Vmcg\n[D] Flex has no Vmcg",
         "CORRECT: [B]. Fixed derate is certified at a lower thrust level, allowing lower minimum control speeds (Vmcg and Vmca), whereas assumed temperature retains the higher full-rated Vmcg.")
    ]

    for q_text, opts, exp in questions_ch10:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Performance Chapter 10 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_perf_ch06()
    build_perf_ch07()
    build_perf_ch08()
    build_perf_ch09()
    build_perf_ch10()
