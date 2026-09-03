#!/usr/bin/env python3
"""
Generator for 010 Air Law:
- Chapter 4: Flight Crew Licensing (EASA Part-FCL, Ratings, Medical Part-MED, Recency, Age limits)
- Chapter 5: Rules of the Air (SERA Regulation 923/2012, VMC Minima, Semicircular Rule, Right-of-Way, Interception)

Generates:
1. resumenes/convocatoria_1/010_air_law/010_ch04_flight_crew_licensing.pdf & .md
2. resumenes/convocatoria_1/010_air_law/010_ch05_rules_of_the_air.pdf & .md

Engineered for study-friendliness: chunked into 15-min modules, clear tables, Exam Trap callouts, and 5-sec flash drills.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

# Paths
CH04_MD = "resumenes/convocatoria_1/010_air_law/010_ch04_flight_crew_licensing.md"
CH04_PDF = "resumenes/convocatoria_1/010_air_law/010_ch04_flight_crew_licensing.pdf"

CH05_MD = "resumenes/convocatoria_1/010_air_law/010_ch05_rules_of_the_air.md"
CH05_PDF = "resumenes/convocatoria_1/010_air_law/010_ch05_rules_of_the_air.pdf"

# ==============================================================================
# CHAPTER 4: FLIGHT CREW LICENSING (PART-FCL & PART-MED)
# ==============================================================================
def build_ch04():
    pdf = PDFBuilder("Air Law", "010", "Chapter 4: Flight Crew Licensing (Part-FCL & Part-MED)")
    pdf.add_title_banner("Air Law", 4, "Flight Crew Licensing & Medical", "67-100")

    pdf.add_heading_1("1. EASA Part-FCL Licence Structure")
    pdf.add_paragraph(
        "Flight Crew Licensing in Europe is governed by Commission Regulation (EU) No 1178/2011 (Part-FCL). "
        "A licence grants basic piloting privileges, but is valid ONLY when accompanied by a valid Class/Type Rating "
        "and a valid Medical Certificate.",
        max_chars=92
    )

    licence_table = [
        ["LAPL(A)", "17 years", "Light Aircraft Pilot Licence. Max 2,000 kg MTOM, max 4 persons, non-commercial only."],
        ["PPL(A)", "17 years", "Private Pilot Licence. Fly without remuneration as PIC or co-pilot in non-commercial ops."],
        ["CPL(A)", "18 years", "Commercial Pilot Licence. Fly for remuneration in commercial air transport (single-pilot) or as co-pilot."],
        ["ATPL(A)", "21 years", "Airline Transport Pilot Licence. Fly as PIC in commercial air transport on multi-pilot aeroplanes. (Prerequisite: 1,500 hours flight time)."]
    ]
    pdf.add_table(
        ["Licence", "Min. Age", "Privileges & Limitations"],
        licence_table,
        col_widths=[75.0, 65.0, 365.0]
    )

    pdf.add_callout(
        "trap",
        "Commercial Remuneration Exception for PPL",
        "A PPL holder may NOT be remunerated for flying. Exception: A PPL holder who is an authorized Flight "
        "Instructor (FI) or Examiner may receive remuneration for flight instruction or testing.",
        max_chars=86
    )

    pdf.add_heading_1("2. Ratings: Class, Type & Instrument (IR)")
    pdf.add_bullet("Class Rating", "Authorizes pilot on non-complex, single-pilot aeroplanes of similar operational characteristics (e.g. SEP - Single Engine Piston, MEP - Multi Engine Piston, TMG - Touring Motor Glider).")
    pdf.add_bullet("Type Rating", "Required for: 1) Each multi-pilot aeroplane (e.g. A320, B737), 2) Single-pilot high-performance complex aeroplanes, 3) Any aircraft deemed necessary by EASA.")
    pdf.add_bullet("Instrument Rating (IR)", "Authorizes flight under IFR with a minimum decision height of 200 ft (Category I). Valid for 1 year.")

    pdf.add_heading_2("Revalidation vs Renewal of Ratings (Crucial Distinction)")
    pdf.add_paragraph(
        "• Revalidation: Performed BEFORE the rating expires (administrative or proficiency check within 3 months of expiry).\n"
        "• Renewal: Performed AFTER the rating has expired (requires refresher training at an ATO + proficiency check with examiner).",
        max_chars=92
    )

    pdf.add_callout(
        "trap",
        "SEP Class Rating Revalidation Rules (Very Common Exam Question)",
        "To revalidate a Single Engine Piston (SEP) rating by experience within the 12 months preceding expiry: "
        "Must complete at least 12 hours of flight time (including 6 hours as PIC, 12 take-offs and landings, and a "
        "training flight of at least 1 hour with a flight instructor) OR pass a proficiency check with an examiner.",
        max_chars=86
    )

    pdf.add_heading_1("3. Recency Requirements (The 90-Day Rule)")
    pdf.add_paragraph(
        "Under Part-FCL.060, a pilot shall NOT operate an aircraft carrying passengers as PIC or co-pilot unless:",
        max_chars=92
    )
    pdf.add_bullet("Day Operations", "Has completed at least 3 take-offs and 3 landings within the preceding 90 days on the same class/type or in a full flight simulator (FSTD).")
    pdf.add_bullet("Night Operations", "Has carried out at least 1 take-off and 1 landing at night within the preceding 90 days as a flying pilot, UNLESS the pilot holds an active Instrument Rating (IR).")

    pdf.add_heading_1("4. Part-MED: Medical Certification & Validity Periods")
    pdf.add_paragraph(
        "Medical certificates are issued under Part-MED by authorized Aero-Medical Examiners (AME):",
        max_chars=92
    )

    med_table = [
        ["Class 1", "CPL / ATPL (Commercial)", "12 months (Under 60 years).\nReduced to 6 months if: aged 60+, OR aged 40+ in single-pilot commercial passenger ops."],
        ["Class 2", "PPL / Balloon / Sailplane", "60 months (Under 40 years).\n24 months (40 to 49 years).\n12 months (50 years and over)."],
        ["LAPL", "LAPL(A)", "60 months (Under 40 years).\n24 months (40 years and over)."]
    ]
    pdf.add_table(
        ["Medical Class", "Applies To", "Validity Periods & Age Reductions"],
        med_table,
        col_widths=[85.0, 140.0, 280.0]
    )

    pdf.add_heading_2("Decrease in Medical Fitness: Mandatory Notification Rules")
    pdf.add_paragraph(
        "A pilot MUST notify the medical assessor/AME and suspend flying privileges in cases of:\n"
        "• Hospital admission or clinic stay exceeding 12 hours.\n"
        "• Any significant surgical operation or medical procedure.\n"
        "• Illness causing incapacity to fly for 21 days or more (Class 1) or 30 days or more (Class 2/LAPL).\n"
        "• Pregnancy: Pilot may fly until end of 26th week of gestation under multi-pilot ops with class 1 medical.",
        max_chars=92
    )

    pdf.add_heading_1("5. Age Limitations for Commercial Air Transport")
    pdf.add_callout(
        "trap",
        "The Rule of 60 and 65 (Part-FCL.065)",
        "• Age 60 to 64: The holder of a pilot licence who has reached age 60 shall NOT act as pilot of an aircraft "
        "engaged in commercial air transport EXCEPT as member of a multi-pilot crew, and provided the other pilot "
        "is under 60 years of age.\n"
        "• Age 65: Absolute cutoff. No pilot aged 65 or over may act as pilot in commercial air transport.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Minimum age to hold an ATPL? -> 21 years (CPL: 18, PPL: 17).")
    pdf.add_bullet("Q2", "Validity of Class 1 medical for a 45-year-old airline pilot flying multi-crew? -> 12 months.")
    pdf.add_bullet("Q3", "Validity of Class 1 medical for a 45-year-old flying single-pilot commercial passenger ops? -> 6 months.")
    pdf.add_bullet("Q4", "Recency rule for carrying passengers? -> 3 take-offs and landings in preceding 90 days.")
    pdf.add_bullet("Q5", "Can a 61-year-old pilot fly commercial air transport? -> Yes, only in multi-pilot crew where other pilot is <60.")

    pdf.compile_pdf(CH04_PDF)

    # Markdown
    md_content = """# 010 Air Law | Chapter 4: Flight Crew Licensing (Part-FCL & Part-MED)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 4 (Pages 67 – 100) |
