#!/usr/bin/env python3
"""
Generator for 010 Air Law:
- Chapter 6: Instrument Departure Procedures (PANS-OPS, SID, PDG 3.3%, Turn minimums)
- Chapter 7: Approach Procedures (Segments, Precision/Non-precision, Aircraft Cats A-E, Reversals)
- Chapter 8: Circling Approach (Visual maneuvering, Radii by Cat, MOC, Missed approach from circling)
- Chapter 9: Holding Procedures (Geometry, Speeds, Outbound timing, Entry sectors 1/2/3, 5-deg buffer, MOC)
- Chapter 10: Altimeter Setting Procedures (QNH, QFE, Standard, Transition Altitude/Level/Layer)

Generates publication-grade, study-friendly PDFs and Markdown files.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

# ==============================================================================
# CHAPTER 6: INSTRUMENT DEPARTURES (PANS-OPS)
# ==============================================================================
def build_ch06():
    pdf_path = os.path.join(BASE_DIR, "010_ch06_departures.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch06_departures.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 6: Instrument Departure Procedures")
    pdf.add_title_banner("Air Law", 6, "Instrument Departure Procedures (SID)", "157-172")

    pdf.add_heading_1("1. Basic Departure Principles (PANS-OPS Doc 8168)")
    pdf.add_paragraph(
        "Instrument departure procedures provide obstacle clearance from the end of the runway until the aircraft "
        "reaches the minimum en-route altitude (MEA) or joins an ATS route. The design assumes that all engines "
        "are operating normally unless specifically designated as an engine-out contingency procedure.",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "Procedure Design Gradient (PDG) = 3.3%",
        "The standard PANS-OPS Procedure Design Gradient (PDG) is 3.3% (approximately 200 ft/NM).\n"
        "It consists of:\n"
        "1. Obstacle Identification Surface (OIS): 2.5%\n"
        "2. Obstacle Clearance Margin: 0.8%\n"
        "-> Total Standard PDG = 3.3%. A steeper gradient is published ONLY if required by obstacles or airspace.",
        max_chars=86
    )

    pdf.add_heading_1("2. Straight vs Turning Departures")
    pdf.add_bullet("Departure End of Runway (DER)", "The end of the area declared suitable for take-off. The departure procedure assumes the aircraft crosses the DER at a minimum screen height of 5 m (16 ft) with zero bank.")
    pdf.add_bullet("Straight Departure", "The departure track does not diverge by more than 15° from the runway centerline heading.")
    pdf.add_bullet("Turning Departure", "Specified whenever the departure track requires a turn of MORE THAN 15°. No turn shall be initiated below 120 m (394 ft) above aerodrome elevation (or DER elevation).")

    pdf.add_callout(
        "trap",
        "Minimum Turn Height & Bank Angles in Departures",
        "• Minimum turn altitude: 120 m (394 ft) above the aerodrome elevation (or DER).\n"
        "• Standard design bank angle in turns: 15° average (or 21° in certain modern criteria).\n"
        "• Turn speed: Procedures specify maximum speeds for turns based on aircraft category.",
        max_chars=86
    )

    pdf.add_heading_1("3. Standard Instrument Departures (SID) & Omnidirectional")
    pdf.add_bullet("Standard Instrument Departure (SID)", "A designated IFR departure route linking the aerodrome or a specific runway with a specified significant point (normally on a designated ATS route) at which the en-route phase begins.")
    pdf.add_bullet("Omnidirectional Departure", "Used when no specific track can be designed due to terrain or when departures are unrestricted. The aircraft climbs straight ahead to 120 m (394 ft) before turning to the desired en-route heading.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "What is the standard PANS-OPS Procedure Design Gradient (PDG)? -> 3.3% (2.5% OIS + 0.8% margin).")
    pdf.add_bullet("Q2", "What is the assumed screen height over the DER? -> 5 m (16 ft).")
    pdf.add_bullet("Q3", "Maximum track divergence for a straight departure? -> 15°.")
    pdf.add_bullet("Q4", "Minimum altitude above aerodrome to begin a turn on departure? -> 120 m (394 ft).")

    pdf.compile_pdf(pdf_path)

    # Markdown
    md_content = """# 010 Air Law | Chapter 6: Instrument Departure Procedures (SID)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 6 (Pages 157 – 172) |
