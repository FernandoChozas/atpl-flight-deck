#!/usr/bin/env python3
"""
Generator for 010 Air Law:
- Chapter 2: Airworthiness of Aircraft (Annex 8, TC, C of A, ADs, Part-M/CAMO, CRS)
- Chapter 3: Aircraft Nationality & Registration Marks (Annex 7, ITU, dimensions, fireproof plate)

Produces publication-grade, study-friendly PDFs and companion Markdown files.
Engineered for EXCLUSIVE STUDY without opening the textbook.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

# Paths
CH02_MD = "resumenes/convocatoria_1/010_air_law/010_ch02_airworthiness.md"
CH02_PDF = "resumenes/convocatoria_1/010_air_law/010_ch02_airworthiness.pdf"

CH03_MD = "resumenes/convocatoria_1/010_air_law/010_ch03_registration_marks.md"
CH03_PDF = "resumenes/convocatoria_1/010_air_law/010_ch03_registration_marks.pdf"

# ==============================================================================
# CHAPTER 2: AIRWORTHINESS OF AIRCRAFT
# ==============================================================================
def build_ch02():
    # 1. PDF
    pdf = PDFBuilder("Air Law", "010", "Chapter 2: Airworthiness of Aircraft")
    pdf.add_title_banner("Air Law", 2, "Airworthiness of Aircraft", "53-58")

    pdf.add_heading_1("1. Regulatory Foundation: Annex 8 & Annex 6")
    pdf.add_paragraph(
        "Airworthiness is the intrinsic safety of an aircraft—ensuring it is designed, manufactured, and "
        "maintained to operate safely within defined operating limitations. Under the Chicago Convention, "
        "two complementary Annexes define airworthiness:",
        max_chars=92
    )
    pdf.add_bullet("Annex 8 (Airworthiness of Aircraft)", "Deals with engineering and physical standards: design, structural integrity, engine reliability, systems, and continuing airworthiness.")
    pdf.add_bullet("Annex 6 (Operation of Aircraft)", "Deals with operational safety standards: operating limitations, performance minimums, onboard safety equipment, and operating procedures.")

    pdf.add_callout(
        "definition",
        "Annex 8 Applicability Scope (EASA Core)",
        "The international airworthiness standards of Annex 8, Part III apply to aeroplanes with a certified "
        "Maximum Take-Off Mass (MTOM) GREATER THAN 5,700 kg, powered by at least TWO engines, and intended "
        "for the international carriage of passengers, cargo, or mail.",
        max_chars=86
    )

    pdf.add_heading_1("2. Certification Process: From Prototype to Airline")
    pdf.add_paragraph(
        "An aircraft goes through distinct legal stages before entering commercial service:",
        max_chars=92
    )

    cert_table = [
        ["1. Permit to Fly", "State of Manufacture / Registry", "Allows non-certified prototype or aircraft with minor technical deviations to fly for flight testing or repositioning."],
        ["2. Type Certificate (TC)", "State of Design / Manufacture", "Certifies that the overall design (model) meets all applicable Airworthiness Codes (e.g. EASA CS-25 for large aeroplanes)."],
        ["3. Supplemental TC (STC)", "State of Design", "Issued when an organization modifies an existing certified aircraft type with major design changes."],
        ["4. Certificate of Airworthiness", "State of Registry", "Issued to EACH INDIVIDUAL aircraft certifying it conforms to the approved Type Certificate and is in condition for safe operation."]
    ]
    pdf.add_table(
        ["Certificate", "Issuing Authority", "Legal Scope & Exam Specifics"],
        cert_table,
        col_widths=[90.0, 110.0, 305.0]
    )

    pdf.add_callout(
        "trap",
        "State of Manufacture vs State of Registry",
        "AviationExam frequently tests this distinction: The TYPE CERTIFICATE (TC) is issued by the State of "
        "Manufacture/Design (e.g. France for Airbus, USA for Boeing). The CERTIFICATE OF AIRWORTHINESS (C of A) "
        "for an individual aircraft is issued or validated by the STATE OF REGISTRY.",
        max_chars=86
    )

    pdf.add_heading_1("3. Certificate of Airworthiness (C of A) Details")
    pdf.add_bullet("Mandatory Carriage", "Article 29 of Chicago Convention requires the C of A to be carried on board on every international flight.")
    pdf.add_bullet("Standard vs Restricted C of A", "Standard C of A is issued to aircraft conforming to a standard Type Certificate. A Restricted C of A is issued to aircraft with special operational limitations.")
    pdf.add_bullet("Mandatory C of A Contents", "Nationality and registration marks, manufacturer designation, aircraft serial number, category/usage (e.g. Transport/Commercial), and issuing authority signature.")
    pdf.add_bullet("Mutual Recognition (Article 33)", "States MUST recognize another Contracting State's C of A, provided the requirements under which it was issued equal or exceed minimum ICAO Annex 8 standards.")

    pdf.add_heading_1("4. Continuing Airworthiness & Maintenance (EASA Rules)")
    pdf.add_paragraph(
        "A Certificate of Airworthiness remains valid only if continuing airworthiness is maintained. "
        "Under EASA regulations, this is governed by Part-M / Part-ML, Part-CAMO, and Part-145:",
        max_chars=92
    )

    maint_table = [
        ["Airworthiness Directive (AD)", "MANDATORY", "Issued by the State of Design/EASA to correct an unsafe condition found in a type. Failure to comply invalidates the C of A immediately."],
        ["Service Bulletin (SB)", "NON-MANDATORY", "Issued by the manufacturer suggesting improvements or inspections. Becomes mandatory ONLY if formally incorporated into an Airworthiness Directive (AD)."],
        ["Maintenance Programme", "MANDATORY", "Approved schedule of maintenance tasks, periodic checks (A, C, D checks), and overhauls tailored to the operator."],
        ["Cert. of Release to Service (CRS)", "MANDATORY", "Issued by authorized Part-145 certifying staff after any maintenance, overhaul, or repair before the aircraft may fly."]
    ]
    pdf.add_table(
        ["Document / Action", "Legal Status", "Operational Purpose & Exam Core"],
        maint_table,
        col_widths=[105.0, 80.0, 320.0]
    )

    pdf.add_callout(
        "trap",
        "Airworthiness Review Certificate (ARC - EASA Form 15)",
        "Under EASA Part-M, a standard C of A has unlimited duration, but it is valid ONLY when accompanied by "
        "a valid Airworthiness Review Certificate (ARC / EASA Form 15), which must be renewed annually (1 year validity).",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Traps & Quick Check")
    pdf.add_callout(
        "trap",
        "Pilot-in-Command Pre-flight Responsibility",
        "Question: 'Who is ultimately responsible for ensuring the aircraft is airworthy before flight?' "
        "Answer: The PILOT-IN-COMMAND. The PIC must not commence a flight unless satisfied that the aircraft is "
        "airworthy, the CRS is issued, mass and balance are within limits, and all required documents are on board.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which ICAO Annex deals with Airworthiness? -> Annex 8.")
    pdf.add_bullet("Q2", "Who issues the Type Certificate? -> State of Design / Manufacture.")
    pdf.add_bullet("Q3", "Who issues the individual C of A? -> State of Registry.")
    pdf.add_bullet("Q4", "Is a manufacturer's Service Bulletin mandatory by default? -> No, only when mandated by an AD.")
    pdf.add_bullet("Q5", "What certificate must be signed before flight after maintenance? -> Certificate of Release to Service (CRS).")

    pdf.compile_pdf(CH02_PDF)

    # 2. Markdown
    md_content = """# 010 Air Law | Chapter 2: Airworthiness of Aircraft

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 2 (Pages 53 – 58) |
| **Difficulty Level** | 🟡 Medium (Core regulatory definitions, responsibilities) |
| **Exam Weighting** | ⭐⭐ High (Consistent questions on C of A, ADs, and issuing authorities) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch02_airworthiness.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch02_airworthiness.pdf) |

