#!/usr/bin/env python3
"""
Generator for Subject 070: Operational Procedures
Volume 2: Chapters 6 to 10
- Chapter 6: Special Approvals: RVSM, NAT HLA & PBCS Contingency Procedures
- Chapter 7: In-Flight Emergencies: Emergency Descent, Evacuation & Ditching
- Chapter 8: All-Weather Flight Hazards: Windshear, Ash Cloud & Wake Turbulence
- Chapter 9: Ground De-Icing & Anti-Icing Operations (Holdover Times - HOT)
- Chapter 10: Carriage of Dangerous Goods by Air (ICAO Annex 18 & IATA DGR)

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Operational Procedures and EASA AIR-OPS (Regulation EU 965/2012).
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/070_operational_procedures"

def build_ops_ch06():
    pdf_path = os.path.join(OUTPUT_DIR, "070_ch06_rvsm_nat_hla_contingency.pdf")
    pdf = PDFBuilder("Operational Procedures", "070", "Chapter 6: RVSM & NAT HLA")

    pdf.add_title_banner(
        "Operational Procedures",
        6,
        "Special Approvals: RVSM, NAT HLA & Contingencies",
        "197-234"
    )

    pdf.add_heading_1("1. Reduced Vertical Separation Minimum (RVSM)")
    pdf.add_paragraph(
        "RVSM reduces vertical separation between aircraft from 2,000 ft to 1,000 ft between FL 290 and FL 410 inclusive, doubling airspace capacity:"
    )
    pdf.add_bullet("Mandatory RVSM Equipment (Part-SPA.RVSM)", "1. Two independent primary altimetry systems (maximum difference +-200 ft in flight); 2. One automatic altitude-control system (autopilot holding altitude within +-65 ft); 3. One altitude-alerting system (+-300 ft alert threshold); 4. One Mode C / Mode S altitude-reporting transponder.")
    pdf.add_bullet("Strategic Lateral Offset Procedures (SLOP)", "In oceanic airspace (NAT HLA), pilots are authorized to fly 1 NM or 2 NM RIGHT OF TRACK to disperse wake turbulence and reduce collision risk without notifying ATC!")

    pdf.add_heading_1("2. Oceanic In-Flight Contingency Procedure (NAT HLA)")
    pdf.add_paragraph(
        "If unable to maintain assigned flight level or route in NAT HLA due to engine failure, depressurization, or medical emergency:"
    )
    pdf.add_bullet("Step 1: Turn", "Turn 30° left or right of track (away from nearest route/traffic).")
    pdf.add_bullet("Step 2: Offset", "Fly to acquire and maintain a 5 NAUTICAL MILE lateral offset from the track centerline.")
    pdf.add_bullet("Step 3: Level Change", "Once established on the 5 NM offset, climb or descend: By 500 FT (if below FL 410); By 1,000 FT (if at or above FL 410) to avoid standard traffic levels!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Executing Oceanic Engine-Out Contingency",
        "SCENARIO (Transatlantic Emergency Descent Drill):\n"
        "A twin-jet airliner is cruising at FL 370 in the North Atlantic (NAT HLA) on Track Charlie (Track 090° True):\n"
        "- An engine fails catastrophically!\n"
        "- Unable to maintain FL 370, the crew cannot establish radio communication with Shanwick ATC immediately\n"
        "QUESTION: What precise maneuver must the crew execute under ICAO NAT Doc 007 contingency rules?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Initial Action:\n"
        "  - Select Maximum Continuous Thrust on good engine, set transponder to 7700, turn on all exterior lights!\n\n"
        "Step 2: Initiate Lateral Turn:\n"
        "  - Turn 30° to the RIGHT (heading 120°) or LEFT (heading 060°) away from conflicting tracks.\n\n"
        "Step 3: Establish 5 NM Lateral Offset:\n"
        "  - Fly out until 5.0 NM away from the centerline of Track Charlie.\n"
        "  - Turn back onto track heading (090° True) to parallel the track 5 NM displaced.\n\n"
        "Step 4: Select Contingency Level (Divert from FL 370):\n"
        "  - Normal traffic flies at whole flight levels: FL 370, FL 360, FL 350, FL 340.\n"
        "  - To avoid hitting opposing or same-direction traffic below:\n"
        "  - Aircraft must descend to an INTERMEDIATE 500 FT LEVEL!\n"
        "  - Drift down to: FL 335, FL 315, or FL 295 (500 ft offset from normal traffic levels)!\n\n"
        "FINAL ANSWER: Turn 30° to establish 5 NM offset, then descend to a 500-ft offset flight level (e.g. FL 335 / FL 315).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The 500 ft vs 1,000 ft Contingency Offset Trap",
        "- If below FL 410: The altitude offset is 500 FT (e.g. FL 335).\n"
        "- If at or above FL 410: The altitude offset is 1,000 FT.\n"
        "- The lateral offset is ALWAYS 5 NM in modern ICAO oceanic airspace (changed from the old 15 NM rule).",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: In RVSM airspace (FL 290 to FL 410), what is the maximum permissible difference between the two primary pilot altimeters in flight?",
         "[A] 50 ft\n[B] NOT EXCEEDING 200 FEET\n[C] 300 ft\n[D] 500 ft",
         "CORRECT: [B]. Under EASA SPA.RVSM.110, the maximum difference between primary altimeters in level flight is 200 ft (and within 75 ft on the ground)."),
        ("Q2: Under Strategic Lateral Offset Procedures (SLOP) in oceanic airspace, what lateral offsets are authorized to the RIGHT of track without ATC clearance?",
         "[A] 10 NM right\n[B] 1 NM or 2 NM RIGHT OF TRACK (or tenths of a mile up to 2 NM)\n[C] 5 NM left\n[D] 1 NM left",
         "CORRECT: [B]. SLOP allows pilots to offset 1 or 2 NM right of centerline to disperse wake turbulence and minimize collision risk."),
        ("Q3: What is the lateral offset distance required when executing an oceanic in-flight contingency in the North Atlantic (NAT HLA)?",
         "[A] 15 NM\n[B] Exactly 5 NAUTICAL MILES\n[C] 30 NM\n[D] 1 NM",
         "CORRECT: [B]. Under modern ICAO Doc 007 procedures, the oceanic contingency offset is standardized at 5 NM.")
    ]

    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Operational Procedures Chapter 6 compiled: {pdf_path}")


def build_ops_ch07():
    pdf_path = os.path.join(OUTPUT_DIR, "070_ch07_inflight_emergencies_descent_evac.pdf")
    pdf = PDFBuilder("Operational Procedures", "070", "Chapter 7: Emergencies & Evacuation")

    pdf.add_title_banner(
        "Operational Procedures",
        7,
        "In-Flight Emergencies: Descent, Evacuation & Ditching",
        "235-272"
    )

    pdf.add_heading_1("1. Emergency Descent (Rapid Depressurization)")
    pdf.add_paragraph(
        "A sudden cabin decompression at high altitude (e.g. FL 390) demands immediate flight crew action before Time of Useful Consciousness (TUC < 30 seconds) expires:"
    )
    pdf.add_bullet("Immediate Memory Items", "1. DON OXYGEN MASKS 100% / Emergency; 2. Establish crew communications; 3. Disengage autothrottle and retard thrust levers to IDLE; 4. EXTEND SPEED BRAKES fully; 5. Pitch down into emergency descent at Vmo / Mmo; 6. Set transponder 7700.")
    pdf.add_bullet("Target Level", "Descend rapidly to 10,000 ft MSL (or FL 100), where oxygen is breathable without supplemental supply, or to the Minimum Sector Altitude (MSA) if flying over mountainous terrain!")

    pdf.add_heading_1("2. Emergency Evacuation Standards")
    pdf.add_paragraph(
        "Under CS-25 certification, an airliner must demonstrate complete evacuation of maximum passenger capacity within 90 SECONDS with 50% OF EXITS BLOCKED, using emergency floor lighting and inflatable escape slides."
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: In the event of a rapid decompression at FL 370, what is the VERY FIRST memory action the pilot flying must execute?",
         "[A] Declare a Mayday to ATC\n[B] DON OXYGEN MASK (100% / Emergency) and establish crew communications\n[C] Extend speed brakes\n[D] Retard thrust levers",
         "CORRECT: [B]. At FL 370, Time of Useful Consciousness is less than 30 seconds. Immediate donning of positive-pressure oxygen masks is paramount to prevent pilot incapacitation."),
        ("Q2: Under CS-25 airworthiness regulations, within what maximum time must an airliner demonstrate full passenger evacuation in a certification test?",
         "[A] 60 seconds\n[B] 90 SECONDS with 50% of available emergency exits blocked\n[C] 120 seconds\n[D] 3 minutes",
         "CORRECT: [B]. Evacuation demonstration requires all passengers and crew to evacuate in dark conditions within 90 seconds using only half the exits."),
        ("Q3: When ditching an aircraft into open ocean waters with significant swell, in what direction relative to the sea swell should the aircraft touch down?",
         "[A] Directly into the face of the highest swell\n[B] PARALLEL TO THE SWELL CRESTS (along the swell), touching down along the top of a swell or along the back of a swell\n[C] Downwind\n[D] Perpendicular to waves",
         "CORRECT: [B]. Landing parallel to the swell prevents the aircraft burying its nose into the oncoming wall of water, minimizing deceleration forces.")
    ]

    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Operational Procedures Chapter 7 compiled: {pdf_path}")


def build_ops_ch08():
    pdf_path = os.path.join(OUTPUT_DIR, "070_ch08_windshear_volcanic_ash_wake_turbulence.pdf")
    pdf = PDFBuilder("Operational Procedures", "070", "Chapter 8: Windshear & Wake Turbulence")

    pdf.add_title_banner(
        "Operational Procedures",
        8,
        "All-Weather Hazards: Windshear, Ash & Wake Turbulence",
        "273-310"
    )

    pdf.add_heading_1("1. Windshear Recognition & Escape Maneuver")
    pdf.add_paragraph(
        "Low-level windshear produces sudden changes in indicated airspeed (> 15 kt), vertical speed (> 500 ft/min), and pitch angle (> 5°):"
    )
    pdf.add_bullet("Immediate Escape Maneuver", "1. Disconnect autopilot; 2. Advance thrust levers to FULL TOGA (firewall power!); 3. Rotate wings-level towards the pitch limit indicator (stick shaker); 4. STRICTLY PROHIBITED: DO NOT CHANGE GEAR OR FLAP CONFIGURATION until terrain clearance is assured (changing gear causes massive temporary drag increase!).")

    pdf.add_heading_1("2. ICAO Wake Turbulence Separation Minima")
    pdf.add_paragraph(
        "Wake vortices trail from wingtips, descending at 400 to 500 ft/min. Maximum hazard occurs behind Heavy aircraft in clean, slow, high-angle-of-attack flight:"
    )

    wake_table = [
        ["Leading Aircraft Category", "Following Aircraft Category", "Departure Time Separation (Same Runway / Intersection)"],
        ["HEAVY (>= 136,000 kg)", "MEDIUM (7,000 to 136,000 kg)", "2 MINUTES (3 minutes if following from intermediate intersection)."],
        ["HEAVY (>= 136,000 kg)", "LIGHT (< 7,000 kg)", "2 MINUTES (3 minutes if following from intermediate intersection)."],
        ["SUPER (Airbus A380)", "HEAVY / MEDIUM", "3 MINUTES full runway (4 minutes from intersection)."],
        ["SUPER (Airbus A380)", "LIGHT", "4 MINUTES (5 minutes from intersection)."]
    ]
    pdf.add_table(["Leading Aircraft Category", "Following Aircraft Category", "Departure Time Separation (Same Runway / Intersection)"], wake_table, col_widths=[125.0, 155.0, 215.0])

    pdf.add_heading_1("3. Volcanic Ash Cloud Encounter Procedures")
    pdf.add_bullet("Engine Flameout Threat", "Volcanic ash melts at 1,100°C inside turbine combustors, fusing into glassy enamel that suffocates turbine cooling holes and causes ALL ENGINES TO FLAMEOUT!")
    pdf.add_bullet("Escape Actions", "1. Execute IMMEDIATE 180° TURN back out of ash cloud; 2. Retard thrust levers to IDLE (reduces combustion temperature below ash melting point); 3. Start APU; 4. Turn on continuous engine ignition; 5. Select maximum cabin air bleed.")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: During an in-flight encounter with low-level WINDSHEAR, why is changing flap or landing gear configuration strictly prohibited?",
         "[A] Flap motor will overheat\n[B] Retracting or extending gear/flaps creates significant TRANSIENT DRAG and loss of lift, drastically increasing the risk of ground impact\n[C] ATC bans gear changes\n[D] Altimeter will fail",
         "CORRECT: [B]. The transient drag during gear door cycling can cause immediate loss of the precious few feet of altitude remaining."),
        ("Q2: What is the mandatory ICAO wake turbulence departure time interval between a HEAVY aircraft taking off and a following LIGHT aircraft from the same runway threshold?",
         "[A] 1 minute\n[B] AT LEAST 2 MINUTES\n[C] 5 minutes\n[D] 30 seconds",
         "CORRECT: [B]. ICAO Doc 4444 requires a minimum 2-minute separation behind a Heavy aircraft for same-runway departures (increased to 3 minutes for intersection take-offs)."),
        ("Q3: When inadvertently penetrating a volcanic ash cloud, why should engine thrust levers be retarded to IDLE?",
         "[A] To save fuel\n[B] To LOWER TURBINE GAS TEMPERATURES below the melting point of volcanic ash (~1,100°C), preventing molten glass from accumulating on turbine blades\n[C] To increase airspeed\n[D] To pressurize cabin",
         "CORRECT: [B]. At idle thrust, EGT drops below the ~1,100°C melting point of silicate ash, stopping the buildup of molten glassy deposits on turbine guide vanes.")
    ]

    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Operational Procedures Chapter 8 compiled: {pdf_path}")


def build_ops_ch09():
    pdf_path = os.path.join(OUTPUT_DIR, "070_ch09_ground_deicing_antiicing_holdover.pdf")
    pdf = PDFBuilder("Operational Procedures", "070", "Chapter 9: De-Icing & Holdover Times")

    pdf.add_title_banner(
        "Operational Procedures",
        9,
        "Ground De-Icing, Anti-Icing & Holdover Times (HOT)",
        "311-346"
    )

    pdf.add_heading_1("1. The Clean Aircraft Concept & Standard Fluids")
    pdf.add_paragraph(
        "Under EASA CAT.OP.MPA.250, no aircraft may commence take-off unless all critical surfaces (wings, control surfaces, engine inlets, pitot tubes) are completely free of frost, ice, slush, or snow:"
    )

    fluid_table = [
        ["ISO / SAE Fluid Type", "Viscosity, Thickener & Dye Color", "Aerodynamic & Operational Characteristics"],
        ["Type I (De-icing)", "Unthickened, low viscosity. DYED ORANGE.", "Applied hot (60°C) to remove ice/snow. Minimal Holdover Time (HOT: 5 to 15 min)."],
        ["Type II (Anti-icing)", "Thickened pseudoplastic. DYED YELLOW / CLEAR.", "Contains polymeric thickeners that absorb freezing moisture. Minimum rotation speed: 100 kt. HOT: 30 to 45 min."],
        ["Type III (Commuter)", "Thickened, intermediate viscosity. DYED BRIGHT GREEN.", "Designed for commuter turboprops with low rotation speed (Vr < 100 kt)."],
        ["Type IV (Advanced Anti-icing)", "Highly thickened pseudoplastic. DYED EMERALD GREEN.", "Provides LONGEST HOLDOVER TIME. Shears off cleanly during take-off roll at Vr >= 100 kt."]
    ]
    pdf.add_table(["ISO / SAE Fluid Type", "Viscosity, Thickener & Dye Color", "Aerodynamic & Operational Characteristics"], fluid_table, col_widths=[125.0, 175.0, 195.0])

    pdf.add_heading_1("2. Holdover Time (HOT) Rules")
    pdf.add_paragraph(
        "Holdover Time is the estimated time anti-icing fluid will prevent frost/ice forming on treated aircraft surfaces:"
    )
    pdf.add_bullet("Exact Start of HOT", "Holdover Time BEGINS AT THE EXACT MOMENT THE FINAL ANTI-ICING APPLICATION COMMENCES! (Not when treatment finishes!).")
    pdf.add_bullet("Pre-Take-Off Contamination Check", "If HOT expires prior to take-off, the aircraft must return for complete de-icing/anti-icing re-treatment, unless an external pre-take-off contamination inspection confirms surfaces remain 100% clean.")

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch09 = [
        ("Q1: Exactly when does the HOLDOVER TIME (HOT) of an anti-icing fluid treatment begin?",
         "[A] When the de-icing truck leaves the aircraft\n[B] At the START of the final anti-icing application\n[C] When take-off clearance is received\n[D] At brake release",
         "CORRECT: [B]. By international ICAO and EASA definition, holdover time begins at the exact start of the final anti-icing application step."),
        ("Q2: What visual color dye is standard for SAE TYPE IV advanced anti-icing fluid?",
         "[A] Orange\n[B] EMERALD GREEN\n[C] Yellow\n[D] Blue",
         "CORRECT: [B]. Type I is orange; Type II is straw/yellow; Type III is bright green; Type IV is emerald green."),
        ("Q3: What happens to a thickened pseudoplastic anti-icing fluid (Type II / IV) during the aircraft's take-off ground run?",
         "[A] It freezes solid\n[B] Under aerodynamic shear stress at speeds above 100 kt, its viscosity collapses and it SHEARS COMPLETELY OFF THE WING, leaving a clean aerodynamic surface\n[C] It remains permanently on the wing\n[D] It dissolves fuel",
         "CORRECT: [B]. Pseudoplastic fluids thin under shear stress, flowing completely off the wing at high speed during rotation to avoid reducing wing lift.")
    ]

    for q_text, opts, exp in questions_ch09:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Operational Procedures Chapter 9 compiled: {pdf_path}")


def build_ops_ch10():
    pdf_path = os.path.join(OUTPUT_DIR, "070_ch10_dangerous_goods_icao_iata.pdf")
    pdf = PDFBuilder("Operational Procedures", "070", "Chapter 10: Dangerous Goods (DGR)")

    pdf.add_title_banner(
        "Operational Procedures",
        10,
        "Carriage of Dangerous Goods by Air (ICAO & IATA)",
        "347-380"
    )

    pdf.add_heading_1("1. The 9 Classes of Dangerous Goods")
    pdf.add_paragraph(
        "Under ICAO Annex 18 and the IATA Dangerous Goods Regulations (DGR), hazardous materials are categorized into 9 distinct hazard classes:"
    )

    dgr_table = [
        ["Class", "Dangerous Goods Category", "Examples & Aircraft Loading Restrictions"],
        ["Class 1", "Explosives (Divisions 1.1 to 1.6)", "Ammunition, flares, fireworks. Most are forbidden on passenger aircraft."],
        ["Class 2", "Gases (Flammable, Non-flammable, Toxic)", "Aerosols, oxygen cylinders, compressed butane, toxic chlorine."],
        ["Class 3", "Flammable Liquids", "Paints, aviation fuels, alcohol solvents (flash point <= 60°C)."],
        ["Class 4", "Flammable Solids", "Matches, white phosphorus, magnesium alloys, spontaneously combustible goods."],
        ["Class 5", "Oxidizing Substances & Organic Peroxides", "Chemical oxygen generators (ValuJet tragedy), hydrogen peroxide."],
        ["Class 6", "Toxic & Infectious Substances", "Pesticides, cyanide, medical viral samples (Division 6.2)."],
        ["Class 7", "Radioactive Material", "Medical isotopes, industrial radiotracers. Classified into Category I, II, III."],
        ["Class 8", "Corrosives", "Sulfuric acid, battery fluids, mercury (corrodes aluminum alloy airframes!)."],
        ["Class 9", "Miscellaneous Dangerous Goods", "LITHIUM-ION BATTERIES, dry ice (solid CO2 creates asphyxiation risk in holds)."]
    ]
    pdf.add_table(["Class", "Dangerous Goods Category", "Examples & Aircraft Loading Restrictions"], dgr_table, col_widths=[75.0, 195.0, 225.0])

    pdf.add_heading_1("2. Notification to Captain (NOTOC)")
    pdf.add_paragraph(
        "Before departure, the airline ground handling agent must deliver a written NOTOC document to the aircraft Commander:"
    )
    pdf.add_bullet("Mandatory NOTOC Data", "1. Proper Shipping Name and UN Number; 2. Hazard Class and Division; 3. Net quantity per package; 4. Exact physical cargo hold compartment location (e.g. Hold 4, Bin 2); 5. Confirmation that packages are undamaged; 6. ICAO Emergency Response Drill Code (e.g. Drill 4L for emergency checklists).")

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch10 = [
        ("Q1: What is the formal document that MUST be provided in writing to the aircraft Commander prior to departure whenever Dangerous Goods are loaded on board?",
         "[A] Flight manifest\n[B] NOTOC (Notification to Captain)\n[C] Cargo bill\n[D] Customs clearance",
         "CORRECT: [B]. Under ICAO Annex 18 and EASA SPA.DG.105, the Commander must receive a written NOTOC detailing all hazardous goods, positions, and emergency drill codes."),
        ("Q2: Under which IATA Dangerous Goods Class are LITHIUM-ION BATTERIES categorized?",
         "[A] Class 1\n[B] CLASS 9 (Miscellaneous Dangerous Goods)\n[C] Class 3\n[D] Class 5",
         "CORRECT: [B]. Lithium batteries (UN 3480 and UN 3481) fall under Class 9: Miscellaneous Dangerous Goods."),
        ("Q3: What hazard is associated with carrying large quantities of DRY ICE (solid carbon dioxide) in an aircraft cargo hold?",
         "[A] Explosion risk\n[B] SUFFOCATION / ASPHYXIATION HAZARD, as dry ice sublimates into gaseous carbon dioxide, displacing oxygen in confined compartments\n[C] Radiation\n[D] Corrosion of steel",
         "CORRECT: [B]. Dry ice sublimates into gaseous CO2 at normal hold temperatures, creating an invisible asphyxiation risk for ground and flight personnel.")
    ]

    for q_text, opts, exp in questions_ch10:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Operational Procedures Chapter 10 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_ops_ch06()
    build_ops_ch07()
    build_ops_ch08()
    build_ops_ch09()
    build_ops_ch10()
