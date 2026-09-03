#!/usr/bin/env python3
"""
Generator for 040 Human Performance & Limitations (HPL)
Chapters 05 to 08:
- Chapter 05: Vision & Visual Illusions in Flight
- Chapter 06: Hearing & The Vestibular System (Spatial Disorientation)
- Chapter 07: Toxic Hazards & Health (CO, Alcohol, Drugs)
- Chapter 08: Information Processing, Perception & Memory

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
# CHAPTER 05: VISION & VISUAL ILLUSIONS IN FLIGHT (~4 pages)
# ==============================================================================
def build_ch05():
    pdf_path = os.path.join(BASE_DIR, "040_ch05_vision_illusions.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 5: Vision & Visual Illusions")
    pdf.add_title_banner("Human Performance", 5, "Vision & Visual Illusions in Flight", "109-158")

    pdf.add_heading_1("1. Functional Anatomy of the Eye")
    pdf.add_paragraph(
        "Vision provides approximately 80% to 90% of all sensory information used by a pilot in flight. "
        "Light enters through the cornea, passes through the pupil (regulated by the iris), is focused by the crystalline "
        "lens (controlled by ciliary muscles during accommodation), and projects an inverted image onto the retina.",
        max_chars=92
    )

    eye_data = [
        ["Cornea", "Refracts light", "Fixed optical element providing ~70% of total refractive power of the eye."],
        ["Crystalline Lens", "Accommodation", "Variable focus. Ciliary muscle contraction relaxes suspensory ligaments, making lens rounder for near vision."],
        ["Fovea Centralis", "Sharp visual acuity", "Small central pit in retina (macula lutea). Contains EXCLUSIVELY CONES (no rods). High-acuity photopic daytime vision."],
        ["Optic Disc", "Blind Spot", "Point where optic nerve exits retina and blood vessels enter. Lacks photoreceptors, creating an anatomical blind spot ~15° temporal."]
    ]
    pdf.add_table(["Anatomical Structure", "Primary Physiological Role", "Aeronautical Significance"], eye_data, col_widths=[125.0, 140.0, 245.0])

    pdf.add_heading_1("2. Photoreceptors: Rods vs Cones (Master Comparison)")
    rods_cones_data = [
        ["Quantity & Distribution", "~6 to 7 million. Concentrated in Fovea Centralis.", "~120 million. Absent in fovea; spread across peripheral retina."],
        ["Lighting Condition", "Photopic Vision (Daylight, bright light).", "Scotopic Vision (Night, low illumination). Mesopic = dusk/dawn."],
        ["Visual Acuity", "Very HIGH acuity (sharp, detailed vision).", "POOR visual acuity; highly sensitive to movement and dim light."],
        ["Color Vision", "Trichromatic: Red, Green, Blue pigments.", "Monochromatic: Black and white / shades of grey only."],
        ["Dark Adaptation Rate", "Fast: Reaches maximum sensitivity in 5-7 min.", "Slow: Rhodopsin (visual purple) requires 30 MINUTES to fully adapt!"]
    ]
    pdf.add_table(["Characteristic", "Cones (Daylight Vision)", "Rods (Night Vision)"], rods_cones_data, col_widths=[130.0, 190.0, 190.0])

    pdf.add_callout(
        "trap",
        "The Night Blind Spot & Off-Center Viewing Technique",
        "• The Night Blind Spot: At night, cones in the fovea centralis become inoperative due to lack of light. "
        "Because there are NO RODS in the fovea, the central 1° to 2° of the visual field is COMPLETELY BLIND at night!\n"
        "• Off-Center Viewing: To detect dim objects or other aircraft at night, the pilot must NEVER look directly at them. "
        "Look 10° to 15° OFF-CENTER so that light falls onto the peripheral retina where rods are dense!",
        max_chars=86
    )

    pdf.add_heading_1("3. Optical Defects & Empty Field Myopia")
    pdf.add_bullet("Myopia (Short-sightedness)", "Eyeball too long or lens too strong. Focal point falls in front of retina. Corrected with CONCAVE lenses (minus diopters).")
    pdf.add_bullet("Hypermetropia (Long-sightedness)", "Eyeball too short. Focal point falls behind retina. Corrected with CONVEX lenses (plus diopters).")
    pdf.add_bullet("Presbyopia", "Aging-related hardening of crystalline lens, reducing accommodation for near vision. Corrected with reading glasses.")
    pdf.add_bullet("Empty Field Myopia (Space Myopia)", "In featureless sky (overcast, haze, darkness), the eye automatically rests at a focal distance of 1 to 2 METERS! Distant aircraft will not be focused. Prevention: Regularly scan distant wingtips or ground features.")

    pdf.add_heading_1("4. Master Runway & Approach Visual Illusions")
    illusions_data = [
        ["Narrow Runway", "Higher than actual", "Pilot perceives aircraft is too high -> flies lower than normal approach -> risks undershooting / landing short."],
        ["Wide Runway", "Lower than actual", "Pilot perceives aircraft is too low -> flies higher approach -> flares too high, risks tailstrike / long landing."],
        ["Upsloping Runway", "Higher than actual", "Upslope gives visual illusion of being too high -> pilot pitches down, flies flatter approach, risks CFIT."],
        ["Downsloping Runway", "Lower than actual", "Downslope gives illusion of being too low -> pilot pitches up, flies steeper approach, lands long."],
        ["Black Hole Approach", "Higher than actual", "Night approach over water/dark terrain with no peripheral cues. Pilot flies dangerously low, curved approach into terrain."]
    ]
    pdf.add_table(["Visual Illusion Condition", "Perceived Aircraft Position", "Pilot Reaction & Flight Safety Hazard"], illusions_data, col_widths=[135.0, 135.0, 240.0])

    pdf.add_callout(
        "definition",
        "Sensory Illusions: Autokinesis & Flicker Vertigo",
        "• Autokinesis: Staring continuously at a single static light in complete darkness causes the light to appear to move "
        "after several seconds due to micro-saccadic eye movements. Prevention: Keep eyes scanning; avoid fixating on a single point.\n"
        "• Flicker Vertigo: Exposure to flashing light (sunlight through rotating propeller or strobe lights) at 4 to 20 Hz "
        "can induce nausea, vomiting, dizziness, loss of consciousness, and epileptic seizures.",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: How long does it take for rod photoreceptors in the human retina to achieve full dark adaptation?",
         "[A] 5 to 7 minutes\n[B] 10 to 15 minutes\n[C] Approximately 30 minutes\n[D] 2 hours",
         "CORRECT: [C]. Cones adapt quickly in 5 to 7 minutes, but rod rhodopsin regeneration requires approximately 30 minutes for complete dark adaptation."),
        ("Q2: What scanning technique should a pilot employ to detect traffic visually at night?",
         "[A] Stare fixedly at the central area where the object is suspected\n[B] Look 10° to 15° off-center and scan peripherally\n[C] Use bright white flashlight inside the cockpit\n[D] Rapidly blink both eyes continuously",
         "CORRECT: [B]. The fovea centralis has no rods and is blind at night (night blind spot). Looking 10° to 15° off-center projects light onto rod-rich peripheral retina."),
        ("Q3: When approaching a runway that is significantly narrower than normal, what visual illusion is created?",
         "[A] Illusion of being lower than actual, causing the pilot to fly a high approach\n[B] Illusion of being higher than actual, causing the pilot to fly a lower approach and risk undershooting\n[C] Illusion of excessive airspeed\n[D] Illusion of bank angle",
         "CORRECT: [B]. A narrow runway subtends a smaller visual angle, leading the pilot to believe they are higher than actual, causing a flatter approach and undershoot risk."),
        ("Q4: What is 'Empty Field Myopia' and what is the typical resting focus distance of the eye in a featureless sky?",
         "[A] Loss of peripheral vision above FL 300\n[B] Accommodation resting at a distance of 1 to 2 meters in the absence of visual focal targets\n[C] Permanent damage caused by UV radiation\n[D] Inability to read cockpit instruments in bright sunlight",
         "CORRECT: [B]. Without focal stimuli, ciliary muscles relax to a resting accommodation distance of approximately 1 to 2 meters (3 to 6 feet)."),
        ("Q5: What optical lens is prescribed to correct myopia (short-sightedness)?",
         "[A] Convex lenses (plus diopters)\n[B] Concave lenses (minus diopters)\n[C] Cylindrical prisms only\n[D] Polarized dark filters",
         "CORRECT: [B]. Myopia focuses light in front of the retina; concave (diverging) lenses move the focal point back onto the retina."),
        ("Q6: How does smoking cigarettes affect a pilot's visual acuity at night?",
         "[A] It improves dark adaptation due to nicotine stimulation\n[B] It has no measurable effect below 10,000 ft\n[C] Carbon monoxide binds to hemoglobin, raising physiological altitude by 4,000-5,000 ft and severely degrading night vision\n[D] It causes immediate temporary color blindness",
         "CORRECT: [C]. Smoking creates 4-8% carboxyhemoglobin, inducing hypoxia in oxygen-hungry retinal rods and significantly degrading night vision even at sea level."),
        ("Q7: What visual illusion does heavy rain on the cockpit windshield produce during final approach?",
         "[A] Creates an illusion of being higher than actual, causing the pilot to pitch down and fly dangerously low\n[B] Creates an illusion of being lower than actual, causing the pilot to fly higher\n[C] Has no effect on perceived glideslope\n[D] Flattens the runway perspective completely",
         "CORRECT: [A]. Water refraction bends light rays downward, making the horizon appear lower and creating the illusion that the aircraft is higher than actual. The pilot tends to fly a flatter, dangerously low approach."),
        ("Q8: Which ocular structure actively changes shape to focus near and far objects during visual accommodation?",
         "[A] The cornea\n[B] The crystalline lens, modulated by the ciliary muscle\n[C] The vitreous humor\n[D] The optic disc",
         "CORRECT: [B]. Contraction and relaxation of the ciliary muscle adjusts the curvature of the crystalline lens to achieve visual focus on near and distant targets.")
    ]
    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 5 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 06: HEARING & THE VESTIBULAR SYSTEM (~4 pages)
# ==============================================================================
def build_ch06():
    pdf_path = os.path.join(BASE_DIR, "040_ch06_hearing_vestibular.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 6: Hearing & Vestibular System")
    pdf.add_title_banner("Human Performance", 6, "Hearing & Vestibular System", "159-204")

    pdf.add_heading_1("1. Anatomy of the Ear: Hearing & Equilibrium")
    pdf.add_paragraph(
        "The human ear performs two completely distinct physiological functions: acoustic perception (hearing) "
        "and vestibular sensing (spatial orientation and equilibrium):",
        max_chars=92
    )

    ear_parts = [
        ["Outer Ear", "Pinna & External Canal", "Collects sound waves and funnels them to the tympanic membrane (eardrum)."],
        ["Middle Ear", "Ossicles (Hammer, Anvil, Stirrup)", "Air-filled cavity. Amplifies mechanical sound vibrations (20:1 ratio) to oval window. Equalized by Eustachian tube."],
        ["Inner Ear (Cochlea)", "Organ of Corti", "Fluid-filled snail-like structure containing hair cells that convert hydraulic pressure waves into neural impulses to cranial nerve VIII."],
        ["Inner Ear (Vestibular)", "Semicircular Canals & Otoliths", "Detects angular acceleration (canals) and linear acceleration / gravity (otoliths)."]
    ]
    pdf.add_table(["Anatomical Region", "Key Structures", "Physiological Function"], ear_parts, col_widths=[115.0, 160.0, 235.0])

    pdf.add_heading_1("2. The Vestibular Apparatus (Canals vs Otoliths)")
    pdf.add_paragraph(
        "The vestibular system is designed exclusively for a terrestrial environment (1G gravity). In three-dimensional "
        "flight, acceleration forces constantly deceive its sensory mechanisms:",
        max_chars=92
    )

    vest_data = [
        ["Semicircular Canals (3 orthogonal planes: roll, pitch, yaw)", "Angular Acceleration (Rotational)", "Endolymph fluid deflects the gelatinous CUPULA. Perception threshold: 0.5° to 2.0°/s^2. In a constant-rate turn, endolymph stabilizes in 10-20 seconds, and the brain senses NO TURN!"],
        ["Otolith Organs (Utricle & Saccule)", "Linear Acceleration & Gravity", "Contains OTOLITHS (calcium carbonate stones) on a sensory gel bed. Linear acceleration pulls otoliths rearward, creating an identical sensory signal to head pitch up!"]
    ]
    pdf.add_table(["Vestibular Organ", "Sensed Movement Type", "Biophysical Mechanism & Limitations"], vest_data, col_widths=[140.0, 140.0, 230.0])

    pdf.add_heading_1("3. Master Flight Vestibular Illusions (Spatial Disorientation)")
    illusions_vest = [
        ["The Leans", "Most common illusion", "An unnoticed roll (< 2°/s) is followed by a rapid wings-level correction. The pilot feels a strong roll in the opposite direction and leans body into turn."],
        ["Somatogravic Illusion", "Rapid acceleration on take-off / go-around", "Inertia displaces otoliths backward. The brain perceives a steep NOSE-UP pitch. The pilot pushes the stick forward into the ground (CFIT risk)."],
        ["Graveyard Spin", "Prolonged spin recovery", "After 15-20 s of spinning, canals adapt (feeling stops). Applying opposite rudder to recover deflects cupula, creating the illusion of spinning in the opposite direction; pilot re-enters original spin!"],
        ["Graveyard Spiral", "Descending coordinated spiral", "Canals adapt to turn. Pilot senses wings level, sees altitude loss on altimeter, pulls back on elevator, tightening the spiral dive!"],
        ["Coriolis Illusion", "Head movement in steady turn", "Tilting head in a different plane during a turn stimulates two canals simultaneously, creating a violent, tumbling sensation of uncontrolled pitch/roll/yaw."]
    ]
    pdf.add_table(["Vestibular Illusion", "Triggering Flight Condition", "Physiological Mechanism & Flight Danger"], illusions_vest, col_widths=[120.0, 145.0, 245.0])

    pdf.add_callout(
        "trap",
        "The Golden Rule for Overcoming Spatial Disorientation",
        "When experiencing spatial disorientation or conflict between bodily sensations and flight instruments:\n"
        "1. NEVER TRUST YOUR 'SEAT-OF-THE-PANTS' SENSATIONS!\n"
        "2. BELIEVE YOUR FLIGHT INSTRUMENTS 100% (Attitude Indicator, Altimeter, VSI, Turn Coordinator);\n"
        "3. Suppress all head movements (avoids Coriolis illusion);\n"
        "4. If available, transfer aircraft control to the other pilot or engage the autopilot.",
        max_chars=86
    )

    pdf.add_heading_1("4. Noise Exposure, Hearing Loss & Motion Sickness")
    pdf.add_bullet("Decibel Scale (Logarithmic)", "Every 3 dB increase DOUBLES sound energy. Permissible continuous exposure without protection is 85 dB for 8 hours (88 dB for 4h, 91 dB for 2h). Pain threshold: 140 dB.")
    pdf.add_bullet("Sensorineural Hearing Loss (NIHL)", "Irreversible destruction of cochlear hair cells caused by chronic noise exposure. Characterized by a distinctive acoustic notch at 4,000 Hz!")
    pdf.add_bullet("Motion Sickness (Kinetosis)", "Triggered by sensory conflict (mismatch) between visual, vestibular, and proprioceptive inputs (e.g. eyes see static cockpit while inner ear senses turbulent roll/pitch).")

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: What is the primary cause of the Somatogravic Illusion during a night or instrument take-off?",
         "[A] Semicircular canal fluid drying out\n[B] Linear acceleration displacing otoliths backward, which the brain interprets as a steep pitch-up\n[C] Rapid change in cabin pressure on climb\n[D] High positive G-forces draining blood from the brain",
         "CORRECT: [B]. Forward linear acceleration moves otolithic stones backward, identical to backward head tilt (pitch up). The pilot falsely pushes nose down."),
        ("Q2: In a prolonged coordinated turn lasting more than 20 seconds, what sensation do the semicircular canals transmit to the brain?",
         "[A] A violent tumbling sensation\n[B] A feeling of constant roll at 45°\n[C] Sensation that the turn has stopped and the aircraft is flying straight and level\n[D] Severe vertigo",
         "CORRECT: [C]. After 10 to 20 seconds of constant angular velocity, endolymph fluid matches canal rotation speed; the cupula returns to neutral (sensing zero turn)."),
        ("Q3: Which sensory illusion is triggered by moving the head out of the plane of rotation while the aircraft is in a steady turn?",
         "[A] Somatogravic illusion\n[B] Coriolis illusion\n[C] Autokinesis\n[D] The Leans",
         "CORRECT: [B]. The Coriolis illusion occurs when head movement stimulates two semicircular canals simultaneously during a turn, creating an overwhelming tumbling sensation."),
        ("Q4: What is 'The Leans' in aviation spatial disorientation?",
         "[A] An otolith illusion occurring only during landing flare\n[B] A false sensation of roll following an undetected slow roll and rapid wings-level correction, prompting the pilot to lean\n[C] Severe neck muscle spasms caused by G-forces\n[D] A vestibular symptom of carbon monoxide poisoning",
         "CORRECT: [B]. Rolling slowly below threshold (< 2°/s) and abruptly returning to level stimulates the cupula in reverse, making the pilot feel tilted and lean to compensate."),
        ("Q5: Noise-induced hearing loss (NIHL) is characterized by an initial hearing deficit at which frequency?",
         "[A] 500 Hz\n[B] 1,000 Hz\n[C] 4,000 Hz\n[D] 12,000 Hz",
         "CORRECT: [C]. Acoustic trauma and chronic noise exposure characteristically damage cochlear hair cells at the 4,000 Hz notch first."),
        ("Q6: What is the most effective immediate countermeasure when a pilot experiences spatial disorientation in IMC?",
         "[A] Close eyes and shake head vigorously\n[B] Disregard bodily sensations completely and fly strictly by reference to the primary flight instruments\n[C] Look out of the window for ground references\n[D] Perform a 360° turn to reset the vestibular canals",
         "CORRECT: [B]. Spatial disorientation is overcome solely by suppressing vestibular cues and strictly believing the flight instruments."),
        ("Q7: What is the underlying physiological mechanism of motion sickness (kinetosis) in flight?",
         "[A] Severe hypoxia in the cochlea\n[B] A sensory mismatch between visual cues, vestibular signals, and proprioceptive receptors\n[C] Sudden decrease in blood sugar level\n[D] Decompression of the middle ear cavity",
         "CORRECT: [B]. The sensory mismatch theory explains motion sickness as an evolutionary defense triggered when the brain receives contradictory movement signals from eyes and ears."),
        ("Q8: Why are the Otolith Organs (Utricle and Saccule) physically incapable of distinguishing between linear acceleration and backward head tilt?",
         "[A] They lack blood supply during acceleration\n[B] Inertial force from forward acceleration displaces the otoliths backwards in the exact same manner as gravitational pull during head pitch-up\n[C] They only respond to sound waves above 1,000 Hz\n[D] They are deactivated above 10,000 ft",
         "CORRECT: [B]. Forward acceleration creates an inertial reaction vector that shifts the otolith mass backward, perfectly mimicking a nose-up attitude.")
    ]
    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 6 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 07: TOXIC HAZARDS & PILOT HEALTH (~4 pages)
# ==============================================================================
def build_ch07():
    pdf_path = os.path.join(BASE_DIR, "040_ch07_toxic_hazards_health.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 7: Toxic Hazards & Health")
    pdf.add_title_banner("Human Performance", 7, "Toxic Hazards & Pilot Health", "205-236")

    pdf.add_heading_1("1. Carbon Monoxide (CO) Poisoning in Aviation")
    pdf.add_paragraph(
        "Carbon Monoxide is a colorless, odorless, tasteless, non-irritating toxic gas produced by incomplete hydrocarbon combustion. "
        "In light aircraft, exhaust gas shroud heaters are the most common source of in-flight CO leaks:",
        max_chars=92
    )

    pdf.add_bullet("Hemoglobin Affinity", "CO binds to hemoglobin with an affinity 200 to 250 TIMES GREATER than oxygen, forming Carboxyhemoglobin (COHb).")
    pdf.add_bullet("Mechanism of Hypoxia", "CO produces both ANEMIC HYPOXIA (reduces O2 capacity) and HISTOTOXIC HYPOXIA (blocks cellular cytochromes). Additionally, it shifts the O2 dissociation curve to the LEFT, locking remaining oxygen onto hemoglobin!")
    pdf.add_bullet("Clinical Symptoms", "Initial: Dull frontal headache, sluggishness, loss of concentration. Intermediate: Throbbing temporal headache, dizziness, nausea, impaired motor coordination. Late: Confusion, cherry-red skin/lips (usually post-mortem), convulsions, coma, death.")
    pdf.add_bullet("In-Flight Treatment", "1) Turn cabin heat OFF immediately; 2) Open 100% fresh air vents; 3) Don oxygen mask with 100% O2 under positive pressure; 4) Land at nearest suitable aerodrome.")

    pdf.add_heading_1("2. Alcohol (Ethanol) & Aeromedical Regulations")
    pdf.add_paragraph(
        "Alcohol is a powerful central nervous system (CNS) depressant. It is rapidly absorbed in the stomach and small intestine, "
        "and metabolized in the liver by alcohol dehydrogenase at a CONSTANT RATE of ~10 to 15 mg% (0.010% to 0.015%) per hour.",
        max_chars=92
    )

    pdf.add_callout(
        "trap",
        "EASA Blood Alcohol Limits & The 'Bottle-to-Throttle' Rule",
        "Under EASA Part-CAT and Part-MED regulations:\n"
        "• Maximum Legal Blood Alcohol Concentration (BAC): 0.20 g/l (0.02% or 20 mg/100 ml). Absolute zero is strongly recommended.\n"
        "• Bottle-to-Throttle Rule: Minimum 8 HOURS between the consumption of any alcohol and reporting for flight duty.\n"
        "• Post-Alcohol Effects (Hangover): A pilot is UNFIT to fly even when BAC reaches 0.00% if fatigue, dehydration, or headache persists. Alcohol alters endolymph density in the inner ear for up to 24-48 hours, inducing Positional Alcohol Nystagmus (PAN) and extreme vertigo!",
        max_chars=86
    )

    pdf.add_heading_1("3. Medications & Flying Restrictions")
    med_data = [
        ["Antihistamines", "Allergies, motion sickness", "STRICTLY DISQUALIFYING. Induce profound sedation, drowsiness, and degraded cognitive reaction times."],
        ["Antibiotics", "Bacterial infections", "PILOT GROUNDED. Disqualification is based both on the drug's side effects (nausea, diarrhea) and the underlying infectious illness."],
        ["Analgesics (Painkillers)", "Headache, muscle ache", "Mild analgesics (Paracetamol, Aspirin) are acceptable in small doses. Strong analgesics containing CODEINE, opioids, or sedatives are PROHIBITED."],
        ["Decongestants", "Nasal congestion", "Oral/nasal pseudoephedrine may cause palpitations, nervousness, and rebound congestion; masking ear block risks."],
        ["Antidepressants & Sedatives", "Depression, insomnia", "Benzodiazepines, sleeping pills, and unapproved SSRIs are STRICTLY DISQUALIFYING."]
    ]
    pdf.add_table(["Medication Category", "Common Usage", "Aeromedical Flying Privilege Status"], med_data, col_widths=[130.0, 130.0, 250.0])

    pdf.add_heading_1("4. Food Hygiene & Crew Meal Separation")
    pdf.add_paragraph(
        "Gastrointestinal illness and food poisoning (e.g. Salmonella, Staphylococcal enterotoxin) represent a severe hazard "
        "for single-pilot incapacitation. In commercial multi-pilot airline operations, airline Standard Operating Procedures (SOPs) "
        "strictly mandate that the Captain and First Officer MUST eat DIFFERENT meals prepared from different kitchens or food sources, "
        "served at different times before and during flight.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: Why is Carbon Monoxide (CO) particularly dangerous in aviation?",
         "[A] It has an irritating smell that causes coughing\n[B] It is odorless, colorless, and binds to hemoglobin with ~250 times greater affinity than oxygen\n[C] It causes immediate lung rupture\n[D] It only affects flights above FL 400",
         "CORRECT: [B]. CO is insidious (odorless, tasteless) and binds strongly to hemoglobin, depriving tissues of oxygen (anemic and histotoxic hypoxia)."),
        ("Q2: What is the maximum permitted blood alcohol concentration (BAC) for flight crew under EASA regulations?",
         "[A] 0.50 g/l (0.05%)\n[B] 0.80 g/l (0.08%)\n[C] 0.20 g/l (0.02%)\n[D] 0.00 g/l with no tolerance",
         "CORRECT: [C]. EASA Part-MED / Part-CAT specifies a legal upper limit of 0.20 g/l (0.02%), although zero tolerance is operational policy."),
        ("Q3: What is the minimum recommended 'bottle-to-throttle' time interval between drinking alcohol and flight duty?",
         "[A] 4 hours\n[B] 8 hours\n[C] 12 hours\n[D] 24 hours",
         "CORRECT: [B]. 8 hours is the mandatory minimum time interval between alcohol consumption and flight duty."),
        ("Q4: Can the metabolic rate of alcohol elimination in the human liver be accelerated by drinking black coffee or exercising?",
         "[A] Yes, coffee speeds up liver enzymes by 50%\n[B] Yes, heavy sweating eliminates alcohol through pores\n[C] NO, alcohol metabolism proceeds at a fixed rate of ~10-15 mg/100 ml per hour and cannot be accelerated\n[D] Yes, with pure oxygen therapy",
         "CORRECT: [C]. Hepatic oxidation of ethanol by alcohol dehydrogenase is zero-order (constant rate) and cannot be accelerated."),
        ("Q5: What is the primary aeromedical hazard of taking over-the-counter antihistamines before flying?",
         "[A] High risk of blood clotting\n[B] Sedation, drowsiness, and impaired psychomotor reaction time\n[C] Eye pupil constriction\n[D] Hypertension",
         "CORRECT: [B]. Classic antihistamines cross the blood-brain barrier and cause marked sedation, slowing reaction times and inducing sleepiness."),
        ("Q6: Why must the Pilot-in-Command and the Co-pilot consume different meals on a commercial flight?",
         "[A] Airline budget optimization\n[B] To prevent simultaneous food poisoning incapacitating both pilots\n[C] Personal preference of senior captain\n[D] Union dietary contracts",
         "CORRECT: [B]. Consuming different meals prepared from different sources prevents dual crew incapacitation from food contamination.")
    ]
    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 7 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 08: INFORMATION PROCESSING, PERCEPTION & MEMORY (~4 pages)
# ==============================================================================
def build_ch08():
    pdf_path = os.path.join(BASE_DIR, "040_ch08_information_processing_memory.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 8: Information Processing & Memory")
    pdf.add_title_banner("Human Performance", 8, "Information Processing & Memory", "237-278")

    pdf.add_heading_1("1. The Human Information Processing Model")
    pdf.add_paragraph(
        "Human cognition in the cockpit operates as an open-loop information system (Wickens' Model): "
        "Sensory Inputs (Vision, Hearing, Proprioception) -> Sensory Memory Store -> Selective Attention & Perception -> "
        "Working Memory & Decision Making -> Motor Action (Effector Organs) -> Environmental Feedback.",
        max_chars=92
    )

    pdf.add_bullet("Sensory Memory Store", "Ultra-short duration: Iconic (visual) store lasts ~0.5 seconds; Echoic (auditory) store lasts ~2 to 4 seconds. Holds raw, unfiltered physical stimuli.")
    pdf.add_bullet("Perception", "The process of interpreting sensory signals by comparing them with past mental models stored in long-term memory. Vulnerable to cognitive expectations and confirmation bias.")
    pdf.add_bullet("Cognitive Bottleneck", "Human conscious processing is SINGLE-CHANNEL and capacity-limited. Simultaneous conscious tasks compete for central cognitive resources, causing channel overload.")

    pdf.add_heading_1("2. Human Memory Architecture (Working vs Long-Term)")
    mem_data = [
        ["Working Memory (Short-Term Memory)", "Capacity: 7 ± 2 items (Miller's Law). Duration: 10 to 20 seconds without rehearsal.", "Highly vulnerable to disruption and cognitive distraction. Rehearsal and chunking (e.g. transponder code '7-5-0-0' as one chunk) expand functional capacity."],
        ["Long-Term Memory: Semantic", "Facts, concepts, rules, language, airspace classes.", "Deeply encoded, organized into mental schema / neural networks. Resilient to decay."],
        ["Long-Term Memory: Episodic", "Personal experiences, specific past flight events.", "Context-dependent memory of past flights, near misses, and simulator training."],
        ["Long-Term Memory: Procedural", "Motor flight skills, crosswind landings, scans.", "Automated 'motor programs'. Executed with minimal conscious attention. Can revert under acute stress!"]
    ]
    pdf.add_table(["Memory System", "Capacity, Duration & Storage Characteristics", "Operational Application & Cockpit Vulnerability"], mem_data, col_widths=[125.0, 160.0, 225.0])

    pdf.add_callout(
        "trap",
        "Miller's Magical Number 7 ± 2 and Cockpit Chunking",
        "• Working Memory Capacity: George Miller demonstrated that human working memory can hold between 5 and 9 items (7 ± 2) simultaneously.\n"
        "• Chunking: Grouping individual pieces of data into meaningful units. For example, the instruction 'Maintain FL 350, heading 240, speed 280 kt, squawk 4215' "
        "contains 13 individual digits. Unchunked, it exceeds working memory capacity. Experienced pilots chunk it into 4 operational concepts, enabling accurate retention!",
        max_chars=86
    )

    pdf.add_heading_1("3. Attention Mechanisms & Cognitive Tunneling")
    pdf.add_paragraph(
        "Attention is the active cognitive mechanism that directs conscious mental processing to selected stimuli:",
        max_chars=92
    )
    pdf.add_bullet("Selective Attention", "Directing focus to one source of information while filtering out irrelevant background noise (e.g. listening to own callsign on busy ATC frequency - 'cocktail party effect').")
    pdf.add_bullet("Divided Attention (Time-Sharing)", "Rapidly switching attention across multiple operational tasks (e.g. instrument cross-check scan: Attitude -> Speed -> Altitude -> Heading). True simultaneous conscious processing is an illusion.")
    pdf.add_bullet("Cognitive Tunneling (Channelized Attention)", "Under high stress, anxiety, or high workload, attention narrows onto one single indicator or problem, completely blinding the pilot to other critical alarms (e.g. Eastern Airlines 401 crash while fixing a landing gear light bulb).")

    pdf.add_heading_1("4. Motor Programs & Negative Habit Transfer")
    pdf.add_paragraph(
        "With practice, flight actions become automated motor programs. This frees working memory for strategic decision-making. "
        "However, when transitioning between different aircraft types (e.g. from conventional control yoke to sidestick, or clockwise to counterclockwise switches), "
        "pilots under stress frequently suffer from NEGATIVE TRANSFER: the unconscious regression to motor habits from the previously flown aircraft type.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: What is the capacity and typical retention duration of human working (short-term) memory without active rehearsal?",
         "[A] Unlimited capacity, lasting several hours\n[B] 7 ± 2 chunks of information, lasting approximately 10 to 20 seconds\n[C] Exactly 3 items, lasting 5 minutes\n[D] 15 items, lasting 1 hour",
         "CORRECT: [B]. Miller's Law established that short-term memory holds 7 ± 2 chunks of information with a decay time of 10 to 20 seconds without rehearsal."),
        ("Q2: In aviation psychology, what is 'chunking' in working memory?",
         "[A] Forgetting unimportant flight data\n[B] Grouping individual data items into larger, meaningful operational units to expand working memory capacity\n[C] Memorizing checklists by rote\n[D] Visualizing aerodynamic airflow",
         "CORRECT: [B]. Chunking aggregates discrete pieces of information into cohesive units, effectively multiplying the storage capability of working memory."),
        ("Q3: What cognitive phenomenon describes a pilot focusing exclusively on a burnt-out landing gear bulb while ignoring an autopilot disconnect and terrain alert?",
         "[A] Sensory adaptation\n[B] Cognitive tunneling (perceptual tunneling / channelized attention)\n[C] Episodic retrieval\n[D] Empty field myopia",
         "CORRECT: [B]. Cognitive tunneling occurs when high stress or fascination causes attentional narrowing onto one problem, ignoring peripheral critical cues."),
        ("Q4: Which memory system stores automated motor flying skills, such as cycling rudder pedals during a crosswind landing?",
         "[A] Semantic memory\n[B] Episodic memory\n[C] Procedural memory\n[D] Echoic memory",
         "CORRECT: [C]. Procedural memory stores automated physical skills and motor programs that operate largely outside conscious working memory."),
        ("Q5: What is 'Negative Habit Transfer' during aircraft type transition?",
         "[A] The inability to learn new procedures\n[B] The unconscious reversion to motor actions or procedures from a previous aircraft type under stress\n[C] Disliking a new cockpit layout\n[D] Forgetting radio phraseology",
         "CORRECT: [B]. Negative transfer occurs when previously ingrained motor habits override newly acquired procedures during moments of high workload or stress."),
        ("Q6: How long does raw auditory information remain in the human echoic sensory store?",
         "[A] 0.1 seconds\n[B] 2 to 4 seconds\n[C] 30 seconds\n[D] Several minutes",
         "CORRECT: [B]. Echoic (auditory) sensory store retains sounds for 2 to 4 seconds, allowing the brain to process spoken ATC clearances just heard.")
    ]
    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 8 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch05()
    build_ch06()
    build_ch07()
    build_ch08()
