#!/usr/bin/env python3
"""
Generator for Subject 032: Performance
Volume 1: Chapters 1 to 5
- Chapter 1: General Performance, Atmosphere, Factored Winds & Slope
- Chapter 2: Single-Engine Piston Aircraft Performance (Class B)
- Chapter 3: Multi-Engine Class B Piston (Take-off & OEI Climb)
- Chapter 4: Class B En-Route & Factorised Landing Performance
- Chapter 5: Class A Commercial Jet Take-Off Speeds (CS-25 Hierarchy)

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Performance and EASA CS-23 / CS-25 regulations.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_3/032_performance"

def build_perf_ch01():
    pdf_path = os.path.join(OUTPUT_DIR, "032_ch01_general_performance_atmosphere_wind.pdf")
    pdf = PDFBuilder("Performance", "032", "Chapter 1: Atmosphere & Wind Factors")

    pdf.add_title_banner(
        "Performance",
        1,
        "General Performance, Atmosphere (ISA), Wind & Runway",
        "1-44"
    )

    pdf.add_heading_1("1. Atmospheric Properties & Altitude Calculations")
    pdf.add_paragraph(
        "Aircraft performance is governed by air density, which dictates aerodynamic lift and engine thrust output:"
    )
    pdf.add_bullet("Pressure Altitude (PA)", "Altitude above the standard 1013.25 hPa datum plane: Pressure Alt = Elevation + 30 ft x (1013.25 - QNH) (or 27 ft/hPa).")
    pdf.add_bullet("Density Altitude (DA)", "Pressure altitude corrected for non-standard temperature: Density Alt = Pressure Alt + 120 ft x (OAT - ISA Temperature). High density altitude severely degrades lift, climb rate, and engine thrust!")
    pdf.add_bullet("ISA Temperature Formula", "ISA Temperature (°C) at altitude h (thousands of ft) = +15°C - 2°C x (h / 1,000 ft) (up to tropopause at 36,090 ft / -56.5°C).")

    pdf.add_heading_1("2. EASA Regulatory Factored Wind Rules")
    pdf.add_paragraph(
        "When taking off or landing, wind provides aerodynamic assistance or penalty. Under EASA regulations, safety margins are legally mandated:"
    )
    pdf.add_bullet("Headwind Credit (50% Rule)", "Operators are permitted to take credit for NO MORE THAN 50% of the reported headwind component! (Factored Headwind = 0.50 x Reported Headwind).")
    pdf.add_bullet("Tailwind Penalty (150% Rule)", "Operators MUST PENALIZE performance by AT LEAST 150% of the reported tailwind component! (Factored Tailwind = 1.50 x Reported Tailwind).")
    pdf.add_bullet("Maximum Certified Tailwind", "Standard certified tailwind limit for commercial transport jets is 10 knots (or 15 knots if specifically certified).")

    pdf.add_heading_1("3. Runway Contamination & Hydroplaning Physics")
    pdf.add_paragraph(
        "Runway surface conditions drastically alter friction coefficients and wheel braking authority:"
    )
    pdf.add_bullet("Dry Runway", "Free of visible moisture; maximum braking coefficient.")
    pdf.add_bullet("Damp / Wet Runway", "Moisture present, water depth <= 3 mm. Reduces friction coefficient; landing distance factored by x 1.15.")
    pdf.add_bullet("Contaminated Runway", "More than 25% of the required runway surface is covered with standing water, slush, or loose snow exceeding 3 mm depth (or compacted snow / ice).")
    pdf.add_bullet("Dynamic Hydroplaning Formula", "Speed at which tires completely ride on water film with zero tire-to-pavement friction: V_p (kt) = 9 x sqrt(P) [P in psi], or V_p (kt) = 5.7 x sqrt(P) [P in bar].")

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Factored Wind & Dynamic Hydroplaning Speed",
        "SCENARIO (Standard AviationExam Drill):\n"
        "A twin-jet is preparing for landing on Runway 27 (magnetic heading 270°):\n"
        "- Tower reported wind: 330° at 20 knots\n"
        "- Main gear tire pressure: 144 psi\n"
        "QUESTION 1: What is the FACTORED HEADWIND component for performance calculations?\n"
        "QUESTION 2: At what ground speed will dynamic hydroplaning occur if runway has standing water?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Part 1: Calculate Reported Wind Components:\n"
        "  - Wind angle to runway = 330° - 270° = 60° off runway heading.\n"
        "  - Reported Headwind = Wind Speed x cos(60°) = 20 kt x 0.50 = 10.0 knots.\n"
        "  - Reported Crosswind = Wind Speed x sin(60°) = 20 kt x 0.866 = 17.3 knots.\n\n"
        "Part 2: Apply EASA 50% Headwind Safety Factor:\n"
        "  - Factored Headwind = 50% of Reported Headwind = 0.50 x 10.0 kt = 5.0 knots!\n"
        "  - (You are ONLY allowed to credit 5 knots of headwind assistance in your landing distance calculation!).\n\n"
        "Part 3: Calculate Dynamic Hydroplaning Speed (V_p):\n"
        "  - Formula: V_p = 9 x sqrt(Tire Pressure in psi)\n"
        "  - Tire Pressure = 144 psi. Sqrt(144) = 12.\n"
        "  - V_p = 9 x 12 = 108 knots!\n\n"
        "FINAL ANSWER: Factored Headwind = 5.0 knots. Dynamic hydroplaning occurs above 108 knots!",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Headwind vs Tailwind Factoring Trap",
        "- Headwind: CREDIT ONLY 50% (Multiply by 0.50). Gives a pessimistic, safe distance.\n"
        "- Tailwind: PENALIZE BY 150% (Multiply by 1.50). Gives an extra-long, safe stopping distance.\n"
        "- Never mix these up! Multiplying tailwind by 0.50 would be a fatal safety error!",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: Under EASA regulations, what proportion of the reported HEADWIND component may be credited for take-off and landing distance calculations?",
         "[A] 100%\n[B] Not more than 50%\n[C] 150%\n[D] Zero",
         "CORRECT: [B]. EASA CS-25 requires that no more than 50% of nominal headwind component be used in performance graphs, providing a safety buffer against wind lulls."),
        ("Q2: An aircraft's main tires are inflated to 100 psi. What is the approximate dynamic hydroplaning speed on a runway with standing water?",
         "[A] 100 knots\n[B] 90 knots\n[C] 60 knots\n[D] 140 knots",
         "CORRECT: [B]. Formula: V_p = 9 x sqrt(P) = 9 x sqrt(100) = 9 x 10 = 90 knots. Above 90 kt, a water wedge completely lifts the tire off the tarmac."),
        ("Q3: How does an UPHILL runway slope affect take-off performance and landing performance?",
         "[A] Improves take-off and degrades landing\n[B] Increases take-off distance (gravity opposes acceleration) and DECREASES landing distance (gravity assists deceleration)\n[C] Has zero effect\n[D] Decreases both distances",
         "CORRECT: [B]. An uphill slope acts as a retardant: it lengthens take-off ground run because gravity opposes engine thrust, but shortens landing roll because gravity helps decelerate the aircraft.")
    ]

    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Performance Chapter 1 compiled: {pdf_path}")


def build_perf_ch02():
    pdf_path = os.path.join(OUTPUT_DIR, "032_ch02_single_engine_piston_performance.pdf")
    pdf = PDFBuilder("Performance", "032", "Chapter 2: Single-Engine Piston (Class B)")

    pdf.add_title_banner(
        "Performance",
        2,
        "Single-Engine Piston Aircraft Performance (Class B)",
        "45-78"
    )

    pdf.add_heading_1("1. Class B Aircraft Certification (CS-23)")
    pdf.add_paragraph(
        "Class B covers propeller-driven aircraft with a Maximum Certified Take-off Mass of 5,700 kg or less, and 9 passenger seats or fewer:"
    )
    pdf.add_bullet("Take-Off Distance (TOD to 50 ft)", "The horizontal distance from brake release to the point where the aircraft reaches a screen height of 50 ft above runway surface, with all engines operating.")
    pdf.add_bullet("Best Angle of Climb Speed (Vx)", "The speed providing the maximum gain of altitude per unit horizontal distance (steepest climb gradient). Used for clearing close-in obstacles after take-off!")
    pdf.add_bullet("Best Rate of Climb Speed (Vy)", "The speed providing the maximum gain of altitude per unit time (highest ft/min). Used for normal en-route climb to cruising altitude.")
    pdf.add_bullet("Absolute Ceiling vs Service Ceiling", "Absolute Ceiling is where maximum rate of climb drops to zero (Vx = Vy). Service Ceiling for single-engine aircraft is defined as the pressure altitude where maximum climb rate drops to 100 ft/min.")

    pdf.add_heading_1("2. Climb Gradient vs Rate of Climb Formulas")
    pdf.add_bullet("Climb Gradient (%)", "Gradient (%) = (Vertical Rise / Horizontal Distance) x 100 = (Thrust - Drag) / Weight x 100")
    pdf.add_bullet("Rate of Climb (ROC) Master Rule", "ROC (ft/min) = Gradient (%) x TAS (kt) (approximate rule of thumb: ROC ~ Gradient % x True Airspeed).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Clearing an Obstacle on Take-Off",
        "SCENARIO (Single-Engine Take-off Problem):\n"
        "A single-engine aircraft takes off from a runway:\n"
        "- Take-Off Distance to 50 ft screen height = 600 meters\n"
        "- An obstacle (tree line) of height 110 ft (33.5 m) is located 1,600 meters from brake release\n"
        "- The aircraft climbs at Vx = 70 kt TAS with an average climb gradient of 8.0%\n"
        "QUESTION: Will the aircraft clear the obstacle, and what will be its vertical clearance margin?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Determine the horizontal climb distance from 50 ft screen height to the obstacle:\n"
        "  - Obstacle distance from brake release = 1,600 m\n"
        "  - Distance to screen height (50 ft) = 600 m\n"
        "  - Climb distance = 1,600 m - 600 m = 1,000 meters.\n\n"
        "Step 2: Calculate the altitude gained over this 1,000 m climb distance:\n"
        "  - Climb Gradient = 8.0% = 0.08\n"
        "  - Altitude gained = Distance x Gradient = 1,000 m x 0.08 = 80 meters (approx 262 ft).\n\n"
        "Step 3: Add the initial screen height (50 ft = 15.2 m) to get total aircraft height:\n"
        "  - Total height over obstacle = 15.2 m + 80.0 m = 95.2 meters (312 ft).\n\n"
        "Step 4: Compare with obstacle height:\n"
        "  - Obstacle height = 33.5 m (110 ft)\n"
        "  - Vertical Clearance = 95.2 m - 33.5 m = 61.7 meters (approx 202 ft)!\n\n"
        "FINAL ANSWER: Yes! The aircraft clears the tree line with a safe vertical margin of 61.7 meters (202 ft).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Vx vs Vy Wind Effect Trap",
        "- Airspeed for Vx and Vy are INDICATED AIRSPEEDS (IAS) and are NOT affected by wind!\n"
        "- Headwind STEEPENS the flight path gradient over the ground (helps obstacle clearance).\n"
        "- Tailwind FLATTENS the flight path gradient over the ground (danger of hitting obstacles)!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: What is the official definition of 'SERVICE CEILING' for a single-engine piston aircraft?",
         "[A] The altitude where climb rate becomes zero\n[B] The pressure altitude at which the maximum rate of climb drops to 100 ft/min\n[C] 10,000 ft\n[D] The altitude where cabin oxygen is required",
         "CORRECT: [B]. Under CS-23 certification, the service ceiling for a single-engine aircraft is reached when the maximum full-power rate of climb decreases to 100 ft/min."),
        ("Q2: When flying a single-engine aircraft to clear a tall obstacle immediately after take-off, which climb speed MUST the pilot select?",
         "[A] Vy (Best Rate of Climb)\n[B] Vx (Best Angle of Climb), because it gives the steepest vertical flight path angle per meter of ground distance\n[C] Vno\n[D] Maximum cruise speed",
         "CORRECT: [B]. Vx produces the maximum altitude gain per horizontal distance traveled, maximizing vertical clearance over close-in obstacles."),
        ("Q3: What happens to the Best Angle of Climb Speed (Vx) and Best Rate of Climb Speed (Vy) as altitude increases?",
         "[A] Vx decreases and Vy increases\n[B] Vx INCREASES slightly and Vy DECREASES until they meet at the absolute ceiling\n[C] Both speeds stay perfectly constant\n[D] Both drop to zero",
         "CORRECT: [B]. With increasing altitude, Vx (IAS) increases slightly while Vy (IAS) decreases. The altitude where Vx equals Vy is the Absolute Ceiling (rate of climb = 0).")
    ]

    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Performance Chapter 2 compiled: {pdf_path}")


def build_perf_ch03():
    pdf_path = os.path.join(OUTPUT_DIR, "032_ch03_multi_engine_class_b_takeoff_climb.pdf")
    pdf = PDFBuilder("Performance", "032", "Chapter 3: Multi-Engine Class B (OEI Climb)")

    pdf.add_title_banner(
        "Performance",
        3,
        "Multi-Engine Class B Piston (Take-Off & OEI Climb)",
        "79-114"
    )

    pdf.add_heading_1("1. Asymmetric Flight & Loss of 80% Climb Performance")
    pdf.add_paragraph(
        "When an engine fails on a twin-engine piston aircraft, 50% of the total engine power is lost. "
        "HOWEVER, CLIMB PERFORMANCE DROPS BY 80% OR MORE! This is because climb depends on EXCESS POWER above that required for level flight:"
    )
    pdf.add_bullet("Excess Power Law", "Power Available drops by 50%, while Power Required INCREASES due to rudder deflection drag and windmilling propeller drag. The remaining margin of excess power is cut by 80% to 100%!")
    pdf.add_bullet("Windmilling Drag", "An unfeathered windmilling propeller produces massive drag (equivalent to dragging a large flat plate through the air). IMMEDIATE ACTION: Feather the dead propeller!")
    pdf.add_bullet("5° Bank Rule", "Banking 2° to 5° TOWARDS THE OPERATING ENGINE and centering the ball with half-deflection creates a horizontal component of lift that opposes engine yaw, reducing rudder drag and maximizing OEI climb gradient.")

    pdf.add_heading_1("2. Multi-Engine Service Ceiling & Speeds")
    pdf.add_bullet("OEI Service Ceiling", "The altitude where the single-engine rate of climb drops to 50 ft/min (with propeller feathered).")
    pdf.add_bullet("Vyse (Blue Line Speed)", "Best Rate of Climb Speed with One Engine Inoperative. Marked on the airspeed indicator by a prominent BLUE RADIAL LINE. The single most important safety speed in twin-engine emergencies!")
    pdf.add_bullet("Vmca (Red Line Speed)", "Minimum Control Speed in the Air. Marked by a RED RADIAL LINE. Airspeed MUST NEVER be allowed to drop below Vmca during asymmetric flight!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Determining OEI Drift Down & Terrain Clearance",
        "SCENARIO (Twin-Engine OEI Emergency):\n"
        "A light twin-engine aircraft is cruising at 9,000 ft MSL:\n"
        "- Aircraft All-Engine Service Ceiling: 18,000 ft\n"
        "- Certified One-Engine Inoperative (OEI) Service Ceiling at current mass: 6,500 ft MSL\n"
        "- The left engine fails catastrophically!\n"
        "- Flight path crosses a mountain ridge with elevation 6,800 ft MSL located 20 miles ahead\n"
        "QUESTION: Can the aircraft maintain level flight at 9,000 ft? What will happen, and can it clear the ridge?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Check if 9,000 ft can be sustained:\n"
        "  - OEI Service Ceiling = 6,500 ft MSL.\n"
        "  - Because current altitude (9,000 ft) is HIGHER than the OEI ceiling (6,500 ft), the aircraft CANNOT sustain level flight!\n"
        "  - The aircraft MUST descend (drift down) toward 6,500 ft.\n\n"
        "Step 2: Compare OEI ceiling with the mountain ridge:\n"
        "  - OEI Service Ceiling = 6,500 ft MSL.\n"
        "  - Mountain ridge height = 6,800 ft MSL.\n"
        "  - Since 6,500 ft < 6,800 ft, the aircraft will eventually settle BELOW the top of the mountain ridge!\n\n"
        "Step 3: Operational Decision / Emergency Procedure:\n"
        "  - Setting blue line speed (Vyse) will only delay descent down to 6,500 ft.\n"
        "  - The pilot MUST IMMEDIATELY TURN AWAY from the mountain ridge toward lower terrain or an emergency diversion airport!\n"
        "FINAL ANSWER: Flight at 9,000 ft cannot be maintained. Aircraft will drift down to 6,500 ft, which is below the 6,800 ft ridge. Immediate diversion is mandatory.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The 50% Power vs 80% Climb Trap",
        "- Losing 1 engine on a twin LOSES 50% OF POWER, BUT 80% TO 90% OF CLIMB RATE!\n"
        "- Example: Twin climbing at 1,000 ft/min on 2 engines does NOT climb at 500 ft/min on 1 engine! It will climb at only 100 to 200 ft/min!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: On a multi-engine piston aircraft airspeed indicator, what does the BLUE RADIAL LINE indicate?",
         "[A] Maximum flap extension speed\n[B] Vyse (Best Rate of Climb Speed with One Engine Inoperative)\n[C] Minimum control speed ground\n[D] Never exceed speed",
         "CORRECT: [B]. The blue line marks Vyse, the airspeed yielding maximum single-engine rate of climb with the critical engine feathered."),
        ("Q2: Why does an aircraft lose approximately 80% of its climb performance when one engine fails on a twin-engine aircraft?",
         "[A] Half the fuel is lost\n[B] Climb depends on EXCESS power; after losing 50% power and adding asymmetric drag, the remaining excess power above level flight is tiny\n[C] The tailplane stalls\n[D] Generator fails",
         "CORRECT: [B]. Climb requires excess thrust above total drag. At single-engine speed, almost all remaining thrust is consumed just keeping the airplane in level flight, leaving very little excess power for climb."),
        ("Q3: Under CS-23, what is the definition of OEI Service Ceiling for multi-engine piston aircraft?",
         "[A] Climb rate = 0 ft/min\n[B] Altitude where maximum rate of climb with one engine feathered drops to 50 ft/min\n[C] 100 ft/min\n[D] 15,000 ft",
         "CORRECT: [B]. For multi-engine Class B aircraft, OEI Service Ceiling is defined at a residual climb rate of 50 ft/min (compared to 100 ft/min for all-engine).")
    ]

    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Performance Chapter 3 compiled: {pdf_path}")


def build_perf_ch04():
    pdf_path = os.path.join(OUTPUT_DIR, "032_ch04_class_b_enroute_landing.pdf")
    pdf = PDFBuilder("Performance", "032", "Chapter 4: Class B En-Route & Landing")

    pdf.add_title_banner(
        "Performance",
        4,
        "Class B En-Route & Factorised Landing Performance",
        "115-148"
    )

    pdf.add_heading_1("1. Cruise Performance: Range vs Endurance")
    pdf.add_paragraph(
        "Cruising efficiency for propeller aircraft depends on matching engine brake horsepower to airframe drag curves:"
    )
    pdf.add_bullet("Maximum Range Cruise Speed (V_MRC)", "Flown at the speed of minimum total drag (V_md / tangent point on drag curve). Provides the maximum nautical miles per kilogram of fuel burned (NMPK).")
    pdf.add_bullet("Maximum Endurance Speed (V_min_power)", "Flown at the speed of minimum power required (V_mp ~ 0.76 x V_md). Provides the maximum flight time (hours) in the air per kilogram of fuel burned. Used for holding patterns!")

    pdf.add_heading_1("2. Class B Commercial Landing Safety Factors")
    pdf.add_paragraph(
        "Under EASA AIR-OPS (CAT.POL.A.330), landing distance on a commercial flight must incorporate legal safety factors:"
    )
    pdf.add_bullet("The 1.43 Landing Factor", "The Landing Distance Available (LDA) at the destination must be at least 1.43 times the actual measured landing distance from 50 ft: Factored Landing Distance = Actual Landing Distance x 1.43.")
    pdf.add_bullet("Grass Runway Corrections", "Dry grass up to 20 cm: Multiply landing distance by 1.20 (+20%). Wet grass: Multiply by 1.30 (+30%).")
    pdf.add_bullet("Slope Corrections", "Downslope runway: Increases landing distance by +5% per 1% downhill slope!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Factored Landing Distance on Wet Grass Runway",
        "SCENARIO (Commercial Class B Landing Problem):\n"
        "A twin-propeller air-taxi is planning to land at an unpaved airfield:\n"
        "- Unfactored (Flight Manual) Landing Distance from 50 ft on dry asphalt = 500 meters\n"
        "- Destination runway: Wet grass surface (+30% correction)\n"
        "- Runway slope: 2.0% downhill slope (+5% per 1% slope = +10% correction)\n"
        "- EASA commercial operation factor: 1.43\n"
        "QUESTION: What is the MINIMUM Landing Distance Available (LDA) required to land legally?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Apply the Runway Surface Correction (Wet Grass = x 1.30):\n"
        "  - Distance after grass factor = 500 m x 1.30 = 650 meters.\n\n"
        "Step 2: Apply the Downslope Correction (2% downhill x 5% = +10% -> x 1.10):\n"
        "  - Distance after slope factor = 650 m x 1.10 = 715 meters.\n\n"
        "Step 3: Apply the mandatory EASA Commercial Safety Factor (x 1.43):\n"
        "  - Factored Required LDA = 715 m x 1.43 = 1,022.45 meters -> 1,023 meters!\n\n"
        "FINAL ANSWER: The runway must have a certified Landing Distance Available (LDA) of AT LEAST 1,023 meters! (More than double the basic 500 m manual distance!).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Sequential Multiplication Trap",
        "- Always apply factors sequentially (Surface -> Slope -> Regulatory factor).\n"
        "- Notice how a 500 m basic distance turns into 1,023 m! In ATPL exams, failing to apply the 1.43 commercial factor is the most common student error!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: Under EASA regulations, what is the regulatory multiplication factor applied to the landing distance of a Class B aircraft on a commercial flight?",
         "[A] 1.15\n[B] 1.43 (meaning required LDA must be at least 143% of actual distance)\n[C] 1.67\n[D] 2.00",
         "CORRECT: [B]. Under CAT.POL.A.330 for Class B aircraft, the landing distance from 50 ft must be multiplied by 1.43 (equivalent to using no more than 70% of the available runway)."),
        ("Q2: At what airspeed does a piston-propeller aircraft achieve MAXIMUM ENDURANCE (maximum time in the air)?",
         "[A] At the speed for minimum power required (V_mp ~ 0.76 V_md)\n[B] At the speed for minimum total drag (V_md)\n[C] At Vno\n[D] At stall speed",
         "CORRECT: [A]. Piston engine fuel burn is proportional to brake horsepower. Flying at the bottom of the Power Required curve (V_mp) burns the minimum fuel per hour, maximizing endurance."),
        ("Q3: How does a DOWNHILL runway slope affect landing distance?",
         "[A] Decreases landing distance\n[B] INCREASES landing distance (approx +5% per 1% of downhill slope)\n[C] Has zero effect on landing roll\n[D] Increases tire wear only",
         "CORRECT: [B]. A downhill slope reduces the deceleration component of gravity, requiring more wheel braking and lengthening landing distance.")
    ]

    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Performance Chapter 4 compiled: {pdf_path}")


def build_perf_ch05():
    pdf_path = os.path.join(OUTPUT_DIR, "032_ch05_class_a_takeoff_speeds.pdf")
    pdf = PDFBuilder("Performance", "032", "Chapter 5: Class A Take-Off Speeds")

    pdf.add_title_banner(
        "Performance",
        5,
        "Class A Take-Off Speeds (CS-25 Hierarchy: V1, Vr, V2)",
        "149-194"
    )

    pdf.add_heading_1("1. The CS-25 Take-Off Speeds Spectrum")
    pdf.add_paragraph(
        "Class A covers commercial jet transports certified under CS-25. Take-off is governed by an interlocking hierarchy of calibrated airspeeds:"
    )

    speeds_table = [
        ["Speed Code & Name", "Aerodynamic & Regulatory Definition", "Mandatory Legal Constraint / Relationship"],
        ["Vs1g / Vsr (Reference Stall)", "Stall speed at 1g normal acceleration in take-off configuration.", "Baseline reference for all minimum safety speeds."],
        ["Vmcg (Min Control Ground)", "Minimum speed to maintain directional control on runway using RUDDER ONLY following engine failure.", "Vmcg <= V1! (If engine fails below Vmcg, rudder cannot keep plane on runway!)."],
        ["V1 (Decision Speed)", "Maximum speed to abort take-off; minimum speed to continue take-off safely following engine failure.", "Vmcg <= V1 <= Vr and V1 <= V_MBE (Max Brake Energy Speed)."],
        ["Vr (Rotation Speed)", "Speed at which pilot initiates backward pull on control column to pitch up.", "Vr >= V1 and Vr >= 1.05 x Vmca."],
        ["Vmu (Min Unstick Speed)", "Minimum speed at which aircraft can safely lift off ground without tail strike.", "Demonstrated during flight test with tail dragging on runway."],
        ["Vlof (Lift-Off Speed)", "Actual speed at which the main tires leave the runway surface.", "Vlof >= 1.10 x Vmu (all engines) or >= 1.05 x Vmu (OEI)."],
        ["V2 (Take-off Safety Speed)", "Target climb speed reached at 35 ft screen height with one engine inoperative.", "V2 >= 1.13 x Vsr and V2 >= 1.10 x Vmca!"]
    ]
    pdf.add_table(["Speed Code & Name", "Aerodynamic & Regulatory Definition", "Mandatory Legal Constraint / Relationship"], speeds_table, col_widths=[110.0, 215.0, 175.0])

    pdf.add_heading_1("2. The Golden Hierarchy of Take-Off Speeds")
    pdf.add_paragraph(
        "The strict sequential order of speeds during an accelerating take-off roll is:"
    )
    pdf.add_bullet("The Take-off Sequence", "Vmcg <= V1 <= Vr < Vlof < V2. (Never can V1 be less than Vmcg, and never can V1 exceed Vr!).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Checking Take-Off Speeds Legality",
        "SCENARIO (Classic EASA Flight Deck Trap Drill):\n"
        "A dispatch calculation for a Boeing 737 yields the following calculated speeds:\n"
        "- Vmcg = 112 kt\n"
        "- Vmca = 118 kt\n"
        "- V1 = 110 kt\n"
        "- Vr = 122 kt\n"
        "- V2 = 130 kt\n"
        "QUESTION: Is this speed schedule legal for departure under CS-25 regulations? If not, what must be corrected?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Check Constraint 1: Vmcg <= V1:\n"
        "  - Vmcg = 112 kt\n"
        "  - V1 = 110 kt\n"
        "  - Check: Is 112 <= 110? NO! V1 (110 kt) is LESS than Vmcg (112 kt)!\n"
        "  - WHY THIS IS DANGEROUS FOR DUMMIES: If an engine fails at 111 kt, you are above V1 (committing to fly), but below Vmcg (meaning the rudder cannot keep the aircraft straight on the runway, causing a runway excursion!).\n"
        "  - Mandatory Fix: V1 MUST be raised to at least 112 kt (V1 >= Vmcg)!\n\n"
        "Step 2: Check Constraint 2: Vr >= 1.05 x Vmca:\n"
        "  - Minimum allowable Vr = 1.05 x 118 kt = 123.9 kt (~124 kt).\n"
        "  - Actual proposed Vr = 122 kt.\n"
        "  - Check: Is 122 >= 124? NO! Vr is 2 knots too low!\n"
        "  - Mandatory Fix: Vr must be raised to at least 124 kt!\n\n"
        "FINAL ANSWER: The schedule is ILLEGAL on two counts! V1 must be increased to at least 112 kt, and Vr must be increased to at least 124 kt.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The V1 Decision Point Trap",
        "- V1 is the DECISION SPEED: The action to abort must be INITIATED BY V1!\n"
        "- In modern regulations, V1 is the MAXIMUM speed by which the pilot must have made the decision AND applied the first stopping action (brakes/spoilers). If an engine fails after V1, YOU MUST CONTINUE THE TAKE-OFF!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: Under CS-25 regulations, what is the strict relationship between V1 (Decision Speed) and Vmcg (Minimum Control Speed Ground)?",
         "[A] V1 must be less than Vmcg\n[B] V1 must be GREATER THAN OR EQUAL TO Vmcg (V1 >= Vmcg)\n[C] V1 is always 1.2 times Vmcg\n[D] Vmcg only applies in flight",
         "CORRECT: [B]. If V1 were below Vmcg, an engine failure between V1 and Vmcg would require continuing the take-off, yet the aerodynamic rudder force would be insufficient to prevent the aircraft veering off the runway."),
        ("Q2: Under CS-25, what is the minimum legal ratio for Take-Off Safety Speed (V2) relative to reference stall speed (Vsr) for twin-turbofan aircraft?",
         "[A] V2 >= 1.13 x Vsr\n[B] V2 >= 1.05 x Vsr\n[C] V2 = Vsr\n[D] V2 >= 1.40 x Vsr",
         "CORRECT: [A]. Under CS-25.107, V2 must provide a stall margin of at least 13% above reference stall speed: V2 >= 1.13 Vsr (and at least 1.10 Vmca)."),
        ("Q3: If an engine fails at a speed HIGHER than V1 on a commercial airliner take-off, what is the legally mandated flight crew action?",
         "[A] Immediately apply maximum wheel braking and reverse thrust\n[B] CONTINUE the take-off, rotate at Vr, and climb away at V2\n[C] Extend full flaps\n[D] Cut the remaining engine",
         "CORRECT: [B]. Above V1, remaining runway is insufficient to stop the aircraft without overrunning. The aircraft is certified to safely climb away on the remaining engine(s).")
    ]

    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Performance Chapter 5 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_perf_ch01()
    build_perf_ch02()
    build_perf_ch03()
    build_perf_ch04()
    build_perf_ch05()