| **Difficulty Level** | 🔴 High (Strict validity tables, age cutoffs, and recency rules) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Heavily examined in AviationExam) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch04_flight_crew_licensing.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch04_flight_crew_licensing.pdf) |

---

## 1. EASA Licence Types & Privileges (Part-FCL)

Governed by Regulation (EU) No 1178/2011:

| Licence | Min. Age | Experience | Key Privileges & Limitations |
| :--- | :---: | :---: | :--- |
| **LAPL(A)** | 17 | 30 hrs | Single-engine piston aeroplanes up to 2,000 kg MTOM, max 4 persons, non-commercial only. Non-ICAO compliant. |
| **PPL(A)** | 17 | 45 hrs | Act without remuneration as PIC or co-pilot in non-commercial operations. ICAO Annex 1 compliant. *(Exception: can be paid if working as authorized FI/FE).* |
| **CPL(A)** | 18 | 200 hrs (150 integrated) | Exercise all PPL privileges; act as PIC or co-pilot in any aeroplane engaged in operations other than commercial air transport; act as PIC in commercial air transport on single-pilot aeroplanes; act as co-pilot on multi-pilot aeroplanes. |
| **ATPL(A)** | 21 | 1,500 hrs | Exercise all PPL and CPL privileges; act as PIC or co-pilot in commercial air transport on multi-pilot aeroplanes. |

