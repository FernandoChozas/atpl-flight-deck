#!/usr/bin/env python3
"""
Generator for Subject 081: Principles of Flight (Aerodynamics)
Volume 4: Chapters 10 to 14 (Stability, Controls & Flight Mechanics)
- Chapter 10: Static & Dynamic Stability Fundamentals
- Chapter 11: Longitudinal Stability & Center of Gravity Margins
- Chapter 12: Directional & Lateral Stability (Dutch Roll & Spiral)
- Chapter 13: Flight Controls, Control Tabs & Aerodynamic Balancing
- Chapter 14: Flight Mechanics, Turns, V-n Diagram & Asymmetric Flight

Fully aligned with CAE Oxford Principles of Flight and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/081_principles_of_flight"

def build_pof_ch10():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch10_stability_fundamentals.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 10: Stability Fundamentals")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        10,
        "Static & Dynamic Stability Fundamentals",
        "345-384"
    )

    pdf.add_heading_1("1. Static Stability: Initial Tendency Upon Disturbance")
    pdf.add_paragraph(
        "Stability defines an aircraft's response to an aerodynamic disturbance from trimmed equilibrium:"
    )
    pdf.add_bullet("Positive Static Stability", "The INITIAL tendency to return toward original trimmed equilibrium following disturbance (creates an opposing restoring moment: dC_M / dAlpha < 0).")
    pdf.add_bullet("Neutral Static Stability", "The initial tendency to remain in the displaced position with zero restoring or diverging force (dC_M / dAlpha = 0).")
    pdf.add_bullet("Negative Static Stability (Static Instability)", "The initial tendency to diverge further away from trimmed equilibrium (dC_M / dAlpha > 0).")

    pdf.add_heading_1("2. Dynamic Stability: Behavior Over Time")
    pdf.add_paragraph(
        "Dynamic stability describes the time history of the motion following an initial statically stable response. "
        "Dynamic stability CAN ONLY EXIST if the aircraft possesses positive static stability first!"
    )

    stab_table = [
        ["Dynamic Stability Condition", "Time-History Motion Characteristics", "Physical Restoring & Damping Forces"],
        ["Positive Dynamic Stability", "Oscillations decrease in amplitude over time (damped motion) until steady equilibrium is restored.", "Aerodynamic damping (e.g. tailplane pitch damping) dissipates kinetic energy into air."],
        ["Neutral Dynamic Stability", "Oscillations continue indefinitely with CONSTANT amplitude (undamped sine wave).", "Zero net damping force."],
        ["Negative Dynamic Stability", "Oscillations amplify progressively over time with growing amplitude (divergent oscillation)!", "Energy is continuously pumped into the oscillation, leading to structural divergence."]
    ]
    pdf.add_table(["Dynamic Stability Condition", "Time-History Motion Characteristics", "Physical Restoring & Damping Forces"], stab_table, col_widths=[125.0, 195.0, 180.0])

    pdf.add_heading_1("3. Longitudinal Dynamic Modes: SPPO vs Phugoid")
    pdf.add_paragraph(
        "Disturbing an aircraft longitudinally excites two distinct coupled pitch-speed oscillations:"
    )
    pdf.add_bullet("Short Period Pitch Oscillation (SPPO)", "High frequency (period typically 1 to 2 seconds), heavily damped. Consists of rapid pitch angle and Angle of Attack oscillations at virtually constant airspeed! If under-damped or if pilot attempts manual corrections out-of-phase, can trigger catastrophic Pilot Induced Oscillations (PIO)!")
    pdf.add_bullet("Phugoid Motion (Long Period Mode)", "Low frequency (period typically 20 to 60+ seconds), weakly damped. Consists of a slow exchange between kinetic energy (airspeed) and potential energy (altitude) at VIRTUALLY CONSTANT ANGLE OF ATTACK! Aircraft climbs and slows down, then dives and speeds up. Easily controlled by pilot or autopilot altitude hold.")

    pdf.add_callout(
        "trap",
        "Short Period (SPPO) vs Phugoid Distinction Trap",
        "- Short Period Pitch Oscillation: Variable AOA, CONSTANT airspeed! (High frequency, dangerous for PIO).\n"
        "- Phugoid Oscillation: CONSTANT AOA, variable airspeed and altitude! (Low frequency, easily damped by pilot).\n"
        "- Strict Rule: An aircraft CANNOT be dynamically stable unless it is statically stable first!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch10 = [
        ("Q1: What is the defining characteristic of an aircraft exhibiting POSITIVE STATIC STABILITY?",
         "[A] It oscillates indefinitely at constant amplitude\n[B] Its INITIAL tendency following an aerodynamic disturbance is to develop forces that restore it toward original trimmed equilibrium\n[C] It requires no pilot controls\n[D] It flies at supersonic speed",
         "CORRECT: [B]. Static stability describes purely the immediate initial tendency upon release from a disturbed displacement. Positive static stability means restoring moments oppose the disturbance."),
        ("Q2: In longitudinal dynamic flight modes, how do angle of attack and airspeed behave during a classic PHUGOID oscillation?",
         "[A] Angle of attack oscillates rapidly while airspeed remains constant\n[B] Angle of attack remains virtually CONSTANT while airspeed and altitude oscillate slowly\n[C] Both parameters remain completely frozen\n[D] Pitch damping is zero",
         "CORRECT: [B]. The phugoid mode is a long-period trade between kinetic and potential energy. Because pitch attitude tracks the flight path, the angle of attack remains essentially constant while speed and altitude cycle."),
        ("Q3: Can an aircraft possess positive dynamic stability if it has negative static stability?",
         "[A] Yes, always\n[B] NO, dynamic stability requires positive static stability as a prerequisite\n[C] Only at high Mach numbers\n[D] Only with flaps down",
         "CORRECT: [B]. If an aircraft is statically unstable, it immediately diverges away from equilibrium, preventing any oscillatory motion from developing. Therefore, positive static stability is mandatory for dynamic stability.")
    ]

    for q_text, opts, exp in questions_ch10:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 10 compiled: {pdf_path}")


def build_pof_ch11():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch11_longitudinal_stability_cg.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 11: Longitudinal Stability & CG")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        11,
        "Longitudinal Stability & CG Margins (Neutral Point)",
        "385-424"
    )

    pdf.add_heading_1("1. Longitudinal Equilibrium: Wing & Tailplane Moments")
    pdf.add_paragraph(
        "Pitch stability (rotation about the lateral axis) is dominated by the interaction between the wing and horizontal tailplane:"
    )
    pdf.add_bullet("Wing Pitching Moment", "Cambered wings generate a constant nose-down pitching moment about their Aerodynamic Center (M_AC). Center of Gravity (CG) is positioned forward of the wing center of lift, creating an additional nose-down couple.")
    pdf.add_bullet("Tailplane Download (Downforce)", "To balance these nose-down couples in trimmed flight, the horizontal tailplane must generate a continuous DOWNWARD AERODYNAMIC FORCE (Tail Download)! This downward force reduces effective total lift and increases fuel burn, but provides pitch stability.")
    pdf.add_bullet("Longitudinal Dihedral", "The angle of incidence of the horizontal stabilizer is set SMALLER than the wing incidence (tailplane incidence < wing incidence). When the aircraft pitches up, the percentage increase in tailplane AOA is greater than the wing, generating an upward restoring lift that pitches the nose back down!")

    pdf.add_heading_1("2. The Neutral Point (NP) & Static Margin")
    pdf.add_paragraph(
        "The Neutral Point is the theoretical aerodynamic center of the ENTIRE AIRCRAFT (wing + fuselage + tail):"
    )
    pdf.add_bullet("Neutral Point (NP)", "The unique CG position where the overall aircraft pitching moment does not change with angle of attack (dC_M / dAlpha = 0). At the Neutral Point, static pitch stability is EXACTLY ZERO (neutral).")
    pdf.add_bullet("Static Margin", "The physical distance between the Center of Gravity and the Neutral Point, expressed as a percentage of the Mean Aerodynamic Chord (MAC): Static Margin = (x_NP - x_CG) / MAC.")
    pdf.add_bullet("Stable CG Regime", "For positive longitudinal stability, the Center of Gravity MUST BE LOCATED FORWARD of the Neutral Point! Static Margin must be POSITIVE (typically 5% to 15% MAC in civil transports).")

    cg_table = [
        ["CG Location Condition", "Stability & Stick Force per 'g'", "Performance, Drag & Stall Speed"],
        ["Forward CG Limit", "MAXIMUM stability. Heavy stick forces; high stick force per g. Excellent recovery from stall.", "High tailplane download required -> higher effective weight -> HIGHER STALL SPEED, higher drag, higher fuel burn. Limited by elevator authority in landing flare!"],
        ["Aft CG Limit", "REDUCED stability. Very light stick forces; low stick force per g. Highly sensitive controls.", "Lower tailplane download -> lower trim drag, LOWER FUEL BURN, lower stall speed. Limited by minimum mandatory static margin!"],
        ["CG Aft of Neutral Point", "STATICALLY UNSTABLE! Any pitch disturbance causes divergent pitch runaway into deep stall or structural overload!", "STRICTLY PROHIBITED in certified civil transport aircraft!"]
    ]
    pdf.add_table(["CG Location Condition", "Stability & Stick Force per 'g'", "Performance, Drag & Stall Speed"], cg_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_callout(
        "trap",
        "Forward CG vs Aft CG Flight Characteristics Trap",
        "- FORWARD CG: More stable, heavier stick forces, higher stall speed, higher fuel consumption, flare authority limited!\n"
        "- AFT CG: Less stable, lighter stick forces (danger of overstressing airframe), lower stall speed, lower fuel consumption (higher cruise range)!\n"
        "- Aft CG Limit Rule: The aft CG limit is determined primarily by the minimum acceptable static longitudinal stability margin!",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch11 = [
        ("Q1: What happens to aircraft static longitudinal stability and stick forces as the Center of Gravity moves progressively REARWARD toward the aft limit?",
         "[A] Stability increases and stick forces increase\n[B] Stability DECREASES and stick force per 'g' DECREASES (controls feel lighter and more sensitive)\n[C] Stability remains unaffected\n[D] The aircraft becomes uncontrollable immediately",
         "CORRECT: [B]. Moving CG aft shortens the distance to the Neutral Point (reducing Static Margin). This weakens restoring moments, reducing pitch stability and lowering stick force per g, making the aircraft more agile but sensitive."),
        ("Q2: Why does an aircraft cruising with a FORWARD Center of Gravity burn more fuel than with an AFT Center of Gravity?",
         "[A] Engine thrust vector is misaligned\n[B] Forward CG requires a larger downward tailplane force to balance the nose-down moment, increasing total lift required and induced trim drag\n[C] Fuel cannot flow to engines\n[D] Forward CG increases skin friction",
         "CORRECT: [B]. Forward CG creates a large nose-down moment, requiring a strong downward tailplane aerodynamic force. The wings must produce extra lift to support both aircraft weight and this tail download, increasing induced drag and fuel burn."),
        ("Q3: What aerodynamic position represents the absolute maximum aft theoretical limit for positive static longitudinal stability?",
         "[A] The wing leading edge\n[B] The NEUTRAL POINT of the aircraft\n[C] The 25% MAC point\n[D] The elevator hinge line",
         "CORRECT: [B]. If the CG reaches the Neutral Point, the Static Margin becomes zero (neutral stability). Moving the CG aft of the Neutral Point results in negative static stability (pitch divergence).")
    ]

    for q_text, opts, exp in questions_ch11:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 11 compiled: {pdf_path}")


def build_pof_ch12():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch12_directional_lateral_stability.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 12: Directional & Lateral Stability")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        12,
        "Directional & Lateral Stability (Dutch Roll & Spiral)",
        "425-464"
    )

    pdf.add_heading_1("1. Directional (Weathercock) Stability")
    pdf.add_paragraph(
        "Directional stability is stability about the normal (vertical) axis following a sideslip angle (Beta):"
    )
    pdf.add_bullet("Weathercock Principle", "When an aircraft sideslips, relative wind strikes the fuselage and vertical tail from the side. The vertical stabilizer (fin) generates a horizontal aerodynamic restoring force behind the CG, yawing the nose back into the relative wind.")
    pdf.add_bullet("Contributions to Directional Stability", "Vertical Fin (major positive stabilizing contributor); Rear Fuselage (stabilizing); Swept Wings (stabilizing: retreating wing has higher effective span and profile drag, pulling nose straight); Forward Fuselage and Nacelles (DESTABILIZING: generate adverse destabilizing yaw moments ahead of CG).")

    pdf.add_heading_1("2. Lateral (Dihedral) Stability & Cross-Coupling")
    pdf.add_paragraph(
        "Lateral stability is stability about the longitudinal axis (roll) when perturbed into a sideslip:"
    )
    pdf.add_bullet("Geometric Dihedral (Gamma)", "Upward angle of wings from root to tip. When wings roll into a sideslip, the low wing meets relative airflow at a HIGHER effective angle of attack than the high wing, generating more lift and rolling the wings back level!")
    pdf.add_bullet("Wing Sweepback Effect", "Massive contributor to lateral stability! When a swept-wing aircraft sideslips, the wing into the wind (leading wing) has reduced effective sweep (Lambda - Beta), increasing its normal velocity component (V cos(Lambda - Beta)) and lift, while the trailing wing loses lift. This produces a powerful restoring roll moment into the slip!")
    pdf.add_bullet("High Wing (Anhedral vs Dihedral)", "High-mounted wings experience airflow blockage by the fuselage during sideslip, increasing high-wing lift (keel effect). Because swept high-wing air transports (C-17, Antonov) possess EXCESSIVE lateral stability, they use ANHEDRAL (negative dihedral / drooped wings) to restore balance!")

    pdf.add_heading_1("3. Dynamic Modes: Dutch Roll vs Spiral Divergence")
    dynamic_lat_table = [
        ["Dynamic Mode", "Relative Stability Balance", "Coupled Flight Motion & Operational Hazard"],
        ["Dutch Roll", "Excessive Lateral Stability (Dihedral/Sweep) combined with WEAK Directional Stability.", "A coupled out-of-phase yaw and roll motion tracing a figure-8 corkscrew trajectory. Annoying to passengers; potentially divergent at high altitudes. MANDATORY REMEDY: Yaw Damper!"],
        ["Spiral Divergence", "STRONG Directional Stability combined with WEAK Lateral Stability (Dihedral).", "Aircraft sideslips into turn; strong fin weathercocks nose into turn, while weak dihedral fails to level wings. Bank angle and rate of descent steepen progressively into a high-speed spiral dive. Non-oscillatory; slow divergence; easily corrected by pilot."]
    ]
    pdf.add_table(["Dynamic Mode", "Relative Stability Balance", "Coupled Flight Motion & Operational Hazard"], dynamic_lat_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_callout(
        "trap",
        "Dutch Roll vs Spiral Stability Trade-off",
        "- Designing for high lateral stability suppresses spiral dive, BUT CREATES DUTCH ROLL!\n"
        "- Designing for high directional stability suppresses Dutch roll, BUT CREATES SPIRAL DIVERGENCE!\n"
        "- Modern transport jets accept mild spiral divergence (easily controlled by autopilot) and eliminate Dutch roll using automatic YAW DAMPERS.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch12 = [
        ("Q1: What stability combination causes an aircraft to be susceptible to DUTCH ROLL?",
         "[A] Strong directional stability and weak lateral stability\n[B] Strong LATERAL stability (dihedral effect) combined with relatively WEAK DIRECTIONAL stability\n[C] Forward CG\n[D] Zero sweepback",
         "CORRECT: [B]. Dutch roll occurs when roll restoring forces (dihedral/sweep) are much stronger than directional yaw restoring forces. The aircraft over-corrects in roll before yaw can damp out, resulting in a corkscrew oscillation."),
        ("Q2: Why do many military cargo aircraft with swept, high-mounted wings incorporate ANHEDRAL (drooped wings)?",
         "[A] To increase cruise speed\n[B] To reduce excessive lateral stability created by the combination of high wing position and wing sweep, which would otherwise induce violent Dutch roll\n[C] To assist engine maintenance\n[D] To increase take-off lift",
         "CORRECT: [B]. Both swept wings and high-wing placement generate strong lateral stability (effective dihedral). Left unchecked, this makes the aircraft violently prone to Dutch roll. Anhedral is added to reduce roll-due-to-sideslip to a safe balance."),
        ("Q3: What is the primary operational function of an aircraft Yaw Damper system?",
         "[A] To steer the nosewheel on landing\n[B] To detect and immediately suppress Dutch Roll oscillations by commanding automatic rudder deflections\n[C] To prevent stalls\n[D] To trim the ailerons",
         "CORRECT: [B]. A yaw damper uses rate gyros to sense yaw rate and commands small, fast opposing rudder deflections via servo actuators, damping out Dutch roll without pilot pedal movement.")
    ]

    for q_text, opts, exp in questions_ch12:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 12 compiled: {pdf_path}")


def build_pof_ch13():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch13_flight_controls_tabs_balance.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 13: Flight Controls & Tabs")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        13,
        "Flight Controls, Control Tabs & Aerodynamic Balance",
        "465-504"
    )

    pdf.add_heading_1("1. Primary Controls & Adverse Yaw Mitigation")
    pdf.add_paragraph(
        "Primary flight controls govern rotation about the aircraft's three axes (Ailerons: Roll; Elevator: Pitch; Rudder: Yaw):"
    )
    pdf.add_bullet("Adverse Yaw Phenomenon", "When ailerons deflect to initiate a roll, the downward-deflected aileron on the rising wing produces more lift AND MORE INDUCED DRAG than the upward-deflected aileron on the falling wing. This differential drag yaws the nose in the direction OPPOSITE to the commanded bank!")
    pdf.add_bullet("Differential Ailerons", "The up-going aileron deflects through a substantially LARGER angle (e.g. 25° up) than the down-going aileron (e.g. 10° down). The large up-deflection generates extra parasite form drag on the inside wing, counteracting adverse yaw.")
    pdf.add_bullet("Frise Ailerons", "The aileron hinge is set back from its leading edge. When deflected UP, the lower lip of the aileron protrudes below the wing lower surface into the slipstream, creating parasite drag on the down-going wing to balance adverse yaw.")
    pdf.add_bullet("Roll Spoilers", "Spoilers deflect upward ONLY on the down-going wing, destroying lift and adding large parasite drag on the inside of the turn, completely eliminating adverse yaw at high speeds.")

    pdf.add_heading_1("2. Control Tabs & Aerodynamic Balancing")
    pdf.add_paragraph(
        "Aerodynamic balancing reduces the physical hinge moment (stick force) required from the pilot:"
    )

    tabs_table = [
        ["Control Tab / Balance Device", "Mechanical Deflection Direction", "Aerodynamic Function & Stick Force Effect"],
        ["Trim Tab (Controllable)", "Deflects OPPOSITE to primary control surface (moved by cockpit trim wheel).", "Holds control surface in deflected position with ZERO stick force from pilot. Trims aircraft for hands-off flight."],
        ["Balance Tab", "Mechanically geared to deflect OPPOSITE to primary surface automatically.", "Reduces pilot control stick forces by using tab aerodynamic lift to help deflect main surface."],
        ["Anti-Balance Tab", "Mechanically geared to deflect in the SAME DIRECTION as primary surface.", "INCREASES control feel and stick forces! Mandatory on all-flying stabilators (Piper Cherokee) to prevent pilot over-controlling and overstressing airframe."],
        ["Servo Tab", "Directly connected to pilot cockpit controls; main surface is free-floating.", "Pilot moves tab only; tab aerodynamic force pushes the entire large control surface into position (BAe 146, DC-9)."],
        ["Spring Tab", "Incorporates a torsion spring in the linkage.", "At low speed, spring acts as rigid rod (direct manual control). At high dynamic pressure, spring compresses, allowing tab to assist pilot as a servo tab."]
    ]
    pdf.add_table(["Control Tab / Balance Device", "Mechanical Deflection Direction", "Aerodynamic Function & Stick Force Effect"], tabs_table, col_widths=[125.0, 185.0, 190.0])

    pdf.add_callout(
        "trap",
        "Balance Tab vs Anti-Balance Tab Direction Trap",
        "- Balance Tab: Moves OPPOSITE to control surface -> REDUCES control stick forces!\n"
        "- Anti-Balance Tab: Moves in SAME DIRECTION as control surface -> INCREASES control stick forces and artificial feel!\n"
        "- Trim Tab: Cockpit trim nose-down commands trim tab UP, which aerodynamically forces the elevator DOWN.",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch13 = [
        ("Q1: How do DIFFERENTIAL AILERONS reduce adverse yaw during a roll maneuver?",
         "[A] By disconnecting the rudder\n[B] The up-going aileron deflects through a GREATER angle than the down-going aileron, producing extra parasite drag on the inside wing to counter adverse induced drag\n[C] By lowering the flaps\n[D] By moving both ailerons downward together",
         "CORRECT: [B]. The up-aileron deflects significantly farther than the down-aileron, creating deliberate form drag on the descending wing to counteract the adverse induced drag of the rising wing."),
        ("Q2: In what direction does an ANTI-BALANCE TAB move relative to the main control surface, and what is its operational purpose?",
         "[A] In the opposite direction, to reduce control forces to zero\n[B] In the SAME DIRECTION as the control surface, to INCREASE stick forces and provide artificial aerodynamic feel on an all-flying tail\n[C] It remains locked in cruise\n[D] It trims the rudder only",
         "CORRECT: [B]. An anti-balance tab deflects in the same direction as the surface, opposing pilot input and increasing stick force per g, preventing over-controlling on light all-flying stabilators."),
        ("Q3: When the pilot trims for NOSE-UP pitch using a conventional elevator trim tab, in which direction does the trim tab surface actually deflect?",
         "[A] The trim tab deflects UP\n[B] The trim tab deflects DOWNWARDS, creating an upward aerodynamic force that pushes and holds the elevator UP\n[C] The tab does not move\n[D] The tab moves laterally",
         "CORRECT: [B]. To hold the elevator up for nose-up trim, the trim tab at the elevator trailing edge must deflect DOWN, generating upward aerodynamic lift that forces the elevator trailing edge up.")
    ]

    for q_text, opts, exp in questions_ch13:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 13 compiled: {pdf_path}")


def build_pof_ch14():
    pdf_path = os.path.join(OUTPUT_DIR, "081_ch14_flight_mechanics_vn_diagram.pdf")
    pdf = PDFBuilder("Principles of Flight", "081", "Chapter 14: Flight Mechanics & V-n Diagram")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Principles of Flight",
        14,
        "Flight Mechanics, V-n Diagram & Asymmetric Flight",
        "505-548"
    )

    pdf.add_heading_1("1. Coordinated Turns: Load Factor, Radius & Rate")
    pdf.add_paragraph(
        "In a level coordinated turn, aerodynamic lift is tilted inward at bank angle Phi, providing the horizontal centripetal force (F_c = L x sin(Phi)):"
    )
    pdf.add_bullet("Load Factor (n)", "Vertical equilibrium requires L x cos(Phi) = Weight (W). Therefore: Load Factor n = Lift / Weight = 1 / cos(Phi). At 60° bank: n = 1 / cos(60°) = 2.0 g!")
    pdf.add_bullet("Turn Radius Formula", "Radius (R) = V^2 / (g x tan(Phi)). Turn radius depends EXCLUSIVELY on True Airspeed and Bank Angle! For a given bank angle, radius increases with speed squared (doubling TAS quadruples turn radius!).")
    pdf.add_bullet("Rate of Turn (ROT)", "ROT = (g x tan(Phi)) / V. Rate 1 Turn = 3°/second (360° turn in 2 minutes). Rule of thumb: Bank Angle for Rate 1 = (TAS / 10) + 7 (e.g. at 140 kt: 14 + 7 = 21° bank).")

    pdf.add_heading_1("2. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Load Factor and Turn Stall Speed in a Steep Turn",
        "SCENARIO (Fundamental Flight Mechanics Exam Drill):\n"
        "An aircraft has a level, unaccelerated 1g stall speed Vs = 60 knots:\n"
        "- The pilot executes a level coordinated steep turn at 60° bank angle (Phi = 60°)\n"
        "QUESTION: What is the load factor (n), and what is the new accelerated stall speed (Vst) in the turn?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Load Factor (n):\n"
        "  - Formula: n = 1 / cos(Bank Angle)\n"
        "  - Bank Angle = 60° -> cos(60°) = 0.50 exactly!\n"
        "  - Load Factor n = 1 / 0.50 = 2.0 g!\n"
        "  - (Both the aircraft structure and pilot experience twice their normal weight!).\n\n"
        "Step 2: Calculate the Accelerated Turn Stall Speed (Vst):\n"
        "  - Master Formula: Vst = Vs x sqrt(n)\n"
        "  - Vs = 60 knots\n"
        "  - sqrt(n) = sqrt(2.0) = 1.414\n"
        "  - Vst = 60 kt x 1.414 = 84.8 knots (~85 knots)!\n\n"
        "FINAL ANSWER: Load Factor = 2.0 g. Turn Stall Speed = 85 knots (a 41.4% increase in stall speed!). If airspeed drops below 85 kt during a 60° bank turn, the aircraft will stall immediately, even though it was flying safely above its 60 kt straight stall speed!",
        max_chars=86
    )

    pdf.add_heading_1("3. The V-n Diagram (Maneuvering Flight Envelope)")
    pdf.add_paragraph(
        "The V-n diagram defines the structural and aerodynamic boundaries within which an aircraft may be safely operated:"
    )

    vn_table = [
        ["Speed / Boundary on V-n Diagram", "Regulatory Definition (CS-25 / CS-23)", "Structural & Aerodynamic Limit Meaning"],
        ["Curved Left Boundary (Stall Line)", "n = C_L_max x (1/2 rho V^2) / (W/S).", "Aerodynamic stall limit. Left of this line, the aircraft cannot generate enough lift to fly."],
        ["Maneuvering Speed (V_A)", "Intersection of positive stall curve and limit load factor.", "The MAXIMUM speed at which FULL, ABRUPT aerodynamic control deflection can be applied without exceeding structural limit load! (Aircraft stalls before structural failure)."],
        ["Positive Limit Load Factor", "+2.5 g (Transport CS-25); +3.8 g (Normal CS-23).", "Maximum certified load factor without permanent structural deformation."],
        ["Ultimate Load Factor", "1.5 x Limit Load Factor (+3.75 g for CS-25).", "Airframe must withstand ultimate load for AT LEAST 3 SECONDS without catastrophic failure!"],
        ["Design Dive Speed (V_D / M_D)", "Maximum structural speed envelope limit.", "Highest speed demonstrated in dive tests; margins above V_MO / M_MO."]
    ]
    pdf.add_table(["Speed / Boundary on V-n Diagram", "Regulatory Definition (CS-25 / CS-23)", "Structural & Aerodynamic Limit Meaning"], vn_table, col_widths=[125.0, 185.0, 190.0])

    pdf.add_heading_1("4. Multi-Engine Asymmetric Flight & V_MCA")
    pdf.add_paragraph(
        "When an engine fails on a multi-engine aircraft, asymmetric thrust creates severe yaw and roll toward the dead engine:"
    )
    pdf.add_bullet("The Critical Engine", "On aircraft with conventional clockwise-rotating propellers, failure of the LEFT ENGINE is critical because the right engine's center of thrust acts farther from the fuselage centerline due to: 1. P-Factor (Asymmetric Blade Effect); 2. Accelerated Slipstream; 3. Torque Reaction; 4. Gyroscopic Precession.")
    pdf.add_bullet("Minimum Control Speed Airborne (V_MCA)", "The minimum calibrated airspeed at which directional and lateral control can be safely maintained with the critical engine inoperative, maximum take-off power on the operating engine, and up to 5° OF BANK HELD INTO THE OPERATING ENGINE! If airspeed drops below V_MCA, rudder authority is lost and catastrophic uncontrollable roll/spin occurs!")

    pdf.add_callout(
        "trap",
        "V_MCA Bank Angle & Weight Dependencies",
        "- 5° Bank Rule: Banking up to 5° TOWARDS THE LIVE ENGINE uses horizontal lift to assist the rudder, REDUCING V_MCA significantly!\n"
        "- Wings Level with Ball Centered: Increases V_MCA by 15-20 knots! Highly dangerous!\n"
        "- Weight Effect: Heavier aircraft has LOWER V_MCA (horizontal component of heavier lift vector helps counter yaw)!\n"
        "- Density Altitude: Higher altitude reduces engine thrust, which REDUCES yaw moment and LOWERS V_MCA!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch14 = [
        ("Q1: What is the aerodynamic definition and safety significance of the 'Maneuvering Speed' (V_A)?",
         "[A] The maximum speed for extending flaps\n[B] The maximum speed at which full, abrupt deflection of flight controls can be made without risk of exceeding structural limit load factors, because the aircraft will stall aerodynamically before breaking\n[C] The minimum drag speed\n[D] The best rate of climb speed",
         "CORRECT: [B]. At speeds at or below V_A, the wing will stall before reaching the structural limit load factor (+2.5g on transport, +3.8g on utility), preventing structural overload during abrupt maneuvers."),
        ("Q2: Under CS-25 regulations, what is the 'Ultimate Load Factor' requirement for transport category aircraft?",
         "[A] Exactly equal to the limit load\n[B] 1.5 times the Limit Load Factor, which the structure must withstand for at least 3 seconds without collapsing\n[C] 9.0 g\n[D] 4.0 g",
         "CORRECT: [B]. Ultimate load incorporates a safety factor of 1.50 over the limit load (+2.5g x 1.5 = +3.75g). The airframe must sustain ultimate load for at least 3 seconds without structural collapse."),
        ("Q3: Why is the LEFT engine considered the 'critical engine' on conventional twin-engine piston aircraft with clockwise-rotating propellers?",
         "[A] Left engine has lower horsepower\n[B] The right engine's center of thrust acts at a greater lateral moment arm from the fuselage centerline due to P-factor (asymmetric blade loading), generating more severe yaw if the left engine fails\n[C] Left engine drives the alternator\n[D] Propeller wash affects the cockpit",
         "CORRECT: [B]. Due to P-factor at high angles of attack, the descending blade produces more thrust. For clockwise propellers, this shifts the right engine's thrust line farther right, creating a larger yaw moment than the left engine.")
    ]

    for q_text, opts, exp in questions_ch14:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"POF Chapter 14 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_pof_ch10()
    build_pof_ch11()
    build_pof_ch12()
    build_pof_ch13()
    build_pof_ch14()
