#!/usr/bin/env python3
"""
Generator for Subject 081: Principles of Flight (Aerodynamics)
Volume 1: Chapters 01 to 04 (Subsonic Aerodynamics & Wing Design)
- Chapter 01: Subsonic Airflow, Continuity Equation & Bernoulli's Principle
- Chapter 02: Airfoil Geometry, Lift Generation & Pitching Moments
- Chapter 03: Lift & Drag Coefficients, Lift Formula & Polar Curves
- Chapter 04: Three-Dimensional Wing Airflow, Aspect Ratio & Induced Drag

Fully aligned with CAE Oxford Principles of Flight and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/081_principles_of_flight"

def build_pof_ch01():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch01_subsonic_airflow_bernoulli.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 1: Subsonic Airflow & Bernoulli")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        1,
        "Subsonic Airflow, Continuity & Bernoulli's Principle",
        "1-34"
    )

    pdf.add_heading_1("1. Air Properties, Atmosphere & The Speed of Sound")
    pdf.add_paragraph(
        "Aerodynamics investigates the interaction between moving air and solid airframe bodies. Air behaves as an ideal compressible gas:"
    )
    pdf.add_bullet("Air Density (rho)", "Mass per unit volume (kg/m^3). Standard sea level density (ISA rho_0) = 1.225 kg/m^3. Density decreases with increasing altitude, increasing temperature, and increasing relative humidity (humid air is LESS DENSE than dry air because H2O molecular weight [18] is less than N2 [28] and O2 [32])!")
    pdf.add_bullet("Static Pressure (p)", "The weight of the atmospheric column acting equally in all directions. Standard MSL pressure = 1013.25 hPa = 101,325 N/m^2.")
    pdf.add_bullet("Speed of Sound (a)", "The propagation velocity of pressure waves: a = sqrt(gamma x R x T) = 38.94 x sqrt(T [Kelvin]). The speed of sound depends EXCLUSIVELY on absolute temperature! At standard ISA sea level (+15°C / 288 K): a = 661.5 kt = 340 m/s.")

    pdf.add_heading_1("2. The Continuity Equation & Streamtube Flow")
    pdf.add_paragraph(
        "For steady, continuous fluid flow through a streamtube, the principle of conservation of mass dictates that mass flow rate (m_dot) is constant:"
    )
    pdf.add_bullet("Continuity Equation", "Mass Flow Rate: m_dot = rho x A x V = Constant (where A = cross-sectional area, V = flow velocity).")
    pdf.add_bullet("Incompressible Flow (Subsonic Mach < 0.3)", "Air density is assumed constant (rho = constant). Therefore: Area x Velocity = Constant: A1 x V1 = A2 x V2. As a streamtube CONVERGES (area decreases), velocity must INCREASE. As it DIVERGES (area expands), velocity must DECREASE.")

    pdf.add_heading_1("3. Bernoulli's Theorem & Venturi Effect")
    pdf.add_paragraph(
        "Bernoulli's theorem represents the conservation of energy in steady, incompressible, frictionless streamline flow:"
    )
    pdf.add_bullet("Total Pressure (Stagnation Pressure)", "Total Pressure (P_t) = Static Pressure (P_s) + Dynamic Pressure (q) = Constant.")
    pdf.add_bullet("Dynamic Pressure Formula", "q = 1/2 rho V^2. Dynamic pressure represents the kinetic energy of the moving fluid.")
    pdf.add_bullet("Venturi Throat Dynamics", "As air flows into a convergent throat: Area narrows -> Velocity increases -> Dynamic pressure increases -> Static pressure DROPS! Downstream divergent section: Area expands -> Velocity decreases -> Static pressure RISES.")

    flow_table = [
        ["Subsonic Convergent Duct", "Decreases", "INCREASES", "INCREASES", "DECREASES (Bernoulli drop)"],
        ["Subsonic Divergent Duct", "Increases", "DECREASES", "DECREASES", "INCREASES (Diffuser action)"],
        ["Supersonic Convergent Duct", "Decreases", "DECREASES", "DECREASES", "INCREASES (Compressibility dominates)"],
        ["Supersonic Divergent Duct", "Increases", "INCREASES", "INCREASES", "DECREASES (Nozzle expansion)"]
    ]
    pdf.add_table(["Regime / Duct Section", "Cross-Sectional Area (A)", "Air Velocity (V)", "Dynamic Pressure (q)", "Static Pressure (P_s)"], flow_table, col_widths=[120.0, 80.0, 95.0, 100.0, 105.0])

    pdf.add_callout(
        "trap",
        "Air Density vs Humidity Exam Trap",
        "- QUESTION: Does high relative humidity increase or decrease air density?\n"
        "- ANSWER: High humidity DECREASES air density!\n"
        "- Water vapor (H2O) has a molecular weight of 18 g/mol, whereas dry air (N2 and O2) averages 29 g/mol. Humid air is lighter and less dense than dry air at the same temperature and pressure, reducing aerodynamic lift and engine thrust!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: According to Bernoulli's equation for steady incompressible flow, what happens to static pressure when airflow velocity accelerates through a constriction?",
         "[A] Static pressure increases\n[B] Static pressure DECREASES while dynamic pressure increases, keeping total pressure constant\n[C] Total pressure drops to zero\n[D] Air density increases",
         "CORRECT: [B]. By Bernoulli's principle, Total Pressure = Static + Dynamic. When velocity accelerates, dynamic pressure (1/2 rho V^2) rises; static pressure must decrease by an equal amount to conserve energy."),
        ("Q2: On what single atmospheric variable does the local speed of sound in air depend?",
         "[A] Static pressure only\n[B] Air density only\n[C] Absolute Air Temperature (Kelvin) ONLY\n[D] Relative humidity",
         "CORRECT: [C]. Formula: a = sqrt(gamma x R x T) = 38.94 x sqrt(T). The speed of sound depends exclusively on absolute air temperature in Kelvin. Pressure and density changes cancel each other out."),
        ("Q3: How does high relative atmospheric humidity affect aircraft aerodynamic take-off performance?",
         "[A] Increases lift and improves engine power\n[B] Reduces air density, which reduces aerodynamic lift and degrades engine take-off thrust\n[C] Increases the speed of sound\n[D] Has zero effect on aviation",
         "CORRECT: [B]. Water molecules are lighter than nitrogen and oxygen molecules. Humid air reduces air density, decreasing dynamic pressure for a given speed, lengthening take-off ground run.")
    ]

    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 1 compiled: {pdf_path}")


def build_pof_ch02():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch02_airfoil_geometry_lift_moments.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 2: Airfoil Geometry & Lift")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        2,
        "Airfoil Geometry, Lift Generation & Pitching Moments",
        "35-72"
    )

    pdf.add_heading_1("1. Airfoil Anatomy & Geometric Terminology")
    pdf.add_paragraph(
        "An airfoil is an aerodynamic cross-section engineered to generate usable lift while minimizing drag:"
    )
    pdf.add_bullet("Chord Line", "A straight reference line connecting the leading edge and trailing edge centers of curvature. Chord length (c) is the reference datum for aerodynamic dimensions.")
    pdf.add_bullet("Mean Camber Line (MCL)", "A line equidistant from the upper and lower airfoil surfaces. If the MCL coincides with the chord line, the airfoil is SYMMETRICAL. If MCL lies above chord, it is POSITIVELY CAMBERED.")
    pdf.add_bullet("Maximum Camber", "The maximum perpendicular distance between chord line and MCL, expressed as a percentage of chord (typically 2% to 4% at 30% to 40% chord). Camber determines zero-lift angle of attack.")
    pdf.add_bullet("Maximum Thickness", "The maximum distance between upper and lower surfaces (t/c ratio, e.g. 12% to 15% for transport aircraft, 9% to 11% for high-speed transonic airfoils).")
    pdf.add_bullet("Angle of Attack (Alpha)", "The acute angle between the airfoil chord line and the RELATIVE AIRFLOW (freestream vector). Alpha is completely independent of the aircraft's pitch attitude relative to the horizon!")

    pdf.add_heading_1("2. Lift Generation: Circulation, Downwash & Pressure Distribution")
    pdf.add_paragraph(
        "Lift is generated through two complementary aerodynamic mechanisms:"
    )
    pdf.add_bullet("Pressure Differential (Bernoulli)", "Air flowing over the curved upper surface accelerates, causing static pressure to drop below ambient (creating suction / low pressure). Air on the lower surface experiences slight compression. Upper surface suction contributes 70% to 80% of total aerodynamic lift!")
    pdf.add_bullet("Newton's Third Law (Downwash Deflection)", "The airfoil deflects oncoming air downwards (downwash angle). The reaction to accelerating air downwards is an equal and opposite upward force: LIFT = Downward Mass Flow x Vertical Acceleration.")

    pdf.add_heading_1("3. Center of Pressure (CP) vs Aerodynamic Center (AC)")
    pdf.add_paragraph(
        "Understanding the distinction between Center of Pressure and Aerodynamic Center is critical for aircraft stability:"
    )

    center_table = [
        ["Center of Pressure (CP)", "Point along chord where total resultant aerodynamic force acts.", "MOVES with Angle of Attack! On a positively cambered airfoil: As AOA increases, CP MOVES FORWARD toward leading edge (up to stall). As AOA decreases, CP moves REARWARD. Inherently unstable!"],
        ["Aerodynamic Center (AC)", "Point along chord about which the pitching moment coefficient remains CONSTANT regardless of AOA.", "DOES NOT MOVE with AOA in subsonic flight! Located at approximately the 25% CHORD POINT (Quarter-Chord) for all subsonic airfoils (moves to 50% chord in supersonic flight)."]
    ]
    pdf.add_table(["Aerodynamic Datum", "Physical Definition & Location", "Behavior with Angle of Attack Changes"], center_table, col_widths=[125.0, 195.0, 180.0])

    pdf.add_callout(
        "trap",
        "Pitching Moment About the Aerodynamic Center",
        "- Symmetrical Airfoil: Pitching moment about the AC is ZERO at all angles of attack!\n"
        "- Positively Cambered Airfoil: Generates a NOSE-DOWN (negative) pitching moment about the AC that remains CONSTANT as AOA changes!\n"
        "- Center of Pressure Movement: On cambered wings, increasing AOA moves CP FORWARD; on symmetrical wings, CP remains virtually fixed at 25% chord.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: For a positively cambered subsonic airfoil, how does the Center of Pressure (CP) move when the Angle of Attack increases within the normal flying range?",
         "[A] CP moves rearward toward the trailing edge\n[B] CP moves FORWARD toward the leading edge\n[C] CP remains fixed at 50% chord\n[D] CP moves downward",
         "CORRECT: [B]. On positively cambered airfoils, increasing AOA intensifies leading-edge suction peak, drawing the resultant Center of Pressure forward toward the quarter-chord point."),
        ("Q2: What is the defining characteristic of an airfoil's Aerodynamic Center (AC) in subsonic flight?",
         "[A] Lift is always zero at the AC\n[B] The pitching moment about the AC remains CONSTANT as angle of attack changes, located at ~25% chord\n[C] Total drag is zero at the AC\n[D] It moves forward with speed",
         "CORRECT: [B]. The Aerodynamic Center is the unique theoretical point where pitching moment coefficient is independent of AOA. In subsonic flow, it is fixed at approximately 25% chord."),
        ("Q3: What contributes the greatest percentage of total aerodynamic lift generated by an aircraft wing?",
         "[A] High pressure pushing up against the lower surface (20-30%)\n[B] Low static pressure (suction) acting on the UPPER surface (70-80%)\n[C] Engine exhaust thrust\n[D] Propeller wash",
         "CORRECT: [B]. Upper surface low pressure (suction) accounts for approximately 70% to 80% of total lift; lower surface positive pressure contributes only 20% to 30%.")
    ]

    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 2 compiled: {pdf_path}")


def build_pof_ch03():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch03_lift_drag_polar_curves.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 3: Lift, Drag & Polar Curves")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        3,
        "Lift & Drag Coefficients, Formulas & Polar Curves",
        "73-108"
    )

    pdf.add_heading_1("1. The Aerodynamic Lift Formula")
    pdf.add_paragraph(
        "Total aerodynamic lift generated by a wing is governed by the universal lift formula:"
    )
    pdf.add_bullet("Lift Equation", "L = C_L x 1/2 rho V^2 x S, where C_L = Lift Coefficient (dimensionless); rho = ambient air density (kg/m^3); V = True Airspeed (TAS, m/s); S = Wing surface area (m^2).")
    pdf.add_bullet("Dynamic Pressure Component (q = 1/2 rho V^2)", "Lift is directly proportional to dynamic pressure and wing planform area.")
    pdf.add_bullet("Lift Coefficient (C_L)", "Represents airfoil lifting efficiency. Depends on: 1. Angle of attack (Alpha); 2. Camber; 3. Airfoil shape; 4. Reynolds Number; 5. Mach number.")
    pdf.add_bullet("C_L vs Alpha Curve", "Linear increase from zero-lift angle of attack up to C_L_max. For positively cambered airfoils, zero lift occurs at a NEGATIVE angle of attack (typically -2° to -4°). Symmetrical airfoils produce zero lift at EXACTLY 0° AOA.")

    pdf.add_heading_1("2. The Drag Formula & Drag Coefficient (C_D)")
    pdf.add_paragraph(
        "Total aerodynamic drag resists aircraft forward motion through the air:"
    )
    pdf.add_bullet("Drag Equation", "D = C_D x 1/2 rho V^2 x S, where C_D = Drag Coefficient.")
    pdf.add_bullet("Total Drag Decomposition", "Total Drag = Parasite Drag (Profile Drag) + Induced Drag (Vortex Drag): C_D = C_Dp + C_Di.")
    pdf.add_bullet("Lift-to-Drag Ratio (L/D)", "L/D = C_L / C_D. Measures aerodynamic efficiency. Maximum L/D ratio (L/D_max) occurs at the tangent from the origin to the polar curve, corresponding to the MINIMUM DRAG SPEED (V_md)!")

    pdf.add_heading_1("3. The Drag Polar (Lilienthal Polar Curve)")
    polar_features = [
        ["Key Polar Feature", "Aerodynamic Meaning & Optimum Point", "Flight Application & Performance Target"],
        ["Origin Tangent Point", "Maximum Lift-to-Drag Ratio: (C_L / C_D)_max.", "Minimum Drag Speed (V_md). Yields: 1. Maximum Glide Range (unpowered); 2. Maximum Endurance for jet aircraft; 3. Maximum Range for piston-prop aircraft."],
        ["Peak of the Curve", "Maximum Lift Coefficient (C_L_max).", "Minimum Flying Airspeed (Stall Speed V_S). Corresponds to stalling angle of attack (Alpha_crit, ~15-18°)."],
        ["Maximum (C_L^(1/2) / C_D)", "Optimum speed for jet aircraft cruising range.", "Long-range cruise speed for jet airliners (typically 1.32 x V_md)."],
        ["Maximum (C_L^(3/2) / C_D)", "Minimum rate of sink / Minimum power required.", "Maximum endurance for propeller aircraft; minimum sink speed for gliders (typically 0.76 x V_md)."]
    ]
    pdf.add_table(["Key Polar Feature", "Aerodynamic Meaning & Optimum Point", "Flight Application & Performance Target"], polar_features, col_widths=[110.0, 195.0, 195.0])

    pdf.add_callout(
        "trap",
        "Glide Performance vs Aircraft Gross Mass Trap",
        "- QUESTION: How does increasing aircraft gross mass affect the maximum glide distance in power-off flight?\n"
        "- ANSWER: Gross mass HAS ZERO EFFECT ON MAXIMUM GLIDE DISTANCE!\n"
        "- Maximum glide ratio equals (L/D)_max, which is purely aerodynamic.\n"
        "- Effect of Heavier Weight: The aircraft glides at a HIGHER TRUE AIRSPEED and has a HIGHER RATE OF DESCENT, covering the exact same ground distance in a shorter time!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: If an aircraft doubles its airspeed (2x V) while maintaining constant altitude and angle of attack, by what factor does total lift increase?",
         "[A] By a factor of 2\n[B] By a factor of 4 (quadruples)\n[C] By a factor of 8\n[D] Lift remains constant",
         "CORRECT: [B]. Lift formula: L = C_L x 1/2 rho V^2 x S. Because lift is proportional to the square of velocity (V^2), doubling airspeed produces (2)^2 = 4 times more lift."),
        ("Q2: At what angle of attack does a SYMMETRICAL airfoil generate zero aerodynamic lift?",
         "[A] At -4° angle of attack\n[B] At exactly ZERO degrees (0°) angle of attack\n[C] At +2° angle of attack\n[D] At stalling angle",
         "CORRECT: [B]. Symmetrical airfoils have identical upper and lower contours with zero camber. Airflow acceleration is identical on both surfaces at 0° AOA, producing zero net lift. (Positively cambered airfoils require negative AOA for zero lift)."),
        ("Q3: What operational flight condition corresponds to the point of Maximum Lift-to-Drag Ratio ((L/D)max)?",
         "[A] Maximum airspeed\n[B] Minimum Total Drag Speed (V_md) and Maximum Glide Range\n[C] Maximum stall speed\n[D] Minimum climb angle",
         "CORRECT: [B]. At (L/D)_max, aerodynamic efficiency is optimized. Total drag is at its absolute minimum (V_md), providing the shallowest glide angle and maximum unpowered glide distance.")
    ]

    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 3 compiled: {pdf_path}")


def build_pof_ch04():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch04_3d_airflow_induced_drag.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 4: 3D Airflow & Induced Drag")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        4,
        "Three-Dimensional Wing Airflow & Induced Drag",
        "109-144"
    )

    pdf.add_heading_1("1. Three-Dimensional Airflow & Wingtip Vortices")
    pdf.add_paragraph(
        "A real finite wing produces 3D airflow due to spanwise pressure differentials between upper and lower wing surfaces:"
    )
    pdf.add_bullet("Spanwise Flow", "Air on the high-pressure lower surface flows OUTWARD toward wingtips; air on the low-pressure upper surface flows INWARD toward fuselage. At the trailing edge and wingtips, these opposing spanwise flows roll up into trailing WINGTIP VORTICES.")
    pdf.add_bullet("Induced Downwash (w)", "Wingtip vortices trail downstream and induce a strong downward vertical velocity component behind the wing called induced downwash. Downwash tilts the local relative airflow vector downwards!")
    pdf.add_bullet("Effective Angle of Attack", "Effective AOA = Geometric AOA - Induced Angle (Alpha_i). Because the relative airflow is tilted downward, the total aerodynamic lift vector tilts REARWARD. The rearward-tilted component of lift is INDUCED DRAG (Vortex Drag)!")

    pdf.add_heading_1("2. Induced Drag Formula & Wing Geometry Factors")
    pdf.add_paragraph(
        "Induced drag is the inevitable aerodynamic price of generating lift with a finite-span wing:"
    )
    pdf.add_bullet("Induced Drag Coefficient", "C_Di = (C_L^2) / (pi x AR x e), where AR = Aspect Ratio, e = Oswald wing efficiency factor (~0.8 to 0.9).")
    pdf.add_bullet("Variation with Speed", "Because C_L is inversely proportional to V^2 in level flight (C_L = W / (q S)), Induced Drag is INVERSELY PROPORTIONAL TO SPEED SQUARED: D_i proportional to 1 / V^2! Induced drag is massive at low speeds (take-off, climb, landing approach) and becomes negligible at high cruising speeds.")
    pdf.add_bullet("Variation with Mass", "Induced drag is directly proportional to the SQUARE OF AIRCRAFT GROSS MASS: D_i proportional to W^2! A 20% increase in mass increases induced drag by (1.20)^2 = 44%!")

    drag_table = [
        ["Design Factor", "Aerodynamic Influence on Induced Drag", "Aeronautical Examples & Trade-offs"],
        ["Aspect Ratio (AR = b^2 / S)", "HIGH Aspect Ratio dramatically REDUCES induced drag (spreads lift over longer wingspan, reducing vortex strength).", "Gliders (AR ~ 25 to 30), high-altitude surveillance (U-2). Limited by wing root bending moments and structural weight."],
        ["Wing Planform Taper", "Elliptical lift distribution produces minimum induced drag (e = 1.0). Tapered wings approximate elliptical distribution.", "Supermarine Spitfire (pure elliptical); modern airliners use trapezoidal tapered wings with aerodynamic washout."],
        ["Winglets / Sharklets", "Vertical wingtip fences diffuse tip vortices, converting vortex energy into forward aerodynamic thrust.", "Airbus sharklets / Boeing blended winglets reduce fuel burn by 3% to 5% in cruise."],
        ["Wing Washout (Twist)", "Geometric wing twist (lower incidence at tip than root).", "Ensures wing root stalls FIRST, preserving aileron roll control at high angles of attack."]
    ]
    pdf.add_table(["Design Factor", "Aerodynamic Influence on Induced Drag", "Aeronautical Examples & Trade-offs"], drag_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_callout(
        "trap",
        "Wake Turbulence & Heavy Jet Vortex Hazard",
        "- When is Wake Turbulence Greatest?: When the generating aircraft is HEAVY, CLEAN (flaps/gear up), and SLOW!\n"
        "- Rotation / Touchdown Points: Vortices begin at nose-wheel rotation and end when nose-wheel touches down.\n"
        "- Avoidance Rule: Rotate BEFORE the preceding heavy aircraft's rotation point, and land BEYOND its touchdown point!",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: How does Induced Drag vary with aircraft airspeed in straight and level flight?",
         "[A] Directly proportional to airspeed\n[B] Directly proportional to airspeed squared (V^2)\n[C] Inversely proportional to airspeed SQUARED (1 / V^2)\n[D] It remains constant",
         "CORRECT: [C]. In level flight, as speed increases, C_L decreases by 1/V^2. Because induced drag is proportional to C_L^2, Induced Drag decreases with 1/V^2, making it dominant at low speeds and tiny at high speeds."),
        ("Q2: What is the primary aerodynamic benefit of fitting winglets to modern jet transport aircraft?",
         "[A] To increase maximum take-off mass\n[B] To reduce Induced Drag by impeding spanwise airflow around wingtips and dissipating wingtip vortices\n[C] To prevent deep stall\n[D] To improve rudder authority",
         "CORRECT: [B]. Winglets act as vertical aerodynamic barriers that disrupt the high-to-low pressure spanwise bleed around wingtips, reducing vortex downwash and cutting induced drag by 3-5%."),
        ("Q3: Under what flight conditions does a transport aircraft generate the strongest, most hazardous wake turbulence vortices?",
         "[A] Fast, light, flaps fully extended\n[B] HEAVY, CLEAN (flaps retracted), and SLOW\n[C] Cruising at high Mach number\n[D] In a steep dive",
         "CORRECT: [B]. Wake vortex strength is proportional to aircraft weight and inversely proportional to airspeed and wingspan. A heavy aircraft flying slowly in clean configuration generates maximum vortex circulation.")
    ]

    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 4 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_pof_ch01()
    build_pof_ch02()
    build_pof_ch03()
    build_pof_ch04()
