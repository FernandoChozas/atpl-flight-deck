#!/usr/bin/env python3
"""
Generator for 010 Air Law:
- Chapter 11: Parallel Runway Operations (Independent 1035m, Dependent 915m, Segregated 760m, NTZ/NOZ)
- Chapter 12: SSR & ACAS (Modes A/C/S, 7500/7600/7700, TCAS II TA/RA, 5s response, RA priority)
- Chapter 13: Airspace Organization & Classification (Classes A-G master table, 250 kt rule, Special use)
- Chapter 14: Air Traffic Services (ATC, FIS, ALRS, INCERFA/ALERFA/DETRESFA)
- Chapter 15: Separation (RVSM 1000 ft, Radar 5NM/3NM, Wake turbulence categories Super/H/M/L, 2/3 min time)
- Chapter 16: Control of Aircraft & Emergencies (Radar vectors, MINIMUM FUEL vs MAYDAY FUEL, Comms failure)

Generates publication-grade, study-friendly PDFs and Markdown files.
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
    md_path = os.path.join(BASE_DIR, "010_ch11_parallel_runways.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 11: Parallel Runway Operations")
    pdf.add_title_banner("Air Law", 11, "Parallel Runway Operations", "239-252")

    pdf.add_heading_1("1. Modes of Operation & Minimum Centerline Spacing")
    pdf.add_paragraph(
        "Simultaneous operations on parallel or near-parallel runways require strict minimum runway separation "
        "distances and dedicated radar monitoring according to ICAO PANS-ATM / PANS-OPS:",
        max_chars=92
    )

    rwy_table = [
        ["Independent Parallel Approaches", "At least 1,035 m (3,400 ft)", "Simultaneous approaches to parallel runways where radar separation between aircraft on adjacent ILS localizers is NOT required."],
        ["Dependent Parallel Approaches", "At least 915 m (3,000 ft)", "Simultaneous approaches where radar separation minima (stagger) between aircraft on adjacent extended centerlines IS required (usually 1.5 or 2.0 NM)."],
        ["Independent Parallel Departures", "At least 1,035 m (3,400 ft)", "Simultaneous departures where departure tracks diverge immediately by at least 15° after take-off."],
        ["Segregated Parallel Operations", "At least 760 m (2,500 ft)", "One runway is used exclusively for departures, and the other runway is used exclusively for arrivals."]
    ]
    pdf.add_table(
        ["Mode of Operation", "Min. Centerline Distance", "Operational Definition & Criteria"],
        rwy_table,
        col_widths=[110.0, 115.0, 280.0]
    )

    pdf.add_heading_1("2. Operating Zones: NOZ and NTZ")
    pdf.add_bullet("Normal Operating Zone (NOZ)", "An airspace corridor extending from runway threshold to point where aircraft intercepts ILS, within which aircraft are expected to maneuver during approach.")
    pdf.add_bullet("No Transgression Zone (NTZ)", "A corridor of at least 610 m (2,000 ft) width located centrally between the two extended runway centerlines. Penetration by an aircraft requires immediate controller breakout instructions.")

    pdf.add_callout(
        "trap",
        "NTZ Penetration & Breakout Maneuver",
        "When an aircraft is observed penetrating the NTZ, the air traffic controller immediately issues a "
        "'BREAKOUT' instruction to the aircraft on the adjacent localizer (e.g. 'Turn left immediately heading 270, "
        "climb to 3,000 ft') to prevent collision. The aircraft must execute the breakout without delay.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Minimum runway centerline spacing for independent parallel approaches? -> 1,035 m.")
    pdf.add_bullet("Q2", "Minimum runway centerline spacing for dependent parallel approaches? -> 915 m.")
    pdf.add_bullet("Q3", "Minimum centerline spacing for segregated parallel operations? -> 760 m.")
    pdf.add_bullet("Q4", "Width of the No Transgression Zone (NTZ)? -> At least 610 m (2,000 ft).")

    pdf.compile_pdf(pdf_path)

    # Markdown
    md_content = """# 010 Air Law | Chapter 11: Parallel Runway Operations

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 11 (Pages 239 – 252) |
| **Difficulty Level** | 🟡 Medium (Runway separation distances, NTZ dimensions) |
| **Exam Weighting** | ⭐⭐ High (Regular numerical questions in AviationExam) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch11_parallel_runways.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch11_parallel_runways.pdf) |

