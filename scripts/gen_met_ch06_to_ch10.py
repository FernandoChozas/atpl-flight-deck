#!/usr/bin/env python3
"""
Generator for Subject 050: Meteorology
Volume 2: Chapters 6 to 10
- Chapter 6: Global Jet Streams, Clear Air Turbulence (CAT) & Tropopause
- Chapter 7: Cloud Classification (10 Genera), Fog Formation Mechanisms & Mist
- Chapter 8: Precipitation Physics, Bergeron Process & Freezing Rain (FZRA)
- Chapter 9: Air Masses, Frontal Systems (Warm, Cold, Occluded) & Frontolysis
- Chapter 10: Pressure Systems: Mid-Latitude Depressions, Anticyclones & Cols

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with EASA ATPL ECQB and AviationExam syllabus.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/050_meteorology"

def build_met_ch06():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch06_jet_streams_cat.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 6: Jet Streams & CAT")

    pdf.add_title_banner(
        "Meteorology",
        6,
        "Global Jet Streams, Clear Air Turbulence & Tropopause",
        "175-208"
    )

    pdf.add_heading_1("1. Jet Stream Architecture & Criteria")
    pdf.add_paragraph(
        "A Jet Stream is a flat, tubular current of quasi-horizontal wind characterized by strong vertical and lateral wind shears:"
    )
    pdf.add_bullet("ICAO Official Definition", "A high-altitude wind stream with a minimum CORE SPEED of at least 60 KNOTS (typically 100 to 200+ knots)!")
    pdf.add_bullet("Polar Front Jet (PFJ)", "Located along the Polar Front between polar and tropical air masses. Core height: ~30,000 ft (FL 300 / 300 hPa). Discontinuous, meanders from 40° to 60° latitude. Strongest in winter!")
    pdf.add_bullet("Subtropical Jet (STJ)", "Located between Hadley and Ferrel cells at ~30° latitude. Core height: ~40,000 ft (FL 400 / 200 hPa). More stable in position, blowing from West to East.")
    pdf.add_bullet("Easterly Tropical Jet", "Summer jet in the Northern Hemisphere flowing from East to West over southern Asia and central Africa at FL 450 to FL 500.")

    pdf.add_heading_1("2. Clear Air Turbulence (CAT) Dynamics")
    pdf.add_paragraph(
        "CAT occurs in cloud-free air, primarily near jet streams and the tropopause break:"
    )
    pdf.add_bullet("Location of Maximum CAT", "Severe CAT is concentrated on the COLD (POLAR) SIDE of the jet core and directly ABOVE the jet core, where horizontal and vertical shears are greatest!")
    pdf.add_bullet("Critical Shear Criteria", "Severe CAT is expected when: Vertical Shear >= 6 knots per 1,000 ft, OR Horizontal Shear >= 18 knots per 100 NM!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Evaluating Wind Shear for Severe CAT Encounter",
        "SCENARIO (AviationExam High-Altitude Navigation Drill):\n"
        "An airliner is cruising at FL 350 on an airway near the Polar Front Jet:\n"
        "- At FL 350, wind is 270° at 140 knots\n"
        "- The pilot is cleared to descend to FL 310\n"
        "- At FL 310 (4,000 ft below), wind is reported as 270° at 170 knots (near the jet core)\n"
        "QUESTION: What is the vertical wind shear per 1,000 ft, and should the crew anticipate severe Clear Air Turbulence (CAT)?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Total Wind Speed Difference:\n"
        "  - Wind at FL 310 = 170 knots\n"
        "  - Wind at FL 350 = 140 knots\n"
        "  - Difference in speed = 170 kt - 140 kt = 30 knots.\n\n"
        "Step 2: Calculate the Altitude Difference in Thousands of Feet:\n"
        "  - Altitude difference = 35,000 ft - 31,000 ft = 4,000 ft = 4.0 thousand ft.\n\n"
        "Step 3: Calculate Vertical Wind Shear per 1,000 ft:\n"
        "  - Vertical Shear = Speed Difference / Height Difference\n"
        "  - Vertical Shear = 30 knots / 4.0 thousand ft = 7.5 knots per 1,000 ft!\n\n"
        "Step 4: Compare with the ICAO Severe CAT Threshold:\n"
        "  - Threshold for Severe CAT = 6.0 knots per 1,000 ft.\n"
        "  - Actual Vertical Shear = 7.5 knots per 1,000 ft.\n"
        "  - Check: 7.5 kt/1,000 ft > 6.0 kt/1,000 ft -> EXCEEDS SEVERE THRESHOLD!\n\n"
        "FINAL ANSWER: Vertical shear is 7.5 kt/1,000 ft. Severe CAT is highly probable! The crew must switch on Fasten Seatbelt signs and select Turbulent Air Penetration Speed (V_ra).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Cold Side vs Warm Side CAT Trap",
        "- The COLD (low pressure/polar) side of the jet stream has MUCH STRONGER SHEAR than the warm side!\n"
        "- If flying parallel to a westerly jet stream in the Northern Hemisphere:\n"
        "- North of the jet core = Cold side = MAXIMUM TURBULENCE.\n"
        "- South of the jet core = Warm side = Moderate/light turbulence.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: What is the official ICAO minimum core wind speed required for a high-altitude wind current to be classified as a 'JET STREAM'?",
         "[A] 40 knots\n[B] AT LEAST 60 KNOTS\n[C] 100 knots\n[D] 150 knots",
         "CORRECT: [B]. Under WMO and ICAO definitions, a jet stream must have a minimum wind speed of 60 knots along its central axis."),
        ("Q2: In relation to the jet stream core, where is the most severe Clear Air Turbulence (CAT) typically located?",
         "[A] Exactly inside the core where speed is fastest\n[B] On the COLD (polar) side of the core and just above the core, where wind shear is greatest\n[C] On the warm side below the core\n[D] Equatorward of the jet",
         "CORRECT: [B]. Turbulence is generated by wind shear (speed gradient), not absolute speed. The polar side exhibits much tighter horizontal and vertical gradients."),
        ("Q3: What seasonal change occurs in the strength and geographic position of the Polar Front Jet (PFJ)?",
         "[A] Strongest in summer and moves equatorward\n[B] STRONGEST IN WINTER and moves EQUATORWARD (lower latitudes)\n[C] Strongest in summer over the poles\n[D] Unchanged throughout the year",
         "CORRECT: [B]. In winter, the equator-to-pole temperature contrast is at its maximum, intensifying the pressure gradient and driving the jet stream further south with higher core speeds.")
    ]

    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 6 compiled: {pdf_path}")


def build_met_ch07():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch07_cloud_classification_fog_mist.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 7: Clouds & Fog Formation")

    pdf.add_title_banner(
        "Meteorology",
        7,
        "Cloud Classification (10 Genera) & Fog Types",
        "209-248"
    )

    pdf.add_heading_1("1. The 10 Cloud Genera (ICAO Classification)")
    pdf.add_paragraph(
        "Clouds are classified by height of base and physical appearance into 10 official genera:"
    )

    cloud_table = [
        ["Cloud Level & Height Range", "Official Cloud Genera Codes", "Physical Characteristics & Composition"],
        ["High Clouds (Base > 20,000 ft / FL 200)", "Ci (Cirrus), Cc (Cirrocumulus), Cs (Cirrostratus)", "Composed purely of ICE CRYSTALS. Cs causes optical HALO around sun/moon. Ci mares' tails signal approaching warm front."],
        ["Medium Clouds (Base 6,500 to 20,000 ft)", "Ac (Altocumulus), As (Altostratus), Ns (Nimbostratus)", "Mixed water droplets and ice. As gives watery sun appearance. Ns produces continuous rain/snow (dark and thick)."],
        ["Low Clouds (Base 0 to 6,500 ft AGL)", "Sc (Stratocumulus), St (Stratus), Cu (Cumulus)", "Water droplets. St is a uniform grey layer causing drizzle. Sc is a rolling grey sheet."],
        ["Clouds with Vertical Development", "Cb (Cumulonimbus), TCU (Towering Cumulus)", "Massive vertical anvil cloud. Generates violent thunderstorms, severe icing, hail, lightning, and microbursts!"]
    ]
    pdf.add_table(["Cloud Level & Height Range", "Official Cloud Genera Codes", "Physical Characteristics & Composition"], cloud_table, col_widths=[115.0, 195.0, 190.0])

    pdf.add_heading_1("2. Fog Formation Mechanisms & Differences")
    pdf.add_bullet("Radiation Fog", "Formed over land on CLEAR, CALM NIGHTS with light wind (2 to 8 kt) and high RH. Terrestrial radiation chills surface air below dew point. Disperses mid-morning with solar heating or strong wind (> 10 kt mixes and lifts it into Stratus). NEVER OCCURS OVER THE OPEN SEA!")
    pdf.add_bullet("Advection Fog", "Formed when WARM, MOIST AIR moves over a COLDER surface. Requires moderate wind (10 to 15 kt). Extremely persistent day and night, over both land and sea (e.g. San Francisco, English Channel).")
    pdf.add_bullet("Upslope Fog (Hill Fog)", "Formed when moist air is forced up mountain slopes, cooling adiabatically to its dew point.")
    pdf.add_bullet("Steam Fog (Arctic Sea Smoke)", "Formed when extremely COLD, DRY AIR blows over WARM WATER. Water evaporates rapidly into the cold air, instantly condensing like steam.")

    pdf.add_heading_1("3. Fog vs Mist vs Haze")
    pdf.add_bullet("Fog (FG)", "Visibility < 1,000 meters, Relative Humidity ~ 100% (water droplets).")
    pdf.add_bullet("Mist (BR)", "Visibility 1,000 to 5,000 meters, Relative Humidity >= 95% (water droplets).")
    pdf.add_bullet("Haze (HZ)", "Visibility <= 5,000 meters, Relative Humidity < 95% (dry dust, smoke, pollutants).")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: Which of the following conditions are REQUIRED for the formation of RADIATION FOG?",
         "[A] Strong wind and thick overcast cloud\n[B] A CLEAR SKY at night, high relative humidity, and LIGHT WIND (2 to 8 knots)\n[C] Warm moist air blowing over cold ocean currents\n[D] Freezing rain",
         "CORRECT: [B]. Radiation fog requires maximum terrestrial cooling (clear sky) and light breeze (2-8 kt) to mix the cooled air throughout the shallow surface layer without dispersing it."),
        ("Q2: Why can RADIATION FOG never form over the open ocean?",
         "[A] Sea water contains salt\n[B] The sea surface temperature undergoes virtually NO DIURNAL TEMPERATURE CHANGE (only ~0.5°C to 1°C)\n[C] Winds over the sea are always calm\n[D] Too much evaporation",
         "CORRECT: [B]. The high specific heat capacity of water prevents the sea surface from cooling rapidly at night, making radiation fog impossible over the open sea."),
        ("Q3: Which cloud genus is responsible for producing an optical HALO around the sun or moon?",
         "[A] Altostratus\n[B] CIRROSTRATUS (Cs), due to light refraction through hexagonal ice crystals\n[C] Stratocumulus\n[D] Nimbostratus",
         "CORRECT: [B]. Cirrostratus is composed entirely of ice crystals that act as prisms, refracting sunlight or moonlight at a 22° angle to produce a prominent halo.")
    ]

    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 7 compiled: {pdf_path}")


def build_met_ch08():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch08_precipitation_freezing_rain.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 8: Precipitation & Freezing Rain")

    pdf.add_title_banner(
        "Meteorology",
        8,
        "Precipitation Physics & Freezing Rain (FZRA)",
        "249-278"
    )

    pdf.add_heading_1("1. Mechanisms of Precipitation Growth")
    pdf.add_paragraph(
        "Cloud droplets are microscopic (~0.02 mm) and held aloft by updrafts. Precipitation requires droplet growth by orders of magnitude (~1 to 5 mm):"
    )
    pdf.add_bullet("Collision-Coalescence Process", "Dominant in 'warm clouds' (temperatures > 0°C, tropics/maritime). Larger droplets fall faster, colliding with smaller droplets and sweeping them up to form raindrops.")
    pdf.add_bullet("The Bergeron-Findeisen Process", "Dominant in 'cold clouds' (temperatures -10°C to -40°C) containing both supercooled water droplets and ice crystals. The saturation vapor pressure over ice is LOWER than over water. Vapor diffuses from water droplets onto ice crystals, causing rapid crystal growth into snowflakes!")

    pdf.add_heading_1("2. Forms of Precipitation")
    pdf.add_bullet("Drizzle (DZ)", "Very small water droplets (diameter < 0.5 mm) falling close together. Produced EXCLUSIVELY by Stratus (St) clouds!")
    pdf.add_bullet("Rain (RA)", "Liquid water droplets (diameter 0.5 to 5.0 mm). Continuous rain from Nimbostratus (Ns); Intermittent showers from Cumuliform clouds.")
    pdf.add_bullet("Sleet / Ice Pellets (PL)", "Translucent frozen raindrops formed when rain falls through a deep freezing layer near the ground.")
    pdf.add_bullet("Hail (GR)", "Balls of concentric ice (diameter >= 5 mm). Produced EXCLUSIVELY by Cumulonimbus (CB) with violent updrafts!")

    pdf.add_heading_1("3. Freezing Rain (FZRA) - The Extreme Hazard")
    pdf.add_paragraph(
        "Freezing rain is one of the most hazardous meteorological phenomena in aviation:"
    )
    pdf.add_bullet("How FZRA Forms", "Snow falls from high clouds into a WARM LAYER ALOFT with temperatures > 0°C, melting completely into rain. The rain then falls into a SUB-ZERO SURFACE COLD AIR LAYER (temperature < 0°C). The drops become supercooled liquid.")
    pdf.add_bullet("Impact on Aircraft", "Upon impacting the cold airframe, the supercooled rain spreads back over the wing and freezes instantly into CLEAR ICE (Glaze). It can accumulate at over 5 cm per hour, covering aerofoils, freezing flight controls, and causing immediate aerodynamic stall!")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: In the Bergeron-Findeisen precipitation process, why do ice crystals grow rapidly while supercooled water droplets evaporate?",
         "[A] Ice is warmer than water\n[B] The saturation vapor pressure over ICE is LOWER than the saturation vapor pressure over WATER at the same sub-zero temperature\n[C] Updrafts only lift ice\n[D] Sun rays melt water",
         "CORRECT: [B]. Because saturation vapor pressure is lower over ice, a vapor pressure gradient exists from water to ice. Water droplets evaporate and deposit directly onto ice crystals."),
        ("Q2: Under which vertical temperature profile does FREEZING RAIN (FZRA) form?",
         "[A] Temperature permanently below -20°C from surface to cruise\n[B] A WARM LAYER ALOFT with temperature > 0°C situated above a cold freezing surface layer with temperature < 0°C\n[C] Standard ISA lapse rate\n[D] Surface heating",
         "CORRECT: [B]. Falling snow melts into liquid rain in the warm air wedge aloft, then becomes supercooled as it falls through the sub-zero layer near the ground, freezing on contact."),
        ("Q3: Which cloud type is EXCLUSIVELY responsible for producing DRIZZLE?",
         "[A] Cirrus\n[B] STRATUS (St)\n[C] Cumulonimbus\n[D] Altocumulus",
         "CORRECT: [B]. Drizzle consists of uniform droplets < 0.5 mm in diameter, produced exclusively by low-level, stable Stratus clouds.")
    ]

    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 8 compiled: {pdf_path}")


def build_met_ch09():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch09_air_masses_frontal_systems.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 9: Air Masses & Frontal Systems")

    pdf.add_title_banner(
        "Meteorology",
        9,
        "Air Masses & Frontal Systems (Warm, Cold, Occluded)",
        "279-322"
    )

    pdf.add_heading_1("1. Air Masses & Source Regions")
    pdf.add_paragraph(
        "An air mass is a large body of air whose temperature and humidity characteristics are relatively uniform over thousands of kilometers:"
    )
    pdf.add_bullet("Source Classifications", "Arctic (A), Polar (P), Tropical (T); subdivided into Maritime (m) (moist) and Continental (c) (dry). E.g. mP = Maritime Polar (cool, moist, unstable); cT = Continental Tropical (hot, dry, unstable).")

    pdf.add_heading_1("2. Frontal Systems Comparison")
    front_table = [
        ["Frontal Parameter", "Warm Front (Warm air replaces cold)", "Cold Front (Cold air replaces warm)"],
        ["Frontal Slope & Speed", "Shallow slope (1:150). Slower speed (~15 to 20 kt).", "Steep slope (1:50). Fast speed (~25 to 40 kt)."],
        ["Cloud Sequence on Approach", "Ci -> Cs (halo) -> As (watery sun) -> Ns (continuous rain).", "Cu building rapidly into Cb and squall lines."],
        ["Precipitation Type", "Continuous, widespread rain or snow. Extensive low Stratus.", "Heavy showers, hail, thunderstorms, brief intense downpour."],
        ["Wind Behavior during Passage", "Veers (clockwise in N Hemisphere) and decreases slightly.", "Sharp, violent VEER (e.g. 210° to 300°), gusty with squalls."],
        ["Post-Frontal Weather", "Warm sector: High dew point, poor visibility, mist, low drizzle.", "Cold air: Rapid clearing, marked temperature DROP, excellent visibility!"]
    ]
    pdf.add_table(["Frontal Parameter", "Warm Front (Warm air replaces cold)", "Cold Front (Cold air replaces warm)"], front_table, col_widths=[125.0, 185.0, 190.0])

    pdf.add_heading_1("3. Occluded Fronts (Cold vs Warm Occlusion)")
    pdf.add_paragraph(
        "Because cold fronts move faster than warm fronts, the cold front eventually catches up with the warm front, lifting the warm sector completely off the ground:"
    )
    pdf.add_bullet("Cold Occlusion", "The air behind the advancing cold front is COLDER than the retreating cold air ahead of the warm front. The advancing cold wedge burrows beneath all air masses.")
    pdf.add_bullet("Warm Occlusion", "The air ahead of the warm front is colder than the air behind the cold front. The advancing cold air rides up over the very cold retreating air.")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch09 = [
        ("Q1: What is the typical cloud sequence observed ahead of an approaching WARM FRONT?",
         "[A] Cb, TCU, Cu, St\n[B] CIRRUS (Ci), CIRROSTRATUS (Cs), ALTOSTRATUS (As), and NIMBOSTRATUS (Ns)\n[C] Stratus, fog, clear sky\n[D] Altocumulus lenticularis",
         "CORRECT: [B]. The gentle slope (1:150) of a warm front pushes warm air aloft up to 600 NM ahead of the surface front, creating a descending cloud shield: Ci -> Cs -> As -> Ns."),
        ("Q2: What happens to the wind direction in the Northern Hemisphere during the passage of an active COLD FRONT?",
         "[A] Backs (turns counter-clockwise)\n[B] SHARPLY VEERS (turns clockwise, e.g. from Southwest to Northwest)\n[C] Remains perfectly constant\n[D] Drops to calm",
         "CORRECT: [B]. Cold front passage is marked by a sharp clockwise wind shift (veering) as the trough line crosses, typically shifting from SW to WNW or NW."),
        ("Q3: What characterizes the weather in the COLD AIR MASS immediately behind an active cold front?",
         "[A] Continuous low stratus and poor visibility\n[B] RAPID CLEARING with isolated convective showers, dropping temperature, and EXCELLENT VISIBILITY\n[C] Warm sector mist\n[D] Severe fog",
         "CORRECT: [B]. The cold, dense polar air is dry and clean, resulting in rapid pressure rise, gusty winds, dropping dew points, and superb visibility outside convective showers.")
    ]

    for q_text, opts, exp in questions_ch09:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 9 compiled: {pdf_path}")


def build_met_ch10():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch10_pressure_systems_depressions_anticyclones.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 10: Depressions & Anticyclones")

    pdf.add_title_banner(
        "Meteorology",
        10,
        "Pressure Systems: Depressions, Anticyclones & Cols",
        "323-358"
    )

    pdf.add_heading_1("1. Low Pressure Systems (Depressions / Cyclones)")
    pdf.add_paragraph(
        "A depression is an area of low barometric pressure surrounded by closed isobars. In the Northern Hemisphere, wind circulates COUNTER-CLOCKWISE and inwards towards the center:"
    )
    pdf.add_bullet("Polar Front Depressions", "Form along the boundary between cold polar and warm tropical air. Life cycle: Initial wave -> Developing depression -> Mature occlusion -> Decaying low.")
    pdf.add_bullet("Thermal Depressions (Heat Lows)", "Form over hot continental land masses in summer due to intense solar heating (e.g. Iberian Peninsula, Persian Gulf). Stationary, shallow, dissipating at night.")
    pdf.add_bullet("Orographic Depressions (Lee Lows)", "Form on the leeward side of mountain ranges as upper air crosses the ridge (e.g. Genoa Low south of the Alps).")

    pdf.add_heading_1("2. High Pressure Systems (Anticyclones)")
    pdf.add_paragraph(
        "An anticyclone is an area of high barometric pressure with widely spaced isobars. Wind circulates CLOCKWISE and outwards in the Northern Hemisphere:"
    )
    pdf.add_bullet("Characteristics of Anticyclones", "SUBSIDENCE: Air gently sinks from high levels, warming adiabatically. Sinking air suppresses vertical convection, producing stable, cloudless skies at upper levels.")
    pdf.add_bullet("Subtropical Anticyclones", "Permanent warm-core highs (e.g. Azores High) driving global trade winds.")
    pdf.add_bullet("Cold Continental Anticyclones", "Winter highs over snow-covered land (Siberian High, Canadian High). Extremely cold, dense surface air with intense ground inversions.")
    pdf.add_bullet("Blocking Highs", "Large, stagnant high-pressure cells that deflect mid-latitude depressions for weeks, causing persistent weather patterns.")

    pdf.add_heading_1("3. Ridges, Troughs & Cols")
    pdf.add_bullet("Ridge of High Pressure", "An elongated wedge of high pressure extending from an anticyclone. Brings improved, settled weather.")
    pdf.add_bullet("Trough of Low Pressure", "An elongated area of low pressure. Acts like a cold front, producing cloud lines, squalls, and showers.")
    pdf.add_bullet("Col", "The neutral saddle-point region between two highs and two lows. Characterized by calm or very light winds. Highly prone to RADIATION FOG IN WINTER, and SEVERE THUNDERSTORMS IN SUMMER!")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch10 = [
        ("Q1: What weather conditions are typically associated with a 'COL' during summer afternoons over land?",
         "[A] Gale-force winds\n[B] Light winds and heavy SEVERE THUNDERSTORMS caused by daytime surface heating\n[C] Persistent radiation fog\n[D] Snow flurries",
         "CORRECT: [B]. In summer, the calm winds and stagnation of a col allow strong diurnal surface heating to trigger violent convective thunderstorms."),
        ("Q2: In an ANTICYCLONE, why is cloud formation generally suppressed at middle and high altitudes?",
         "[A] Strong winds blow clouds away\n[B] Because of AIR SUBSIDENCE (sinking air warms adiabatically, lowering relative humidity)\n[C] Air is too cold to form clouds\n[D] Pressure is too low",
         "CORRECT: [B]. Sinking air warms at DALR (3°C/1,000 ft), moving further away from saturation (lower relative humidity) and evaporating cloud droplets."),
        ("Q3: What is a 'BLOCKING HIGH' in European meteorology?",
         "[A] A small thunderstorm cell\n[B] A large, quasi-stationary anticyclone that remains in place for days or weeks, blocking and deflecting approaching Atlantic depressions\n[C] An inversion at 1,000 ft\n[D] A hurricane eye",
         "CORRECT: [B]. Blocking anticyclones divert the mid-latitude westerly storm track to the north or south, locking the region into persistent dry or cold weather.")
    ]

    for q_text, opts, exp in questions_ch10:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 10 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_met_ch06()
    build_met_ch07()
    build_met_ch08()
    build_met_ch09()
    build_met_ch10()
