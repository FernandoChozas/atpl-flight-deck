#!/usr/bin/env python3
"""
Generator for Subject 081: Principles of Flight (Aerodynamics)
Volume 2: Chapters 05 to 07 (Drag, Stalling & High-Lift Devices)
- Chapter 05: Total Drag, Minimum Drag Speed (Vmd) & Ground Effect
- Chapter 06: Stalling Mechanics, Boundary Layer & Flow Separation
- Chapter 07: High-Lift Devices (Flaps, Slats) & Airframe Contamination

Fully aligned with CAE Oxford Principles of Flight and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/081_principles_of_flight"

def build_pof_ch05():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch05_total_drag_vmd_ground_effect.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 5: Total Drag & Ground Effect")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        5,
        "Total Drag, Minimum Drag Speed (Vmd) & Ground Effect",
        "145-184"
    )

    pdf.add_heading_1("1. Parasite Drag Components: Skin Friction, Form & Interference")
    pdf.add_paragraph(
        "Parasite drag includes all aerodynamic drag not associated with the generation of lift. It increases with the square of airspeed (D_p proportional to V^2):"
    )
    pdf.add_bullet("Skin Friction Drag", "Result of viscous shearing stresses in the boundary layer. Minimized by keeping surfaces polished and maintaining laminar flow.")
    pdf.add_bullet("Form Drag (Pressure Drag)", "Result of boundary layer separation creating a low-pressure wake behind bluff bodies. Minimized by streamlining and optimizing fineness ratio (length-to-diameter ratio ~3:1 to 4:1).")
    pdf.add_bullet("Interference Drag", "Result of turbulent mixing of boundary layers at structural junctions (wing root, fuselage, engine pylons). Minimized by aerodynamic fairings and root fillets.")

    pdf.add_heading_1("2. Total Drag Curve & Minimum Drag Speed (Vmd)")
    pdf.add_paragraph(
        "Total drag is the sum of Induced Drag (D_i proportional to 1/V^2) and Parasite Drag (D_p proportional to V^2):"
    )
    pdf.add_bullet("Vmd Equality Point", "At Minimum Drag Speed (V_md), INDUCED DRAG EXACTLY EQUALS PARASITE DRAG: D_i = D_p = 1/2 Total Drag!")
    pdf.add_bullet("Speed Stability Regimes", "Speeds above V_md: Speed-stable (parasite drag dominates; slowing down reduces drag). Speeds below V_md: The 'Backside of the Drag Curve' / Reverse Command (induced drag dominates; flying slower REQUIRES MORE THRUST to maintain level flight!).")
    pdf.add_bullet("Weight Variation", "Increasing aircraft gross mass (W) shifts the entire total drag curve UP and to the RIGHT: V_md increases with the square root of mass (V_md proportional to sqrt(W)); Minimum Total Drag increases directly proportional to mass (Total Drag proportional to W).")

    pdf.add_heading_1("3. Ground Effect Aerodynamics")
    pdf.add_paragraph(
        "When an aircraft flies within one wingspan distance above the ground (h <= b, especially pronounced at h <= b/4):"
    )

    ground_table = [
        ["Aerodynamic Parameter", "Physical Change Entering Ground Effect", "Cockpit Symptoms & Pilot Action"],
        ["Induced Downwash & Vortices", "Ground physically blocks vertical flow, suppressing wingtip vortices and reducing downwash angle.", "Induced drag DROPS by up to 50%!"],
        ["Effective Angle of Attack", "Reduction of downwash rotates lift vector forward toward the vertical.", "Lift INCREASES significantly at the same geometric pitch attitude."],
        ["Elevator Control Effectiveness", "Reduced downwash over the tailplane decreases horizontal stabilizer download.", "Generates an uncommanded NOSE-DOWN pitching moment on landing!"],
        ["Airspeed Indicator Static Vent", "Local static pressure at the vent increases slightly.", "ASI and Altimeter read slightly LOWER than actual in ground effect."]
    ]
    pdf.add_table(["Aerodynamic Parameter", "Physical Change Entering Ground Effect", "Cockpit Symptoms & Pilot Action"], ground_table, col_widths=[125.0, 195.0, 180.0])

    pdf.add_callout(
        "trap",
        "Ground Effect Traps on Take-off and Landing",
        "- LANDING (Floating): Due to the sudden reduction in induced drag, an aircraft entering flare with excess airspeed will FLOAT down the runway, risking runway overrun!\n"
        "- TAKE-OFF (Premature Liftoff Stall): An aircraft can lift off prematurely at a dangerously low speed inside ground effect. As it climbs out of ground effect (above h > b/2), induced drag suddenly increases and effective AOA drops, causing the aircraft to stall or settle back onto the runway!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: At the Minimum Drag Speed (V_md) in straight and level flight, what is the exact mathematical relationship between Induced Drag and Parasite Drag?",
         "[A] Induced Drag is twice Parasite Drag\n[B] Induced Drag EXACTLY EQUALS Parasite Drag (D_i = D_p = 50% of Total Drag)\n[C] Induced Drag is zero\n[D] Parasite Drag is zero",
         "CORRECT: [B]. At the minimum point of the total drag curve (V_md), the decreasing induced drag curve intersects the increasing parasite drag curve. Induced drag and parasite drag are exactly equal."),
        ("Q2: How does an increase in aircraft gross mass affect the Minimum Drag Speed (V_md) and minimum total drag?",
         "[A] V_md decreases and drag increases\n[B] Both V_md and minimum total drag INCREASE\n[C] V_md increases but drag remains constant\n[D] Neither changes",
         "CORRECT: [B]. Increasing weight requires higher lift. Higher lift requires higher speed to minimize drag (V_md increases proportional to sqrt(W)) and produces higher total drag at that speed."),
        ("Q3: What occurs aerodynamically when an aircraft enters Ground Effect during landing flare?",
         "[A] Induced drag increases and lift decreases\n[B] Induced drag drops significantly, effective AOA increases, and the aircraft experiences an uncommanded nose-down pitching moment\n[C] Skin friction drag triples\n[D] The stall speed increases",
         "CORRECT: [B]. The proximity of the runway suppresses wingtip vortices and downwash, slashing induced drag, boosting lift (causing floating), and reducing tailplane downforce (causing a nose-down pitch).")
    ]

    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 5 compiled: {pdf_path}")


def build_pof_ch06():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch06_stalling_boundary_layer.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 6: Stalling & Boundary Layer")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        6,
        "Stalling Mechanics, Boundary Layer & Flow Separation",
        "185-224"
    )

    pdf.add_heading_1("1. The Boundary Layer: Laminar vs Turbulent")
    pdf.add_paragraph(
        "The boundary layer is the microscopic fluid layer adjacent to the solid surface where viscous forces slow velocity from zero (surface no-slip) up to 99% of freestream:"
    )

    bl_table = [
        ["Boundary Layer Characteristic", "Laminar Boundary Layer", "Turbulent Boundary Layer"],
        ["Fluid Particle Motion", "Smooth, parallel microscopic streamlines with zero cross-mixing.", "Vortical, swirling eddies with intense kinetic momentum exchange."],
        ["Layer Thickness & Profile", "Extremely thin; steep velocity gradient at wall.", "Thicker; flatter velocity profile with energetic fluid near wall."],
        ["Skin Friction Drag", "VERY LOW (ideal for laminar flow airfoils).", "HIGHER (roughly double the friction drag of laminar)."],
        ["Separation Resistance", "POOR. Lacks kinetic energy; separates readily under mild adverse pressure gradient.", "EXCELLENT. Kinetic mixing energizes lower layers, delaying flow separation against adverse pressure gradients!"]
    ]
    pdf.add_table(["Boundary Layer Characteristic", "Laminar Boundary Layer", "Turbulent Boundary Layer"], bl_table, col_widths=[125.0, 185.0, 190.0])

    pdf.add_bullet("Transition Point", "The point where the boundary layer transitions from laminar to turbulent. Moves FORWARD with: increasing airspeed/Reynolds number, increasing angle of attack, adverse pressure gradient, and surface roughness.")

    pdf.add_heading_1("2. Aerodynamic Stalling Mechanics")
    pdf.add_paragraph(
        "As angle of attack increases past the maximum lift coefficient (C_L_max), the adverse pressure gradient on the upper surface decelerates boundary layer air to a complete standstill, reversing flow direction and causing MASSIVE FLOW SEPARATION:"
    )
    pdf.add_bullet("Critical Angle of Attack (Alpha_crit)", "The stalling angle of attack (typically 15° to 18°). An airfoil ALWAYS stalls at the EXACT SAME critical angle of attack, regardless of airspeed, gross mass, bank angle, or altitude!")
    pdf.add_bullet("Stall Speed Formula", "V_S = sqrt( (2 x W) / (rho x S x C_L_max) ).")
    pdf.add_bullet("Factors Affecting Stall Speed", "1. Mass: V_S increases proportional to sqrt(W); 2. Load Factor (n): V_S = V_S0 x sqrt(n) = V_S0 x sqrt(1 / cos(bank)); 3. Center of Gravity: Forward CG increases stall speed (larger download on tailplane increases effective wing loading); 4. Flaps: Flap extension increases C_L_max, lowering stall speed.")

    pdf.add_callout(
        "trap",
        "Accelerated Stall & Steep Turns Calculation Trap",
        "- In a level coordinated turn, Load Factor n = 1 / cos(Bank Angle Phi):\n"
        "- At 45° Bank: n = 1.41 g -> Stall Speed increases by sqrt(1.41) = +19%!\n"
        "- At 60° Bank: n = 2.00 g -> Stall Speed increases by sqrt(2.00) = 1.414 (+41.4%)!\n"
        "- If an aircraft stalls at 60 kt clean: At 60° bank it will stall at 60 x 1.414 = 85 KNOTS!",
        max_chars=86
    )

    pdf.add_heading_1("3. Wing Planform Stall Progression Patterns")
    pdf.add_bullet("Rectangular Wing", "Stalls at WING ROOT first. Safest planform: root stall buffet provides natural pilot warning; ailerons at wingtips remain in unstalled air, retaining full roll control.")
    pdf.add_bullet("Tapered / Swept Wing", "Stalls at WINGTIP first. Dangerous: tip stall causes loss of aileron roll control and creates a severe, uncommanded NOSE-UP pitching moment (washout twist and stall strips are added to force root stall).")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: If an aircraft with a clean level-flight stall speed of 70 knots enters a coordinated 60° banked turn, what is the new stalling speed?",
         "[A] 70 knots\n[B] 85 knots\n[C] 99 knots (70 x sqrt(2))\n[D] 140 knots",
         "CORRECT: [C]. Load factor at 60° bank is n = 1 / cos(60°) = 2.0 g. The stalling speed formula is V_S(turn) = V_S x sqrt(n) = 70 x sqrt(2) = 70 x 1.414 = 98.98 (~99 knots)."),
        ("Q2: Why does a TURBULENT boundary layer resist flow separation better than a LAMINAR boundary layer?",
         "[A] Turbulent flow has zero viscosity\n[B] Turbulent vortices mix high-energy air from the outer freestream down into the lower layer, energizing it to overcome adverse pressure gradients\n[C] Turbulent flow is thinner\n[D] Turbulent flow has lower skin friction",
         "CORRECT: [B]. The defining advantage of turbulent boundary layers is kinetic turbulent mixing. High-speed fluid from above is churned down near the wall, allowing the flow to remain attached longer against opposing adverse pressure gradients."),
        ("Q3: How does moving the aircraft Center of Gravity (CG) FORWARD affect the clean stall speed?",
         "[A] Reduces stall speed\n[B] INCREASES stall speed slightly\n[C] Has zero effect on stall speed\n[D] Causes an unrecoverable spin",
         "CORRECT: [B]. Forward CG increases the nose-down moment, requiring a greater downward aerodynamic force from the tailplane for trim. This extra downward load adds to the aircraft weight, increasing wing loading and raising stall speed.")
    ]

    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 6 compiled: {pdf_path}")


def build_pof_ch07():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch07_high_lift_devices_flaps_slats.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 7: High-Lift Devices & Icing")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        7,
        "High-Lift Devices (Flaps & Slats) & Contamination",
        "225-264"
    )

    pdf.add_heading_1("1. Trailing-Edge Flaps: Camber & Area Expansion")
    pdf.add_paragraph(
        "Trailing-edge flaps increase maximum lift coefficient (C_L_max) to reduce take-off and landing speeds:"
    )

    flap_table = [
        ["Flap Type", "Mechanism of Operation & Boundary Layer Control", "Aerodynamic Characteristics"],
        ["Plain Flap", "Simple hinged trailing edge deflects downward, increasing camber.", "Increases C_L_max moderately; moderate drag increase."],
        ["Split Flap", "Deflects lower surface downward while upper surface remains fixed.", "Large suction wake behind split plate; massive parasite drag increase; ideal dive brake."],
        ["Slotted Flap", "Leaves an aerodynamic converging slot between wing and flap.", "High-pressure lower air shoots through slot as high-velocity jet, energizing flap boundary layer and delaying flow separation."],
        ["Fowler Flap", "Translates REARWARD on tracks before deflecting downward.", "INCREASES BOTH CAMBER AND WING SURFACE AREA (S)! Achieves the highest C_L_max increase of any flap design! Modern airliners use multi-slotted Fowler flaps."]
    ]
    pdf.add_table(["Flap Type", "Mechanism of Operation & Boundary Layer Control", "Aerodynamic Characteristics"], flap_table, col_widths=[105.0, 200.0, 195.0])

    pdf.add_bullet("Aerodynamic Effects of Flap Extension", "1. Increases C_L_max (lowers stall speed V_S); 2. Increases Drag (steepens approach descent angle); 3. Generates NOSE-DOWN pitching moment (due to rearward movement of center of pressure); 4. REDUCES the critical stalling angle of attack (Alpha_crit decreases by ~2° to 4°!).")

    pdf.add_heading_1("2. Leading-Edge High-Lift Devices: Slats & Slots")
    pdf.add_paragraph(
        "Leading-edge slats allow an aircraft to operate at dramatically higher angles of attack without stalling:"
    )
    pdf.add_bullet("Slats & Slots Principle", "A leading-edge slat opens a convergent nozzle slot that ducts high-energy air onto the upper surface. This delays flow separation at high angles of attack.")
    pdf.add_bullet("Alpha_crit Extension", "Unlike trailing-edge flaps (which decrease Alpha_crit), LEADING-EDGE SLATS EXTEND THE STALLING ANGLE OF ATTACK from ~15° up to 25° or even 30°! Slats do not change zero-lift AOA.")
    pdf.add_bullet("Krueger Flaps", "Folding leading-edge flaps that rotate out from beneath the lower wing leading edge. Used near the engine nacelles on Boeing 747/777/737.")

    pdf.add_heading_1("3. Airframe Contamination: The Clean Aircraft Concept")
    pdf.add_paragraph(
        "Frost, ice, and snow clinging to aerodynamic surfaces degrade flight safety catastrophically:"
    )
    pdf.add_bullet("Surface Roughness Effect", "Even a thin frost layer with the roughness of medium sandpaper: 1. Reduces maximum lift (C_L_max) by 25% to 30%! 2. Increases stall speed by 15% to 20%! 3. Increases drag by over 100%! 4. Drastically reduces stalling angle of attack.")
    pdf.add_bullet("Clean Aircraft Concept (EASA Mandate)", "Take-off is STRICTLY PROHIBITED unless all critical aerodynamic lifting surfaces, control surfaces, and engine intakes are completely free from frost, ice, snow, and slush contamination!")

    pdf.add_callout(
        "trap",
        "Flaps vs Slats Stalling Angle of Attack Traps",
        "- Trailing-Edge Flaps: INCREASE C_L_max, but DECREASE the stalling angle of attack (Alpha_crit drops by 2-4°)!\n"
        "- Leading-Edge Slats: INCREASE C_L_max, and DRAMATICALLY INCREASE the stalling angle of attack (Alpha_crit increases from ~15° to 25°+)!\n"
        "- Frost / Ice on Wings: Reduces C_L_max AND reduces Alpha_crit (wing can stall prematurely at take-off pitch attitude)!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: What happens to the critical stalling angle of attack (Alpha_crit) when TRAILING-EDGE FLAPS are extended?",
         "[A] Stalling angle of attack increases\n[B] Stalling angle of attack DECREASES (wing stalls at a lower AOA than clean)\n[C] Stalling angle remains unchanged\n[D] Stalling angle becomes 45°",
         "CORRECT: [B]. Extending trailing-edge flaps increases camber, raising the upper surface adverse pressure gradient. This causes the boundary layer to separate earlier, reducing the critical stalling AOA by 2° to 4°."),
        ("Q2: What is the primary aerodynamic mechanism of a Fowler flap compared to a plain flap?",
         "[A] It reduces parasite drag\n[B] It extends rearward on tracks before deflecting, increasing both wing surface area (S) and camber, providing superior C_L_max increase\n[C] It prevents Dutch roll\n[D] It trims the rudder",
         "CORRECT: [B]. Fowler flaps translate aft on tracks to increase effective wing planform area before deflecting down to increase camber, yielding the highest C_L_max increase of any flap type."),
        ("Q3: How does a thin layer of frost on the wing upper surface affect take-off aerodynamic characteristics?",
         "[A] It has zero effect\n[B] It reduces maximum lift by up to 30%, increases stall speed significantly, and reduces the critical stalling angle of attack\n[C] It lowers fuel consumption\n[D] It acts as a laminar flow generator",
         "CORRECT: [B]. Frost acts like coarse sandpaper, tripping the laminar boundary layer prematurely into a thick, low-energy turbulent layer that separates prematurely, causing stall at normal take-off rotation angles.")
    ]

    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 7 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_pof_ch05()
    build_pof_ch06()
    build_pof_ch07()
