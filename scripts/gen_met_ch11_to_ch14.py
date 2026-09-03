#!/usr/bin/env python3
"""
Generator for Subject 050: Meteorology
Volume 3: Chapters 11 to 14
- Chapter 11: Flight Hazards I: Airframe Icing, Turbulence & Mountain Waves
- Chapter 12: Flight Hazards II: Thunderstorms (CB), Microbursts & Windshear
- Chapter 13: Tropical Meteorology, Tropical Revolving Storms & Climatology
- Chapter 14: Meteorological Reports, Forecasts & Charts (METAR, TAF, SIGMET)

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with EASA ATPL ECQB and AviationExam syllabus.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/050_meteorology"

def build_met_ch11():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch11_icing_turbulence_mountain_waves.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 11: Icing, Turbulence & Waves")

    pdf.add_title_banner(
        "Meteorology",
        11,
        "Flight Hazards I: Icing, Turbulence & Mountain Waves",
        "359-398"
    )

    pdf.add_heading_1("1. Airframe Structural Icing Physics")
    pdf.add_paragraph(
        "Structural icing occurs when an aircraft flies through visible liquid moisture (clouds/rain) at temperatures below 0°C:"
    )

    ice_table = [
        ["Icing Type", "Cloud Type & Temperature Range", "Physical Structure & Aerodynamic Severity"],
        ["Rime Ice (Rough / Opaque)", "Stratiform clouds (St, Sc, As) at -10°C to -20°C. Small supercooled droplets.", "Freezes instantly upon impact without spreading. Traps air, milky white, brittle. Alters aerofoil camber, increases drag."],
        ["Clear Ice (Glaze / Transparent)", "Cumuliform clouds (Cu, Cb) and FZRA at 0°C to -10°C. Large supercooled droplets.", "Freezes slowly, spreading aft beyond de-icing boots. Heavy, hard, tenacious. SEVEREST ICING HAZARD in aviation!"],
        ["Mixed Ice", "Mixed clouds at -10°C to -15°C. Combination of small and large droplets.", "Rough, hard, difficult to shed with de-icing boots."],
        ["Hoar Frost", "Forms on parked aircraft overnight, or descending rapidly into warm, moist air.", "Crystalline frost. Degrades boundary layer: INCREASES STALL SPEED by up to 33% and reduces lift by 30%!"]
    ]
    pdf.add_table(["Icing Type", "Cloud Type & Temperature Range", "Physical Structure & Aerodynamic Severity"], ice_table, col_widths=[115.0, 195.0, 190.0])

    pdf.add_heading_1("2. Mountain Waves (Lee Waves)")
    pdf.add_paragraph(
        "Mountain waves develop on the leeward side of mountain ridges under specific conditions:"
    )
    pdf.add_bullet("Necessary Conditions", "1. Wind direction within 30° of perpendicular to ridge; 2. Wind speed at crest level >= 20 knots and increasing with altitude; 3. Very stable air layer sandwiched between less stable layers above and below.")
    pdf.add_bullet("Wave Cloud Features", "Cap cloud (Föhn wall) over crest; Lenticular clouds (Altocumulus lenticularis) stationary at wave crests; Rotor clouds (Roll clouds) formed beneath wave crests with VIOLENT, DESTRUCTIVE TURBULENCE!")
    pdf.add_bullet("Wave Wavelength Rule of Thumb", "Wavelength (NM) ~ 0.5 x Wind speed across ridge (knots) (e.g. 40 kt wind -> ~20 NM wavelength).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Mountain Wave Rotor & Descent Hazards",
        "SCENARIO (Mountain Flight Safety Drill):\n"
        "A twin-engine aircraft is flying across the Pyrenees:\n"
        "- Mountain ridge height = 8,000 ft MSL\n"
        "- Wind at crest = 010° at 40 knots (directly perpendicular to ridge)\n"
        "- The leeward side exhibits Altocumulus lenticularis clouds at 12,000 ft and ragged roll clouds at 5,000 ft AGL\n"
        "QUESTION: What is the estimated distance between wave crests, and what lethal hazard lies inside the roll clouds?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Mountain Wave Wavelength:\n"
        "  - Formula: Wavelength (NM) ~ 0.5 x Wind Speed (knots)\n"
        "  - Wavelength = 0.5 x 40 kt = 20 Nautical Miles!\n"
        "  - (Successive downdrafts and updrafts will repeat every 20 NM downwind of the mountain!).\n\n"
        "Step 2: Identify the Hazards in the Roll Cloud (Rotor Zone):\n"
        "  - The roll cloud marks a closed atmospheric vortex (ROTOR).\n"
        "  - Air rotates violently about a horizontal axis.\n"
        "  - Updrafts and downdrafts exceed 3,000 to 5,000 ft/min.\n"
        "  - Flying into a rotor zone can cause structural overload, control loss, and violent barometric altimeter fluctuations!\n\n"
        "Step 3: Pilot Action:\n"
        "  - Never attempt to penetrate roll clouds! Fly at least 3,000 to 5,000 ft ABOVE the mountain crests, and approach ridges at a 45° angle to permit a retreat turn into the valley.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Hoar Frost Lift-Off Trap",
        "- Even a paper-thin layer of hoar frost on the upper wing surface ruins the laminar boundary layer!\n"
        "- It INCREASES STALL SPEED BY UP TO 33%, and REDUCES MAXIMUM LIFT BY 30%!\n"
        "- Take-off with frost on critical surfaces is STRICTLY ILLEGAL (Clean Aircraft Concept).",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch11 = [
        ("Q1: Under what cloud and temperature conditions is SEVERE CLEAR ICE most likely to form on an aircraft?",
         "[A] Thin Cirrostratus at -40°C\n[B] CUMULIFORM clouds (Cu, Cb) with large supercooled droplets at temperatures between 0°C and -10°C\n[C] Fog at +5°C\n[D] Stratocumulus at -30°C",
         "CORRECT: [B]. Large supercooled droplets have high kinetic energy; upon impact, latent heat of fusion prevents instant freezing, allowing water to flow back and form solid, dense clear ice."),
        ("Q2: What atmospheric conditions are ESSENTIAL for the formation of marked MOUNTAIN WAVES?",
         "[A] Calm winds and thick fog\n[B] Wind blowing nearly PERPENDICULAR to the ridge at >= 20 knots, increasing with altitude, and a STABLE atmospheric layer over the crest\n[C] Intense thunderstorm activity\n[D] Strong tailwind on landing",
         "CORRECT: [B]. The stable layer acts as an elastic spring: air displaced over the ridge oscillates downstream, creating stationary gravity waves."),
        ("Q3: How does a small accumulation of frost on the wing surface affect aerodynamic performance during take-off?",
         "[A] Decreases stall speed\n[B] Increases drag and DECREASES MAXIMUM LIFT significantly (can cause premature stall on rotation)\n[C] Has zero effect\n[D] Increases ground roll friction only",
         "CORRECT: [B]. Frost acts like coarse sandpaper, tripping laminar airflow into turbulent flow early, dramatically reducing maximum lift coefficient Cl_max.")
    ]

    for q_text, opts, exp in questions_ch11:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 11 compiled: {pdf_path}")


def build_met_ch12():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch12_thunderstorms_microbursts_windshear.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 12: Thunderstorms & Microbursts")

    pdf.add_title_banner(
        "Meteorology",
        12,
        "Flight Hazards II: Thunderstorms & Microbursts",
        "399-438"
    )

    pdf.add_heading_1("1. The Thunderstorm (CB) Life Cycle")
    pdf.add_paragraph(
        "A thunderstorm requires: (1) High atmospheric instability, (2) Abundant moisture, and (3) A lifting trigger (thermal, frontal, or orographic):"
    )
    pdf.add_bullet("1. Cumulus Stage (Initial / Building)", "Purely UPDRAFTS (1,000 to 3,000 ft/min). Cloud grows vertically into a towering mass. No precipitation reaching ground.")
    pdf.add_bullet("2. Mature Stage (Peak Hazard)", "Marked by the ONSET OF PRECIPITATION at the surface! Updrafts (up to 6,000 ft/min) and downdrafts (up to 4,000 ft/min) coexist side-by-side. Severe turbulence, hail, lightning, microbursts. Duration: 20 to 30 minutes.")
    pdf.add_bullet("3. Dissipating Stage (Decay)", "DOWNDRAFTS PREDOMINATE throughout the cloud. The top freezes into a fibrous cirrus anvil (incus). Rain eases; cloud gradually dissipates.")

    pdf.add_heading_1("2. The Microburst Phenomenon")
    pdf.add_paragraph(
        "A microburst is an extremely concentrated, violent downdraft descending from a convective cloud:"
    )
    pdf.add_bullet("Dimensions & Strength", "Horizontal diameter < 4 km (2.2 NM). Downdraft speed can exceed 6,000 ft/min. Lifespan: 5 to 15 minutes.")
    pdf.add_bullet("Aviation Flight Path Impact", "An aircraft flying through a microburst encounters three rapid stages: (1) Severe HEADWIND increase (airspeed jumps, plane balloons above glide slope), (2) Severe DOWNBURST (vertical drop), and (3) Severe TAILWIND increase (airspeed plummets, catastrophic loss of lift and ground impact)!")

    pdf.add_heading_1("3. Airborne Weather Radar (AWR) Avoidance Rules")
    pdf.add_bullet("Lateral Avoidance Margins", "Avoid active CB cells by AT LEAST: 20 NAUTICAL MILES at or above FL 200; 10 NM below FL 200 (5 NM if temperature > 0°C).")
    pdf.add_bullet("Vertical Avoidance", "Avoid overflying an active CB by at least 1,000 ft for every 10 knots of wind speed at cloud top (or at least 5,000 ft above anvil)!")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch12 = [
        ("Q1: What meteorological event formally marks the transition from the Cumulus stage to the MATURE STAGE of a thunderstorm?",
         "[A] The first formation of an anvil\n[B] The ONSET OF PRECIPITATION reaching the ground and the appearance of downdrafts\n[C] Lightning seen in the distance\n[D] Cloud top reaching FL 100",
         "CORRECT: [B]. Friction from falling rain drops drags air down, creating the first downdraft and marking the start of the mature stage."),
        ("Q2: When penetrating an active MICROBURST on final approach, what is the initial indication observed in the cockpit?",
         "[A] Sudden severe loss of airspeed\n[B] A SUDDEN INCREASE IN HEADWIND causing an abrupt increase in indicated airspeed and pitch-up above the glide path\n[C] Stall warning\n[D] Altimeter drops to zero",
         "CORRECT: [B]. The outflow ring produces a headwind first, causing airspeed to jump. If the pilot reduces thrust, the subsequent downdraft and tailwind will cause an unrecoverable crash."),
        ("Q3: What is the recommended minimum lateral separation from an active Cumulonimbus (CB) cell at FL 250?",
         "[A] 5 NM\n[B] AT LEAST 20 NAUTICAL MILES\n[C] 2 NM\n[D] 1 NM",
         "CORRECT: [B]. At high flight levels (above FL 200), hail can be ejected miles outside the visible cloud column; 20 NM lateral clearance is standard airline SOP.")
    ]

    for q_text, opts, exp in questions_ch12:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 12 compiled: {pdf_path}")


def build_met_ch13():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch13_tropical_meteorology_climatology.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 13: Tropical Meteorology")

    pdf.add_title_banner(
        "Meteorology",
        13,
        "Tropical Meteorology, Revolving Storms & Climatology",
        "439-472"
    )

    pdf.add_heading_1("1. The Intertropical Convergence Zone (ITCZ)")
    pdf.add_paragraph(
        "The ITCZ is the equatorial meteorological trough where the Northeast Trade Winds of the Northern Hemisphere meet the Southeast Trade Winds of the Southern Hemisphere:"
    )
    pdf.add_bullet("Characteristics", "Intense solar heating causes broad-scale convergence and ascent, generating massive clusters of Cumulonimbus (CB) reaching FL 550 to FL 600. Known maritime name: The Doldrums.")
    pdf.add_bullet("Seasonal Migration", "Migrates north of the equator in Northern summer (July) and south in Northern winter (January). Migration is much greater over land masses (up to 25°N over Asia) than over oceans.")

    pdf.add_heading_1("2. Tropical Revolving Storms (TRS)")
    pdf.add_paragraph(
        "Severe tropical cyclones with warm cores and sustained winds >= 64 knots. Names: Hurricane (Atlantic/Eastern Pacific), Typhoon (Northwest Pacific), Cyclone (Indian Ocean/South Pacific):"
    )
    pdf.add_bullet("Mandatory Formation Conditions", "1. Warm ocean water with Sea Surface Temperature (SST) >= 26°C to 27°C down to 50 m depth; 2. Latitude between 5° and 20° (Coriolis force is too weak to create rotation between 0° and 5°!); 3. Low vertical wind shear (< 10 kt); 4. Pre-existing tropical disturbance.")
    pdf.add_bullet("TRS Anatomy", "The Eye: 10 to 30 NM diameter central core with calm/light winds, descending air (subsidence), clear skies; The Eyewall: Ring of ferocious towering CBs surrounding the eye with MAXIMUM SUSTAINED WINDS (100 to 180 kt) and torrential rain; Storm Surge: Coastal sea level rise responsible for 90% of casualties.")

    pdf.add_heading_1("3. The Asian Monsoons")
    pdf.add_bullet("Southwest Monsoon (Summer: June to Sept)", "Intense heating over Asia creates a deep continental heat low. Warm, moisture-laden maritime air from the Indian Ocean sweeps northeast across India, bringing torrential rainfall and continuous low cloud.")
    pdf.add_bullet("Northeast Monsoon (Winter: Dec to March)", "The massive Siberian High builds over cold Asia. Cool, dry continental air flows southwest towards the ocean, producing clear skies and dry weather.")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch13 = [
        ("Q1: Why do Tropical Revolving Storms (Hurricanes / Typhoons) NEVER form between latitudes 0° and 5° North or South of the Equator?",
         "[A] Ocean water is too cold\n[B] The CORIOLIS FORCE is too weak near the equator to initiate cyclonic rotation\n[C] Trade winds are too strong\n[D] Too many islands",
         "CORRECT: [B]. The Coriolis parameter is proportional to sin(latitude). At latitudes under 5°, Coriolis force is virtually zero, preventing air from spinning into a closed vortex."),
        ("Q2: What weather conditions exist inside the 'EYE' of a mature Tropical Revolving Storm?",
         "[A] Maximum hurricane-force winds\n[B] CALM OR LIGHT WINDS, descending air (subsidence), and relatively CLEAR SKIES surrounded by the towering eyewall\n[C] Continuous hail\n[D] Severe turbulence",
         "CORRECT: [B]. Sinking air in the central eye suppresses cloud formation, creating an eerie pocket of calm air surrounded by violent eyewall winds."),
        ("Q3: What causes the wet SOUTHWEST MONSOON over the Indian subcontinent between June and September?",
         "[A] Cold fronts from Antarctica\n[B] Intense summer solar heating forming a continental thermal low over Asia, drawing warm, moist maritime air from the Indian Ocean\n[C] High pressure over the Himalayas\n[D] Volcanic activity",
         "CORRECT: [B]. The Asian thermal low draws equatorial maritime air across the Arabian Sea and Bay of Bengal, unleashing the summer monsoon.")
    ]

    for q_text, opts, exp in questions_ch13:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 13 compiled: {pdf_path}")


def build_met_ch14():
    pdf_path = os.path.join(OUTPUT_DIR, "050_ch14_metar_taf_sigmet_charts.pdf")
    pdf = PDFBuilder("Meteorology", "050", "Chapter 14: METAR, TAF & SIGMET")

    pdf.add_title_banner(
        "Meteorology",
        14,
        "Meteorological Reports & Forecasts (METAR, TAF, SIGMET)",
        "473-510"
    )

    pdf.add_heading_1("1. METAR & SPECI Decoding Rules")
    pdf.add_paragraph(
        "METAR is an aerodrome routine meteorological report issued every 30 or 60 minutes. SPECI is a special report issued when weather deteriorates across critical thresholds:"
    )
    pdf.add_bullet("Wind Group", "e.g. 24015G28KT = Mean wind 240° True at 15 kt, gusting to 28 kt. 180V260 = Wind direction varying between 180° and 260°.")
    pdf.add_bullet("Visibility & RVR", "e.g. 1400 = Prevailing visibility 1,400 meters. R27/0800VP1500U = Runway 27 RVR varying from 800 m to greater than 1,500 m, with upward trend (U).")
    pdf.add_bullet("Present Weather Codes", "Descriptors: TS (Thunderstorm), FZ (Freezing), SH (Shower); Precipitation: DZ (Drizzle), RA (Rain), SN (Snow), GR (Hail >= 5 mm); Obscuration: FG (Fog), BR (Mist), HZ (Haze).")
    pdf.add_bullet("Cloud Coverage & Base", "FEW = 1-2 octas, SCT = 3-4 octas, BKN = 5-7 octas (CEILING!), OVC = 8 octas (CEILING!). Base given in hundreds of feet AGL (e.g. BKN015 = Broken at 1,500 ft AGL). Only CB and TCU cloud types are appended.")
    pdf.add_bullet("CAVOK Conditions (All 4 must be satisfied!)", "1. Visibility >= 10 km; 2. No cloud below 5,000 ft or Minimum Sector Altitude (MSA); 3. No CB or TCU; 4. No significant weather phenomena!")

    pdf.add_heading_1("2. TAF (Terminal Aerodrome Forecast)")
    pdf.add_bullet("Validity Periods", "Short TAF: 9 hours (issued every 3h). Long TAF: 24 to 30 hours (issued every 6h).")
    pdf.add_bullet("Change Groups", "BECMG: Gradual change over the specified time window. TEMPO: Temporary fluctuations lasting < 1 hour and covering < 50% of the period. FM (From): Rapid permanent change at the exact hour and minute.")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Complete METAR & TAF Flight Dispatch Decoding",
        "SCENARIO (EASA Flight Deck Dispatch Drill):\n"
        "A flight crew reviews the destination weather:\n"
        "METAR LEMD 121430Z 04018G32KT 010V080 3000 +SHRA SCT008 BKN018CB 14/11 Q1008 NOSIG=\n"
        "QUESTION: Decode all items in this METAR step-by-step for flight dispatch.\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Header -> LEMD (Madrid Barajas), 12th day of the month at 14:30 UTC.\n"
        "Step 2: Wind -> 04018G32KT = Mean wind 040° True at 18 knots, gusting to 32 knots!\n"
        "  - 010V080 = Wind direction is varying clockwise/counter-clockwise between 010° and 080°.\n"
        "Step 3: Visibility -> 3000 = Minimum prevailing visibility is 3,000 meters.\n"
        "Step 4: Weather -> +SHRA = HEAVY (+) SHOWERS (SH) OF RAIN (RA)!\n"
        "Step 5: Clouds:\n"
        "  - SCT008 = Scattered (3 to 4 octas) at 800 ft AGL (NOT a ceiling).\n"
        "  - BKN018CB = Broken (5 to 7 octas) at 1,800 ft AGL containing CUMULONIMBUS (CB)! This constitutes an official CEILING at 1,800 ft with severe convective hazards!\n"
        "Step 6: Temperatures -> 14/11 = Outside Air Temperature +14°C, Dew Point +11°C (narrow 3°C spread).\n"
        "Step 7: Pressure -> Q1008 = QNH is 1008 hPa.\n"
        "Step 8: Trend -> NOSIG = No significant change expected during the next 2 hours.\n\n"
        "FINAL ANSWER: Madrid has gusty winds to 32 kt, heavy rain showers, visibility 3 km, and CB cloud ceiling at 1,800 ft AGL.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Ceiling Definition Trap",
        "- By official ICAO definition, a 'CEILING' is the height above ground of the lowest layer of clouds covering MORE THAN HALF THE SKY:\n"
        "- BKN (5-7 octas) = CEILING.\n"
        "- OVC (8 octas) = CEILING.\n"
        "- FEW (1-2 octas) and SCT (3-4 octas) are NOT ceilings!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch14 = [
        ("Q1: Which of the following conditions MUST be met simultaneously for 'CAVOK' to be reported in a METAR?",
         "[A] Visibility 5,000 m and no low clouds\n[B] Visibility >= 10 km, NO CLOUD below 5,000 ft or MSA (whichever is higher), NO CB or TCU, and NO significant weather\n[C] Clear sky and zero wind\n[D] Zero fog",
         "CORRECT: [B]. CAVOK (Ceiling And Visibility OK) requires >= 10 km visibility, absence of clouds below 5,000 ft / MSA, no CB/TCU at any level, and no significant weather phenomena."),
        ("Q2: In aviation meteorology, which cloud coverage codes constitute an official 'CEILING'?",
         "[A] Only OVC (Overcast)\n[B] BROKEN (BKN: 5 to 7 octas) and OVERCAST (OVC: 8 octas)\n[C] SCT and BKN\n[D] FEW and SCT",
         "CORRECT: [B]. Under ICAO Annex 3, a cloud ceiling is defined as the height of the base of the lowest layer covering more than 4 octas (i.e. BKN or OVC)."),
        ("Q3: In a TAF forecast, what does the change indicator 'TEMPO 1216 2000' signify?",
         "[A] Permanent change to 2,000 m visibility from 12:00 to 16:00\n[B] TEMPORARY fluctuations to 2,000 meters visibility occurring between 12:00 UTC and 16:00 UTC, each lasting less than 1 hour and covering in aggregate less than half the period\n[C] Temperature will reach 20°C\n[D] Wind 200° at 16 kt",
         "CORRECT: [B]. TEMPO denotes temporary weather fluctuations lasting less than 60 minutes per instance and less than 50% of the total time window.")
    ]

    for q_text, opts, exp in questions_ch14:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Meteorology Chapter 14 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_met_ch11()
    build_met_ch12()
    build_met_ch13()
    build_met_ch14()