---

## 1. Regulatory Framework: Annex 8 vs Annex 6

Airworthiness is the intrinsic safety of an aircraft:
* **Annex 8 (Airworthiness of Aircraft)**: Covers engineering, design, structural integrity, flight characteristics, powerplant reliability, and continuing airworthiness.
* **Annex 6 (Operation of Aircraft)**: Covers operational standards, minimum safety equipment, and operating limitations.

> **Annex 8 Applicability Scope (EASA Core Rule)**:
> The international Standards of Annex 8 Part III apply to aeroplanes with a certified **Maximum Take-Off Mass (MTOM) greater than 5,700 kg**, powered by at least **two engines**, and intended for the international commercial carriage of passengers, cargo, or mail.
> *EASA Equivalent: Certification Specifications (CS-23 for light aircraft, CS-25 for large aeroplanes, CS-27/29 for rotorcraft, CS-E for engines, CS-P for propellers).*

---

## 2. The Aircraft Certification Chain

```mermaid
flowchart LR
    A["Design Phase"] --> B["Permit to Fly (Prototype testing)"]
    B --> C["Type Certificate - TC (State of Manufacture)"]
    C --> D["Production Aircraft"]
    D --> E["Certificate of Airworthiness - C of A (State of Registry)"]
    E --> F["Operational Service + Part-M / CAMO + Annual ARC"]
```