| **Difficulty Level** | 🟡 Medium (Key design gradients, DER screen height, turn limitations) |
| **Exam Weighting** | ⭐⭐ High (Regularly tested in AviationExam) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch06_departures.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch06_departures.pdf) |

---

## 1. PANS-OPS Departure Design Gradients

* **Procedure Design Gradient (PDG)**: The standard departure gradient is **3.3%** (~200 ft/NM).
  $$\text{Standard PDG (3.3%)} = \text{Obstacle Identification Surface (2.5%)} + \text{Margin (0.8%)}$$
* If no obstacles penetrate the 2.5% OIS, no gradient is published, and the standard 3.3% applies.
* If an obstacle penetrates the 2.5% surface, a **minimum climb gradient steeper than 3.3%** is published together with the altitude up to which it must be maintained.

---

## 2. Departure Segments & Geometry

* **Screen Height at DER**: The procedure assumes the aircraft crosses the Departure End of Runway (DER) at a height of **5 m (16 ft)**.
* **Straight Departure**: Track divergence is **≤ 15°** from the runway centerline.
* **Turning Departure**:
  * Required whenever the track turns by **more than 15°**.
  * **No turn may be initiated below 120 m (394 ft)** above aerodrome elevation (or DER elevation).
  * Design bank angle: average **15°**.

---

## 3. ⚠️ AviationExam Traps

> [!WARNING]
> **Trap 1: Composition of the 3.3% PDG**
> * *AviationExam Question*: "The 3.3% Procedure Design Gradient consists of..."
> * *Answer*: **2.5% Obstacle Identification Surface (OIS) + 0.8% obstacle clearance margin**.

> [!WARNING]
> **Trap 2: Minimum Turn Altitude on Departure**
> * *Answer*: **120 m (394 ft)** above aerodrome elevation.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 6: {pdf_path}")