---

## 1. Summary of Minimum Centerline Distances

| Operational Mode | Minimum Centerline Separation | Key Criteria |
| :--- | :---: | :--- |
| **Independent Parallel Approaches** | **1,035 m (3,400 ft)** | No radar separation required between aircraft on adjacent localizers. Dedicated radar monitor controller. |
| **Dependent Parallel Approaches** | **915 m (3,000 ft)** | Radar separation (stagger of 1.5 to 2 NM) maintained between adjacent approaches. |
| **Independent Parallel Departures** | **1,035 m (3,400 ft)** | Tracks must diverge by at least **15°** immediately after departure. |
| **Segregated Parallel Operations** | **760 m (2,500 ft)** | One runway used for departures only, the other for arrivals only. |

---

## 2. Protected Zones

* **Normal Operating Zone (NOZ)**: Extends from threshold to point of ILS intercept.
* **No Transgression Zone (NTZ)**: Non-maneuvering corridor of at least **610 m (2,000 ft)** width established centrally between extended centerlines.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 11: {pdf_path}")

# ==============================================================================
# CHAPTER 12: SSR AND ACAS
# ==============================================================================
def build_ch12():
    pdf_path = os.path.join(BASE_DIR, "010_ch12_ssr_acas.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch12_ssr_acas.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 12: SSR and ACAS")
    pdf.add_title_banner("Air Law", 12, "SSR and ACAS (TCAS II)", "253-262")

    pdf.add_heading_1("1. Secondary Surveillance Radar (SSR) Modes")
    pdf.add_bullet("Mode A", "4-digit octal code (4,096 combinations) for aircraft identification assigned by ATC.")
    pdf.add_bullet("Mode C", "Transmits automated pressure altitude (referenced to 1013.25 hPa) in 100 ft increments.")
    pdf.add_bullet("Mode S", "Transmits unique 24-bit aircraft address; selective interrogation; enhanced surveillance parameters (Downlink Airborne Parameters - DAP: selected altitude, roll angle, IAS, Mach).")

    pdf.add_callout(
        "trap",
        "Mandatory Emergency Transponder Codes",
        "• 7500: Unlawful Interference (Hijacking).\n"
        "• 7600: Lost Communications (Radio Failure).\n"
        "• 7700: General Emergency / Distress.\n"
        "• 7000: Standard VFR conspicuity in Europe (1200 in USA).\n"
        "• 2000: Default IFR entry code into uncontrolled airspace or oceanic control without assigned code.",
        max_chars=86
    )

    pdf.add_heading_1("2. Airborne Collision Avoidance System (ACAS II / TCAS II)")
    pdf.add_paragraph(
        "ACAS II operates by interrogating Mode C/S transponders of nearby aircraft. It provides warnings based "
        "on Time to Closest Point of Approach (tau):",
        max_chars=92
    )

    acas_table = [
        ["Traffic Advisory (TA)", "Yellow solid circle", "20 to 48 seconds to CPA", "Audio: 'TRAFFIC, TRAFFIC'. Helps flight crew visually acquire intruder. NO EVASIVE MANEUVER PERMITTED."],
        ["Resolution Advisory (RA)", "Red solid square", "15 to 35 seconds to CPA", "Audio: 'CLIMB', 'DESCEND', etc. Vertical evasive instruction. Crew MUST disconnect autopilot and comply immediately."]
    ]
    pdf.add_table(
        ["Alert Level", "Cockpit Symbol", "Time to CPA (Tau)", "Cockpit Action & Pilot Response"],
        acas_table,
        col_widths=[105.0, 95.0, 100.0, 205.0]
    )

    pdf.add_callout(
        "trap",
        "Pilot Response Time & ATC Conflict (Absolute Exam Core)",
        "1. Response Time: The pilot must initiate response within 5 SECONDS for initial RA, and within 2.5 SECONDS "
        "for an increased or reversal RA (G-load 0.25 g initial, 0.35 g reversal).\n"
        "2. RA vs ATC Clearance: TCAS RA OVERRULES ATC CLEARANCE. If an RA contradicts an ATC instruction, the "
        "pilot MUST follow the RA without hesitation, and advise ATC as soon as possible ('TCAS RA').",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Transponder code for unlawful interference? -> 7500.")
    pdf.add_bullet("Q2", "Transponder code for radio failure? -> 7600.")
    pdf.add_bullet("Q3", "Pilot response time to an initial TCAS RA? -> 5 seconds (2.5 s for reversal).")
    pdf.add_bullet("Q4", "If ATC says 'Descend' but TCAS says 'Climb, Climb', what must the pilot do? -> Follow the TCAS RA ('Climb').")

    pdf.compile_pdf(pdf_path)

    # Markdown
    md_content = """# 010 Air Law | Chapter 12: SSR and ACAS (TCAS II)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 12 (Pages 253 – 262) |
| **Difficulty Level** | 🔴 High (Emergency codes, ACAS timeframes, legal priority of RA over ATC) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Every sitting contains TCAS and emergency code questions) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch12_ssr_acas.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch12_ssr_acas.pdf) |

---

## 1. Emergency Transponder Codes

* **7500**: Unlawful Interference (Hijacking).
* **7600**: Radio Communication Failure.
* **7700**: General Emergency / Distress.
* **7000**: Standard VFR conspicuity code (Europe).
* **2000**: Default IFR code when entering airspace without an assigned squawk.

---

## 2. ACAS II (TCAS II version 7.1)

| Warning Level | Time to CPA | Display Symbol | Required Pilot Action |
| :--- | :---: | :---: | :--- |
| **Traffic Advisory (TA)** | 20 – 48 s | Amber circle | Visual scan only. **No evasive maneuver permitted.** |
| **Resolution Advisory (RA)** | 15 – 35 s | Red square | **Mandatory immediate response within 5 seconds** (2.5 s for reversal RA). Adjust vertical speed. |

> [!WARNING]
> **Priority Rule: TCAS RA vs ATC Clearance**
> In the event of a conflict between an ATC instruction and a TCAS RA, **the flight crew MUST follow the RA**. The pilot is protected legally and informs ATC as soon as possible.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 12: {pdf_path}")

# ==============================================================================
# CHAPTER 13: AIRSPACE
# ==============================================================================
def build_ch13():
    pdf_path = os.path.join(BASE_DIR, "010_ch13_airspace.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch13_airspace.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 13: Airspace Organization & Classification")
    pdf.add_title_banner("Air Law", 13, "Airspace Classes (A to G)", "263-278")

    pdf.add_heading_1("1. Master Table: ICAO/EASA Airspace Classes A to G")
    pdf.add_paragraph(
        "Airspace is categorized into 7 classes (A to G). Classes A to E are Controlled Airspace; "
        "Classes F and G are Uncontrolled Airspace:",
        max_chars=92
    )

    airspace_table = [
        ["Class A", "IFR only", "IFR from IFR", "Continuous 2-way", "ATC Clearance MANDATORY.\nVFR is PROHIBITED."],
        ["Class B", "IFR & VFR", "All flights from all", "Continuous 2-way", "ATC Clearance MANDATORY.\nFull separation to all."],
        ["Class C", "IFR & VFR", "IFR from IFR & VFR.\nVFR from IFR only.", "Continuous 2-way", "ATC Clearance MANDATORY.\nVFR gets traffic info on VFR."],
        ["Class D", "IFR & VFR", "IFR from IFR only.", "Continuous 2-way", "ATC Clearance MANDATORY.\nTraffic info given to VFR."],
        ["Class E", "IFR & VFR", "IFR from IFR only.", "Continuous 2-way for IFR only", "Clearance MANDATORY for IFR.\nVFR does NOT need clearance or radio!"],
        ["Class F", "IFR & VFR", "None (Advisory only)", "Continuous for participating IFR", "Uncontrolled. IFR gets air traffic advisory service."],
        ["Class G", "IFR & VFR", "None", "Continuous for IFR where required", "Uncontrolled. Flight Information Service (FIS) on request."]
    ]
    pdf.add_table(
        ["Class", "Flights", "Separation Provided", "Radio Comms", "ATC Clearance & Key Features"],
        airspace_table,
        col_widths=[60.0, 75.0, 115.0, 110.0, 145.0]
    )

    pdf.add_callout(
        "trap",
        "Class E Airspace: The Trap Question",
        "AviationExam Trap: 'Is an ATC clearance required to fly VFR in Class E airspace?' "
        "Answer: NO. In Class E, VFR flights do NOT require an ATC clearance and do NOT require two-way radio comms. "
        "Only IFR flights require ATC clearance and continuous communication in Class E.",
        max_chars=86
    )

    pdf.add_heading_1("2. Speed Limitations in Airspace")
    pdf.add_bullet("General Speed Limit", "A maximum speed of 250 kt IAS applies to all flights operating below FL 100 (or 10,000 ft AMSL), EXCEPT in Class A and B airspace, or when authorized by ATC.")

    pdf.add_heading_1("3. Special Use Airspace")
    pdf.add_bullet("Prohibited Area (P)", "Airspace of defined dimensions within which flight of aircraft is strictly prohibited (e.g. nuclear facilities, royal residences).")
    pdf.add_bullet("Restricted Area (R)", "Flight of aircraft is restricted in accordance with specified conditions (e.g. military firing ranges).")
    pdf.add_bullet("Danger Area (D)", "Activities dangerous to flight may exist at specified times (e.g. parachuting, aerobatics). Flight is not legally prohibited, but extreme caution required.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Can VFR fly in Class A airspace? -> NO, strictly IFR only.")
    pdf.add_bullet("Q2", "In Class C, does ATC separate VFR from VFR? -> NO (only traffic information is provided).")
    pdf.add_bullet("Q3", "Standard speed limit below FL 100? -> 250 kt IAS.")
    pdf.add_bullet("Q4", "Does a VFR flight need an ATC clearance in Class E? -> NO.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    md_content = """# 010 Air Law | Chapter 13: Airspace Organization & Classification

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 13 (Pages 263 – 278) |
| **Difficulty Level** | 🔴 High (Classes A to G comparison table, speed rules) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Heavily tested on every exam) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch13_airspace.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch13_airspace.pdf) |

