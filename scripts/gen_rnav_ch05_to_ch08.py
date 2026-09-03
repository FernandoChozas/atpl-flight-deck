#!/usr/bin/env python3
"""
Generator for Subject 062: Radio Navigation & PBN
Volume 2: Chapters 5 to 8
- Chapter 5: Instrument Landing System (ILS: Localizer, Glide Path & Markers)
- Chapter 6: Microwave Landing System (MLS) & Satellite Landing (GLS/SBAS)
- Chapter 7: Primary Pulse Radar Principles & Airborne Weather Radar (AWR)
- Chapter 8: Secondary Surveillance Radar (SSR), Transponders, Mode S & ADS-B

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Radio Navigation and EASA ATPL ECQB syllabus.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/062_radio_navigation_pbn"

def build_rnav_ch05():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch05_ils_localizer_glide_path.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 5: ILS Localizer & Glide Path")

    pdf.add_title_banner(
        "Radio Navigation",
        5,
        "Instrument Landing System (ILS: LOC, GP & Markers)",
        "169-216"
    )

    pdf.add_heading_1("1. The ILS Tri-Component Architecture")
    pdf.add_paragraph(
        "The Instrument Landing System provides precision lateral, vertical, and distance guidance during final approach:"
    )

    ils_table = [
        ["ILS Subsystem", "Frequency Band & Modulation Carrier", "Beam Dimensions & Guaranteed Coverage"],
        ["Localizer (LOC)", "VHF (108.10 to 111.95 MHz, odd tenths). 90 Hz (Left) / 150 Hz (Right) DDM.", "Course width: ~5° (total 350 ft at threshold). Coverage: 35° each side to 17 NM; 10° each side to 25 NM."],
        ["Glide Path (GP)", "UHF (329.15 to 335.00 MHz, paired with LOC). 90 Hz (Above) / 150 Hz (Below) DDM.", "Slope: Standard 3.0°. Beam thickness: ~1.4° (0.7° above/below). Coverage: 8° each side to 10 NM. False slopes at 6° and 9°!"],
        ["Marker Beacons", "VHF 75.0 MHz (vertical fan beam).", "Outer (OM: 400 Hz, blue dashes, 4-7 NM); Middle (MM: 1300 Hz, amber dot-dashes, 0.5-0.8 NM); Inner (IM: 3000 Hz, white dots)."]
    ]
    pdf.add_table(["ILS Subsystem", "Frequency Band & Modulation Carrier", "Beam Dimensions & Guaranteed Coverage"], ils_table, col_widths=[115.0, 195.0, 190.0])

    pdf.add_heading_1("2. Glide Path Rate of Descent (ROD) Formula")
    pdf.add_bullet("Master ROD Formula (3.0° Glide Path)", "Rate of Descent (ft/min) = Groundspeed (knots) x 5 (e.g. at 140 kt GS: ROD = 140 x 5 = 700 ft/min!).")
    pdf.add_bullet("Non-Standard Slope Formula", "ROD (ft/min) = Groundspeed (knots) x Glide Angle (degrees) x 100 / 60.")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Target Rate of Descent on ILS",
        "SCENARIO (Everyday Airline Flying Drill):\n"
        "An airliner is established on an ILS approach with a 3.0° glide slope:\n"
        "- Target approach speed (Vref) = 140 knots Indicated Airspeed\n"
        "- Headwind component on final approach = 20 knots\n"
        "QUESTION: What target Rate of Descent (ft/min) must the flight crew maintain on the vertical speed indicator (VSI)?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Groundspeed (GS):\n"
        "  - Remember: Rate of descent depends on GROUNDSPEED, not airspeed!\n"
        "  - Groundspeed = TAS - Headwind\n"
        "  - At sea level, TAS ~ IAS = 140 kt.\n"
        "  - Groundspeed = 140 kt - 20 kt = 120 knots!\n\n"
        "Step 2: Recall the Master 3.0° Glide Path Formula:\n"
        "  - Rate of Descent (ft/min) = Groundspeed (kt) x 5!\n\n"
        "Step 3: Calculate Target ROD:\n"
        "  - ROD = 120 knots x 5 = 600 ft/min!\n\n"
        "FINAL ANSWER: Target Rate of Descent is 600 ft/min. If headwind decreases, groundspeed rises and ROD must increase proportionally.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "False Glide Path Trap",
        "- False glide paths are generated at HARMONIC MULTIPLES (typically 2 x 3° = 6°, and 3 x 3° = 9°)!\n"
        "- The first false glide path at 6° has NORMAL SENSING (90 Hz above, 150 Hz below)!\n"
        "- If intercepted from above, you will descend at double the normal rate (1,400 ft/min)!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: At what angle does the lowest FALSE GLIDE PATH occur on a standard 3.0° ILS installation?",
         "[A] 4.5°\n[B] At DOUBLE the nominal glide path angle: 6.0 DEGREES\n[C] 9.0°\n[D] 1.5°",
         "CORRECT: [B]. False glide paths occur at multiples of the true angle; the lowest false path is at twice the true slope (2 x 3° = 6°)."),
        ("Q2: In which frequency band does the ILS GLIDE PATH transmitter operate?",
         "[A] VHF\n[B] UHF (329.15 to 335.00 MHz)\n[C] SHF\n[D] LF",
         "CORRECT: [B]. The Glide Path operates in the UHF band, while the Localizer operates in the VHF band."),
        ("Q3: What is the audio modulation frequency and visual color of the ILS OUTER MARKER (OM)?",
         "[A] 1300 Hz amber\n[B] 400 HZ with BLUE light flashing dashes (two per second)\n[C] 3000 Hz white\n[D] Continuous tone red",
         "CORRECT: [B]. The Outer Marker is identified by a 400 Hz tone keyed as low-pitched dashes with a flashing blue light.")
    ]

    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 5 compiled: {pdf_path}")


def build_rnav_ch06():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch06_mls_gls_sbas_landing.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 6: MLS & Satellite Landing")

    pdf.add_title_banner(
        "Radio Navigation",
        6,
        "Microwave Landing System (MLS) & GLS/SBAS",
        "217-252"
    )

    pdf.add_heading_1("1. Microwave Landing System (MLS)")
    pdf.add_paragraph(
        "MLS was developed to overcome ILS frequency saturation and multipath limitations. It operates in the SHF (C-band) from 5030 to 5091 MHz (200 channels):"
    )
    pdf.add_bullet("Time-Referenced Scanning Beam (TRSB)", "A narrow beam sweeps back-and-forth across the coverage sector (TO and FRO scan). The time interval between the TO and FRO beam pulses received by the aircraft directly indicates azimuth and elevation angles!")
    pdf.add_bullet("Operational Capabilities", "Azimuth coverage: +-40° (up to +-60°); Elevation: 0.9° to 15°; Range: 20 NM. Enables CURVED AND SEGMENTED APPROACHES for noise abatement and terrain clearance.")

    pdf.add_heading_1("2. Satellite-Based Landing Systems (GLS / GBAS)")
    pdf.add_paragraph(
        "The Ground-Based Augmentation System (GBAS) provides differential GPS corrections enabling GLS (GBAS Landing System) Cat I, II, and III precision approaches:"
    )
    pdf.add_bullet("How GLS Works", "4 reference GPS receivers on the airport measure satellite pseudo-range errors. A ground station calculates corrections and broadcasts them along with Final Approach Segment Data Blocks (FASB) over a VHF Data Broadcast (VDB, 108-118 MHz).")
    pdf.add_bullet("Pilot Interface", "The pilot selects a 5-digit channel number on the nav control panel. The cockpit display is identical to ILS, but with pinpoint differential accuracy and zero beam scalloping!")

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: In which frequency band does the Microwave Landing System (MLS) operate?",
         "[A] UHF\n[B] SHF (C-Band: 5030 MHz to 5091 MHz)\n[C] VHF\n[D] EHF",
         "CORRECT: [B]. MLS operates in the SHF C-band, rendering it immune to low-frequency site reflections and FM radio interference."),
        ("Q2: What is the primary operational advantage of MLS over conventional ILS?",
         "[A] Lower cost\n[B] Wide-angle proportional coverage permitting CURVED AND SEGMENTED APPROACH PATHS with variable glide slope angles\n[C] Operates without electricity\n[D] Long-range en route guidance",
         "CORRECT: [B]. MLS provides wide azimuth (+-40°) and elevation coverage, allowing aircraft to fly curved noise-abatement profiles down to touchdown."),
        ("Q3: In a GBAS Landing System (GLS), how are the ground differential corrections transmitted to the aircraft?",
         "[A] Via satellite phone\n[B] Via a VHF DATA BROADCAST (VDB) in the 108.000 to 117.975 MHz band\n[C] Via HF sky wave\n[D] Via primary radar",
         "CORRECT: [B]. The GBAS ground station broadcasts corrections via an omnidirectional VHF Data Broadcast antenna at the airport.")
    ]

    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 6 compiled: {pdf_path}")


def build_rnav_ch07():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch07_primary_radar_weather_radar.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 7: Primary & Weather Radar")

    pdf.add_title_banner(
        "Radio Navigation",
        7,
        "Primary Pulse Radar & Airborne Weather Radar (AWR)",
        "253-296"
    )

    pdf.add_heading_1("1. Primary Radar Equations & Principles")
    pdf.add_paragraph(
        "Primary radar relies on the reflection of transmitted radio frequency pulses by a target:"
    )
    pdf.add_bullet("Pulse Recurrence Frequency (PRF)", "Number of pulses transmitted per second. Maximum Unambiguous Range: R_max = c / (2 x PRF). E.g. PRF = 500 Hz -> R_max = 300,000 / 1,000 = 300 km.")
    pdf.add_bullet("Pulse Length (tau)", "Duration of the pulse (microseconds). Minimum Blind Range: R_min = (c x tau) / 2. Range Resolution = (c x tau) / 2.")
    pdf.add_bullet("Beam Width & Angular Resolution", "Beam Width = (70 x lambda) / Antenna Diameter. Angular resolution improves with a larger antenna and shorter wavelength!")

    pdf.add_heading_1("2. Airborne Weather Radar (AWR) Operations")
    pdf.add_paragraph(
        "AWR operates in the SHF X-band at ~9,375 MHz (wavelength lambda = 3.2 cm), calibrated to reflect off wet precipitation droplets:"
    )
    pdf.add_bullet("Color Coding", "Green (Light rain), Yellow (Moderate rain), Red (Heavy rain / CB core), Magenta (Severe turbulence detected by Doppler shift).")
    pdf.add_bullet("Radar Shadow (Attenuation)", "A massive storm cell completely absorbs the radar beam. Behind the red core, a black shadow appears on the display. NEVER FLY INTO A RADAR SHADOW: A lethal second storm is hiding inside!")
    pdf.add_bullet("Tilt Formula", "Antenna Tilt (degrees) = (Height Difference in feet / Distance in NM x 100) - (Beam Width / 2).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating AWR Antenna Tilt Setting",
        "SCENARIO (Weather Radar Tilt Drill):\n"
        "An airliner is cruising at FL 330 (33,000 ft):\n"
        "- A severe storm cell is detected 40 NM ahead\n"
        "- The freezing level (cloud base of hazard) is at 13,000 ft MSL\n"
        "- The radar antenna has a 4.0° beam width\n"
        "QUESTION: What antenna TILT angle must the pilot select so the BOTTOM of the radar beam sweeps through the 13,000 ft level at 40 NM?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Height Difference between aircraft and target level:\n"
        "  - Aircraft Altitude = 33,000 ft\n"
        "  - Target Altitude = 13,000 ft\n"
        "  - Height Difference = 33,000 ft - 13,000 ft = 20,000 ft (target is BELOW aircraft).\n\n"
        "Step 2: Calculate the Depression Angle (degrees) to the target level:\n"
        "  - Rule of Thumb: 1° = 100 ft per Nautical Mile!\n"
        "  - Depression Angle = Height Difference / (Distance x 100)\n"
        "  - Depression Angle = 20,000 ft / (40 NM x 100) = 20,000 / 4,000 = 5.0° DOWN (-5.0°).\n\n"
        "Step 3: Adjust for Half the Beam Width (Beam Width = 4.0°):\n"
        "  - Beam Width / 2 = 4.0° / 2 = 2.0°.\n"
        "  - To place the BOTTOM of the beam at the target, the center of the beam must aim 2.0° HIGHER:\n"
        "  - Tilt Setting = Depression Angle + Half Beam Width = -5.0° + 2.0° = -3.0° (3° DOWN)!\n\n"
        "FINAL ANSWER: Set antenna tilt to -3.0° DOWN.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Radar Shadow Trap",
        "- If a storm displays a deep black notch or blind zone directly behind a red cell:\n"
        "- That black area is NOT clear air! It is a RADAR SHADOW caused by beam attenuation!\n"
        "- Flying into a radar shadow is one of the most fatal thunderstorm traps in aviation.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: What wavelength is used by standard Airborne Weather Radar (AWR) systems operating in the X-band?",
         "[A] 10 meters\n[B] APPROXIMATELY 3.2 CENTIMETERS (frequency ~9,375 MHz)\n[C] 10 cm\n[D] 1 mm",
         "CORRECT: [B]. The 3 cm X-band provides optimal reflectivity from liquid raindrops while maintaining an antenna dish size that fits within an aircraft nose radome."),
        ("Q2: On an Airborne Weather Radar display, what does a completely BLACK area situated immediately behind an intense RED return indicate?",
         "[A] A cloud-free valley\n[B] A RADAR SHADOW caused by heavy rain completely absorbing and attenuating the radar beam\n[C] Safe flying zone\n[D] Ground return",
         "CORRECT: [B]. The radar pulse cannot penetrate through dense water cores, creating a blind shadow where severe convective storms remain hidden."),
        ("Q3: What radar parameter determines the MINIMUM BLIND RANGE of a primary pulse radar?",
         "[A] Antenna rotation speed\n[B] PULSE LENGTH (tau) (the receiver cannot receive while the transmitter is transmitting)\n[C] PRF only\n[D] Wavelength",
         "CORRECT: [B]. During pulse transmission (pulse duration tau), the receiver is disconnected to prevent damage: R_min = (c x tau) / 2.")
    ]

    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 7 compiled: {pdf_path}")


def build_rnav_ch08():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch08_ssr_transponders_mode_s_adsb.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 8: SSR, Mode S & ADS-B")

    pdf.add_title_banner(
        "Radio Navigation",
        8,
        "Secondary Surveillance Radar, Mode S & ADS-B",
        "297-340"
    )

    pdf.add_heading_1("1. Secondary Surveillance Radar (SSR) Principles")
    pdf.add_paragraph(
        "Unlike primary radar which depends on passive echoes, SSR relies on active cooperation between ground interrogator and aircraft transponder:"
    )
    pdf.add_bullet("Frequencies", "Interrogation uplink = 1030 MHz (UHF). Transponder reply downlink = 1090 MHz (UHF). (Separate frequencies completely eliminate ground clutter and weather reflections!).")
    pdf.add_bullet("Mode A (Identity)", "4-digit octal code (0000 to 7777, 4,096 combinations). Special Emergency Squawks: 7700 (General Emergency / Mayday), 7600 (Radio Communications Failure), 7500 (Unlawful Interference / Hijacking!).")
    pdf.add_bullet("Mode C (Pressure Altitude)", "Automatically encodes pressure altitude referenced to 1013.25 hPa in 100 ft increments (Gillham code). (Always reports standard pressure altitude, regardless of cockpit altimeter subscale setting!).")

    pdf.add_heading_1("2. Mode S Transponder & ADS-B Out")
    pdf.add_paragraph(
        "Mode S provides selective interrogation and high-capacity data link communication:"
    )
    pdf.add_bullet("Unique 24-Bit ICAO Address", "Over 16 million unique aircraft addresses permanently assigned to the airframe registration. Eliminates identity confusion.")
    pdf.add_bullet("Altitude Resolution", "Reports altitude in 25 ft increments (compared to 100 ft in Mode C).")
    pdf.add_bullet("ADS-B Out (Automatic Dependent Surveillance-Broadcast)", "The transponder automatically broadcasts aircraft GPS position, velocity, and intent over the 1090 MHz Extended Squitter once per second without requiring ground interrogation.")

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: What are the uplink (interrogation) and downlink (reply) frequencies used by Secondary Surveillance Radar (SSR)?",
         "[A] 108 MHz and 118 MHz\n[B] 1030 MHz uplink and 1090 MHz downlink\n[C] 960 MHz and 1215 MHz\n[D] 5 GHz",
         "CORRECT: [B]. By international standard, SSR interrogates on 1030 MHz and transponders reply on 1090 MHz."),
        ("Q2: When a transponder transmits MODE C altitude information to ATC, to what barometric pressure datum is this altitude referenced?",
         "[A] Local aerodrome QNH\n[B] STANDARD 1013.25 hPa (permanently, regardless of the subscale set on the altimeter)\n[C] Aerodrome QFE\n[D] Zero pressure",
         "CORRECT: [B]. Mode C reports uncorrected pressure altitude referenced strictly to standard 1013.25 hPa. Ground ATC radar computers convert this to indicated altitude using local QNH."),
        ("Q3: Which transponder squawk code MUST a pilot select immediately following a complete loss of two-way radio communications?",
         "[A] 7500\n[B] 7600\n[C] 7700\n[D] 2000",
         "CORRECT: [B]. Emergency transponder codes: 7700 = Emergency; 7600 = Radio Communications Failure; 7500 = Hijack / Unlawful Interference.")
    ]

    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 8 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_rnav_ch05()
    build_rnav_ch06()
    build_rnav_ch07()
    build_rnav_ch08()
