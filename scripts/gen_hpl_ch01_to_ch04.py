#!/usr/bin/env python3
"""
Generator for 040 Human Performance & Limitations (HPL)
Chapters 01 to 04:
- Chapter 01: Human Factors - Basic Concepts, Safety Culture & Accident Statistics
- Chapter 02: Aviation Physiology - Atmosphere, Respiration & Gas Laws
- Chapter 03: Hypoxia & Hyperventilation
- Chapter 04: Decompression Sickness & Barotrauma

Exclusively for 100% EASA / AviationExam self-sufficient study.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "resumenes", "convocatoria_1", "040_human_performance"
)
os.makedirs(BASE_DIR, exist_ok=True)

# ==============================================================================
# CHAPTER 01: HUMAN FACTORS - BASIC CONCEPTS & ACCIDENT STATISTICS (~3-4 pages)
# ==============================================================================
def build_ch01():
    pdf_path = os.path.join(BASE_DIR, "040_ch01_human_factors_concepts.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 1: Human Factors & Safety Culture")
    pdf.add_title_banner("Human Performance", 1, "Human Factors & Safety Culture", "1-22")

    pdf.add_heading_1("1. The Discipline of Human Factors (Ergonomics)")
    pdf.add_paragraph(
        "Human Factors (or Ergonomics) is the multidisciplinary science that studies human capabilities, "
        "limitations, and behaviors to optimize the design of aeronautical equipment, operating procedures, "
        "and work environments. The ultimate objective is dual: to enhance flight safety and system efficiency, "
        "while safeguarding human well-being and performance.",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "Official Definition of Human Factors (ICAO Doc 9683)",
        "Human Factors is about people in their living and working situations; about their relationship with "
        "machines, with procedures, and with the environment; and about their relationships with other people.",
        max_chars=86
    )

    pdf.add_heading_1("2. Aviation Accident Statistics & The Human Contribution")
    pdf.add_paragraph(
        "Statistical analysis across global commercial aviation over the past five decades reveals that:",
        max_chars=92
    )
    pdf.add_bullet("Human Error Factor", "Between 70% and 80% of all civil aviation accidents have human error as the primary or contributing causal factor.")
    pdf.add_bullet("Accident Phase Distribution", "More than 60% of all fatal accidents occur during the Take-off / Initial Climb and Final Approach / Landing phases, despite these phases accounting for only ~16% of total flight duration.")
    pdf.add_bullet("Deadliest Accident Categories", "Loss of Control In-Flight (LOC-I) and Controlled Flight Into Terrain (CFIT) historically represent the highest numbers of fatalities in commercial transport operations.")

    pdf.add_heading_1("3. Accident Causation & Safety Principles")
    stats_data = [
        ["Heinrich's Safety Triangle", "1 : 29 : 300", "For every 1 major/fatal accident, there are 29 minor injuries/incidents, and 300 unsafe acts or near-misses. Eliminating minor hazards prevents major catastrophes."],
        ["Murphy's Law", "'If it can happen, it will'", "A system must be designed so that incorrect installation or operation is physically impossible (Poka-Yoke / design ergonomics, e.g. distinct cable fittings)."],
        ["Swiss Cheese Model (Reason)", "Latent vs Active", "Catastrophes occur when defensive barriers across organizational, supervisory, and operational layers breach simultaneously."]
    ]
    pdf.add_table(["Safety Principle / Model", "Core Ratio or Principle", "Aeronautical Operational Implication"], stats_data, col_widths=[140.0, 110.0, 250.0])

    pdf.add_heading_1("4. Safety Culture, Just Culture & ICAO SMS")
    pdf.add_callout(
        "trap",
        "AviationExam Core Trap: The Definition of 'Just Culture'",
        "A 'Just Culture' is NOT complete immunity from disciplinary action! Under EASA and ICAO Annex 19:\n"
        "• Protected: Honest human errors, cognitive slips, lapses, and mistakes reported promptly are non-punitive.\n"
        "• UNPROTECTED: Wilful violations, gross negligence, criminal intent, and substance abuse (drugs/alcohol) "
        "are strictly subject to disciplinary and legal sanction.",
        max_chars=86
    )

    pdf.add_paragraph(
        "Key pillars of an effective corporate safety culture:\n"
        "1. Informed Culture: Knowledgeable about human, technical, and organizational factors.\n"
        "2. Reporting Culture: Staff freely report errors, near misses, and safety hazards without fear.\n"
        "3. Learning Culture: The organization draws conclusions from safety data and implements structural reforms.\n"
        "4. Flexible Culture: Adapting authority structures dynamically during emergencies.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: What percentage of aircraft accidents are attributed primarily to human error?",
         "[A] 20% to 30%\n[B] 50% exactly\n[C] 70% to 80%\n[D] Over 95%",
         "CORRECT: [C]. Industry and EASA accident data consistently confirm that between 70% and 80% of all aircraft accidents are caused by human error."),
        ("Q2: In Heinrich's accident pyramid, what is the ratio between major accidents, minor incidents, and unsafe acts?",
         "[A] 1 : 10 : 100\n[B] 1 : 29 : 300\n[C] 1 : 50 : 500\n[D] 1 : 100 : 1,000",
         "CORRECT: [B]. Heinrich's ratio is 1 major accident to 29 minor accidents/injuries to 300 unsafe acts or near misses."),
        ("Q3: In a modern corporate 'Just Culture', which behavior is exempt from disciplinary action?",
         "[A] Gross negligence resulting in aircraft damage\n[B] Flying under the influence of alcohol\n[C] Honest, inadvertent errors reported openly through the safety management system\n[D] Deliberate violation of published SOPs",
         "CORRECT: [C]. A Just Culture encourages non-punitive reporting of honest errors and inadvertent slips, but explicitly punishes gross negligence and wilful violations."),
        ("Q4: During which phase of flight do the majority of fatal commercial aviation accidents occur?",
         "[A] High altitude cruise\n[B] Take-off and landing phases\n[C] Initial climb above 10,000 ft\n[D] Descent prior to terminal area entry",
         "CORRECT: [B]. Take-off/initial climb and approach/landing account for > 60% of fatal accidents despite representing a small fraction of flight time."),
        ("Q5: What is the primary operational goal of cockpit ergonomics?",
         "[A] Making the cockpit as inexpensive as possible to build\n[B] Adapting the machine and working environment to human physiological and psychological characteristics\n[C] Replacing the human pilot completely with automation\n[D] Enforcing military discipline among crew members",
         "CORRECT: [B]. Ergonomics optimizes the human-machine interface by matching technology to human capabilities and limitations."),
        ("Q6: How does Murphy's Law apply to aircraft maintenance and component design?",
         "[A] All mechanical parts fail within 1,000 flight hours\n[B] Components must be designed so that improper assembly or reverse connection is mechanically impossible\n[C] Pilots should not perform pre-flight inspections\n[D] Checklist usage is optional for experienced pilots",
         "CORRECT: [B]. In aviation ergonomics, Murphy's law requires 'error-tolerant' design (e.g. keyways, asymmetric pins) preventing incorrect installation.")
    ]
    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 1 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 02: AVIATION PHYSIOLOGY - ATMOSPHERE, RESPIRATION & GAS LAWS (~4 pages)
# ==============================================================================
def build_ch02():
    pdf_path = os.path.join(BASE_DIR, "040_ch02_aviation_physiology_gas_laws.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 2: Atmosphere, Respiration & Gas Laws")
    pdf.add_title_banner("Human Performance", 2, "Aviation Physiology & Gas Laws", "23-56")

    pdf.add_heading_1("1. Atmospheric Composition & Vertical Structure")
    pdf.add_paragraph(
        "Clean, dry atmospheric air has an essentially constant volumetric composition up to approximately "
        "70,000 ft (the homosphere):",
        max_chars=92
    )
    pdf.add_bullet("Nitrogen (N2)", "78.08% (~78%) - Inert diluent gas; dissolves in body fluids under pressure.")
    pdf.add_bullet("Oxygen (O2)", "20.95% (~21%) - Vital gas for cellular metabolism and aerobic respiration.")
    pdf.add_bullet("Argon (Ar)", "0.93% - Inert noble gas.")
    pdf.add_bullet("Carbon Dioxide (CO2)", "0.04% - Crucial physiological regulator of respiration.")

    pdf.add_paragraph(
        "ISA Standards at Mean Sea Level (MSL): Pressure = 1013.25 hPa (760 mmHg = 29.92 inHg); Temperature = +15°C. "
        "Standard temperature lapse rate: 2°C per 1,000 ft (6.5°C per 1,000 m) up to the Tropopause (36,090 ft / 11 km), "
        "where temperature becomes constant at -56.5°C.",
        max_chars=92
    )

    pdf.add_heading_1("2. The Master Aviation Gas Laws (AviationExam Core)")
    laws_data = [
        ["Dalton's Law", "P_total = P1 + P2 + ... + Pn", "Total pressure equals the sum of partial pressures. Because O2 is 21%, P_O2 = 0.21 x P_ambient. As ambient pressure falls with altitude, P_O2 falls proportionally, causing Hypoxic Hypoxia."],
        ["Boyle's Law", "P x V = Constant (at const T)", "Pressure and volume of a gas are inversely proportional. As altitude increases, trapped body gases EXPAND (Middle ear, sinuses, tooth pulp, GI tract). Gas volume doubles at FL 180 (0.5 atm)!"],
        ["Henry's Law", "Amount dissolved = k x P_gas", "The mass of gas dissolved in a liquid is proportional to its partial pressure. Rapid decompression causes nitrogen to bubble out of physical solution, causing Decompression Sickness (DCS)."],
        ["Graham's Law", "Rate of diffusion inversely prop. to sqrt(mass)", "Gases diffuse from high partial pressure to low partial pressure across alveolar-capillary membranes. Light gases diffuse faster."],
        ["Charles' Law", "V1 / T1 = V2 / T2 (at const P)", "Gas volume increases directly with temperature. Critical for oxygen storage cylinder pressure variations with ambient temperature."]
    ]
    pdf.add_table(["Gas Law", "Mathematical Formulation", "Aeronautical & Human Physiological Impact"], laws_data, col_widths=[105.0, 145.0, 250.0])

    pdf.add_callout(
        "trap",
        "Gas Volume Expansion Factors with Altitude (Boyle's Law)",
        "AviationExam frequently tests the exact volume multiplier for trapped body gases:\n"
        "• Sea Level (1.0 atm / 1013 hPa): Volume = 1.0\n"
        "• FL 180 (18,000 ft / 0.5 atm / ~500 hPa): Gas volume DOUBLES (2.0x)\n"
        "• FL 340 (34,000 ft / 0.25 atm / ~250 hPa): Gas volume QUADRUPLES (4.0x)\n"
        "• FL 420 (42,000 ft / 0.17 atm / ~170 hPa): Gas volume expands SIX TIMES (6.0x)!",
        max_chars=86
    )

    pdf.add_heading_1("3. Respiratory Mechanics & Alveolar Gas Exchange")
    pdf.add_paragraph(
        "• External Respiration: Gas exchange in the lungs between alveoli and pulmonary capillary blood.\n"
        "• Internal Respiration: Gas exchange between systemic capillaries and metabolizing tissue cells.\n"
        "• Alveolar Gas Environment: In the alveoli, inspired air is fully humidified with water vapor (P_H2O = 47 mmHg at 37°C) "
        "and mixed with carbon dioxide (P_CO2 = 40 mmHg).",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "The Alveolar Oxygen Formula (Critical Physiological Threshold)",
        "P_A_O2 = (P_ambient - 47) x 0.21 - (P_CO2 / 0.8)\n"
        "• At Sea Level: P_A_O2 = (760 - 47) x 0.21 - (40 / 0.8) = 150 - 50 = ~100 mmHg.\n"
        "• At 10,000 ft: P_A_O2 drops to ~60 mmHg (arterial saturation drops to 90%). Performance deteriorates!\n"
        "• Above 63,000 ft (Armstrong's Line): Ambient pressure drops below 47 mmHg; body fluids boil at 37°C!",
        max_chars=86
    )

    pdf.add_heading_1("4. Hemoglobin, Oxygen Transport & The Bohr Effect")
    pdf.add_paragraph(
        "Oxygen is carried in the blood in two forms: 1.5% physically dissolved in blood plasma, and 98.5% chemically bound "
        "to hemoglobin (Hb) inside erythrocytes (red blood cells). Each gram of Hb can bind 1.34 ml of oxygen.",
        max_chars=92
    )
    pdf.add_bullet("Oxygen Dissociation Curve", "A non-linear, sigmoidal (S-shaped) curve relating arterial P_O2 to hemoglobin saturation (SaO2). The steep portion below 60 mmHg means small altitude increases cause rapid desaturation.")
    pdf.add_bullet("The Bohr Effect (Right Shift)", "The curve shifts to the RIGHT (lowering Hb affinity for oxygen, promoting O2 unloading to tissues) under: Increased blood P_CO2 (hypercapnia), Increased acidity (lower pH), Increased body temperature, and increased 2,3-DPG.")

    pdf.add_heading_1("5. The Primary Chemical Driver of Respiration")
    pdf.add_callout(
        "trap",
        "Absolute Exam Trap: What Controls Your Breathing Rate?",
        "• Primary Chemical Stimulus: Breathing rate and depth are controlled by chemoreceptors in the MEDULLA OBLONGATA "
        "sensitive to the partial pressure of CARBON DIOXIDE (P_CO2) and H+ ion concentration (pH) in arterial blood.\n"
        "• Secondary Stimulus: Peripheral chemoreceptors in the carotid and aortic bodies monitor low P_O2 (hypoxia), "
        "but this hypoxic drive acts only as a backup when P_O2 drops below 60 mmHg!",
        max_chars=86
    )

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: What is the primary chemical stimulus that regulates the rate and depth of breathing in a healthy human?",
         "[A] Low oxygen partial pressure in the lungs\n[B] High nitrogen saturation in the blood\n[C] The concentration of carbon dioxide (P_CO2) and hydrogen ions in arterial blood\n[D] Blood glucose concentration",
         "CORRECT: [C]. The respiratory center in the brainstem (medulla) is primarily driven by P_CO2 and pH levels, NOT by oxygen deficiency."),
        ("Q2: According to Boyle's law, if an aircraft experiences a rapid decompression from sea level to FL 180, what happens to the volume of trapped gas in the pilot's body?",
         "[A] It remains unchanged\n[B] It doubles (2x)\n[C] It quadruples (4x)\n[D] It is halved (0.5x)",
         "CORRECT: [B]. At FL 180, atmospheric pressure is halved (~500 hPa vs 1013 hPa), so gas volume doubles according to Boyle's law (P x V = const)."),
        ("Q3: Which gas law explains the development of Decompression Sickness (DCS) during high altitude flight?",
         "[A] Dalton's Law\n[B] Boyle's Law\n[C] Henry's Law\n[D] Charles' Law",
         "CORRECT: [C]. Henry's law states that the amount of dissolved gas in a liquid depends on its partial pressure. When pressure drops, dissolved nitrogen bubbles out."),
        ("Q4: What is the percentage of oxygen in atmospheric air at 34,000 ft compared to sea level?",
         "[A] Exactly the same (approx. 21%)\n[B] Approximately 10%\n[C] Less than 5%\n[D] 0%",
         "CORRECT: [A]. The percentage of oxygen remains constant at ~21% throughout the homosphere (up to 70,000 ft). Hypoxia occurs because total pressure, and therefore oxygen partial pressure, drops (Dalton's Law)."),
        ("Q5: What is 'Armstrong's Line' in aviation physiology and at what approximate altitude does it occur?",
         "[A] FL 100 where supplemental oxygen is required\n[B] FL 180 where gas volume doubles\n[C] Approx. 63,000 ft where atmospheric pressure equals body water vapor pressure (47 mmHg) and exposed body fluids boil\n[D] The tropopause at 36,000 ft",
         "CORRECT: [C]. At 63,000 ft (pressure 47 mmHg / 63 hPa), water boils at normal body temperature (37°C). A full pressure suit is mandatory."),
        ("Q6: Which condition shifts the hemoglobin oxygen dissociation curve to the right (Bohr Effect), facilitating oxygen release to working muscles?",
         "[A] Decreased temperature and hypothermia\n[B] Decreased P_CO2 (hypocapnia) and elevated pH (alkalosis)\n[C] Increased blood P_CO2, increased acidity (lower pH), and elevated temperature\n[D] Low altitude exposure",
         "CORRECT: [C]. Acidosis, high P_CO2, and heat shift the curve rightwards, decreasing Hb affinity and facilitating oxygen delivery to metabolizing tissues."),
        ("Q7: What is the standard atmospheric pressure and temperature at Mean Sea Level according to the International Standard Atmosphere (ISA)?",
         "[A] 1000 hPa and 20°C\n[B] 1013.25 hPa (760 mmHg) and +15°C\n[C] 1020 hPa and 0°C\n[D] 29.92 hPa and 15°C",
         "CORRECT: [B]. Standard ISA MSL values are 1013.25 hPa (29.92 inHg / 760 mmHg) and +15°C."),
        ("Q8: Under what physiological condition does the body's peripheral chemoreceptor backup drive (hypoxic drive) activate?",
         "[A] When arterial P_O2 falls below approximately 60 mmHg (corresponding to altitudes above 10,000 ft)\n[B] When blood pH rises above 7.45\n[C] Only during deep REM sleep\n[D] When nitrogen bubbles form in capillaries",
         "CORRECT: [A]. The peripheral chemoreceptors (carotid and aortic bodies) respond to severe hypoxia only when arterial P_O2 falls below ~60 mmHg.")
    ]
    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 2 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 03: HYPOXIA & HYPERVENTILATION (~4 pages)
# ==============================================================================
def build_ch03():
    pdf_path = os.path.join(BASE_DIR, "040_ch03_hypoxia_hyperventilation.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 3: Hypoxia & Hyperventilation")
    pdf.add_title_banner("Human Performance", 3, "Hypoxia & Hyperventilation", "57-82")

    pdf.add_heading_1("1. The Four Types of Hypoxia (Classification & Causes)")
    hypoxia_data = [
        ["1. Hypoxic Hypoxia (Altitude Hypoxia)", "Deficiency in alveolar oxygen partial pressure (P_O2). Most common in aviation. Caused by high altitude, cabin depressurization, or airway obstruction."],
        ["2. Anemic (Hypemic) Hypoxia", "Reduction in oxygen-carrying capacity of the blood. Hemoglobin is deficient or bound by another agent (Carbon Monoxide poisoning, severe blood loss, smoking, anemia). CO has 200-250x affinity for Hb!"],
        ["3. Stagnant (Circulatory) Hypoxia", "Inadequate regional blood circulation despite normal blood oxygenation. Caused by high positive acceleration (+Gz pulling blood to feet), heart failure, arterial disease, or extreme cold."],
        ["4. Histotoxic Hypoxia", "Inability of cells to use available oxygen due to cellular poisoning of enzyme systems (cytochrome oxidase). Caused by alcohol, cyanide, narcotics, or carbon monoxide."]
    ]
    pdf.add_table(["Hypoxia Type", "Aetiology, Mechanism & Aeronautical Causes"], hypoxia_data, col_widths=[150.0, 350.0])

    pdf.add_heading_1("2. Stages of Hypoxic Hypoxia & Blood Saturation")
    stages_data = [
        ["Indifferent Stage", "0 to 10,000 ft", "98% down to 90%", "Mild night vision impairment starting at 4,000-5,000 ft (rod cells lack O2). No other daytime symptoms."],
        ["Compensatory Stage", "10,000 to 15,000 ft", "90% down to 80%", "Body compensates: increased heart rate and respiratory ventilation. Subtle euphoria, impaired complex arithmetic."],
        ["Disturbance Stage", "15,000 to 20,000 ft", "80% down to 70%", "Headache, fatigue, loss of self-criticism, cognitive confusion, tunnel vision, cyanosis (blue skin/lips). Loss of fine motor coordination."],
        ["Critical Stage", "Above 20,000 ft", "Below 70%", "Rapid incapacitation, deterioration of consciousness, convulsions, coma, followed by irreversible brain death."]
    ]
    pdf.add_table(["Stage Name", "Altitude Range", "Arterial O2 Saturation", "Clinical Symptoms & Operational Hazards"], stages_data, col_widths=[110.0, 95.0, 105.0, 190.0])

    pdf.add_heading_1("3. Time of Useful Consciousness (TUC) Master Matrix")
    pdf.add_paragraph(
        "TUC (also termed Effective Performance Time - EPT) is the maximum time a pilot has from the onset of oxygen "
        "deficiency until the ability to perform deliberate, coordinated flight actions is lost:",
        max_chars=92
    )

    tuc_data = [
        ["FL 180 (18,000 ft)", "20 to 30 minutes", "Moderate cognitive decline, euphoria."],
        ["FL 220 (22,000 ft)", "5 to 10 minutes", "Motor impairment, blurred vision."],
        ["FL 250 (25,000 ft)", "3 to 5 minutes", "Rapid loss of reasoning ability."],
        ["FL 300 (30,000 ft)", "1 to 2 minutes (60-120 s)", "Severe confusion, motor collapse."],
        ["FL 350 (35,000 ft)", "30 to 60 seconds", "Extremely rapid incapacitation."],
        ["FL 400 (40,000 ft)", "15 to 20 seconds", "Just enough time to don oxygen mask."],
        ["FL 450 and above", "9 to 12 seconds", "Circulation time from lungs to brain (~10 s)."]
    ]
    pdf.add_table(["Flight Level / Altitude", "Time of Useful Consciousness (TUC)", "Operational State & Pilot Capability"], tuc_data, col_widths=[125.0, 165.0, 210.0])

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Time of Useful Consciousness (TUC) Under Rapid Decompression",
        "SCENARIO (Crucial Flight Physiology Exam Drill):\n"
        "A transport jet is cruising at FL 350 (35,000 ft) when a cargo door seal fails catastrophically, producing an immediate explosive cabin depressurization:\n"
        "- Under normal conditions at FL 350, baseline TUC is 30 to 60 seconds\n"
        "QUESTION: What is the pilot's revised TUC following this explosive decompression, and what mandatory immediate action must be taken?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Identify the Physiological Effect of Explosive Decompression:\n"
        "  - Sudden pressure drop forces air out of lungs and creates reverse diffusion (oxygen leaves blood back into lungs!).\n"
        "  - Regulatory/Medical Rule: TUC is cut by 50% (half of normal baseline!).\n\n"
        "Step 2: Calculate the Reduced TUC Window:\n"
        "  - Normal TUC at FL 350 = 30 to 60 seconds\n"
        "  - Reduced TUC = 50% x (30 to 60 s) = 15 to 30 SECONDS!\n\n"
        "Step 3: Determine Immediate Pilot Survival Protocol:\n"
        "  - 15-30 seconds leaves ZERO time for troubleshooting or communications!\n"
        "  - Immediate memory item: DON OXYGEN MASK FIRST (within 5 seconds), establish 100% positive pressure oxygen, then initiate emergency descent to FL 100 / MEA!\n\n"
        "FINAL ANSWER: Revised TUC is 15 to 30 seconds. The flight crew must don quick-donning masks immediately within 5 seconds before cognitive paralysis occurs!",
        max_chars=86
    )

    pdf.add_heading_1("5. Hyperventilation vs Hypoxia: Differential Diagnosis")
    pdf.add_paragraph(
        "Hyperventilation is breathing in excess of metabolic needs, causing excessive elimination of carbon dioxide (hypocapnia). "
        "This drives blood pH up (Respiratory Alkalosis), causing cerebral vasoconstriction (reduced brain blood supply).",
        max_chars=92
    )

    diff_data = [
        ["Causes", "High altitude, depressurization, mask failure.", "Stress, panic, anxiety, vibration, motion sickness."],
        ["Blood Gas Shift", "Severely decreased arterial P_O2.", "Severely decreased arterial P_CO2; blood alkalosis."],
        ["Early Symptoms", "Euphoria, false security, loss of judgment.", "Anxiety, lightheadedness, cold clammy sweat."],
        ["Specific Sign", "Cyanosis (bluish skin, lips, nailbeds).", "Paresthesia (tingling lips/fingers), Carpopedal spasms (tetany)."],
        ["Emergency Action", "100% O2 on, descend below 10,000 ft.", "Slow down breathing rate (talk, breathe in paper bag)."]
    ]
    pdf.add_table(["Diagnostic Parameter", "Hypoxic Hypoxia", "Hyperventilation"], diff_data, col_widths=[110.0, 195.0, 195.0])

    pdf.add_callout(
        "definition",
        "The Universal In-Flight Emergency Rule",
        "Because the subjective symptoms of hypoxia and hyperventilation overlap (dizziness, tingling, confusion):\n"
        "IF ABOVE 10,000 FT, ALWAYS ASSUME HYPOXIA FIRST!\n"
        "1. Immediately don oxygen mask (100% O2 under positive pressure);\n"
        "2. Check oxygen supply and regulator;\n"
        "3. Consciously control and slow down respiratory rate to 10-12 breaths/min;\n"
        "4. Initiate emergency descent if unpressurized.",
        max_chars=86
    )

    pdf.add_heading_1("5. Flight Deck & Passenger Oxygen Systems")
    ox_data = [
        ["Continuous Flow", "Passengers (Cabin < FL 250)", "Fixed rate or barometrically controlled. Rebreather bag. Inefficient for flight crew."],
        ["Diluter Demand", "Flight Crew (Up to FL 340)", "Mixes ambient air with pure O2 proportionally with altitude. Delivers 100% O2 automatically above FL 320 or when selected."],
        ["Pressure Demand", "Flight Crew (Above FL 340 / FL 390)", "Forces 100% pure oxygen into lungs under POSITIVE PRESSURE to overcome low barometric pressure. Requires active, conscious exhalation!"],
        ["Quick-Donning Mask", "Mandatory for Flight Crew", "Must be capable of being placed on face with ONE HAND in LESS THAN 5 SECONDS from the stowed position, accommodating eyeglasses."]
    ]
    pdf.add_table(["Oxygen Delivery System", "Operational User & Altitude Range", "Delivery Mechanism & In-Flight Requirements"], ox_data, col_widths=[125.0, 150.0, 225.0])

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: What is the approximate Time of Useful Consciousness (TUC) for a pilot at FL 300 following a gradual decompression?",
         "[A] 10 to 15 minutes\n[B] 1 to 2 minutes\n[C] 15 to 20 seconds\n[D] 9 to 12 seconds",
         "CORRECT: [B]. At FL 300, normal TUC is 1 to 2 minutes (reduced to 30-60 seconds in an explosive decompression)."),
        ("Q2: In the event of an explosive decompression at FL 350, how is the pilot's Time of Useful Consciousness affected?",
         "[A] It is doubled due to adrenaline rush\n[B] It is unchanged\n[C] It is reduced by one third to one half (30% to 50%)\n[D] It is extended to 10 minutes",
         "CORRECT: [C]. Explosive decompression reduces TUC by 33% to 50% due to rapid lung exhalation and reverse oxygen diffusion from blood to alveoli."),
        ("Q3: Carbon monoxide poisoning causes which specific type of hypoxia?",
         "[A] Hypoxic hypoxia\n[B] Anemic (hypemic) hypoxia\n[C] Stagnant hypoxia\n[D] Histotoxic hypoxia",
         "CORRECT: [B]. Carbon monoxide binds to hemoglobin with ~250 times greater affinity than oxygen, depriving blood of oxygen transport capacity (anemic hypoxia)."),
        ("Q4: What is the primary physiological consequence of hyperventilation?",
         "[A] Increased arterial P_CO2 and severe acidosis\n[B] Excessive loss of CO2 (hypocapnia) resulting in respiratory alkalosis and cerebral vasoconstriction\n[C] Immediate lung tissue collapse\n[D] High arterial oxygen toxicity",
         "CORRECT: [B]. Hyperventilation blows off CO2, raising blood pH (alkalosis) and constricting cerebral blood vessels, leading to dizziness and tingling."),
        ("Q5: If a pilot at FL 250 suddenly feels lightheaded, dizzy, and notices tingling in the fingers, what immediate action must be taken?",
         "[A] Assume hyperventilation, remove oxygen mask, and breathe into a bag\n[B] Assume hypoxia immediately, don oxygen mask with 100% oxygen, and check oxygen connections\n[C] Increase cockpit temperature\n[D] Drink water to restore blood circulation",
         "CORRECT: [B]. Above 10,000 ft, always assume hypoxia first. Don oxygen mask with 100% O2 immediately before diagnosing hyperventilation."),
        ("Q6: At what altitude does night vision acuity begin to deteriorate noticeably due to mild rod cell hypoxia?",
         "[A] At sea level\n[B] Around 4,000 to 5,000 ft\n[C] Above 10,000 ft only\n[D] Above 18,000 ft",
         "CORRECT: [B]. The retina has the highest metabolic oxygen demand in the human body; rod photoreceptors show degraded night vision above 4,000–5,000 ft."),
        ("Q7: Why is a pressure-demand oxygen mask required for flight crew operations at altitudes above FL 390?",
         "[A] To prevent oxygen cylinder freezing\n[B] Because ambient barometric pressure is so low that 100% oxygen at ambient pressure cannot provide sufficient alveolar P_O2\n[C] To allow pilots to speak without a microphone\n[D] Because continuous flow systems are illegal in Europe",
         "CORRECT: [B]. Above FL 390, total ambient pressure (148 mmHg) is barely above body water vapor and CO2 pressure (47 + 40 = 87 mmHg); positive pressure breathing is required to force oxygen into blood.")
    ]
    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 3 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 04: DECOMPRESSION SICKNESS & BAROTRAUMA (~4 pages)
# ==============================================================================
def build_ch04():
    pdf_path = os.path.join(BASE_DIR, "040_ch04_dcs_barotrauma.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 4: Decompression Sickness & Barotrauma")
    pdf.add_title_banner("Human Performance", 4, "Decompression Sickness & Barotrauma", "83-108")

    pdf.add_heading_1("1. Decompression Sickness (DCS) & Henry's Law")
    pdf.add_paragraph(
        "Under normal atmospheric pressure, nitrogen gas is held in physical solution in body fluids and fatty tissues. "
        "When ambient barometric pressure decreases rapidly (above FL 180, and especially above FL 300), the body tissues "
        "become supersaturated, and nitrogen comes out of solution forming gaseous bubbles.",
        max_chars=92
    )

    pdf.add_heading_1("2. The Four Classical Clinical Forms of DCS")
    dcs_data = [
        ["The Bends (Joint & Muscular)", "85% of cases", "Deep, dull, throbbing pain in joints (knees, shoulders, elbows). Pain increases on movement. Relieved temporarily by firm pressure."],
        ["The Chokes (Pulmonary)", "Rare (< 2%), but FATAL", "Bubbles lodge in pulmonary capillary bed. Symptoms: Substernal burning chest pain, severe paroxysmal dry cough, dyspnoea, cyanosis, circulatory collapse."],
        ["The Creeps (Cutaneous / Skin)", "10% of cases", "Nitrogen bubbles in dermal capillaries. Symptoms: Intense itching, burning, tingling ('ants crawling under skin' - formication), mottled reddish/purplish skin rash."],
        ["The Staggers (Neurological)", "Severe / Critical", "Bubbles in central nervous system or spinal cord. Symptoms: Visual scotoma, severe headache, confusion, ataxia, hemiplegia, stroke-like focal deficits."]
    ]
    pdf.add_table(["DCS Clinical Form", "Incidence & Severity", "Typical Symptoms & Clinical Manifestations"], dcs_data, col_widths=[125.0, 105.0, 270.0])

    pdf.add_callout(
        "definition",
        "Emergency Treatment of In-Flight Decompression Sickness",
        "1. Immediate emergency descent to sea level or the lowest safe altitude;\n"
        "2. Administer 100% OXYGEN via tightly fitting mask (accelerates nitrogen washout);\n"
        "3. Immobilize affected limbs (do NOT exercise the affected joint);\n"
        "4. Urgent transfer to a medical facility equipped with a HYPERBARIC RECOMPRESSION CHAMBER.",
        max_chars=86
    )

    pdf.add_heading_1("3. Scuba Diving Rules Before Flying (EASA Part-MED / ICAO)")
    pdf.add_callout(
        "trap",
        "Mandatory Wait Times Between Diving and Flying (Memorize 100%)",
        "Scuba diving loads body tissues with dissolved nitrogen under high hyperbaric pressure. Flying afterward greatly multiplies DCS risk!\n"
        "• Non-Decompression Diving (Depth < 10 m / 30 ft, no decompression stops): Wait at least 12 HOURS before flying.\n"
        "• Decompression Diving (Requiring decompression stops) OR Multiple Dives over consecutive days: Wait at least 24 HOURS before flying.\n"
        "• Deep Technical / Saturation Diving: Recommended wait time is 48 HOURS.",
        max_chars=86
    )

    pdf.add_heading_1("4. Barotrauma (Boyle's Law P x V = Constant)")
    pdf.add_paragraph(
        "Barotrauma is physical tissue damage caused by expansion or contraction of trapped gas inside rigid body cavities "
        "when pressure changes cannot equalize:",
        max_chars=92
    )

    baro_data = [
        ["Otic Barotrauma (Ear Block)", "Middle ear via Eustachian Tube", "Ascent: Air vents passively out easily. Descent: Eustachian tube acts as flap valve; if inflamed (cold/rhinitis), tube locks shut. Result: Severe pain, eardrum retraction, hematoma, rupture. Prevention: Valsalva, swallowing."],
        ["Sinus Barotrauma (Barosinusitis)", "Frontal & Maxillary Sinuses", "Blocked ostia trap air. Extreme sharp pain over forehead/cheeks on descent. May cause nosebleeds (epistaxis)."],
        ["Dental Barotrauma (Barodontalgia)", "Tooth pulp / defective cavity", "Air pocket trapped under filling or abscess. Severe sharp toothache, typically occurs on ASCENT."],
        ["Gastrointestinal Barotrauma", "Stomach, Small & Large Intestine", "Gas expands on ascent (doubles by FL 180). Causes severe abdominal distension and cramping. Prevent by avoiding carbonated drinks and gas-producing food."]
    ]
    pdf.add_table(["Type of Barotrauma", "Anatomical Site", "Mechanism, Peak Danger Phase & Symptoms"], baro_data, col_widths=[125.0, 115.0, 260.0])

    pdf.add_callout(
        "trap",
        "Ascent vs Descent: When is Barotrauma Worst?",
        "• Ear Barotrauma (Otic) and Sinus Barotrauma occur almost exclusively during DESCENT, because air cannot enter "
        "swollen passages from the higher outside pressure.\n"
        "• Dental Barotrauma (Barodontalgia) and Gastrointestinal Distension occur predominantly during ASCENT, "
        "as trapped air expands.",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: Following a scuba dive requiring decompression stops, what is the minimum required waiting time before flying under EASA regulations?",
         "[A] 4 hours\n[B] 12 hours\n[C] 24 hours\n[D] 48 hours",
         "CORRECT: [C]. EASA Part-MED mandates at least 24 hours wait time after decompression diving (or multiple dives). For single non-decompression dives < 10 m, the minimum is 12 hours."),
        ("Q2: Which manifestation of Decompression Sickness is characterized by substernal burning chest pain, dry hacking cough, and shortness of breath?",
         "[A] The Bends\n[B] The Creeps\n[C] The Chokes\n[D] The Staggers",
         "CORRECT: [C]. The Chokes is pulmonary DCS caused by gas bubbles occluding the pulmonary microcirculation; it is a life-threatening medical emergency."),
        ("Q3: During which phase of flight is a pilot most susceptible to acute otic barotrauma (ear block)?",
         "[A] Rapid climb after take-off\n[B] Steady high-altitude cruise\n[C] Rapid descent from cruising altitude\n[D] Engine start on the ground",
         "CORRECT: [C]. During descent, ambient pressure rises and the Eustachian tube may collapse shut, preventing pressure equalization in the middle ear."),
        ("Q4: What gas law governs the formation of nitrogen bubbles in blood and joint tissues in Decompression Sickness?",
         "[A] Boyle's Law\n[B] Henry's Law\n[C] Dalton's Law\n[D] Charles' Law",
         "CORRECT: [B]. Henry's law governs the solubility of gases in liquids under varying ambient pressures."),
        ("Q5: What is the most common clinical manifestation of Decompression Sickness in aviation personnel?",
         "[A] The Chokes\n[B] The Bends (joint and deep muscle pain)\n[C] Permanent paralysis\n[D] Cardiac arrest",
         "CORRECT: [B]. The Bends represents ~85% of all DCS cases, causing dull throbbing pain in large joints (knees, elbows, shoulders)."),
        ("Q6: A pilot who is suffering from a head cold flies a sector and experiences excruciating frontal headache during descent. What condition is this?",
         "[A] Aerodontalgia\n[B] Barosinusitis (sinus barotrauma)\n[C] The Staggers\n[D] Hyperventilation syndrome",
         "CORRECT: [B]. Swollen mucous membranes block the sinus ostia, causing negative pressure and intense barosinusitis pain during descent.")
    ]
    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 4 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch01()
    build_ch02()
    build_ch03()
    build_ch04()