---

## 2. Ratings: Class, Type & Instrument (IR)

* **Class Rating**: Authorizes operation of non-complex, single-pilot aeroplanes:
  * **SEP (Land / Sea)**: Single Engine Piston. Valid 2 years.
  * **MEP (Land / Sea)**: Multi Engine Piston. Valid 1 year.
  * **TMG**: Touring Motor Glider.
* **Type Rating**: Required for all multi-pilot aeroplanes and high-performance single-pilot aeroplanes. Valid 1 year.
* **Instrument Rating (IR)**: Valid 1 year. Allows flight under IFR with Category I minimums (decision height not less than 200 ft).

### Revalidation vs Renewal
* **Revalidation**: Done **BEFORE** expiry. Rating renewed without formal retraining.
* **Renewal**: Done **AFTER** expiry. Pilot must undergo refresher training at an Approved Training Organisation (ATO) and pass a proficiency check with a designated examiner.
* **SEP Revalidation by Experience**:
  * Within 12 months preceding expiry: at least **12 hours flight time** (including 6 hours as PIC, 12 take-offs and landings, and a 1-hour training flight with an FI) OR pass a proficiency check within 3 months of expiry.

---

## 3. Recency Requirements (90-Day Rule - Part-FCL.060)

A pilot shall NOT act as PIC or co-pilot carrying passengers unless:
1. **Day Flight**: Has carried out at least **3 take-offs and 3 landings** in the preceding **90 days** on the same class/type or approved FSTD.
2. **Night Flight**: Has carried out at least **1 take-off and 1 landing at night** in the preceding 90 days as flying pilot, **UNLESS holding an active Instrument Rating (IR)**.

---

## 4. Part-MED: Medical Certificates & Validity

| Medical Class | Target Licence | Standard Validity | Reductions / Special Cases |
| :--- | :--- | :---: | :--- |
| **Class 1** | CPL, ATPL, MPL | **12 months** | Reduced to **6 months** if: <br>• Age **60+** in commercial air transport.<br>• Age **40+** in single-pilot commercial passenger operations. |
| **Class 2** | PPL, BPL, SPL | **60 months** (<40 yrs)<br>**24 months** (40-49 yrs)<br>**12 months** (50+ yrs) | Standard step-down at ages 40 and 50. |
| **LAPL** | LAPL | **60 months** (<40 yrs)<br>**24 months** (40+ yrs) | Standard step-down at age 40. |

### Mandatory Decrease in Medical Fitness Reporting:
* Hospital stay > 12 hours.
* Surgical procedure.
* Illness causing incapacity > **21 days** (Class 1) or > **30 days** (Class 2).
* Pregnancy: Fly up to end of **26th week** with multi-pilot crew.

