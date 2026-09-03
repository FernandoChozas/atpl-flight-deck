#!/usr/bin/env python3
"""
Generator for 090 Communications (VFR + IFR)
Chapters 01 to 04:
- Chapter 01: General Operating Procedures, Phraseology & Phonetics
- Chapter 02: Radio Wave Propagation & Frequency Bands (VHF, HF, 8.33 kHz)
- Chapter 03: Aerodrome Control Communications (VFR & Ground)
- Chapter 04: Approach & En-route Control Communications (IFR & Radar)

Exclusively for 100% EASA / AviationExam self-sufficient study.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "resumenes", "convocatoria_1", "090_communications"
)
os.makedirs(BASE_DIR, exist_ok=True)

# ==============================================================================
# CHAPTER 01: GENERAL OPERATING PROCEDURES & PHRASEOLOGY (~4 pages)
# ==============================================================================
def build_ch01():
    pdf_path = os.path.join(BASE_DIR, "090_ch01_general_procedures_phraseology.pdf")
    pdf = PDFBuilder("Communications", "090", "Chapter 1: General Procedures & Phraseology")
    pdf.add_title_banner("Communications", 1, "General Procedures & Phraseology", "1-32")

    pdf.add_heading_1("1. The ICAO Standard Radiotelephony Alphabet & Numbers")
    pdf.add_paragraph(
        "Aeronautical radiotelephony communications require absolute clarity and zero phonetic ambiguity. "
        "Standard ICAO phonetic spelling and number pronunciation must be used across all aeronautical frequencies:",
        max_chars=92
    )

    phonetic_data = [
        ["A - Alpha", "B - Bravo", "C - Charlie", "D - Delta", "E - Echo", "F - Foxtrot"],
        ["G - Golf", "H - Hotel", "I - India", "J - Juliett", "K - Kilo", "L - Lima"],
        ["M - Mike", "N - November", "O - Oscar", "P - Papa", "Q - Quebec", "R - Romeo"],
        ["S - Sierra", "T - Tango", "U - Uniform", "V - Victor", "W - Whiskey", "X - X-ray"],
        ["Y - Yankee", "Z - Zulu", "0 - ZE-RO", "1 - WUN", "2 - TOO", "3 - TREE"],
        ["4 - FOW-er", "5 - FIFE", "6 - SIX", "7 - SEV-en", "8 - AIT", "9 - NIN-er"]
    ]
    pdf.add_table(["Col 1", "Col 2", "Col 3", "Col 4", "Col 5", "Col 6"], phonetic_data, col_widths=[84.0, 84.0, 84.0, 84.0, 84.0, 85.0])

    pdf.add_callout(
        "trap",
        "AviationExam Number Transmission Rules (ICAO Doc 4444 / Annex 10)",
        "• General Rule: Each digit must be transmitted individually (e.g. FL 180 is 'FLIGHT LEVEL WUN AIT ZE-RO').\n"
        "• EXCEPTIONS for Whole Hundreds & Thousands:\n"
        "  - 800 is transmitted as 'AIT HUND-red'.\n"
        "  - 5,000 is transmitted as 'FIFE TOU-SAND'.\n"
        "  - 11,000 is transmitted as 'WUN WUN TOU-SAND'.\n"
        "  - 38,300 is transmitted as 'TREE AIT TOU-SAND TREE HUND-red'.\n"
        "• Altimeter Settings: 1013 hPa is 'WUN ZE-RO WUN TREE'. 29.92 inHg is 'TOO NIN-er DAY-SEE-MAL NIN-er TOO'.\n"
        "• 8.33 kHz Frequencies: All 6 digits must be spoken (e.g. 118.005 is 'WUN WUN AIT DAY-SEE-MAL ZE-RO ZE-RO FIFE'), "
        "EXCEPT when the 5th and 6th digits are both zero (e.g. 118.000 is 'WUN WUN AIT DAY-SEE-MAL ZE-RO').",
        max_chars=86
    )

    pdf.add_heading_1("2. Readability Scale (Signal Strength & Clarity 1 to 5)")
    read_data = [
        ["1", "Unreadable", "Signal cannot be understood at all."],
        ["2", "Readable now and then", "Only occasional words or syllables intelligible."],
        ["3", "Readable but with difficulty", "Message can be understood only with severe concentration and repeats."],
        ["4", "Readable", "Transmission clear with minor background noise or distortion."],
        ["5", "Perfectly readable", "Crystal clear audio quality; zero background noise or distortion."]
    ]
    pdf.add_table(["Scale Value", "Official ICAO Definition", "Operational Meaning & Quality"], read_data, col_widths=[80.0, 180.0, 245.0])

    pdf.add_heading_1("3. Standard ICAO Words and Phrases")
    words_data = [
        ["ROGER", "I have received all of your last transmission.", "CRITICAL: ROGER does NOT mean clearance, permission, or agreement! It means receipt only."],
        ["WILCO", "I understand your message and will comply with it.", "Combines ROGER and compliance. Never say 'ROGER WILCO' (redundant)."],
        ["AFFIRM / NEGATIVE", "'Yes' / 'No'", "Standard affirmations. Never use conversational slang ('Yeah', 'Nope')."],
        ["STANDBY", "Wait and I will call you.", "The caller must pause and wait; does not grant permission to act."],
        ["CORRECTION", "An error has been made in this transmission...", "The correct version follows immediately ('...correction heading 280')."],
        ["CLEARED", "Authorized to proceed under the conditions specified.", "Reserved strictly for air traffic control clearances."]
    ]
    pdf.add_table(["Phrase / Word", "ICAO Definition", "Operational Context & Exam Nuance"], words_data, col_widths=[105.0, 205.0, 195.0])

    pdf.add_heading_1("4. Aircraft Callsigns & Abbreviation Rules")
    pdf.add_bullet("Type A (Registration)", "Characters corresponding to aircraft registration (e.g. G-ABCD). May be abbreviated to first letter and at least last two (G-CD).")
    pdf.add_bullet("Type B (Operator + Registration)", "Telephony designator of operator + registration (e.g. SPEEDBIRD G-ABCD -> SPEEDBIRD CD).")
    pdf.add_bullet("Type C (Operator + Flight Number)", "Telephony designator + flight number (e.g. IBERIA 1234). NEVER ABBREVIATED under any circumstances!")
    pdf.add_bullet("Golden Rule of Abbreviation", "An aircraft station may use its abbreviated callsign ONLY AFTER it has been addressed in this manner by an air traffic communication station!")

    pdf.add_callout(
        "trap",
        "Mandatory Readback Items (AviationExam Absolute Core - ICAO Annex 11)",
        "The flight crew MUST read back verbatim:\n"
        "1. ATC route clearances;\n"
        "2. Clearances to enter, land on, take off on, hold short of, cross, taxi and backtrack on ANY runway;\n"
        "3. Runway-in-use, altimeter settings (QNH, QFE), SSR codes (squawk), level instructions, heading and speed instructions;\n"
        "4. Transition levels.",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: How should the frequency 118.005 MHz be transmitted over the radio under 8.33 kHz channel spacing?",
         "[A] 'One eighteen point zero zero'\n[B] 'One one eight decimal zero zero five'\n[C] 'One one eight point zero five'\n[D] 'One eighteen zero zero five'",
         "CORRECT: [B]. In 8.33 kHz channel spacing, all six digits must be pronounced: 'One one eight decimal zero zero five'."),
        ("Q2: How should an altimeter setting of 1013 hPa be pronounced in ICAO radiotelephony?",
         "[A] 'One thousand and thirteen'\n[B] 'Ten thirteen'\n[C] 'One zero one three'\n[D] 'One zero thirteen'",
         "CORRECT: [C]. Altimeter settings are transmitted by pronouncing each digit separately: 'One zero one three'."),
        ("Q3: What does the ICAO standard word 'ROGER' mean when transmitted by an aircraft?",
         "[A] I agree with your proposal\n[B] I have received all of your last transmission\n[C] I will comply with your instructions\n[D] Cleared as requested",
         "CORRECT: [B]. 'ROGER' means 'I have received all of your last transmission'. It does NOT mean compliance (which is 'WILCO') nor authorization."),
        ("Q4: When is a pilot permitted to use an abbreviated aircraft callsign (e.g. 'G-CD' instead of 'G-ABCD')?",
         "[A] Anytime after initial contact\n[B] Only after the ground station has first addressed the aircraft using the abbreviated callsign\n[C] In emergency situations only\n[D] When flying outside controlled airspace",
         "CORRECT: [B]. A pilot must use full callsign until the ground station initiates the abbreviation; only then may the pilot use the abbreviated callsign."),
        ("Q5: Which of the following instructions must ALWAYS be read back verbatim by the pilot?",
         "[A] Meteorological wind updates\n[B] Altimeter setting (QNH), runway-in-use, and holding point instructions\n[C] Time checks\n[D] Surface temperature and dew point",
         "CORRECT: [B]. Runway instructions, holding points, QNH, squawks, headings, speeds, and levels are strictly mandatory readback items under ICAO Doc 4444."),
        ("Q6: How is a transmission readability of '3' defined on the ICAO 1 to 5 scale?",
         "[A] Perfectly readable\n[B] Readable with difficulty\n[C] Readable now and then\n[D] Unreadable",
         "CORRECT: [B]. 1 = Unreadable, 2 = Readable now and then, 3 = Readable but with difficulty, 4 = Readable, 5 = Perfectly readable."),
        ("Q7: How should a pilot report climbing from FL 150 to FL 220 under standard ICAO radiotelephony?",
         "[A] 'Climbing to two twenty'\n[B] 'Leaving flight level one five zero, climbing to flight level two two zero'\n[C] 'Up to flight level two two zero'\n[D] 'Flight level two two zero now'",
         "CORRECT: [B]. When vacating a level, both the vacated level and the cleared level must be stated: 'Leaving flight level one five zero, climbing to flight level two two zero'."),
        ("Q8: Which component of an air traffic message does NOT require mandatory verbatim readback by the flight crew?",
         "[A] Altimeter setting (QNH)\n[B] Surface wind and ambient temperature\n[C] Transponder SSR squawk code\n[D] Runway holding point instructions",
         "CORRECT: [B]. Surface wind, temperature, and runway surface condition are advisory reports and do not require verbatim readback, unlike instructions, levels, and QNH.")
    ]
    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Comms Chapter 1 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 02: RADIO WAVE PROPAGATION & FREQUENCY BANDS (~4 pages)
# ==============================================================================
def build_ch02():
    pdf_path = os.path.join(BASE_DIR, "090_ch02_propagation_frequency_bands.pdf")
    pdf = PDFBuilder("Communications", "090", "Chapter 2: Propagation & Frequency Bands")
    pdf.add_title_banner("Communications", 2, "Propagation & Frequency Bands", "33-60")

    pdf.add_heading_1("1. The Radio Frequency Spectrum & Aeronautical Bands")
    bands_data = [
        ["VLF (Very Low Frequency)", "3 to 30 kHz", "Worldwide navigation, submarine communications."],
        ["LF (Low Frequency)", "30 to 300 kHz", "Non-Directional Beacons (NDB), commercial broadcast."],
        ["MF (Medium Frequency)", "300 to 3,000 kHz", "NDBs, commercial AM radio (subject to night effect)."],
        ["HF (High Frequency)", "3 to 30 MHz", "Long-range oceanic & polar aeronautical communications (Skywave)."],
        ["VHF (Very High Frequency)", "30 to 300 MHz", "Aeronautical RTF (118.000 - 136.975 MHz), VOR (108.0-117.95 MHz), ILS Localizer (108.1-111.95 MHz), Emergency (121.500 MHz)."],
        ["UHF (Ultra High Frequency)", "300 to 3,000 MHz", "ILS Glidepath (329.15-335 MHz), DME, SSR (1030/1090 MHz), GPS (1575.42 MHz), Military Guard (243.0 MHz)."],
        ["SHF (Super High Frequency)", "3 to 30 GHz", "Airborne Weather Radar (9 GHz), MLS (5 GHz), Satellite communications."]
    ]
    pdf.add_table(["Band Name", "Frequency Range", "Aeronautical Applications"], bands_data, col_widths=[140.0, 100.0, 265.0])

    pdf.add_heading_1("2. VHF Propagation & Theoretical Range Formula")
    pdf.add_paragraph(
        "VHF radio waves travel essentially by direct 'space wave' (line of sight). Atmospheric refraction bends waves "
        "slightly downward around the curvature of the Earth (effective earth radius = 4/3 of true radius):",
        max_chars=92
    )

    pdf.add_callout(
        "trap",
        "The Master VHF Radio Range Formula (AviationExam Absolute Core)",
        "Range (NM) = 1.23 x ( sqrt(h_aircraft [ft]) + sqrt(h_ground_station [ft]) )\n\n"
        "• Example 1: Aircraft at FL 100 (10,000 ft), ground station at sea level (0 ft):\n"
        "  Range = 1.23 x sqrt(10,000) = 1.23 x 100 = 123 NM.\n"
        "• Example 2: Aircraft at FL 360 (36,000 ft), ground station at 400 ft:\n"
        "  Range = 1.23 x ( sqrt(36,000) + sqrt(400) ) = 1.23 x (189.7 + 20) = 1.23 x 209.7 = ~258 NM!\n"
        "• Note: Optical horizon uses 1.06; Radio horizon uses 1.23 due to atmospheric refraction!",
        max_chars=86
    )

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: VHF Line-of-Sight Range and 8.33 kHz Channeling",
        "SCENARIO (AviationExam Standard Radiotelephony Calculation):\n"
        "An airliner is cruising at FL 360 (36,000 ft) en route to Madrid:\n"
        "- The Madrid ATC VHF transmitter antenna is located on a hill at 400 ft AMSL\n"
        "QUESTION: What is the maximum theoretical VHF two-way communication range in Nautical Miles (NM)?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Identify the Master Refracted Line-of-Sight Formula:\n"
        "  - Master Equation: Range (NM) = 1.23 x [ sqrt(h_aircraft) + sqrt(h_station) ]\n"
        "  - (Factor is 1.23 for radio waves due to atmospheric refraction, vs 1.06 for visible light!).\n\n"
        "Step 2: Calculate the Square Roots of the Heights:\n"
        "  - Aircraft Height h1 = 36,000 ft --> sqrt(36,000) = 189.74\n"
        "  - Ground Station Height h2 = 400 ft --> sqrt(400) = 20.00\n"
        "  - Sum of roots = 189.74 + 20.00 = 209.74\n\n"
        "Step 3: Multiply by the 1.23 Refraction Factor:\n"
        "  - Range = 1.23 x 209.74 = 257.98 NM (~258 Nautical Miles)!\n\n"
        "FINAL ANSWER: Maximum VHF communication range is 258 NM! Beyond this distance, the direct VHF space wave is blocked by the curvature of the Earth.",
        max_chars=86
    )

    pdf.add_heading_1("4. HF Skywave Propagation & The Ionosphere")
    pdf.add_paragraph(
        "High Frequency (HF: 3-30 MHz) propagates over thousands of miles via ionospheric refraction (skywave):",
        max_chars=92
    )
    pdf.add_bullet("Ionospheric Layers", "D layer (50-90 km, daytime only, ABSORBS HF waves); E layer (90-140 km); F1 & F2 layers (140-400 km, merge into single F layer at night, REFLECTS HF waves back to Earth).")
    pdf.add_bullet("Day vs Night Frequencies", "DAY: Higher frequencies (10-18 MHz) required to penetrate the absorbing D layer and reach the F layer. NIGHT: Lower frequencies (3-8 MHz) required because the D layer vanishes and the F layer refracts lower frequencies.")
    pdf.add_bullet("Dead Zone (Skip Zone)", "The area between the outer limit of the ground wave and the first returning sky wave where NO HF SIGNAL can be received.")
    pdf.add_bullet("SELCAL (Selective Calling)", "An automated ground-to-air audio tone signaling system (4 letters, e.g. AB-CD). Alerts flight crew with chime and light, eliminating the need to listen to continuous static noise on HF.")

    pdf.add_heading_1("4. 8.33 kHz Channel Spacing Transition")
    pdf.add_paragraph(
        "To relieve severe VHF channel congestion in European airspace, the channel spacing was reduced from 25 kHz "
        "to 8.33 kHz (dividing each 25 kHz channel into three 8.33 kHz channels). Carriage of 8.33 kHz capable radio "
        "equipment is mandatory across all controlled airspace in the European ICAO region.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: What is the theoretical VHF radio communication range between an aircraft at FL 250 (25,000 ft) and a ground station at sea level?",
         "[A] 123 NM\n[B] 195 NM\n[C] 250 NM\n[D] 320 NM",
         "CORRECT: [B]. Formula: Range = 1.23 x sqrt(h) = 1.23 x sqrt(25,000) = 1.23 x 158.11 = 194.5 NM (~195 NM)."),
        ("Q2: Why must a higher frequency band be selected for HF communications during the daytime compared to nighttime?",
         "[A] Atmospheric pressure is higher during the day\n[B] The D layer of the ionosphere forms during daytime and strongly absorbs lower HF frequencies\n[C] Solar wind turns off the F layer\n[D] Transmitters require cooling at night",
         "CORRECT: [B]. Solar UV radiation ionizes the lower D layer during the day, which heavily absorbs low frequencies; higher frequencies are required to penetrate to the reflecting F layer."),
        ("Q3: What is the 'Dead Space' (Skip Zone) in HF radio communications?",
         "[A] An area where aircraft engines fail\n[B] The geographic area between the limit of the ground wave and the first returning sky wave where no signal is received\n[C] The blind cone directly above a VOR station\n[D] Space above the ionosphere",
         "CORRECT: [B]. The skip zone is the silent gap between the ground wave coverage limit and the touchdown point of the first ionospheric skywave."),
        ("Q4: What is the primary operational function of the SELCAL (Selective Calling) system?",
         "[A] Automatically transmitting emergency MAYDAY messages\n[B] Relieving the flight crew from continuously monitoring noisy HF audio frequencies\n[C] Calculating aircraft ground speed\n[D] Encoding digital transponder codes",
         "CORRECT: [B]. SELCAL monitors the HF frequency and alerts the crew with a chime and visual annunciator only when the ground station calls their specific 4-letter code."),
        ("Q5: In which frequency band does the international aeronautical emergency frequency 121.500 MHz operate?",
         "[A] HF (High Frequency)\n[B] VHF (Very High Frequency)\n[C] UHF (Ultra High Frequency)\n[D] LF (Low Frequency)",
         "CORRECT: [B]. 121.500 MHz is located in the VHF band (30 to 300 MHz)."),
        ("Q6: What is the primary benefit of introducing 8.33 kHz channel spacing in European VHF communications?",
         "[A] Doubling transmitter power\n[B] Tripling the number of available communication channels to alleviate severe spectrum congestion\n[C] Increasing VHF range to 1,000 NM\n[D] Eliminating thunderstorm static",
         "CORRECT: [B]. Dividing 25 kHz channels into three 8.33 kHz channels triples available frequency channels.")
    ]
    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Comms Chapter 2 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 03: AERODROME CONTROL COMMUNICATIONS (~4 pages)
# ==============================================================================
def build_ch03():
    pdf_path = os.path.join(BASE_DIR, "090_ch03_aerodrome_control.pdf")
    pdf = PDFBuilder("Communications", "090", "Chapter 3: Aerodrome Control Communications")
    pdf.add_title_banner("Communications", 3, "Aerodrome Control Communications", "61-88")

    pdf.add_heading_1("1. Departure Information & Pushback / Start-up")
    pdf.add_paragraph(
        "Prior to requesting start-up or taxi, the flight crew must monitor ATIS and obtain local aerodrome information:",
        max_chars=92
    )
    pdf.add_bullet("ATIS Acknowledgment", "'INFORMATION CHARLIE RECEIVED, QNH 1014'.")
    pdf.add_bullet("Start-up Request", "Pilot: 'REQUEST START UP'. Controller: 'START UP APPROVED' or 'EXPECT START UP AT 35'.")
    pdf.add_bullet("Pushback Request", "Pilot: 'REQUEST PUSHBACK'. Controller: 'PUSHBACK APPROVED, FACING EAST'.")
    pdf.add_bullet("Taxi Request", "Pilot: 'REQUEST TAXI'. Controller: 'TAXI TO HOLDING POINT RUNWAY 27 VIA TAXIWAY ALPHA'. Readback: 'TAXI TO HOLDING POINT RUNWAY 27 VIA TAXIWAY ALPHA, IBERIA 123'.")

    pdf.add_heading_1("2. Holding Point Procedures & Runway Crossings")
    pdf.add_callout(
        "trap",
        "Runway Safety & Mandatory Holding Point Readback",
        "• A clearance to 'TAXI TO HOLDING POINT RUNWAY 27' is NOT a clearance to enter the runway!\n"
        "• The aircraft MUST HOLD SHORT of the yellow illuminated runway holding position markings.\n"
        "• Runway Crossing: Requires explicit, distinct clearance: 'CROSS RUNWAY 09, REPORT VACATED'. "
        "The readback MUST include the runway designator: 'CROSS RUNWAY 09, WILCO, IBERIA 123'.",
        max_chars=86
    )

    pdf.add_heading_1("3. Conditional Clearances (Strict ICAO Format)")
    pdf.add_paragraph(
        "Conditional clearances involve an aircraft being cleared to line up, cross, or take off subject to a preceding "
        "movement. To eliminate runway incursions, ICAO mandates a strict 3-part phrasing sequence:",
        max_chars=92
    )

    cond_data = [
        ["1. The Condition", "Preceding traffic identification", "'IBERIA 456, BEHIND LANDING AIRBUS A320...'"],
        ["2. The Clearance", "Action authorized", "'...LINE UP AND WAIT RUNWAY 27...'"],
        ["3. Repetition of Condition", "Re-affirmation of restriction", "'...BEHIND.'"],
        ["Mandatory Readback", "Full verbatim repetition", "'BEHIND LANDING AIRBUS A320, LINE UP AND WAIT RUNWAY 27 BEHIND, IBERIA 456.'"]
    ]
    pdf.add_table(["Conditional Element", "Operational Purpose", "Exact ICAO Phraseology Example"], cond_data, col_widths=[125.0, 155.0, 225.0])

    pdf.add_heading_1("4. Take-off, Aborted Take-off & Landing Clearances")
    pdf.add_bullet("Line Up & Wait", "'LINE UP AND WAIT RUNWAY 27' (or 'LINE UP RUNWAY 27 AND WAIT').")
    pdf.add_bullet("Take-off Clearance", "'CLEARED FOR TAKE-OFF RUNWAY 27, WIND 250 DEGREES 10 KNOTS'. Readback: 'CLEARED FOR TAKE-OFF RUNWAY 27, IBERIA 123'.")
    pdf.add_bullet("Cancelling Take-off Clearance (Before Roll)", "Controller: 'TAKE-OFF CLEARANCE CANCELLED, HOLD POSITION'. Pilot: 'HOLDING, IBERIA 123'.")
    pdf.add_bullet("Aborting Take-off (Emergency During Roll)", "Controller: 'STOP IMMEDIATELY, IBERIA 123 STOP IMMEDIATELY'. Pilot: 'STOPPING, IBERIA 123'.")
    pdf.add_bullet("Landing Clearance", "'CLEARED TO LAND RUNWAY 27, WIND 260 DEGREES 12 KNOTS'.")
    pdf.add_bullet("Missed Approach / Go-Around", "Controller: 'GO AROUND, CLIMB TO 3000 FEET'. Pilot: 'GOING AROUND, IBERIA 123'.")
    pdf.add_bullet("Runway Vacated", "Pilot: 'RUNWAY VACATED' (transmitted only after the entire aircraft is clear of the runway holding markings).")

    pdf.add_heading_1("5. VFR Traffic Circuit Position Reports")
    circuit_data = [
        ["Downwind", "Opposite direction to landing", "Transmit aircraft type, intentions (touch-and-go / full stop): 'G-ABCD, DOWNWIND RUNWAY 27, TOUCH AND GO'."],
        ["Base Leg", "Turn onto base", "Transmit: 'G-ABCD, BASE RUNWAY 27'."],
        ["Final", "Aligned with runway (< 4 NM)", "Transmit: 'G-ABCD, FINAL RUNWAY 27'."],
        ["Long Final", "Aligned at greater distance", "Transmit: 'G-ABCD, LONG FINAL RUNWAY 27' (between 4 and 8 NM from touchdown)."]
    ]
    pdf.add_table(["Circuit Position", "Flight Path Geometry", "Standard ICAO Radio Phraseology"], circuit_data, col_widths=[110.0, 155.0, 240.0])

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: What is the correct phraseology used by a controller to instruct an aircraft to abort its take-off roll immediately?",
         "[A] 'Abort take-off, cancel clearance'\n[B] 'Stop immediately, Speedbird 123 stop immediately'\n[C] 'Speedbird 123, hold position'\n[D] 'Discontinue take-off now'",
         "CORRECT: [B]. The standard emergency phraseology to abort an active take-off roll is 'STOP IMMEDIATELY' repeated twice, addressed with aircraft callsign."),
        ("Q2: In a conditional clearance, what must be transmitted first by the controller?",
         "[A] The clearance to line up\n[B] The condition (identification of preceding traffic)\n[C] The surface wind\n[D] The aircraft callsign followed by 'cleared'",
         "CORRECT: [B]. Under ICAO standards, the condition must always precede the clearance (e.g. 'Behind landing B737, line up and wait behind')."),
        ("Q3: When should a pilot transmit the phrase 'RUNWAY VACATED'?",
         "[A] As soon as the main wheels touch down\n[B] When the nose gear crosses the runway edge line\n[C] Only when the entire aircraft has passed beyond the runway holding position marking\n[D] When parked on the apron",
         "CORRECT: [C]. 'Runway vacated' is transmitted only when all parts of the aircraft are completely past the runway holding line."),
        ("Q4: An aircraft is instructed: 'Taxi to holding point runway 09 via taxiway Bravo'. Does this authorize the aircraft to cross runway 09?",
         "[A] Yes, if no traffic is visible\n[B] No, the pilot must hold short of runway 09 until receiving an explicit clearance to cross\n[C] Yes, after transmitting 'Crossing'\n[D] Only in daytime VMC",
         "CORRECT: [B]. Taxi clearances to a holding point strictly terminate at the holding point. Crossing any runway requires an explicit separate clearance."),
        ("Q5: What is the correct phraseology for an aircraft commencing a missed approach on final approach?",
         "[A] 'Aborting landing'\n[B] 'Going around'\n[C] 'Pulling up'\n[D] 'Cancelling landing'",
         "CORRECT: [B]. 'GOING AROUND' is the standard ICAO radiotelephony phraseology for initiating a missed approach."),
        ("Q6: At what distance from the runway threshold is an aircraft considered to be on 'Long Final'?",
         "[A] Between 1 and 2 NM\n[B] Between 4 and 8 NM\n[C] Beyond 15 NM\n[D] Under 1 NM",
         "CORRECT: [B]. 'Long Final' is reported when an aircraft is turning onto final approach or tracking final at a distance greater than 4 NM (typically 4 to 8 NM).")
    ]
    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Comms Chapter 3 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 04: APPROACH & EN-ROUTE CONTROL COMMUNICATIONS (~4 pages)
# ==============================================================================
def build_ch04():
    pdf_path = os.path.join(BASE_DIR, "090_ch04_approach_enroute_control.pdf")
    pdf = PDFBuilder("Communications", "090", "Chapter 4: Approach & En-route Communications")
    pdf.add_title_banner("Communications", 4, "Approach & En-route Communications", "89-118")

    pdf.add_heading_1("1. IFR Departure Clearances & Level Instructions")
    pdf.add_paragraph(
        "Initial IFR clearances contain route of flight, assigned SID, initial altitude/FL, and transponder squawk code:",
        max_chars=92
    )
    pdf.add_bullet("Clearance Delivery", "'IBERIA 123, CLEARED TO PARIS CHARLES DE GAULLE VIA PINUS 1A DEPARTURE, CLIMB FLIGHT LEVEL 80, SQUAWK 4215'.")
    pdf.add_bullet("Climb & Descent Phrasing", "'CLIMB TO FLIGHT LEVEL 240', 'DESCEND TO 4000 FEET QNH 1018'.")
    pdf.add_bullet("Transition Altitude & Level", "Transition Altitude (TA) is referenced to QNH (feet). Transition Level (TL) is referenced to standard pressure 1013.25 hPa (Flight Levels). Transition Layer is the airspace between TA and TL.")

    pdf.add_heading_1("2. Standard En-route Position Reporting")
    pdf.add_paragraph(
        "Unless operating under radar coverage where 'Radar Contact' has been confirmed and position reports waived, "
        "an IFR flight must transmit standard position reports over designated compulsory reporting points:",
        max_chars=92
    )

    pos_data = [
        ["1. Aircraft Identification", "Callsign", "'IBERIA 123'"],
        ["2. Position", "Compulsory reporting fix", "'OVER CLACTON'"],
        ["3. Time", "Minutes past the hour", "'AT 25'"],
        ["4. Flight Level / Altitude", "Present level", "'FLIGHT LEVEL 280'"],
        ["5. Next Position & Estimate", "Next fix and estimated time", "'ESTIMATING OTFORD AT 42'"],
        ["6. Ensuing Significant Point", "Subsequent fix name", "'NEXT LYDD'"]
    ]
    pdf.add_table(["Report Element", "Description", "Standard Radiotelephony Phrasing"], pos_data, col_widths=[130.0, 150.0, 225.0])

    pdf.add_heading_1("3. Radar Vectoring & Speed Control Commands")
    pdf.add_bullet("Vectoring Instructions", "'TURN LEFT HEADING 090', 'LEAVE HEADING 270 FLY HEADING 310', 'FLY HEADING 040 FOR INTERCEPT'.")
    pdf.add_bullet("Speed Control", "'MAINTAIN 250 KNOTS', 'REDUCE TO MINIMUM CLEAN SPEED', 'RESUME NORMAL SPEED'.")
    pdf.add_bullet("Intercepting Localizer", "'CLEARED ILS APPROACH RUNWAY 24, REPORT ESTABLISHED ON LOCALIZER'.")

    pdf.add_heading_1("4. Surveillance Radar Approach (SRA)")
    pdf.add_paragraph(
        "A Surveillance Radar Approach (SRA) is an instrument approach guided by a radar controller transmitting "
        "heading instructions and advisory altitudes per nautical mile from touchdown:",
        max_chars=92
    )

    pdf.add_callout(
        "trap",
        "SRA Transmission Intervals & Missed Approach Criteria (Exam Trap)",
        "• Transmission Frequency on Final Approach: The radar controller must transmit to the aircraft at intervals "
        "of NOT MORE THAN 5 SECONDS during final approach!\n"
        "• Missed Approach Rule: If no transmission is received from the controller for an interval of 5 SECONDS "
        "(or 15 seconds in some national procedures), the pilot MUST IMMEDIATELY EXECUTE A MISSED APPROACH!\n"
        "• Termination of SRA: The controller terminates the approach at 2 NM from touchdown (or 1/2 NM for high-precision SRA), "
        "or when the pilot reports the runway in sight.",
        max_chars=86
    )

    pdf.add_heading_1("5. Controller-Pilot Data Link Communications (CPDLC)")
    pdf.add_paragraph(
        "CPDLC allows direct two-way digital text messaging between ground ATC automation and the aircraft FMS. "
        "Benefits include eliminating voice frequency congestion, accents, and garbled transmissions. "
        "Standard crew responses to CPDLC uplink clearances are: WILCO, UNABLE, STANDBY, or ROGER.",
        max_chars=92
    )

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: What are the required elements of a standard ICAO position report in that exact sequence?",
         "[A] Callsign, Altitude, Speed, Fuel, Next point\n[B] Callsign, Position, Time, Flight Level, Next position and estimated time, Ensuing significant point\n[C] Callsign, Heading, Wind, Estimated time of arrival\n[D] Callsign, Squawk code, Distance to go",
         "CORRECT: [B]. The mandatory sequence is: Callsign -> Position -> Time -> Flight Level -> Next position & estimate -> Ensuing point."),
        ("Q2: During a Surveillance Radar Approach (SRA), what action must the pilot take if radio contact with the radar controller is lost for more than 5 seconds on final approach?",
         "[A] Continue descent to MDA and land visual\n[B] Immediately execute a missed approach\n[C] Switch to tower frequency and land\n[D] Orbit in place",
         "CORRECT: [B]. On SRA final approach, communications failure (> 5s silence) mandates an immediate missed approach climb."),
        ("Q3: At what approximate distance from touchdown is a standard Surveillance Radar Approach (SRA) terminated by the controller?",
         "[A] 10 NM\n[B] 5 NM\n[C] 2 NM (or 1/2 NM if high-precision)\n[D] At the runway threshold",
         "CORRECT: [C]. Standard SRA terminates at 2 NM from touchdown (or 0.5 NM if certified to lower minima)."),
        ("Q4: What phrase does a pilot transmit upon becoming established on the ILS localizer course?",
         "[A] 'Localizer captured'\n[B] 'Established on localizer' (or 'Established runway 27')\n[C] 'On the beam'\n[D] 'ILS locked'",
         "CORRECT: [B]. 'ESTABLISHED' or 'ESTABLISHED ON LOCALIZER' is the standard ICAO radiotelephony report."),
        ("Q5: What does the instruction 'RESUME NORMAL SPEED' signify to a flight crew following ATC speed restrictions?",
         "[A] Accelerate to maximum speed Vmo\n[B] The previously issued speed restriction is cancelled; pilot flies normal operational flight plan speeds\n[C] Fly exactly 250 kt\n[D] Slow down to approach speed",
         "CORRECT: [B]. 'Resume normal speed' cancels ATC-imposed speed control, returning aircraft to operator's flight plan profile."),
        ("Q6: What is the primary operational objective of CPDLC in oceanic and en-route airspace?",
         "[A] Replacing visual scans\n[B] Eliminating voice frequency congestion and audio language misunderstandings through digital text messaging\n[C] Automatically controlling aircraft engines\n[D] Providing weather radar pictures",
         "CORRECT: [B]. CPDLC replaces voice communications with structured data messages, reducing HF/VHF frequency congestion.")
    ]
    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Comms Chapter 4 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch01()
    build_ch02()
    build_ch03()
    build_ch04()
