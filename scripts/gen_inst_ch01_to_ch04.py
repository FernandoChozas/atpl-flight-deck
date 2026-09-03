#!/usr/bin/env python3
"""
Generator for Subject 022: AGK - Instrumentation
Volume 1: Chapters 01 to 04 (Air Data & Pressure Instruments)
- Chapter 01: Pitot-Static Systems & Temperature Measurement
- Chapter 02: Pressure Altimeters & Vertical Speed Indicators (VSI/IVSI)
- Chapter 03: Airspeed Indicators & Machmeter
- Chapter 04: Air Data Computers (ADC) & ADIRU

Fully aligned with CAE Oxford Book 5 (Instrumentation) and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/022_instrumentation"

def build_inst_ch01():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch01_pitot_static_temperature.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 1: Pitot-Static & Temp")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        1,
        "Pitot-Static Systems & Temperature Measurement",
        "1-38"
    )

    pdf.add_heading_1("1. Pressure Sourcing: Pitot Pressure & Static Pressure")
    pdf.add_paragraph(
        "Aeronautical pressure instruments (Altimeter, ASI, VSI, Machmeter) rely on samples of atmospheric ambient pressure "
        "and impact pressure captured through dedicated external fuselage sensors:"
    )
    pdf.add_bullet("Static Pressure (P_s)", "The ambient barometric pressure of undisturbed still air at the aircraft's flight level. Sampled via flush static vents mounted on opposite sides of the fuselage (plumbing joined in a balance pipe to cancel yaw/sideslip errors).")
    pdf.add_bullet("Pitot Pressure (P_t / Total Pressure)", "The total stagnation pressure captured by open-ended, forward-facing pitot probes aligned parallel to the longitudinal axis: Total Pressure (P_t) = Static Pressure (P_s) + Dynamic Pressure (q).")
    pdf.add_bullet("Dynamic Pressure (q)", "Pressure resulting from aircraft forward velocity: q = 1/2 rho V^2. Pitot pressure alone cannot measure airspeed; the static pressure must be subtracted (P_t - P_s = q)!")
    pdf.add_bullet("Alternate Static Source", "Located inside unpressurized flight deck or avionics bay. Due to airflow venturi suction around the fuselage, pressure inside the cabin is LOWER than ambient outside static pressure! Selecting alternate static causes: Altimeter reads HIGH, ASI reads HIGH, VSI shows momentary climb then stabilizes.")

    pdf.add_heading_1("2. Pitot-Static Errors & Sensor Heating")
    pdf.add_paragraph(
        "Measurement errors distort raw pressure readings before reaching instrument capsules:"
    )

    error_table = [
        ["Instrument Error", "Mechanical imperfections, capsule hysteresis, and friction in gear linkages.", "Calibrated during factory manufacturing; negligible in modern digital ADC air data sensors."],
        ["Position / Pressure Error", "Airflow around fuselage disturbs ambient static pressure at the vent.", "Varies with Angle of Attack and airspeed/flaps. Sensed by ADC and corrected electronically via lookup tables."],
        ["Maneuver / Lag Error", "Time delay as pressure transmits through long pneumatic tubing.", "Eliminated in digital aircraft by mounting ADMs (Air Data Modules) right beside the pitot/static probes."],
        ["Electrical Heating", "MANDATORY electrical resistive heating elements inside pitot probes and static plates.", "Prevents ice blockage. Toggled on automatically on engine start or flight crew checklist. Inoperative probe heater risks catastrophic instrument misreadings!"]
    ]
    pdf.add_table(["Error Source", "Physical Mechanism & Flight Effect", "Correction & Operational Mitigation"], error_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_callout(
        "trap",
        "Alternate Static Source Selection Flight Deck Effects",
        "When the alternate static valve is opened on unpressurized aircraft:\n"
        "- Cabin static pressure is LOWER than true ambient atmospheric pressure (fuselage Bernoulli suction).\n"
        "- Altimeter: Reads HIGHER than actual altitude!\n"
        "- Airspeed Indicator (ASI): Reads HIGHER than actual airspeed!\n"
        "- Vertical Speed Indicator (VSI): Shows a MOMENTARY FALSE CLIMB, then returns to indicate true rate of climb/descent!",
        max_chars=86
    )

    pdf.add_heading_1("3. Air Temperature Measurement: SAT, TAT & Ram Rise")
    pdf.add_paragraph(
        "Accurate outside temperature is essential for True Airspeed (TAS) computation, Mach number calculation, and icing detection:"
    )
    pdf.add_bullet("Static Air Temperature (SAT / OAT)", "The true ambient temperature of undisturbed outside air through which the aircraft is flying.")
    pdf.add_bullet("Total Air Temperature (TAT)", "The temperature measured by a stagnation probe (Rosemount probe) exposed to the airstream. Due to adiabatic kinetic compression and boundary layer friction, air is brought to rest at the probe sensor, generating kinetic heating ('Ram Rise'): TAT = SAT + Ram Rise.")
    pdf.add_bullet("Ram Rise Formula", "Ram Rise = (V_TAS / 100)^2, or thermodynamically: TAT = SAT x (1 + 0.2 x K_r x M^2), where temperatures are in Kelvin (K = °C + 273), M = Mach number, and K_r = probe recovery factor (~1.0 for flight test).")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: In an unpressurized aircraft, what occurs to the primary flight instruments if the pilot selects the alternate static source inside the cockpit?",
         "[A] Altimeter reads low, ASI reads low, VSI shows momentary descent\n[B] Altimeter reads HIGH, ASI reads HIGH, and VSI shows a momentary false CLIMB\n[C] All instruments read zero\n[D] Only the Machmeter is affected",
         "CORRECT: [B]. Airflow over the fuselage creates suction inside the cockpit, making cockpit pressure lower than outside static. Lower static pressure causes the altimeter to indicate higher, the ASI differential to indicate faster, and the VSI to sense a momentary climb."),
        ("Q2: An aircraft is cruising at Mach 0.80 with a Static Air Temperature (SAT) of -50°C. What is the approximate Total Air Temperature (TAT) sensed by the aircraft temp probe (assume recovery factor Kr = 1.0)?",
         "[A] -70°C\n[B] -50°C\n[C] -21°C\n[D] 0°C",
         "CORRECT: [C]. Formula: TAT (K) = SAT (K) x (1 + 0.2 x M^2). Convert SAT: -50°C + 273 = 223 K. Factor: 1 + 0.2 x (0.80)^2 = 1 + 0.2 x 0.64 = 1.128. TAT = 223 x 1.128 = 251.5 K. Convert back to Celsius: 251.5 - 273 = -21.5°C (~ -21°C)."),
        ("Q3: Which flight instruments require a pneumatic connection to the PITOT pressure line?",
         "[A] Altimeter and VSI only\n[B] Airspeed Indicator (ASI) and Machmeter only\n[C] Altimeter, ASI and VSI\n[D] Turn coordinator and artificial horizon",
         "CORRECT: [B]. Only the Airspeed Indicator and the Machmeter require pitot (total) pressure to measure dynamic pressure. The Altimeter and VSI connect exclusively to the static pressure line.")
    ]

    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 1 compiled: {pdf_path}")


def build_inst_ch02():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch02_altimeter_vsi.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 2: Altimeter & VSI")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        2,
        "Pressure Altimeters & Vertical Speed Indicators",
        "39-78"
    )

    pdf.add_heading_1("1. Pressure Altimeter Mechanics & Pressure Datums")
    pdf.add_paragraph(
        "The pressure altimeter is an absolute pressure gauge calibrated to the ICAO Standard Atmosphere (ISA: MSL pressure 1013.25 hPa, "
        "temperature +15°C, lapse rate 1.98°C / 6.5°C per 1,000 m up to 36,090 ft):"
    )
    pdf.add_bullet("Internal Mechanism", "Contains an EVACUATED aneroid capsule (sealed with internal near-perfect vacuum). Ambient static pressure enters the instrument case. As aircraft climbs, static pressure drops; the capsule expands under internal leaf-spring tension, rotating pointer needles via jewel-pivoted magnifying gears.")
    pdf.add_bullet("QNH (Nautical Height)", "Altimeter subscale set to station barometric pressure adjusted to MSL using ISA temperature lapse. Reads aerodrome elevation when on the ground; indicates ALTITUDE above mean sea level in flight.")
    pdf.add_bullet("QFE (Field Elevation)", "Subscale set to actual atmospheric pressure at aerodrome reference point. Reads ZERO on ground; indicates HEIGHT above airfield runway.")
    pdf.add_bullet("Standard Setting (1013.25 hPa / 29.92 inHg)", "Set when climbing through the Transition Altitude (TA). Altimeter indicates FLIGHT LEVEL (FL). Standardizes vertical separation between all cruising traffic worldwide.")

    pdf.add_heading_1("2. Altimeter Temperature & Pressure Errors")
    alt_table = [
        ["Error Type", "Atmospheric Deviation Phenomenon", "Mathematical Rule & Rule of Thumb"],
        ["Pressure Error", "Flying from high pressure into low pressure without updating QNH subscale.", "True altitude is LOWER than indicated altitude! For every 1 hPa error: altimeter misreads by approximately 27 to 30 FEET (Rule: 1 hPa = 30 ft at sea level)."],
        ["Temperature Error", "Flying in air colder or warmer than standard ISA (+15°C at MSL, -2°C/1,000 ft).", "Rule of Thumb: 4 ft per 1,000 ft of altitude for each 1°C of ISA deviation. Cold Air: True altitude is LOWER than indicated! Hot Air: True altitude is HIGHER than indicated!"]
    ]
    pdf.add_table(["Error Type", "Atmospheric Deviation Phenomenon", "Mathematical Rule & Rule of Thumb"], alt_table, col_widths=[105.0, 195.0, 200.0])

    pdf.add_callout(
        "trap",
        "Universal Altimeter Error Mnemonic",
        "'HIGH TO LOW OR HOT TO COLD, LOOK OUT BELOW!'\n"
        "- When flying from high pressure to low pressure, or from warm air to cold air:\n"
        "- THE ALTIMETER READS ERRONEOUSLY HIGH! (You are dangerously closer to the ground/mountain peaks than the instrument indicates)!\n"
        "- In sub-zero winter temperatures, published IFR approach MDA/DA and minimum sector altitudes MUST be corrected using cold temperature correction tables!",
        max_chars=86
    )

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Altimeter Temperature Error and True Altitude",
        "SCENARIO (AviationExam Classic Cold Weather Altimetry Drill):\n"
        "An aircraft is cruising at FL 100 with an indicated altitude of 10,000 ft on 1013.25 hPa:\n"
        "- The outside air temperature (OAT / SAT) is -25°C\n"
        "- The route passes over high mountain peaks with minimum clearance required\n"
        "QUESTION: Calculate the True Altitude of the aircraft, and assess the terrain clearance hazard.\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Determine Standard ISA Temperature at 10,000 ft:\n"
        "  - ISA Sea Level Temp = +15°C\n"
        "  - ISA Lapse Rate = 2°C per 1,000 ft\n"
        "  - ISA Temp at 10,000 ft = +15°C - (2°C x 10) = +15°C - 20°C = -5°C.\n\n"
        "Step 2: Calculate the ISA Temperature Deviation (Delta-ISA):\n"
        "  - Actual Temp = -25°C\n"
        "  - Delta-ISA = Actual - Standard = -25°C - (-5°C) = -20°C (Air is 20°C colder than standard ISA!).\n\n"
        "Step 3: Apply the 4 ft per 1,000 ft Rule of Thumb:\n"
        "  - Formula: Temperature Correction = 4 ft x (Altitude / 1,000) x Delta-ISA\n"
        "  - Correction = 4 x 10 x (-20) = -800 feet!\n\n"
        "Step 4: Calculate True Altitude:\n"
        "  - True Altitude = Indicated Altitude + Correction\n"
        "  - True Altitude = 10,000 ft - 800 ft = 9,200 ft!\n\n"
        "FINAL ANSWER: True Altitude is 9,200 ft. The aircraft is 800 ft lower than what the altimeter displays ('High to low, hot to cold, look out below!').",
        max_chars=86
    )

    pdf.add_heading_1("4. Vertical Speed Indicators: VSI vs Instantaneous VSI (IVSI)")
    pdf.add_paragraph(
        "The Vertical Speed Indicator measures the rate of change of static pressure, indicating rate of climb or descent in feet per minute (fpm):"
    )
    pdf.add_bullet("Conventional VSI Mechanism", "Contains a flexible diaphragm capsule fed directly with static pressure. The surrounding sealed case is fed through a calibrated capillary metering leak tube. In level flight, pressures equalize (0 fpm). In a climb, capsule pressure drops instantly while case pressure leaks slowly through the capillary, creating a differential pressure that deflects the needle.")
    pdf.add_bullet("VSI Time Lag (6 to 9 Seconds)", "Because air takes several seconds to choke through the capillary leak, conventional VSIs suffer a 6 to 9 second lag before indicating a steady-state rate of climb/descent!")
    pdf.add_bullet("Instantaneous VSI (IVSI)", "Eliminates time lag by incorporating inertia dashpot pistons (accelerometer pumps). When the aircraft enters a pitch change, inertial mass of the piston pumps instantaneous differential pressure into the capsule, giving ZERO-LAG vertical speed indication!")

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: An aircraft is flying at FL 100 with an indicated altitude of 10,000 ft on 1013 hPa. Outside Air Temperature (OAT) is -25°C. What is the true altitude (approximate)?",
         "[A] 10,000 ft\n[B] 10,800 ft\n[C] 9,200 ft\n[D] 8,500 ft\n",
         "CORRECT: [C]. Standard ISA temp at 10,000 ft = 15 - (2 x 10) = -5°C. Actual temp = -25°C -> ISA deviation = -20°C (COLD AIR). Correction formula: 4 ft x (Alt / 1,000) x Delta-ISA = 4 x 10 x (-20) = -800 ft. True Altitude = 10,000 - 800 = 9,200 ft!"),
        ("Q2: What is the primary operational advantage of an Instantaneous Vertical Speed Indicator (IVSI) over a conventional VSI?",
         "[A] It requires no static pressure connection\n[B] It eliminates the 6 to 9 second time lag by using inertia-activated dashpot accelerometer pistons\n[C] It indicates airspeed during cruise\n[D] It operates on 28V DC power",
         "CORRECT: [B]. Conventional VSIs suffer a 6-9 second pneumatic metering lag. An IVSI uses acceleration dashpot pistons that pump immediate differential pressure into the capsule during maneuvers, providing instant response."),
        ("Q3: What will the pressure altimeter indicate on the runway before take-off if the subscale is set to the aerodrome QFE?",
         "[A] The aerodrome elevation above MSL\n[B] Exactly ZERO feet\n[C] Standard flight level zero\n[D] Pressure altitude",
         "CORRECT: [B]. QFE is station barometric pressure at the runway reference point. Setting QFE references the altimeter to field height, reading exactly 0 ft on the runway threshold.")
    ]

    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 2 compiled: {pdf_path}")


def build_inst_ch03():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch03_asi_machmeter.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 3: ASI & Machmeter")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        3,
        "Airspeed Indicators & The Machmeter",
        "79-118"
    )

    pdf.add_heading_1("1. Airspeed Indicator (ASI) Principles & Airspeed Hierarchy")
    pdf.add_paragraph(
        "The Airspeed Indicator measures dynamic pressure (q = 1/2 rho V^2). Pitot pressure feeds the inside of an expandable metal capsule, "
        "while static pressure feeds the sealed instrument case: Differential Pressure = P_pitot - P_static = Dynamic Pressure (q):"
    )
    pdf.add_bullet("Indicated Airspeed (IAS)", "The raw airspeed reading displayed on the cockpit ASI dial or PFD speed tape, uncorrected for errors.")
    pdf.add_bullet("Calibrated Airspeed (CAS / RAS)", "IAS corrected for instrument errors and position / pressure errors (static vent aerodynamic disturbance). CAS is equal to EAS at low sub-transonic airspeeds at sea level.")
    pdf.add_bullet("Equivalent Airspeed (EAS)", "CAS corrected for atmospheric compressibility effects. Crucial at high speeds and altitudes (> 250 kt / > 10,000 ft) where compressed air molecules generate false excess dynamic pressure: EAS = CAS - Compressibility Correction.")
    pdf.add_bullet("True Airspeed (TAS)", "The actual physical velocity of the aircraft relative to the surrounding air mass. Calculated by correcting EAS for actual ambient air density: TAS = EAS x sqrt(rho_0 / rho). TAS increases with altitude for a constant IAS (~1.5% to 2% increase per 1,000 ft)!")

    pdf.add_heading_1("2. ASI Color Coding Arcs (CS-23 / CS-25)")
    asi_table = [
        ["Color Arc / Line", "Speed Range Limits", "Aerodynamic Significance & Pilot Actions"],
        ["White Arc", "V_SO to V_FE", "Flap operating range. Lower limit is stall speed in landing configuration (V_SO); upper limit is maximum flap extended speed (V_FE)."],
        ["Green Arc", "V_S1 to V_NO", "Normal operating range. Lower limit is stall speed clean (V_S1); upper limit is Maximum Structural Cruising Speed (V_NO)."],
        ["Yellow Arc", "V_NO to V_NE", "Caution range. Maneuvers allowed in smooth air only; do not make abrupt control movements."],
        ["Red Radial Line", "V_NE (Never Exceed)", "Never Exceed speed. Exceeding risks catastrophic structural flutter and aerodynamic breakup!"]
    ]
    pdf.add_table(["Color Arc / Line", "Speed Range Limits", "Aerodynamic Significance & Pilot Actions"], asi_table, col_widths=[105.0, 150.0, 245.0])

    pdf.add_heading_1("3. The Machmeter: Mechanism & Operational Errors")
    pdf.add_paragraph(
        "Mach number is the ratio of True Airspeed (TAS) to the local speed of sound (a): M = TAS / a. "
        "Local speed of sound depends EXCLUSIVELY on absolute temperature: a = 38.94 x sqrt(T [Kelvin]):"
    )
    pdf.add_bullet("Machmeter Architecture", "Contains TWO separate capsules mechanically coupled via a floating sliding ratio divider arm: 1. Airspeed capsule (fed by pitot/static differential, sensing q); 2. Altimeter aneroid capsule (evacuated, sensing static ambient pressure P_s).")
    pdf.add_bullet("Aeronautical Ratio", "Because dynamic pressure q is proportional to P_s x M^2, the ratio of (P_t - P_s) / P_s depends ONLY ON MACH NUMBER! The altimeter capsule continuously modifies the pivot leverage of the airspeed capsule.")
    pdf.add_bullet("Zero Temperature / Density Error", "CRITICAL EXAM POINT: The Machmeter suffers NO DENSITY ERRORS and NO TEMPERATURE ERRORS! Temperature and density factors mathematically cancel out in the ratio of dynamic to static pressure. The Machmeter is subject ONLY to instrument error and position error!")

    pdf.add_callout(
        "trap",
        "Climbing / Descending at Constant Speed Scenarios",
        "- CLIMB at Constant IAS: TAS INCREASES (density drops); Mach number INCREASES (temperature drops)!\n"
        "- CLIMB at Constant Mach: TAS DECREASES (until tropopause, then constant); IAS DECREASES rapidly!\n"
        "- CROSSOVER ALTITUDE: The altitude where the aircraft transitions from climbing at constant IAS to climbing at constant Mach number (typically FL 280 to FL 310).",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: What errors affect a mechanical aircraft Machmeter?",
         "[A] Density error and temperature error\n[B] Instrument error and position (pressure) error ONLY\n[C] Compressibility error only\n[D] Lag error only",
         "CORRECT: [B]. The Machmeter measures the ratio of dynamic pressure to static pressure. Air density and temperature variables mathematically cancel out. Therefore, a Machmeter has NO density or temperature errors!"),
        ("Q2: As an aircraft climbs at a constant Indicated Airspeed (IAS) of 280 knots from sea level up to FL 280, what happens to True Airspeed (TAS) and Mach Number?",
         "[A] Both TAS and Mach number decrease\n[B] Both TAS and Mach number INCREASE\n[C] TAS increases while Mach number remains constant\n[D] TAS remains constant while Mach number increases",
         "CORRECT: [B]. As altitude increases, air density drops, so TAS must increase for the same dynamic pressure (IAS). Simultaneously, outside air temperature drops, lowering the local speed of sound; therefore, Mach number increases rapidly!"),
        ("Q3: What is the aerodynamic definition of Equivalent Airspeed (EAS)?",
         "[A] IAS corrected for density altitude\n[B] Calibrated Airspeed (CAS) corrected for compressibility effects\n[C] Groundspeed corrected for wind\n[D] True airspeed at the tropopause",
         "CORRECT: [B]. Equivalent Airspeed represents Calibrated Airspeed corrected for the adiabatic compressibility of air molecules at high forward speeds and high altitudes.")
    ]

    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 3 compiled: {pdf_path}")


def build_inst_ch04():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch04_air_data_computer_adiru.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 4: ADC & ADIRU")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        4,
        "Air Data Computers (ADC) & ADIRU Architecture",
        "119-148"
    )

    pdf.add_heading_1("1. Air Data Computer (ADC) Inputs & Computed Outputs")
    pdf.add_paragraph(
        "Modern glass-cockpit airliners replace individual mechanical instrument capsules with centralized digital Air Data Computers (ADC):"
    )

    adc_table = [
        ["Raw Sensor Inputs to ADC", "Pitot Pressure (P_t), Static Pressure (P_s), Total Air Temperature (TAT), Angle of Attack (Alpha)."],
        ["Primary Computed Outputs", "Pressure Altitude (1013.25 hPa), Baro-corrected Altitude (QNH/QFE), Calibrated Airspeed (CAS), True Airspeed (TAS), Mach Number, Static Air Temperature (SAT), Vertical Speed (VSI)."],
        ["Downstream Consumer Systems", "EFIS Primary Flight Displays, Autopilot (AFCS), Flight Management System (FMS), TCAS II, GPWS/EGPWS, FADEC engine controllers, and Transponder Mode S Altitude Reporting."]
    ]
    pdf.add_table(["ADC Functional Category", "Aeronautical Parameters & Connected Systems"], adc_table, col_widths=[160.0, 340.0])

    pdf.add_bullet("Electronic Position Error Correction (SSEC)", "The ADC automatically applies Static Source Error Corrections (SSEC) stored in digital calibration tables based on current Mach number, AOA, and flap position, achieving flawless altitude and speed precision.")

    pdf.add_heading_1("2. Air Data Inertial Reference Unit (ADIRU) Architecture")
    pdf.add_paragraph(
        "Modern commercial airliners (e.g. Airbus A320/A350/A380, Boeing 777/787) integrate the ADC and the Inertial Reference System (IRS) "
        "into a single unified line replaceable unit called an ADIRU:"
    )
    pdf.add_bullet("ADIRU Segregation", "Each ADIRU contains two distinct, fault-isolated parts: 1. The ADR (Air Data Reference) part, processing pitot/static/temp data; 2. The IR (Inertial Reference) part, processing laser gyro and accelerometer attitude/position data.")
    pdf.add_bullet("Triple Redundancy", "Transport category aircraft install three independent ADIRUs (ADIRU 1, ADIRU 2, ADIRU 3). ADIRU 1 supplies the Captain's PFD/ND; ADIRU 2 supplies the First Officer's PFD/ND; ADIRU 3 acts as a standby hot backup selectable via cockpit switching.")
    pdf.add_bullet("ADIRU Rotary Mode Selector", "OFF: Unit depowered; NAV: Normal operating mode (inertial navigation active); ATT: Attitude-only reversion mode (used if navigation position computation fails in flight; provides basic pitch, roll, and heading, but velocity/position navigation is lost!).")

    pdf.add_callout(
        "trap",
        "ADIRU Switching & In-Flight Reversion",
        "- If an ADR fault occurs: The pilot switches the Air Data selector to CAPT ON 3 or F/O ON 3.\n"
        "- If an IR fault occurs in flight: The pilot switches the mode selector to ATT (Attitude mode). The aircraft MUST be flown straight and level for 30 seconds to level the attitude platform. Entering magnetic heading manually via MCDU is mandatory in ATT mode!",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: Which of the following parameters is directly COMPUTED by an Air Data Computer (ADC) rather than sensed directly?",
         "[A] Pitot pressure\n[B] Total Air Temperature\n[C] True Airspeed (TAS) and Mach Number\n[D] Angle of attack",
         "CORRECT: [C]. Pitot pressure, static pressure, TAT, and AOA are raw physical inputs. True Airspeed, Mach number, and calibrated airspeed are mathematically computed by the ADC processors."),
        ("Q2: In an aircraft equipped with three ADIRUs, what capability remains if an Inertial Reference (IR) unit is switched to 'ATT' mode in flight?",
         "[A] Full LNAV and RNAV navigation\n[B] Pitch, roll attitude, and heading information ONLY (navigation capability is lost)\n[C] Autoland CAT III capability\n[D] TCAS resolution advisories",
         "CORRECT: [B]. The ATT (Attitude) mode is an emergency reversion. It retains basic gyro attitude (pitch/roll) and magnetic heading, but completely disables inertial position, groundspeed, and navigation tracking."),
        ("Q3: What is the operational purpose of Static Source Error Correction (SSEC) within an Air Data Computer?",
         "[A] To de-ice the pitot probe\n[B] To automatically compensate for aerodynamic position errors around the static vents across various Mach numbers and angles of attack\n[C] To calibrate cockpit compasses\n[D] To measure fuel density",
         "CORRECT: [B]. Static vents suffer position error caused by airflow pressure disturbances. The ADC applies SSEC algorithms to eliminate position error, ensuring highly accurate altitude and airspeed readouts.")
    ]

    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 4 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_inst_ch01()
    build_inst_ch02()
    build_inst_ch03()
    build_inst_ch04()
