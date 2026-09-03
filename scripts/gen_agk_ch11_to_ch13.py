#!/usr/bin/env python3
"""
Generator for Subject 021: AGK - Airframe, Systems, Electrics & Powerplant
Volume 3: Chapters 11 to 13 (Electrics - DC & Batteries)
- Chapter 11: DC Principles, Components & Circuit Protection
- Chapter 12: Aircraft Batteries (Lead-Acid vs Nickel-Cadmium & Thermal Runaway)
- Chapter 13: Magnetism, DC Generation & Starter-Generators

Fully aligned with CAE Oxford Book 3 (Electrics and Electronics) and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant"

def build_agk_ch11():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch11_dc_principles_circuits.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 11: DC Principles & Circuits")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        11,
        "DC Principles, Components & Circuit Protection",
        "1-42 (Elec)"
    )

    pdf.add_heading_1("1. Fundamental DC Electrical Laws & Units")
    pdf.add_paragraph(
        "Direct Current (DC) flows continuously in one direction from positive to negative (conventional current flow) "
        "or negative to positive (electron flow). Aeronautical DC systems operate at a standard 28 Volts DC (nominal):"
    )
    pdf.add_bullet("Ohm's Law", "Voltage (V) = Current (I) x Resistance (R). Current is directly proportional to voltage and inversely proportional to resistance.")
    pdf.add_bullet("Electrical Power", "Power (P) = Voltage (V) x Current (I) = I^2 x R = V^2 / R. Measured in Watts (W) or Kilowatts (kW). 1 Horsepower (HP) = 746 Watts.")
    pdf.add_bullet("Kirchhoff's Current Law (KCL)", "The algebraic sum of currents entering and leaving any electrical node is zero (Total current in = Total current out).")
    pdf.add_bullet("Kirchhoff's Voltage Law (KVL)", "The directed sum of electrical potential differences (voltage) around any closed loop is zero.")
    pdf.add_bullet("Resistance Combinations", "Series: R_total = R1 + R2 + R3 (current identical through all, voltages add). Parallel: 1/R_total = 1/R1 + 1/R2 + 1/R3 (voltage identical across all, currents add; total resistance is always LESS than the smallest individual resistor).")

    pdf.add_heading_1("2. Circuit Protection: Fuses vs Circuit Breakers (Trip-Free)")
    pdf.add_paragraph(
        "Electrical conductors are sized according to current rating and allowable voltage drop. Circuit protection devices "
        "protect the WIRING against excessive current and fire, not the downstream consumer device:"
    )

    protection_table = [
        ["Thermal Circuit Breaker", "Bimetallic strip heats up under excessive current (I^2 x R), bends, and trips mechanical latch.", "Standard aircraft cockpit protection. Push-pull button with white indicator collar exposed when tripped."],
        ["Trip-Free Circuit Breaker", "Internal mechanism trips contacts open even if the pilot physically holds or tapes the button in!", "MANDATORY CS-25 requirement for flight deck circuit breakers. Prevents crew from overriding an active electrical short-circuit and setting fire to aircraft wiring!"],
        ["Resetting Policy (SOP)", "Commercial airline Standard Operating Procedures strictly regulate resetting tripped CBs.", "CRITICAL: Tripped CBs must NEVER be reset in flight unless deemed essential for safe continuation of flight (e.g. landing gear extension), and then ONCE ONLY after a 3-minute cooling period!"],
        ["Static Dischargers (Wicks)", "Conductive carbon fibers mounted at wingtips, elevator tips, and rudder trailing edge.", "Discharges accumulated electrostatic precipitation static (P-static) harmlessly into ambient slipstream at low current density, eliminating VHF/HF radio interference."]
    ]
    pdf.add_table(["Device", "Operating Principle", "Aeronautical Rule & Reset Philosophy"], protection_table, col_widths=[120.0, 190.0, 190.0])

    pdf.add_callout(
        "trap",
        "Trip-Free Circuit Breaker CS-25 Mandate",
        "- Definition: A 'Trip-Free' circuit breaker will open the circuit and trip even if the operating knob or lever is held mechanically in the 'ON' (pushed) position!\n"
        "- Reason: Guarantees that an electrical short circuit or severe wiring overheat cannot be forced to remain energized by a crew member holding the breaker in.",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch11 = [
        ("Q1: What is the primary purpose of a circuit breaker in an aircraft electrical distribution system?",
         "[A] To protect the electrical wiring against overheating and electrical fire caused by excessive current\n[B] To protect the generator against overvoltage\n[C] To convert AC to DC\n[D] To regulate bus voltage",
         "CORRECT: [A]. Circuit breakers are engineered and sized primarily to protect the aircraft wiring harness from drawing excessive current, overheating, and igniting an in-flight fire."),
        ("Q2: What is the defining characteristic of a 'trip-free' circuit breaker as mandated by CS-25 regulations?",
         "[A] It can be reset an unlimited number of times\n[B] It trips automatically under fault current even if the reset button is held depressed manually\n[C] It trips with zero time delay\n[D] It requires no physical reset",
         "CORRECT: [B]. A trip-free breaker has an internal linkage that will trip open regardless of whether the pilot holds the external button down, preventing forced overload of shorted wiring."),
        ("Q3: What happens to the total resistance of an electrical circuit when additional resistors are connected in PARALLEL?",
         "[A] Total resistance increases\n[B] Total resistance decreases and is always less than the lowest individual resistor value\n[C] Total resistance remains constant\n[D] Total resistance becomes zero",
         "CORRECT: [B]. In parallel circuits (1/R_tot = 1/R1 + 1/R2...), adding parallel pathways provides more routes for current to flow, which always reduces total overall resistance below that of any individual resistor.")
    ]

    for q_text, opts, exp in questions_ch11:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 11 compiled: {pdf_path}")


def build_agk_ch12():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch12_batteries_lead_acid_nicad.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 12: Batteries (Lead-Acid & Ni-Cad)")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        12,
        "Aircraft Batteries & Thermal Runaway",
        "43-68 (Elec)"
    )

    pdf.add_heading_1("1. Aircraft Battery Chemistries: Lead-Acid vs Nickel-Cadmium (Ni-Cad)")
    pdf.add_paragraph(
        "Aviation storage batteries supply emergency DC electrical power, APU/engine starting current, and stabilize DC bus voltage. "
        "Two incompatible electrochemical battery chemistries are used in transport aviation:"
    )

    batt_table = [
        ["Electrolyte", "Dilute Sulphuric Acid (H2SO4) in water (S.G. ~1.280 fully charged).", "Potassium Hydroxide (KOH) in water (~30% solution). DOES NOT CHANGE S.G. during charge/discharge!"],
        ["Cell Voltage", "2.0 Volts per cell nominal (12 cells in series = 24V battery).", "1.2 Volts per cell nominal (20 cells in series = 24V battery)."],
        ["Discharge Curve", "Voltage drops progressively and steadily throughout discharge.", "Maintains virtually FLAT constant voltage output until 90% discharged, then drops precipitously."],
        ["State of Charge Check", "Measured accurately using a hydrometer to check electrolyte Specific Gravity (S.G. drops as battery discharges).", "CANNOT be checked by hydrometer or voltage! (KOH is only a catalytic medium; voltage remains constant). Must undergo controlled workshop discharge test."],
        ["Cold Weather Performance", "Discharged battery can freeze at -10°C (electrolyte becomes pure water).", "Superior cold-weather starting performance; electrolyte freezing point is -60°C."]
    ]
    pdf.add_table(["Feature", "Lead-Acid Battery", "Nickel-Cadmium (Ni-Cad) Battery"], batt_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_callout(
        "trap",
        "Thermal Runaway in Nickel-Cadmium (Ni-Cad) Batteries",
        "- Mechanism: Ni-Cad batteries have a NEGATIVE TEMPERATURE COEFFICIENT OF RESISTANCE! As battery temperature rises, internal electrical resistance DECREASES.\n"
        "- The Vicious Cycle: At constant-voltage charging, lower resistance draws HIGHER charging current -> generates MORE heat -> resistance drops further -> draws even MORE current -> violently boils electrolyte, releases explosive hydrogen gas, and causes violent battery explosion/fire!\n"
        "- Protection: Ni-Cad battery compartments MUST be equipped with battery temperature sensors and thermal cut-off switches!",
        max_chars=86
    )

    pdf.add_heading_1("2. Battery Capacity & Emergency Standby Duration")
    pdf.add_paragraph(
        "Battery capacity is rated in Ampere-Hours (Ah). A 40 Ah battery can theoretically supply 40 Amperes for 1 hour, or 4 Amperes for 10 hours:"
    )
    pdf.add_bullet("CS-25 Emergency Duration", "In the event of complete primary electrical power generation failure (dual generator loss), aircraft emergency batteries MUST supply essential flight deck instruments, emergency lighting, and VHF comms for AT LEAST 30 MINUTES.")
    pdf.add_bullet("Separation of Maintenance Shops", "Lead-acid and Ni-Cad batteries must be serviced in COMPLETELY SEPARATE battery servicing rooms. Acid fumes from lead-acid neutralize alkaline KOH electrolyte in Ni-Cad cells, destroying both batteries!")

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch12 = [
        ("Q1: What is the fundamental electro-chemical mechanism that triggers thermal runaway in an aircraft Nickel-Cadmium (Ni-Cad) battery?",
         "[A] High internal resistance at freezing temperatures\n[B] A negative temperature coefficient of resistance, where increasing internal temperature causes internal resistance to drop, drawing exponentially higher charging current under constant voltage\n[C] Acid vaporization\n[D] Over-dilution of sulfuric acid",
         "CORRECT: [B]. Ni-Cad cells have a negative temperature coefficient. As they heat up, internal resistance drops, causing the battery to draw more current from the constant-voltage bus, producing more heat in an uncontrollable thermal runaway cycle."),
        ("Q2: How can the state of charge of an aircraft lead-acid battery be determined accurately in a maintenance facility?",
         "[A] By measuring the specific gravity of the electrolyte with a hydrometer\n[B] By shaking the battery\n[C] By weighing the battery plates\n[D] By checking battery temperature",
         "CORRECT: [A]. As a lead-acid battery discharges, sulfuric acid is consumed to form lead sulfate and water, dropping electrolyte specific gravity from 1.280 to 1.150. S.G. directly indicates state of charge."),
        ("Q3: Under CS-25 certification requirements, for what minimum time period must emergency aircraft batteries supply essential flight and navigation systems following total generator loss?",
         "[A] 10 minutes\n[B] 15 minutes\n[C] 30 minutes\n[D] 60 minutes",
         "CORRECT: [C]. Transport category aircraft batteries must provide at least 30 minutes of emergency power to essential flight instruments, standby attitude indicator, and communication equipment.")
    ]

    for q_text, opts, exp in questions_ch12:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 12 compiled: {pdf_path}")


def build_agk_ch13():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch13_magnetism_dc_generation.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 13: Magnetism & DC Generation")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        13,
        "Magnetism, DC Generation & Starter-Generators",
        "69-96 (Elec)"
    )

    pdf.add_heading_1("1. Electromagnetic Induction & DC Generator Principles")
    pdf.add_paragraph(
        "Electrical generation is based on Faraday's Law of Electromagnetic Induction: when an electrical conductor cuts magnetic lines of flux, "
        "an Electromotive Force (EMF / Voltage) is induced in the conductor:"
    )
    pdf.add_bullet("Fleming's Right-Hand Rule (Generators)", "Thumb = Motion of conductor; First finger = Magnetic Field (North to South); Second finger = Induced Current direction.")
    pdf.add_bullet("Fundamental AC Generation in Armature", "ALL rotating generators fundamentally produce ALTERNATING CURRENT (AC) inside the spinning armature coils as the wire alternates cutting north and south magnetic poles!")
    pdf.add_bullet("The Commutator (Mechanical Rectifier)", "In a DC generator, the rotating armature is connected to a split copper cylinder called a COMMUTATOR. Stationary carbon brushes ride on the commutator segments, mechanically switching connections at the exact instant induced voltage reverses, outputting pulsing DIRECT CURRENT (DC) to the busbar.")

    pdf.add_heading_1("2. DC Voltage Regulation & Shunt Generators")
    pdf.add_paragraph(
        "Aircraft DC generators are self-exciting shunt generators (field coils connected in parallel with the armature). "
        "Generated EMF is proportional to: 1. Magnetic field strength (flux); 2. Rotational speed (RPM); 3. Number of armature conductor turns:"
    )
    pdf.add_bullet("Voltage Control Mechanism", "Because engine RPM varies widely across flight regimes (idle to take-off), generator output voltage MUST BE REGULATED by controlling FIELD CURRENT in the stationary field windings.")
    pdf.add_bullet("Carbon Pile Voltage Regulator", "Contains a stack of carbon discs in series with the field winding. An electromagnet sensing bus voltage compresses or releases spring pressure on the carbon stack. Higher voltage -> electromagnet pulls against spring -> decompresses carbon discs -> stack resistance increases -> field current drops -> generator voltage drops back to 28V.")
    pdf.add_bullet("Reverse Current Circuit Breaker (RCCB)", "Prevents the battery from discharging backward into the generator when engine RPM drops below generator cut-in speed (motoring the generator). Disconnects generator automatically if current reverses.")

    pdf.add_callout(
        "trap",
        "Starter-Generator Operating Modes in Turboprops",
        "- Twin-role machine: Acts as a powerful DC electric motor during engine start, then switches automatically to become a 28V DC generator once engine accelerates past self-sustaining starter cut-out speed!\n"
        "- During Start: Series field windings engaged for maximum high-torque starting power.\n"
        "- During Generation: Switches to shunt field windings with voltage regulator active to supply steady 28V DC.",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch13 = [
        ("Q1: What is the primary operational function of the commutator in a DC aircraft generator?",
         "[A] To increase rotational speed\n[B] To act as a mechanical rotary rectifier, converting the alternating current (AC) naturally produced in the armature into direct current (DC)\n[C] To regulate system voltage\n[D] To insulate the brushes",
         "CORRECT: [B]. All rotating armatures induce AC. The commutator is a split copper ring that mechanically reverses contact polarity twice per revolution, rectifying AC into pulsating DC."),
        ("Q2: How is the output voltage of an aircraft DC generator regulated as engine RPM changes in flight?",
         "[A] By altering the number of windings on the armature\n[B] By varying the strength of the magnetic field current\n[C] By moving the carbon brushes mechanically\n[D] By changing battery electrolyte levels",
         "CORRECT: [B]. Output voltage = k x Flux x RPM. Because RPM varies with engine throttle, the voltage regulator modulates the current flowing through the shunt field coils to keep bus voltage constant at 28V."),
        ("Q3: What device prevents an aircraft battery from discharging back into a DC generator when engine RPM drops below idle cut-in speed?",
         "[A] A carbon pile\n[B] A Reverse Current Circuit Breaker (RCCB) or reverse current diode\n[C] A static inverter\n[D] A transformer rectifier unit",
         "CORRECT: [B]. If generator voltage drops below battery voltage, current would reverse and try to drive the generator as an electric motor. The RCCB detects reverse current flow and instantly opens the contactor.")
    ]

    for q_text, opts, exp in questions_ch13:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 13 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_agk_ch11()
    build_agk_ch12()
    build_agk_ch13()