---

## 5. Age Limits for Commercial Air Transport (Part-FCL.065)

```mermaid
flowchart LR
    A["Age < 60"] --> B["Normal Commercial Operations"]
    B --> C["Age 60 to 64"]
    C --> D["Multi-Pilot Operations ONLY<br>Other pilot MUST be < 60"]
    D --> E["Age 65"]
    E --> F["ABSOLUTE STOP for Commercial Air Transport"]
```

---

## 6. ⚠️ AviationExam Traps

> [!WARNING]
> **Trap 1: Class 1 Medical Validity for Airline Pilot aged 45**
> * *AviationExam Question*: "What is the validity of a Class 1 medical for a 45-year-old pilot flying for an airline (multi-pilot crew)?"
> * *Answer*: **12 MONTHS**. The 6-month reduction at age 40 applies ONLY to *single-pilot commercial passenger flights*. In airline multi-pilot operations, the 6-month reduction happens only at age 60!

> [!WARNING]
> **Trap 2: Flying with an Expired Rating**
> * *Answer*: If a rating expires even by 1 day, it cannot be "revalidated"; it must be **RENEWED** via an ATO refresher and an examiner test.
"""
    os.makedirs(os.path.dirname(os.path.abspath(CH04_MD)), exist_ok=True)
    with open(CH04_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 4: {CH04_MD} and {CH04_PDF}")

# ==============================================================================
# CHAPTER 5: RULES OF THE AIR (SERA)
# ==============================================================================
def build_ch05():
    pdf = PDFBuilder("Air Law", "010", "Chapter 5: Rules of the Air (SERA Regulation)")
    pdf.add_title_banner("Air Law", 5, "Rules of the Air & SERA", "101-156")

    pdf.add_heading_1("1. Regulatory Authority: SERA & Annex 2")
    pdf.add_paragraph(
        "Rules of the air are established by ICAO Annex 2 and standardized in European airspace by Commission "
        "Implementing Regulation (EU) No 923/2012 (SERA - Standardised European Rules of the Air). "
        "The Pilot-in-Command (PIC) has final authority over the disposition of the aircraft and is responsible "
        "for operation in compliance with the rules of the air, but may deviate in emergencies in the interest of safety.",
        max_chars=92
    )

    pdf.add_heading_1("2. Visual Meteorological Conditions (VMC) Minima")
    pdf.add_paragraph(
        "VMC minima define when a flight may proceed under Visual Flight Rules (VFR). AviationExam questions "
        "frequently test exact cloud distance and visibility numbers across airspace classes:",
        max_chars=92
    )

    vmc_table = [
        ["FL 100 and above", "Classes A, B, C, D, E, F, G", "8 km", "1,500 m horizontal, 1,000 ft (300 m) vertical."],
        ["Below FL 100 (or 3,000 ft AMSL whichever is higher)", "Classes B, C, D, E, F, G (Class A: IFR only)", "5 km", "1,500 m horizontal, 1,000 ft (300 m) vertical."],
        ["At or below 3,000 ft AMSL (or 1,000 ft AGL whichever is higher)", "Classes F and G", "5 km*", "Clear of clouds and with the surface in sight.\n(*Reduced to 1,500 m if speed <= 140 kt IAS)."]
    ]
    pdf.add_table(
        ["Altitude / Level", "Airspace Classes", "Min. Flight Visibility", "Distance from Clouds"],
        vmc_table,
        col_widths=[105.0, 115.0, 85.0, 200.0]
    )

    pdf.add_callout(
        "trap",
        "VFR in Airspace Class A & Special VFR",
        "1. Airspace Class A: VFR flights are STRICTLY PROHIBITED (IFR only).\n"
        "2. Special VFR (CTR only): Permitted when weather is below VMC: Ground visibility min. 1,500 m "
        "(800 m for helicopters), ceiling min. 600 ft, clear of clouds and in sight of surface, max speed 140 kt IAS.",
        max_chars=86
    )

    pdf.add_heading_1("3. Minimum Heights for VFR Flights")
    pdf.add_bullet("Congested Areas (Cities, Towns, Open-Air Gatherings)", "At least 1,000 ft (300 m) above the highest obstacle within a 600 m radius of the aircraft, and high enough to permit safe emergency landing.")
    pdf.add_bullet("Other Areas (Rural / Sea)", "At least 500 ft (150 m) above ground or water, or 500 ft above the highest obstacle within 150 m of the aircraft.")

    pdf.add_heading_1("4. Semicircular Cruising Levels (SERA Rule)")
    pdf.add_paragraph(
        "Cruising levels are based on MAGNETIC TRACK. In RVSM airspace (FL 290 to FL 410), vertical separation is 1,000 ft:",
        max_chars=92
    )

    level_table = [
        ["Track 000° to 179° (EAST)", "ODD Flight Levels (FL 050, 070, 090, 110, 130...)", "ODD + 500 ft (FL 055, 075, 095, 115...)"],
        ["Track 180° to 359° (WEST)", "EVEN Flight Levels (FL 060, 080, 100, 120, 140...)", "EVEN + 500 ft (FL 065, 085, 105, 125...)"]
    ]
    pdf.add_table(
        ["Magnetic Track", "IFR Cruising Levels", "VFR Cruising Levels (Above 3,000 ft)"],
        level_table,
        col_widths=[125.0, 190.0, 190.0]
    )

    pdf.add_heading_1("5. Right-of-Way Rules (Collision Avoidance)")
    pdf.add_bullet("Hierarchy", "Balloons > Gliders > Airships > Power-driven flying machines. (An aircraft towing another has right of way over power-driven aircraft).")
    pdf.add_bullet("Converging", "When two aircraft of the same category converge at approximately the same level, the aircraft that has the other on its RIGHT shall give way.")
    pdf.add_bullet("Approaching Head-on", "Each shall alter its heading to the RIGHT.")
    pdf.add_bullet("Overtaking", "The aircraft being overtaken has right-of-way. The overtaking aircraft shall keep out of the way by altering heading to the RIGHT.")
    pdf.add_bullet("Landing Priority", "Aircraft in flight or on the ground shall give way to aircraft landing or in final stages of approach. Between two aircraft approaching to land, the LOWER aircraft has right of way, but shall not cut in front of the other.")

    pdf.add_heading_1("6. Aircraft Lights (SERA.3215)")
    pdf.add_paragraph(
        "Navigation lights must be displayed from SUNSET TO SUNRISE (and any other period prescribed by authority):",
        max_chars=92
    )
    pdf.add_bullet("Port Wing Light", "RED light showing an unbroken arc of 110° from dead ahead to port.")
    pdf.add_bullet("Starboard Wing Light", "GREEN light showing an unbroken arc of 110° from dead ahead to starboard.")
    pdf.add_bullet("Tail Light", "WHITE light showing an unbroken arc of 140° visible aft.")
    pdf.add_bullet("Anti-Collision Lights (Beacons/Strobes)", "Flashing red or white light displayed by day and night to indicate running engines.")

    pdf.add_heading_1("7. Interception of Civil Aircraft")
    pdf.add_callout(
        "trap",
        "Interception Procedures (Annex 2 / SERA)",
        "• Interception is a measure of last resort.\n"
        "• Intercepted aircraft must immediately: 1) Follow interceptor instructions, 2) Notify ATS, "
        "3) Squawk 7700 on Mode A/C (unless instructed otherwise), 4) Monitor 121.5 MHz (and 243.0 MHz).\n"
        "• Day Signal: Interceptor rocks wings and turns slowly to the left -> 'You have been intercepted, follow me'. "
        "Rocking wings in response = 'Understood, will comply'.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Can you fly VFR in Class A airspace? -> NO, strictly prohibited.")
    pdf.add_bullet("Q2", "VMC horizontal distance from clouds above 3,000 ft? -> 1,500 m (vertical: 1,000 ft).")
    pdf.add_bullet("Q3", "When two aircraft approach head-on, which way do they turn? -> Both turn to the RIGHT.")
    pdf.add_bullet("Q4", "Navigation light angular coverage for tail light? -> 140° white light.")
    pdf.add_bullet("Q5", "What transponder code is set when intercepted? -> Mode A Code 7700.")

    pdf.compile_pdf(CH05_PDF)

    # Markdown
    md_content = """# 010 Air Law | Chapter 5: Rules of the Air (SERA Regulation)

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 5 (Pages 101 – 156) |
| **Difficulty Level** | 🔴 High (Core operational rules, VMC table, right-of-way, lights) |
| **Exam Weighting** | ⭐⭐⭐ Critical (Heavy question volume on every EASA exam) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch05_rules_of_the_air.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch05_rules_of_the_air.pdf) |

