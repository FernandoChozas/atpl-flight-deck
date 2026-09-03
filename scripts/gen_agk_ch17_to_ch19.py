#!/usr/bin/env python3
"""
Generator for Subject 021: AGK - Airframe, Systems, Electrics & Powerplant
Volume 4: Chapters 17 to 19 (Powerplant - Piston Engines & Propellers)
- Chapter 17: Piston Engines Structure, 4-Stroke Cycle & Supercharging
- Chapter 18: Piston Fuels, Carburation, Injection & Lubrication
- Chapter 19: Propellers & Constant Speed Governors

Fully aligned with CAE Oxford Book 4 (Powerplant) and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant"

def build_agk_ch17():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch17_piston_engines_cycles.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 17: Piston Engines & 4-Stroke Cycle")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        17,
        "Piston Engines Structure & 4-Stroke Cycle",
        "1-48 (Pwr)"
    )

    pdf.add_heading_1("1. The Four-Stroke Otto Cycle & Valve Timing")
    pdf.add_paragraph(
        "Aero piston engines operate on the 4-stroke constant-volume Otto cycle. One complete engine cycle requires "
        "four piston strokes (two complete 360° revolutions of the crankshaft / 720° total rotation):"
    )

    stroke_table = [
        ["1. Induction", "TDC to BDC (Top to Bottom Dead Center)", "0° to 180°. Inlet valve open, exhaust valve closed. Low cylinder pressure draws in air-fuel mixture."],
        ["2. Compression", "BDC to TDC", "180° to 360°. Both valves closed. Piston compresses mixture into combustion chamber (~7:1 to 9:1 compression ratio). Ignition fires ~20-25° BEFORE TDC!"],
        ["3. Power (Combustion)", "TDC to BDC", "360° to 540°. Both valves closed. Burning fuel gases expand rapidly, driving piston down to generate mechanical crankshaft torque."],
        ["4. Exhaust", "BDC to TDC", "540° to 720°. Exhaust valve open, inlet valve closed. Piston sweeps burned combustion gases out through exhaust manifold."]
    ]
    pdf.add_table(["Stroke Name", "Piston Travel Direction", "Crankshaft Rotation & Valve Position"], stroke_table, col_widths=[110.0, 190.0, 200.0])

    pdf.add_bullet("Valve Lead & Lag", "Inlet valve opens before TDC (valve lead) and closes after BDC (valve lag) to capitalize on incoming gas inertia, maximizing cylinder volumetric filling.")
    pdf.add_bullet("Valve Overlap", "The period around TDC at the end of the exhaust stroke and start of the induction stroke when BOTH inlet and exhaust valves are open simultaneously. Incoming fresh charge assists scavenging of exhaust gases and cools valve heads.")

    pdf.add_heading_1("2. Power Terminology, Efficiencies & BMEP")
    pdf.add_paragraph(
        "Engine performance is measured across different efficiency boundaries:"
    )
    pdf.add_bullet("Indicated Horsepower (IHP)", "Theoretical power developed by expanding combustion gases inside the cylinders: IHP = (P_L_A_N_K) / 33,000, where P = Indicated Mean Effective Pressure (IMEP).")
    pdf.add_bullet("Brake Horsepower (BHP)", "Actual usable mechanical power delivered at the propeller drive shaft, measured with a dynamometer: BHP = IHP - FHP (Friction Horsepower lost to bearing friction, oil pumping, and driving accessories).")
    pdf.add_bullet("Mechanical Efficiency", "BHP / IHP (typically 80% to 90%).")
    pdf.add_bullet("Brake Mean Effective Pressure (BMEP)", "The average effective combustion pressure acting on the piston throughout the power stroke that produces the shaft BHP output.")

    pdf.add_heading_1("3. Supercharging & Turbocharging Mechanics")
    pdf.add_paragraph(
        "Naturally aspirated engines lose power as altitude increases (~3% power loss per 1,000 ft) due to decreasing atmospheric density. "
        "Forced induction restores manifold pressure (MAP):"
    )
    pdf.add_bullet("Supercharger (Mechanically Driven)", "Centrifugal compressor driven by engine crankshaft gears. Draws significant engine power (parasitic loss) to spin compressor.")
    pdf.add_bullet("Turbocharger (Exhaust Driven)", "Exhaust gas spins an exhaust turbine wheel connected via a common shaft to a centrifugal compressor. Harnesses normally wasted exhaust gas energy with minimal parasitic shaft load.")
    pdf.add_bullet("Wastegate Controller", "A butterfly or poppet valve that modulates how much exhaust gas passes across the turbo turbine vs bypassing directly overboard. Modulated by an oil-pressure actuator to maintain selected manifold pressure.")
    pdf.add_bullet("Critical Altitude", "The maximum altitude at which a turbocharged engine can maintain its maximum rated sea-level manifold pressure (or rated BHP) with the wastegate fully closed. Above critical altitude, manifold pressure and power decline steadily with altitude.")

    pdf.add_callout(
        "trap",
        "Critical Altitude Definition & Behavior",
        "- Definition: The maximum altitude at which a turbocharged engine can produce its maximum rated continuous power / sea level manifold pressure.\n"
        "- Below Critical Altitude: The wastegate is PARTIALLY OPEN and closes progressively as altitude increases to maintain constant MAP.\n"
        "- At Critical Altitude: The wastegate reaches its FULLY CLOSED position!\n"
        "- Above Critical Altitude: The wastegate cannot close any further; MAP and engine power drop with further climb exactly like a naturally aspirated engine!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch17 = [
        ("Q1: What is 'valve overlap' in a four-stroke aero piston engine?",
         "[A] The time when both spark plugs fire together\n[B] The angular period of crankshaft rotation around TDC when both the inlet and exhaust valves are open simultaneously\n[C] The time when both valves are closed on the power stroke\n[D] The clearance between valve rocker and stem",
         "CORRECT: [B]. Valve overlap occurs at the end of the exhaust stroke and start of the induction stroke when the inlet valve opens before the exhaust valve has completely seated, enhancing scavenging."),
        ("Q2: In a turbocharged aircraft piston engine, what is the 'Critical Altitude'?",
         "[A] The altitude where detonation always occurs\n[B] The maximum altitude at which the engine can maintain its maximum rated power or sea-level manifold pressure with the wastegate fully closed\n[C] The altitude where the turbocharger compressor stalls\n[D] The service ceiling of the aircraft",
         "CORRECT: [B]. Critical altitude is reached when the turbo wastegate is 100% closed. Below this altitude, full rated power can be maintained; above it, manifold pressure declines as ambient density drops."),
        ("Q3: How does Brake Horsepower (BHP) compare mathematically to Indicated Horsepower (IHP)?",
         "[A] BHP is always greater than IHP\n[B] BHP = IHP minus Friction Horsepower (FHP)\n[C] BHP is unrelated to IHP\n[D] BHP = IHP multiplied by 1.5",
         "CORRECT: [B]. Indicated Horsepower is the total chemical energy converted in the cylinders. Brake Horsepower is the net usable shaft power delivered to the propeller after deducting internal friction horsepower losses.")
    ]

    for q_text, opts, exp in questions_ch17:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 17 compiled: {pdf_path}")


def build_agk_ch18():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch18_piston_fuels_carburation.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 18: Fuels, Carburation & Lubrication")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        18,
        "Aviation Gasoline, Carburation & Lubrication",
        "49-92 (Pwr)"
    )

    pdf.add_heading_1("1. Aviation Gasoline (AVGAS): Grades, Color Codes & Detonation")
    pdf.add_paragraph(
        "Piston aircraft burn Aviation Gasoline (AVGAS) engineered for high volatility resistance and anti-knock stability:"
    )

    avgas_table = [
        ["AVGAS 100LL (Low Lead)", "DYED BLUE", "Most common aviation gasoline worldwide. 100 octane rating; contains limited tetraethyl lead (TEL) anti-knock additive. Density ~0.72 kg/litre."],
        ["AVGAS 100 (Green)", "DYED GREEN", "High-lead 100/130 aviation gasoline. Used in high-power supercharged vintage piston engines."],
        ["AVGAS 80/87", "DYED RED", "Low-octane fuel for vintage low-compression light aircraft engines."],
        ["Jet A-1 (Kerosene)", "CLEAR / STRAW (Colorless)", "STRICT PROHIBITION: NEVER PUT JET FUEL IN A PISTON ENGINE! Causes immediate catastrophic engine detonation, complete power loss, and engine destruction on take-off!"]
    ]
    pdf.add_table(["Fuel Grade", "Identification Dye Color", "Octane / Performance Rating & Typical Use"], avgas_table, col_widths=[110.0, 150.0, 240.0])

    pdf.add_bullet("Detonation (Knocking)", "Uncontrolled explosive auto-ignition of the remaining unburned end-gas ahead of the normal flame front. Creates supersonic shockwaves, extreme cylinder head temperatures (CHT), and can burn holes through piston crowns within seconds! Caused by: low fuel octane, excessively lean mixture, high MAP with low RPM, or high CHT.")
    pdf.add_bullet("Pre-Ignition", "Combustion initiated BEFORE the spark plug fires, caused by an incandescent hotspot in the cylinder (glowing carbon deposit, cracked spark plug insulator). Can lead directly to violent detonation.")

    pdf.add_heading_1("2. Carburettor Icing: Types & Ambient Conditions")
    pdf.add_paragraph(
        "Float-type carburettors are highly susceptible to ice formation even in warm, sunny weather:"
    )
    pdf.add_bullet("Fuel Evaporation Ice", "Liquid gasoline vaporizing in the venturi absorbs latent heat of vaporization, dropping air temperature inside the carburettor throat by up to 20°C to 25°C!")
    pdf.add_bullet("Throttle Ice", "Pressure drop across a partially closed throttle butterfly valve causes adiabatic expansion cooling, causing moisture to freeze directly onto the throttle valve.")
    pdf.add_bullet("Icing Risk Envelope", "Carburettor icing can occur with Outside Air Temperature (OAT) as high as +25°C or even +30°C if relative humidity is above 80%! Most severe risk occurs between -7°C and +21°C at moderate-to-high humidity and low power settings (descent/glide).")
    pdf.add_bullet("Carb Heat Operation", "Selects unfiltered air ducted across the hot exhaust shroud. When carb heat is selected ON: 1. Manifold pressure / RPM drops initially (hot air is less dense); 2. Engine runs rough as melted ice passes through; 3. RPM / MAP then rises higher than original as ice clears.")

    pdf.add_callout(
        "trap",
        "Carburettor Heat Application Sequence Trap",
        "- Carburettor heat is an ANTI-ICING and DE-ICING control. When selected ON, it admits hot, UNFILTERED air into the engine.\n"
        "- Ground Rule: Do NOT use carb heat on the ground in dusty conditions (unfiltered air sucks grit into cylinders) except for brief pre-take-off functional check!\n"
        "- Throttle Rule: Carb heat should ALWAYS be applied BEFORE reducing power for descent, because exhaust shrouds cool rapidly at low throttle!",
        max_chars=86
    )

    pdf.add_heading_1("3. Engine Lubrication Systems: Wet vs Dry Sump")
    pdf.add_paragraph(
        "Engine oil cools internal components, lubricates bearing journals to reduce friction, cleans away carbon particles, cushions impact loads, "
        "and forms a gas seal between piston rings and cylinder walls:"
    )
    pdf.add_bullet("Wet-Sump System", "Oil is stored in the crankcase oil pan (sump) beneath the engine. Used on light aircraft (Lycoming O-320/O-360). Simple, but oil sloshes during aerobatics/maneuvers, risking pump cavitation.")
    pdf.add_bullet("Dry-Sump System", "Oil is stored in an external separate oil tank. A scavenge pump (with capacity 25-50% larger than the pressure pump) draws oil from the shallow crankcase pan, routes it through an oil cooler, and pumps it back to the tank.")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch18 = [
        ("Q1: What ambient weather conditions present the highest risk for severe carburettor icing in an aircraft piston engine?",
         "[A] OAT -20°C with 10% relative humidity\n[B] OAT between -7°C and +21°C with high relative humidity (>80%), especially at low power settings\n[C] OAT +35°C in dry desert air\n[D] Only when flying through freezing rain",
         "CORRECT: [B]. Fuel vaporization drops air temperature by up to 25°C. When ambient air is between -7°C and +21°C with high humidity, this temperature drop freezes moisture rapidly, choking the carburettor venturi."),
        ("Q2: What is the aviation dye color code for AVGAS 100LL (Low Lead)?",
         "[A] Green\n[B] Red\n[C] Blue\n[D] Amber",
         "CORRECT: [C]. AVGAS 100LL is dyed BLUE worldwide. (AVGAS 100 is green, AVGAS 80 is red, and Jet A-1 is clear/straw)."),
        ("Q3: Why does engine RPM drop slightly when carburettor heat is selected ON in an aircraft with a fixed-pitch propeller?",
         "[A] The ignition timing retards\n[B] Hot air is less dense than cold ambient air, reducing charge mass entering the cylinders and producing a richer, less powerful mixture\n[C] The throttle valve closes partially\n[D] The exhaust valve sticks open",
         "CORRECT: [B]. Hot air ducted from the exhaust shroud has lower density, which reduces the mass of air entering the engine, slightly richening the mixture and causing an immediate small drop in power/RPM.")
    ]

    for q_text, opts, exp in questions_ch18:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 18 compiled: {pdf_path}")


def build_agk_ch19():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch19_propellers_governors.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 19: Propellers & Governors")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        19,
        "Propellers & Constant Speed Governors",
        "93-138 (Pwr)"
    )

    pdf.add_heading_1("1. Propeller Aerodynamics: Blade Angle vs Angle of Attack")
    pdf.add_paragraph(
        "A propeller blade is a rotating airfoil that converts engine shaft torque into forward aerodynamic thrust:"
    )
    pdf.add_bullet("Blade Element Theory", "The blade is twisted from root to tip. Because rotational speed (omega x r) increases towards the tip while forward airspeed is constant, the blade angle must decrease progressively toward the tip to maintain an optimal aerodynamic Angle of Attack (Alpha) along the entire blade length.")
    pdf.add_bullet("Blade Angle (Pitch)", "The acute angle between the blade chord line and the propeller plane of rotation.")
    pdf.add_bullet("Angle of Attack (Alpha)", "The angle between the blade chord line and the RELATIVE AIRFLOW (which is the vector sum of rotational velocity and forward airspeed).")
    pdf.add_bullet("Propeller Slip", "Geometric Pitch (theoretical distance advanced in one revolution with zero slip) minus Effective Pitch (actual distance advanced in flight). Slip = Geometric Pitch - Effective Pitch.")

    pdf.add_heading_1("2. Constant Speed Unit (CSU / Governor) Operation")
    pdf.add_paragraph(
        "A Constant Speed Propeller maintains an exact, selected engine RPM automatically regardless of aircraft airspeed or throttle position, "
        "modulating blade pitch hydraulically via an engine-driven governor (CSU):"
    )

    gov_table = [
        ["ON-SPEED", "Centrifugal force on rotating flyweights EXACTLY BALANCES speeder spring tension.", "Pilot valve lands cover oil metering ports; oil trapped in propeller cylinder; blade pitch remains constant."],
        ["OVER-SPEED (Dive / Throttle Advance)", "Rotational RPM increases -> flyweights tilt OUTWARDS against spring, lifting pilot valve.", "Meters high-pressure engine oil to/from propeller hub to COARSE (increase) blade pitch. Increased aerodynamic load slows engine back down to selected RPM!"],
        ["UNDER-SPEED (Climb / Throttle Retard)", "Rotational RPM drops -> speeder spring overcomes flyweights and pushes pilot valve DOWN.", "Changes oil flow to FINE (decrease) blade pitch. Reduced aerodynamic drag allows engine to accelerate back to selected RPM!"]
    ]
    pdf.add_table(["Flight Condition", "Governor Flyweights & Valve State", "Propeller Blade Pitch Response"], gov_table, col_widths=[110.0, 190.0, 200.0])

    pdf.add_heading_1("3. Feathering Systems & Windmilling Drag")
    pdf.add_paragraph(
        "If a multi-engine aircraft suffers an engine failure in flight, a windmilling propeller creates massive parasite drag and severe yaw:"
    )
    pdf.add_bullet("Feathering (Blade Angle ~85° to 90°)", "Blades are aligned parallel to the relative airflow, stopping propeller rotation and minimizing aerodynamic drag to the lowest possible value.")
    pdf.add_bullet("Feathering Mechanism", "Multi-engine propellers use heavy counterweights and internal feathering springs to drive blades into feather. Oil pressure opposes the springs to move blades toward fine pitch. Therefore, if engine oil pressure is lost, the propeller FEATHERS AUTOMATICALLY for safety!")
    pdf.add_bullet("Centrifugal Latch Pins", "Prevent the propeller from feathering when the engine is shut down on the ground below ~800-1,000 RPM. (If blades feathered on the ground, starting loads on the electric starter motor would be dangerously excessive).")
    pdf.add_bullet("Unfeathering Accumulator", "Stores high-pressure oil during normal flight. When the pilot moves the propeller lever out of feather in flight, an unfeathering solenoid releases accumulator oil back to the prop cylinder, driving blades back to fine pitch to windmill and air-start the engine.")

    pdf.add_callout(
        "trap",
        "Single-Engine vs Multi-Engine Propeller Pitch Failure Modes",
        "- Single-Engine Propeller: Engineered to fail toward FINE PITCH (low pitch) upon oil loss, ensuring maximum power remains available for safe landing!\n"
        "- Multi-Engine Propeller: Engineered to fail toward FEATHER (high pitch) upon oil loss (driven by counterweights and springs), preventing catastrophic windmilling drag and uncontrollable asymmetric yaw!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch19 = [
        ("Q1: In a multi-engine aircraft equipped with constant speed propellers, what happens to blade pitch if engine oil pressure to the propeller hub is completely lost?",
         "[A] The propeller drives to full reverse pitch\n[B] The propeller drives automatically to the FEATHERED position under the action of mechanical counterweights and feathering springs\n[C] The propeller remains locked in fine pitch\n[D] The propeller falls off",
         "CORRECT: [B]. Multi-engine propellers use oil pressure to maintain fine pitch. If oil pressure drops to zero, internal springs and counterweights drive the blades to full feather (~90°) to prevent high windmilling drag."),
        ("Q2: In a constant speed propeller governor (CSU), what directly balances the centrifugal force generated by the rotating governor flyweights?",
         "[A] Propeller blade torque\n[B] The tension of the pilot-controlled speeder spring\n[C] Atmospheric ambient air pressure\n[D] High-pressure nitrogen",
         "CORRECT: [B]. The speeder spring tension (controlled by the cockpit blue propeller lever) pushes down on the flyweights. Flyweights spin with engine RPM and tilt outward with centrifugal force, balancing at 'on-speed'."),
        ("Q3: Why are propeller blades manufactured with an aerodynamic twist from root to tip?",
         "[A] To make the blades stronger near the tip\n[B] To maintain a relatively constant aerodynamic Angle of Attack along the entire length of the blade as rotational velocity increases toward the tip\n[C] To reduce manufacturing cost\n[D] To improve ground clearance",
         "CORRECT: [B]. Linear rotational speed is lowest at the hub and fastest at the blade tip. To prevent tip stall and maintain uniform lift distribution, blade angle is twisted (highest at root, lowest at tip).")
    ]

    for q_text, opts, exp in questions_ch19:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 19 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_agk_ch17()
    build_agk_ch18()
    build_agk_ch19()
