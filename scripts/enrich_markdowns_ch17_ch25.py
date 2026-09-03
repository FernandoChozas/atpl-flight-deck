#!/usr/bin/env python3
"""
Enrich companion Markdown files for 010 Air Law Chapters 17 to 25
so that the Markdown files are 100% as comprehensive and formatted as the PDFs.
"""

import os

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

md_files = {
    "010_ch17_ais.md": """# 010 Air Law | Chapter 17: Aeronautical Information Service (AIS)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 17 (Pages 357 – 374) |
| **Difficulty Level** | 🟡 Medium (AIP structure, AIRAC cycles, NOTAM series) |
| **Exam Weighting** | ⭐⭐ High (Regular numerical questions on AIRAC & NOTAM validity) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch17_ais.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch17_ais.pdf) |

---

## 1. The Integrated Aeronautical Information Package (IAIP)

Under ICAO Annex 15, the IAIP comprises:
* **AIP (Aeronautical Information Publication)**: Basic permanent regulatory document.
  * **Part 1 - GEN (General)**: National regulations, tables, units, services, charges.
  * **Part 2 - ENR (En-Route)**: General rules, airspace, ATS routes, navigation aids, warnings.
  * **Part 3 - AD (Aerodromes)**: Aerodromes, heliports, visual aids, runway data.
* **AIP Amendments (AIP AMDT)**: Permanent changes to the AIP.
* **AIP Supplements (AIP SUP)**: Temporary changes of long duration (**3 months or longer**) or extensive text/graphics. Published on **yellow paper**.
* **NOTAM (Notice to Airmen)**: Urgent operational information. Maximum validity is **3 months**.
* **PIB (Pre-flight Information Bulletin)**: Plain-language presentation of current NOTAMs for flight preparation.
* **AIC (Aeronautical Information Circulars)**: Operational, technical, or administrative matters:
  * **White**: Administrative.
  * **Yellow**: Operational (ATC, navigation facilities).
  * **Pink**: Safety awareness.
  * **Mauve**: National airspace restrictions.

---

## 2. The AIRAC System (28-Day Cycle)

* Governs operationally significant changes (e.g. ATS routes, navaids, airspace).
* **Cycle**: Predetermined dates based on a **28-day cycle**.
* **Publication lead time**: Sent at least **42 days** before effective date.
* **Major changes**: Sent at least **56 days** before effective date.

---

## 3. Special NOTAM Formats

* **SNOWTAM**: Presence of snow, slush, ice, or standing water. Max validity: **8 hours** (or 24 hours).
* **ASHTAM**: Volcanic ash contamination. Max validity: **24 hours**.
""",

    "010_ch18_aerodromes_characteristics.md": """# 010 Air Law | Chapter 18: Aerodromes - Physical Characteristics

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 18 (Pages 375 – 398) |
| **Difficulty Level** | 🔴 High (Reference code numbers/letters, declared distances) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Heavy calculation and definition question volume) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch18_aerodromes_characteristics.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch18_aerodromes_characteristics.pdf) |

---

## 1. Aerodrome Reference Code (Annex 14)

### Element 1 (Code Number - Airplane Reference Field Length):
* **Code 1**: $< 800\\text{ m}$
* **Code 2**: $800\\text{ m to } < 1,200\\text{ m}$
* **Code 3**: $1,200\\text{ m to } < 1,800\\text{ m}$
* **Code 4**: $\\ge 1,800\\text{ m}$ *(Standard transport runways)*

### Element 2 (Code Letter - Wingspan & Outer Main Gear Wheel Span):
* **Code A**: Wingspan $< 15\\text{ m}$ (Gear span $< 4.5\\text{ m}$)
* **Code B**: Wingspan $15\\text{ m to } < 24\\text{ m}$ (Gear span $4.5\\text{ to } < 6\\text{ m}$)
* **Code C**: Wingspan $24\\text{ m to } < 36\\text{ m}$ (Gear span $6\\text{ to } < 9\\text{ m}$) *(Airbus A320, Boeing 737)*
* **Code D**: Wingspan $36\\text{ m to } < 52\\text{ m}$ (Gear span $9\\text{ to } < 14\\text{ m}$) *(Boeing 767)*
* **Code E**: Wingspan $52\\text{ m to } < 65\\text{ m}$ (Gear span $9\\text{ to } < 14\\text{ m}$) *(Boeing 777, 787, Airbus A330, A350)*
* **Code F**: Wingspan $65\\text{ m to } < 80\\text{ m}$ (Gear span $14\\text{ to } < 16\\text{ m}$) *(Airbus A380-800, Boeing 747-8)*

---

## 2. Declared Distances (TORA, TODA, ASDA, LDA)

* **TORA (Take-Off Run Available)**: Length suitable for ground run on take-off.
* **TODA (Take-Off Distance Available)**: $\\text{TORA} + \\text{Clearway}$ *(Clearway max = $0.5 \\times \\text{TORA}$)*.
* **ASDA (Accelerate-Stop Distance Available)**: $\\text{TORA} + \\text{Stopway}$.
* **LDA (Landing Distance Available)**: Length available from the threshold.
* **Displaced Threshold**: LDA is reduced by the displacement distance. Take-off in the opposite direction is NOT reduced.
* **RESA (Runway End Safety Area)**: Min length **90 m** (recommended **240 m** for Code 3/4); width at least **twice the runway width**.
""",

    "010_ch19_visual_aids_markings.md": """# 010 Air Law | Chapter 19: Visual Aids - Markings and Signs

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 19 (Pages 399 – 424) |
| **Difficulty Level** | 🟡 Medium (Runway threshold stripes, sign color codes) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Guaranteed questions on sign colors and holding markings) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch19_visual_aids_markings.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch19_visual_aids_markings.pdf) |

---

## 1. Runway Threshold Markings (Piano Keys - White)

| Runway Width | Number of Threshold Stripes |
| :---: | :---: |
| **18 m** | 4 stripes |
| **23 m** | 6 stripes |
| **30 m** | 8 stripes |
| **45 m** | **12 stripes** *(Most common exam question)* |
| **60 m** | 16 stripes |

* **Aiming Point**: Two white rectangles located **400 m** from threshold on runways $\\ge 2,400\\text{ m}$.
* **Touchdown Zone (TDZ)**: Pairs of rectangular stripes spaced at **150 m** intervals.

---

## 2. Taxiway Markings & Holding Positions (Yellow)

* **Pattern A Holding Position**: Two solid yellow lines and two dashed yellow lines. Solid side is on the taxiway side; dashed side is on runway side. Do not cross solid lines without ATC clearance.
* **Pattern B Holding Position**: Ladder pattern. Used for CAT II / CAT III ILS critical areas.

---

## 3. Aerodrome Signs

* **Mandatory Instruction Sign**: **WHITE on RED**. Must not enter without ATC clearance (e.g. `27-09`, `NO ENTRY`, `CAT I/II/III`).
* **Location Sign**: **YELLOW on BLACK**. Identifies current taxiway or runway (*"Black square, you are there"*).
* **Direction / Destination Sign**: **BLACK on YELLOW**. Identifies intersecting taxiways and exit direction (*"Yellow lead you to the fellow"*).
""",

    "010_ch20_aerodrome_lighting.md": """# 010 Air Law | Chapter 20: Aerodrome Lighting

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 20 (Pages 425 – 446) |
| **Difficulty Level** | 🔴 High (Color sequences on runway end, centerline, PAPI angles) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Frequent visual questions in AviationExam) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch20_aerodrome_lighting.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch20_aerodrome_lighting.pdf) |

---

## 1. Runway Lighting Color Progression

* **Runway Edge Lights**: Variable white, except the **last 600 m** (or one third, whichever is less) which are **yellow / amber** on instrument runways.
* **Threshold Lights**: Unbroken line of **GREEN** lights.
* **Runway End Lights**: Unbroken line of **RED** lights.
* **Runway Centerline Lights**:
  * Threshold to 900 m from end: **WHITE**.
  * 900 m to 300 m from end: **Alternating RED and WHITE**.
  * Last 300 m: **RED**.
* **Taxiway**: Edge lights are **BLUE**; Centerline lights are **GREEN**.

---

## 2. Precision Approach Path Indicator (PAPI)

4 multi-lamp units on left side of runway:
* **4 White**: High ($> 3^\\circ 30'$)
* **3 White, 1 Red**: Slightly High ($3^\\circ 10'$)
* **2 White, 2 Red**: **ON GLIDEPATH ($3^\\circ 00'$)**
* **1 White, 3 Red**: Slightly Low ($2^\\circ 50'$)
* **4 Red**: Low ($< 2^\\circ 30'$)
""",

    "010_ch21_obstacle_marking_services.md": """# 010 Air Law | Chapter 21: Obstacles & Aerodrome Services (RFFS)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 21 (Pages 447 – 460) |
| **Difficulty Level** | 🟡 Medium (RFFS categories, response time rules) |
| **Exam Weighting** | ⭐⭐ High (RFFS response time and A320/B737 category) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch21_obstacle_marking_services.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch21_obstacle_marking_services.pdf) |

---

## 1. Rescue and Fire Fighting Services (RFFS)

* Based on aircraft **overall length** and **fuselage width**:
  * **Category 7**: Airbus A320, Boeing 737 (length 39 to 49 m).
  * **Category 9**: Boeing 777, 747, Airbus A350 (length 61 to 76 m).
  * **Category 10**: Airbus A380 (length 76 to 90 m).
* **Mandatory Response Time**:
  * **Optimum**: Not exceeding **2 minutes** to the end of each operational runway.
  * **Maximum**: Not exceeding **3 minutes** to any point of each operational runway in optimum visibility.

---

## 2. Obstacle Lighting

* **Low-Intensity**: Fixed **RED** lights for obstacles $< 45\\text{ m}$.
* **Medium-Intensity**: Flashing **RED** or flashing **WHITE** for obstacles $45\\text{ to } 150\\text{ m}$.
* **High-Intensity**: Flashing **WHITE** for obstacles $> 150\\text{ m}$ (operates day and night).
""",

    "010_ch22_facilitation.md": """# 010 Air Law | Chapter 22: Facilitation (Annex 9)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 22 (Pages 461 – 470) |
| **Difficulty Level** | 🟢 Low (Standard documentation and customs principles) |
| **Exam Weighting** | ⭐ Medium (General Declaration and crew entry questions) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch22_facilitation.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch22_facilitation.pdf) |

---

## 1. Core Principles of ICAO Annex 9

* Elimination of unnecessary delays for aircraft, crew, passengers, and cargo.
* **General Declaration**: Signed by pilot-in-command or authorized agent. Includes flight route, health declaration, and manifests.
* **Crew Member Certificate (CMC)**: Permits temporary visa-free entry for crew for operational duties.
* **Transit Passengers**: No disembarkation cards required if remaining in airport transit area.
""",

    "010_ch23_sar.md": """# 010 Air Law | Chapter 23: Search and Rescue (Annex 12)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 23 (Pages 471 – 480) |
| **Difficulty Level** | 🟡 Medium (Visual ground-air signal codes) |
| **Exam Weighting** | ⭐⭐ High (Guaranteed visual signals questions) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch23_sar.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch23_sar.pdf) |

---

## 1. Ground-to-Air Visual Signal Codes

| Symbol | Official Meaning |
| :---: | :--- |
| **`V`** | **Require assistance** |
| **`X`** | **Require medical assistance** |
| **`N`** | **NO or Negative** |
| **`Y`** | **YES or Affirmative** |
| **`->`** | **Proceeding in this direction** |
| **`LL`** | All well (used by search parties) |

---

## 2. Aircraft Acknowledgement Signals

* **Day**: **Rocking wings** (alternately banking left and right) = *Understood*.
* **Night**: **Flashing landing lights or navigation lights twice** = *Understood*.
* **Not Understood**: Complete $360^\\circ$ turn to the right, or yawing from side to side.
""",

    "010_ch24_security.md": """# 010 Air Law | Chapter 24: Security (Annex 17)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 24 (Pages 481 – 494) |
| **Difficulty Level** | 🟢 Low (Cockpit door rules, unruly passengers) |
| **Exam Weighting** | ⭐ Medium (Cockpit door locking protocol) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch24_security.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch24_security.pdf) |

---

## 1. ICAO Annex 17: Safeguarding Against Unlawful Interference

* Primary objective: Safety of passengers, crew, ground personnel, and the general public.
* **Flight Crew Compartment Door**:
  * Mandatory for passenger aircraft $> 45,500\\text{ kg MTOM}$ or carrying $> 60$ passengers.
  * Bullet-resistant and shrapnel-resistant.
  * Must be lockable and unlockable from either pilot seat.
  * **Must remain closed and locked from the moment all external doors are closed after passenger embarkation until any external door is opened for disembarkation.**
""",

    "010_ch25_accident_investigation.md": """# 010 Air Law | Chapter 25: Accident & Incident Investigation (Annex 13)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 25 (Pages 495 – 504) |
| **Difficulty Level** | 🟡 Medium (Accident definition, sole objective, 12-month report) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Sole objective question appears on every exam) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch25_accident_investigation.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch25_accident_investigation.pdf) |

---

## 1. Official Definition of an ACCIDENT (Annex 13)

Occurs between the time any person boards the aircraft with **intention of flight** until all persons have disembarked, in which:
1. A person is **fatally or seriously injured** (excluding self-inflicted, natural causes, or stowaways);
2. The aircraft sustains **damage or structural failure** adversely affecting strength, performance, or flight characteristics, requiring major repair; OR
3. The aircraft is **missing** or completely inaccessible.

---

## 2. Sole Objective of Investigation

> [!IMPORTANT]
> **The SOLE objective of an investigation under Annex 13 is the PREVENTION of future accidents and incidents.**
> **It is explicitly NOT the purpose of this activity to apportion blame or legal liability.**

---

## 3. Investigation Protocol

* **State of Occurrence**: Responsible for instituting and conducting the investigation.
* **Accredited Representatives**: Appointed by State of Registry, State of Operator, State of Design, and State of Manufacture.
* **Final Report**: Released as soon as possible, ideally within **12 months** of occurrence.
"""
}

for fname, content in md_files.items():
    path = os.path.join(BASE_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated Markdown: {path}")

print("All companion markdowns for Ch 17-25 enriched!")
