#!/usr/bin/env python3
"""
Generator for 040 Human Performance & Limitations (HPL)
Chapters 09 to 13:
- Chapter 09: Human Error & Reliability (SHELL, Reason's Swiss Cheese)
- Chapter 10: Decision Making & Judgement (DECIDE, Situational Awareness)
- Chapter 11: Stress & Workload (Yerkes-Dodson, GAS)
- Chapter 12: Fatigue, Sleep & Circadian Rhythms (WOCL, Sleep Architecture)
- Chapter 13: Communication, CRM & Cockpit Teamwork (Authority Gradient, PACE)

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
# CHAPTER 09: HUMAN ERROR & RELIABILITY (~4 pages)
# ==============================================================================
def build_ch09():
    pdf_path = os.path.join(BASE_DIR, "040_ch09_human_error_reliability.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 9: Human Error & Reliability")
    pdf.add_title_banner("Human Performance", 9, "Human Error & Reliability Models", "279-318")

    pdf.add_heading_1("1. Human Error Taxonomies: Rasmussen's SRK Model")
    pdf.add_paragraph(
        "Jens Rasmussen classified human cognitive behavior and associated error mechanisms into three distinct levels:",
        max_chars=92
    )

    srk_data = [
        ["Skill-Based (SB)", "Automated sensory-motor performance (flying manual approach, checklist scanning).", "SLIPS (action execution failure - unintended switch selection) and LAPSES (memory failure - skipped checklist item due to distraction). Occurs in familiar, practiced routines."],
        ["Rule-Based (RB)", "Applying established IF-THEN procedures, rules, or checklists to a known problem.", "RULE-BASED MISTAKES: Selecting the wrong rule, or correctly applying a bad/flawed rule. High confidence, but incorrect diagnosis of situation."],
        ["Knowledge-Based (KB)", "Novel, unfamiliar emergency scenarios with no pre-existing rule or SOP (unprecedented crisis).", "KNOWLEDGE-BASED MISTAKES: Incomplete or incorrect mental model of the system. Highest mental workload and cognitive effort. High probability of error."]
    ]
    pdf.add_table(["Performance Level", "Cognitive Nature & Cockpit Context", "Characteristic Error Mechanisms"], srk_data, col_widths=[115.0, 165.0, 230.0])

    pdf.add_heading_1("2. Errors vs Violations (Intentionality Spectrum)")
    pdf.add_bullet("Human Error", "Unintentional deviation. The planned action fails to achieve the desired outcome (Slips, Lapses, Mistakes). Non-punitive under Just Culture.")
    pdf.add_bullet("Routine Violation", "Deliberate shortcutting of SOPs commonly condoned by peer group or company culture (e.g. not calling for official checklist, speeding on taxiways).")
    pdf.add_bullet("Situational Violation", "Deliberate rule infringement driven by commercial pressure, poor equipment, or time deficit ('getting the job done').")
    pdf.add_bullet("Exceptional Violation", "One-off isolated violation occurring in an unprecedented emergency to save life or aircraft.")

    pdf.add_heading_1("3. James Reason's Swiss Cheese Model (Defenses-in-Depth)")
    pdf.add_paragraph(
        "Catastrophes in complex sociotechnical systems never result from a single isolated human error. They occur when "
        "defensive barriers across multiple organizational and operational layers breach simultaneously:",
        max_chars=92
    )

    cheese_data = [
        ["Organizational Influences", "Latent Conditions", "Corporate cost-cutting, inadequate training budget, flawed rostering, unrealistic flight schedules."],
        ["Unsafe Supervision", "Latent Conditions", "Tolerating known SOP non-compliance, inadequate flight crew pairing, failure to address maintenance reports."],
        ["Preconditions for Unsafe Acts", "Latent / Hybrid", "Crew fatigue, high workload, emotional stress, poor cockpit ergonomic layout, confusing checklists."],
        ["Unsafe Acts (Active Failures)", "Active Failures", "Immediate operational errors committed by front-line personnel (pilots, ATCOs): pilot flies below MDA, misses readback error."]
    ]
    pdf.add_table(["Barrier / Cheese Layer", "Failure Nature", "Aeronautical Manifestation & Trigger Mechanism"], cheese_data, col_widths=[140.0, 110.0, 260.0])

    pdf.add_callout(
        "trap",
        "Latent Conditions vs Active Failures (AviationExam Absolute Core)",
        "• Latent Conditions: Decisions made by management, regulators, designers, or maintainers that lie DORMANT in the system "
        "for months or years without causing harm, until triggered by operational circumstances.\n"
        "• Active Failures: Unsafe acts committed by operational personnel at the sharp end (pilots, controllers) whose consequences "
        "are felt ALMOST IMMEDIATELY.",
        max_chars=86
    )

    pdf.add_heading_1("4. The SHELL Model & Threat and Error Management (TEM)")
    pdf.add_paragraph(
        "• SHELL Model (Hawkins / Edwards): Software (rules, SOPs, manuals), Hardware (airframe, cockpit displays), "
        "Environment (weather, night, noise), Liveware (the human operator at the center, interacting with Liveware-Others - crew, ATC).\n"
        "• Threat and Error Management (TEM): A proactive operational framework dividing operations into Threats (environmental/technical), "
        "Errors (crew deviations), and Undesired Aircraft States (UAS - deviations requiring immediate recovery before an accident occurs).",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch09 = [
        ("Q1: According to Jens Rasmussen's SRK model, a pilot who inadvertently operates the landing gear switch instead of the flap switch is committing what type of error?",
         "[A] A rule-based mistake\n[B] A knowledge-based mistake\n[C] A skill-based slip of action\n[D] An exceptional violation",
         "CORRECT: [C]. Operating the wrong control in a familiar automated motor routine is a classic slip of action (skill-based level)."),
        ("Q2: In James Reason's Swiss Cheese model, what distinguishes a 'latent condition' from an 'active failure'?",
         "[A] Latent conditions always cause instant crashes\n[B] Active failures are organizational; latent conditions are individual\n[C] Latent conditions are dormant systemic defects created by management or design, whereas active failures are immediate unsafe acts committed by front-line operators\n[D] Latent conditions only apply to maintenance",
         "CORRECT: [C]. Latent conditions exist dormant within the system (rostering, training, SOP design), triggered into an accident by an active front-line operator failure."),
        ("Q3: In the SHELL model of human factors, what is positioned at the central core of the system?",
         "[A] Hardware (the aircraft avionics)\n[B] Software (the operating procedures and regulations)\n[C] Liveware (the human being)\n[D] Environment (the atmospheric weather)",
         "CORRECT: [C]. Liveware (the human operator) sits at the center, interacting with Software, Hardware, Environment, and other Liveware."),
        ("Q4: A flight crew deliberately decides to omit a mandatory before-landing checklist to expedite approach due to tight turnaround time. How is this classified?",
         "[A] An involuntary lapse\n[B] A situational / routine violation\n[C] A skill-based slip\n[D] A knowledge-based error",
         "CORRECT: [B]. A conscious, intentional departure from published rules under time or operational pressure is classified as a violation."),
        ("Q5: Under Threat and Error Management (TEM), what is an 'Undesired Aircraft State' (UAS)?",
         "[A] An airline undergoing bankruptcy\n[B] An aircraft configuration or position deviation caused by an unmanaged error, which reduces safety margins\n[C] A bird strike during take-off\n[D] Moderate clear air turbulence",
         "CORRECT: [B]. A UAS is an operational deviation (e.g. unstable approach, wrong altitude) that must be recovered immediately to prevent an accident."),
        ("Q6: At which cognitive performance level does human conscious mental workload reach its maximum and have the highest likelihood of error?",
         "[A] Skill-based level\n[B] Rule-based level\n[C] Knowledge-based level\n[D] Automated reflex level",
         "CORRECT: [C]. The knowledge-based level requires deep analytical problem solving in novel emergency scenarios, placing extreme demands on working memory.")
    ]
    for q_text, opts, exp in questions_ch09:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 9 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 10: DECISION MAKING & JUDGEMENT IN AVIATION (~4 pages)
# ==============================================================================
def build_ch10():
    pdf_path = os.path.join(BASE_DIR, "040_ch10_decision_making_judgement.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 10: Decision Making & Judgement")
    pdf.add_title_banner("Human Performance", 10, "Aeronautical Decision Making", "319-354")

    pdf.add_heading_1("1. Aeronautical Decision Making (ADM) & DECIDE Model")
    pdf.add_paragraph(
        "Aeronautical Decision Making (ADM) is the systematic, structured mental process used by flight crews to consistently "
        "determine the safest course of action in response to changing flight circumstances. The standardized FAA/EASA model is DECIDE:",
        max_chars=92
    )

    decide_data = [
        ["D - Detect", "Detect the change", "Notice that a change in aircraft status, weather, fuel, or operational environment has occurred."],
        ["E - Estimate", "Estimate the significance", "Assess the operational significance and urgency of the problem for flight safety."],
        ["C - Choose", "Choose the desired outcome", "Define the safe operational objective (e.g. divert to alternate aerodrome)."],
        ["I - Identify", "Identify options & actions", "Determine actionable solutions to achieve the chosen outcome."],
        ["D - Do", "Do the necessary action", "Execute the selected solution decisively using CRM and checklist procedures."],
        ["E - Evaluate", "Evaluate the outcome", "Monitor and review whether the chosen action is solving the problem or requires revision."]
    ]
    pdf.add_table(["DECIDE Step", "Operational Action", "Flight Deck Application"], decide_data, col_widths=[105.0, 150.0, 255.0])

    pdf.add_heading_1("2. Situational Awareness (Endsley's 3-Level Model)")
    pdf.add_paragraph(
        "Situational Awareness (SA) is having an accurate, dynamic mental model of the flight environment. "
        "Mica Endsley defined three hierarchical levels:",
        max_chars=92
    )
    pdf.add_bullet("Level 1: Perception", "Perceiving the status, attributes, and dynamics of elements in the cockpit and environment (seeing altimeter reading, hearing ATC clearance, noticing warning lights). Loss of Level 1 accounts for ~76% of SA errors!")
    pdf.add_bullet("Level 2: Comprehension", "Integrating and synthesizing sensory data to understand what it means in relation to operational goals (e.g. realizing fuel burn is higher than planned due to headwinds).")
    pdf.add_bullet("Level 3: Projection", "The highest level: projecting the future status and trajectory of the aircraft (predicting that the flight will arrive below final reserve fuel if no diversion is initiated).")

    pdf.add_heading_1("3. Master Cognitive Biases & 'Get-There-Itis'")
    pdf.add_bullet("Confirmation Bias", "The human tendency to seek, notice, and overvalue information that confirms pre-existing beliefs, while ignoring contradictory evidence (e.g. noticing one clearing sky patch while ignoring severe thunderstorm radar returns).")
    pdf.add_bullet("Plan Continuation Bias ('Get-There-Itis')", "Unconscious cognitive lock-in to complete a planned flight or landing despite deteriorating weather, marginal fuel, or unstable approach parameters.")
    pdf.add_bullet("Availability Heuristic", "Judging the probability of an event by how readily vivid past occurrences come to mind.")
    pdf.add_bullet("Sunk Cost Fallacy", "Justifying continuing a compromised flight because substantial effort, time, and fuel have already been expended.")

    pdf.add_heading_1("4. The Five Hazardous Attitudes & Antidotes (FAA / EASA)")
    hazards_data = [
        ["1. Anti-Authority ('Don't tell me!')", "Resents rules, regulations, and ATC instructions.", "'Follow the rules; they are usually right.'"],
        ["2. Impulsivity ('Do something quickly!')", "Acts instantly without thinking or assessing options.", "'Not so fast. Think first.'"],
        ["3. Invulnerability ('It won't happen to me!')", "Believes accidents only happen to others; takes risks.", "'It could happen to me.'"],
        ["4. Macho ('I can do it / Watch this!')", "Takes unnecessary risks to impress others or prove superiority.", "'Taking chances is foolish.'"],
        ["5. Resignation ('What's the use?')", "Feels helpless; abdicates control to luck or circumstances.", "'I am not helpless. I can make a difference.'"]
    ]
    pdf.add_table(["Hazardous Attitude", "Typical Pilot Thought Pattern", "Mandatory Mental Antidote"], hazards_data, col_widths=[140.0, 200.0, 170.0])

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch10 = [
        ("Q1: In Mica Endsley's model of Situational Awareness, what represents Level 3 SA?",
         "[A] Reading the altimeter accurately\n[B] Comprehending the fuel flow rate\n[C] Projecting the future status and position of the aircraft in time and space\n[D] Executing a missed approach",
         "CORRECT: [C]. Level 1 is Perception; Level 2 is Comprehension; Level 3 is Projection of future status."),
        ("Q2: What psychological bias describes a pilot who continues an unstable visual approach in thick fog because 'the flight has come this far'?",
         "[A] Sensory adaptation\n[B] Plan continuation bias ('get-there-itis')\n[C] The Leans\n[D] Hyperventilation syndrome",
         "CORRECT: [B]. Plan continuation bias is the unconscious tendency to adhere to an original flight plan despite evidence showing it is no longer safe."),
        ("Q3: What is the mental antidote for the hazardous attitude 'Anti-Authority' ('Don't tell me what to do!')?",
         "[A] 'Not so fast. Think first.'\n[B] 'Follow the rules. They are usually right.'\n[C] 'It could happen to me.'\n[D] 'Taking chances is foolish.'",
         "CORRECT: [B]. The antidote for Anti-Authority is 'Follow the rules. They are usually right.'"),
        ("Q4: Which step in the DECIDE aeronautical decision-making model involves evaluating whether the chosen course of action has solved the problem?",
         "[A] Detect\n[B] Choose\n[C] Do\n[D] Evaluate",
         "CORRECT: [D]. Evaluate is the 6th and final step: closing the loop by assessing the actual consequences of the action."),
        ("Q5: What is 'Confirmation Bias' in flight deck operations?",
         "[A] Always confirming ATC clearances on the radio\n[B] Seeking only clues that support one's desired hypothesis while dismissing contradictory safety warnings\n[C] Agreeing with the captain out of politeness\n[D] Performing duplicate checklist verification",
         "CORRECT: [B]. Confirmation bias leads pilots to filter out warning signs that contradict their preconceived mental model."),
        ("Q6: The hazardous attitude 'Resignation' is characterized by which pilot mindset?",
         "[A] Believing rules do not apply to them\n[B] Believing that whatever happens is out of their control and leaving the outcome to fate\n[C] Rushing into actions without evaluating consequences\n[D] Showing off flying skills",
         "CORRECT: [B]. Resignation occurs when a pilot abdicates responsibility, believing 'what's the use, it's out of my hands.' Antidote: 'I can make a difference.'")
    ]
    for q_text, opts, exp in questions_ch10:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 10 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 11: STRESS & WORKLOAD (~4 pages)
# ==============================================================================
def build_ch11():
    pdf_path = os.path.join(BASE_DIR, "040_ch11_stress_workload.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 11: Stress & Workload Management")
    pdf.add_title_banner("Human Performance", 11, "Stress & Workload Management", "355-392")

    pdf.add_heading_1("1. Arousal & The Yerkes-Dodson Law (Inverted-U Curve)")
    pdf.add_paragraph(
        "Human performance varies non-linearly with the level of psychological and physiological arousal (the Yerkes-Dodson Law):",
        max_chars=92
    )

    arousal_data = [
        ["Hypo-Arousal (Underload / Boredom)", "Low stress, low stimulation (long cruise at night).", "Inattention, sluggish reaction time, sleepiness, complacency, high error rate."],
        ["Optimum Arousal (Peak Performance)", "Moderate stress, challenging but manageable workload.", "MAXIMUM cognitive performance, sharp sensory perception, flexible reasoning, optimal situational awareness."],
        ["Hyper-Arousal (Overload / Panic)", "Extreme acute stress, severe emergency, sensory overload.", "Catastrophic breakdown in performance, cognitive tunneling, motor regression, paralysis of action ('freezing')."]
    ]
    pdf.add_table(["Arousal State", "Cockpit Environmental Conditions", "Performance & Cognitive Characteristics"], arousal_data, col_widths=[140.0, 160.0, 210.0])

    pdf.add_heading_1("2. Hans Selye's General Adaptation Syndrome (GAS)")
    pdf.add_paragraph(
        "The human biological response to prolonged stressors proceeds through three predictable physiological stages:",
        max_chars=92
    )
    pdf.add_bullet("1. Alarm Reaction", "Acute 'fight-or-flight' activation via the sympathetic nervous system and adrenal glands. Release of adrenaline and noradrenaline. Increased heart rate, blood pressure, pupil dilation, muscle tension.")
    pdf.add_bullet("2. Resistance Stage", "The body adapts to sustained stress. Cortisol release maintains high blood glucose levels. Parasympathetic system moderates shock. High metabolic energy expenditure.")
    pdf.add_bullet("3. Exhaustion Stage", "Prolonged chronic stress drains bodily reserves. Immune breakdown, burnout, clinical depression, chronic fatigue, severe cognitive degradation.")

    pdf.add_heading_1("3. Acute vs Chronic Stress")
    pdf.add_bullet("Acute Stress", "Short-term, sudden demand (e.g. engine failure at V1, windshear encounter). Mobilizes body resources immediately. Resolves once crisis ends.")
    pdf.add_bullet("Chronic Stress", "Long-term persistent cumulative pressure (marital conflict, bereavement, financial troubles, toxic workplace). Insidious: permanently raises baseline cortisol, degrades sleep quality, and lowers tolerance to acute in-flight crises.")

    pdf.add_heading_1("4. Cockpit Workload Management & Task Prioritization")
    pdf.add_callout(
        "trap",
        "The Universal Cockpit Golden Rule: Aviate - Navigate - Communicate",
        "When dealing with any emergency, high workload, or system malfunction, the flight crew must strictly enforce the golden hierarchy:\n"
        "1. AVIATE: Maintain control of the aircraft, pitch attitude, airspeed, and altitude;\n"
        "2. NAVIGATE: Know present position, terrain clearance (MSA), and heading;\n"
        "3. COMMUNICATE: Advise ATC, company, and cabin crew only AFTER the aircraft is stabilized;\n"
        "4. ADMINISTRATE: Complete systems diagnostics, ECAM/QRH checklists, and passenger briefings.",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch11 = [
        ("Q1: What does the Yerkes-Dodson Law state regarding the relationship between arousal and human performance?",
         "[A] Performance increases linearly with stress indefinitely\n[B] Performance is an inverted U-curve: optimal at intermediate arousal, but poor under both under-arousal and over-arousal\n[C] Performance is independent of psychological stress\n[D] Pilots perform best under extreme panic",
         "CORRECT: [B]. The inverted-U curve demonstrates that both sensory underload (boredom) and severe overload (panic) degrade performance; peak capability occurs at moderate arousal."),
        ("Q2: In Hans Selye's General Adaptation Syndrome (GAS), which stage immediately follows the initial Alarm Reaction?",
         "[A] The Exhaustion stage\n[B] The Resistance stage\n[C] The Recovery stage\n[D] The Burnout stage",
         "CORRECT: [B]. The three phases of GAS are: 1) Alarm Reaction, 2) Resistance, and 3) Exhaustion."),
        ("Q3: When multiple alarms and flight anomalies occur simultaneously, what is the mandatory priority order of crew tasks?",
         "[A] Communicate -> Navigate -> Aviate\n[B] Aviate -> Navigate -> Communicate\n[C] Checklists -> Radios -> Flying\n[D] Declare MAYDAY -> Read QRH -> Hand fly",
         "CORRECT: [B]. 'Aviate, Navigate, Communicate' is the absolute priority rule in aviation safety."),
        ("Q4: How does severe acute stress affect a pilot's visual and mental processing?",
         "[A] Expands peripheral field of view\n[B] Induces cognitive tunneling (attentional narrowing onto a single feature, ignoring critical warnings)\n[C] Enhances ability to perform complex mathematics\n[D] Eliminates spatial disorientation",
         "CORRECT: [B]. Severe stress causes perceptual and cognitive tunneling, blinding the pilot to peripheral cues and multi-task information."),
        ("Q5: What is the primary operational hazard of cockpit underload (hypo-arousal) during long oceanic flights?",
         "[A] Adrenaline surge\n[B] Complacency, vigilance decrement, loss of situational awareness, and delayed response to unexpected events\n[C] Immediate hyperventilation\n[D] Otic barotrauma",
         "CORRECT: [B]. Low workload leads to complacency and reduced vigilance, leaving crew unprepared for sudden emergency deviations."),
        ("Q6: Which biological system triggers the immediate 'fight-or-flight' alarm response during an engine fire on take-off?",
         "[A] The parasympathetic nervous system\n[B] The sympathetic nervous system and adrenal medulla releasing adrenaline\n[C] The vestibular otolith organs\n[D] The immune system",
         "CORRECT: [B]. The sympathetic nervous system triggers instant adrenaline release, elevating heart rate and blood pressure for rapid physical response.")
    ]
    for q_text, opts, exp in questions_ch11:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 11 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 12: FATIGUE, SLEEP & CIRCADIAN RHYTHMS (~4 pages)
# ==============================================================================
def build_ch12():
    pdf_path = os.path.join(BASE_DIR, "040_ch12_fatigue_sleep_circadian.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 12: Fatigue & Circadian Rhythms")
    pdf.add_title_banner("Human Performance", 12, "Fatigue, Sleep & Circadian Rhythms", "393-432")

    pdf.add_heading_1("1. Sleep Architecture & Polysomnography")
    pdf.add_paragraph(
        "Sleep is an active physiological process essential for physical repair and cognitive restoration. "
        "A healthy human sleep cycle lasts approximately 90 MINUTES and alternates between two primary states:",
        max_chars=92
    )

    sleep_data = [
        ["NREM Stage 1", "Light transitional sleep", "Theta waves on EEG. Drowsiness, easily awakened. Muscle tone decreases."],
        ["NREM Stage 2", "True light sleep", "Presence of Sleep Spindles and K-complexes on EEG. Accounts for ~50% of total sleep time."],
        ["NREM Stages 3 & 4 (Slow-Wave Sleep - SWS)", "Deep restorative sleep", "Delta waves on EEG. Growth hormone secretion; physical body and tissue repair. Waking from SWS causes severe SLEEP INERTIA (grogginess lasting 15-30 min)."],
        ["REM Sleep (Rapid Eye Movement)", "Dreaming / Paradoxical sleep", "Fast, desynchronized Beta-like EEG waves. Total skeletal muscle paralysis (atonia). High brain metabolism. Mental, emotional and memory consolidation."]
    ]
    pdf.add_table(["Sleep Phase", "Physiological Nature", "Biophysical Function & EEG Signature"], sleep_data, col_widths=[125.0, 145.0, 240.0])

    pdf.add_heading_1("2. Circadian Rhythms & The Window of Circadian Low (WOCL)")
    pdf.add_paragraph(
        "Human physiology follows a ~24-to-25 hour biological rhythm governed by the Suprachiasmatic Nucleus (SCN) "
        "in the hypothalamus. Melatonin is secreted by the pineal gland during darkness.",
        max_chars=92
    )

    pdf.add_callout(
        "trap",
        "The Window of Circadian Low (WOCL: 02:00 to 05:59 Local Time)",
        "• Core body temperature, cortisol, alertness, and mental acuity reach their ABSOLUTE DAILY MINIMUM between 02:00 and 05:59.\n"
        "• A secondary circadian dip occurs in the early afternoon (13:00 to 16:00 - post-prandial dip).\n"
        "• Flight operations during the WOCL carry a dramatically elevated risk of micro-sleeps, lapses, and severe cognitive degradation!",
        max_chars=86
    )

    pdf.add_heading_1("3. Jet Lag Management & Directionality")
    pdf.add_paragraph(
        "Jet Lag (circadian desynchronosis) occurs when crossing multiple time zones rapidly, disrupting the internal body clock:",
        max_chars=92
    )
    pdf.add_bullet("Westward Travel ('West is Best')", "Lengthens the day. Human circadian clock naturally runs slightly longer than 24 hours (~25h). Much easier to adapt (body stays up later).")
    pdf.add_bullet("Eastward Travel ('East is a Beast')", "Shortens the day. Forcing sleep earlier when the body is not ready is physiologically much harder; recovery takes ~50% longer than westward travel!")

    pdf.add_heading_1("4. In-Flight Controlled Rest (Flight Deck Napping)")
    pdf.add_callout(
        "definition",
        "EASA Regulations on Controlled Rest on the Flight Deck",
        "• Maximum Nap Duration: Limited to 40 TO 45 MINUTES maximum. This prevents entering deep Stage 3/4 Slow-Wave Sleep (SWS), avoiding severe sleep inertia.\n"
        "• Recovery Wake Period: Must include at least 20 MINUTES of awake time before resuming operational flight duties.\n"
        "• Permitted only during low-workload cruise flight in multi-pilot aircraft with strict briefing to the remaining alert pilot.",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch12 = [
        ("Q1: What is the typical duration of a single complete adult human sleep cycle?",
         "[A] 30 minutes\n[B] 90 minutes (approx. 1.5 hours)\n[C] 3 hours\n[D] 8 hours",
         "CORRECT: [B]. Human sleep progresses through NREM and REM stages in cycles lasting approximately 90 minutes, repeating 4 to 6 times per night."),
        ("Q2: During which time window does the Window of Circadian Low (WOCL) occur, where human alertness and performance reach their lowest ebb?",
         "[A] 12:00 to 14:00\n[B] 18:00 to 22:00\n[C] 02:00 to 05:59 local time\n[D] 06:00 to 09:00",
         "CORRECT: [C]. The WOCL occurs between 02:00 and 05:59 local time, characterized by minimum core body temperature and maximum fatigue vulnerability."),
        ("Q3: Why is trans-meridian jet lag significantly harder to adapt to following eastward travel compared to westward travel?",
         "[A] Eastward flights cross the equator\n[B] Eastward travel shortens the day, forcing sleep before the natural circadian cycle, whereas westward travel lengthens the day, aligning with the human clock (~25h)\n[C] Higher altitude winds\n[D] Cosmic radiation",
         "CORRECT: [B]. 'West is best, East is a beast'. The internal human circadian pacemaker has an intrinsic period slightly exceeding 24 hours (~25h), making phase delay (westward) much easier than phase advance (eastward)."),
        ("Q4: What is the primary biological function of deep Slow-Wave Sleep (NREM Stages 3 and 4)?",
         "[A] Dreaming and emotional stress processing\n[B] Physical, muscular, and cellular tissue repair through growth hormone secretion\n[C] Rapid eye movements\n[D] High mental alertness",
         "CORRECT: [B]. SWS (Delta sleep) is dedicated to physical restoration and cellular rebuilding; REM sleep is dedicated to cognitive and memory consolidation."),
        ("Q5: What is the maximum recommended nap duration during Controlled Rest on the flight deck under EASA guidelines?",
         "[A] 15 minutes\n[B] 40 to 45 minutes (followed by 20 min wake-up period)\n[C] 90 minutes\n[D] 2 hours",
         "CORRECT: [B]. Controlled rest is limited to 40-45 minutes to prevent deep Stage 3/4 sleep, followed by a mandatory 20-minute recovery period to eliminate sleep inertia."),
        ("Q6: What is 'Sleep Inertia' and how does it manifest in flight crew?",
         "[A] The inability to fall asleep in a hotel\n[B] A state of grogginess, impaired motor coordination, and sluggish cognition immediately upon waking from deep sleep, lasting 15 to 30 minutes\n[C] Sleepwalking on the aircraft\n[D] Extreme insomnia",
         "CORRECT: [B]. Sleep inertia is the period of impaired performance and confusion experienced upon abrupt awakening from deep Slow-Wave Sleep.")
    ]
    for q_text, opts, exp in questions_ch12:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 12 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 13: COMMUNICATION, CRM & COCKPIT TEAMWORK (~4 pages)
# ==============================================================================
def build_ch13():
    pdf_path = os.path.join(BASE_DIR, "040_ch13_communication_crm.pdf")
    pdf = PDFBuilder("Human Performance", "040", "Chapter 13: Communication, CRM & Teamwork")
    pdf.add_title_banner("Human Performance", 13, "Communication, CRM & Teamwork", "433-464")

    pdf.add_heading_1("1. Evolution & Goals of Crew Resource Management (CRM)")
    pdf.add_paragraph(
        "Crew Resource Management (CRM) was established following major multi-pilot air disasters (such as the 1977 Tenerife collision "
        "and the 1978 Portland fuel exhaustion). CRM is the effective utilization of ALL available resources (human, hardware, and information) "
        "to achieve safe and efficient flight operations:",
        max_chars=92
    )

    pdf.add_bullet("Core Focus", "Interpersonal communication, leadership, team coordination, conflict management, assertiveness, and error mitigation.")
    pdf.add_bullet("Modern Scope", "Expanded from cockpit-only to company-wide: Flight Crew, Cabin Crew, Maintenance Staff, Flight Dispatchers, and Air Traffic Control.")

    pdf.add_heading_1("2. The Trans-Cockpit Authority Gradient")
    pdf.add_paragraph(
        "The psychological relationship and authority dynamic between Captain and First Officer:",
        max_chars=92
    )

    gradient_data = [
        ["Steep Authority Gradient (Autocratic)", "Dictatorial, aggressive captain; intimidated, submissive co-pilot.", "First officer notices deviations or dangerous errors, but is afraid to speak up (Tenerife catastrophe). Highly dangerous."],
        ["Flat Authority Gradient (Laissez-faire)", "Overly informal, peer-level dynamic; lack of clear command structure.", "Ambiguity over who has aircraft control; lack of firm leadership during emergencies. Decisions are delayed or compromised."],
        ["Optimum Authority Gradient (Democratic / Assertive)", "Captain maintains decisive leadership; actively solicits input and encourages open crew cross-checking.", "Co-pilot is assertive, respectful, and empowered to challenge errors immediately. Optimal safety synergy!"]
    ]
    pdf.add_table(["Gradient Profile", "Cockpit Interpersonal Dynamic", "Flight Safety Implication & Hazard"], gradient_data, col_widths=[140.0, 160.0, 210.0])

    pdf.add_heading_1("3. Crew Assertiveness & The PACE Escalation Model")
    pdf.add_paragraph(
        "When an observant crew member detects an operational hazard, deviation from SOP, or safety risk, "
        "assertive communication must be graded using the PACE model:",
        max_chars=92
    )

    pace_data = [
        ["P - Probe", "'Captain, did you notice our altitude?'", "Non-confrontational inquiry to assess awareness."],
        ["A - Alert", "'Captain, we are 300 ft below our assigned flight level.'", "Direct, objective statement of observed flight parameter."],
        ["C - Challenge", "'Captain, we are below minimum safe altitude; you must climb now.'", "Unambiguous demand for immediate corrective action."],
        ["E - Emergency", "'I have control! Executing immediate go-around.'", "Direct intervention and takeover of controls to prevent catastrophe."]
    ]
    pdf.add_table(["PACE Stage", "Cockpit Verbal Phraseology", "Operational Escalation Objective"], pace_data, col_widths=[105.0, 205.0, 200.0])

    pdf.add_heading_1("4. Group Dynamics: Groupthink, Risky Shift & Synergy")
    pdf.add_bullet("Synergy (1 + 1 > 2)", "Effective teamwork produces operational output and safety margins far exceeding the individual sum of the crew members' capabilities.")
    pdf.add_bullet("Groupthink", "A psychological drive for consensus within a cohesive group that suppresses dissenting opinions and realistic assessment of alternative courses of action.")
    pdf.add_bullet("Risky Shift", "Groups frequently make riskier decisions collectively than any individual member would make alone, due to shared perceived responsibility.")

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch13 = [
        ("Q1: What is an 'optimal trans-cockpit authority gradient' in multi-pilot flight operations?",
         "[A] A completely equal authority distribution where all decisions are voted upon\n[B] An autocratic captain who tolerates no questions\n[C] A decisive captain who exercises clear leadership while actively fostering an open atmosphere of inquiry and assertive co-pilot cross-checking\n[D] A gradient where the co-pilot always commands",
         "CORRECT: [C]. The optimum gradient provides clear leadership by the PIC while empowering the First Officer to challenge deviations assertively without fear."),
        ("Q2: In the PACE graded assertiveness model, what does the letter 'C' stand for?",
         "[A] Coordinate\n[B] Challenge (unambiguous demand for corrective action)\n[C] Checklist\n[D] Cancel clearance",
         "CORRECT: [B]. PACE stands for: Probe -> Alert -> Challenge -> Emergency."),
        ("Q3: What is 'Groupthink' in aviation crew dynamics?",
         "[A] Brainstorming session before departure\n[B] The tendency of a cohesive group to strive for unanimity, suppressing dissenting opinions and failing to evaluate hazards realistically\n[C] Synchronized navigation computer cross-talk\n[D] Multi-pilot checklist discipline",
         "CORRECT: [B]. Groupthink leads teams to overlook obvious dangers because members avoid conflict and conform to the perceived group consensus."),
        ("Q4: What is 'Risky Shift' in operational decision making?",
         "[A] Changing flight levels in turbulence\n[B] The phenomenon where a group collectively accepts a higher level of risk than individual crew members would accept on their own\n[C] Shifting from manual flight to autopilot\n[D] Diverting to an unfamiliar airport",
         "CORRECT: [B]. In group dynamics, perceived diffusion of personal responsibility encourages crews to accept greater collective risks than individuals alone."),
        ("Q5: What is the primary objective of modern Crew Resource Management (CRM)?",
         "[A] Teaching pilots how to repair engines in flight\n[B] The effective utilization of all available resources (human, hardware, and information) to achieve safe and efficient flight operations\n[C] Eliminating the role of the captain\n[D] Replacing visual scanning with radar surveillance",
         "CORRECT: [B]. CRM optimizes crew communication, situational awareness, workload distribution, and decision making across the entire operational spectrum."),
        ("Q6: When a co-pilot notices the aircraft descending through decision height without visual contact with the runway, what is the mandatory immediate CRM action?",
         "[A] Wait for the captain to make a decision\n[B] Clearly and assertively call 'Go-Around', and if no immediate response, take control and execute go-around\n[C] Look out of the window to assist visual search\n[D] Silence the audio warnings",
         "CORRECT: [B]. Standard SOP and CRM mandate an immediate assertive go-around call, escalating to control intervention if the pilot flying fails to react.")
    ]
    for q_text, opts, exp in questions_ch13:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"HPL Chapter 13 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch09()
    build_ch10()
    build_ch11()
    build_ch12()
    build_ch13()
