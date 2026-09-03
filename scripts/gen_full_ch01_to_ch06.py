#!/usr/bin/env python3
"""
Full-Depth Study Manual Generator - Volume 1 (Chapters 1 to 6).
Designed for 100% self-contained study.
Target: ~20 pages total across Chapters 1 to 6.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.pdf_builder import PDFBuilder

BASE_DIR = "resumenes/convocatoria_1/010_air_law"

# ==============================================================================
# CHAPTER 1: INTERNATIONAL AGREEMENTS AND ORGANIZATIONS (~6 pages)
# ==============================================================================
def build_ch01():
    pdf_path = os.path.join(BASE_DIR, "010_ch01_international_agreements.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 1: International Agreements & ICAO")
    pdf.add_title_banner("Air Law", 1, "International Agreements & ICAO", "21-52")

    pdf.add_heading_1("1. Historical Evolution & Chicago Convention (1944)")
    pdf.add_paragraph(
        "Prior to World War II, international aviation was governed by fragmented regional treaties such as the 1919 "
        "Paris Convention (which first codified national sovereignty over airspace) and the 1928 Havana Convention. "
        "The massive technological advances of World War II created an urgent need for a unified global framework. "
        "On 7 December 1944, representatives of 52 Allied and neutral nations signed the Convention on International "
        "Civil Aviation in Chicago. It entered into force on 4 April 1947 after ratification by the 26th State, "
        "officially establishing the International Civil Aviation Organization (ICAO).",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "Preamble of the Chicago Convention",
        "WHEREAS the future development of international civil aviation can greatly help to create and preserve "
        "friendship and understanding among the nations and peoples of the world, yet its abuse can become a threat to "
        "the general security; ... THEREFORE, the undersigned governments have concluded certain principles and "
        "arrangements in order that international civil aviation may be developed in a safe and orderly manner.",
        max_chars=86
    )

    pdf.add_heading_1("2. Exhaustive Analysis of Chicago Convention Articles")
    pdf.add_paragraph(
        "The Chicago Convention consists of 96 articles divided into four parts. The following 22 articles are "
        "frequently and rigorously tested in EASA examinations:",
        max_chars=92
    )

    articles_1 = [
        ["Art. 1: Sovereignty", "Every Contracting State has complete and exclusive sovereignty over the airspace above its territory."],
        ["Art. 2: Territory", "Territory consists of the land areas and adjacent territorial waters (up to 12 NM) under the sovereignty of the State. Airspace over the High Seas is international and has no State sovereignty."],
        ["Art. 3: Civil vs State Aircraft", "Applies SOLELY to civil aircraft. Aircraft used in military, customs, and police services are deemed State aircraft. State aircraft cannot fly over or land on foreign territory without authorization by special agreement."],
        ["Art. 3 bis: Non-use of Weapons", "Contracting States must refrain from resorting to the use of weapons against civil aircraft in flight. In case of interception, the lives of persons on board must not be endangered. States may require landing at a designated airport."],
        ["Art. 5: Non-scheduled Flights", "Aircraft of Contracting States not engaged in scheduled international services have the right to fly into or in transit non-stop across territory and make stops for non-traffic purposes without prior permission, subject to the right of the State to require landing."],
        ["Art. 6: Scheduled Air Services", "No scheduled international air service may be operated over or into the territory of a Contracting State except with special permission or authorization of that State."],
        ["Art. 7: Cabotage", "Each Contracting State has the right to refuse permission to the aircraft of other States to take on passengers, cargo, and mail destined for another point within its own territory for remuneration."],
        ["Art. 8: Pilotless Aircraft", "No aircraft capable of being flown without a pilot shall be flown without a pilot over the territory of a Contracting State without special authorization."],
        ["Art. 9: Prohibited Areas", "States may restrict or prohibit aircraft from flying over certain areas of territory for reasons of military necessity or public safety, provided no distinction is made between national and foreign aircraft."]
    ]
    pdf.add_table(["Article", "Official Legal Requirement & Exam Core"], articles_1, col_widths=[140.0, 370.0])

    articles_2 = [
        ["Art. 10: Customs Airports", "Every aircraft entering a State must land at a designated customs airport if required by regulations."],
        ["Art. 11: Applicability of Air Regulations", "Domestic air laws and regulations apply to all aircraft without distinction as to nationality."],
        ["Art. 12: Rules of the Air", "Over the High Seas, the rules in force are those established by ICAO (Annex 2) WITHOUT EXCEPTION. Over land, national rules apply."],
        ["Art. 13: Entry and Clearance", "The laws and regulations of a State regarding immigration, customs, quarantine, and passports must be complied with upon entry, departure, or while within territory."],
        ["Art. 16: Search of Aircraft", "Authorities of a Contracting State have the right to search foreign aircraft upon landing or departure without causing unreasonable delay."],
        ["Art. 22 & 23: Facilitation", "States agree to adopt all practicable measures to facilitate air navigation and prevent unnecessary delays."],
        ["Art. 24: Customs Duties on Fuel", "Fuel, lubricating oils, spare parts, and regular equipment on board an aircraft of a Contracting State on arrival shall be exempt from customs duty and inspection fees."],
        ["Art. 29: Documents on Board", "Every aircraft on an international flight MUST carry: 1) Certificate of Registration, 2) Certificate of Airworthiness, 3) Crew Licences, 4) Journey Log Book, 5) Aircraft Radio Licence, 6) Passenger Manifest (names and places of embarkation/destination), 7) Cargo Manifest."],
        ["Art. 31 & 32: C of A and Licences", "Every aircraft must have a valid C of A issued by State of Registry. Flight crew must hold licences issued or validated by State of Registry."],
        ["Art. 33: Mutual Recognition", "Certificates of Airworthiness and licences issued or validated by the State of Registry MUST be recognized as valid by other States, provided the requirements equal or exceed minimum ICAO standards."],
        ["Art. 37: Adoption of Standards", "ICAO shall adopt International Standards and Recommended Practices (SARPs) in Annexes."],
        ["Art. 38: Notification of Differences", "Any State that finds it impracticable to comply with an international Standard MUST immediately give notification to ICAO of differences. Notification is mandatory for Standards."],
        ["Art. 83 bis: Transfer of Functions", "Enables transfer of State of Registry functions (licensing, airworthiness, ops) to the State of the Operator in cases of dry/wet lease, charter, or interchange of aircraft."]
    ]
    pdf.add_table(["Article", "Official Legal Requirement & Exam Core (Continued)"], articles_2, col_widths=[140.0, 370.0])

    pdf.add_callout(
        "trap",
        "AviationExam Traps on Articles 3, 7, 12, 24 and 38",
        "• State Aircraft Status: Military, police, and customs are State aircraft. An unarmed military transport carrying civilian cargo is STILL a State aircraft!\n"
        "• High Seas Jurisdiction: No State has sovereignty over the High Seas. ICAO Annex 2 applies universally without exception.\n"
        "• Customs on Fuel: Fuel inside aircraft tanks is exempt from customs duties. Fuel unloaded into ground tanks is NOT exempt!\n"
        "• Article 38 Differences: Compulsory ONLY for Standards (compulsory). Recommended Practices do NOT legally require formal notification under Art. 38.",
        max_chars=86
    )

    pdf.add_heading_1("3. The Nine Freedoms of the Air")
    pdf.add_paragraph(
        "Commercial transit and traffic rights are granted through bilateral Air Transport Agreements (e.g. Bermuda Agreements). "
        "ICAO classifies these traffic rights into 9 distinct Freedoms of the Air:",
        max_chars=92
    )

    freedoms_table = [
        ["1st Freedom (Overflight)", "Technical", "The right to fly across the territory of another State without landing.", "British Airways flying London to Athens over France."],
        ["2nd Freedom (Tech Stop)", "Technical", "The right to land in foreign territory for non-traffic purposes (refueling, crew rest, mechanical).", "Iberia landing in the Azores (Portugal) for fuel en-route to South America."],
        ["3rd Freedom (Outbound Traffic)", "Commercial", "The right to put down passengers, mail, and cargo taken on in the airline's Home State into a foreign State.", "Lufthansa flying passengers from Frankfurt to New York."],
        ["4th Freedom (Inbound Traffic)", "Commercial", "The right to take on passengers, mail, and cargo in a foreign State and put them down in the airline's Home State.", "Lufthansa flying passengers from New York to Frankfurt."],
        ["5th Freedom (Intermediate Traffic)", "Commercial", "The right to carry traffic between two foreign States on a flight originating or terminating in the airline's Home State.", "Emirates flying Dubai -> London -> New York, boarding commercial passengers in London for New York."],
        ["6th Freedom (Hub Traffic)", "Extended", "The right to carry traffic between two foreign States via a commercial transit stop in the airline's Home State.", "Air France carrying passengers from Madrid to Tokyo via Paris CDG hub."],
        ["7th Freedom (Stand-Alone Foreign)", "Extended", "The right to carry traffic between two foreign States entirely outside the Home State, with no connection to home.", "Ryanair (Irish airline) operating scheduled flights between Rome (Italy) and Berlin (Germany)."],
        ["8th Freedom (Consecutive Cabotage)", "Cabotage", "The right to carry traffic between two domestic points in a foreign State on a flight starting or ending in Home State.", "Air France operating Paris -> Madrid -> Barcelona, carrying passengers between Madrid and Barcelona."],
        ["9th Freedom (Pure Cabotage)", "Cabotage", "The right to operate domestic passenger services entirely within a foreign State without any connection to Home State.", "Lufthansa operating scheduled domestic flights between Madrid and Seville in Spain."]
    ]
    pdf.add_table(["Freedom", "Category", "Official ICAO Definition", "Practical Airline Scenario"], freedoms_table, col_widths=[95.0, 65.0, 190.0, 160.0])

    pdf.add_heading_1("4. Structure and Governance of ICAO")
    pdf.add_paragraph(
        "ICAO is a specialized agency of the United Nations headquartered in Montreal, Quebec, Canada. Its governance "
        "consists of three principal organs:",
        max_chars=92
    )
    pdf.add_bullet("The Assembly", "Sovereign body comprising all 193 Contracting States. Meets once every 3 YEARS. Each State has ONE vote. Key functions: elects the Council, reviews technical work, approves triennial budget, and amends the Convention by a 2/3 vote.")
    pdf.add_bullet("The Council", "Permanent governing executive body responsible to the Assembly, comprising 36 Contracting States elected for a 3-year term. Categories of election: 1) States of chief importance in air transport, 2) States making largest contribution to provision of facilities, 3) States ensuring geographic representation. Key functions: ADOPTS ANNEXES (SARPs) by a 2/3 vote, appoints the Secretary General, manages finances, and investigates any situation presenting avoidable obstacles to international air navigation.")
    pdf.add_bullet("Air Navigation Commission (ANC)", "Composed of 19 independent technical experts nominated by Contracting States and appointed by the Council. Responsible for drafting and updating all Annexes and PANS.")
    pdf.add_bullet("Regional Offices", "7 offices: Paris (EUR/NAT), Dakar (WACAF), Nairobi (ESAF), Cairo (MID), Bangkok (APAC), Lima (SAM), and Mexico City (NACC).")

    pdf.add_heading_1("5. Master Catalogue: All 19 ICAO Annexes")
    annexes_full = [
        ["Annex 1", "Personnel Licensing", "Licences for flight crew, ATCOs, flight engineers, maintenance engineers; medical classes 1, 2, 3."],
        ["Annex 2", "Rules of the Air", "Visual flight rules (VFR), instrument flight rules (IFR), right of way, lights, signals, interception."],
        ["Annex 3", "Meteorological Service", "METAR, TAF, SIGMET, AIRMET, GAMET, aerodrome forecasts, world area forecast system (WAFS)."],
        ["Annex 4", "Aeronautical Charts", "17 chart types including SID, STAR, Instrument Approach, Aerodrome Obstacle Charts Type A and B."],
        ["Annex 5", "Units of Measurement", "SI units and non-SI alternatives: altitude in feet, speed in knots, distance in nautical miles."],
        ["Annex 6", "Operation of Aircraft", "Part I: Commercial Air Transport Aeroplanes, Part II: General Aviation, Part III: Helicopters."],
        ["Annex 7", "Aircraft Nationality & Registration", "Lettering height (30 cm wings/fuselage), hyphen rule, fireproof identification plate near entrance."],
        ["Annex 8", "Airworthiness of Aircraft", "Type Certificates, C of A, continuing airworthiness, applicability to MTOM > 5,700 kg, multi-engine."],
        ["Annex 9", "Facilitation", "Simplification of customs, immigration, General Declaration, crew identity, transit rules."],
        ["Annex 10", "Aeronautical Telecommunications", "Vol I: Nav Aids (ILS, VOR, DME), Vol II: Voice procedures, Vol III: Data, Vol IV: Radar, Vol V: Spectrum."],
        ["Annex 11", "Air Traffic Services", "Air Traffic Control (ATC), Flight Information Service (FIS), Alerting Service, Airspace classes A-G."],
        ["Annex 12", "Search and Rescue (SAR)", "Rescue Coordination Centres (RCC), emergency phases (INCERFA, ALERFA, DETRESFA), search patterns."],
        ["Annex 13", "Aircraft Accident Investigation", "Accident/Incident definitions, notification, State of Occurrence, sole objective: PREVENT recurrence."],
        ["Annex 14", "Aerodromes", "Vol I: Aerodrome Design & Operations (runways, taxiways, markings, lighting, RFFS), Vol II: Heliports."],
        ["Annex 15", "Aeronautical Information Services", "AIP (GEN, ENR, AD), AIRAC 28-day cycle, NOTAM, SNOWTAM, ASHTAM, AICs, pre-flight bulletins."],
        ["Annex 16", "Environmental Protection", "Vol I: Aircraft noise certification (Chapters 3, 4, 14), Vol II: Engine emissions, Vol III: CO2 emissions."],
        ["Annex 17", "Security", "Safeguarding civil aviation against acts of unlawful interference, cockpit door security, screening."],
        ["Annex 18", "Dangerous Goods", "Technical Instructions for Safe Transport of Dangerous Goods by Air, packaging, labelling, NOTOC."],
        ["Annex 19", "Safety Management", "State Safety Programmes (SSP) and Safety Management Systems (SMS) for operators and aerodromes."]
    ]
    pdf.add_table(["Annex", "Title", "Core Scope & Key EASA Exam Focus"], annexes_full, col_widths=[75.0, 155.0, 280.0])

    pdf.add_heading_1("6. International Penal and Liability Conventions")
    conv_full = [
        ["Tokyo Convention (1963)", "Offences Committed on Board Aircraft", "Jurisdiction of the State of Registry over criminal acts committed on board. Bestows extensive powers on the Pilot-in-Command: authority to impose reasonable restraint on disruptive passengers, require assistance from crew or passengers, disembark offenders in any Contracting State, and deliver serious offenders to police authorities."],
        ["The Hague Convention (1970)", "Suppression of Unlawful Seizure (Hijacking)", "Establishes universal jurisdiction over hijackers. Any State where the offender is found must either extradite the offender or prosecute without exception ('Aut dedere aut judicare'). Defines hijacking as an extraditable offence in all bilateral treaties."],
        ["Montreal Convention (1971)", "Suppression of Unlawful Acts Against Safety", "Criminalizes acts of sabotage, violence against crew/passengers that endanger flight safety, placing bombs on aircraft, destruction of aircraft in service, and destruction of air navigation facilities."],
        ["Rome Convention (1933 / 1952)", "Damage Caused by Foreign Aircraft to 3rd Parties", "Strict (absolute) liability of aircraft operators for surface damage caused to persons or property on the ground. Proof of fault is not required; victim needs only prove damage caused by aircraft or falling objects."],
        ["Warsaw Convention (1929)", "Air Carrier Liability (Historic)", "Unified liability limits for passenger injury/death (originally 125,000 gold francs), checked baggage, and cargo loss. Established liability presumption against carrier unless carrier proves all necessary measures were taken."],
        ["Montreal Convention (1999)", "Modernised Air Carrier Liability", "Completely modernized passenger carrier liability into a TWO-TIER SYSTEM using SDRs (Special Drawing Rights): Tier 1 (Strict liability up to ~128,821 SDRs, carrier cannot contest), Tier 2 (Unlimited liability based on fault, carrier liable unless proving damage was not due to its negligence). Eliminates passenger ticket technicality defenses."]
    ]
    pdf.add_table(["Convention & Year", "Legal Scope", "Key Principles & Detailed Exam Specifics"], conv_full, col_widths=[110.0, 140.0, 260.0])

    pdf.add_heading_1("7. European Aviation Regulatory Architecture")
    pdf.add_bullet("EASA (European Union Aviation Safety Agency)", "Headquartered in Cologne, Germany. Established by Basic Regulation (EU) 2018/1139. Responsible for: drafting European aviation legislation (Cover Regulations, AMC & GM), issuing Type Certificates for aircraft/engines/propellers, approving design and production organizations (Part-21), approving non-EU maintenance organizations, and standardization inspections across EU National Aviation Authorities (NAAs).")
    pdf.add_bullet("EUROCONTROL", "Headquartered in Brussels, Belgium. Founded in 1960. 41 Member States. Operates the Network Manager Operations Centre (NMOC) managing air traffic flow management (ATFM) slots across Europe to prevent sector overload, and the Central Route Charges Office (CRCO) collecting overflight navigation charges.")
    pdf.add_bullet("ECAC (European Civil Aviation Conference)", "Established in 1955, located in Paris. 44 European States. Consultative intergovernmental body promoting safety harmonization, aviation security audit programs, and environmental policies.")

    pdf.add_heading_2("AviationExam 10-Question Comprehensive Drill")
    drills = [
        ("Q1: Who adopts ICAO Annexes?", "The Council of ICAO by a two-thirds (2/3) majority vote."),
        ("Q2: Under which Article must a State notify differences to ICAO Standards?", "Article 38 of the Chicago Convention."),
        ("Q3: Does the Chicago Convention apply to military or customs aircraft?", "NO. Under Article 3, it applies exclusively to civil aircraft."),
        ("Q4: Over the High Seas, whose rules of the air apply?", "ICAO Rules of the Air (Annex 2) apply without exception (Article 12)."),
        ("Q5: Carrying passengers between two domestic points in a foreign State is which freedom?", "8th Freedom (consecutive cabotage) or 9th Freedom (pure stand-alone cabotage)."),
        ("Q6: Which Convention gives the Pilot-in-Command authority to restrain unruly passengers?", "The Tokyo Convention (1963)."),
        ("Q7: Under the Montreal Convention 1999, what is the carrier's liability system?", "A two-tier system: strict liability up to ~128,821 SDRs, and unlimited fault-based liability thereafter."),
        ("Q8: What is the purpose of Article 83 bis?", "Allows transfer of State of Registry regulatory functions to the State of the Operator in aircraft leases."),
        ("Q9: What is the legal status of an ICAO Recommended Practice?", "Desirable, but not essential. Notification of differences under Art. 38 is not strictly mandatory."),
        ("Q10: Where are EASA and EUROCONTROL headquartered?", "EASA is in Cologne (Germany); EUROCONTROL is in Brussels (Belgium).")
    ]
    for q, a in drills:
        pdf.add_bullet(q, a)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 1 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 2: AIRWORTHINESS OF AIRCRAFT & MEL (~4 pages)
# ==============================================================================
def build_ch02():
    pdf_path = os.path.join(BASE_DIR, "010_ch02_airworthiness.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 2: Airworthiness of Aircraft & MEL")
    pdf.add_title_banner("Air Law", 2, "Airworthiness & MEL Systems", "53-58")

    pdf.add_heading_1("1. Regulatory Framework: Annex 8 vs Annex 6")
    pdf.add_paragraph(
        "Airworthiness is the intrinsic safety of an aircraft to operate safely within authorized flight operating limits. "
        "Under the ICAO regulatory framework, airworthiness is split across two core Annexes:",
        max_chars=92
    )
    pdf.add_bullet("Annex 8 (Airworthiness of Aircraft)", "Deals with technical, physical, and design standards: structural integrity, propulsion reliability, systems crashworthiness, avionics testing, and continuing airworthiness.")
    pdf.add_bullet("Annex 6 (Operation of Aircraft)", "Deals with operational safety standards: flight instruments, operating limitations, emergency equipment, performance operating minimums, and maintenance operational management.")

    pdf.add_callout(
        "definition",
        "Annex 8 Applicability Scope (EASA ECQB Core)",
        "The international airworthiness standards of ICAO Annex 8, Part III apply to aeroplanes with a Maximum "
        "Take-Off Mass (MTOM) GREATER THAN 5,700 kg, powered by at least TWO engines, and intended for the "
        "international carriage of passengers, cargo, or mail.",
        max_chars=86
    )

    pdf.add_heading_1("2. Certification Chain: Prototype to Commercial Airline")
    pdf.add_paragraph(
        "An aircraft design and individual airframe pass through strict legal certification stages:",
        max_chars=92
    )

    cert_table = [
        ["1. Permit to Fly", "State of Registry or State of Design", "Allows non-certified prototype aircraft or aircraft with minor airworthiness defects to fly for flight testing, prototype evaluation, or ferry flight to a maintenance facility."],
        ["2. Type Certificate (TC)", "State of Design / Manufacture", "Certifies that the design (model) of the aircraft meets all applicable Airworthiness Codes (e.g. EASA CS-25 for large aeroplanes, CS-23 for light aeroplanes). Held by the manufacturer (Airbus, Boeing)."],
        ["3. Supplemental TC (STC)", "State of Design", "Issued to an organization that introduces major modifications or alterations to an existing certified aircraft type (e.g. winglet installation, cargo conversion, glass cockpit upgrade)."],
        ["4. Certificate of Airworthiness (C of A)", "State of Registry", "Issued to EACH INDIVIDUAL aircraft certifying it conforms to the approved Type Certificate and is in condition for safe operation. Must be carried on board on every international flight (Art. 29)."]
    ]
    pdf.add_table(["Certificate", "Issuing Authority", "Legal Scope & Operational Purpose"], cert_table, col_widths=[110.0, 130.0, 270.0])

    pdf.add_callout(
        "trap",
        "State of Manufacture vs State of Registry",
        "AviationExam Trap: Who issues what?\n"
        "• The TYPE CERTIFICATE (TC) is issued by the STATE OF DESIGN / MANUFACTURE (e.g. France for Airbus, USA for Boeing).\n"
        "• The CERTIFICATE OF AIRWORTHINESS (C of A) for each individual aircraft is issued or validated by the STATE OF REGISTRY.",
        max_chars=86
    )

    pdf.add_heading_1("3. Continuing Airworthiness: EASA Part-M, Part-CAMO & Part-145")
    pdf.add_paragraph(
        "A Certificate of Airworthiness remains valid only if continuing airworthiness is maintained in accordance with EASA Part-M:",
        max_chars=92
    )
    pdf.add_bullet("Airworthiness Directives (AD)", "Legally enforceable rules issued by the State of Design or EASA to correct an unsafe condition found in an aircraft type. ADs are MANDATORY. Failure to comply with an AD invalidates the C of A immediately, grounding the aircraft.")
    pdf.add_bullet("Service Bulletins (SB)", "Technical documents issued by aircraft or engine manufacturers suggesting improvements, modifications, or specialized inspections. SBs are NON-MANDATORY by default, unless mandated by an Airworthiness Directive.")
    pdf.add_bullet("Certificate of Release to Service (CRS)", "Issued by appropriately licensed Part-145 certifying staff after any maintenance, overhaul, repair, or modification before the aircraft is permitted to fly.")
    pdf.add_bullet("Airworthiness Review Certificate (ARC - EASA Form 15a/b/c)", "Under EASA Part-M, a standard C of A has an unlimited duration, but is legally valid ONLY when accompanied by a valid ARC, which must be renewed ANNUALLY (1-year validity). Form 15a is issued by the Authority; Form 15b is issued by an approved CAMO; Form 15c by a CAO.")

    pdf.add_heading_1("4. Minimum Equipment List (MEL) & CDL Architecture")
    pdf.add_paragraph(
        "Commercial transport aircraft may depart with inoperative instruments or equipment ONLY under strict approved relief rules:",
        max_chars=92
    )
    pdf.add_bullet("MMEL (Master Minimum Equipment List)", "Established by the manufacturer and approved by the State of Design. Lists items that may temporarily be inoperative under specified operating conditions.")
    pdf.add_bullet("MEL (Minimum Equipment List)", "Established by the OPERATOR for each aircraft type, based on the MMEL, and approved by the State of the Operator. The MEL can be MORE restrictive than the MMEL, but NEVER LESS restrictive.")
    pdf.add_bullet("Configuration Deviation List (CDL)", "Lists external missing aerodynamic or structural parts (e.g. flap track fairings, landing gear doors, static wicks) permitted for dispatch, along with associated aircraft performance penalties.")

    pdf.add_heading_2("MEL Rectification Interval Categories (AviationExam Core)")
    mel_data = [
        ["Category A", "No standard calendar time limit. Must be repaired within the specific time interval listed in the remarks column of the MEL (e.g. 5 flight cycles, 10 flight hours)."],
        ["Category B", "Must be rectified within THREE (3) consecutive calendar days (72 hours), excluding the day the defect was entered in the logbook."],
        ["Category C", "Must be rectified within TEN (10) consecutive calendar days (240 hours), excluding the day the defect was discovered."],
        ["Category D", "Must be rectified within ONE HUNDRED AND TWENTY (120) consecutive calendar days, excluding the day of discovery."]
    ]
    pdf.add_table(["Rectification Category", "Mandatory Legal Repair Time Limit"], mel_data, col_widths=[125.0, 385.0])

    pdf.add_heading_1("5. Maintenance Records & Component Release (EASA Form 1)")
    pdf.add_paragraph(
        "Continuing airworthiness records must be preserved to prove compliance:\n"
        "• Maintenance records must be retained until 36 MONTHS after the aircraft has been permanently withdrawn from service.\n"
        "• EASA Form 1: The official Authorized Release Certificate certifying that a component or part has been manufactured or maintained in accordance with approved data.",
        max_chars=92
    )

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: Under EASA Part-M, what is the validity period of an Airworthiness Review Certificate (ARC)?",
         "[A] 6 months\n[B] 1 year\n[C] 2 years\n[D] Unlimited provided maintenance is carried out",
         "CORRECT: [B]. The ARC is valid for 1 year and must be re-issued annually by an approved CAMO or authority."),
        ("Q2: What is the legal status of an Airworthiness Directive (AD) versus a Service Bulletin (SB)?",
         "[A] Both are voluntary recommendations.\n[B] SBs are mandatory; ADs are optional.\n[C] ADs are mandatory; SBs are non-mandatory unless mandated by an AD.\n[D] ADs only apply to military aircraft.",
         "CORRECT: [C]. An Airworthiness Directive is legally binding and mandatory. A Service Bulletin is recommended by the manufacturer but only becomes legally mandatory if incorporated into an AD."),
        ("Q3: Can an operator depart with an item inoperative that is NOT listed in the MEL?",
         "[A] Yes, at the discretion of the Commander.\n[B] Yes, if operating in daylight VMC.\n[C] NO, all inoperative items must be covered by relief in the MEL or repaired before flight.\n[D] Yes, for domestic ferry flights.",
         "CORRECT: [C]. Under Part-CAT, an aircraft cannot be dispatched with an inoperative item unless specifically permitted by the approved MEL."),
        ("Q4: What is the maximum allowable rectification interval for Category C MEL items?",
         "[A] 3 calendar days (72 hours)\n[B] 10 calendar days (240 hours)\n[C] 30 calendar days\n[D] 120 calendar days",
         "CORRECT: [B]. Category C items must be rectified within 10 consecutive calendar days excluding the day of discovery."),
        ("Q5: What document certifies that an individual aircraft component has been maintained to approved data?",
         "[A] EASA Form 1\n[B] EASA Form 15b\n[C] Certificate of Airworthiness\n[D] Journey Log Book",
         "CORRECT: [A]. EASA Form 1 is the official Authorised Release Certificate for aircraft components and parts.")
    ]
    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 2 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 3: AIRCRAFT NATIONALITY AND REGISTRATION MARKS (~3 pages)
# ==============================================================================
def build_ch03():
    pdf_path = os.path.join(BASE_DIR, "010_ch03_registration_marks.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 3: Aircraft Nationality & Registration Marks")
    pdf.add_title_banner("Air Law", 3, "Nationality & Registration Marks", "59-66")

    pdf.add_heading_1("1. Legal Foundations: Chicago Convention & Annex 7")
    pdf.add_paragraph(
        "Under Article 17 of the Chicago Convention, aircraft have the nationality of the State in which they are registered. "
        "Annex 7 specifies international standards for nationality and registration marks, placement, lettering dimensions, "
        "and identification plates.",
        max_chars=92
    )

    pdf.add_bullet("Dual Registration Prohibited (Art. 18)", "An aircraft cannot be validly registered in more than one State at the same time. However, registration may be transferred from one State to another.")
    pdf.add_bullet("Domestic Law Governs (Art. 19)", "The registration or transfer of registration of aircraft in any Contracting State shall be made in accordance with its national laws and regulations.")
    pdf.add_bullet("Display of Marks (Art. 20)", "Every aircraft engaged in international air navigation shall bear its appropriate nationality and registration marks.")

    pdf.add_heading_1("2. Structure of Marks: Nationality vs Registration")
    pdf.add_bullet("Nationality Mark", "Selected from the series of nationality symbols included in the radio call signs allocated to the State of Registry by the International Telecommunication Union (ITU). Examples: G = United Kingdom, F = France, D = Germany, EC = Spain, EI = Ireland, N = USA, HB = Switzerland, OO = Belgium, PH = Netherlands.")
    pdf.add_bullet("Registration Mark", "Consists of letters, numbers, or a combination assigned by the State of Registry or common mark registering authority.")
    pdf.add_bullet("The Hyphen Rule", "When the first character of the registration mark is a LETTER, it MUST be preceded by a HYPHEN (e.g. G-ABCD, EC-MNA, F-GZTA). In the USA, 'N' followed by numbers requires no hyphen (e.g. N12345).")
    pdf.add_bullet("Common Mark", "Assigned by ICAO to the common mark registering authority of an international operating agency (such as Arab Air Cargo). Preceded by a symbol assigned by ICAO.")

    pdf.add_heading_1("3. Location and Minimum Sizing Rules (Annex 7)")
    size_data = [
        ["Wings (Lower Surface)", "Port (left) half of lower wing surface.", "At least 30 cm (300 mm)", "Tops of letters directed toward leading edge."],
        ["Fuselage / Vertical Tail", "Each side of fuselage (between wings and tail) OR upper halves of vertical tail surfaces.", "At least 30 cm (300 mm)", "If multi-tail, displayed on outer sides of outer vertical fins."],
        ["Lighter-than-Air (Airships)", "Tail surface or envelope.", "At least 50 cm (500 mm)", "Visible from ground and both sides."],
        ["Lighter-than-Air (Balloons)", "Two places near maximum diameter on opposite sides.", "At least 50 cm (500 mm)", "Equatorial position."]
    ]
    pdf.add_table(["Location on Aircraft", "Position Specifics", "Min. Height", "Orientation & Spacing"], size_data, col_widths=[125.0, 150.0, 110.0, 125.0])

    pdf.add_heading_2("Lettering Proportions & Typography Standards")
    pdf.add_paragraph(
        "• Letters must be capital letters in Roman characters without ornamentation.\n"
        "• Width of each character (except I and 1) shall be 2/3 of its height.\n"
        "• Thickness of lines (stroke) shall be 1/6 of the character height.\n"
        "• Spacing between characters shall not be less than 1/4 of a character width, nor more than 1/2 of character width.",
        max_chars=92
    )

    pdf.add_heading_1("4. The Aircraft Identification Plate")
    pdf.add_paragraph(
        "Every aircraft engaged in international air navigation must carry an identification plate inscribed with its "
        "nationality mark and registration mark:\n"
        "• Material: Must be made of FIREPROOF METAL or other fireproof material of suitable physical properties.\n"
        "• Location: Secured in a prominent position NEAR THE MAIN ENTRANCE of the aircraft.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: Can an aircraft be validly registered in more than one State at the same time?",
         "[A] Yes, in up to 3 States with bilateral approval.\n[B] NO, dual registration is strictly prohibited by Article 18.\n[C] Yes, if operated under wet lease.\n[D] Only within EU Member States.",
         "CORRECT: [B]. Article 18 of the Chicago Convention explicitly prohibits dual registration."),
        ("Q2: Who allocates the series of nationality mark symbols used by States?",
         "[A] ICAO\n[B] The International Telecommunication Union (ITU)\n[C] EASA\n[D] United Nations Security Council",
         "CORRECT: [B]. Nationality marks are selected from radio call sign series allocated by the ITU."),
        ("Q3: What is the minimum height of registration marks displayed on aeroplane wings?",
         "[A] 15 cm\n[B] 30 cm (300 mm)\n[C] 50 cm\n[D] 60 cm",
         "CORRECT: [B]. Annex 7 specifies at least 30 cm for wings and fuselage of heavier-than-air aircraft (50 cm for airships/balloons)."),
        ("Q4: Which of the following letter combinations is strictly prohibited in an aircraft registration mark?",
         "[A] EC-ABC\n[B] G-PAN\n[C] D-AIBA\n[D] F-GLZK",
         "CORRECT: [B]. Combinations that can be confused with distress signals (PAN, SOS, XXX, TTT) or Q-codes (QAA-QNZ) are strictly prohibited."),
        ("Q5: Where must the fireproof aircraft identification plate be located?",
         "[A] Inside the cockpit on the instrument panel\n[B] On the exterior near the main entrance\n[C] Inside the main landing gear bay\n[D] On the vertical fin next to the registration mark",
         "CORRECT: [B]. Under Annex 7, the identification plate must be secured in a prominent position near the main entrance.")
    ]
    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 3 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 4: FLIGHT CREW LICENSING (PART-FCL & PART-MED) (~5 pages)
# ==============================================================================
def build_ch04():
    pdf_path = os.path.join(BASE_DIR, "010_ch04_flight_crew_licensing.pdf")
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

    pdf.add_heading_1("7. ATPL Theory Validity & Crediting Rules")
    pdf.add_paragraph(
        "• ATPL Theoretical Knowledge Examination Pass: Remains valid for the issue of a CPL(A) or IR(A) for a period of 36 MONTHS from the day the pilot successfully passes all theoretical exams.\n"
        "• IR Validity to ATPL: Provided an IR(A) or type rating is kept valid (or renewed within 7 years of last expiry), the ATPL theoretical examination credits remain valid indefinitely for the issue of an ATPL(A).\n"
        "• Multi-Crew Cooperation (MCC): Mandatory before flying multi-pilot aircraft. 25 hours theoretical instruction and at least 20 hours simulator (or 16 hours in FNPT II).",
        max_chars=92
    )

    pdf.add_heading_1("8. Part-MED Clinical Examination Standards")
    med_specs = [
        ["Visual Acuity", "Distant visual acuity 6/9 (0.7) in each eye, 6/6 (1.0) with both eyes. Refractive error limits: +5.0 to -6.0 diopters. Astigmatism max 2.0 diopters. Spare pair of glasses mandatory."],
        ["Color Vision", "Normal trichromatic color vision required. Tested with Ishihara 24 plates (must pass 15 plates on first try). If failed, advanced testing (CAD test / Anomaloscope) required."],
        ["Hearing (Audiometry)", "Pure tone audiometry: Max hearing loss of 20 dB at 500, 1000, 2000 Hz; max 35 dB at 3000 Hz in each ear separately."],
        ["Cardiovascular (ECG)", "Standard resting 12-lead ECG required at initial exam, every 5 years up to age 30, every 2 years up to age 40, annually up to age 50, and at all subsequent medicals."],
        ["Alcohol & Drugs", "Blood Alcohol Concentration (BAC) limit: 0.20 g/l (0.02%). Bottle-to-throttle rule: Minimum 8 hours between alcohol consumption and flight duty."]
    ]
    pdf.add_table(["Clinical Parameter", "Regulatory Medical Standards (EASA Part-MED Class 1)"], med_specs, col_widths=[140.0, 370.0])

    pdf.add_heading_1("9. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: What is the total flight time required for the issue of an ATPL(A)?",
         "[A] 500 hours\n[B] 1,000 hours\n[C] 1,500 hours\n[D] 2,000 hours",
         "CORRECT: [C]. 1,500 hours total flight time is mandatory for ATPL(A), including 500 hours multi-pilot and 250 hours PIC (or 500 PICUS)."),
        ("Q2: What is the validity of a Class 1 medical certificate for a 45-year-old pilot flying single-pilot commercial passenger flights?",
         "[A] 6 months\n[B] 12 months\n[C] 24 months\n[D] 60 months",
         "CORRECT: [A]. Under Part-MED, Class 1 validity is reduced from 12 months to 6 months for pilots aged 40 and over operating single-pilot commercial passenger operations (or age 60+ in any commercial air transport)."),
        ("Q3: What are the recent experience requirements to carry passengers by day under Part-FCL.060?",
         "[A] 3 take-offs and landings in the preceding 60 days\n[B] 3 take-offs and landings in the preceding 90 days\n[C] 5 take-offs and landings in the preceding 90 days\n[D] 10 hours in the preceding 30 days",
         "CORRECT: [B]. The pilot must have completed at least 3 take-offs and landings as flying pilot on the same type/class or FSTD in the preceding 90 days."),
        ("Q4: Under what conditions may a pilot aged 62 act as pilot in commercial air transport?",
         "[A] In single-pilot operations only\n[B] As a member of a multi-pilot crew, provided the other pilot is under 60\n[C] Never, commercial operations stop at 60\n[D] Only during domestic daytime flights",
         "CORRECT: [B]. Between ages 60 and 64, commercial air transport is permitted only in a multi-pilot crew where the other pilot is under age 60."),
        ("Q5: What is the revalidation requirement by experience for a Single-Engine Piston (SEP) class rating?",
         "[A] 10 hours flight time in the preceding 6 months\n[B] 12 hours flight time including 6 hours PIC, 12 take-offs/landings, and 1 hour with an FI within the preceding 12 months\n[C] Passing a theoretical examination every 2 years\n[D] 3 take-offs and landings within the preceding 90 days",
         "CORRECT: [B]. SEP revalidation by experience requires 12 hours (6 PIC, 12 take-offs/landings, 1 hour training flight with FI) within the 12 months preceding expiry.")
    ]
    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 4 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 5: RULES OF THE AIR (SERA, VMC, SIGNALS & INTERCEPTION) (~6 pages)
# ==============================================================================
def build_ch05():
    pdf_path = os.path.join(BASE_DIR, "010_ch05_rules_of_the_air.pdf")
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
        "Navigation lights must be displayed from SUNSET TO SUNRISE (and any other period prescribed by authority):\n"
        "• Port Wing Light: RED light showing an unbroken arc of 110° from dead ahead to port.\n"
        "• Starboard Wing Light: GREEN light showing an unbroken arc of 110° from dead ahead to starboard.\n"
        "• Tail Light: WHITE light showing an unbroken arc of 140° visible aft.\n"
        "• Anti-Collision Lights: Flashing red or white light displayed by day and night to indicate operating engines.",
        max_chars=92
    )

    pdf.add_heading_1("7. ATC Light Gun Signals (Tower to Aircraft)")
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

    pdf.add_heading_1("9. Marshalling Signals (Annex 2 / SERA.3301)")
    marsh_data = [
        ["Wingman / Identify Gate", "Raise right arm fully vertical, wand pointing up; left wand pointed horizontally toward gate."],
        ["Straight Ahead", "Bend arms repeatedly upward and backward from elbows with wands pointing up."],
        ["Turn Left", "Point left arm and wand down; move right arm repeatedly upward/backward."],
        ["Turn Right", "Point right arm and wand down; move left arm repeatedly upward/backward."],
        ["Normal Stop", "Cross arms and wands overhead rapidly with wands crossed."],
        ["Emergency Stop", "Abruptly cross arms overhead and wave wands vigorously side to side."],
        ["Insert Chocks", "Arms extended palms inwards; swing arms from outwards to cross below waist."],
        ["Cut Engines", "Extend arm with wand at throat level; draw wand across throat in slicing motion."]
    ]
    pdf.add_table(["Signal Action", "Marshaller Visual Description & Crew Action"], marsh_data, col_widths=[140.0, 370.0])

    pdf.add_heading_1("10. Interception Procedures (Annex 2 / SERA)")
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

    pdf.add_heading_1("11. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: What does a flashing red light from the aerodrome control tower indicate to an aircraft in flight?",
         "[A] Cleared to land\n[B] Aerodrome unsafe, DO NOT LAND\n[C] Give way to other aircraft and continue circling\n[D] Return for landing",
         "CORRECT: [B]. Flashing red in flight means aerodrome unsafe, do not land (steady red means give way and continue circling)."),
        ("Q2: In Class G airspace at 2,000 ft AMSL, what are the VMC minima for an aeroplane flying at 130 kt IAS?",
         "[A] 8 km visibility and 1,500 m horizontal from clouds\n[B] 5 km visibility, 1,500 m horizontal, 1,000 ft vertical\n[C] 1,500 m visibility, clear of clouds and in sight of the surface\n[D] Special VFR clearance required",
         "CORRECT: [C]. At or below 3,000 ft AMSL (or 1,000 ft AGL) in Class F/G, VMC visibility is 5 km, but may be reduced to 1,500 m if speed is <= 140 kt, clear of clouds and surface in sight."),
        ("Q3: What visual aerodrome signal indicates that landings are prohibited?",
         "[A] A red square with a single yellow diagonal\n[B] A red square with two yellow diagonals\n[C] A white dumb-bell\n[D] A landing T",
         "CORRECT: [B]. A red square with yellow cross diagonals signifies that landings are prohibited and prohibition is likely prolonged."),
        ("Q4: Two power-driven aircraft are converging at approximately the same altitude. Which aircraft has the right of way?",
         "[A] The faster aircraft\n[B] The aircraft that has the other on its right\n[C] The aircraft that has the other on its left\n[D] The heavier aircraft",
         "CORRECT: [C]. The aircraft which has the other on its right shall give way; therefore, the aircraft that has the other on its left has right of way."),
        ("Q5: What are the minimum weather conditions for a Special VFR flight in a CTR?",
         "[A] Ground visibility >= 1,500 m, ceiling >= 600 ft, clear of clouds, ground in sight\n[B] Visibility >= 5 km, clear of clouds\n[C] Visibility >= 800 m and ceiling >= 1,000 ft\n[D] Any condition provided IFR traffic is absent",
         "CORRECT: [A]. Under SERA, Special VFR requires ground visibility >= 1,500 m (800 m helo) and cloud ceiling >= 600 ft.")
    ]
    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 5 compiled: {pdf_path}")

# ==============================================================================
# CHAPTER 6: INSTRUMENT DEPARTURES & NADP (~3 pages)
# ==============================================================================
def build_ch06():
    pdf_path = os.path.join(BASE_DIR, "010_ch06_departures.pdf")
    pdf = PDFBuilder("Air Law", "010", "Chapter 6: Instrument Departure Procedures")
    pdf.add_title_banner("Air Law", 6, "Instrument Departures (SID & NADP)", "157-172")

    pdf.add_heading_1("1. PANS-OPS Departure Design Gradients")
    pdf.add_paragraph(
        "Instrument departure procedures (ICAO Doc 8168 PANS-OPS) provide obstacle clearance from the end of the "
        "runway until the aircraft reaches the minimum en-route altitude (MEA). Design assumes all engines operating.",
        max_chars=92
    )

    pdf.add_callout(
        "definition",
        "Procedure Design Gradient (PDG) = 3.3%",
        "The standard PANS-OPS Procedure Design Gradient (PDG) is 3.3% (~200 ft/NM).\n"
        "It consists of:\n"
        "1. Obstacle Identification Surface (OIS): 2.5%\n"
        "2. Obstacle Clearance Margin: 0.8%\n"
        "-> Total Standard PDG = 3.3%. A steeper climb gradient is published ONLY if required by obstacles or airspace.",
        max_chars=86
    )

    pdf.add_heading_1("2. Straight vs Turning Departures")
    pdf.add_bullet("Screen Height at DER", "The departure procedure assumes the aircraft crosses the Departure End of Runway (DER) at a minimum screen height of 5 m (16 ft) with wings level.")
    pdf.add_bullet("Straight Departure", "Track does not diverge by more than 15° from runway centerline heading.")
    pdf.add_bullet("Turning Departure", "Specified whenever track requires a turn of MORE THAN 15°. No turn shall be initiated below 120 m (394 ft) above aerodrome elevation (or DER).")
    pdf.add_bullet("Turn Design Parameters", "Average bank angle: 15° (max 21°). Speed limits are specified per category.")

    pdf.add_heading_1("3. Noise Abatement Departure Procedures (NADP 1 vs NADP 2)")
    pdf.add_paragraph(
        "ICAO Annex 6 and PANS-OPS define two standardized noise abatement departure procedures for jet aeroplanes:",
        max_chars=92
    )

    nadp_data = [
        ["NADP 1 (Noise Close to Aerodrome)", "Climb at V2 + 10 to 20 kt with take-off flaps to 800 ft (or higher). At 800 ft to 3,000 ft, reduce to climb thrust, maintain climb speed with flaps intact. At 3,000 ft, accelerate and retract flaps."],
        ["NADP 2 (Noise Distant from Aerodrome)", "Climb at V2 + 10 to 20 kt to 800 ft. At 800 ft, accelerate while retracting flaps on schedule, then reduce to climb thrust. Continue climb to 3,000 ft."]
    ]
    pdf.add_table(["Procedure", "Climb Profile & Flap Retraction Schedule"], nadp_data, col_widths=[150.0, 360.0])

    pdf.add_heading_1("4. Omnidirectional Departures & Obstacle Clearances")
    pdf.add_paragraph(
        "Used when no specific SID route is published. The departure is divided into two distinct phases:\n"
        "• Phase 1: Aircraft climbs straight ahead on runway centerline to at least 120 m (394 ft) above aerodrome elevation.\n"
        "• Phase 2: Aircraft initiates turn towards the en-route track while maintaining at least 3.3% PDG.\n"
        "• Obstacle clearance: 90 m (295 ft) MOC provided throughout the turn area, increasing with distance from aerodrome.",
        max_chars=92
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: What is the standard Procedure Design Gradient (PDG) under PANS-OPS for instrument departures?",
         "[A] 2.5%\n[B] 3.3%\n[C] 5.0%\n[D] 6.5%",
         "CORRECT: [B]. The standard PDG is 3.3% (consisting of 2.5% Obstacle Identification Surface + 0.8% safety margin)."),
        ("Q2: What is the assumed screen height over the Departure End of Runway (DER)?",
         "[A] 0 m\n[B] 5 m (16 ft)\n[C] 10.7 m (35 ft)\n[D] 15 m (50 ft)",
         "CORRECT: [B]. PANS-OPS assumes 5 m (16 ft) screen height over DER (Note: CS-25 engine-out performance assumes 35 ft, but PANS-OPS obstacle assessment starts at 5 m)."),
        ("Q3: What is the minimum altitude above aerodrome elevation before a turn may be initiated on a turning departure?",
         "[A] 90 m (295 ft)\n[B] 120 m (394 ft)\n[C] 150 m (492 ft)\n[D] 300 m (984 ft)",
         "CORRECT: [B]. No turn shall be initiated below 120 m (394 ft) above the elevation of the aerodrome."),
        ("Q4: Which noise abatement departure procedure provides noise relief for areas close to the aerodrome?",
         "[A] NADP 1\n[B] NADP 2\n[C] Continuous Descent Departure\n[D] Balanced Field Take-off",
         "CORRECT: [A]. NADP 1 provides noise relief close to the airport by maintaining flaps and climbing steeply to 3,000 ft before accelerating."),
        ("Q5: What average bank angle is assumed in the design of turning departures under PANS-OPS?",
         "[A] 10°\n[B] 15° (maximum 21°)\n[C] 25°\n[D] 30°",
         "CORRECT: [B]. PANS-OPS departure design assumes an average bank angle of 15°, not to exceed 21°."),
        ("Q6: In an omnidirectional departure, what is the minimum height above aerodrome elevation before initiating a turn to en-route heading?",
         "[A] 90 m\n[B] 120 m (394 ft)\n[C] 150 m\n[D] 300 m",
         "CORRECT: [B]. In Phase 1 of an omnidirectional departure, the aircraft must climb straight ahead on runway heading to at least 120 m (394 ft) before beginning any turn."),
        ("Q7: Under what circumstances is a departure climb gradient steeper than the standard 3.3% published on a SID chart?",
         "[A] Always for jet aircraft operations\n[B] When dictated by obstacle clearance requirements or airspace restrictions\n[C] Only during summer high-temperature operations\n[D] Whenever the runway length is less than 2,000 m",
         "CORRECT: [B]. A gradient steeper than the standard 3.3% PDG is published only when required by obstacles in the climb path or by ATC airspace constraints.")
    ]
    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Deep Chapter 6 compiled: {pdf_path}")

if __name__ == "__main__":
    build_ch01()
    build_ch02()
    build_ch03()
    build_ch04()
    build_ch05()
    build_ch06()



