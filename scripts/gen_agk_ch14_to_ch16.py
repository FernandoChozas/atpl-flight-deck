#!/usr/bin/env python3
"""
Generator for Subject 021: AGK - Airframe, Systems, Electrics & Powerplant
Volume 3: Chapters 14 to 16 (Electrics - AC, Distribution & Avionics Buses)
- Chapter 14: AC Generation, Alternators & CSD / IDG
- Chapter 15: AC Distribution, TRUs, Inverters & Bus Architecture
- Chapter 16: Semiconductors, Logic Gates & Aircraft Data Buses (ARINC 429)

Fully aligned with CAE Oxford Book 3 (Electrics and Electronics) and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant"

def build_agk_ch14():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch14_ac_generation_csd_idg.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 14: AC Generation & CSD/IDG")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        14,
        "AC Generation, Alternators & CSD / IDG",
        "97-138 (Elec)"
    )

    pdf.add_heading_1("1. Aeronautical AC Specifications: 115V / 200V at 400 Hz")
    pdf.add_paragraph(
        "Transport aircraft utilize 3-phase Alternating Current (AC) as the primary electrical generation medium due to dramatic weight savings "
        "and superior motor/transformer efficiency compared to DC systems:"
    )
    pdf.add_bullet("Voltage Specification", "Standard commercial aircraft AC power is 115 Volts RMS Phase-to-Neutral (Star configuration) and 200 Volts RMS Line-to-Line (Phase-to-Phase): V_line = sqrt(3) x V_phase = 1.732 x 115V = 200V.")
    pdf.add_bullet("Frequency Specification (400 Hz)", "Commercial aircraft operate at 400 Hertz (cycles per second), compared to 50/60 Hz domestic ground mains. High 400 Hz frequency allows transformers, alternators, and motors to be manufactured with dramatically smaller, lighter magnetic iron cores, saving tons of aircraft weight!")
    pdf.add_bullet("Frequency Formula", "Frequency (f) = (P x N) / 120, where P = number of magnetic poles and N = generator rotational speed in RPM. For an 8-pole generator to produce 400 Hz: N = (120 x 400) / 8 = 6,000 RPM (CONSTANT)!")

    pdf.add_heading_1("2. Modern Brushless AC Generator Architecture")
    pdf.add_paragraph(
        "High-altitude sparking and rapid carbon brush wear in thin air led to the universal adoption of brushless AC generators, "
        "housing three distinct electrical machines on a single rotating rotor shaft:"
    )

    brushless_table = [
        ["1. Pilot Exciter", "Permanent Magnet Rotor (spinning magnets).", "Permanent Magnet Generator (PMG) 3-phase stator. Induces AC voltage to power the Generator Control Unit (GCU) independently without battery power!"],
        ["2. Main Exciter", "3-phase AC armature winding feeding rotating rectifier diodes.", "DC Field Winding controlled by the GCU. GCU varies DC current to regulate main output voltage."],
        ["3. Rotating Rectifier", "Six silicon diodes mounted on the rotating shaft.", "Rectifies 3-phase AC from main exciter rotor into DC, directly feeding the main generator field WITHOUT BRUSHES!"],
        ["4. Main Generator", "Heavy DC magnetic field windings (poles).", "Main 3-phase Star-connected stator. Delivers primary 115V / 200V 400 Hz power to the main aircraft busbars."]
    ]
    pdf.add_table(["Stage", "Rotating Rotor Element", "Stationary Stator Element & Function"], brushless_table, col_widths=[100.0, 180.0, 220.0])

    pdf.add_heading_1("3. Constant Speed Drive (CSD) & Integrated Drive Generator (IDG)")
    pdf.add_paragraph(
        "Because jet engine accessory gearbox speed varies constantly (from ~4,500 to ~9,000 RPM), an intermediate hydromechanical transmission "
        "is mandatory to drive the generator at an EXACT, UNVARYING 6,000 RPM to maintain 400 Hz (+/- 1% / 396 to 404 Hz):"
    )
    pdf.add_bullet("Constant Speed Drive (CSD)", "A variable hydromechanical transmission (hydraulic pump and motor linked through a differential planetary gear train) that adds or subtracts speed to keep the output shaft locked at 6,000 RPM.")
    pdf.add_bullet("Integrated Drive Generator (IDG)", "The modern standard (e.g. A320, B737NG, B777). Integrates the CSD transmission and the brushless AC generator inside a single, common oil-cooled casing, saving weight and maintenance.")
    pdf.add_bullet("CSD / IDG In-Flight Disconnect", "If CSD oil temperature exceeds limits or oil pressure drops, a cockpit DISCONNECT switch fires an electro-mechanical solenoid that physically disengages a dog-clutch from the engine gearbox. CRITICAL EXAM POINT: Once disconnected in flight, the CSD / IDG CANNOT BE RECONNECTED IN FLIGHT! It can ONLY be reset manually by ground mechanics after landing!")

    pdf.add_callout(
        "trap",
        "CSD / IDG Disconnect Rules & Warnings",
        "- Cockpit Disconnect Switch: Protected by a red guarded cover. Activated when high oil temperature or low oil pressure is annunciated.\n"
        "- Thermal Disconnect: Many IDGs incorporate a eutectic solder plug that automatically disconnects the drive if case temperature exceeds ~180°C.\n"
        "- STRICT EXAM RULE: The CSD CANNOT be reconnected in flight under any circumstances!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch14 = [
        ("Q1: Why do commercial transport aircraft use an electrical AC frequency of 400 Hz instead of standard commercial 50 Hz or 60 Hz?",
         "[A] To prevent radio interference\n[B] Because 400 Hz allows transformers, motors, and magnetic components to be engineered with much smaller and lighter iron cores, saving substantial aircraft weight\n[C] Because 400 Hz does not cause electrical shocks\n[D] To improve generator brush life",
         "CORRECT: [B]. The size and weight of electromagnetic iron cores (in transformers, generators, and electric motors) is inversely proportional to frequency. 400 Hz allows miniature, lightweight components compared to bulky 50/60 Hz industrial equipment."),
        ("Q2: In a 3-phase 115V AC star-connected aircraft generator, what is the line-to-line (phase-to-phase) voltage?",
         "[A] 115 V\n[B] 200 V\n[C] 230 V\n[D] 345 V",
         "CORRECT: [B]. Line-to-line voltage is related to phase-to-neutral voltage by V_line = sqrt(3) x V_phase. Thus: 1.732 x 115V = 199.2 V (~200 Volts AC)."),
        ("Q3: Can an Integrated Drive Generator (IDG) that has been disconnected in flight by the pilot be reconnected before landing?",
         "[A] Yes, by pressing the IDG reset button on the overhead panel\n[B] Yes, once the oil cools below 100°C\n[C] No, mechanical reconnection is physically impossible in flight and can only be performed manually on the ground by maintenance personnel\n[D] Yes, by recycling the engine master switch",
         "CORRECT: [C]. The CSD/IDG disconnect separates a mechanical spring-loaded dog clutch. Once pulled out of mesh, it cannot be engaged while running and must be reset manually on the ground.")
    ]

    for q_text, opts, exp in questions_ch14:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 14 compiled: {pdf_path}")


def build_agk_ch15():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch15_ac_distribution_inverters.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 15: AC Distribution & TRUs/Inverters")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        15,
        "AC Distribution, TRUs, Inverters & Architecture",
        "139-166 (Elec)"
    )

    pdf.add_heading_1("1. Busbar Architectures: Split-Bus vs Parallel Systems")
    pdf.add_paragraph(
        "Commercial aircraft distribute electrical power through rigid copper or aluminum conductor rails called busbars (buses). "
        "Two distinct system philosophies govern AC generator connection:"
    )

    bus_table = [
        ["Split-Bus System (Isolated)", "Generators NEVER operate in parallel! Each AC generator powers its own independent AC busbar.", "Standard on twin-engine aircraft (A320, B737, B777, B787). If one generator fails, a Bus Tie Breaker (BTB) closes automatically so the remaining generator powers both sides. Paralleling is strictly prohibited!"],
        ["Parallel System", "All AC generators are synchronized in frequency, voltage, and phase angle, connected to a common tie busbar.", "Four-engine heavy transports (B747-400, older widebodies). Requires complex real (kW) and reactive (kVAR) load sharing circuitry in the GCU."]
    ]
    pdf.add_table(["Distribution System", "Operating Philosophy & Generator Connection", "Aircraft Examples & Nuances"], bus_table, col_widths=[110.0, 205.0, 185.0])

    pdf.add_heading_1("2. Power Conversion Units: TRUs & Static Inverters")
    pdf.add_paragraph(
        "Modern airliners carry both AC and DC equipment, requiring two-way electrical power conversion:"
    )
    pdf.add_bullet("Transformer Rectifier Unit (TRU)", "Converts primary 115V AC (400 Hz) into 28V DC (nominal) to power DC busbars, charge batteries, and supply DC avionics. Contains a step-down transformer and a 6-phase bridge silicon diode rectifier. Has NO MOVING PARTS and requires cooling airflow.")
    pdf.add_bullet("Static Inverter", "Converts 28V DC (from aircraft batteries or DC buses) into 115V AC (single-phase, 400 Hz) to power essential flight instruments (standby attitude indicator, flight controls, navigation radios) during complete AC generator failure.")

    pdf.add_callout(
        "trap",
        "TRU vs Inverter Conversion Direction Trap",
        "- TRU (Transformer Rectifier Unit): Converts AC -> DC (115V AC in -> 28V DC out)!\n"
        "- Static Inverter: Converts DC -> AC (28V DC in -> 115V AC out)!\n"
        "- Mnemonic: Inverter INVERTS the normal flow (takes battery DC and produces AC)!",
        max_chars=86
    )

    pdf.add_heading_1("3. Generator Control Unit (GCU) & Automatic Load Shedding")
    pdf.add_paragraph(
        "Each AC generator is supervised by an electronic Generator Control Unit (GCU) providing protection and switching:"
    )
    pdf.add_bullet("GCU Protective Trips", "Monitors for Overvoltage, Undervoltage, Overfrequency, Underfrequency, Feeder Fault (differential current between neutral and bus), and Reverse Power. If a fault occurs, the GCU opens the Generator Breaker (GB) and de-excites the generator field.")
    pdf.add_bullet("Automatic Load Shedding", "If an electrical generator is lost in flight, the remaining generator may exceed 100% rated capacity. The electrical system automatically sheds non-essential utility loads (galley ovens, cabin entertainment, passenger seat power, secondary water heaters) to preserve electrical power for flight instruments and safety systems!")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch15 = [
        ("Q1: What is the operational function of a Transformer Rectifier Unit (TRU) in an aircraft electrical system?",
         "[A] To convert 28V DC into 115V AC\n[B] To convert 115V AC into 28V DC\n[C] To regulate generator frequency at 400 Hz\n[D] To charge oxygen cylinders",
         "CORRECT: [B]. A TRU steps down 115V AC power and rectifies it through solid-state silicon diodes into 28V DC power for the aircraft's DC busbars."),
        ("Q2: In a twin-engine jet aircraft featuring a 'split-bus' electrical architecture, what prevents two AC generators from powering the same busbar simultaneously?",
         "[A] A reverse current relay\n[B] Interlocked Bus Tie Breakers (BTBs) that ensure generators operate completely isolated and never in parallel\n[C] Static inverters\n[D] Thermal fuses",
         "CORRECT: [B]. In split-bus systems, parallel connection is prohibited. Control logic interlocks ensure that when an external generator or second engine generator connects, the bus tie opens or isolates."),
        ("Q3: Following an in-flight generator failure on a commercial airliner, what occurs automatically during 'load shedding'?",
         "[A] Fuel is jettisoned from the wings\n[B] Non-essential electrical consumers (galley equipment, passenger entertainment) are disconnected automatically to prevent overloading the remaining generator\n[C] The APU shuts down\n[D] Flight controls switch to manual reversion",
         "CORRECT: [B]. Load shedding disconnects high-draw commercial utility loads (galleys) to guarantee sufficient capacity for essential flight guidance, instruments, and pumps.")
    ]

    for q_text, opts, exp in questions_ch15:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 15 compiled: {pdf_path}")


def build_agk_ch16():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch16_semiconductors_logic_buses.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 16: Logic Gates & Avionics Buses")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        16,
        "Semiconductors, Logic Gates & ARINC 429 Buses",
        "167-200 (Elec)"
    )

    pdf.add_heading_1("1. Solid-State Semiconductor Devices")
    pdf.add_paragraph(
        "Solid-state electronics form the core of aircraft digital control units (FADEC, FMS, Fly-by-Wire FCCs, EGPWS):"
    )
    pdf.add_bullet("PN Junction Diode", "Allows current to flow in one direction only (forward bias); blocks current in reverse. Used for rectification and reverse current protection.")
    pdf.add_bullet("Zener Diode", "Operates in reverse breakdown mode at an exact, predetermined voltage (Zener voltage). Used as high-precision VOLTAGE REGULATORS and voltage reference standards.")
    pdf.add_bullet("Transistors (BJT / MOSFET)", "Three-terminal semiconductor devices (Base, Collector, Emitter or Gate, Drain, Source). Used as electronic solid-state switches and amplifiers.")

    pdf.add_heading_1("2. Digital Logic Gates: Truth Tables & Aeronautical Logic")
    pdf.add_paragraph(
        "Flight control computers and warning systems utilize Boolean logic gates to evaluate flight parameters:"
    )

    logic_table = [
        ["AND Gate", "Output = A . B", "Output is HIGH (1) ONLY IF ALL inputs are HIGH (1). Example: Cabin altitude horn = Cabin Alt > 10,000 ft AND Aircraft Airborne."],
        ["OR Gate", "Output = A + B", "Output is HIGH (1) IF ANY input is HIGH (1). Example: Master Caution = Low Hyd Press OR Low Fuel Press OR Gen Trip."],
        ["NOT Gate (Inverter)", "Output = NOT A", "Output is the exact opposite of input (1 becomes 0; 0 becomes 1)."],
        ["NAND Gate", "Output = NOT (A . B)", "Output is LOW (0) ONLY if all inputs are HIGH (1). Inverted AND gate."],
        ["NOR Gate", "Output = NOT (A + B)", "Output is HIGH (1) ONLY if all inputs are LOW (0). Inverted OR gate."]
    ]
    pdf.add_table(["Gate Type", "Boolean Equation", "Output Condition & Aircraft System Application"], logic_table, col_widths=[90.0, 140.0, 270.0])

    pdf.add_heading_1("3. Avionics Digital Data Buses: ARINC 429 Standard")
    pdf.add_paragraph(
        "Modern avionics units (LRUs) communicate digitally over standardized serial data buses rather than individual heavy point-to-point analog wiring harnesses:"
    )
    pdf.add_bullet("ARINC 429 Architecture", "The universal commercial standard. It is a SIMPLEX (one-directional) data bus. Transmits data from one single transmitter to up to 20 receivers across a twisted shielded wire pair.")
    pdf.add_bullet("Word Structure (32 Bits)", "Every ARINC 429 transmission is an uncompressed 32-bit digital word: Bits 1-8: Label (identifies parameter, e.g. 203 = Pressure Altitude, 310 = Present Position Latitude); Bits 9-10: SDI (Source/Destination Identifier); Bits 11-29: Data Field (BCD or BNR numeric value); Bits 30-31: SSM (Sign/Status Matrix: Normal, Test, Failure Warning); Bit 32: Parity Bit (Odd parity standard to detect transmission errors).")
    pdf.add_bullet("Transmission Speeds", "Low-speed mode: 12.5 to 14.5 kbps; High-speed mode: 100 kbps.")
    pdf.add_bullet("Advanced Aircraft Buses", "Boeing 777 uses ARINC 629 (bidirectional, multi-transmitter); Airbus A380 / A350 and Boeing 787 use AFDX (Avionics Full-Duplex Switched Ethernet, 100 Mbps).")

    pdf.add_callout(
        "trap",
        "ARINC 429 Exam Traps Summary",
        "- Simplex Bus: Data flows in ONE DIRECTION ONLY! (Two-way communication requires two separate wire pairs).\n"
        "- Word Length: Exactly 32 bits!\n"
        "- Parity: Bit 32 is always ODD parity.\n"
        "- Physical Wire: Twisted shielded pair with 78-ohm characteristic impedance.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch16 = [
        ("Q1: What is the bit structure length of a standard ARINC 429 digital avionics data bus word?",
         "[A] 16 bits\n[B] 32 bits\n[C] 64 bits\n[D] 128 bits",
         "CORRECT: [B]. The standard ARINC 429 data word consists of exactly 32 bits, comprising an 8-bit label, 2-bit SDI, 19-bit data field, 2-bit SSM, and a 1-bit parity check."),
        ("Q2: Which type of semiconductor diode is specifically engineered to operate in reverse breakdown mode to provide a precise constant reference voltage?",
         "[A] Photodiode\n[B] Zener diode\n[C] Light Emitting Diode (LED)\n[D] Germanium power diode",
         "CORRECT: [B]. Zener diodes are designed to conduct in reverse once a specific breakdown voltage is reached, maintaining a stable reference voltage regardless of current variations."),
        ("Q3: How many transmitters can be connected to a single ARINC 429 digital data bus wire pair?",
         "[A] Only ONE transmitter (simplex operation)\n[B] Up to 20 transmitters\n[C] Unlimited transmitters\n[D] Exactly two transmitters in full-duplex",
         "CORRECT: [A]. ARINC 429 is strictly point-to-point or point-to-multipoint SIMPLEX: it permits ONLY ONE single transmitter per bus line, driving up to 20 listening receivers.")
    ]

    for q_text, opts, exp in questions_ch16:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 16 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_agk_ch14()
    build_agk_ch15()
    build_agk_ch16()