---

## 1. Master Airspace Table (ICAO & SERA)

| Class | Permitted | Separation Provided | Radio Req. | Clearance Req. |
| :---: | :---: | :--- | :--- | :--- |
| **A** | IFR only | IFR from IFR | Continuous 2-way | **Yes** (VFR Prohibited) |
| **B** | IFR & VFR | All flights from all flights | Continuous 2-way | **Yes** (All) |
| **C** | IFR & VFR | IFR from IFR & VFR.<br>VFR from IFR only. | Continuous 2-way | **Yes** (All) *(VFR-VFR get traffic info only)* |
| **D** | IFR & VFR | IFR from IFR only. | Continuous 2-way | **Yes** (All) *(VFR get traffic info on all)* |
| **E** | IFR & VFR | IFR from IFR only. | Continuous (IFR only) | **IFR: Yes** \| **VFR: NO** |
| **F** | IFR & VFR | None (Advisory for IFR) | Continuous (participating) | **No** (Uncontrolled) |
| **G** | IFR & VFR | None | None (except IFR where req) | **No** (Uncontrolled) |

---

## 2. Speed Limits & Special Airspace

* **250 kt IAS below FL 100 (10,000 ft AMSL)**: Applies in Classes C, D, E, F, G.
* **Prohibited (P)**: Flight forbidden.
* **Restricted (R)**: Flight allowed only under published conditions.
* **Danger (D)**: Hazardous activities; flight not legally barred.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 13: {pdf_path}")