---

## 1. Visual Meteorological Conditions (VMC) Minima Table

Governed by SERA (Standardised European Rules of the Air - Regulation (EU) No 923/2012):

| Altitude Band | Airspace Classes | Flight Visibility | Distance from Clouds |
| :--- | :--- | :---: | :--- |
| **At and above FL 100** | A, B, C, D, E, F, G | **8 km** | 1,500 m horizontal, 1,000 ft (300 m) vertical |
| **Below FL 100** *(or above 3,000 ft AMSL, whichever is higher)* | B, C, D, E, F, G *(Class A: IFR only)* | **5 km** | 1,500 m horizontal, 1,000 ft (300 m) vertical |
| **At or below 3,000 ft AMSL** *(or 1,000 ft AGL, whichever is higher)* | F, G | **5 km** *(1,500 m if IAS ≤ 140 kt)* | **Clear of clouds and in sight of surface** |

### Special VFR (CTR only):
* Clearance granted by ATC to operate within a Control Zone (CTR) when weather is below VMC.
* Minimum ground visibility: **1,500 m** (800 m for helicopters).
* Minimum ceiling: **600 ft (180 m)**.
* Must remain clear of clouds, in sight of surface, and speed ≤ 140 kt IAS.

---

## 2. Semicircular Cruising Levels (Magnetic Track)

