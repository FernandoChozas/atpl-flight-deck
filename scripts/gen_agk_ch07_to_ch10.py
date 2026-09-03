#!/usr/bin/env python3
"""
Generator for Subject 021: AGK - Airframe, Systems, Electrics & Powerplant
Volume 2: Chapters 07 to 10
- Chapter 07: Ice and Rain Protection (Thermal, Pneumatic & Electrical)
- Chapter 08: Aircraft Oxygen Equipment (Crew Demand & Passenger Chemical)
- Chapter 09: Smoke & Fire Detection and Protection Systems
- Chapter 10: Aircraft Fuel Systems (Tanks, Pumps, Crossfeed & Jettison)

Fully aligned with CAE Oxford Book 2 (Airframes and Systems) and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant"

def build_agk_ch07():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch07_ice_rain_protection.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 7: Ice & Rain Protection")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        7,
        "Ice and Rain Protection Systems",
        "235-258"
    )

    pdf.add_heading_1("1. Anti-Icing vs De-Icing Philosophies")
    pdf.add_paragraph(
        "Ice accumulation on aerodynamic surfaces reduces maximum lift by up to 30%, increases parasite drag by over 100%, and increases "
        "stall speed significantly. Commercial aircraft utilize two distinct operational methods:"
    )
    pdf.add_bullet("Anti-Icing (Preventative)", "Operates CONTINUOUSLY before entering suspected icing conditions (OAT <= +10°C in visible moisture) to PREVENT any ice formation from ever adhering to protected surfaces.")
    pdf.add_bullet("De-Icing (Remedial)", "Operates INTERMITTENTLY to break off and shed ice layers AFTER a predetermined thickness (e.g. 6 to 12 mm / 1/4 to 1/2 inch) has accumulated.")

    systems_table = [
        ["Thermal Anti-Ice", "Hot engine bleed air (~200°C) piped through Piccolo tubes inside leading edge.", "Slats and wing leading edges; engine nacelle intake cowlings. Engine anti-ice uses raw bleed air directly and operates independently of wing anti-ice."],
        ["Pneumatic De-Ice Boots", "Inflatable neoprene rubber boots bonded to leading edges. Inflated cyclically by bleed air / vacuum pump.", "Wings and tail empennage on turboprop and commuter aircraft. Must allow ice to build up before inflating; premature cycling can cause 'ice bridging' (ice forms a rigid shell around inflated boot)."],
        ["Electrical Heating", "Embedded resistive heating elements (AC or DC powered).", "Pitot probes, static ports, TAT sensors, AOA vanes, propeller blade boots, flight deck windshields, and waste water drain masts."],
        ["Fluid (Weeping Wing)", "Ethylene glycol fluid pumped through microscopic laser-drilled pores in titanium panels (TKS system).", "General aviation and light turboprops. Provides both anti-icing and de-icing; limited by fluid reservoir quantity."]
    ]
    pdf.add_table(["System Type", "Operating Medium & Mechanism", "Aircraft Protected Areas & Operational Limits"], systems_table, col_widths=[110.0, 190.0, 200.0])

    pdf.add_callout(
        "trap",
        "Engine Anti-Ice vs Wing Anti-Ice Selection Rules",
        "- Engine Anti-Ice: MUST BE SELECTED ON whenever OAT (on ground) or TAT (in flight) is +10°C OR BELOW in visible moisture (clouds, fog with visibility < 1,000 m, rain, snow, slush)!\n"
        "- Wing Anti-Ice: Selected on in flight when ice accumulation is observed, or continuously in severe icing. Usually inhibited automatically on the ground via squat switch (except for brief functional test) to prevent overheating leading-edge slats!",
        max_chars=86
    )

    pdf.add_heading_1("2. Windscreen Heating & Rain Removal")
    pdf.add_paragraph(
        "Transport aircraft flight deck windshields are multi-laminated glass-vinyl sandwiches with two critical operational requirements:"
    )
    pdf.add_bullet("Electrical Demisting / De-icing", "A transparent conductive metallic coating (e.g. gold film or Stannic oxide) laminated inside the glass is heated with AC power. Thermistors embedded in the vinyl modulate power to maintain ~35°C to 45°C. This prevents icing and demists the inner pane.")
    pdf.add_bullet("Bird-Strike Impact Resistance", "At cruising temperatures (-50°C), vinyl interlayers become brittle. Electrical heating softens the vinyl interlayer, making it pliable and ductile, allowing it to absorb a 4-lb bird impact at V_c without cockpit penetration!")
    pdf.add_bullet("Rain Removal Systems", "1. Mechanical windshield wipers (limited to V_max_wiper, ~250 kt); 2. Rain repellent liquid sprayed onto glass (banned in dry conditions: smears into opaque grease); 3. Hydrophobic chemical surface coating that makes water bead off aerodynamically.")

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: Why must flight deck windshield electrical heating remain powered during normal cruise at high altitudes even when no icing conditions are present?",
         "[A] To prevent cockpit glass fogging only\n[B] To warm the vinyl interlayer, maintaining elasticity and shatterproof impact resistance against bird-strikes at freezing temperatures\n[C] To supply emergency AC power\n[D] To improve cockpit night vision",
         "CORRECT: [B]. At -50°C in cruise, cold vinyl is brittle. Windscreen heating keeps the vinyl core pliable and elastic, which is mandatory to certify bird-strike impact resistance under CS-25."),
        ("Q2: What operational hazard is associated with operating pneumatic de-ice boots prematurely before sufficient ice has accumulated?",
         "[A] The rubber boot will blow off the wing\n[B] Ice bridging: ice can freeze over the inflated boot shape, forming a hollow shell that subsequent boot cycles cannot break\n[C] Engine bleed air pressure drops to zero\n[D] The boots will overheat",
         "CORRECT: [B]. If inflated when only a thin slushy film exists, water can freeze over the extended contour, creating an 'ice bridge'. Subsequent inflations occur inside the cavity without shedding the outer ice shell."),
        ("Q3: When must engine cowl thermal anti-icing be turned ON in flight?",
         "[A] Only when ice chunks are visibly flying into the engine\n[B] Whenever Total Air Temperature (TAT) is +10°C or below and visible moisture (clouds, rain, snow) is present\n[C] At all times above FL 250\n[D] Only during descent",
         "CORRECT: [B]. Under EASA standards, engine anti-ice must be on whenever TAT is +10°C or colder in any visible moisture, preventing ice buildup on cowl lips that could shed into engine fan blades.")
    ]

    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 7 compiled: {pdf_path}")


def build_agk_ch08():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch08_oxygen_equipment.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 8: Aircraft Oxygen Equipment")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        8,
        "Aircraft Oxygen Equipment (Crew & Passenger)",
        "259-280"
    )

    pdf.add_heading_1("1. Flight Crew vs Passenger Oxygen Requirements")
    pdf.add_paragraph(
        "Aviation oxygen systems are divided into two completely segregated architectures due to differing physiological and emergency demands:"
    )

    oxy_table = [
        ["Supply Source", "High-pressure gaseous oxygen cylinder (1,800 to 2,000 psi) painted green.", "Chemical oxygen generators (sodium chlorate candles) mounted in PSUs; or central gaseous cylinder in some widebodies."],
        ["Delivery Mode", "Diluter-Demand (normal) or 100% Continuous Pressure-Demand (smoke/fire or cabin alt > 39,000 ft).", "Continuous flow into a rebreather bag mask."],
        ["Deployment", "Manual donning. Quick-donning masks stowed beside pilot seats; must be don-able in LESS THAN 5 SECONDS with one hand!", "Automatic drop-down when cabin pressure altitude exceeds 14,000 ft; can also be deployed manually from cockpit switch."],
        ["Duration", "Sized for entire emergency descent down to 10,000 ft plus prolonged cruise at 10,000 ft (typically > 2 hours).", "12 to 15 minutes minimum duration (sufficient for emergency descent from FL 410 down to safe breathing altitude < 10,000 ft)."],
        ["Smoke Protection", "Provides positive overpressure inside mask to prevent toxic cockpit smoke/fumes from entering. Built-in smoke goggles.", "NOT suitable for smoke/toxic fumes (ambient air enters dilution holes)."]
    ]
    pdf.add_table(["System Feature", "Flight Crew Oxygen System", "Passenger Emergency Oxygen System"], oxy_table, col_widths=[90.0, 205.0, 205.0])

    pdf.add_callout(
        "trap",
        "Chemical Oxygen Generators (Sodium Chlorate Candles) Hazards",
        "- Chemical Reaction: Sodium Chlorate (NaClO3) + Iron (Fe) -> Sodium Chloride (salt) + Oxygen (O2) + Heat!\n"
        "- The reaction is EXOTHERMIC. Generator core temperatures reach 230°C to 260°C (450°F)!\n"
        "- Activation: Pulling the mask lanyard releases a spring-loaded firing pin that strikes a percussion cap.\n"
        "- CRITICAL: Once initiated, a chemical oxygen generator CANNOT BE SHUT OFF OR EXTINGUISHED until fully consumed (12-15 min)!",
        max_chars=86
    )

    pdf.add_heading_1("2. Flight Crew Mask Modes: Normal vs 100% vs Emergency")
    pdf.add_paragraph(
        "The flight crew oxygen regulator provides three selectable switch positions:"
    )
    pdf.add_bullet("NORMAL (Diluter Demand)", "Supplies a variable mix of ambient cabin air and pure oxygen. The regulator automatically increases oxygen concentration as cabin altitude increases, reaching 100% oxygen at approximately 32,000 ft cabin altitude.")
    pdf.add_bullet("100% OXYGEN", "Supplies 100% pure oxygen on inhalation demand, bypassing all ambient cabin air. Selected immediately in rapid decompression or contamination.")
    pdf.add_bullet("EMERGENCY (Pressure Demand)", "Supplies 100% pure oxygen under continuous POSITIVE PRESSURE into the mask. Forces oxygen into the pilot's lungs and forces any smoke or toxic fumes out around mask edges. Mandatory when flying through dense cockpit smoke or above 39,000 ft cabin altitude.")

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: Once initiated by pulling the mask lanyard, can a passenger chemical oxygen generator be turned off by the flight crew?",
         "[A] Yes, by turning off the passenger oxygen switch in the cockpit\n[B] No, the chemical reaction is exothermic and self-sustaining; it cannot be stopped until all chemical fuel is exhausted (12-15 minutes)\n[C] Yes, by closing the overhead PSU door\n[D] Yes, by dumping cabin pressure",
         "CORRECT: [B]. Chemical oxygen generators use an exothermic chemical burning process (sodium chlorate and iron). Once the firing pin is released, the reaction produces oxygen and intense heat (~250°C) continuously until depleted."),
        ("Q2: Under EASA CS-25 certification requirements, a flight crew quick-donning oxygen mask must be capable of being placed on the face with one hand within how many seconds?",
         "[A] 3 seconds\n[B] 5 seconds\n[C] 10 seconds\n[D] 15 seconds",
         "CORRECT: [B]. Regulations mandate that a pilot must be able to don and latch a quick-donning oxygen mask using only one hand within 5 seconds, while continuing to fly and communicate."),
        ("Q3: What is the primary purpose of the 'EMERGENCY' setting on a flight crew oxygen regulator?",
         "[A] To save oxygen supply during long descents\n[B] To provide 100% oxygen under continuous positive pressure, preventing toxic fumes and smoke from entering the mask\n[C] To inflate the passenger cabin\n[D] To heat the oxygen gas",
         "CORRECT: [B]. The Emergency mode delivers continuous positive pressure, which prevents toxic smoke, carbon monoxide, or irritant gases from seeping past the mask facial seal into the pilot's respiratory tract.")
    ]

    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 8 compiled: {pdf_path}")


def build_agk_ch09():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch09_smoke_fire_protection.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 9: Smoke & Fire Protection")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        9,
        "Smoke & Fire Detection and Protection Systems",
        "281-308"
    )

    pdf.add_heading_1("1. Fire Classifications & Extinguishing Agents")
    pdf.add_paragraph(
        "Aircraft fires present an immediate mortal threat in flight. Extinguishing agents must extinguish fire rapidly without "
        "generating toxic byproducts or causing electrical short circuits:"
    )

    fire_classes = [
        ["Class A", "Solid combustibles (wood, paper, fabrics, upholstery).", "Water with antifreeze, or Halon followed by water dousing to quench deep embers."],
        ["Class B", "Flammable liquids (aviation kerosene, hydraulic oil, lubricating grease).", "Halon 1211 (BCF) or Halon 1301. Smothers flame; NEVER USE WATER (causes explosive liquid spread)!"],
        ["Class C", "Energized electrical equipment (avionics, circuit breaker panels).", "Halon 1211 / 1301 or CO2. Non-conductive agent mandatory to prevent pilot electrocution and equipment corrosion."],
        ["Class D", "Combustible metals (magnesium wheels, titanium engine components).", "Dry powder extinguishing agents (sand, copper powder). Very difficult to extinguish; water reacts violently!"]
    ]
    pdf.add_table(["Fire Class", "Combustible Material Type", "Authorized Aeronautical Extinguishing Agent"], fire_classes, col_widths=[90.0, 200.0, 210.0])

    pdf.add_heading_1("2. Fire Detection Systems: Continuous Thermal Loops")
    pdf.add_paragraph(
        "Engine nacelles and APU compartments use continuous loop thermal detectors routed around high-risk zones:"
    )
    pdf.add_bullet("Fenwal System (Resistance)", "A continuous Inconel tube packed with a ceramic thermistor core surrounding a central nickel conductor wire. As temperature rises anywhere along the loop, electrical resistance of the ceramic drops exponentially, allowing current to flow and triggering the fire alarm.")
    pdf.add_bullet("Kidde System (Dual Element)", "Two wire conductors embedded in a thermistor material inside an Inconel tube, measuring resistance and capacitance changes.")
    pdf.add_bullet("Systron-Donner (Pneumatic Pressure)", "Stainless steel tube sealed with a helium gas charge and a central core saturated with titanium hydride (releasing hydrogen at high temperatures). Average overheat expands the helium gas (closing a low-pressure switch); localized fire releases hydrogen gas (closing a high-pressure fire switch). If the tube is severed, helium leaks out, triggering a FAULT/INTEGRITY warning!")
    pdf.add_bullet("Dual-Loop Logic (AND vs OR)", "Engines feature two independent loops (Loop A and Loop B). Normal logic is 'A AND B' (both loops must sense fire to trigger cockpit alarm, eliminating false warnings). If one loop fails, logic switches automatically to single loop ('A OR B').")

    pdf.add_callout(
        "trap",
        "Engine Fire Drill Sequence (The Fire Handle Pull)",
        "Pulling an Engine Fire Shutoff Handle accomplishes five vital isolation actions mechanically and electrically:\n"
        "1. Shuts the engine fuel low-pressure (LP) firewall shutoff valve;\n"
        "2. Shuts the engine hydraulic supply firewall shutoff valve;\n"
        "3. Closes the engine pneumatic bleed air valve;\n"
        "4. De-excites the engine AC generator (trips generator breaker and field breaker);\n"
        "5. ARMS the fire extinguisher bottle discharge squibs (cartridges)!",
        max_chars=86
    )

    pdf.add_heading_1("3. Smoke Detection & Cargo Compartment Classifications")
    pdf.add_paragraph(
        "Cargo compartments under CS-25 / FAR-25 are classified according to accessibility and fire suppression capabilities:"
    )
    cargo_table = [
        ["Class A", "Readily accessible to crew in flight (e.g. cockpit coat closet).", "Fire easily discovered; hand fire extinguisher sufficient."],
        ["Class B", "Accessible to crew in flight with sufficient access to reach any part.", "Equipped with smoke/fire detection and separate hand fire extinguishing access."],
        ["Class C", "INACCESSIBLE lower cargo holds on passenger airliners (standard baggage hold).", "MANDATORY: 1. Separate smoke/fire detector system; 2. Built-in built-in Halon extinguishing system controlled from cockpit; 3. Means to control ventilation to starve fire of oxygen."],
        ["Class D", "Obsolete class (unventilated, relied on oxygen starvation). Banned following ValuJet 592 crash!", "All former Class D holds have been retrofitted to Class C standards with active fire extinguishing."],
        ["Class E", "Main deck cargo cabins on ALL-CARGO freighter aircraft.", "Equipped with smoke detection; crew shuts down ventilation and depressurizes cargo cabin in flight to starve fire."]
    ]
    pdf.add_table(["Class", "Accessibility & Suppression", "Aviation Regulations & Examples"], cargo_table, col_widths=[75.0, 215.0, 210.0])

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch09 = [
        ("Q1: What does pulling an engine fire shutoff handle in the cockpit accomplish?",
         "[A] Discharges both fire bottles immediately into the engine core\n[B] Shuts off fuel, hydraulics, bleed air, trips the generator, and arms the fire bottle squibs\n[C] Feather the opposite engine\n[D] Extends the landing gear",
         "CORRECT: [B]. The fire handle isolates all fluid and electrical supplies to the engine (fuel, hydraulics, pneumatic bleed, generator) and arms the explosive squibs. Rotating the handle then discharges the extinguisher bottle."),
        ("Q2: In a dual-loop engine fire detection system (Loop A and Loop B), what is the normal alarm logic to prevent false alarms?",
         "[A] Loop A must detect fire, while Loop B must detect smoke\n[B] Both Loop A AND Loop B must detect the fire condition simultaneously\n[C] Either Loop A OR Loop B is sufficient\n[D] Loop A tests Loop B every 30 seconds",
         "CORRECT: [B]. Dual-loop systems require 'AND' logic to trigger master warning bells and lights. If both loops agree, a fire is confirmed. If only one triggers, a loop fault is annunciated unless manual override is selected."),
        ("Q3: Which cargo compartment class applies to the inaccessible lower underfloor baggage holds of modern passenger transport aircraft?",
         "[A] Class A\n[B] Class B\n[C] Class C\n[D] Class E",
         "CORRECT: [C]. Class C cargo holds are inaccessible in flight and must have smoke/fire detection, built-in cockpit-controlled extinguishing systems (Halon flooding and metering bottles), and ventilation shutoff controls.")
    ]

    for q_text, opts, exp in questions_ch09:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 9 compiled: {pdf_path}")


def build_agk_ch10():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch10_fuel_systems.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 10: Aircraft Fuel Systems")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        10,
        "Aircraft Fuel Systems (Tanks, Pumps & Jettison)",
        "309-338"
    )

    pdf.add_heading_1("1. Aviation Turbine Fuels: Jet A-1 vs Jet A vs Jet B")
    pdf.add_paragraph(
        "Jet engines burn kerosene-type aviation fuels possessing high energy density, low freezing points, and clean combustion characteristics:"
    )

    fuel_table = [
        ["Jet A-1", "Civil standard kerosene used worldwide (except domestic USA).", "Freezing Point: -47°C maximum.\nFlash Point: +38°C (100°F) minimum.\nNominal Density: 0.80 kg/litre (6.7 lb/US Gal)."],
        ["Jet A", "Civil kerosene used primarily in the domestic United States.", "Freezing Point: -40°C maximum (7°C higher than Jet A-1!).\nFlash Point: +38°C minimum.\nDensity: 0.80 kg/litre."],
        ["Jet B (Wide-Cut)", "Blend of gasoline and kerosene (military equivalent JP-4).", "Freezing Point: -60°C maximum.\nFlash Point: VERY LOW (-20°C). Highly volatile and hazardous; used only in extreme Arctic/polar operations."]
    ]
    pdf.add_table(["Fuel Designation", "Chemical Base & Composition", "Freezing Point & Flash Point Specification"], fuel_table, col_widths=[110.0, 190.0, 200.0])

    pdf.add_callout(
        "trap",
        "Fuel Temperature & Freezing Monitoring in Long-Range Cruise",
        "- Minimum Fuel Temperature Limit: Fuel temperature in flight must not be allowed to drop closer than 3°C above the fuel freezing point (e.g. For Jet A-1 with freezing point -47°C, minimum allowable fuel temp is -44°C)!\n"
        "- Corrective Actions for Cold Fuel: 1. Accelerate to higher Mach number (increases kinetic Ram rise heating: TAT = SAT x (1 + 0.2 M^2)); 2. Descend to a lower, warmer altitude.",
        max_chars=86
    )

    pdf.add_heading_1("2. Tank Architecture, Boost Pumps & Crossfeed")
    pdf.add_paragraph(
        "Commercial airliners store fuel primarily in the wings (wet wing integral tanks) and center fuselage tank:"
    )
    pdf.add_bullet("Integral Tanks (Wet Wing)", "The wing structure itself (spars, skin, ribs) forms the fuel tank, sealed with polysulfide sealant. Saves massive weight compared to separate fuel cells.")
    pdf.add_bullet("Wing Bending Relief", "Fuel in the wings counteracts upward aerodynamic wing bending moments during flight, reducing stress on the wing root! For this reason, fuel from the CENTER TANK is always burned FIRST, keeping wing fuel loaded until later in the flight.")
    pdf.add_bullet("Submerged Fuel Boost Pumps", "Each tank contains AC motor-driven submerged centrifugal pumps. Center tank pumps have higher output pressure (override/jettison pumps) than wing pumps, ensuring center tank fuel feeds engines preferentially.")
    pdf.add_bullet("Crossfeed Valve", "Allows any fuel tank to feed any engine, permitting lateral fuel balance corrections in flight, or allowing remaining engines to feed from all tanks during engine-out operations.")
    pdf.add_bullet("Fuel Jettison (Dumping)", "Mandatory on aircraft whose Maximum Take-Off Mass (MTOM) significantly exceeds Maximum Landing Mass (MLM). Must be capable of dumping fuel rapidly down to maximum landing mass within 15 minutes, while maintaining sufficient fuel reserve to fly to an alternate.")

    pdf.add_heading_1("3. Aircraft Refueling Safety & Nitrogen Inerting (OBIGGS)")
    pdf.add_paragraph(
        "Ground refueling presents extreme fire and static discharge hazards:"
    )
    pdf.add_bullet("Electrical Bonding", "Before fuel hose connection, a grounding/bonding wire must be attached between the fuel truck and aircraft to equalize electrostatic potential and prevent sparks.")
    pdf.add_bullet("Nitrogen Inerting (OBIGGS)", "On-Board Inert Gas Generating Systems separate nitrogen from bleed air and pump nitrogen-enriched air (NEA, oxygen < 9%) into fuel tank vapor ullage spaces, eliminating flammable oxygen mixtures (preventing TWA 800 center tank explosion scenario).")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch10 = [
        ("Q1: Why is center tank fuel burned before wing tank fuel during normal flight in transport aircraft?",
         "[A] Because center tank fuel freezes faster\n[B] To preserve fuel mass in the wings as long as possible, providing upward wing-bending relief against aerodynamic lift forces\n[C] Because center tank fuel cannot be jettisoned\n[D] To keep the center of gravity as far aft as possible",
         "CORRECT: [B]. The weight of fuel stored inside the wings opposes upward aerodynamic lift, reducing bending moments at the wing root. Consuming center tank fuel first preserves this structural wing-bending relief."),
        ("Q2: What is the specified maximum freezing point of standard international Jet A-1 fuel?",
         "[A] -40°C\n[B] -47°C\n[C] -50°C\n[D] -60°C",
         "CORRECT: [B]. Jet A-1 has a mandatory maximum freezing point of -47°C. (Jet A, used in the US, has a freezing point of -40°C)."),
        ("Q3: In a long-range jet flying in polar airspace, fuel temperature indicates -43°C while burning Jet A-1 (freezing point -47°C). What action must the flight crew take?",
         "[A] Jettison the cold fuel immediately\n[B] Descend to a warmer altitude or increase Mach number to increase aerodynamic kinetic heating\n[C] Turn off the fuel boost pumps\n[D] Shut down one engine to heat the wing",
         "CORRECT: [B]. Fuel temp must remain at least 3°C above freezing point (minimum -44°C for Jet A-1). At -43°C, fuel is dangerously close to waxing. Pilots must accelerate (higher Mach = higher TAT ram rise) or descend into warmer air.")
    ]

    for q_text, opts, exp in questions_ch10:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 10 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_agk_ch07()
    build_agk_ch08()
    build_agk_ch09()
    build_agk_ch10()
