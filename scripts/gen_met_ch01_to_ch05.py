#!/usr/bin/env python3
"""
Generator for Subject 050: Meteorology
Volume 1: Chapters 1 to 5
- Chapter 1: The Atmosphere: Structure, Composition, Vertical Extent & ISA
- Chapter 2: Atmospheric Pressure, Altimetry & Q-Codes (QNH, QFE, QNE)
- Chapter 3: Atmospheric Density, Temperature & Thermal Inversions
- Chapter 4: Moisture, Humidity, Adiabatic Processes & Atmospheric Stability
- Chapter 5: Wind Dynamics, Global Circulation, Coriolis & Local Wind Systems

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with EASA ATPL ECQB and AviationExam syllabus.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/050_meteorology"

def build_met_ch01():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch01_atmosphere_structure_composition.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 1: Atmosphere Structure & ISA")

    pdf.add_title_banner(
        "Meteorology",
        1,
        "The Atmosphere: Structure, Composition & ISA",
        "1-32"
    )

    pdf.add_heading_1("1. Composition & Vertical Thermal Structure")
    pdf.add_paragraph(
        "The atmosphere is a mechanical mixture of gases surrounding the Earth, structured into concentric thermal layers:"
    )
    pdf.add_bullet("Gas Composition of Dry Air", "Nitrogen (N2) = 78.08%, Oxygen (O2) = 20.95%, Argon (Ar) = 0.93%, Carbon Dioxide (CO2) = 0.04%. Water vapor varies from 0% (polar/desert) to 4% (humid tropics).")
    pdf.add_bullet("Troposphere", "Lowest layer containing 75% of atmospheric mass and virtually all weather (clouds, precipitation). Temperature decreases with altitude. Upper boundary: Tropopause.")
    pdf.add_bullet("Tropopause Height Variation", "Pole: ~8 km (26,000 ft) with temperature ~ -45°C to -50°C. Mid-latitudes: ~11 km (36,090 ft) at -56.5°C. Equator: ~16 to 18 km (55,000 ft) with temperature ~ -75°C to -80°C (COLDEST TROPOPAUSE IS OVER THE EQUATOR!).")
    pdf.add_bullet("Stratosphere", "From Tropopause to Stratopause (~50 km). Temperature increases with altitude due to UV absorption by Ozone (O3). Smooth air, virtually zero water vapor.")

    pdf.add_heading_1("2. The ICAO Standard Atmosphere (ISA)")
    pdf.add_paragraph(
        "ISA provides an internationally agreed baseline for calibrating altimeters and aircraft performance:"
    )

    isa_table = [
        ["ISA Parameter", "Standard Sea Level Value", "Lapse Rate / Boundary Specification"],
        ["Mean Sea Level Pressure (MSL)", "1013.25 hPa (mbar) = 29.92 inHg = 760 mmHg", "Decreases ~ 1 hPa per 27 ft (or 30 ft) at sea level."],
        ["Mean Sea Level Temperature", "+15.0°C (288.15 Kelvin)", "Lapses at exactly 2.0°C / 1,000 ft (0.65°C / 100 m)."],
        ["Mean Sea Level Air Density", "1.225 kg/m^3", "Decreases with altitude and increasing temperature."],
        ["Speed of Sound at MSL (a_0)", "340.3 m/s = 661.5 knots", "Depends solely on absolute temperature: a = 38.94 x sqrt(T_K)."],
        ["ISA Tropopause Boundary", "11,000 meters = 36,090 ft", "Temperature reaches -56.5°C (216.65 K), remaining ISOTHERMAL up to 20 km (65,600 ft)."]
    ]
    pdf.add_table(["ISA Parameter", "Standard Sea Level Value", "Lapse Rate / Boundary Specification"], isa_table, col_widths=[115.0, 195.0, 190.0])

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating ISA Temperature & ISA Deviation",
        "SCENARIO (Fundamental AviationExam Question):\n"
        "An airliner is cruising at FL 330 (33,000 ft). The cockpit Outside Air Temperature (OAT) gauge reads -45°C.\n"
        "QUESTION: What is the ISA temperature at FL 330, and what is the ISA Deviation (Delta ISA)?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Recall the ISA Standard Sea Level Temperature:\n"
        "  - ISA MSL Temperature = +15.0°C.\n\n"
        "Step 2: Calculate the standard temperature decrease up to FL 330:\n"
        "  - ISA Lapse Rate = 2.0°C per 1,000 ft.\n"
        "  - Total temperature decrease = 33 x 2.0°C = 66.0°C.\n\n"
        "Step 3: Calculate ISA Temperature at 33,000 ft:\n"
        "  - ISA Temp = MSL Temp - Temperature Decrease\n"
        "  - ISA Temp = +15.0°C - 66.0°C = -51.0°C!\n\n"
        "Step 4: Calculate the ISA Deviation (Delta ISA):\n"
        "  - Formula: Delta ISA = Actual OAT - ISA Temperature\n"
        "  - Delta ISA = -45.0°C - (-51.0°C) = -45.0°C + 51.0°C = +6.0°C!\n\n"
        "FINAL ANSWER: ISA Temperature at FL 330 = -51°C. ISA Deviation = ISA +6°C (WARMER than standard).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Coldest Tropopause Exam Trap",
        "- The tropopause is HIGHEST and COLDEST over the EQUATOR (17 km / -80°C)!\n"
        "- It is LOWEST and WARMEST over the POLES (8 km / -45°C).\n"
        "- Many students incorrectly guess that the poles have the coldest tropopause. That is false!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: What are the standard values for temperature and pressure in the ICAO Standard Atmosphere (ISA) at Mean Sea Level?",
         "[A] 0°C and 1000 hPa\n[B] +15°C and 1013.25 hPa\n[C] +20°C and 1013.25 hPa\n[D] +15°C and 1000 hPa",
         "CORRECT: [B]. The ICAO Standard Atmosphere defines MSL datum as +15°C (288.15 K) and 1013.25 hPa (29.92 inHg)."),
        ("Q2: Where on Earth is the tropopause physically highest and its temperature coldest?",
         "[A] Over the North and South Poles\n[B] Over the Equator (height ~16-18 km, temperature ~ -75°C to -80°C)\n[C] Over mid-latitude depressions\n[D] Over the Sahara desert",
         "CORRECT: [B]. Intense convective heating expands the equatorial troposphere to 17-18 km. Because temperature lapses continuously through this deep column, the equatorial tropopause is the coldest."),
        ("Q3: Up to what altitude does the ISA temperature lapse rate of 2°C per 1,000 ft remain valid before becoming isothermal?",
         "[A] 20,000 ft\n[B] 36,090 ft (11,000 meters), where temperature reaches -56.5°C\n[C] 50,000 ft\n[D] 45,000 ft",
         "CORRECT: [B]. Under ISA definition, the lapse rate terminates at 11 km (36,090 ft) at -56.5°C, where the isothermal stratosphere begins.")
    ]

    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 1 compiled: {pdf_path}")


def build_met_ch02():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch02_pressure_altimetry_qcodes.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 2: Pressure & Altimetry")

    pdf.add_title_banner(
        "Meteorology",
        2,
        "Atmospheric Pressure, Altimetry & Q-Codes",
        "33-68"
    )

    pdf.add_heading_1("1. Pressure Gradients & Altimeter Q-Codes")
    pdf.add_paragraph(
        "Atmospheric pressure is the weight of the air column above a unit surface area. It governs altimetry:"
    )

    q_table = [
        ["Q-Code / Datum", "Reference Pressure Datum Plane", "Altimeter Reading & Cockpit Usage"],
        ["QNH (Nautical Height)", "Atmospheric pressure reduced to Mean Sea Level (MSL) using ISA lapse rate.", "Altimeter reads ALTITUDE above MSL. Reads exact aerodrome elevation on runway!"],
        ["QFE (Field Elevation)", "Actual atmospheric pressure measured at the aerodrome reference datum.", "Altimeter reads HEIGHT (AGL) above aerodrome. Reads exactly ZERO on runway threshold!"],
        ["QNE / Standard (1013.25)", "Standard datum plane 1013.25 hPa.", "Altimeter reads FLIGHT LEVELS (FL) above Transition Altitude. (e.g. FL 350 = 35,000 ft standard)."]
    ]
    pdf.add_table(["Q-Code / Datum", "Reference Pressure Datum Plane", "Altimeter Reading & Cockpit Usage"], q_table, col_widths=[115.0, 195.0, 190.0])

    pdf.add_heading_1("2. Temperature Errors in Altimetry")
    pdf.add_paragraph(
        "An altimeter is calibrated strictly to the ISA atmosphere. Non-standard temperatures create dangerous errors:"
    )
    pdf.add_bullet("Rule of Thumb", "'From High to Low or Hot to Cold, Look Out Below!' When flying into air that is colder than ISA, the atmospheric column compresses. The altimeter over-reads, and your TRUE ALTITUDE IS LOWER than indicated!")
    pdf.add_bullet("Cold Temperature Correction", "True Altitude Correction = 4 ft x (Height above station / 1,000 ft) x (ISA Deviation below standard).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Altimeter Reading Changing QNH to Standard",
        "SCENARIO (Classic Altimetry Transition Drill):\n"
        "An aircraft is cruising at an Indicated Altitude of 5,000 ft with the subscale set to QNH 993 hPa.\n"
        "ATC clears the pilot to climb to FL 80 and instructs: 'Set Standard 1013 hPa'.\n"
        "QUESTION: What will the altimeter indicate immediately after setting the subscale to 1013.25 hPa before any climb takes place?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Pressure Difference on the subscale:\n"
        "  - New setting = 1013 hPa\n"
        "  - Old setting = 993 hPa\n"
        "  - Pressure Change = 1013 - 993 = +20 hPa.\n\n"
        "Step 2: Understand the physical rule for subscale adjustment:\n"
        "  - Turning the subscale to a HIGHER pressure number forces the altimeter hands to WIND UP (indicate a higher altitude)!\n"
        "  - Rate of change: 1 hPa = approx 27 ft (or 30 ft in low-altitude rules).\n"
        "  - Using standard EASA rule of 27 ft/hPa (or 30 ft/hPa):\n"
        "    * 20 hPa x 27 ft/hPa = 540 ft (using 30 ft/hPa = 600 ft).\n\n"
        "Step 3: Calculate the New Indicated Altitude:\n"
        "  - New Indicated Altitude = Old Indicated + Adjustment\n"
        "  - Using 27 ft/hPa: 5,000 ft + 540 ft = 5,540 ft!\n"
        "  - (Using 30 ft/hPa: 5,000 ft + 600 ft = 5,600 ft).\n\n"
        "FINAL ANSWER: The altimeter pointer winds clockwise to indicate approximately 5,540 ft to 5,600 ft.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The High to Low Pressure Trap",
        "- If you fly from an area of HIGH pressure into an area of LOW pressure without resetting the altimeter:\n"
        "- The altimeter CONTINUES TO READ THE OLD ALTITUDE, but your airplane has descended!\n"
        "- You are physically CLOSER TO THE GROUND than your instrument displays ('High to low, look out below!').",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: If an aircraft flies from a region of HIGH pressure into an area of LOW pressure without adjusting the altimeter subscale, what does the altimeter read?",
         "[A] It reads lower than the true altitude\n[B] It reads HIGHER than the true altitude (the aircraft is lower than the pilot believes)\n[C] It reads the correct altitude\n[D] It fails",
         "CORRECT: [B]. The altimeter measures ambient pressure. In low pressure, the altimeter assumes the plane has climbed, so it over-reads. The aircraft's true altitude is lower."),
        ("Q2: When on the ground at an aerodrome with the altimeter subscale set to QFE, what does the altimeter indicate?",
         "[A] Aerodrome elevation above sea level\n[B] Exactly ZERO feet\n[C] Density altitude\n[D] Pressure altitude",
         "CORRECT: [B]. QFE is the measured pressure at the airfield datum. With QFE set on the ground, the altimeter indicates height above the field, which is 0 ft."),
        ("Q3: What is the Transition Level (TRL)?",
         "[A] The highest altitude where QNH is used\n[B] The LOWEST AVAILABLE FLIGHT LEVEL above the Transition Altitude (TA)\n[C] 3,000 ft\n[D] The level of the tropopause",
         "CORRECT: [B]. Transition Altitude (TA) is the highest altitude using QNH. Transition Level (TRL) is the lowest usable Flight Level using standard 1013.25 hPa above the transition layer.")
    ]

    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 2 compiled: {pdf_path}")


def build_met_ch03():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch03_density_temperature_inversions.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 3: Density & Temperature Inversions")

    pdf.add_title_banner(
        "Meteorology",
        3,
        "Atmospheric Density, Temperature & Inversions",
        "69-98"
    )

    pdf.add_heading_1("1. Air Density & Aircraft Performance")
    pdf.add_paragraph(
        "Air density (rho) is mass per unit volume. Lift, drag, engine thrust, and propeller efficiency are directly proportional to air density:"
    )
    pdf.add_bullet("Density Relationships", "Density INCREASES with: Increasing pressure, Decreasing temperature, and Decreasing humidity (dry air is denser than moist air because H2O molecular weight 18 is lighter than N2 28 / O2 32!).")
    pdf.add_bullet("Density Altitude (DA)", "Pressure altitude corrected for non-standard temperature: Density Alt = Pressure Alt + 120 ft x (OAT - ISA Temp). High density altitude severely degrades take-off roll and climb!")

    pdf.add_heading_1("2. Temperature Inversions (Negative Lapse Rate)")
    pdf.add_paragraph(
        "An inversion occurs when temperature INCREASES with altitude instead of decreasing:"
    )
    pdf.add_bullet("Radiation Inversion (Ground Inversion)", "Forms on clear, calm nights as the ground radiates heat into space. Chills the contact air layer. Disperses mid-morning with solar heating.")
    pdf.add_bullet("Subsidence Inversion", "Forms in high-pressure anticylones as sinking air warms adiabatically, capping pollution, haze, and stratocumulus clouds below it.")
    pdf.add_bullet("Frontal Inversion", "Occurs across a warm front where warm air ascends over a wedge of cold surface air.")
    pdf.add_bullet("Aviation Hazards of Inversions", "Creates intense low-level windshear across the inversion boundary, severely degrades engine performance climbing through the warm layer, and traps pollutants reducing visibility.")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Density Altitude from QNH and OAT",
        "SCENARIO (Classic Performance & Meteorology Exam Question):\n"
        "An airfield has an elevation of 3,000 ft MSL:\n"
        "- Current QNH = 1003 hPa\n"
        "- Outside Air Temperature (OAT) = +31°C\n"
        "QUESTION: What is the Pressure Altitude and the Density Altitude at the airfield?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate Pressure Altitude (PA):\n"
        "  - Formula: PA = Elevation + 27 ft x (1013.25 - QNH)\n"
        "  - Pressure difference = 1013.25 - 1003 = +10.25 hPa.\n"
        "  - Altitude correction = 10.25 hPa x 27 ft/hPa = 277 ft (or ~300 ft).\n"
        "  - PA = 3,000 ft + 277 ft = 3,277 ft (~3,280 ft).\n\n"
        "Step 2: Calculate ISA Temperature at 3,277 ft:\n"
        "  - ISA Temp at Sea Level = +15.0°C.\n"
        "  - Lapse = 3.28 x 2°C = 6.56°C.\n"
        "  - ISA Temp at airfield = +15.0°C - 6.56°C = +8.44°C (~ +8.5°C).\n\n"
        "Step 3: Calculate ISA Deviation:\n"
        "  - Actual OAT = +31.0°C\n"
        "  - Delta ISA = 31.0°C - 8.44°C = +22.56°C (22.6°C WARMER than standard!).\n\n"
        "Step 4: Calculate Density Altitude (DA):\n"
        "  - Formula: DA = Pressure Altitude + 120 ft x Delta ISA\n"
        "  - Temperature adjustment = 120 ft x 22.56°C = 2,707 ft!\n"
        "  - DA = 3,277 ft + 2,707 ft = 5,984 ft (~6,000 ft)!\n\n"
        "FINAL ANSWER: Pressure Altitude = 3,280 ft. Density Altitude = 5,984 ft! (The aircraft will perform as if it were taking off at 6,000 ft altitude!).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Humid Air vs Dry Air Density Trap",
        "- Many students think humid air is heavier than dry air. THIS IS A TRAP!\n"
        "- Water vapor (H2O, molecular mass 18) is LIGHTER than dry air (N2 28 + O2 32, average mass 29)!\n"
        "- Therefore, HIGH HUMIDITY DECREASES AIR DENSITY and degrades aircraft performance!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: Under which weather conditions is a SURFACE RADIATION INVERSION most likely to develop?",
         "[A] Strong winds and heavy overcast clouds\n[B] CLEAR NIGHTS with calm or very light wind\n[C] Active cold front passage\n[D] Midday summer sun",
         "CORRECT: [B]. Rapid terrestrial radiative cooling into a clear sky combined with calm air allows the surface air to chill rapidly while the air above remains warmer."),
        ("Q2: How does an increase in moisture content (relative humidity) affect the density of the air?",
         "[A] Increases density\n[B] DECREASES density (moist air is less dense than dry air)\n[C] Has zero effect\n[D] Doubles air pressure",
         "CORRECT: [B]. Water molecules (H2O, mol wt 18) displace heavier nitrogen (28) and oxygen (32) molecules in a given volume, making humid air lighter/less dense."),
        ("Q3: What flight hazard is most frequently encountered when climbing or descending through a strong temperature inversion?",
         "[A] Severe airframe icing\n[B] Marked LOW-LEVEL WINDSHEAR and turbulence across the inversion boundary\n[C] Complete loss of pitot pressure\n[D] Heavy hail",
         "CORRECT: [B]. The thermal boundary decouples surface air from the upper flow, frequently generating severe vertical and directional windshear.")
    ]

    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 3 compiled: {pdf_path}")


def build_met_ch04():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch04_moisture_humidity_adiabatic_processes.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 4: Moisture & Adiabatic Processes")

    pdf.add_title_banner(
        "Meteorology",
        4,
        "Moisture, Humidity & Atmospheric Stability",
        "99-136"
    )

    pdf.add_heading_1("1. Humidity Concepts & The Dew Point")
    pdf.add_paragraph(
        "Water vapor is the driving fuel of atmospheric thermodynamics:"
    )
    pdf.add_bullet("Relative Humidity (RH)", "Ratio of actual water vapor pressure to the saturation vapor pressure at that temperature, expressed as %: RH = (Actual Vapor Pressure / Saturation Vapor Pressure) x 100.")
    pdf.add_bullet("Dew Point (DP / Td)", "The temperature to which unsaturated air must be cooled at constant pressure to become fully saturated (RH = 100%). Small temperature-dew point spread indicates imminent fog or cloud formation!")

    pdf.add_heading_1("2. Adiabatic Lapse Rates & Stability")
    pdf.add_paragraph(
        "As an air parcel rises, it expands due to decreasing external pressure and cools without exchanging heat with surrounding air (adiabatic process):"
    )
    pdf.add_bullet("Dry Adiabatic Lapse Rate (DALR)", "Applies to unsaturated air: Constant at 3.0°C / 1,000 ft (1.0°C / 100 m = 9.8°C / km).")
    pdf.add_bullet("Saturated Adiabatic Lapse Rate (SALR)", "Applies once condensation occurs (saturated air): Variable, approximately 1.5°C / 1,000 ft (0.5°C to 0.7°C / 100 m). SALR is lower than DALR because latent heat of condensation (600 cal/g) is released into the parcel, retarding its cooling!")
    pdf.add_bullet("Environmental Lapse Rate (ELR)", "The actual measured temperature profile of the ambient atmosphere.")

    stability_table = [
        ["Atmospheric Stability State", "Mathematical Criterion (ELR vs DALR / SALR)", "Associated Weather & Cloud Types"],
        ["Absolute Stability", "ELR < SALR (Lapse rate is shallow or inverted, e.g. < 1.5°C/1,000 ft).", "No vertical convection. Stratiform flat clouds (Stratus), smooth air, poor surface visibility/fog."],
        ["Absolute Instability", "ELR > DALR (Lapse rate is steep, > 3.0°C/1,000 ft / superadiabatic).", "Violent convective up/downdrafts, Cumulonimbus (CB), severe turbulence, good visibility outside showers."],
        ["Conditional Instability", "SALR < ELR < DALR (ELR is between 1.5°C and 3.0°C/1,000 ft).", "Stable if air is dry; violently UNSTABLE if lifted to its saturation level (LCL)!"]
    ]
    pdf.add_table(["Atmospheric Stability State", "Mathematical Criterion (ELR vs DALR / SALR)", "Associated Weather & Cloud Types"], stability_table, col_widths=[125.0, 195.0, 180.0])

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Convective Cloud Base Height",
        "SCENARIO (Extremely Common EASA Exam Question):\n"
        "Surface weather observations report:\n"
        "- Surface Temperature = +22°C\n"
        "- Surface Dew Point = +12°C\n"
        "- Airfield elevation = 500 ft MSL\n"
        "QUESTION: At what altitude MSL will the base of convective Cumulus clouds form?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Temperature - Dew Point Spread at surface:\n"
        "  - Spread = Surface Temperature - Dew Point\n"
        "  - Spread = 22°C - 12°C = 10°C.\n\n"
        "Step 2: Understand how the Spread closes with altitude in a rising parcel:\n"
        "  - Rising dry parcel cools at DALR = 3.0°C per 1,000 ft.\n"
        "  - Dew point also drops slightly as pressure falls = 0.5°C per 1,000 ft.\n"
        "  - Net closing rate of the spread = 3.0°C - 0.5°C = 2.5°C per 1,000 ft (or 400 ft per °C)!\n\n"
        "Step 3: Calculate Cloud Base Height Above Ground Level (AGL):\n"
        "  - Cloud Base AGL = (Spread / 2.5°C) x 1,000 ft\n"
        "  - Cloud Base AGL = (10°C / 2.5°C) x 1,000 ft = 4 x 1,000 ft = 4,000 ft AGL!\n\n"
        "Step 4: Convert Height AGL to Altitude MSL (Add airfield elevation):\n"
        "  - Cloud Base MSL = Height AGL + Field Elevation\n"
        "  - Cloud Base MSL = 4,000 ft + 500 ft = 4,500 ft MSL!\n\n"
        "FINAL ANSWER: Cloud base forms at 4,000 ft AGL (4,500 ft MSL).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "AGL vs MSL Cloud Base Trap",
        "- The formula (T - DP)/2.5 gives cloud base ABOVE GROUND LEVEL (AGL)!\n"
        "- If the exam question asks for ALTITUDE MSL, you MUST ADD aerodrome elevation!\n"
        "- Forgetting to add elevation is the most frequent trap in this question.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: Why is the Saturated Adiabatic Lapse Rate (SALR) lower than the Dry Adiabatic Lapse Rate (DALR)?",
         "[A] Saturated air is heavier\n[B] Because LATENT HEAT of condensation is released when water vapor condenses, warming the rising parcel\n[C] Friction with falling rain\n[D] Sun heating",
         "CORRECT: [B]. As water vapor condenses into water droplets, latent heat (approx 2.5 x 10^6 J/kg) is released into the air parcel, partially offsetting adiabatic expansion cooling."),
        ("Q2: If the ambient Environmental Lapse Rate (ELR) is 2.2°C per 1,000 ft, what is the stability state of the atmosphere?",
         "[A] Absolute stability\n[B] Absolute instability\n[C] CONDITIONAL INSTABILITY (because ELR lies between SALR ~1.5°C and DALR 3.0°C)\n[D] Neutral",
         "CORRECT: [C]. When ELR is between SALR and DALR, the atmosphere is conditionally unstable: stable if unsaturated, but unstable if forced to saturation."),
        ("Q3: What type of cloud is produced when an absolutely STABLE layer of air is forced to rise over a mountain ridge?",
         "[A] Cumulonimbus with severe hail\n[B] STRATIFORM clouds (smooth sheets such as Stratus or Altostratus) without vertical development\n[C] Isolated towering cumulus\n[D] Mammatus",
         "CORRECT: [B]. In stable air, displaced air resists vertical motion, producing flat, horizontal layer clouds without thermal turbulence.")
    ]

    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 4 compiled: {pdf_path}")


def build_met_ch05():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch05_wind_dynamics_global_circulation.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 5: Wind Dynamics & Local Winds")

    pdf.add_title_banner(
        "Meteorology",
        5,
        "Wind Dynamics, Coriolis & Local Wind Systems",
        "137-174"
    )

    pdf.add_heading_1("1. Forces Governing Wind & Balance")
    pdf.add_paragraph(
        "Air motion is governed by four fundamental forces:"
    )
    pdf.add_bullet("Pressure Gradient Force (PGF)", "Acts perpendicular to isobars from HIGH pressure towards LOW pressure. Initiates all horizontal air motion.")
    pdf.add_bullet("Coriolis Force", "Apparent force caused by Earth's rotation. Deflects moving air to the RIGHT in the Northern Hemisphere (to the LEFT in the Southern Hemisphere). Zero at equator; maximum at poles. Proportional to wind speed.")
    pdf.add_bullet("Geostrophic Wind", "Theoretical wind resulting from an exact balance between PGF and Coriolis force blowing parallel to straight, parallel isobars above friction layer.")
    pdf.add_bullet("Surface Friction Effect (Veering vs Backing)", "Friction slows surface wind, reducing Coriolis force. PGF pulls air across isobars towards low pressure (~30° over land, ~10° over sea). In Northern Hemisphere: Climbing out, wind VEERS (turns clockwise) and INCREASES; Descending to land, wind BACKS (turns counter-clockwise) and DECREASES!")

    pdf.add_heading_1("2. Local Wind Phenomena")
    pdf.add_bullet("Sea Breeze vs Land Breeze", "Sea breeze develops by day (cooler sea air blows onshore toward heated land). Land breeze develops at night (cooling land air blows offshore).")
    pdf.add_bullet("Anabatic vs Katabatic Winds", "Anabatic wind: Daytime upslope wind as sun heats valley walls. Katabatic wind: Nighttime downslope gravity wind as dense cold air drains into valleys (e.g. Bora, Mistral).")
    pdf.add_bullet("The Föhn Effect (Chinook)", "Moist air rises on windward mountain slope cooling at SALR (losing moisture by rain). Descending on leeward slope, dry air warms at DALR (3°C/1,000 ft), arriving warm and extremely dry!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Temperature & Dew Point in a Föhn Wind",
        "SCENARIO (Standard EASA Föhn Exam Problem):\n"
        "Air at sea level (0 ft) on the windward side of a 6,000 ft mountain has:\n"
        "- Surface Temperature = +18°C\n"
        "- Surface Dew Point = +10.5°C\n"
        "- Cloud base (condensation level) on windward slope = 3,000 ft\n"
        "- Air crosses the ridge at 6,000 ft and descends to sea level on the leeward side\n"
        "QUESTION: What will be the temperature and dew point of the air when it reaches sea level on the leeward side?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Part 1: Windward Ascent (0 to 6,000 ft):\n"
        "  - From 0 to 3,000 ft (Dry ascent below cloud base at DALR = 3°C/1,000 ft):\n"
        "    * Temp decrease = 3 x 3.0°C = 9.0°C.\n"
        "    * Temp at 3,000 ft = 18.0°C - 9.0°C = +9.0°C.\n"
        "  - From 3,000 to 6,000 ft (Saturated ascent inside cloud at SALR = 1.5°C/1,000 ft):\n"
        "    * Temp decrease = 3 x 1.5°C = 4.5°C.\n"
        "    * Temp at mountain top (6,000 ft) = 9.0°C - 4.5°C = +4.5°C.\n"
        "    * (Because it is saturated at the peak, Dew Point at 6,000 ft = +4.5°C!).\n\n"
        "Part 2: Leeward Descent (6,000 ft down to 0 ft):\n"
        "  - The air dropped its moisture as rain on the windward side! All clouds evaporate instantly upon descending.\n"
        "  - ENTIRE DESCENT IS DRY at DALR = 3.0°C / 1,000 ft!\n"
        "  - Temperature increase = 6 x 3.0°C = +18.0°C.\n"
        "  - Final Leeward Temp at sea level = +4.5°C + 18.0°C = +22.5°C!\n\n"
        "Part 3: Final Dew Point on leeward side:\n"
        "  - Dew point increases down the slope at 0.5°C / 1,000 ft = 6 x 0.5°C = 3.0°C.\n"
        "  - Final Leeward Dew Point = 4.5°C + 3.0°C = +7.5°C.\n\n"
        "FINAL ANSWER: Leeward surface air is dramatically WARMER (+22.5°C vs +18°C) and DRIER (Dew Point +7.5°C vs +10.5°C)! Classic Föhn wind.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Veering vs Backing Memory Trap",
        "- In the Northern Hemisphere:\n"
        "- VEER = Clockwise turn (e.g. 240° to 270°). Occurs when CLIMBING.\n"
        "- BACK = Counter-clockwise turn (e.g. 270° to 240°). Occurs when DESCENDING towards landing.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: In the Northern Hemisphere, what happens to the wind direction and speed when descending from 3,000 ft AGL down to the runway surface?",
         "[A] Veers and increases\n[B] BACKS (turns counter-clockwise) and DECREASES in speed due to surface friction\n[C] Veers and decreases\n[D] Remains unchanged",
         "CORRECT: [B]. Surface friction slows the wind, reducing the Coriolis force. The pressure gradient force pulls the wind towards lower pressure, causing it to back and reduce speed."),
        ("Q2: What is the primary characteristic of a KATABATIC wind?",
         "[A] Warm daytime wind blowing upslope\n[B] COLD, DENSE AIR flowing downhill at night under the force of gravity\n[C] Wind blowing from sea to land\n[D] Jet stream core",
         "CORRECT: [B]. Nocturnal terrestrial radiation cools mountain air, making it dense and heavy. Gravity pulls this cold pool down valleys and slopes as a katabatic wind."),
        ("Q3: In the Föhn effect, why is the air arriving on the leeward side of the mountain warmer than when it started on the windward side?",
         "[A] Ground friction heats the air\n[B] Air cools at SALR on the wet ascent (releasing latent heat), but warms at the STEEPER DALR during the entire dry descent\n[C] Solar radiation doubles\n[D] Coriolis force",
         "CORRECT: [B]. Latent heat released during cloud formation on ascent warms the parcel; during descent, cloud dissipation allows dry adiabatic warming (3°C/1000 ft) over the full height.")
    ]

    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 5 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_met_ch01()
    build_met_ch02()
    build_met_ch03()
    build_met_ch04()
    build_met_ch05()