| Magnetic Track | IFR Cruising Levels | VFR Cruising Levels (above 3,000 ft) |
| :--- | :--- | :--- |
| **000° to 179° (EAST)** | **ODD** Flight Levels (FL 050, 070, 090, 110...) | **ODD + 500 ft** (FL 055, 075, 095, 115...) |
| **180° to 359° (WEST)** | **EVEN** Flight Levels (FL 060, 080, 100, 120...) | **EVEN + 500 ft** (FL 065, 085, 105, 125...) |

---

## 3. Right-of-Way & Collision Avoidance

* **Aircraft Category Hierarchy**:
  $$\text{Balloons} > \text{Gliders} > \text{Airships} > \text{Power-Driven Flying Machines}$$
  *(An aircraft towing another has priority over power-driven aircraft).*
* **Converging**: Aircraft on the other's **RIGHT** has right-of-way.
* **Head-on**: Both aircraft turn to the **RIGHT**.
* **Overtaking**: Overtaken aircraft has priority; overtaking aircraft passes on the **RIGHT**.
* **Landing**: Aircraft on final approach has priority. Between two landing aircraft, the **LOWER** has priority (shall not cut in).

---

## 4. Aircraft Lights (SERA.3215)

* Displayed between **sunset and sunrise** (and whenever prescribed by authority):
  * **Port Light**: **RED**, visible through unbroken arc of **110°**.
  * **Starboard Light**: **GREEN**, visible through unbroken arc of **110°**.
  * **Tail Light**: **WHITE**, visible through unbroken arc of **140°** (70° each side of rear axis).
  * **Anti-collision Lights**: Flashing red/white, active day and night whenever engines run.

---

## 5. Interception Procedures

1. Follow instructions given by interceptor.
2. Notify ATS unit immediately.
3. Attempt radio communication on emergency frequency **121.5 MHz** (or 243.0 MHz).
4. Set SSR transponder to **Mode A Code 7700**.
5. Interceptor signals:
   * **Rocking wings + banking turn to the left**: "You have been intercepted; follow me."
   * **Abrupt breakaway climb and turn**: "You may proceed."
"""
    os.makedirs(os.path.dirname(os.path.abspath(CH05_MD)), exist_ok=True)
    with open(CH05_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 5: {CH05_MD} and {CH05_PDF}")

if __name__ == "__main__":
    build_ch04()
    build_ch05()