1. **Permit to Fly**:
   * Issued for aircraft that do not currently meet airworthiness standards but are capable of safe flight (e.g. flight testing prototypes, ferrying an aircraft to a maintenance base).
2. **Type Certificate (TC)**:
   * Issued by the **State of Design / Manufacture** (e.g. France for Airbus, USA for Boeing).
   * Certifies that the aircraft type/model design meets the airworthiness code.
3. **Supplemental Type Certificate (STC)**:
   * Issued when an organization other than the original manufacturer modifies an existing certified aircraft type with major design changes (e.g. winglets, new avionics suite).
4. **Certificate of Airworthiness (C of A)**:
   * Issued to **each individual serial-numbered aircraft** by the **State of Registry** when satisfactory evidence is provided that it conforms to the approved Type Certificate and is in condition for safe operation.

---

## 3. Certificate of Airworthiness (C of A) Essentials

* **Mandatory Onboard Document**: Required by Article 29 of the Chicago Convention.
* **Mandatory Information Stated on C of A**:
  1. Nationality and registration marks.
  2. Manufacturer and manufacturer's designation of aircraft (e.g. Airbus A320-200).
  3. Aircraft serial number (airframe chassis number).
  4. Categories / operational limitations.
  5. State of Registry signature and official stamp.
* **Mutual Recognition (Article 33)**: Other Contracting States must recognize the C of A, provided requirements equal or exceed minimum ICAO Annex 8 standards.

---

## 4. Continuing Airworthiness & Maintenance

An aircraft is only airworthy if maintained according to strict rules throughout its service life:

| Document / Tool | Legal Character | Purpose & AviationExam Core |
| :--- | :---: | :--- |
| **Airworthiness Directive (AD)** | **MANDATORY** | Issued by the aviation authority (e.g. EASA or FAA) when an unsafe condition is discovered in a type. Must be complied with within the specified timeframe. Non-compliance immediately suspends/invalidates the C of A. |
| **Service Bulletin (SB)** | **NON-MANDATORY** *(by default)* | Issued by the manufacturer (Boeing, Airbus) recommending maintenance enhancements. Only becomes mandatory if formally mandated by an Airworthiness Directive (AD). |
| **Maintenance Programme** | **MANDATORY** | Approved schedule of maintenance inspections (daily, A-check, C-check, D-check overhaul) tailored to the aircraft and operations. |
| **Certificate of Release to Service (CRS)** | **MANDATORY** | Issued by authorized Part-145 certifying staff after any maintenance, overhaul, or modification before the aircraft is permitted to fly. |
| **Airworthiness Review Certificate (ARC)** | **MANDATORY** *(EASA)* | Under EASA Part-M/CAMO, the C of A has unlimited duration, but is valid ONLY when accompanied by a valid ARC (EASA Form 15), renewed every 12 months. |