# ==============================================================================
# CHAPTER 7: APPROACH PROCEDURES
# ==============================================================================
def build_ch07():
    pdf_path = os.path.join(BASE_DIR, "010_ch07_approach_procedures.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch07_approach_procedures.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 7: Approach Procedures")
    pdf.add_title_banner("Air Law", 7, "Approach Procedures (PANS-OPS)", "173-206")

    pdf.add_heading_1("1. The Five Approach Segments")
    pdf.add_paragraph(
        "An instrument approach procedure is divided into up to 5 distinct segments, each with specific "
        "obstacle clearance margins (MOC) and operational objectives:",
        max_chars=92
    )

    segments_table = [
        ["1. Arrival", "En-route to IAF", "Transitions aircraft from en-route airway to the initial approach fix (IAF). Standard Terminal Arrival (STAR)."],
        ["2. Initial", "IAF to IF", "MOC at least 300 m (984 ft) in primary area. Aircraft navigates toward the intermediate fix (IF). Reversal/racetrack maneuvers occur here."],
        ["3. Intermediate", "IF to FAF / FAP", "Aircraft speed and configuration adjusted. MOC tapers from 300 m to 150 m (492 ft). Optimum descent gradient: flat (max 5.2% / 3.0°)."],
        ["4. Final", "FAF / FAP to MAPt", "Precision (glidepath 3.0° to DA/H) or Non-Precision (FAF to MDA/H). Decision to land or execute missed approach."],
        ["5. Missed Approach", "MAPt to holding/en-route", "3 phases: Initial (MAPt to start of climb, no turn), Intermediate (2.5% climb, MOC 30 m), Final (climb to safe level, MOC 50 m)."]
    ]
    pdf.add_table(
        ["Segment", "Fix Boundaries", "Operational Purpose & Minimum Obstacle Clearance (MOC)"],
        segments_table,
        col_widths=[100.0, 105.0, 300.0]
    )

    pdf.add_heading_1("2. Aircraft Approach Categories (A, B, C, D, E)")
    pdf.add_paragraph(
        "Categories are determined by the indicated airspeed at threshold (Vat), which equals stall speed "
        "in landing configuration (Vso) multiplied by 1.3, or 1.23 x Vs1g, at maximum certified landing mass:",
        max_chars=92
    )

    cats_table = [
        ["Category A", "Less than 91 kt", "Light single/twin piston aircraft (e.g. Cessna 172, Piper PA-28)."],
        ["Category B", "91 kt to 120 kt", "Heavy twins, turboprops (e.g. King Air, ATR-42/72)."],
        ["Category C", "121 kt to 140 kt", "Medium commercial jets (e.g. Airbus A320, Boeing 737)."],
        ["Category D", "141 kt to 165 kt", "Large wide-body jets (e.g. Boeing 747, 777, Airbus A350, A380)."],
        ["Category E", "166 kt to 210 kt", "Special military / high-performance jet aircraft."]
    ]
    pdf.add_table(
        ["Category", "Vat Range (Speed at Threshold)", "Typical Aircraft Types"],
        cats_table,
        col_widths=[85.0, 160.0, 260.0]
    )

    pdf.add_heading_1("3. Reversal and Racetrack Procedures")
    pdf.add_bullet("45°/180° Procedure Turn", "Turn 45° off outbound track, fly for 1 minute (Cat A/B) or 1 min 15 s (Cat C/D/E), then make a 180° turn in opposite direction to intercept inbound track.")
    pdf.add_bullet("80°/260° Procedure Turn", "Turn 80° off outbound track, immediately followed by a 260° turn in opposite direction to intercept inbound track.")
    pdf.add_bullet("Base Turn", "Aircraft flies outbound on a specified radial/track, then makes a turn to intercept the final approach track.")
    pdf.add_bullet("Racetrack Procedure", "Aircraft flies outbound parallel to inbound track for a specified time (1 to 3 minutes), then turns to intercept inbound.")

    pdf.add_callout(
        "trap",
        "OCA/H vs MDA/H and DA/H",
        "• Obstacle Clearance Altitude/Height (OCA/H): Determined solely by procedure design based on terrain/obstacles.\n"
        "• Decision Altitude/Height (DA/H): Used in PRECISION approaches. Aircraft continues descent to decision point, "
        "and if visual reference is not established, missed approach is initiated immediately (no level-off).\n"
        "• Minimum Descent Altitude/Height (MDA/H): Used in NON-PRECISION approaches. The aircraft may descend to MDA/H "
        "but MUST NOT descend below it unless visual reference is established. Level flight at MDA is permitted.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Formula for Vat? -> Vat = 1.3 x Vso at maximum certified landing mass.")
    pdf.add_bullet("Q2", "Vat speed range for Category C aircraft? -> 121 kt to 140 kt.")
    pdf.add_bullet("Q3", "MOC in the Initial Approach Segment? -> 300 m (984 ft).")
    pdf.add_bullet("Q4", "Nominal climb gradient in missed approach? -> 2.5%.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    md_content = """# 010 Air Law | Chapter 7: Approach Procedures (PANS-OPS)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 7 (Pages 173 – 206) |
| **Difficulty Level** | 🔴 High (5 approach segments, aircraft categories A-E, reversal geometry) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Highest question density in PANS-OPS) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch07_approach_procedures.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch07_approach_procedures.pdf) |

---

## 1. The 5 Approach Segments

```mermaid
flowchart LR
    A["Arrival (STAR)"] --> B["Initial (IAF)"]
    B --> C["Intermediate (IF)"]
    C --> D["Final (FAF/FAP)"]
    D --> E["Missed Approach (MAPt)"]
```

1. **Arrival Segment**: En-route airway to Initial Approach Fix (IAF).
2. **Initial Segment**: IAF to Intermediate Fix (IF). MOC = **300 m (984 ft)**. Reversals/racetracks take place here.
3. **Intermediate Segment**: IF to Final Approach Fix (FAF). Speed/flaps adjusted. MOC decreases to **150 m (492 ft)**. Maximum descent gradient: **5.2% (3.0°)**.
4. **Final Segment**: FAF to MAPt (non-precision) or FAP to DA/H (precision, glidepath typically 3.0°).
5. **Missed Approach Segment**: Initiated at MAPt or DA/H. Nominal climb gradient is **2.5%**.

---

## 2. Aircraft Categories by Threshold Speed ($V_{at}$)

$$V_{at} = 1.3 \times V_{s0} \quad \text{(or } 1.23 \times V_{s1g} \text{) at Max Certified Landing Mass}$$

| Category | $V_{at}$ Speed Range | Typical Aircraft Types |
| :---: | :---: | :--- |
| **A** | **< 91 kt** | Light single/twin piston (C172, PA-28) |
| **B** | **91 – 120 kt** | Turboprops, light twins (King Air, ATR) |
| **C** | **121 – 140 kt** | Medium transport jets (A320, B737) |
| **D** | **141 – 165 kt** | Heavy transport jets (B747, B777, A350) |
| **E** | **166 – 210 kt** | High-performance military jets |

