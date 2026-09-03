#!/usr/bin/env python3
"""
Full-Depth Study Manual Generator - Volume 3 (Chapters 13 to 18).
Designed for 100% self-contained study.
Target: ~18 to 20 pages total across Chapters 13 to 18.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

# ==============================================================================
# CHAPTER 13: AIRSPACE CLASSIFICATION (~3-4 pages)
# ==============================================================================
def build_ch13():
    pdf_path = os.path.join(BASE_DIR, "010_ch13_airspace.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 13: Airspace Organization & Classification")
    pdf.add_title_banner("Air Law", 13, "Airspace Classes (A to G)", "263-278")

    pdf.add_heading_1("1. Master Airspace Classification Table (ICAO & SERA)")
    pdf.add_paragraph(
        "Airspace is categorized into 7 classes (A to G). Classes A to E are Controlled Airspace; "
        "Classes F and G are Uncontrolled Airspace. Separation and communications requirements vary strictly by class:",
        max_chars=92
    )

    air_data = [
        ["Class A", "IFR only", "IFR from IFR", "Continuous 2-way", "ATC Clearance MANDATORY.\nVFR is STRICTLY PROHIBITED."],
        ["Class B", "IFR & VFR", "All flights from all flights", "Continuous 2-way", "ATC Clearance MANDATORY.\nFull separation provided to all."],
        ["Class C", "IFR & VFR", "IFR from IFR & VFR.\nVFR from IFR only.", "Continuous 2-way", "ATC Clearance MANDATORY.\nVFR receives traffic info on other VFR."],
        ["Class D", "IFR & VFR", "IFR from IFR only.", "Continuous 2-way", "ATC Clearance MANDATORY.\nTraffic information given to VFR on all flights."],
        ["Class E", "IFR & VFR", "IFR from IFR only.", "Continuous 2-way for IFR only", "Clearance MANDATORY for IFR.\nVFR does NOT need clearance or radio!"],
        ["Class F", "IFR & VFR", "None (Advisory only)", "Continuous for participating IFR", "Uncontrolled. IFR receives air traffic advisory service."],
        ["Class G", "IFR & VFR", "None", "Continuous for IFR where required", "Uncontrolled. Flight Information Service (FIS) on request."]
    ]
    pdf.add_table(["Class", "Flights", "Separation Provided", "Radio Comms", "ATC Clearance & Key Rules"], air_data, col_widths=[55.0, 75.0, 115.0, 115.0, 150.0])

    pdf.add_callout(
        "trap",
        "Class E Airspace: The Famous AviationExam Trap",
        "Question: Is an ATC clearance required to fly VFR in Class E airspace?\n"
        "Answer: NO. In Class E, VFR flights do NOT require an ATC clearance and do NOT require two-way radio comms. "
        "Only IFR flights require ATC clearance and continuous communication in Class E.",
        max_chars=86
    )

    pdf.add_heading_1("2. Speed Limitations in Airspace")
    pdf.add_bullet("General Speed Limit", "A maximum speed of 250 kt IAS applies to all flights operating below FL 100 (or 10,000 ft AMSL), EXCEPT in Class A and B airspace, or when authorized by ATC.")

    pdf.add_heading_1("3. Special Use Airspace")
    pdf.add_bullet("Prohibited Area (P)", "Airspace within which flight of aircraft is strictly prohibited.")
    pdf.add_bullet("Restricted Area (R)", "Flight of aircraft is restricted in accordance with specified conditions.")
    pdf.add_bullet("Danger Area (D)", "Activities dangerous to flight may exist at specified times. Flight is not legally barred, but caution required.")
    pdf.add_bullet("Temporary Segregated Area (TSA)", "Airspace temporarily segregated for exclusive use of specific users.")
    pdf.add_bullet("Temporary Reserved Area (TRA)", "Airspace temporarily reserved for specific operations with civil transit permitted under ATC.")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch13 = [
        ("Q1: In which airspace classes are VFR flights strictly prohibited?",
         "[A] Class A only\n[B] Classes A and B\n[C] Classes A, B, and C\n[D] Class G",
         "CORRECT: [A]. Class A airspace is reserved exclusively for IFR flights; VFR is prohibited."),
        ("Q2: In Class C airspace, does ATC separate VFR flights from other VFR flights?",
         "[A] Yes, full separation is provided.\n[B] No, VFR receives only traffic information in respect of other VFR flights.\n[C] Only during night operations.\n[D] Only above FL 100.",
         "CORRECT: [B]. In Class C, IFR is separated from IFR and VFR. VFR is separated from IFR, but receives only traffic information regarding other VFR."),
        ("Q3: Does a VFR flight require an ATC clearance to enter Class E airspace?",
         "[A] Yes, clearance is mandatory for all flights.\n[B] No, VFR flights do not require ATC clearance in Class E.\n[C] Yes, unless squawking 7000.\n[D] Only when entering a control zone.",
         "CORRECT: [B]. Class E is controlled for IFR only. VFR flights do not require ATC clearance or two-way radio communication."),
        ("Q4: What is the standard speed limitation for aircraft operating below FL 100 in Class D airspace?",
         "[A] 200 kt IAS\n[B] 250 kt IAS\n[C] 280 kt IAS\n[D] No speed limit applies",
         "CORRECT: [B]. 250 kt IAS is the standard maximum speed below FL 100 across classes C to G."),
        ("Q5: What is the definition of a Danger Area (D)?",
         "[A] Airspace where flight of aircraft is completely prohibited\n[B] Airspace within which activities dangerous to the flight of aircraft may exist at specified times\n[C] Airspace reserved exclusively for supersonic military flight\n[D] Airspace surrounding a nuclear power plant",
         "CORRECT: [B]. A Danger Area denotes airspace within which activities dangerous to flight may occur at specified times (flight is not legally barred, unlike a Prohibited area).")
    ]
    for q_text, opts, exp in questions_ch13:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 13 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 14: AIR TRAFFIC SERVICES (~3 pages)
# ==============================================================================
def build_ch14():
    pdf_path = os.path.join(BASE_DIR, "010_ch14_air_traffic_services.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 14: Air Traffic Services")
    pdf.add_title_banner("Air Law", 14, "Air Traffic Services & Emergencies", "279-296")

    pdf.add_heading_1("1. The Three Core Air Traffic Services (ATS)")
    pdf.add_bullet("1. Air Traffic Control (ATC)", "Prevents collisions between aircraft and between aircraft and obstacles on the maneuvering area, and expedites and maintains an orderly flow of traffic. (Subdivided into: Area Control ACC, Approach Control APP, Aerodrome Control TWR).")
    pdf.add_bullet("2. Flight Information Service (FIS)", "Provides advice and information useful for the safe and efficient conduct of flights (weather, changes in serviceability of nav aids, traffic information).")
    pdf.add_bullet("3. Alerting Service (ALRS)", "Notifies appropriate organizations regarding aircraft in need of search and rescue aid, and assists such organizations as required. Provided to ALL aircraft provided with ATC, or submitting a flight plan.")

    pdf.add_heading_1("2. Automatic Terminal Information Service (ATIS)")
    pdf.add_paragraph(
        "Continuous broadcast of routine non-control information at busy aerodromes (Voice-ATIS and D-ATIS):\n"
        "• Identified by a designator letter from the ICAO spelling alphabet (Alpha to Zulu), updated sequentially.\n"
        "• Updated whenever a significant change in meteorological or operational conditions occurs.\n"
        "• Pilot must acknowledge current ATIS code upon initial contact with ATC.",
        max_chars=92
    )

    pdf.add_heading_1("3. The Three Emergency Phases (Annex 11 / 12)")
    phases_data = [
        ["1. INCERFA (Uncertainty Phase)", "No communication received within 30 minutes after time it should have been received, OR aircraft fails to arrive within 30 minutes of ETA."],
        ["2. ALERFA (Alert Phase)", "Following INCERFA, attempts to communicate fail; OR aircraft cleared to land fails to land within 5 minutes of ETA; OR operating efficiency impaired."],
        ["3. DETRESFA (Distress Phase)", "Following ALERFA, or fuel on board considered exhausted, or information indicates aircraft about to make forced landing or has crashed."]
    ]
    pdf.add_table(["Emergency Phase", "Official Activation Criteria (AviationExam Core)"], phases_data, col_widths=[145.0, 365.0])

    pdf.add_heading_1("4. Mandatory Readback Requirements (SERA.8015)")
    pdf.add_paragraph(
        "The flight crew shall read back to the air traffic controller safety-related parts of ATC clearances and "
        "instructions which are transmitted orally. The following parts shall ALWAYS be read back:",
        max_chars=92
    )
    pdf.add_bullet("1. Route Clearances", "Any ATC route clearance, SID, STAR, or route modification.")
    pdf.add_bullet("2. Clearances and Instructions to Enter, Land On, Take Off On, Hold Short Of, Cross, or Taxi On", "Any runway instruction must be read back completely with runway designator.")
    pdf.add_bullet("3. Runway-in-use, Altimeter Settings, SSR Codes", "Crucial numerical flight parameters.")
    pdf.add_bullet("4. Newly Assigned Level Instructions, Heading and Speed Instructions", "Vertical and horizontal vectors.")
    pdf.add_bullet("5. Transition Levels", "Whether given by ATC or ATIS.")

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch14 = [
        ("Q1: What condition triggers the declaration of INCERFA (Uncertainty Phase)?",
         "[A] Aircraft fails to land within 5 minutes of landing clearance.\n[B] No communication within 30 minutes after time it should have been received.\n[C] Fuel on board is below reserve.\n[D] Pilot squawks 7600.",
         "CORRECT: [B]. INCERFA is declared when no communication has been received within 30 minutes of the time it should have been received."),
        ("Q2: An aircraft that has been cleared to land fails to land within what time interval to trigger ALERFA?",
         "[A] 2 minutes\n[B] 5 minutes\n[C] 10 minutes\n[D] 15 minutes",
         "CORRECT: [B]. An aircraft cleared to land that fails to land within 5 minutes of estimated landing time triggers an immediate Alert Phase (ALERFA)."),
        ("Q3: When the fuel on board is considered exhausted, which emergency phase is declared?",
         "[A] INCERFA\n[B] ALERFA\n[C] DETRESFA\n[D] PAN PAN",
         "CORRECT: [C]. Fuel exhaustion triggers the Distress Phase (DETRESFA)."),
        ("Q4: To whom is the Alerting Service (ALRS) provided?",
         "[A] Only to IFR flights in Class A airspace\n[B] To all aircraft provided with air traffic control service and to any other aircraft submitting a flight plan\n[C] Exclusively to commercial passenger airliners\n[D] Only during search and rescue operations",
         "CORRECT: [B]. Alerting service is provided to all aircraft receiving ATC service, having filed a flight plan, or otherwise known to ATS."),
        ("Q5: Which ATS unit provides air traffic control service to en-route controlled flights?",
         "[A] Aerodrome Control Tower (TWR)\n[B] Approach Control Unit (APP)\n[C] Area Control Centre (ACC)\n[D] Flight Information Centre (FIC)",
         "CORRECT: [C]. The Area Control Centre (ACC) is responsible for en-route air traffic control."),
        ("Q6: What emergency frequency must be continuously monitored by aircraft equipped with VHF radio when operating in areas where ATS is provided?",
         "[A] 121.5 MHz\n[B] 123.45 MHz\n[C] 118.0 MHz\n[D] 136.0 MHz",
         "CORRECT: [A]. Under SERA and ICAO Annex 10, 121.5 MHz is the international VHF aeronautical emergency frequency and must be monitored whenever practicable.")
    ]
    for q_text, opts, exp in questions_ch14:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 14 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 15: SEPARATION METHODS AND MINIMA (~4 pages)
# ==============================================================================
def build_ch15():
    pdf_path = os.path.join(BASE_DIR, "010_ch15_separation.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 15: Separation Methods & Minima")
    pdf.add_title_banner("Air Law", 15, "Separation & Wake Turbulence", "297-330")

    pdf.add_heading_1("1. Vertical Separation & RVSM")
    pdf.add_bullet("Standard Vertical Separation", "1,000 ft below FL 290; 2,000 ft above FL 290.")
    pdf.add_bullet("RVSM (Reduced Vertical Separation Minimum)", "1,000 ft vertical separation between FL 290 and FL 410 inclusive for approved aircraft. Above FL 410, separation is 2,000 ft.")

    pdf.add_heading_1("2. Horizontal Radar & Procedural Separation")
    pdf.add_bullet("Standard Radar Separation", "5 NM en-route; 3 NM in terminal areas (reduced to 2.5 NM under special radar criteria).")
    pdf.add_bullet("Non-Radar Longitudinal Separation", "15 minutes standard; reduced to 10 minutes if navigation aids permit frequent position determination; 5 minutes for climbing/descending aircraft on same track; 3 minutes for departing aircraft.")
    pdf.add_bullet("DME Separation", "20 NM on same track; 10 NM if leading aircraft maintains >= 20 kt higher true airspeed.")
    pdf.add_bullet("Mach Number Technique", "Used in oceanic/continental airspace: 80 NM or 10 minutes when longitudinal separation is based on Mach number.")

    pdf.add_heading_1("3. Non-Radar Lateral Separation by Track Divergence")
    pdf.add_paragraph(
        "Lateral separation between two aircraft departing or navigating along diverging tracks:\n"
        "• VOR: Tracks diverge by at least 15° and at least one aircraft is at or beyond 15 NM from the VOR.\n"
        "• NDB: Tracks diverge by at least 30° and at least one aircraft is at or beyond 15 NM from the NDB.\n"
        "• Dead Reckoning (DR): Tracks diverge by at least 45° and at least one aircraft is at or beyond 15 NM from intersection.",
        max_chars=92
    )

    pdf.add_heading_1("4. Wake Turbulence Categories & Minima Matrix")
    wake_data = [
        ["SUPER", "Airbus A380-800", "Behind Super: Heavy 6 NM, Medium 7 NM, Light 8 NM."],
        ["HEAVY (H)", "136,000 kg or more", "Behind Heavy: Heavy 4 NM, Medium 5 NM, Light 6 NM."],
        ["MEDIUM (M)", "Between 7,000 kg and 136,000 kg", "Behind Medium: Heavy/Medium Radar min, Light 5 NM."],
        ["LIGHT (L)", "7,000 kg or less", "Light twins and single-engine aircraft."]
    ]
    pdf.add_table(["Category", "Certified Take-Off Mass (MTOM)", "Radar Wake Separation (Trailing)"], wake_data, col_widths=[95.0, 185.0, 230.0])

    pdf.add_callout(
        "trap",
        "Timed Departure Wake Turbulence Separation (Non-Radar)",
        "When taking off behind a HEAVY aircraft from the same runway:\n"
        "• Full length of runway: 2 MINUTES separation.\n"
        "• From an INTERMEDIATE intersection (displaced threshold): 3 MINUTES separation (due to vortex drift).",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch15 = [
        ("Q1: What is the maximum certified take-off mass for a HEAVY wake turbulence category aircraft?",
         "[A] 100,000 kg or more\n[B] 136,000 kg or more\n[C] 150,000 kg or more\n[D] 300,000 kg or more",
         "CORRECT: [B]. The HEAVY wake turbulence category applies to aircraft of 136,000 kg (300,000 lbs) or more."),
        ("Q2: What is the radar wake turbulence separation for a LIGHT aircraft following a HEAVY aircraft on approach?",
         "[A] 4 NM\n[B] 5 NM\n[C] 6 NM\n[D] 7 NM",
         "CORRECT: [C]. Heavy behind Heavy is 4 NM; Medium behind Heavy is 5 NM; Light behind Heavy is 6 NM."),
        ("Q3: When departing behind a Heavy aircraft from an intermediate intersection, what is the required time separation?",
         "[A] 2 minutes\n[B] 3 minutes\n[C] 4 minutes\n[D] 5 minutes",
         "CORRECT: [B]. From an intermediate intersection, 3 minutes separation is required (compared to 2 minutes from full length)."),
        ("Q4: What is the standard non-radar longitudinal separation between two aircraft on the same track if navigation aids permit frequent position fixes?",
         "[A] 5 minutes\n[B] 10 minutes\n[C] 15 minutes\n[D] 20 minutes",
         "CORRECT: [B]. Standard procedural separation is 15 minutes, reduced to 10 minutes when navaids permit frequent updates."),
        ("Q5: What is the vertical separation applied in RVSM airspace between FL 290 and FL 410?",
         "[A] 500 ft\n[B] 1,000 ft\n[C] 2,000 ft\n[D] 4,000 ft",
         "CORRECT: [B]. Reduced Vertical Separation Minimum (RVSM) provides 1,000 ft vertical separation between FL 290 and FL 410."),
        ("Q6: What is the radar wake turbulence separation for a MEDIUM aircraft following a HEAVY aircraft on approach?",
         "[A] 3 NM\n[B] 4 NM\n[C] 5 NM\n[D] 6 NM",
         "CORRECT: [C]. Heavy behind Heavy is 4 NM; Medium behind Heavy is 5 NM; Light behind Heavy is 6 NM."),
        ("Q7: What is the minimum lateral divergence angle required between two departing aircraft navigating via VOR?",
         "[A] 10°\n[B] 15° (at or beyond 15 NM)\n[C] 30°\n[D] 45°",
         "CORRECT: [B]. Lateral separation by VOR requires tracks diverging by at least 15° at a distance of at least 15 NM from the facility.")
    ]
    for q_text, opts, exp in questions_ch15:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 15 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 16: CONTROL OF AIRCRAFT & EMERGENCIES (~3 pages)
# ==============================================================================
def build_ch16():
    pdf_path = os.path.join(BASE_DIR, "010_ch16_control_aircraft.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 16: Control of Aircraft & Emergencies")
    pdf.add_title_banner("Air Law", 16, "Control of Aircraft & Emergencies", "331-356")

    pdf.add_heading_1("1. Speed Control Limitations (ATC)")
    pdf.add_paragraph(
        "ATC may apply speed control to maintain separation. However, speed adjustments must not be applied "
        "or continued within 4 NM of the runway threshold on final approach. Speed reductions should not "
        "normally be below 160 kt IAS for jet aircraft on intermediate/final approach.",
        max_chars=92
    )

    pdf.add_heading_1("2. Fuel Emergencies: MINIMUM FUEL vs MAYDAY FUEL")
    pdf.add_callout(
        "trap",
        "MINIMUM FUEL vs MAYDAY MAYDAY MAYDAY FUEL",
        "• 'MINIMUM FUEL': Informs ATC that all planned aerodrome options are committed and that any change to "
        "clearance may result in landing with less than planned final reserve fuel. IT IS NOT AN EMERGENCY and "
        "DOES NOT CONFER PRIORITY.\n"
        "• 'MAYDAY MAYDAY MAYDAY FUEL': Distress message. Declares that calculated usable fuel on landing will be "
        "LESS than the mandatory final reserve fuel. Confers ABSOLUTE PRIORITY.",
        max_chars=86
    )

    pdf.add_heading_1("3. Radio Communications Failure Procedures (SERA.8035)")
    pdf.add_bullet("Transponder Setting", "Squawk Mode A Code 7600 immediately.")
    pdf.add_bullet("In VMC", "Continue to fly in VMC; land at the nearest suitable aerodrome; report arrival to the appropriate ATS unit by the most expeditious means.")
    pdf.add_bullet("In IMC (Controlled Airspace)", "Maintain last assigned speed and level for 7 MINUTES (or 3 minutes if being radar vectored), then adjust level/speed in accordance with filed flight plan. Proceed to destination radio aid and commence descent at expected approach time (EAT) or ETA.")

    pdf.add_heading_1("4. Emergency Descent Procedures in Controlled Airspace")
    pdf.add_paragraph(
        "When an aircraft is forced to execute an immediate emergency descent (e.g. rapid cabin depressurization):\n"
        "1. Turn immediately 30° (or 45°) left or right to clear the airway centerline.\n"
        "2. Transmit distress message: 'MAYDAY MAYDAY MAYDAY [Callsign] EMERGENCY DESCENT'.\n"
        "3. Squawk Mode A Code 7700; select emergency frequency 121.5 MHz.\n"
        "4. Turn on all exterior aircraft lights to maximize conspicuity.",
        max_chars=92
    )

    pdf.add_heading_1("5. Distress and Urgency Radiotelephony Communications")
    radio_data = [
        ["Distress (MAYDAY)", "Grave and imminent danger requiring immediate assistance.", "MAYDAY MAYDAY MAYDAY, Callsign, Position, Level, Nature of distress, Intentions. Absolute priority."],
        ["Urgency (PAN PAN)", "Condition concerning safety of aircraft/person, not requiring immediate assistance.", "PAN PAN PAN PAN PAN PAN, Callsign, Position, Level, Nature of urgency. Priority over all except distress."],
        ["Medical Transport", "Aircraft protected under Geneva Conventions transporting medical personnel/supplies.", "Prefix 'PAN PAN MEDICAL' announces protected status."]
    ]
    pdf.add_table(["Category & Spoken Prefix", "Operational Definition & Circumstances", "Transmission Contents & Radiotelephony Status"], radio_data, col_widths=[125.0, 195.0, 190.0])

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch16 = [
        ("Q1: Does transmitting the phrase 'MINIMUM FUEL' give the aircraft priority over other traffic?",
         "[A] Yes, immediate clearance to land.\n[B] No, it is not an emergency and confers no priority.\n[C] Only if flying in Class A airspace.\n[D] Yes, priority over all VFR flights.",
         "CORRECT: [B]. 'MINIMUM FUEL' indicates that the flight cannot accept undue delays, but confers NO PRIORITY. Priority is only granted by declaring 'MAYDAY MAYDAY MAYDAY FUEL'."),
        ("Q2: In IMC, following a communications failure while being radar vectored, how long must the assigned speed and level be maintained?",
         "[A] 3 minutes\n[B] 7 minutes\n[C] 15 minutes\n[D] Until reaching destination",
         "CORRECT: [A]. Under SERA.8035, if under radar vectors, maintain speed/level for 3 minutes (compared to 7 minutes if on a published route)."),
        ("Q3: Within what distance of the runway threshold must ATC cease applying speed control?",
         "[A] 2 NM\n[B] 4 NM\n[C] 8 NM\n[D] 10 NM",
         "CORRECT: [B]. Speed control shall not be applied or continued within 4 NM of the threshold on final approach."),
        ("Q4: Which distress call prefix is used when an aircraft is threatened by grave and imminent danger and requires immediate assistance?",
         "[A] PAN PAN\n[B] MAYDAY spoken three times\n[C] SECURITE\n[D] EMERGENCY",
         "CORRECT: [B]. The international spoken distress signal is 'MAYDAY' spoken three times."),
        ("Q5: If an aircraft suffers complete radio failure in VMC, what action should the PIC take?",
         "[A] Squawk 7600 and continue to destination at assigned Flight Level\n[B] Continue in VMC, land at the nearest suitable aerodrome, and notify ATS expeditiously\n[C] Circle in present position for 45 minutes\n[D] Descend immediately to 500 ft AGL",
         "CORRECT: [B]. Under SERA.8035, if in VMC, the aircraft must remain in VMC, land at the nearest suitable aerodrome, and report to ATS."),
        ("Q6: In radiotelephony phraseology, what standard word indicates that a transmission has ended and no response is expected?",
         "[A] ROGER\n[B] OVER\n[C] OUT\n[D] WILCO",
         "CORRECT: [C]. 'OUT' signifies that the exchange is finished and no answer is expected ('OVER' signifies my transmission has ended and I expect an answer).")
    ]
    for q_text, opts, exp in questions_ch16:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 16 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 17: AIS & AIRAC (~3 pages)
# ==============================================================================
def build_ch17():
    pdf_path = os.path.join(BASE_DIR, "010_ch17_ais.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 17: Aeronautical Information Service (AIS)")
    pdf.add_title_banner("Air Law", 17, "AIS, AIP & AIRAC System", "357-374")

    pdf.add_heading_1("1. The Integrated Aeronautical Information Package (IAIP)")
    pdf.add_paragraph(
        "Under ICAO Annex 15, the purpose of the Aeronautical Information Service (AIS) is to ensure the flow of "
        "aeronautical data and information necessary for the safety, regularity, and efficiency of air navigation. "
        "The Integrated Aeronautical Information Package (IAIP) consists of:",
        max_chars=92
    )
    pdf.add_bullet("AIP (Aeronautical Information Publication)", "Basic permanent regulatory document for flight operations. Divided into 3 PARTS: GEN (General), ENR (En-Route), and AD (Aerodromes).")
    pdf.add_bullet("AIP Amendments (AIP AMDT)", "Permanent changes to the AIP. Regular amendments or AIRAC amendments.")
    pdf.add_bullet("AIP Supplements (AIP SUP)", "Temporary changes of long duration (3 MONTHS OR LONGER) or changes with extensive text or graphics. Published on conspicuous YELLOW paper.")
    pdf.add_bullet("NOTAM (Notice to Airmen)", "Information of urgent operational significance that cannot be published in the AIP in time. Maximum validity: 3 MONTHS.")
    pdf.add_bullet("PIB (Pre-flight Information Bulletin)", "Recapitulation of current NOTAMs and urgent information prepared for flight crews prior to departure.")
    pdf.add_bullet("AIC (Aeronautical Information Circulars)", "Notices regarding flight safety, technical, administrative, or legislative matters: White (Administrative), Yellow (Operational / ATC), Pink (Flight Safety awareness), Mauve (Airspace restrictions).")

    pdf.add_heading_1("2. The AIRAC System (AviationExam Core)")
    pdf.add_paragraph(
        "The Aeronautical Information Regulation and Control (AIRAC) system governs the publication of operationally "
        "significant changes on predetermined dates based on a 28-DAY INTERVAL:",
        max_chars=92
    )
    pdf.add_bullet("Standard AIRAC Cycle", "28 days. Effective dates are Thursdays at 00:00 UTC.")
    pdf.add_bullet("Publication Lead Time", "Information must be dispatched by AIS at least 42 DAYS prior to the effective date so as to reach recipients at least 28 days before.")
    pdf.add_bullet("Major Operational Changes", "For significant changes (e.g. major airspace restructuring, new ATS routes, new runway), information must be dispatched at least 56 DAYS in advance.")

    pdf.add_heading_1("3. NOTAM Structure & Q-Code Decoding")
    notam_data = [
        ["Q) Line", "Contains FIR, 5-letter Q-code (e.g. QFAXX), Traffic (I/V/IV), Purpose (N/B/O/M), Scope (A/E/W), Lower/Upper FL, Coordinates & Radius."],
        ["Item A)", "ICAO 4-letter location indicator of the aerodrome or FIR (e.g. LEMD, EGLL)."],
        ["Item B)", "Ten-figure date/time group indicating start of validity (YYMMDDHHMM UTC)."],
        ["Item C)", "Ten-figure date/time group indicating end of validity, or 'PERM' for permanent changes, or 'EST' for estimated duration."],
        ["Item D)", "Daily or periodic schedule of operation (if applicable)."],
        ["Item E)", "Plain-language decoded text of the NOTAM detailing the operational condition."],
        ["Items F) & G)", "Lower and upper altitude or flight level limits (e.g. GND / FL 120)."]
    ]
    pdf.add_table(["NOTAM Item", "Operational Meaning & Contents"], notam_data, col_widths=[95.0, 415.0])

    pdf.add_heading_1("4. Global Reporting Format (GRF) & SNOWTAM")
    grf_data = [
        ["RWYCC 6", "DRY", "Normal braking performance and directional control."],
        ["RWYCC 5", "FROST, WET (<= 3 mm water), SLUSH (<= 3 mm)", "Good braking action."],
        ["RWYCC 3", "COMPACTED SNOW (temp <= -15°C)", "Medium braking action."],
        ["RWYCC 2", "WET COMPACTED SNOW", "Medium to poor braking action."],
        ["RWYCC 1", "ICE", "Poor braking action."],
        ["RWYCC 0", "WET ICE, WATER ON COMPACTED SNOW", "LESS THAN POOR / NIL (Operations prohibited)."]
    ]
    pdf.add_table(["Condition Code", "Runway Contaminant & Depth", "Reported Braking Action"], grf_data, col_widths=[105.0, 225.0, 180.0])

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch17 = [
        ("Q1: What is the interval between consecutive AIRAC effective dates?",
         "[A] 14 days\n[B] 28 days\n[C] 42 days\n[D] 56 days",
         "CORRECT: [B]. The AIRAC cycle is based on predetermined dates separated by 28 days."),
        ("Q2: What is the maximum validity period of a standard NOTAM?",
         "[A] 24 hours\n[B] 1 month\n[C] 3 months\n[D] 6 months",
         "CORRECT: [C]. A NOTAM has a maximum validity period of 3 months."),
        ("Q3: What paper color is used to publish AIP Supplements (AIP SUP)?",
         "[A] White\n[B] Pink\n[C] Yellow\n[D] Blue",
         "CORRECT: [C]. AIP Supplements are printed on yellow paper to make them conspicuous."),
        ("Q4: How many days in advance must information for major AIRAC changes be dispatched?",
         "[A] 28 days\n[B] 42 days\n[C] 56 days\n[D] 90 days",
         "CORRECT: [C]. Major operational changes require 56 days advance dispatch (standard changes require 42 days)."),
        ("Q5: Under the Global Reporting Format (GRF), what does a Runway Condition Code (RWYCC) of 6 represent?",
         "[A] Poor braking action on wet ice\n[B] Dry runway with normal braking\n[C] Standing water / aquaplaning risk\n[D] Compacted snow",
         "CORRECT: [B]. RWYCC 6 indicates a dry runway with normal braking performance.")
    ]
    for q_text, opts, exp in questions_ch17:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 17 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 18: AERODROMES - PHYSICAL CHARACTERISTICS (~4 pages)
# ==============================================================================
def build_ch18():
    pdf_path = os.path.join(BASE_DIR, "010_ch18_aerodromes_characteristics.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 18: Aerodromes - Physical Characteristics")
    pdf.add_title_banner("Air Law", 18, "Aerodrome Design & OLS Surfaces", "375-398")

    pdf.add_heading_1("1. Aerodrome Reference Code (Annex 14)")
    pdf.add_paragraph(
        "Annex 14 classifies aerodrome facilities using a two-element reference code based on critical aircraft design:",
        max_chars=92
    )

    code_data = [
        ["Code 1", "Reference Field Length < 800 m", "Code A", "Wingspan < 15 m (Gear span < 4.5 m)"],
        ["Code 2", "Field Length 800 m to < 1,200 m", "Code B", "Wingspan 15 m to < 24 m (Gear span 4.5 to < 6 m)"],
        ["Code 3", "Field Length 1,200 m to < 1,800 m", "Code C", "Wingspan 24 m to < 36 m (Gear span 6 to < 9 m) [A320, B737]"],
        ["Code 4", "Field Length >= 1,800 m", "Code D", "Wingspan 36 m to < 52 m (Gear span 9 to < 14 m) [B767]"],
        ["—", "—", "Code E", "Wingspan 52 m to < 65 m (Gear span 9 to < 14 m) [B777, A350]"],
        ["—", "—", "Code F", "Wingspan 65 m to < 80 m (Gear span 14 to < 16 m) [A380, B747-8]"]
    ]
    pdf.add_table(["Code No.", "Airplane Reference Field Length", "Code Letter", "Wingspan & Outer Main Gear Wheel Span"], code_data, col_widths=[65.0, 175.0, 80.0, 190.0])

    pdf.add_heading_1("2. Runway Strips, Clearways & Stopways")
    pdf.add_bullet("Runway Strip", "A defined area including runway and stopway intended: 1) To reduce damage if aircraft veers off runway, 2) To protect aircraft flying over during take-off or landing. For Code 3/4 precision runways, extends 60 m beyond each runway end, with a total width of at least 280 m (140 m each side of centerline) or 300 m (150 m each side).")
    pdf.add_bullet("Clearway", "Rectangular area on ground or water under control of aerodrome, selected or prepared as suitable area over which an aeroplane may make a portion of its initial climb to a specified height. Maximum length shall not exceed HALF THE LENGTH OF TORA (Clearway max = 0.5 x TORA). Upward slope max 1.25%.")
    pdf.add_bullet("Stopway", "Defined rectangular area on ground at end of take-off run available, prepared as suitable area in which an aircraft can be stopped in the event of an abandoned take-off. Width equal to runway.")

    pdf.add_heading_1("3. Declared Distances (TORA, TODA, ASDA, LDA)")
    pdf.add_paragraph(
        "Declared distances are the operational lengths available for aircraft performance calculations:",
        max_chars=92
    )
    dist_data = [
        ["TORA (Take-Off Run Available)", "Length of runway declared available and suitable for the ground run of an aircraft taking off."],
        ["TODA (Take-Off Distance Available)", "TORA + Clearway. (The length of TORA plus length of clearway, if provided)."],
        ["ASDA (Accelerate-Stop Distance Available)", "TORA + Stopway. (The length of TORA plus length of stopway, if provided)."],
        ["LDA (Landing Distance Available)", "Length of runway declared available and suitable for the ground run of an aeroplane landing. Measured from threshold."]
    ]
    pdf.add_table(["Declared Distance", "Calculation Formula & Operational Definition"], dist_data, col_widths=[170.0, 340.0])

    pdf.add_callout(
        "trap",
        "Displaced Threshold & Practical Calculation Exercise",
        "When a runway threshold is DISPLACED (moved down the runway):\n"
        "• Landing Distance Available (LDA) is REDUCED by the displacement distance.\n"
        "• Take-Off Run Available (TORA), TODA, and ASDA are NOT reduced for take-off in that direction.\n"
        "• The area preceding a displaced threshold is suitable for take-off and roll, but NEVER for landing.",
        max_chars=86
    )

    pdf.add_heading_1("4. Runway End Safety Area (RESA)")
    pdf.add_paragraph(
        "An area symmetrical about extended runway centerline intended to reduce risk of damage to aircraft undershooting "
        "or overrunning runway. For Code 3 and 4 runways: minimum length is 90 m (recommended 240 m); width must be at "
        "least TWICE the width of the associated runway.",
        max_chars=92
    )

    pdf.add_heading_1("5. Obstacle Limitation Surfaces (OLS)")
    ols_data = [
        ["Approach Surface", "Inclined plane preceding threshold. Slope varies from 2.0% (Code 4 precision) to 3.3%."],
        ["Transitional Surface", "Complex surface sloping upward and outward from runway strip edges to the inner horizontal surface. Standard slope: 14.3% (1:7) for Code 3/4 runways."],
        ["Inner Horizontal Surface", "Circular horizontal plane located 45 m above aerodrome elevation (radius 4,000 m for Code 4). Protects visual maneuvering area."],
        ["Conical Surface", "Surface sloping upward and outward from perimeter of inner horizontal surface at a 5% slope to a specified height (100 m for Code 4)."],
        ["Balked Landing Surface", "Inclined plane located after threshold at a specified distance protecting aircraft executing a missed approach at very low altitude."]
    ]
    pdf.add_table(["OLS Surface", "Dimensions & Operational Protection Objective"], ols_data, col_widths=[140.0, 370.0])

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch18 = [
        ("Q1: What is the maximum allowable length of a clearway relative to TORA?",
         "[A] 25% of TORA\n[B] 50% of TORA\n[C] Equal to TORA\n[D] Unlimited provided slope is < 1.25%",
         "CORRECT: [B]. Under ICAO Annex 14, the length of a clearway shall not exceed half the length of the take-off run available (0.5 x TORA)."),
        ("Q2: At what height above aerodrome elevation is the Inner Horizontal Surface established?",
         "[A] 30 m\n[B] 45 m\n[C] 60 m\n[D] 100 m",
         "CORRECT: [B]. The Inner Horizontal Surface is located 45 m above the aerodrome elevation datum."),
        ("Q3: What is the standard minimum length of a Runway End Safety Area (RESA) for Code 4 runways?",
         "[A] 60 m\n[B] 90 m (recommended 240 m)\n[C] 120 m\n[D] 300 m",
         "CORRECT: [B]. Standard minimum RESA length is 90 m, with 240 m recommended by ICAO."),
        ("Q4: Given: Runway length = 2,500 m, Displaced threshold = 300 m, Clearway = 400 m, Stopway = 200 m. What is the Landing Distance Available (LDA)?",
         "[A] 2,500 m\n[B] 2,200 m\n[C] 2,700 m\n[D] 2,900 m",
         "CORRECT: [B]. LDA is measured from the threshold to runway end: 2,500 m - 300 m displacement = 2,200 m."),
        ("Q5: What is the slope of the transitional surface for a Code 4 precision approach runway?",
         "[A] 5.0%\n[B] 10.0%\n[C] 14.3% (1:7)\n[D] 20.0%",
         "CORRECT: [C]. The transitional surface slope for Code 4 runways is 14.3% (or 1:7).")
    ]
    for q_text, opts, exp in questions_ch18:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 18 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch13()
    build_ch14()
    build_ch15()
    build_ch16()
    build_ch17()
    build_ch18()
