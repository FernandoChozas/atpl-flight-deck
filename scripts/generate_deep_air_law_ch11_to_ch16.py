#!/usr/bin/env python3
"""
Deep Comprehensive Generator for 010 Air Law (Chapters 11 to 16).
Designed for 100% self-contained study without textbooks.
Includes:
- Chapter 11: Parallel Runway Operations & PRM (2 pages)
- Chapter 12: SSR and ACAS (TCAS II v7.1) (2 pages)
- Chapter 13: Airspace Classification (Classes A to G Master Table) (3 pages)
- Chapter 14: Air Traffic Services & Emergency Phases (2 pages)
- Chapter 15: Separation (RVSM, Radar, Non-Radar, Wake Turbulence) (3 pages)
- Chapter 16: Control of Aircraft & Emergencies (Fuel, Comms Failure) (2 pages)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

# ==============================================================================
# CHAPTER 11: PARALLEL RUNWAY OPERATIONS
# ==============================================================================
def build_ch11():
    pdf_path = os.path.join(BASE_DIR, "010_ch11_parallel_runways.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 11: Parallel Runway Operations")
    pdf.add_title_banner("Air Law", 11, "Parallel Runway Operations", "239-252")

    pdf.add_heading_1("1. Modes of Operation & Minimum Centerline Spacing")
    pdf.add_paragraph(
        "Simultaneous operations on parallel or near-parallel runways are governed by ICAO Doc 4444 (PANS-ATM) "
        "and Doc 8168. Minimum centerline separation distances are strictly tested:",
        max_chars=92
    )

    rwy_data = [
        ["Independent Parallel Approaches", "At least 1,035 m (3,400 ft)", "Simultaneous approaches where radar separation between aircraft on adjacent ILS localizers is NOT required. Requires dedicated radar monitor controllers."],
        ["Dependent Parallel Approaches", "At least 915 m (3,000 ft)", "Simultaneous approaches where radar separation minima (stagger) between aircraft on adjacent extended centerlines IS required (usually 1.5 or 2.0 NM)."],
        ["Independent Parallel Departures", "At least 1,035 m (3,400 ft)", "Simultaneous departures where departure tracks diverge immediately by at least 15° after take-off."],
        ["Segregated Parallel Operations", "At least 760 m (2,500 ft)", "One runway is used exclusively for departures, and the other runway is used exclusively for arrivals."]
    ]
    pdf.add_table(["Operational Mode", "Min. Centerline Spacing", "Operational Criteria & Stagger Requirements"], rwy_data, col_widths=[115.0, 115.0, 280.0])

    pdf.add_heading_1("2. Protected Zones: NOZ and NTZ")
    pdf.add_bullet("Normal Operating Zone (NOZ)", "An airspace corridor extending from runway threshold to point where aircraft intercepts ILS, within which aircraft are expected to maneuver.")
    pdf.add_bullet("No Transgression Zone (NTZ)", "A non-maneuvering corridor of at least 610 m (2,000 ft) width located centrally between the two extended runway centerlines. Penetration by an aircraft requires immediate controller breakout instructions.")

    pdf.add_callout(
        "trap",
        "NTZ Penetration & Breakout Instructions",
        "When an aircraft is observed penetrating the NTZ, the radar controller immediately instructs the "
        "threatened aircraft on the adjacent localizer to execute a BREAKOUT MANEUVER (e.g. 'Turn left immediately "
        "heading 270, climb to 3,000 ft'). The pilot must execute the breakout without delay.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Min centerline spacing for independent parallel approaches? -> 1,035 m.")
    pdf.add_bullet("Q2", "Min centerline spacing for dependent parallel approaches? -> 915 m.")
    pdf.add_bullet("Q3", "Min centerline spacing for segregated parallel operations? -> 760 m.")
    pdf.add_bullet("Q4", "Width of the No Transgression Zone (NTZ)? -> At least 610 m (2,000 ft).")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 11 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 12: SSR AND ACAS
# ==============================================================================
def build_ch12():
    pdf_path = os.path.join(BASE_DIR, "010_ch12_ssr_acas.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 12: SSR and ACAS (TCAS II)")
    pdf.add_title_banner("Air Law", 12, "SSR and ACAS (TCAS II)", "253-262")

    pdf.add_heading_1("1. Secondary Surveillance Radar (SSR) Modes")
    pdf.add_bullet("Mode A", "4-digit octal code (4,096 combinations) for aircraft identification assigned by ATC.")
    pdf.add_bullet("Mode C", "Transmits automated pressure altitude (referenced to 1013.25 hPa) in 100 ft increments.")
    pdf.add_bullet("Mode S", "Transmits unique 24-bit aircraft address; selective interrogation; enhanced surveillance parameters (Downlink Airborne Parameters - DAP: selected altitude, roll angle, IAS, Mach).")

    pdf.add_callout(
        "trap",
        "Mandatory Emergency Transponder Codes (Memorize 100%)",
        "• 7500: Unlawful Interference (Hijacking).\n"
        "• 7600: Lost Communications (Radio Failure).\n"
        "• 7700: General Emergency / Distress.\n"
        "• 7000: Standard VFR conspicuity in Europe (1200 in USA).\n"
        "• 2000: Default IFR entry code into uncontrolled airspace or oceanic control without assigned code.",
        max_chars=86
    )

    pdf.add_heading_1("2. Airborne Collision Avoidance System (ACAS II / TCAS II)")
    pdf.add_paragraph(
        "ACAS II interrogates Mode C/S transponders of nearby aircraft to provide warnings based on Time to CPA (tau):",
        max_chars=92
    )

    acas_data = [
        ["Traffic Advisory (TA)", "Amber solid circle", "20 to 48 seconds to CPA", "Audio: 'TRAFFIC, TRAFFIC'. Visual scan only. NO EVASIVE MANEUVER PERMITTED."],
        ["Resolution Advisory (RA)", "Red solid square", "15 to 35 seconds to CPA", "Audio: 'CLIMB', 'DESCEND', etc. Vertical evasive instruction. Pilot MUST disconnect autopilot and comply immediately."]
    ]
    pdf.add_table(["Warning Level", "Display Symbol", "Time to CPA (Tau)", "Cockpit Action & Pilot Response"], acas_data, col_widths=[105.0, 100.0, 100.0, 205.0])

    pdf.add_callout(
        "trap",
        "Pilot Response Time & Absolute Priority of TCAS RA",
        "1. Response Time: Pilot must initiate response within 5 SECONDS for initial RA, and within 2.5 SECONDS for "
        "an increased or reversal RA (G-load 0.25 g initial, 0.35 g reversal).\n"
        "2. RA vs ATC Clearance: TCAS RA OVERRULES ATC CLEARANCE. If an RA contradicts an ATC instruction, the pilot "
        "MUST follow the RA without hesitation, and advise ATC as soon as possible ('TCAS RA').",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Transponder code for hijacking? -> 7500.")
    pdf.add_bullet("Q2", "Transponder code for radio failure? -> 7600.")
    pdf.add_bullet("Q3", "Pilot response time to an initial TCAS RA? -> 5 seconds (2.5 s for reversal).")
    pdf.add_bullet("Q4", "If ATC says 'Descend' but TCAS says 'Climb', which do you follow? -> Follow the TCAS RA ('Climb').")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 12 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 13: AIRSPACE CLASSIFICATION
# ==============================================================================
def build_ch13():
    pdf_path = os.path.join(BASE_DIR, "010_ch13_airspace.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 13: Airspace Organization & Classification")
    pdf.add_title_banner("Air Law", 13, "Airspace Classes (A to G)", "263-278")

    pdf.add_heading_1("1. Master Airspace Classification Table (ICAO & SERA)")
    pdf.add_paragraph(
        "Airspace is categorized into 7 classes (A to G). Classes A to E are Controlled Airspace; "
        "Classes F and G are Uncontrolled Airspace:",
        max_chars=92
    )

    air_data = [
        ["Class A", "IFR only", "IFR from IFR", "Continuous 2-way", "ATC Clearance MANDATORY.\nVFR is PROHIBITED."],
        ["Class B", "IFR & VFR", "All flights from all flights", "Continuous 2-way", "ATC Clearance MANDATORY.\nFull separation to all."],
        ["Class C", "IFR & VFR", "IFR from IFR & VFR.\nVFR from IFR only.", "Continuous 2-way", "ATC Clearance MANDATORY.\nVFR gets traffic info on VFR."],
        ["Class D", "IFR & VFR", "IFR from IFR only.", "Continuous 2-way", "ATC Clearance MANDATORY.\nTraffic info given to VFR on all."],
        ["Class E", "IFR & VFR", "IFR from IFR only.", "Continuous 2-way for IFR only", "Clearance MANDATORY for IFR.\nVFR does NOT need clearance or radio!"],
        ["Class F", "IFR & VFR", "None (Advisory only)", "Continuous for participating IFR", "Uncontrolled. IFR gets air traffic advisory service."],
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

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Can VFR fly in Class A airspace? -> NO, strictly IFR only.")
    pdf.add_bullet("Q2", "In Class C, does ATC separate VFR from VFR? -> NO (only traffic information provided).")
    pdf.add_bullet("Q3", "Standard speed limit below FL 100? -> 250 kt IAS.")
    pdf.add_bullet("Q4", "Does a VFR flight need an ATC clearance in Class E? -> NO.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 13 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 14: AIR TRAFFIC SERVICES
# ==============================================================================
def build_ch14():
    pdf_path = os.path.join(BASE_DIR, "010_ch14_air_traffic_services.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 14: Air Traffic Services")
    pdf.add_title_banner("Air Law", 14, "Air Traffic Services & Emergencies", "279-296")

    pdf.add_heading_1("1. The Three Core Air Traffic Services (ATS)")
    pdf.add_bullet("1. Air Traffic Control (ATC)", "Prevents collisions between aircraft and between aircraft and obstacles on the maneuvering area, and expedites and maintains an orderly flow of traffic. (Subdivided into: Area Control ACC, Approach Control APP, Aerodrome Control TWR).")
    pdf.add_bullet("2. Flight Information Service (FIS)", "Provides advice and information useful for the safe and efficient conduct of flights (weather, changes in serviceability of nav aids, traffic information).")
    pdf.add_bullet("3. Alerting Service (ALRS)", "Notifies appropriate organizations regarding aircraft in need of search and rescue aid, and assists such organizations as required. Provided to ALL aircraft provided with ATC, or submitting a flight plan.")

    pdf.add_heading_1("2. The Three Emergency Phases (Annex 11 / 12)")
    phases_data = [
        ["1. INCERFA (Uncertainty Phase)", "No communication within 30 minutes after time it should have been received, OR aircraft fails to arrive within 30 minutes of ETA."],
        ["2. ALERFA (Alert Phase)", "Following INCERFA, attempts to communicate fail; OR aircraft cleared to land fails to land within 5 minutes of ETA; OR operating efficiency impaired."],
        ["3. DETRESFA (Distress Phase)", "Following ALERFA, or fuel on board considered exhausted, or information indicates aircraft about to make forced landing or has crashed."]
    ]
    pdf.add_table(["Emergency Phase", "Official Activation Criteria (AviationExam Core)"], phases_data, col_widths=[145.0, 365.0])

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Time limit for lack of communication to trigger INCERFA? -> 30 minutes.")
    pdf.add_bullet("Q2", "Failure to land after clearance that triggers ALERFA? -> 5 minutes after ETA.")
    pdf.add_bullet("Q3", "When fuel is considered exhausted, what phase is declared? -> DETRESFA.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 14 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 15: SEPARATION METHODS AND MINIMA
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

    pdf.add_heading_1("3. Wake Turbulence Categories (MTOM)")
    wake_data = [
        ["SUPER", "Airbus A380-800", "Special category created for A380."],
        ["HEAVY (H)", "136,000 kg or more", "Wide-body aircraft (B777, A350, A330, B747)."],
        ["MEDIUM (M)", "Between 7,000 kg and 136,000 kg", "Standard single-aisle jets (A320, B737) and regional aircraft."],
        ["LIGHT (L)", "7,000 kg or less", "Light twins and single-engine aircraft (C172, PA-28, King Air)."]
    ]
    pdf.add_table(["Category", "Max Certified Take-Off Mass (MTOM)", "Representative Aircraft Types"], wake_data, col_widths=[90.0, 195.0, 225.0])

    pdf.add_heading_1("4. Wake Turbulence Separation Minima")
    sep_data = [
        ["Behind HEAVY", "Heavy: 4 NM", "Medium: 5 NM", "Light: 6 NM"],
        ["Behind MEDIUM", "Heavy: Radar min", "Medium: Radar min", "Light: 5 NM"]
    ]
    pdf.add_table(["Preceding Aircraft", "Trailing Heavy", "Trailing Medium", "Trailing Light"], sep_data, col_widths=[125.0, 125.0, 125.0, 135.0])

    pdf.add_callout(
        "trap",
        "Timed Departure Wake Turbulence Separation (Non-Radar)",
        "When taking off behind a HEAVY aircraft from the same runway:\n"
        "• Full length of runway: 2 MINUTES separation.\n"
        "• From an INTERMEDIATE intersection (displaced threshold): 3 MINUTES separation (due to vortex drift).",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "RVSM airspace vertical separation? -> 1,000 ft between FL 290 and FL 410.")
    pdf.add_bullet("Q2", "MTOM threshold for HEAVY category? -> 136,000 kg or more.")
    pdf.add_bullet("Q3", "Radar wake separation for a LIGHT aircraft behind a HEAVY? -> 6 NM.")
    pdf.add_bullet("Q4", "Departure delay for Medium behind Heavy from an intersection? -> 3 minutes.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 15 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 16: CONTROL OF AIRCRAFT & EMERGENCIES
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

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Does 'MINIMUM FUEL' give you priority over other aircraft? -> NO.")
    pdf.add_bullet("Q2", "What radio call gives absolute priority for low fuel? -> 'MAYDAY MAYDAY MAYDAY FUEL'.")
    pdf.add_bullet("Q3", "How long do you maintain level/speed in IMC radio failure? -> 7 minutes (3 mins on radar vector).")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 16 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch11()
    build_ch12()
    build_ch13()
    build_ch14()
    build_ch15()
    build_ch16()
