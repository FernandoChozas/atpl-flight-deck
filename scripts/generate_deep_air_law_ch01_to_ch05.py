#!/usr/bin/env python3
"""
Deep Comprehensive Generator for 010 Air Law (Chapters 1 to 5).
Designed for 100% self-contained study without textbooks.
Includes:
- Chapter 1: International Agreements & Organizations (6 pages)
- Chapter 2: Airworthiness of Aircraft & Continuing Airworthiness / MEL (4 pages)
- Chapter 3: Aircraft Nationality and Registration Marks (3 pages)
- Chapter 4: Flight Crew Licensing (Part-FCL & Part-MED) (7 pages)
- Chapter 5: Rules of the Air (SERA, VMC, Semicircular, Lights, Light Gun, Marshalling, Signals) (7 pages)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"
os.makedirs(BASE_DIR, exist_ok=True)

# ==============================================================================
# CHAPTER 1: INTERNATIONAL AGREEMENTS AND ORGANIZATIONS
# ==============================================================================
def build_ch01():
    pdf_path = os.path.join(BASE_DIR, "010_ch01_international_agreements.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch01_international_agreements.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 1: International Agreements & ICAO")
    pdf.add_title_banner("Air Law", 1, "International Agreements & ICAO", "21-52")

    pdf.add_heading_1("1. The Chicago Convention (1944) & Historical Context")
    pdf.add_paragraph(
        "The Convention on International Civil Aviation was signed in Chicago on 7 December 1944 by 52 States, "
        "entering into force on 4 April 1947 after ratification by the required 26 States. It established the "
        "fundamental legal principles, operational uniformity, and safety framework for global commercial aviation, "
        "creating the International Civil Aviation Organization (ICAO).",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "Preamble & Fundamental Purpose of the Convention",
        "To ensure that international civil aviation may be developed in a safe and orderly manner, and that "
        "international air transport services may be established on the basis of equality of opportunity and "
        "operated soundly and economically.",
        max_chars=86
    )

    pdf.add_heading_1("2. Exhaustive Analysis of Key Articles (EASA ECQB Core)")
    articles_data = [
        ["Art. 1: Sovereignty", "Every State has complete and exclusive sovereignty over the airspace above its territory."],
        ["Art. 2: Territory", "Land areas and territorial waters under State sovereignty. Excludes the High Seas."],
        ["Art. 3: Civil vs State", "Applies SOLELY to civil aircraft. Aircraft used in military, customs, and police services are deemed State aircraft. State aircraft cannot fly over foreign territory without authorization."],
        ["Art. 3 bis: Non-use of Weapons", "Contracting States must refrain from resorting to the use of weapons against civil aircraft in flight, and must not endanger the lives of persons on board."],
        ["Art. 5: Non-scheduled Flights", "Aircraft not engaged in scheduled international services have the right to fly across territory and make non-traffic stops without prior permission (subject to right to require landing)."],
        ["Art. 6: Scheduled Services", "No scheduled international air service may be operated over or into the territory of a Contracting State except with special permission or authorization of that State."],
        ["Art. 7: Cabotage", "Each State may refuse permission to aircraft of other States to take on passengers, cargo, and mail carried for remuneration between points within its territory."],
        ["Art. 8: Pilotless Aircraft", "No aircraft capable of being flown without a pilot shall be flown over territory without special authorization."],
        ["Art. 9: Prohibited Areas", "States may restrict or prohibit aircraft from flying over certain areas for military necessity or public safety, provided it applies equally to national aircraft."],
        ["Art. 10: Customs Airports", "States may require aircraft entering territory to land at a designated customs airport for customs and immigration inspection."],
        ["Art. 11: Applicability", "Laws and regulations relating to admission and departure shall apply to aircraft of all Contracting States without distinction as to nationality."],
        ["Art. 12: Rules of the Air", "Over the High Seas, ICAO Rules of the Air apply WITHOUT EXCEPTION. Each State undertakes to prosecute all persons violating regulations."],
        ["Art. 16: Search of Aircraft", "Authorities of each Contracting State have the right to search aircraft of other States on landing or departure and inspect certificates without unreasonable delay."],
        ["Art. 24: Customs Duties", "Fuel, lubricating oils, spare parts, and regular equipment on board an aircraft of a Contracting State on arrival shall be exempt from customs duties."],
        ["Art. 29: Documents on Board", "Every aircraft on international flight must carry: 1) Certificate of Registration, 2) Certificate of Airworthiness, 3) Crew Licences, 4) Journey Log Book, 5) Radio Licence, 6) Passenger Manifest, 7) Cargo Manifest."],
        ["Art. 32: Crew Licences", "The pilot and flight crew shall be provided with certificates of competency and licences issued or rendered valid by the State of Registry."],
        ["Art. 33: Mutual Recognition", "Certificates of Airworthiness and crew licences issued by the State of Registry MUST be recognized as valid by other States, provided requirements equal or exceed ICAO minimum standards."],
        ["Art. 37: Adoption of SARPs", "ICAO adopts International Standards and Recommended Practices in Annexes to ensure uniformity."],
        ["Art. 38: Differences Notification", "Any State unable to comply with a Standard MUST immediately notify ICAO of differences. Notification is mandatory for Standards, but optional for Recommended Practices."],
        ["Art. 83 bis: Transfer of Duties", "Allows transfer of certain functions and duties of the State of Registry to the State of the Operator in cases of lease, charter, or interchange of aircraft."]
    ]
    pdf.add_table(["Article & Concept", "Legal Rule & Exam Specifics"], articles_data, col_widths=[140.0, 370.0])

    pdf.add_callout(
        "trap",
        "AviationExam Trap: Cabotage Types (Article 7)",
        "• Consecutive Cabotage (8th Freedom): Operating domestic traffic in a foreign State as a continuation of an "
        "international flight (e.g. Madrid -> Paris -> Nice operated by an airline of Spain).\n"
        "• Stand-Alone Cabotage (9th Freedom): Domestic flight operated entirely within a foreign State without "
        "touching the airline's home country. States retain sovereign right to deny cabotage privileges.",
        max_chars=86
    )

    pdf.add_heading_1("3. The Nine Freedoms of the Air")
    pdf.add_paragraph(
        "Air transit and commercial transport rights are granted via bilateral or multilateral agreements:",
        max_chars=92
    )

    freedoms_data = [
        ["1st Freedom", "Technical", "Right to fly over foreign territory without landing (Overflight)."],
        ["2nd Freedom", "Technical", "Right to land in foreign territory for non-traffic purposes (Refueling, technical maintenance)."],
        ["3rd Freedom", "Commercial", "Right to carry revenue traffic from Home State to Foreign State."],
        ["4th Freedom", "Commercial", "Right to carry revenue traffic from Foreign State back to Home State."],
        ["5th Freedom", "Commercial", "Right to carry revenue traffic between two foreign States on a flight originating or terminating in the Home State (e.g. Madrid -> London -> New York operated by Iberia, carrying passengers between London and New York)."],
        ["6th Freedom", "Extended", "Right to carry revenue traffic between two foreign States via the airline's Home State hub (e.g. London -> Dubai -> Sydney operated by Emirates)."],
        ["7th Freedom", "Extended", "Right to carry traffic between two foreign States entirely outside the airline's Home State without touching home territory."],
        ["8th Freedom", "Consecutive Cabotage", "Right to carry revenue traffic between two domestic points in a foreign State on a flight starting or ending in the Home State."],
        ["9th Freedom", "Stand-Alone Cabotage", "Right to operate scheduled domestic passenger service entirely within a foreign State (e.g. Lufthansa operating Madrid to Barcelona)."]
    ]
    pdf.add_table(["Freedom", "Category", "Operational Definition & Practical Airline Example"], freedoms_data, col_widths=[80.0, 110.0, 320.0])

    pdf.add_heading_1("4. Structure and Governance of ICAO")
    pdf.add_bullet("Headquarters", "Permanently located in Montreal, Quebec, Canada.")
    pdf.add_bullet("The Assembly", "Sovereign body comprising ALL Contracting States. Meets once every 3 YEARS. Each State has ONE vote. Responsibilities: determines policy, votes triennial budget, elects the Council, reviews work.")
    pdf.add_bullet("The Council", "Permanent governing executive body responsible to the Assembly, comprising 36 Contracting States elected for 3 years. Responsibilities: ADOPTS ANNEXES (Standards & Recommended Practices) by a TWO-THIRDS (2/3) MAJORITY vote, manages finances, and arbitrates disputes between States.")
    pdf.add_bullet("Air Navigation Commission (ANC)", "Composed of 19 independent technical experts appointed by the Council. Considers and recommends amendments to SARPs.")
    pdf.add_bullet("Regional Offices", "7 worldwide offices: Paris (EUR/NAT), Dakar (WACAF), Nairobi (ESAF), Cairo (MID), Bangkok (APAC), Lima (SAM), and Mexico City (NACC).")

    pdf.add_heading_1("5. Standards, Recommended Practices & PANS")
    pdf.add_bullet("Standards (SARP)", "Any specification recognized as NECESSARY for the safety or regularity of international air navigation. Mandatory for Contracting States. Notification of difference is compulsory under Article 38.")
    pdf.add_bullet("Recommended Practice", "Any specification recognized as DESIRABLE in the interest of safety, regularity, or efficiency. States endeavor to conform; notification of difference is requested but not legally binding.")
    pdf.add_bullet("PANS (Procedures for Air Navigation Services)", "Operational practices too detailed for Annexes (e.g. Doc 8168 PANS-OPS, Doc 4444 PANS-ATM). Approved by the Council (not adopted as Annexes).")

    pdf.add_heading_1("6. Master Reference: All 19 ICAO Annexes")
    annexes_data = [
        ["Annex 1", "Personnel Licensing", "Flight crew, ATCOs, aircraft maintenance engineers, medical requirements."],
        ["Annex 2", "Rules of the Air", "General rules, visual flight rules (VFR), instrument flight rules (IFR), right of way."],
        ["Annex 3", "Meteorological Service", "METAR, TAF, SIGMET, aerodrome climatological information, volcanic ash."],
        ["Annex 4", "Aeronautical Charts", "Aerodrome charts, SID, STAR, instrument approach charts, en-route charts."],
        ["Annex 5", "Units of Measurement", "SI units, non-SI alternatives permitted (feet, knots, nautical miles)."],
        ["Annex 6", "Operation of Aircraft", "Part I: Commercial Air Transport (Aeroplanes), Part II: GA, Part III: Helicopters."],
        ["Annex 7", "Aircraft Nationality & Registration", "Allocation of marks, placement, lettering height, fireproof identification plates."],
        ["Annex 8", "Airworthiness of Aircraft", "Design, manufacture, testing, Type Certificates, Certificate of Airworthiness."],
        ["Annex 9", "Facilitation", "Customs, immigration, clearance formalities, General Declaration, crew identity."],
        ["Annex 10", "Aeronautical Telecommunications", "Vol I: Radio Nav, Vol II: Comms procedures, Vol III: Voice/Data, Vol IV/V: Radar."],
        ["Annex 11", "Air Traffic Services", "Air Traffic Control (ATC), Flight Information (FIS), Alerting Service, Airspace."],
        ["Annex 12", "Search and Rescue (SAR)", "SAR organization, coordination, RCCs, emergency phases, ground-air signals."],
        ["Annex 13", "Aircraft Accident Investigation", "Accident/incident definitions, notification, investigation protocol, sole aim."],
        ["Annex 14", "Aerodromes", "Vol I: Aerodrome Design & Operations (runways, lighting, markings), Vol II: Heliports."],
        ["Annex 15", "Aeronautical Information Services", "AIP, NOTAM, SNOWTAM, ASHTAM, AIRAC cycles, AICs, pre-flight bulletins."],
        ["Annex 16", "Environmental Protection", "Vol I: Aircraft noise certification, Vol II: Aircraft engine emissions."],
        ["Annex 17", "Security", "Safeguarding international civil aviation against unlawful interference."],
        ["Annex 18", "Safe Transport of Dangerous Goods", "Packaging, labelling, loading, emergency response, operator responsibilities."],
        ["Annex 19", "Safety Management", "State Safety Programme (SSP), Safety Management Systems (SMS) for operators."]
    ]
    pdf.add_table(["Annex", "Title", "Scope & Exam Relevance"], annexes_data, col_widths=[75.0, 160.0, 275.0])

    pdf.add_heading_1("7. Supplementary International Conventions")
    conv_data = [
        ["Tokyo (1963)", "Offences Committed on Board", "Jurisdiction of the State of Registry. Grants broad legal authority to the Pilot-in-Command, including power to restrain disruptive persons, disembark offenders, and deliver them to authorities."],
        ["The Hague (1970)", "Unlawful Seizure (Hijacking)", "Establishes universal jurisdiction over aircraft hijackers. Contracting States are obligated to extradite or prosecute hijackers severely."],
        ["Montreal (1971)", "Sabotage & Violence against Aviation", "Criminalizes acts directed against the in-flight safety of aircraft, destruction of aircraft in service, and sabotage of air navigation facilities."],
        ["Rome (1933/1952)", "Surface Damage to Third Parties", "Strict (absolute) liability of the aircraft operator for damage caused by an aircraft in flight to persons or property on the ground."],
        ["Warsaw (1929)", "Carrier Liability (Historic)", "First uniform international rules governing airline liability for passenger injury, death, baggage loss, and cargo damage, establishing liability caps."],
        ["Montreal (1999)", "Modernised Carrier Liability", "Replaced Warsaw. Introduces a two-tier liability system using SDRs (Special Drawing Rights): Tier 1 (strict liability up to ~128,821 SDRs), Tier 2 (unlimited fault-based liability unless carrier proves no negligence)."]
    ]
    pdf.add_table(["Convention", "Subject Matter", "Core Legal Principle & Operational Impact"], conv_data, col_widths=[95.0, 155.0, 260.0])

    pdf.add_heading_1("8. European Aviation Framework")
    pdf.add_bullet("EASA (European Union Aviation Safety Agency)", "Headquartered in Cologne, Germany. Established by Basic Regulation (EU) 2018/1139. Responsible for EU-wide rulemaking, Type Certification, environmental certification, and oversight.")
    pdf.add_bullet("EUROCONTROL", "Headquartered in Brussels, Belgium. European Organisation for the Safety of Air Navigation. Operates Network Management (NMOC) for air traffic flow management (ATFM) and Central Route Charges Office (CRCO).")
    pdf.add_bullet("ECAC (European Civil Aviation Conference)", "Located in Paris. Consultative intergovernmental body promoting safety, efficiency, and environmental harmonization among 44 European States.")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Which body adopts ICAO Annexes? -> The Council of ICAO by a 2/3 majority vote.")
    pdf.add_bullet("Q2", "Over the High Seas, whose rules of the air apply? -> ICAO Rules of the Air apply without exception.")
    pdf.add_bullet("Q3", "Carrying passengers between two points in a foreign country is which freedom? -> 8th (consecutive) or 9th (stand-alone) cabotage.")
    pdf.add_bullet("Q4", "Which Convention established universal jurisdiction over hijacking? -> The Hague Convention (1970).")
    pdf.add_bullet("Q5", "Which ICAO Annex deals with Security? -> Annex 17 (Facilitation is Annex 9).")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 1 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 2: AIRWORTHINESS OF AIRCRAFT & MEL
# ==============================================================================
def build_ch02():
    pdf_path = os.path.join(BASE_DIR, "010_ch02_airworthiness.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch02_airworthiness.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 2: Airworthiness of Aircraft & MEL")
    pdf.add_title_banner("Air Law", 2, "Airworthiness & MEL Systems", "53-58")

    pdf.add_heading_1("1. Regulatory Foundation: Annex 8 & Annex 6")
    pdf.add_paragraph(
        "Airworthiness is the intrinsic fitness of an aircraft to operate safely within its operating envelope. "
        "Under the Chicago Convention, airworthiness is divided between engineering design standards (Annex 8) "
        "and operational airworthiness standards (Annex 6):",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "Annex 8 Applicability Scope (EASA Exam Core)",
        "The international standards of ICAO Annex 8, Part III apply to aeroplanes with a Maximum Take-Off "
        "Mass (MTOM) GREATER THAN 5,700 kg, powered by at least TWO engines, and intended for the international "
        "carriage of passengers, cargo, or mail.",
        max_chars=86
    )

    pdf.add_heading_1("2. Certification Chain: From Design to Flight")
    cert_data = [
        ["1. Permit to Fly", "State of Registry or State of Design", "Issued to aircraft that do not meet standard airworthiness requirements but are capable of safe flight (e.g. flight testing prototypes, repositioning for maintenance)."],
        ["2. Type Certificate (TC)", "State of Design / Manufacture", "Certifies that the design of the aircraft type meets all airworthiness codes (e.g. EASA CS-25 for large aeroplanes, CS-23 for normal). Held by manufacturer."],
        ["3. Supplemental TC (STC)", "State of Design", "Issued to an organization that introduces major modifications to an existing certified aircraft type (e.g. avionics upgrade, winglet installation)."],
        ["4. Certificate of Airworthiness (C of A)", "State of Registry", "Issued to EACH INDIVIDUAL aircraft certifying it conforms to the approved Type Certificate and is safe for flight. Mandatory on board on all international flights (Art. 29)."]
    ]
    pdf.add_table(["Certificate", "Issuing Authority", "Legal Scope & Operational Purpose"], cert_data, col_widths=[110.0, 130.0, 270.0])

    pdf.add_callout(
        "trap",
        "Type Certificate vs Certificate of Airworthiness",
        "AviationExam Trap: Who issues the Type Certificate vs the Certificate of Airworthiness?\n"
        "• Type Certificate (TC): Issued by the STATE OF DESIGN / MANUFACTURE (e.g. France for Airbus, USA for Boeing).\n"
        "• Certificate of Airworthiness (C of A): Issued or rendered valid by the STATE OF REGISTRY for each individual tail number.",
        max_chars=86
    )

    pdf.add_heading_1("3. Continuing Airworthiness: Part-M, Part-145, Part-CAMO")
    pdf.add_paragraph(
        "An aircraft C of A remains valid only as long as continuing airworthiness is maintained in accordance with EASA Part-M:",
        max_chars=92
    )
    pdf.add_bullet("Airworthiness Directives (AD)", "Issued by the State of Design or EASA to correct an unsafe condition. ADs are MANDATORY. Failure to comply with an AD invalidates the Certificate of Airworthiness immediately.")
    pdf.add_bullet("Service Bulletins (SB)", "Issued by the aircraft/engine manufacturer suggesting improvements, modifications, or inspections. SBs are NON-MANDATORY by default, unless mandated by an Airworthiness Directive.")
    pdf.add_bullet("Certificate of Release to Service (CRS)", "Issued by appropriately licensed Part-145 certifying staff after any maintenance task, overhaul, repair, or modification before the aircraft may fly.")
    pdf.add_bullet("Airworthiness Review Certificate (ARC - EASA Form 15a/b/c)", "Under EASA, a C of A is issued for an unlimited period, but is legally valid ONLY when accompanied by a valid ARC, which must be renewed ANNUALLY (1 year validity).")

    pdf.add_heading_1("4. Master Minimum Equipment List (MMEL) vs MEL vs CDL")
    pdf.add_paragraph(
        "Commercial operations require precise instruments and equipment. However, an aircraft may depart with inoperative "
        "items under approved relief documents:",
        max_chars=92
    )
    pdf.add_bullet("MMEL (Master MEL)", "Developed by the aircraft manufacturer and approved by the State of Design. Lists items that may temporarily be inoperative under specific conditions.")
    pdf.add_bullet("MEL (Minimum Equipment List)", "Developed by the OPERATOR for each aircraft type, based on the MMEL, and approved by the State of the Operator. The MEL can be MORE restrictive than the MMEL, but NEVER LESS restrictive.")
    pdf.add_bullet("Configuration Deviation List (CDL)", "Lists secondary exterior parts of an aircraft that may be missing for dispatch (e.g. flap track fairings, landing gear doors, static wicks) along with performance penalties.")

    pdf.add_heading_2("MEL Rectification Interval Categories (AviationExam Core)")
    mel_cats = [
        ["Category A", "No standard time limit. Must be repaired within the time interval specified in the remarks column (e.g. 5 flight cycles)."],
        ["Category B", "Must be rectified within THREE (3) consecutive calendar days (72 hours), excluding the day of discovery."],
        ["Category C", "Must be rectified within TEN (10) consecutive calendar days (240 hours), excluding the day of discovery."],
        ["Category D", "Must be rectified within ONE HUNDRED AND TWENTY (120) consecutive calendar days, excluding the day of discovery."]
    ]
    pdf.add_table(["Category", "Mandatory Rectification Time Limit"], mel_cats, col_widths=[90.0, 420.0])

    pdf.add_callout(
        "trap",
        "Pilot-in-Command Pre-Flight Responsibility",
        "Question: Who is ultimately responsible for ensuring the aircraft is airworthy before flight?\n"
        "Answer: The PILOT-IN-COMMAND. The PIC must not commence a flight unless satisfied that: 1) The aircraft is airworthy, "
        "2) The CRS is signed, 3) Mass and balance are within limits, 4) Operational equipment meets MEL, 5) Emergency gear is on board.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Are Service Bulletins (SBs) mandatory by default? -> No, only when mandated by an AD.")
    pdf.add_bullet("Q2", "Validity period of an EASA Airworthiness Review Certificate (ARC)? -> 1 year.")
    pdf.add_bullet("Q3", "Rectification period for Category B MEL items? -> 3 consecutive calendar days (72 hours).")
    pdf.add_bullet("Q4", "Can an operator's MEL be less restrictive than the manufacturer's MMEL? -> NO, never.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 2 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 3: AIRCRAFT NATIONALITY AND REGISTRATION MARKS
# ==============================================================================
def build_ch03():
    pdf_path = os.path.join(BASE_DIR, "010_ch03_registration_marks.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch03_registration_marks.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 3: Aircraft Nationality & Registration Marks")
    pdf.add_title_banner("Air Law", 3, "Nationality and Registration Marks", "59-66")

    pdf.add_heading_1("1. Legal Basis: Chicago Convention & Annex 7")
    pdf.add_paragraph(
        "Under Article 17 of the Chicago Convention, aircraft have the nationality of the State in which they are registered. "
        "Annex 7 specifies international standards for nationality and registration marks, placement, lettering dimensions, "
        "and identification plates.",
        max_chars=92
    )

    pdf.add_bullet("Dual Registration Prohibited (Art. 18)", "An aircraft cannot be validly registered in more than one State at the same time. Registration may be transferred from one State to another.")
    pdf.add_bullet("Domestic Law Governs (Art. 19)", "The registration or transfer of registration of aircraft in any Contracting State shall be made in accordance with its laws and regulations.")
    pdf.add_bullet("Display of Marks (Art. 20)", "Every aircraft engaged in international air navigation shall bear its appropriate nationality and registration marks.")

    pdf.add_heading_1("2. Structure of Marks: Nationality vs Registration")
    pdf.add_bullet("Nationality Mark", "Selected from the series of nationality symbols included in radio call signs allocated to the State of Registry by the International Telecommunication Union (ITU). Examples: G = UK, F = France, D = Germany, EC = Spain, EI = Ireland, N = USA, HB = Switzerland.")
    pdf.add_bullet("Registration Mark", "Consists of letters, numbers, or a combination assigned by the State of Registry.")
    pdf.add_bullet("The Hyphen Rule", "When the first character of the registration mark is a LETTER, it MUST be preceded by a HYPHEN (e.g. G-ABCD, EC-MNA, F-GZTA). In the USA, 'N' followed by numbers requires no hyphen (e.g. N12345).")
    pdf.add_bullet("Common Mark", "Assigned by ICAO to the common mark registering authority of an international operating agency (such as Arab Air Cargo).")

    pdf.add_callout(
        "trap",
        "Prohibited Letter Combinations in Registration Marks",
        "Registration marks must NEVER be assigned if they can be confused with:\n"
        "1. Distress signals: SOS, PAN, TTT, XXX.\n"
        "2. Q-codes: QAA to QNZ (e.g. QNH, QFE, QDM, QNE, QDR).\n"
        "3. 5-letter combinations used in the International Code of Signals.",
        max_chars=86
    )

    pdf.add_heading_1("3. Location and Minimum Sizing Rules (Annex 7)")
    size_data = [
        ["Wings (Lower Surface)", "Port (left) half of the lower wing surface.", "At least 30 cm (300 mm)", "Tops of letters directed toward the leading edge."],
        ["Fuselage / Vertical Tail", "Each side of fuselage (between wings and tail) OR upper halves of vertical tail surfaces.", "At least 30 cm (300 mm)", "If multi-tail, displayed on the outer sides of the outer vertical fins."],
        ["Lighter-than-Air (Airships)", "Tail surface or envelope.", "At least 50 cm (500 mm)", "Visible from ground and both sides."],
        ["Lighter-than-Air (Balloons)", "Two places near maximum diameter on opposite sides.", "At least 50 cm (500 mm)", "Equatorial position."]
    ]
    pdf.add_table(["Location on Aircraft", "Position Specifics", "Min. Height", "Orientation & Spacing"], size_data, col_widths=[125.0, 150.0, 110.0, 125.0])

    pdf.add_heading_2("Lettering Proportions & Typography Standards")
    pdf.add_paragraph(
        "• Letters must be capital letters in Roman characters without ornamentation.\n"
        "• Width of each character (except I and 1) shall be 2/3 of its height.\n"
        "• Thickness of lines (stroke) shall be 1/6 of the character height.\n"
        "• Spacing between characters shall not be less than 1/4 of a character width.",
        max_chars=92
    )

    pdf.add_heading_1("4. The Aircraft Identification Plate")
    pdf.add_paragraph(
        "Every aircraft engaged in international air navigation must carry an identification plate inscribed with its "
        "nationality mark and registration mark:",
        max_chars=92
    )
    pdf.add_bullet("Material", "Must be made of FIREPROOF METAL or other fireproof material of suitable physical properties.")
    pdf.add_bullet("Location", "Secured in a prominent position NEAR THE MAIN ENTRANCE of the aircraft (for unpowered aircraft, on the exterior near the tail).")

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Can an aircraft be registered in two States at the same time? -> NO, strictly prohibited by Article 18.")
    pdf.add_bullet("Q2", "Who allocates the nationality mark symbols? -> The ITU (International Telecommunication Union).")
    pdf.add_bullet("Q3", "Minimum height of registration letters on aeroplane wings? -> 30 cm (300 mm).")
    pdf.add_bullet("Q4", "Where is the aircraft identification plate located? -> In a prominent position near the main entrance.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 3 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 4: FLIGHT CREW LICENSING (PART-FCL & PART-MED)
# ==============================================================================
def build_ch04():
    pdf_path = os.path.join(BASE_DIR, "010_ch04_flight_crew_licensing.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch04_flight_crew_licensing.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 4: Flight Crew Licensing (Part-FCL & Part-MED)")
    pdf.add_title_banner("Air Law", 4, "Flight Crew Licensing & Medical", "67-100")

    pdf.add_heading_1("1. European Regulatory Framework (Part-FCL)")
    pdf.add_paragraph(
        "Flight Crew Licensing in Europe is governed by Commission Regulation (EU) No 1178/2011 (Part-FCL). "
        "A licence grants basic piloting privileges, but is valid ONLY when accompanied by a valid Class or Type Rating, "
        "a valid Medical Certificate, and proof of language proficiency (ICAO English Level 4 minimum).",
        max_chars=92
    )

    pdf.add_heading_1("2. Licences: Age Limits, Experience & Privileges")
    licences_data = [
        ["LAPL(A)", "17 years", "30 hours flight time (15 dual, 6 solo).", "Light Aircraft Pilot Licence. Max 2,000 kg MTOM, max 4 persons, non-commercial only. Valid only in EASA Member States (non-ICAO)."],
        ["PPL(A)", "17 years", "45 hours flight time (25 dual, 10 solo including 5 solo cross-country with 1 qualifying flight >= 150 NM with 2 landings).", "Private Pilot Licence. Fly without remuneration as PIC or co-pilot in non-commercial ops. ICAO Annex 1 compliant. (Exception: can receive payment if working as authorized FI or FE)."],
        ["CPL(A)", "18 years", "Modular: 200 hours (or Integrated: 150 hours). Breakdown: 100 hrs PIC, 20 hrs cross-country PIC with 300 NM flight, 10 hrs instrument, 5 hrs night.", "Commercial Pilot Licence. Exercise all PPL privileges; act as PIC in commercial air transport on single-pilot aeroplanes; act as co-pilot in multi-pilot aeroplanes."],
        ["MPL(A)", "18 years", "Minimum 240 hours of flight and simulator training in an approved course.", "Multi-crew Pilot Licence. Exercise co-pilot privileges in commercial air transport restricted to multi-pilot aeroplanes."],
        ["ATPL(A)", "21 years", "1,500 hours total flight time (see detailed breakdown below).", "Airline Transport Pilot Licence. Act as PIC or co-pilot in commercial air transport on multi-pilot aeroplanes."]
    ]
    pdf.add_table(["Licence", "Min Age", "Minimum Experience Requirements", "Privileges & Limitations"], licences_data, col_widths=[65.0, 55.0, 170.0, 220.0])

    pdf.add_heading_2("ATPL(A) 1,500-Hour Mandatory Breakdown (AviationExam Core)")
    pdf.add_paragraph(
        "To qualify for the issue of an ATPL(A), the applicant must complete at least 1,500 hours of flight time including:\n"
        "• 500 hours in multi-pilot operations on aeroplanes.\n"
        "• 250 hours as PIC, OR at least 500 hours as PICUS (PIC Under Supervision), OR 70 hours PIC and the remainder as PICUS.\n"
        "• 200 hours of cross-country flight time, of which at least 100 hours must be as PIC or PICUS.\n"
        "• 75 hours of instrument flight time, of which a maximum of 30 hours may be instrument ground time (FSTD).\n"
        "• 100 hours of night flight as PIC or co-pilot.",
        max_chars=92
    )

    pdf.add_callout(
        "trap",
        "Commercial Remuneration for PPL Holders",
        "Can a PPL holder receive remuneration for flying?\n"
        "Answer: NO, as a general rule. EXCEPTION: A PPL holder who holds an authorized Flight Instructor (FI) or "
        "Flight Examiner (FE) certificate may receive remuneration for providing flight instruction or testing.",
        max_chars=86
    )

    pdf.add_heading_1("3. Ratings: Class, Type, Instrument (IR) & Revalidation")
    pdf.add_bullet("Class Rating", "Authorizes pilot on non-complex, single-pilot aeroplanes: SEP (Single Engine Piston - valid 2 years), MEP (Multi Engine Piston - valid 1 year), TMG (Touring Motor Glider).")
    pdf.add_bullet("Type Rating", "Required for: 1) Each multi-pilot aeroplane (e.g. A320, B737), 2) Single-pilot high-performance complex aeroplanes. Valid 1 year.")
    pdf.add_bullet("Instrument Rating (IR)", "Authorizes flight under IFR with Category I minimums (DH >= 200 ft). Valid 1 year.")

    pdf.add_heading_2("Revalidation vs Renewal (Crucial Regulatory Distinction)")
    pdf.add_bullet("Revalidation", "The administrative action taken within the period of validity of a rating which allows the holder to continue to exercise the privileges (performed BEFORE expiry).")
    pdf.add_bullet("Renewal", "The administrative action taken AFTER a rating has expired for the purpose of renewing the privileges. Requires refresher training at an ATO + proficiency check with examiner.")

    pdf.add_callout(
        "trap",
        "SEP Class Rating Revalidation Rules (Very Frequently Tested)",
        "For revalidation of a Single-Engine Piston (SEP) class rating by experience, the pilot must within the "
        "12 MONTHS preceding the expiry date of the rating:\n"
        "1. Complete at least 12 HOURS of flight time, including:\n"
        "   - 6 hours as PIC;\n"
        "   - 12 take-offs and 12 landings; AND\n"
        "   - A training flight of at least 1 HOUR with a Flight Instructor (FI).\n"
        "OR: Pass a proficiency check with an examiner within the 3 months preceding expiry.",
        max_chars=86
    )

    pdf.add_heading_1("4. Recent Experience Requirements (Part-FCL.060)")
    pdf.add_paragraph(
        "A pilot shall NOT act as PIC or co-pilot carrying passengers unless:",
        max_chars=92
    )
    pdf.add_bullet("Day Flight", "Has carried out at least 3 take-offs and 3 landings in the preceding 90 DAYS on the same class/type or approved FSTD.")
    pdf.add_bullet("Night Flight", "Has carried out at least 1 take-off and 1 landing at NIGHT in the preceding 90 DAYS as flying pilot, UNLESS holding an active Instrument Rating (IR).")

    pdf.add_heading_1("5. Part-MED: Medical Certification & Validity")
    med_data = [
        ["Class 1", "CPL, ATPL, MPL (Commercial Air Transport)", "12 months (Under 60 years).\nReduced to 6 months if: aged 60+, OR aged 40+ in single-pilot commercial passenger operations."],
        ["Class 2", "PPL, Sailplane, Balloon (Private flying)", "60 months (Under 40 years).\n24 months (40 to 49 years).\n12 months (50 years and over)."],
        ["LAPL", "LAPL(A), LAPL(H)", "60 months (Under 40 years).\n24 months (40 years and over)."]
    ]
    pdf.add_table(["Medical Class", "Applies To", "Standard Validity & Age Reductions"], med_data, col_widths=[90.0, 160.0, 260.0])

    pdf.add_heading_2("Decrease in Medical Fitness: Mandatory Reporting")
    pdf.add_paragraph(
        "A pilot MUST notify the Aero-Medical Examiner (AME) and suspend flight privileges in cases of:\n"
        "• Hospital admission or clinic stay exceeding 12 hours.\n"
        "• Any significant surgical operation or invasive procedure.\n"
        "• Illness causing incapacity to fly for 21 DAYS or more (Class 1) or 30 DAYS or more (Class 2/LAPL).\n"
        "• Pregnancy: Pilot may fly until end of the 26th week of gestation under multi-pilot ops with Class 1 medical.",
        max_chars=92
    )

    pdf.add_heading_1("6. Age Limitations for Commercial Operations (Part-FCL.065)")
    pdf.add_callout(
        "trap",
        "The Rule of 60 and 65 (Part-FCL.065)",
        "• Age 60 to 64: A pilot licence holder who has reached age 60 shall NOT act as pilot in commercial air transport "
        "EXCEPT as member of a multi-pilot crew, and provided the other pilot is UNDER 60 YEARS OF AGE.\n"
        "• Age 65: Absolute cutoff. No pilot aged 65 or over may act as pilot in commercial air transport.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Total flight time required for ATPL(A)? -> 1,500 hours.")
    pdf.add_bullet("Q2", "Multi-pilot hours required for ATPL? -> 500 hours.")
    pdf.add_bullet("Q3", "Validity of Class 1 medical for a 45-year-old airline pilot? -> 12 months (6 months only for single-pilot pax).")
    pdf.add_bullet("Q4", "Number of days of incapacity triggering Class 1 notification? -> 21 days (Class 2: 30 days).")
    pdf.add_bullet("Q5", "Recency requirement to carry passengers? -> 3 take-offs and landings in preceding 90 days.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 4 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 5: RULES OF THE AIR (SERA, VMC, SIGNALS & INTERCEPTION)
# ==============================================================================
def build_ch05():
    pdf_path = os.path.join(BASE_DIR, "010_ch05_rules_of_the_air.pdf")
    md_path = os.path.join(BASE_DIR, "010_ch05_rules_of_the_air.md")

    pdf = PDFBuilder("Air Law", "010", "Chapter 5: Rules of the Air (SERA Regulation)")
    pdf.add_title_banner("Air Law", 5, "Rules of the Air & SERA", "101-156")

    pdf.add_heading_1("1. Regulatory Authority & PIC Responsibilities (SERA)")
    pdf.add_paragraph(
        "Standard European Rules of the Air (SERA) are established by Commission Implementing Regulation (EU) No 923/2012 "
        "and ICAO Annex 2. The Pilot-in-Command (PIC) has final authority over the disposition of the aircraft and is "
        "responsible for compliance with the rules of the air, but may deviate in an emergency in the interest of safety.",
        max_chars=92
    )

    pdf.add_heading_1("2. Visual Meteorological Conditions (VMC) Minima Table")
    pdf.add_paragraph(
        "VMC minima define when a flight may proceed under Visual Flight Rules (VFR). AviationExam questions "
        "strictly test exact cloud distance and visibility numbers across airspace classes:",
        max_chars=92
    )

    vmc_table = [
        ["FL 100 and above", "Classes A, B, C, D, E, F, G", "8 km", "1,500 m horizontal, 1,000 ft (300 m) vertical."],
        ["Below FL 100 (or above 3,000 ft AMSL whichever is higher)", "Classes B, C, D, E, F, G (Class A: IFR only)", "5 km", "1,500 m horizontal, 1,000 ft (300 m) vertical."],
        ["At or below 3,000 ft AMSL (or 1,000 ft AGL whichever is higher)", "Classes F and G", "5 km*", "Clear of clouds and with the surface in sight.\n(*Reduced to 1,500 m if speed <= 140 kt IAS)."]
    ]
    pdf.add_table(["Altitude / Level Band", "Airspace Classes", "Min. Flight Visibility", "Distance from Clouds"], vmc_table, col_widths=[105.0, 115.0, 85.0, 205.0])

    pdf.add_callout(
        "trap",
        "VFR in Class A Airspace & Special VFR (CTR)",
        "1. Airspace Class A: VFR flights are STRICTLY PROHIBITED (IFR only).\n"
        "2. Special VFR (Control Zone CTR only): Granted by ATC when weather is below VMC:\n"
        "   - Ground visibility: at least 1,500 m (800 m for helicopters);\n"
        "   - Ceiling: at least 600 ft (180 m);\n"
        "   - Clear of clouds and in sight of the surface;\n"
        "   - Maximum indicated airspeed: 140 kt IAS.",
        max_chars=86
    )

    pdf.add_heading_1("3. Minimum Safe Heights for VFR Flights")
    pdf.add_bullet("Congested Areas (Cities, Towns, Open-Air Gatherings)", "At least 1,000 ft (300 m) above the highest obstacle within a 600 m radius of the aircraft, and high enough to permit safe emergency landing.")
    pdf.add_bullet("Other Areas (Rural / Sea)", "At least 500 ft (150 m) above ground or water, or 500 ft above the highest obstacle within 150 m of the aircraft.")

    pdf.add_heading_1("4. Semicircular Cruising Levels (SERA.5015)")
    pdf.add_paragraph(
        "Cruising levels are based on MAGNETIC TRACK. In RVSM airspace (FL 290 to FL 410), vertical separation is 1,000 ft:",
        max_chars=92
    )

    levels_data = [
        ["Track 000° to 179° (EAST)", "ODD Flight Levels (FL 050, 070, 090, 110, 130...)", "ODD + 500 ft (FL 055, 075, 095, 115...)"],
        ["Track 180° to 359° (WEST)", "EVEN Flight Levels (FL 060, 080, 100, 120, 140...)", "EVEN + 500 ft (FL 065, 085, 105, 125...)"]
    ]
    pdf.add_table(["Magnetic Track", "IFR Cruising Levels", "VFR Cruising Levels (Above 3,000 ft)"], levels_data, col_widths=[125.0, 190.0, 190.0])

    pdf.add_heading_1("5. Right-of-Way Rules (Collision Avoidance)")
    pdf.add_bullet("Hierarchy", "Balloons > Gliders > Airships > Power-driven aircraft. (Aircraft towing another has right of way over power-driven aircraft).")
    pdf.add_bullet("Converging", "When two aircraft converge at approximately the same level, the aircraft having the other on its RIGHT shall give way.")
    pdf.add_bullet("Approaching Head-on", "Each aircraft shall alter its heading to the RIGHT.")
    pdf.add_bullet("Overtaking", "The aircraft being overtaken has right-of-way. The overtaking aircraft keeps clear by altering heading to the RIGHT.")
    pdf.add_bullet("Landing", "Aircraft in flight or on ground shall give way to aircraft landing or in final approach. Between two approaching to land, the LOWER aircraft has right of way, but shall not cut in.")

    pdf.add_heading_1("6. Aircraft Lights (SERA.3215)")
    pdf.add_paragraph(
        "Navigation lights must be displayed from SUNSET TO SUNRISE (and any other period prescribed by authority):",
        max_chars=92
    )
    pdf.add_bullet("Port Wing Light", "RED light showing an unbroken arc of 110° from dead ahead to port.")
    pdf.add_bullet("Starboard Wing Light", "GREEN light showing an unbroken arc of 110° from dead ahead to starboard.")
    pdf.add_bullet("Tail Light", "WHITE light showing an unbroken arc of 140° visible aft.")
    pdf.add_bullet("Anti-Collision Lights", "Flashing red or white light displayed by day and night to indicate operating engines.")

    pdf.add_heading_1("7. ATC Light Gun Signals (Tower to Aircraft)")
    pdf.add_paragraph(
        "When radio communication fails, the control tower uses a directional light gun to control aircraft:",
        max_chars=92
    )

    light_gun_data = [
        ["Steady Green", "Cleared to land", "Cleared for take-off"],
        ["Flashing Green", "Return for landing (followed by steady green)", "Cleared to taxi"],
        ["Steady Red", "Give way to other aircraft and continue circling", "STOP immediately"],
        ["Flashing Red", "Aerodrome unsafe, DO NOT LAND", "Taxi clear of runway in use"],
        ["Flashing White", "Land at this aerodrome and proceed to apron", "Return to starting point on aerodrome"],
        ["Red Pyrotechnic", "Notwithstanding previous instructions, DO NOT LAND for the time being", "—"]
    ]
    pdf.add_table(["Light Signal", "Meaning to Aircraft IN FLIGHT", "Meaning to Aircraft ON GROUND"], light_gun_data, col_widths=[105.0, 200.0, 205.0])

    pdf.add_heading_1("8. Visual Ground Signals in Aerodrome Signal Area")
    signals_data = [
        ["Red square with yellow diagonals", "Landings prohibited; prohibition is likely to be prolonged."],
        ["Red square with one yellow diagonal", "Special precautions landing: state of maneuvering area poor, land with care."],
        ["White dumb-bell", "Landings, take-offs, and taxiing must be confined to paved/hard surfaces."],
        ["White dumb-bell with black bars", "Take-offs and landings on runways only, but other movements not confined to paved taxiways."],
        ["White cross on runway/taxiway", "Runway or taxiway unserviceable; closed to all aircraft movements."],
        ["Landing T (White or Orange)", "Landings and take-offs shall be in a direction parallel to the shaft toward the crossarm."],
        ["Tetrahedron (White or Orange)", "Indicates landing direction: aircraft lands in direction towards which apex points."],
        ["Arrow on runway (Yellow/White)", "Preceding area before displaced threshold fit for taxi and take-off, but NOT for landing."]
    ]
    pdf.add_table(["Ground Signal Symbol", "Official Meaning & Requirement (Annex 14 / SERA)"], signals_data, col_widths=[160.0, 350.0])

    pdf.add_heading_1("9. Interception Procedures (Annex 2 / SERA)")
    pdf.add_callout(
        "trap",
        "Interception of Civil Aircraft (AviationExam Core)",
        "• Interception is a measure of last resort.\n"
        "• Intercepted aircraft must immediately:\n"
        "  1) Follow instructions given by intercepting aircraft;\n"
        "  2) Notify ATS unit immediately;\n"
        "  3) Squawk Mode A Code 7700 (unless instructed otherwise);\n"
        "  4) Monitor emergency frequency 121.5 MHz (and 243.0 MHz).\n"
        "• Interceptor Day Signals:\n"
        "  - Rocking wings and slow left turn: 'You have been intercepted, follow me'. Response: Rocking wings ('Understood, will comply').\n"
        "  - Abrupt breakaway climb and turn: 'You may proceed'.",
        max_chars=86
    )

    pdf.add_heading_2("5-Second Flash Drill")
    pdf.add_bullet("Q1", "Tower light signal: Flashing Red to aircraft in flight? -> Aerodrome unsafe, DO NOT LAND.")
    pdf.add_bullet("Q2", "Tower light signal: Steady Red to aircraft on ground? -> STOP.")
    pdf.add_bullet("Q3", "Visual signal: Red square with yellow diagonals? -> Landings prohibited.")
    pdf.add_bullet("Q4", "Transponder code set when intercepted? -> Mode A Code 7700.")
    pdf.add_bullet("Q5", "Angular coverage of the tail navigation light? -> 140° white light.")

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 5 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch01()
    build_ch02()
    build_ch03()
    build_ch04()
    build_ch05()