# ==============================================================================
# CHAPTER 14: AIR TRAFFIC SERVICES
# ==============================================================================
def build_ch14():
    pdf_path = os.path.join(BASE_DIR, "010_ch14_air_traffic_services.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch14_air_traffic_services.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 14: Air Traffic Services")
    pdf.add_title_banner("Air Law", 14, "Air Traffic Services & Emergency Phases", "279-296")

    pdf.add_heading_1("1. The Three Core Air Traffic Services (ATS)")
    pdf.add_bullet("1. Air Traffic Control (ATC) Service", "Prevents collisions between aircraft and between aircraft and obstacles on the maneuvering area, and expedites and maintains an orderly flow of traffic. (Subdivided into: Area Control ACC, Approach Control APP, Aerodrome Control TWR).")
    pdf.add_bullet("2. Flight Information Service (FIS)", "Provides advice and information useful for the safe and efficient conduct of flights (weather, changes in serviceability of nav aids, traffic information).")
    pdf.add_bullet("3. Alerting Service (ALRS)", "Notifies appropriate organizations regarding aircraft in need of search and rescue aid, and assists such organizations as required. Provided to ALL aircraft provided with ATC, or submitting a flight plan.")

    pdf.add_heading_1("2. The Three Emergency Phases (Annex 11 / 12)")
    pdf.add_paragraph(
        "The Alerting Service declares three progressive emergency phases:",
        max_chars=92
    )

    phases_table = [
        ["1. INCERFA (Uncertainty Phase)", "No communication within 30 minutes after time it should have been received, OR aircraft fails to arrive within 30 minutes of ETA."],
        ["2. ALERFA (Alert Phase)", "Following INCERFA, attempts to communicate fail; OR aircraft cleared to land fails to land within 5 minutes of ETA; OR operating efficiency impaired."],
        ["3. DETRESFA (Distress Phase)", "Following ALERFA, or fuel on board considered exhausted, or information indicates aircraft about to make forced landing or has crashed."]
    ]
    pdf.add_table(
        ["Emergency Phase", "Official Activation Criteria (AviationExam Core)"],
        phases_table,
        col_widths=[145.0, 360.0]
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Time limit for lack of communication to trigger INCERFA? -> 30 minutes.")
    pdf.add_bullet("Q2", "Failure to land after clearance that triggers ALERFA? -> 5 minutes after ETA.")
    pdf.add_bullet("Q3", "When fuel is considered exhausted, what phase is declared? -> DETRESFA.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    md_content = """# 010 Air Law | Chapter 14: Air Traffic Services & Emergency Phases

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 14 (Pages 279 – 296) |
| **Difficulty Level** | 🟡 Medium (ATS structure, emergency phase trigger times) |
| **Exam Weighting** | ⭐⭐ High (Regular questions on INCERFA/ALERFA/DETRESFA) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch14_air_traffic_services.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch14_air_traffic_services.pdf) |

---

## 1. The 3 ATS Services
1. **Air Traffic Control (ATC)**: Area (ACC), Approach (APP), Tower (TWR).
2. **Flight Information Service (FIS)**.
3. **Alerting Service (ALRS)**.

---

## 2. Emergency Phases

* **INCERFA (Uncertainty)**: **30 minutes** without communication or overdue by 30 mins.
* **ALERFA (Alert)**: Unsuccessful inquiries, or cleared to land but fails to land within **5 minutes** of ETA, or impaired operating efficiency.
* **DETRESFA (Distress)**: Fuel exhausted, forced landing imminent, or crash confirmed.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 14: {pdf_path}")

# ==============================================================================
# CHAPTER 15: SEPARATION
# ==============================================================================
def build_ch15():
    pdf_path = os.path.join(BASE_DIR, "010_ch15_separation.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch15_separation.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 15: Separation Methods & Minima")
    pdf.add_title_banner("Air Law", 15, "Separation & Wake Turbulence", "297-330")

    pdf.add_heading_1("1. Vertical Separation & RVSM")
    pdf.add_bullet("Standard Vertical Separation", "1,000 ft below FL 290; 2,000 ft above FL 290.")
    pdf.add_bullet("RVSM (Reduced Vertical Separation Minimum)", "1,000 ft vertical separation between FL 290 and FL 410 inclusive for approved aircraft. Above FL 410, separation is 2,000 ft.")

    pdf.add_heading_1("2. Horizontal & Radar Separation")
    pdf.add_bullet("Standard Radar Separation", "5 NM en-route; 3 NM in terminal areas (may be reduced to 2.5 NM under special radar criteria).")

    pdf.add_heading_1("3. Wake Turbulence Categories (MTOM)")
    wake_cats = [
        ["SUPER", "Airbus A380-800", "Special category for A380."],
        ["HEAVY (H)", "136,000 kg or more", "Wide-body aircraft (B777, A350, A330, B747)."],
        ["MEDIUM (M)", "Between 7,000 kg and 136,000 kg", "Standard single-aisle jets (A320, B737) and regional jets."],
        ["LIGHT (L)", "7,000 kg or less", "Light twins and single-engine aircraft (C172, PA-28, King Air)."]
    ]
    pdf.add_table(
        ["Category", "Max Certified Take-Off Mass (MTOM)", "Representative Aircraft Types"],
        wake_cats,
        col_widths=[90.0, 195.0, 220.0]
    )

    pdf.add_heading_1("4. Wake Turbulence Separation Minima")
    pdf.add_paragraph(
        "Radar Wake Turbulence Separation (Aircraft behind a HEAVY):",
        max_chars=92
    )

    sep_table = [
        ["Behind HEAVY", "Heavy: 4 NM", "Medium: 5 NM", "Light: 6 NM"],
        ["Behind MEDIUM", "Heavy: Radar min (2.5/3)", "Medium: Radar min (2.5/3)", "Light: 5 NM"]
    ]
    pdf.add_table(
        ["Preceding Aircraft", "Trailing Heavy", "Trailing Medium", "Trailing Light"],
        sep_table,
        col_widths=[125.0, 125.0, 125.0, 130.0]
    )

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
    pdf.add_bullet("Q4", "Departure delay for a Medium taking off behind a Heavy from an intersection? -> 3 minutes.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    md_content = """# 010 Air Law | Chapter 15: Separation Methods & Minima

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 15 (Pages 297 – 330) |
| **Difficulty Level** | 🔴 High (Wake turbulence tables, RVSM levels, departure delays) |
| **Exam Weighting** | ⭐⭐⭐ Critical (One of the most heavily tested numerical chapters) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch15_separation.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch15_separation.pdf) |

---

## 1. Wake Turbulence Categories (by MTOM)

* **SUPER**: Airbus A380-800.
* **HEAVY (H)**: **≥ 136,000 kg**.
* **MEDIUM (M)**: **> 7,000 kg and < 136,000 kg**.
* **LIGHT (L)**: **≤ 7,000 kg**.

---

## 2. Radar Wake Turbulence Separation

| Preceding Aircraft | Following HEAVY | Following MEDIUM | Following LIGHT |
| :---: | :---: | :---: | :---: |
| **HEAVY** | **4 NM** | **5 NM** | **6 NM** |
| **MEDIUM** | Standard radar | Standard radar | **5 NM** |

---

## 3. Non-Radar Departure Time Intervals (Behind HEAVY)

* **Same runway, full length**: **2 minutes**.
* **Same runway, from an INTERMEDIATE intersection**: **3 minutes**.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 15: {pdf_path}")

# ==============================================================================
# CHAPTER 16: CONTROL OF AIRCRAFT & EMERGENCIES
# ==============================================================================
def build_ch16():
    pdf_path = os.path.join(BASE_DIR, "010_ch16_control_aircraft.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch16_control_aircraft.md")

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

    # Markdown
    md_content = """# 010 Air Law | Chapter 16: Control of Aircraft & Emergencies

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 16 (Pages 331 – 356) |
| **Difficulty Level** | 🔴 High (Fuel emergency declarations, radio failure procedures) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Strict operational protocol questions) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch16_control_aircraft.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch16_control_aircraft.pdf) |

---

## 1. Fuel State Declarations

* **"MINIMUM FUEL"**:
  * Informs ATC that no further route diversion is possible.
  * **NOT an emergency** and does **NOT confer traffic priority**.
* **"MAYDAY MAYDAY MAYDAY FUEL"**:
  * Declares distress.
  * Usable fuel on landing will be less than final reserve.
  * **Confers immediate, absolute priority**.

---

## 2. Two-Way Radio Failure (Squawk 7600)

* **In VMC**: Continue in VMC, land at nearest suitable aerodrome, report arrival.
* **In IMC**: Maintain assigned speed and level for **7 minutes** (or **3 minutes** if being vectored), then fly according to filed flight plan to destination aid and hold until EAT/ETA.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 16: {pdf_path}")

if __name__ == "__main__":
    build_ch11()
    build_ch12()
    build_ch13()
    build_ch14()
    build_ch15()
    build_ch16()