---

## 5. ⚠️ AviationExam Traps

> [!WARNING]
> **Trap 1: Who issues the Type Certificate vs the C of A?**
> * *Type Certificate*: Issued by the **State of Design / Manufacture**.
> * *Certificate of Airworthiness*: Issued by the **State of Registry**.

> [!WARNING]
> **Trap 2: Is a manufacturer's Service Bulletin mandatory?**
> * *Answer*: **NO**. It is informational/advisory. It becomes legally mandatory **ONLY IF** an Airworthiness Directive (AD) is issued by the regulatory authority referencing that SB.

> [!WARNING]
> **Trap 3: Pilot-in-Command Final Responsibility**
> * *Answer*: The Pilot-in-Command (PIC) is ultimately responsible for ensuring the aircraft is safe for flight and that all required documents (C of A, ARC, CRS, Journey Log) are in order before departure.
"""
    os.makedirs(os.path.dirname(os.path.abspath(CH02_MD)), exist_ok=True)
    with open(CH02_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 2: {CH02_MD} and {CH02_PDF}")

# ==============================================================================
# CHAPTER 3: AIRCRAFT NATIONALITY & REGISTRATION MARKS
# ==============================================================================
def build_ch03():
    # 1. PDF
    pdf = PDFBuilder("Air Law", "010", "Chapter 3: Aircraft Nationality & Registration Marks")
    pdf.add_title_banner("Air Law", 3, "Nationality & Registration Marks", "59-66")

    pdf.add_heading_1("1. Regulatory Basis: Annex 7 & Chicago Convention")
    pdf.add_paragraph(
        "Under Article 17 of the Chicago Convention, aircraft have the nationality of the State in which "
        "they are registered. Annex 7 specifies international standards for nationality and registration "
        "marks, placement, dimensions, and identification plates.",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "Key Principles of Aircraft Registration",
        "1. Dual Registration Prohibited (Art. 18): An aircraft cannot be validly registered in more than one "
        "State at the same time. However, registration may be transferred from one State to another.\n"
        "2. Domestic Law Governs (Art. 19): The registration or transfer of registration of aircraft in any "
        "Contracting State shall be made in accordance with its laws and regulations.",
        max_chars=86
    )

    pdf.add_heading_1("2. Structure of Marks: Nationality vs Registration")
    pdf.add_bullet("Nationality Mark", "Selected from the series of nationality symbols included in radio call signs allocated to the State of Registry by the International Telecommunication Union (ITU).")
    pdf.add_bullet("Registration Mark", "Letters, numbers, or a combination of both assigned by the State of Registry or common mark authority.")
    pdf.add_bullet("The Hyphen Rule", "When the first character of the registration mark is a LETTER, it MUST be preceded by a HYPHEN (e.g. G-ABCD, EC-ABC, F-GZTA). In the USA, 'N' followed directly by numbers requires no hyphen (e.g. N12345).")
    pdf.add_bullet("Common Mark", "Assigned by ICAO to the common mark registering authority of an international operating agency (such as Arab Air Cargo). Preceded by a common mark symbol.")

    pdf.add_callout(
        "trap",
        "Prohibited Letter Combinations in Registration Marks",
        "To avoid confusion with radio telecommunication signals, registration marks must NEVER be assigned if "
        "they can be confused with: 1) Distress signals: SOS, PAN, TTT, XXX. 2) Q-codes: QAA to QNZ. "
        "3) 5-letter combinations used in the International Code of Signals.",
        max_chars=86
    )

    pdf.add_heading_1("3. Location and Minimum Sizing (Heavier-than-Air Aircraft)")
    pdf.add_paragraph(
        "The marks must be painted or affixed by permanent means, clean, and visible at all times. "
        "Sizing rules for aeroplanes are strictly tested in AviationExam:",
        max_chars=92
    )

    marks_table = [
        ["Wings (Lower Surface)", "Port (Left) half of lower wing surface", "At least 30 cm (300 mm)", "Tops of letters directed toward leading edge."],
        ["Fuselage / Vertical Tail", "Each side of fuselage OR upper halves of vertical tail", "At least 30 cm (300 mm)", "If multi-tail, displayed on outer sides of the outer surfaces."],
        ["Lighter-than-Air (Airships)", "Tail surface or envelope", "At least 50 cm (500 mm)", "Visible from ground and sides."],
        ["Lighter-than-Air (Balloons)", "At max diameter on opposite sides", "At least 50 cm (500 mm)", "Displayed near equator of balloon."]
    ]
    pdf.add_table(
        ["Aircraft Component", "Location on Aircraft", "Min. Height", "Orientation & Details"],
        marks_table,
        col_widths=[110.0, 155.0, 95.0, 145.0]
    )

    pdf.add_heading_1("4. The Aircraft Identification Plate")
    pdf.add_paragraph(
        "Every aircraft engaged in international air navigation must carry an identification plate:",
        max_chars=92
    )
    pdf.add_bullet("Material", "Must be made of FIREPROOF METAL or other fireproof material of suitable physical properties.")
    pdf.add_bullet("Content", "Inscribed with at least the nationality and registration mark of the aircraft.")
    pdf.add_bullet("Location", "Secured in a prominent position near the MAIN ENTRANCE of the aircraft (for unpowered aircraft, on the exterior near the tail).")

    pdf.add_heading_1("5. AviationExam Traps & Quick Check")
    pdf.add_callout(
        "trap",
        "Dual Nationality Question",
        "Question: 'Can an aircraft be registered in two States at once?' "
        "Answer: ABSOLUTELY NOT. Article 18 explicitly prohibits registration in more than one State. "
        "The aircraft's nationality is determined solely by its current State of Registry.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which ICAO Annex governs Aircraft Nationality and Registration Marks? -> Annex 7.")
    pdf.add_bullet("Q2", "Who allocates the nationality mark symbols? -> The International Telecommunication Union (ITU).")
    pdf.add_bullet("Q3", "What is the minimum height of registration letters on aeroplane wings? -> 30 cm (300 mm).")
    pdf.add_bullet("Q4", "What is the minimum height on aeroplane fuselage/tail? -> 30 cm (300 mm).")
    pdf.add_bullet("Q5", "What material must the identification plate be made of? -> Fireproof metal (or fireproof material).")
    pdf.add_bullet("Q6", "Where is the identification plate fitted? -> In a prominent position near the main entrance.")

    pdf.compile_pdf(CH03_PDF)

    # 2. Markdown
    md_content = """# 010 Air Law | Chapter 3: Aircraft Nationality & Registration Marks