---

## 3. ⚠️ AviationExam Traps

> [!WARNING]
> **Trap 1: DA/H vs MDA/H**
> * *Precision Approach*: Uses **Decision Altitude/Height (DA/H)**. A missed approach is initiated immediately if visual reference is not established upon reaching DA/H.
> * *Non-Precision Approach*: Uses **Minimum Descent Altitude/Height (MDA/H)**. The aircraft may fly level at MDA until the MAPt.

> [!WARNING]
> **Trap 2: Initial Phase of Missed Approach**
> * During the *Initial Missed Approach Phase* (between MAPt and start of climb), **NO TURNS ARE PERMITTED**. Turns begin only in the intermediate/final phase.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 7: {pdf_path}")

# ==============================================================================
# CHAPTER 8: CIRCLING APPROACH
# ==============================================================================
def build_ch08():
    pdf_path = os.path.join(BASE_DIR, "010_ch08_circling_approach.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch08_circling_approach.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 8: Circling Approach")
    pdf.add_title_banner("Air Law", 8, "Circling Approach Procedures", "207-214")

    pdf.add_heading_1("1. Definition & Operational Principles")
    pdf.add_paragraph(
        "A circling approach is the visual phase of an instrument approach to bring an aircraft into position for "
        "landing on a runway which is not suitably located for a straight-in approach (runway alignment exceeds 30°, "
        "or excessive descent gradient).",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "Visual Reference Requirement in Circling",
        "The aircraft MUST maintain visual reference to the runway environment (runway threshold, runway lights, "
        "markings) throughout the circling maneuver, and remain at or above the circling MDA/H until aligned "
        "with the landing runway.",
        max_chars=86
    )

    pdf.add_heading_1("2. Circling Area Radii & Obstacle Clearance (MOC)")
    pdf.add_paragraph(
        "The circling area is constructed by drawing arcs from the threshold of each usable runway. "
        "The radius of the arc depends on the aircraft category speed (bank angle 20° or rate 3°/s):",
        max_chars=92
    )

    circling_table = [
        ["Cat A", "100 kt", "1.68 NM (3.11 km)", "90 m (295 ft)"],
        ["Cat B", "135 kt", "2.66 NM (4.93 km)", "90 m (295 ft)"],
        ["Cat C", "180 kt", "4.20 NM (7.78 km)", "120 m (394 ft)"],
        ["Cat D", "205 kt", "5.28 NM (9.78 km)", "120 m (394 ft)"],
        ["Cat E", "240 kt", "6.94 NM (12.85 km)", "150 m (492 ft)"]
    ]
    pdf.add_table(
        ["Category", "Max Circling Speed", "Circling Radius", "Minimum Obstacle Clearance (MOC)"],
        circling_table,
        col_widths=[75.0, 115.0, 140.0, 175.0]
    )

    pdf.add_heading_1("3. Missed Approach from Circling Maneuver")
    pdf.add_callout(
        "trap",
        "Missed Approach during Circling (Crucial Exam Trap)",
        "If visual reference is lost while circling to land:\n"
        "1. The pilot must initiate an immediate CLIMBING TURN TOWARDS THE LANDING RUNWAY.\n"
        "2. Establish the aircraft overhead the aerodrome.\n"
        "3. Follow the published missed approach procedure for the instrument runway on which the initial approach was conducted.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "When is circling required instead of straight-in? -> When runway alignment exceeds 30° from final track.")
    pdf.add_bullet("Q2", "Circling radius for Category C? -> 4.20 NM.")
    pdf.add_bullet("Q3", "MOC for Cat C circling? -> 120 m (394 ft).")
    pdf.add_bullet("Q4", "First action if visual reference is lost while circling? -> Immediate climbing turn towards landing runway.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    md_content = """# 010 Air Law | Chapter 8: Circling Approach Procedures

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 8 (Pages 207 – 214) |
| **Difficulty Level** | 🟡 Medium (Radii table, MOC numbers, missed approach procedure) |
| **Exam Weighting** | ⭐⭐ High (Guaranteed questions on Cat C/D radii and lost visual reference) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch08_circling_approach.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch08_circling_approach.pdf) |

---

## 1. Principles of Circling

* Required when final approach track alignment differs by **> 30°** from runway centerline (or descent gradient exceeds maximum).
* Aircraft descends on instrument approach to **Circling MDA/H**, levels off, and maneuvers visually.

---

## 2. Circling Area Dimensions & Obstacle Clearance (MOC)

| Category | Max Circling Speed | Circling Radius from Threshold | Minimum Obstacle Clearance (MOC) |
| :---: | :---: | :---: | :---: |
| **A** | 100 kt | **1.68 NM** | **90 m (295 ft)** |
| **B** | 135 kt | **2.66 NM** | **90 m (295 ft)** |
| **C** | 180 kt | **4.20 NM** | **120 m (394 ft)** |
| **D** | 205 kt | **5.28 NM** | **120 m (394 ft)** |
| **E** | 240 kt | **6.94 NM** | **150 m (492 ft)** |

---

## 3. ⚠️ AviationExam Traps

> [!WARNING]
> **Trap: Loss of Visual Reference While Circling**
> * *AviationExam Question*: "If visual reference is lost while circling to land from an instrument approach, what action must the pilot take?"
> * *Answer*: Initiate an **immediate climbing turn towards the landing runway** to overhead the aerodrome, and then join the published missed approach procedure for the **instrument runway initially used**.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 8: {pdf_path}")

# ==============================================================================
# CHAPTER 9: HOLDING PROCEDURES
# ==============================================================================
def build_ch09():
    pdf_path = os.path.join(BASE_DIR, "010_ch09_holding_procedures.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch09_holding_procedures.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 9: Holding Procedures")
    pdf.add_title_banner("Air Law", 9, "Holding Procedures (PANS-OPS)", "215-226")

    pdf.add_heading_1("1. Holding Pattern Geometry & Standards")
    pdf.add_paragraph(
        "A holding procedure keeps an aircraft within a specified airspace while awaiting clearance. "
        "Standard holding pattern: racetrack pattern using RIGHT-HAND turns (non-standard uses left-hand turns).",
        max_chars=92
    )
    pdf.add_bullet("Turn Rate", "Standard rate of 3° per second (Rate 1 turn) or 25° bank angle, whichever requires less bank.")
    pdf.add_bullet("Outbound Timing", "1 minute at or below 14,000 ft (4,250 m). 1.5 minutes above 14,000 ft.")
    pdf.add_bullet("Outbound Timing Start", "Begins over or abeam the holding fix, whichever occurs later (or on wings level if abeam point cannot be determined).")

    pdf.add_heading_1("2. Maximum Holding Speeds (PANS-OPS / EASA)")
    speeds_table = [
        ["Up to 14,000 ft", "230 kt (Cat A & B: 170 kt)", "280 kt (or 0.8 Mach whichever is less)"],
        ["Above 14,000 ft up to 20,000 ft", "240 kt", "280 kt (or 0.8 Mach whichever is less)"],
        ["Above 20,000 ft up to 34,000 ft", "265 kt", "280 kt (or 0.8 Mach whichever is less)"],
        ["Above 34,000 ft", "0.83 Mach", "0.83 Mach"]
    ]
    pdf.add_table(
        ["Altitude Band", "Normal Holding Speed", "Turbulence Conditions"],
        speeds_table,
        col_widths=[150.0, 165.0, 190.0]
    )

    pdf.add_heading_1("3. The 3 Entry Sectors (with 5° Buffer)")
    pdf.add_paragraph(
        "Entry into the holding pattern is determined by the aircraft heading relative to the 3 entry sectors:",
        max_chars=92
    )
    pdf.add_bullet("Sector 1 (Parallel Entry - 110° sector)", "Fly to holding fix, turn to parallel the outbound track on reciprocal heading, fly for 1 (or 1.5) min, turn left towards holding side to intercept inbound track.")
    pdf.add_bullet("Sector 2 (Offset / Teardrop Entry - 70° sector)", "Fly to holding fix, turn to fly on a track 30° to the holding side, fly for 1 (or 1.5) min, turn right to intercept inbound track.")
    pdf.add_bullet("Sector 3 (Direct Entry - 180° sector)", "Fly to holding fix, turn directly right onto holding pattern.")

    pdf.add_callout(
        "trap",
        "Entry Sector Flexibility (The 5° Buffer)",
        "The entry sectors include a 5° buffer on either side of the sector boundary. A pilot approaching within "
        "5° of a sector boundary may choose either entry procedure.",
        max_chars=86
    )

    pdf.add_heading_1("4. Minimum Obstacle Clearance (MOC) in Holding")
    pdf.add_bullet("Primary Holding Area", "Full MOC provided throughout: at least 300 m (984 ft / 1,000 ft), or 600 m (2,000 ft) in designated mountainous areas.")
    pdf.add_bullet("Buffer Area", "Extends 5 NM beyond the primary area boundary. MOC decreases linearly from full value at inner edge to ZERO at the outer 5 NM boundary.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Standard outbound leg time below 14,000 ft? -> 1 minute (above 14,000 ft: 1.5 minutes).")
    pdf.add_bullet("Q2", "Standard holding turn rate? -> 3°/sec or 25° bank (whichever is less).")
    pdf.add_bullet("Q3", "Max holding speed below 14,000 ft? -> 230 kt.")
    pdf.add_bullet("Q4", "Size of Sector 2 (Offset entry)? -> 70° (Sector 1: 110°, Sector 3: 180°).")
    pdf.add_bullet("Q5", "MOC in primary holding area over mountains? -> 600 m (2,000 ft).")

    pdf.compile_pdf(pdf_path)

    # Markdown
    md_content = """# 010 Air Law | Chapter 9: Holding Procedures (PANS-OPS)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 9 (Pages 215 – 226) |
| **Difficulty Level** | 🔴 High (Speeds, outbound timings, 3 entry sectors, buffers) |
| **Exam Weighting** | ⭐⭐⭐ Critical (One of the most examined chapters in 010) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch09_holding_procedures.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch09_holding_procedures.pdf) |

---

## 1. Holding Geometry & Rules

* Standard pattern: **Right-hand turns**. Rate of turn: **3°/sec** or **25° bank** (whichever is less).
* **Outbound Leg Timing**:
  * Up to and including 14,000 ft: **1 minute**.
  * Above 14,000 ft: **1.5 minutes**.

---

## 2. Maximum Holding Speeds (PANS-OPS)

| Altitude Band | Normal Speed | Turbulence Conditions |
| :--- | :---: | :---: |
| **Up to 14,000 ft** | **230 kt** *(Cat A/B: 170 kt)* | **280 kt** (or 0.8M) |
| **14,000 ft to 20,000 ft** | **240 kt** | **280 kt** (or 0.8M) |
| **20,000 ft to 34,000 ft** | **265 kt** | **280 kt** (or 0.8M) |
| **Above 34,000 ft** | **0.83 Mach** | **0.83 Mach** |

---

## 3. The 3 Entry Sectors

```mermaid
flowchart TD
    H["Holding Fix"] --> S1["Sector 1: Parallel Entry (110°)"]
    H --> S2["Sector 2: Offset / Teardrop Entry (70° / 30° offset)"]
    H --> S3["Sector 3: Direct Entry (180°)"]
```

* **Sector 1 (Parallel)**: 110°.
* **Sector 2 (Offset)**: 70° (fly 30° offset).
* **Sector 3 (Direct)**: 180°.
* **Sector Buffer**: **5°** flexibility on each side of the boundary lines.

---

## 4. Minimum Obstacle Clearance (MOC)

* **Primary Area**: **300 m (1,000 ft)** over flat terrain; **600 m (2,000 ft)** over mountainous terrain.
* **Buffer Area**: Extends **5 NM** around the primary area. MOC reduces to zero at outer edge.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 9: {pdf_path}")

# ==============================================================================
# CHAPTER 10: ALTIMETER SETTING PROCEDURES
# ==============================================================================
def build_ch10():
    pdf_path = os.path.join(BASE_DIR, "010_ch10_altimeter_setting.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch10_altimeter_setting.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 10: Altimeter Setting Procedures")
    pdf.add_title_banner("Air Law", 10, "Altimeter Setting Procedures", "227-238")

    pdf.add_heading_1("1. Pressure Settings: QNH, QFE, Standard")
    pdf.add_bullet("QNH (Altimeter setting)", "Station pressure reduced to mean sea level according to ISA. Altimeter indicates ALTITUDE above MSL. On the ground at aerodrome, it reads aerodrome elevation.")
    pdf.add_bullet("QFE", "Atmospheric pressure at aerodrome elevation (or runway threshold). Altimeter indicates HEIGHT above aerodrome. On the ground at the aerodrome datum, it reads ZERO.")
    pdf.add_bullet("Standard Setting (1013.25 hPa / 29.92 inHg)", "Altimeter indicates FLIGHT LEVEL (FL). Used for vertical separation en-route.")

    pdf.add_heading_1("2. Transition Altitude, Level & Layer")
    pdf.add_paragraph(
        "To ensure vertical separation during all phases of flight, the airspace is divided by a transition structure:",
        max_chars=92
    )

    trans_table = [
        ["Transition Altitude (TA)", "Published on charts (Fixed)", "Altitude at or below which vertical position is controlled by reference to ALTITUDES (QNH). Typically 3,000 ft or higher."],
        ["Transition Level (TRL)", "Calculated by ATC (Variable)", "Lowest available FLIGHT LEVEL above the TA. Controlled by reference to Standard (1013.25). Varies with actual QNH."],
        ["Transition Layer", "Airspace between TA and TRL", "Airspace between TA and TRL. Must be at least 300 m (1,000 ft) thick. Level cruising flight in this layer is PROHIBITED."]
    ]
    pdf.add_table(
        ["Component", "Publication / Authority", "Operational Rule & Altimeter Reference"],
        trans_table,
        col_widths=[125.0, 145.0, 235.0]
    )

    pdf.add_callout(
        "trap",
        "Altimeter Changeover Point (Climbing vs Descending)",
        "• CLIMBING: The altimeter is changed from QNH to STANDARD (1013.25 hPa) when PASSING THE TRANSITION ALTITUDE (TA).\n"
        "• DESCENDING: The altimeter is changed from STANDARD (1013.25) to QNH when PASSING THE TRANSITION LEVEL (TRL).",
        max_chars=86
    )

    pdf.add_heading_1("3. Lowest Usable Flight Level")
    pdf.add_paragraph(
        "The lowest usable flight level provides at least the minimum obstacle clearance (MOC) above terrain "
        "when operating on standard setting. When atmospheric pressure is low (QNH < 1013), the true altitude is "
        "LOWER than the indicated flight level, requiring a higher transition level.",
        max_chars=92
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "What does altimeter read on ground with QFE set? -> Zero (at aerodrome datum).")
    pdf.add_bullet("Q2", "What does altimeter read on ground with QNH set? -> Aerodrome elevation.")
    pdf.add_bullet("Q3", "When climbing, at what point do you change to 1013.25? -> Passing Transition Altitude (TA).")
    pdf.add_bullet("Q4", "Can you cruise in the transition layer? -> NO, prohibited.")

    pdf.compile_pdf(pdf_path)

    # Markdown
    md_content = """# 010 Air Law | Chapter 10: Altimeter Setting Procedures

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 10 (Pages 227 – 238) |
| **Difficulty Level** | 🟡 Medium (Pressure settings, TA/TRL changeover rules) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Tested in Air Law, Met, and Flight Planning) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch10_altimeter_setting.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch10_altimeter_setting.pdf) |

