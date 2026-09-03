#!/usr/bin/env python3
"""
Generator for 090 Communications (VFR + IFR)
Chapters 05 to 07:
- Chapter 05: Weather Broadcasts & Meteorological Information (ATIS, VOLMET, SIGMET)
- Chapter 06: Distress & Urgency Procedures (MAYDAY vs PAN PAN, 121.5 MHz, 7700)
- Chapter 07: Communications Failure & Aerodrome Light Signals (7600, VMC vs IMC, Aldis Lamp)

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
# CHAPTER 05: WEATHER BROADCASTS & METEOROLOGICAL INFORMATION (~4 pages)
# ==============================================================================
def build_ch05():
    pdf_path = os.path.join(BASE_DIR, "090_ch05_weather_broadcasts.pdf")
    pdf = PDFBuilder("Communications", "090", "Chapter 5: Weather Broadcasts & Met Information")
    pdf.add_title_banner("Communications", 5, "Weather Broadcasts & Met Information", "119-142")

    pdf.add_heading_1("1. Automatic Terminal Information Service (ATIS)")
    pdf.add_paragraph(
        "ATIS is the continuous broadcast of recorded non-control aeronautical and meteorological information "
        "at high-density aerodromes. Its primary operational purpose is to relieve ATC frequency congestion:",
        max_chars=92
    )

    pdf.add_bullet("Identification Designator", "Each ATIS broadcast is identified by a phonetic letter from the ICAO alphabet (ALPHA through ZULU). When updated, the designator increments sequentially.")
    pdf.add_bullet("Crew Acknowledgment", "On initial contact with Approach or Tower, flight crew must state receipt of the broadcast code letter and QNH: 'INFORMATION ECHO RECEIVED, QNH 1013'.")
    pdf.add_bullet("Voice vs D-ATIS", "Voice ATIS is broadcast on dedicated VHF channels or VOR voice subcarriers. D-ATIS (Data link ATIS) transmits digital text directly into the aircraft cockpit FMS/ACARS printer.")

    pdf.add_heading_1("2. Standard ATIS Content & Message Sequence")
    atis_data = [
        ["1. Aerodrome & Code", "'GATWICK INFORMATION FOXTROT'"],
        ["2. Observation Time", "'TIME 1420 UTC'"],
        ["3. Expected Approach & Runway", "'EXPECT ILS APPROACH RUNWAY 26L'"],
        ["4. Runway Surface Conditions", "'RUNWAY WET WET WET'"],
        ["5. Transition Level", "'TRANSITION LEVEL 60'"],
        ["6. Surface Wind", "'WIND 240 DEGREES 15 KNOTS GUSTING 25 KNOTS'"],
        ["7. Visibility & RVR", "'VISIBILITY 4000 METRES, RVR RUNWAY 26L 1200 METRES'"],
        ["8. Present Weather & Clouds", "'MODERATE RAIN, FEW 800 FEET, BROKEN 1500 FEET'"],
        ["9. Temperature, Dewpoint & QNH", "'TEMPERATURE 12, DEWPOINT 10, QNH 1014'"],
        ["10. Operational Warnings", "'WINDSHEAR REPORTED ON FINAL APPROACH'"]
    ]
    pdf.add_table(["Message Element", "Exact Broadcast Format Example"], atis_data, col_widths=[175.0, 325.0])

    pdf.add_heading_1("3. VOLMET, SIGMET & AIRMET Broadcasts")
    pdf.add_paragraph(
        "• VOLMET: Continuous broadcast of routine aerodrome weather reports (METAR), special reports (SPECI), "
        "and 9-hour trend forecasts (TAF) for major airports, transmitted over scheduled VHF and HF frequencies.\n"
        "• SIGMET: Warning issued by a Meteorological Watch Office (MWO) concerning en-route weather phenomena "
        "which may affect the SAFETY OF ALL AIRCRAFT (e.g. severe turbulence, severe icing, thunderstorm lines, volcanic ash).\n"
        "• AIRMET: Information for low-level flights (below FL 100 or FL 150) regarding weather phenomena not included "
        "in regional forecasts (moderate icing, moderate turbulence, widespread IMC).",
        max_chars=92
    )

    pdf.add_heading_1("4. Radiotelephony Weather Terminology & CAVOK")
    pdf.add_callout(
        "trap",
        "The Official Definition of 'CAVOK' (Ceiling And Visibility OK)",
        "The term 'CAVOK' replaces visibility, present weather, and cloud groups when ALL FOUR conditions are met:\n"
        "1. Visibility is 10 KILOMETRES OR MORE;\n"
        "2. No cloud of operational significance (NO CLOUD BELOW 5,000 FT or below the highest Minimum Sector Altitude, whichever is greater);\n"
        "3. NO CUMULONIMBUS (CB) and NO TOWERING CUMULUS (TCU) at any altitude;\n"
        "4. No significant weather phenomena (no rain, snow, fog, thunderstorm, etc.).",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: Which of the following conditions is mandatory to report 'CAVOK' in an aeronautical weather broadcast?",
         "[A] Visibility 5 km and sky clear\n[B] Visibility 10 km or more, no clouds below 5,000 ft or MSA, no CB/TCU at any level, and no significant weather\n[C] Wind calm and temperature above freezing\n[D] QNH exactly 1013.25 hPa",
         "CORRECT: [B]. CAVOK requires >= 10 km visibility, no clouds below 5,000 ft or MSA, no CB or TCU at any altitude, and no significant weather."),
        ("Q2: How does an ATIS broadcast identify that new or updated meteorological information has been published?",
         "[A] A tone sounds on the emergency frequency\n[B] The phonetic letter designator advances to the next sequential letter (e.g. from Bravo to Charlie)\n[C] The frequency changes\n[D] The broadcast announces 'Flash update'",
         "CORRECT: [B]. ATIS messages are identified sequentially by phonetic letters (Alpha through Zulu) with each newly issued observation."),
        ("Q3: What type of meteorological broadcast provides warnings of severe en-route weather hazardous to ALL aircraft?",
         "[A] METAR\n[B] TAF\n[C] SIGMET\n[D] ATIS",
         "CORRECT: [C]. SIGMET is an en-route safety warning issued for phenomena that affect the safety of all aircraft (severe icing/turbulence, volcanic ash)."),
        ("Q4: What is the primary purpose of a VOLMET broadcast?",
         "[A] Providing aerodrome control tower instructions\n[B] Providing current METARs, SPECIs, and TAFs for major international aerodromes to aircraft in flight\n[C] Monitoring ELT distress beacons\n[D] Broadcasting satellite navigation corrections",
         "CORRECT: [B]. VOLMET broadcasts surface weather reports and aerodrome forecasts to airborne aircraft over VHF and HF."),
        ("Q5: How should a pilot acknowledge receipt of ATIS information 'Golf' on initial radio contact with Approach?",
         "[A] 'We have the weather'\n[B] 'Information Golf received, QNH 1018'\n[C] 'Roger Golf'\n[D] 'Weather checked'",
         "CORRECT: [B]. The pilot must explicitly state the phonetic designator ('Information Golf received') and read back the altimeter setting (QNH)."),
        ("Q6: In an RVR report, what does the designation 'R26L/P1500' signify?",
         "[A] Runway 26 Left RVR is exactly 1,500 feet\n[B] Runway 26 Left RVR is greater than 1,500 metres\n[C] Runway 26 Left is closed for 1,500 seconds\n[D] Precision approach required",
         "CORRECT: [B]. The prefix 'P' indicates that the Runway Visual Range exceeds the maximum reporting capability of the transmissometer (greater than 1,500 m).")
    ]
    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Comms Chapter 5 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 06: DISTRESS & URGENCY PROCEDURES (~4 pages)
# ==============================================================================
def build_ch06():
    pdf_path = os.path.join(BASE_DIR, "090_ch06_distress_urgency_procedures.pdf")
    pdf = PDFBuilder("Communications", "090", "Chapter 6: Distress & Urgency Procedures")
    pdf.add_title_banner("Communications", 6, "Distress & Urgency Procedures", "143-168")

    pdf.add_heading_1("1. Distress vs Urgency States (ICAO Definitions)")
    states_data = [
        ["Distress (MAYDAY)", "Spoken 3 TIMES: 'MAYDAY, MAYDAY, MAYDAY'", "Condition of being threatened by grave and/or imminent danger and of requiring immediate assistance (e.g. dual engine failure, uncontrolled in-flight fire, structural failure, forced landing / ditching)."],
        ["Urgency (PAN PAN)", "Spoken 3 TIMES: 'PAN PAN, PAN PAN, PAN PAN'", "Condition concerning the safety of an aircraft or other vehicle, or of some person on board or within sight, but which does NOT require immediate assistance (e.g. critical passenger medical condition, lost orientation with safe fuel, single engine failure in twin cruise)."]
    ]
    pdf.add_table(["Emergency State", "Radiotelephony Callout", "ICAO Definition & Aeronautical Scenarios"], states_data, col_widths=[125.0, 160.0, 215.0])

    pdf.add_heading_1("2. International Emergency Frequencies & Squawk Codes")
    pdf.add_paragraph(
        "A distress or urgency call should normally be made on the frequency in current use. If unable, or if no contact "
        "is established, transmit on the international emergency frequencies:",
        max_chars=92
    )

    pdf.add_bullet("121.500 MHz", "International VHF Aeronautical Emergency Frequency (VHF Guard). Continuously monitored by military, civil ATC, and oceanic stations.")
    pdf.add_bullet("243.000 MHz", "International UHF Military Emergency Frequency (UHF Guard).")
    pdf.add_bullet("406.0 MHz", "Digital Emergency Locator Transmitter (ELT) satellite frequency. Detected by the Cospas-Sarsat constellation; transmits unique 24-bit aircraft hex code. 121.5 MHz is retained for localized homing.")

    pdf.add_callout(
        "trap",
        "The Three Master Emergency Transponder Squawks (Memorize 100%)",
        "• Squawk 7700: GENERAL EMERGENCY (Distress or Urgency condition);\n"
        "• Squawk 7600: RADIO COMMUNICATION FAILURE (Complete loss of two-way radio);\n"
        "• Squawk 7500: UNLAWFUL INTERFERENCE (Hijacking / aircraft seizure).\n"
        "Note: In an emergency, select 7700 immediately on the Mode A/C transponder. This triggers automated audio and visual alarms on ATC radar consoles!",
        max_chars=86
    )

    pdf.add_heading_1("3. Structure of a Distress Message (Order of Priority)")
    pdf.add_paragraph(
        "Under ICAO Annex 10, a distress message must contain the following information in sequence:",
        max_chars=92
    )

    dist_order = [
        ["1. Distress Call", "'MAYDAY, MAYDAY, MAYDAY'"],
        ["2. Addressed Station", "'MADRID RADAR' (or 'ALL STATIONS')"],
        ["3. Aircraft Callsign", "'IBERIA 456' (spoken 3 times on initial call)"],
        ["4. Nature of Distress", "'ENGINE FIRE ON ENGINE NUMBER ONE'"],
        ["5. Pilot Intentions", "'DESCENDING IMMEDIATELY, DIVERTING TO BARCELONA'"],
        ["6. Present Position & Level", "'POSITION 20 NM SOUTH OF REUS, FLIGHT LEVEL 150, HEADING 040'"],
        ["7. Additional Information", "'142 PERSONS ON BOARD, FUEL ENDURANCE TWO HOURS'"]
    ]
    pdf.add_table(["Transmission Order", "Exact ICAO Radiotelephony Phrasing"], dist_order, col_widths=[165.0, 335.0])

    pdf.add_heading_1("4. Radio Silence, Relay & Emergency Termination")
    pdf.add_bullet("Imposing Radio Silence", "The aircraft in distress or the controlling station can order all other traffic to cease transmitting: 'STOP TRANSMITTING, MAYDAY' (or 'SILENCE MAYDAY').")
    pdf.add_bullet("MAYDAY RELAY", "Transmitted when an aircraft observes another aircraft in distress that cannot transmit its own message: 'MAYDAY RELAY, MAYDAY RELAY, MAYDAY RELAY'.")
    pdf.add_bullet("Termination of Distress", "When the emergency has ended: Aircraft transmits 'CANCEL DISTRESS'; the controlling station transmits 'DISTRESS TRAFFIC ENDED'.")

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: How is a condition of 'Distress' distinguished from a condition of 'Urgency' in ICAO radiotelephony?",
         "[A] Distress uses PAN PAN; Urgency uses MAYDAY\n[B] Distress indicates grave and imminent danger requiring immediate assistance; Urgency concerns safety but does not require immediate assistance\n[C] Distress applies only on the ground\n[D] Urgency requires immediate ditching",
         "CORRECT: [B]. Distress (MAYDAY) = grave and imminent danger requiring immediate assistance. Urgency (PAN PAN) = safety concern not requiring immediate assistance."),
        ("Q2: What is the primary international aeronautical emergency frequency in the VHF band?",
         "[A] 118.000 MHz\n[B] 121.500 MHz\n[C] 123.450 MHz\n[D] 243.000 MHz",
         "CORRECT: [B]. 121.500 MHz is the international VHF aeronautical emergency frequency (VHF Guard). 243.000 MHz is UHF military guard."),
        ("Q3: Which SSR transponder code must be set immediately when an aircraft encounters an in-flight emergency?",
         "[A] 7000\n[B] 7500\n[C] 7600\n[D] 7700",
         "CORRECT: [D]. Squawk 7700 indicates general emergency (distress or urgency). 7600 is radio failure; 7500 is unlawful interference."),
        ("Q4: What phraseology is used by an air traffic controller to impose radio silence on a frequency during an active emergency?",
         "[A] 'Silence on the frequency'\n[B] 'Stop transmitting, MAYDAY'\n[C] 'All aircraft maintain radio silence'\n[D] 'Standby all stations'",
         "CORRECT: [B]. Standard ICAO phraseology to impose radio silence is 'STOP TRANSMITTING, MAYDAY'."),
        ("Q5: What is the correct phraseology transmitted by an aircraft to cancel a previously declared PAN PAN urgency condition?",
         "[A] 'Emergency cancelled'\n[B] 'Cancel PAN PAN, situation resolved'\n[C] 'Disregard PAN PAN'\n[D] 'Back to normal'",
         "CORRECT: [B]. The pilot transmits 'CANCEL PAN PAN' followed by callsign and current status."),
        ("Q6: On what satellite frequency do modern digital Emergency Locator Transmitters (ELTs) transmit encoded distress alerts to the Cospas-Sarsat system?",
         "[A] 121.5 MHz\n[B] 243.0 MHz\n[C] 406.0 MHz\n[D] 1090 MHz",
         "CORRECT: [C]. Modern digital ELTs transmit digital distress data on 406.0 MHz to rescue satellites, retaining 121.5 MHz for final acoustic homing.")
    ]
    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Comms Chapter 6 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 07: COMMUNICATIONS FAILURE & TOWER LIGHT SIGNALS (~4 pages)
# ==============================================================================
def build_ch07():
    pdf_path = os.path.join(BASE_DIR, "090_ch07_communications_failure.pdf")
    pdf = PDFBuilder("Communications", "090", "Chapter 7: Communications Failure & Light Signals")
    pdf.add_title_banner("Communications", 7, "Communications Failure & Light Signals", "169-194")

    pdf.add_heading_1("1. Action on Suspected Communications Failure")
    pdf.add_paragraph(
        "When two-way radio communication is lost, the flight crew must perform systematic cockpit checks:\n"
        "1. Check frequency selector, audio control panel switches, volume, squelch, and headset plugs;\n"
        "2. Attempt contact on previous ATC frequency, company frequency, or 121.500 MHz;\n"
        "3. If receiver failure is suspected, transmit blind: 'TRANSMITTING BLIND DUE TO RECEIVER FAILURE' "
        "(transmit the message twice, including present position, intentions, and time of next transmission);\n"
        "4. Set transponder Mode A/C code to 7600!",
        max_chars=92
    )

    pdf.add_heading_1("2. Radio Failure Procedures: VMC vs IMC (ICAO Annex 2)")
    pdf.add_paragraph(
        "The mandatory operational procedure depends strictly on current meteorological flight conditions:",
        max_chars=92
    )

    proc_data = [
        ["Flight in VMC", "1. Set squawk 7600;\n2. Continue flight in Visual Meteorological Conditions (VMC);\n3. Land at the NEAREST SUITABLE AERODROME;\n4. Report arrival to ATC by the most expeditious means (telephone)."],
        ["Flight in IMC (Non-Radar)", "1. Set squawk 7600;\n2. Maintain assigned speed and level for 20 MINUTES following failure to report over a compulsory reporting point, then conform to filed flight plan;\n3. Proceed to destination nav-aid; hold until EAT (or ETA if no EAT);\n4. Commence descent at EAT/ETA and land within 30 MINUTES."],
        ["Flight in IMC (Radar)", "1. Set squawk 7600;\n2. Maintain assigned speed and level for 7 MINUTES following 7600 selection or failure to report, then conform to flight plan;\n3. Proceed to destination nav-aid, commence descent at EAT/ETA, and land within 30 MINUTES."]
    ]
    pdf.add_table(["Meteorological Condition", "Mandatory ICAO Operational Failure Procedure"], proc_data, col_widths=[145.0, 355.0])

    pdf.add_callout(
        "trap",
        "AviationExam Critical Numbers: 7 Minutes vs 20 Minutes in IMC",
        "• IN AIRSPACE WHERE RADAR IS USED: Maintain assigned speed and level for 7 MINUTES, then follow flight plan!\n"
        "• IN AIRSPACE WHERE RADAR IS NOT USED: Maintain assigned speed and level for 20 MINUTES, then follow flight plan!\n"
        "• Holding & Descent: Hold at the designated destination navigation aid until the last acknowledged EAT "
        "(Expected Approach Time), or ETA if no EAT was given. Land within 30 MINUTES of EAT or ETA!",
        max_chars=86
    )

    pdf.add_heading_1("3. Master Table of Aerodrome Light Signals from Control Tower")
    pdf.add_paragraph(
        "In the event of complete radio failure, the aerodrome control tower directs aircraft using an Aldis lamp "
        "(focused optical light gun). Memorize this entire matrix for AviationExam:",
        max_chars=92
    )

    light_data = [
        ["Steady Green", "CLEARED TO LAND", "CLEARED FOR TAKE-OFF"],
        ["Flashing Green", "RETURN FOR LANDING (Wait for steady green)", "CLEARED TO TAXI"],
        ["Steady Red", "GIVE WAY TO OTHER AIRCRAFT & CONTINUE CIRCLING", "STOP"],
        ["Flashing Red", "AERODROME UNSAFE, DO NOT LAND", "TAXI CLEAR OF RUNWAY IN USE"],
        ["Flashing White", "LAND AT THIS AERODROME & PROCEED TO APRON", "RETURN TO STARTING POINT ON AERODROME"],
        ["Red Pyrotechnic (Flare)", "NOTWITHSTANDING PREVIOUS INSTRUCTIONS, DO NOT LAND FOR THE TIME BEING", "DO NOT LAND FOR THE TIME BEING"]
    ]
    pdf.add_table(["Light Signal from Tower", "Meaning to Aircraft IN FLIGHT", "Meaning to Aircraft ON GROUND"], light_data, col_widths=[130.0, 185.0, 185.0])

    pdf.add_heading_1("4. Aircraft Acknowledgement of Tower Light Signals")
    pdf.add_bullet("In Flight (Daylight)", "Rocking the aircraft's wings (except on final approach).")
    pdf.add_bullet("In Flight (Night)", "Flashing landing lights twice, or if not equipped, flashing navigation lights twice.")
    pdf.add_bullet("On Ground (Daylight)", "Moving the ailerons or rudder.")
    pdf.add_bullet("On Ground (Night)", "Flashing landing lights twice, or flashing navigation lights twice.")

    pdf.add_heading_1("5. SSR Transponder Modes & Data Link (Mode S)")
    ssr_data = [
        ["Mode A", "4-digit octal code (4096 combinations)", "Provides identity only (e.g. Squawk 7600). Does not transmit altitude."],
        ["Mode C", "Pressure altitude reporting", "Transmits standard pressure altitude referenced to 1013.25 hPa in 100-foot increments."],
        ["Mode S", "Discrete 24-bit aircraft address", "Selective interrogation; altitude reporting in 25-foot increments; downlinks aircraft parameters (DAP: selected altitude, roll angle, IAS/Mach). Mandatory in European airspace."]
    ]
    pdf.add_table(["Transponder Mode", "Data Transmitted to ATC", "Operational Role & European Mandate"], ssr_data, col_widths=[125.0, 175.0, 200.0])

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: What does a STEADY RED light signal from the aerodrome control tower mean to an aircraft in flight?",
         "[A] Cleared to land\n[B] Aerodrome unsafe, do not land\n[C] Give way to other aircraft and continue circling\n[D] Return to starting point",
         "CORRECT: [C]. To an aircraft in flight, Steady Red means 'Give way to other aircraft and continue circling'. (On ground, it means 'Stop')."),
        ("Q2: What does a FLASHING RED light signal from the control tower mean to an aircraft on the ground?",
         "[A] Stop immediately\n[B] Taxi clear of runway in use\n[C] Cleared to taxi\n[D] Return to starting point",
         "CORRECT: [B]. Flashing Red to an aircraft on the ground means 'Taxi clear of runway in use'. (In flight, it means 'Aerodrome unsafe, do not land')."),
        ("Q3: What does a FLASHING WHITE light signal from the control tower mean to an aircraft on the ground?",
         "[A] Cleared for take-off\n[B] Stop\n[C] Return to starting point on the aerodrome\n[D] Cleared to taxi",
         "CORRECT: [C]. Flashing White on the ground instructs the pilot to 'Return to starting point on the aerodrome'."),
        ("Q4: An IFR aircraft experiences complete communication failure in IMC while operating in an airspace where radar IS USED. How long must the pilot maintain assigned level and speed before adjusting to the flight plan?",
         "[A] 3 minutes\n[B] 7 minutes\n[C] 20 minutes\n[D] 30 minutes",
         "CORRECT: [B]. In radar airspace, the pilot maintains assigned speed and level for 7 minutes. In non-radar airspace, the requirement is 20 minutes."),
        ("Q5: If an aircraft experiences complete two-way communication failure in VMC, what is the mandatory course of action?",
         "[A] Continue IFR flight plan to original destination\n[B] Set transponder to 7600, continue in VMC, land at nearest suitable aerodrome, and report to ATC\n[C] Hold over the nearest VOR for 20 minutes\n[D] Climb to FL 150",
         "CORRECT: [B]. Under ICAO Annex 2, radio failure in VMC requires maintaining VMC, landing at the nearest suitable aerodrome, and reporting arrival."),
        ("Q6: How does an aircraft in flight acknowledge light signals from the control tower during the hours of daylight?",
         "[A] By rocking the aircraft's wings (except on base and final)\n[B] By firing a green flare\n[C] By deploying spoilers\n[D] By cycling the landing gear",
         "CORRECT: [A]. In daylight, an airborne aircraft acknowledges tower light signals by rocking its wings."),
        ("Q7: What does a RED PYROTECHNIC FLARE fired from the control tower signify to an aircraft on final approach?",
         "[A] Cleared to land immediately\n[B] Notwithstanding any previous instructions, do not land for the time being\n[C] Windshear warning\n[D] Runway surface wet",
         "CORRECT: [B]. A red flare fired from the ground unconditionally forbids landing: 'Notwithstanding any previous instructions, do not land for the time being'."),
        ("Q8: What resolution of pressure altitude reporting is provided by Mode S transponders compared to classic Mode C?",
         "[A] Exactly the same (100 ft increments)\n[B] 25-foot increments (compared to 100 ft in Mode C)\n[C] 1-foot increments\n[D] 500-foot increments",
         "CORRECT: [B]. Mode S transponders report pressure altitude in fine 25-foot increments, significantly improving ACAS II and ATC conflict detection compared to Mode C's 100-foot increments.")
    ]
    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Comms Chapter 7 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch05()
    build_ch06()
    build_ch07()