| Document Data | Specification |
| :--- | :--- |
| **Subject** | 010 Air Law (EASA ATPL) |
| **CAE Oxford Manual** | Chapter 3 (Pages 59 – 66) |
| **Difficulty Level** | 🟢 Low-Medium (Clear dimensions, concise rules) |
| **Exam Weighting** | ⭐⭐ High (Regular questions on 30 cm height, fireproof plate, and ITU) |
| **Target Score** | ≥ 90% in AviationExam Mock Tests |
| **PDF Summary File** | [`010_ch03_registration_marks.pdf`](file:///Users/fernandochozasaliseda/Desktop/PROYECTO%20ATPL/resumenes/convocatoria_1/010_air_law/010_ch03_registration_marks.pdf) |

---

## 1. Principles of Aircraft Nationality (Chicago Convention & Annex 7)

* **Article 17 (Nationality of Aircraft)**: Aircraft have the nationality of the State in which they are registered.
* **Article 18 (Dual Registration)**: An aircraft **cannot be validly registered in more than one State at the same time**. It may, however, transfer registration from one State to another.
* **Article 19 (Domestic Law)**: Registration is conducted according to national laws.
* **Certificate of Registration**: Must be carried on board on all international flights (Article 29).

---

## 2. Nationality Mark vs Registration Mark

* **Nationality Mark**:
  * Selected from the series of nationality symbols in radio call signs allocated by the **International Telecommunication Union (ITU)**.
  * Identifies the State of Registry (e.g. `G` = United Kingdom, `EC` = Spain, `F` = France, `D` = Germany).
* **Registration Mark**:
  * Assigned by the State of Registry. Letters, numbers, or a combination.
  * **The Hyphen Rule**: When the first character of the registration mark is a **letter**, it must be preceded by a **hyphen** (e.g. `EC-MNA`, `G-BOAC`).
* **Prohibited Letter Combinations**:
  * Any signal that can be confused with distress or emergency: `SOS`, `PAN`, `XXX`, `TTT`.
  * Q-codes: Any combination from `QAA` through `QNZ`.
  * 5-letter combinations used in the International Code of Signals.
* **Common Mark**:
  * Assigned by ICAO to an international operating agency (preceded by a common mark symbol).

---

## 3. Location and Minimum Sizing (Heavier-than-Air Aircraft)

| Component | Exact Placement | Minimum Height | Orientation & Rules |
| :--- | :--- | :---: | :--- |
| **Wings** | **Lower surface** of the wing structure. On the **left (port) half** of the lower surface (unless extending across both). | **30 cm (300 mm)** | Tops of letters oriented toward the leading edge. |
| **Fuselage** | On each side between the wing and the tail surfaces. | **30 cm (300 mm)** | Must not be interfered with by engine nacelles or struts. |
| **Vertical Tail** | On the **upper half** of the vertical tail surface (on both sides). | **30 cm (300 mm)** | If multi-tail, displayed on the outer sides of the outer surfaces. |
| **Lighter-than-Air** | Airships and balloons. | **50 cm (500 mm)** | Visible from ground and sides. |

---

## 4. The Aircraft Identification Plate

Every aircraft engaged in international air navigation must carry an identification plate:
* **Material**: **Fireproof metal** or other fireproof material of suitable physical properties.
* **Inscribed Information**: Nationality and registration mark.
* **Location**: In a prominent position **near the main entrance**.

---

## 5. ⚠️ AviationExam Traps

> [!WARNING]
> **Trap 1: Who allocates the Nationality Marks?**
> * *AviationExam Trap*: "Who determines the nationality marks for aircraft?"
> * *Answer*: The **ITU (International Telecommunication Union)** allocates the nationality symbols (from the radio call sign allocations), and the State selects from that series and informs ICAO.

> [!WARNING]
> **Trap 2: Letter Height on Wings vs Fuselage**
> * *AviationExam Trap*: The question offers choices like "50 cm on wings and 30 cm on fuselage".
> * *Answer*: For aeroplanes, the minimum height is **30 cm (300 mm) on BOTH wings and fuselage/vertical tail**. (50 cm is only for lighter-than-air aircraft like airships and balloons).

> [!WARNING]
> **Trap 3: Identification Plate Location**
> * *Answer*: Near the **MAIN ENTRANCE**, made of **fireproof metal**.
"""
    os.makedirs(os.path.dirname(os.path.abspath(CH03_MD)), exist_ok=True)
    with open(CH03_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Ch 3: {CH03_MD} and {CH03_PDF}")

if __name__ == "__main__":
    build_ch02()
    build_ch03()