---

## 1. Pressure Settings

* **QNH**: Station pressure reduced to sea level. Indicates **Altitude** above MSL. On ground: indicates **aerodrome elevation**.
* **QFE**: Station pressure at aerodrome elevation. Indicates **Height** above aerodrome. On ground: indicates **ZERO**.
* **Standard (1013.25 hPa)**: Indicates **Flight Level (FL)**.

---

## 2. Transition Altitude, Level & Layer

```mermaid
flowchart TD
    FL["FLIGHT LEVELS (Standard 1013.25)"]
    TRL["TRANSITION LEVEL (TRL) - Lowest FL (Issued by ATC)"]
    TL["TRANSITION LAYER - No Level Flight Permitted"]
    TA["TRANSITION ALTITUDE (TA) - Published on Charts"]
    ALT["ALTITUDES (QNH)"]
    
    FL --> TRL
    TRL --> TL
    TL --> TA
    TA --> ALT
```

* **Climbing**: Change from QNH to 1013.25 hPa when passing **Transition Altitude (TA)**.
* **Descending**: Change from 1013.25 hPa to QNH when passing **Transition Level (TRL)**.
* **Level flight within the Transition Layer is PROHIBITED**.

---

## 3. ⚠️ AviationExam Traps

> [!WARNING]
> **Trap: When is the altimeter changed during descent?**
> * *Answer*: Passing the **Transition Level (TRL)**, as advised by ATC.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 10: {pdf_path}")

if __name__ == "__main__":
    build_ch06()
    build_ch07()
    build_ch08()
    build_ch09()
    build_ch10()
