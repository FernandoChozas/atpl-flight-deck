#!/usr/bin/env python3
"""
Generator for Subject 062: Radio Navigation & PBN
Volume 1: Chapters 1 to 4
- Chapter 1: Radio Wave Propagation, Antennas, Frequencies & Modulation
- Chapter 2: Non-Directional Beacon (NDB) & Automatic Direction Finder (ADF)
- Chapter 3: VHF Omnidirectional Range (VOR & Doppler DVOR) & Radials
- Chapter 4: Distance Measuring Equipment (DME) & Slant Range Geometry

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Radio Navigation and EASA ATPL ECQB syllabus.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/062_radio_navigation_pbn"

def build_rnav_ch01():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch01_radio_propagation_antennas.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 1: Radio Wave Propagation")

    pdf.add_title_banner(
        "Radio Navigation",
        1,
        "Radio Wave Propagation, Antennas & Frequencies",
        "1-44"
    )

    pdf.add_heading_1("1. The Electromagnetic Spectrum & Frequency Bands")
    pdf.add_paragraph(
        "Radio waves travel at the speed of light (c = 300,000 km/s = 3 x 10^8 m/s). Wavelength is inversely proportional to frequency: lambda (meters) = c / frequency (Hz):"
    )

    bands_table = [
        ["Frequency Band", "Frequency Range & Wavelength", "Aviation Navigational Aids & Communications"],
        ["VLF (Very Low)", "3 to 30 kHz (100 to 10 km)", "Submarine communications, Omega navigation (obsolete)."],
        ["LF (Low Frequency)", "30 to 300 kHz (10 to 1 km)", "NDB (Non-Directional Beacons), commercial AM radio."],
        ["MF (Medium Frequency)", "300 to 3,000 kHz (1 km to 100 m)", "NDB, Locator beacons, maritime radio."],
        ["HF (High Frequency)", "3 to 30 MHz (100 to 10 m)", "Long-range transoceanic voice communications (Sky wave)."],
        ["VHF (Very High)", "30 to 300 MHz (10 to 1 m)", "VHF Comms (118-137 MHz), VOR (108-118 MHz), ILS Localizer (108-112 MHz)."],
        ["UHF (Ultra High)", "300 to 3,000 MHz (1 m to 10 cm)", "ILS Glide Path (329-335 MHz), DME (960-1215 MHz), SSR (1030/1090 MHz), GPS L1 (1575 MHz)."],
        ["SHF (Super High)", "3 to 30 GHz (10 to 1 cm)", "Airborne Weather Radar (AWR 9.3 GHz), MLS (5 GHz), Radar Altimeter (4.3 GHz)."]
    ]
    pdf.add_table(["Frequency Band", "Frequency Range & Wavelength", "Aviation Navigational Aids & Communications"], bands_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_heading_1("2. Wave Propagation Modes & Maximum Range")
    pdf.add_bullet("Ground Wave (Surface Wave)", "Follows the curvature of the Earth. Dominant in LF and MF bands (NDB). Range is greatest over seawater (high conductivity) and lowest over dry sand/ice.")
    pdf.add_bullet("Sky Wave (Ionospheric Reflection)", "Reflected by ionosphere layers (D, E, F1, F2). Dominant in HF band. Subject to skip distance, skip zones, and severe night effect fading.")
    pdf.add_bullet("Space Wave (Line-of-Sight)", "Straight-line propagation in VHF, UHF, and SHF bands. Limited by atmospheric refraction and Earth curvature: Maximum Theoretical Range (NM) = 1.23 x (sqrt(h_transmitter) + sqrt(h_receiver)) [heights in feet]!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: VHF Maximum Line-of-Sight Radio Range",
        "SCENARIO (Fundamental AviationExam Question):\n"
        "An aircraft is cruising at FL 360 (36,000 ft).\n"
        "A VOR ground station antenna is located at an elevation of 900 ft MSL.\n"
        "QUESTION: What is the maximum theoretical range in Nautical Miles at which the aircraft can receive the VOR signal?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Identify Transmitter and Receiver Heights in feet:\n"
        "  - Aircraft Height (h_rx) = 36,000 ft\n"
        "  - VOR Ground Antenna Height (h_tx) = 900 ft\n\n"
        "Step 2: Recall the Master VHF Line-of-Sight Range Formula:\n"
        "  - Formula: Range (NM) = 1.23 x [ sqrt(h_tx) + sqrt(h_rx) ]\n\n"
        "Step 3: Calculate the square roots of each height:\n"
        "  - sqrt(900) = 30\n"
        "  - sqrt(36,000) = 189.74\n"
        "  - Sum of square roots = 30 + 189.74 = 219.74.\n\n"
        "Step 4: Multiply by the atmospheric refraction constant (1.23):\n"
        "  - Range (NM) = 1.23 x 219.74 = 270.28 NM (~270 Nautical Miles)!\n\n"
        "FINAL ANSWER: The maximum theoretical VOR reception range is approximately 270 Nautical Miles.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The 1.05 vs 1.23 Range Constant Trap",
        "- If both antennas are optical line-of-sight in a vacuum: constant = 1.05.\n"
        "- In the Earth's atmosphere, radio waves BEND SLIGHTLY downwards due to atmospheric refraction: constant = 1.23 (or 1.25)!\n"
        "- EASA exams universally use 1.23: Range = 1.23 x (sqrt(h1) + sqrt(h2)).",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: In which frequency band does the Instrument Landing System (ILS) LOCALIZER operate?",
         "[A] UHF\n[B] VHF (108.10 MHz to 111.95 MHz, odd tenths)\n[C] SHF\n[D] LF",
         "CORRECT: [B]. The ILS Localizer operates in the VHF band between 108.10 and 111.95 MHz on odd-tenth frequencies (e.g. 109.10, 109.30). The Glide Path operates in UHF."),
        ("Q2: Over which surface type does an LF/MF Ground Wave travel with the GREATEST range and minimum signal attenuation?",
         "[A] Dry desert sand\n[B] SEAWATER (due to high electrical conductivity)\n[C] Dense forest\n[D] Mountainous rocky terrain",
         "CORRECT: [B]. Seawater has the highest electrical conductivity of any natural Earth surface, producing minimum ground attenuation and maximum surface wave range."),
        ("Q3: What is the wavelength of a radar operating on a frequency of 10 GHz (10,000 MHz)?",
         "[A] 3 meters\n[B] 3 CENTIMETERS (lambda = 300,000,000 m/s / 10,000,000,000 Hz = 0.03 m = 3 cm)\n[C] 30 cm\n[D] 30 meters",
         "CORRECT: [B]. Formula: lambda = c / f. For 10 GHz: 3 x 10^8 / 10 x 10^9 = 0.03 m = 3 cm (standard Airborne Weather Radar X-band).")
    ]

    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 1 compiled: {pdf_path}")


def build_rnav_ch02():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch02_ndb_adf_principles_errors.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 2: NDB & ADF Navigation")

    pdf.add_title_banner(
        "Radio Navigation",
        2,
        "Non-Directional Beacon (NDB) & ADF Navigation",
        "45-88"
    )

    pdf.add_heading_1("1. NDB Ground Station & ADF Airborne Receiver")
    pdf.add_paragraph(
        "The NDB is an omnidirectional transmitter operating in the LF/MF bands (190 to 1750 kHz). The airborne receiver is the Automatic Direction Finder (ADF):"
    )
    pdf.add_bullet("Antenna Principle", "Uses a combined Loop Antenna (figure-8 reception pattern with two nulls) and Sense Antenna (circular pattern). Combining them produces a CARDIOID (heart-shaped) pattern with a single unique null, eliminating 180° ambiguity.")
    pdf.add_bullet("Relative Bearing (RB)", "The angle measured clockwise from the aircraft's nose to the station.")
    pdf.add_bullet("Magnetic Bearing TO Station (QDM)", "QDM = Magnetic Heading (MH) + Relative Bearing (RB) (If sum > 360°, subtract 360°!).")
    pdf.add_bullet("Magnetic Bearing FROM Station (QDR)", "QDR = QDM +- 180°.")

    pdf.add_heading_1("2. ADF Operational Errors & Limitations")
    pdf.add_bullet("Night Effect (The Biggest Hazard)", "At night (especially dawn/dusk), sky waves reflected by the ionosphere interfere with the ground wave. The ADF needle hunts, oscillates violently, or points 30° to 90° off course!")
    pdf.add_bullet("Coastal Refraction", "Radio waves travel faster over water than over land. When crossing a coastline obliquely, the wave bends TOWARDS THE COASTLINE NORMAL. The needle indicates the station is closer to the coast than it actually is!")
    pdf.add_bullet("Thunderstorm / Static Error", "Lightning discharges emit massive LF/MF radio noise. The ADF needle swings away from the NDB and POINTS DIRECTLY TOWARDS THE CUMULONIMBUS CLOUD!")
    pdf.add_bullet("Mountain Effect & Quadrantal Error", "Mountain reflections create false nulls. Quadrantal error is caused by aircraft metal bending the incoming wave (zero at nose, tail, and wingtips; maximum on quadrants: 045°, 135°, 225°, 315°).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating QDM and Intercepting NDB Inbound Radial",
        "SCENARIO (Classic AviationExam Navigation Problem):\n"
        "An aircraft is flying on Magnetic Heading (MH) = 040°:\n"
        "- The Relative Bearing Indicator (RBI) needle points to 220°\n"
        "ATC instructs: 'Intercept and track inbound on the 070° QDM to the NDB with a 30° intercept angle.'\n"
        "QUESTION 1: What is the current QDM and QDR?\n"
        "QUESTION 2: What heading should the pilot turn to intercept the 070° QDM at 30°?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate current QDM (Bearing TO the station):\n"
        "  - Formula: QDM = Magnetic Heading (MH) + Relative Bearing (RB)\n"
        "  - QDM = 040° + 220° = 260°!\n"
        "  - (QDR = 260° - 180° = 080° from the station).\n\n"
        "Step 2: Understand where you are relative to target QDM (070°):\n"
        "  - Current QDM = 260° (You are Southwest of the station, bearing 260° to it).\n"
        "  - Target QDM = 070° (You need to fly inbound towards 070°).\n\n"
        "Step 3: Calculate Intercept Heading (Inbound track 070° with 30° intercept):\n"
        "  - Target Track Inbound = 070°.\n"
        "  - You are on the right/south side of the desired track.\n"
        "  - Intercept Heading = Inbound Track - 30° = 070° - 30° = 040° Magnetic!\n\n"
        "FINAL ANSWER: Current QDM = 260°. Intercept heading = 040° Magnetic.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "QDM vs QDR Memory Trap",
        "- QDM = Bearing TO the station (Inbound track to fly in zero wind).\n"
        "- QDR = Bearing FROM the station (Radial outbound from station).\n"
        "- Always check if the question asks for QDM or QDR: QDR = QDM +- 180°!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: An aircraft is flying on a magnetic heading of 120°. The ADF needle points to relative bearing 080°. What is the QDM to the NDB?",
         "[A] 040°\n[B] 200° (QDM = MH + RB = 120° + 080° = 200°)\n[C] 020°\n[D] 300°",
         "CORRECT: [B]. Formula: QDM = MH + RB = 120° + 80° = 200° magnetic bearing to the station."),
        ("Q2: Why does the ADF suffer from severe 'NIGHT EFFECT' errors at dawn and dusk?",
         "[A] Cold air bends the wave\n[B] SKY WAVES reflected by the ionosphere interfere with the ground wave, causing needle hunting and wild bearing errors\n[C] Aircraft generators produce static\n[D] Moisture in the antenna",
         "CORRECT: [B]. At night and twilight, ionospheric reflection permits sky waves to reach the receiver with shifting polarization, degrading the loop antenna null."),
        ("Q3: When flying in the vicinity of active thunderstorm activity, what does an ADF needle tend to do?",
         "[A] Points to Magnetic North\n[B] POINTS TOWARDS THE LIGHTNING ELECTRICAL DISCHARGES in the Cumulonimbus cloud\n[C] Spins continuously at 100 rpm\n[D] Freezes at 000°",
         "CORRECT: [B]. Lightning creates powerful electromagnetic pulses in the LF/MF band, causing the ADF sense loop to track the storm cell rather than the NDB.")
    ]

    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 2 compiled: {pdf_path}")


def build_rnav_ch03():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch03_vor_dvor_principles_errors.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 3: VOR & Doppler DVOR")

    pdf.add_title_banner(
        "Radio Navigation",
        3,
        "VHF Omnidirectional Range (VOR) & Doppler DVOR",
        "89-130"
    )

    pdf.add_heading_1("1. VOR Operating Principle & Frequencies")
    pdf.add_paragraph(
        "VOR operates in the VHF band from 108.000 to 117.950 MHz (50 kHz channel spacing). It transmits 360 magnetic radials originating from the station:"
    )
    pdf.add_bullet("Phase Comparison Principle", "The VOR transmits two separate 30 Hz signals: (1) Reference Signal: 30 Hz FM omnidirectional pulse transmitted simultaneously in all directions; (2) Variable Signal: 30 Hz AM directional beam rotating clockwise at 30 revolutions per second (1,800 rpm).")
    pdf.add_bullet("Radial Determination", "The phase difference between the Reference and Variable signals EXACTLY EQUALS THE MAGNETIC BEARING (RADIAL) from the station! At Magnetic North (000°), the signals are in phase (0° phase difference); at 090° Radial, phase difference is 90°.")

    pdf.add_heading_1("2. Conventional VOR (CVOR) vs Doppler VOR (DVOR)")
    pdf.add_paragraph(
        "Conventional VOR suffers from site error caused by ground reflections (buildings, mountains, trees) producing 'scalloping' (needle oscillation) and course bends:"
    )
    pdf.add_bullet("Doppler VOR (DVOR) Superiority", "DVOR uses a wide-aperture circular antenna array (~13.5 m diameter, 50 antennas) simulating counter-clockwise rotation at 30 revs/sec. The simulated motion creates a 30 Hz FM Doppler shift. Because of the wide aperture, DVOR is VIRTUALLY IMMUNE TO SITE REFLECTION ERRORS!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Reading Course Deviation Indicator (CDI)",
        "SCENARIO (Standard EASA VOR Instrument Drill):\n"
        "An aircraft is flying on Magnetic Heading 360° (due North):\n"
        "- The pilot tunes the VOR and selects Omni-Bearing Selector (OBS) = 270°\n"
        "- The Course Deviation Indicator (CDI) needle deflects 3 DOTS TO THE RIGHT\n"
        "- The indicator displays a 'FROM' flag\n"
        "- Standard VOR CDI sensitivity: Full-scale deflection (5 dots) = 10° (2° per dot)\n"
        "QUESTION: On which radial is the aircraft currently located?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Determine the Angular Displacement from the needle deflection:\n"
        "  - Needle is deflected 3 dots to the RIGHT.\n"
        "  - Rule: 1 dot = 2.0 degrees.\n"
        "  - Displacement = 3 dots x 2.0°/dot = 6.0° off course.\n\n"
        "Step 2: Understand the CDI with a 'FROM' Flag:\n"
        "  - With a FROM flag and OBS selected to 270°:\n"
        "  - Center needle = You are on Radial 270°.\n"
        "  - Needle deflected RIGHT = The selected radial (270°) is to your RIGHT.\n"
        "  - Therefore, your current position is to the LEFT of Radial 270°!\n"
        "  - (Remember: On a compass rose, moving left/counter-clockwise from 270° means LOWER numbers: 270° - 6° = 264°).\n\n"
        "Step 3: State the Current Aircraft Radial:\n"
        "  - Current Radial = 270° - 6° = Radial 264°!\n\n"
        "FINAL ANSWER: The aircraft is located on Radial 264° from the VOR station.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Reverse Sensing VOR Trap",
        "- If you fly TOWARDS a VOR with a FROM flag selected:\n"
        "- The CDI gives REVERSE SENSING (if the needle is left, the track is to your right)!\n"
        "- To prevent reverse sensing: When flying inbound, ALWAYS select the inbound course with a TO flag!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: What is the phase relationship between the reference signal and variable signal of a VOR on Radial 090°?",
         "[A] In phase (0°)\n[B] The variable signal lags the reference signal by EXACTLY 90 DEGREES\n[C] 180° out of phase\n[D] 270°",
         "CORRECT: [B]. The phase difference between the reference and variable 30 Hz signals matches the radial angle from magnetic north: on radial 090°, phase difference is 90°."),
        ("Q2: Why is a Doppler VOR (DVOR) significantly more accurate than a Conventional VOR (CVOR) in mountainous terrain?",
         "[A] It uses UHF frequencies\n[B] Its wide-aperture simulated rotating antenna array greatly REDUCES SITE AND REFLECTION ERRORS (scalloping)\n[C] It uses satellite links\n[D] It has higher transmitter power",
         "CORRECT: [B]. DVOR's 13.5 m wide aperture antenna array creates a signal that is remarkably resilient against terrain and building multipath reflections."),
        ("Q3: On a standard VOR Course Deviation Indicator (CDI), what angular displacement is represented by FULL SCALE deflection (5 dots)?",
         "[A] 5°\n[B] 10 DEGREES (2.0° per dot)\n[C] 2.5°\n[D] 20°",
         "CORRECT: [B]. Standard VOR CDI sensitivity is 2.0° per dot, meaning full-scale 5-dot deflection represents a 10° angular displacement off track.")
    ]

    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 3 compiled: {pdf_path}")


def build_rnav_ch04():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch04_dme_principles_slant_range.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 4: DME & Slant Range")

    pdf.add_title_banner(
        "Radio Navigation",
        4,
        "Distance Measuring Equipment & Slant Range Geometry",
        "131-168"
    )

    pdf.add_heading_1("1. DME Operating Principles & UHF Frequencies")
    pdf.add_paragraph(
        "DME operates in the UHF band from 960 to 1215 MHz (1 MHz spacing). It is a secondary radar system measuring line-of-sight distance:"
    )
    pdf.add_bullet("Pulse Pair Interrogation", "Airborne interrogator transmits pulse pairs (12 microsecond spacing). Ground transponder receives them, delays reply by exactly 50 microseconds, and re-transmits on a frequency offset by +-63 MHz.")
    pdf.add_bullet("Slant Range Formula", "Total Elapsed Time = Round-trip propagation time + 50 microsecond transponder delay. Distance (NM) = (Elapsed Time - 50 microsec) / 12.36 microseconds (since radio waves travel 1 NM round-trip in 12.36 microseconds).")
    pdf.add_bullet("Capacity & Saturation", "A DME ground beacon can handle up to 100 AIRCRAFT SIMULTANEOUSLY. If overloaded, it reduces receiver sensitivity, cutting off weaker (distant) interrogators.")

    pdf.add_heading_1("2. Slant Range Error (Overhead Geometry)")
    pdf.add_paragraph(
        "DME measures direct line-of-sight hypotenuse distance (Slant Range), NOT horizontal ground distance:"
    )
    pdf.add_bullet("The Pythagoras Geometry", "Ground Distance = sqrt( Slant Range^2 - Height^2 ) [Height in NM: Height (NM) = Altitude in feet / 6,076 ft].")
    pdf.add_bullet("Overhead Station Indication", "When passing DIRECTLY OVERHEAD the DME station, Ground Distance is ZERO, but the DME indicates the aircraft's ALTITUDE ABOVE THE STATION IN NAUTICAL MILES (e.g. at FL 360, DME reads 6.0 NM overhead!)")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating True Ground Distance from DME Slant Range",
        "SCENARIO (Standard EASA DME Geometry Problem):\n"
        "An airliner is descending at FL 240 (24,000 ft above a sea-level DME station):\n"
        "- The cockpit DME indicator reads 5.0 NM\n"
        "QUESTION: What is the aircraft's actual HORIZONTAL GROUND DISTANCE from the station?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Convert Aircraft Height from feet into Nautical Miles:\n"
        "  - Rule: 1 Nautical Mile = approx 6,000 feet (exact 6,076 ft).\n"
        "  - Height (NM) = 24,000 ft / 6,000 ft = 4.0 NM!\n\n"
        "Step 2: Draw the Right-Angled Triangle:\n"
        "  - Hypotenuse (DME Slant Range) = 5.0 NM\n"
        "  - Vertical leg (Height) = 4.0 NM\n"
        "  - Horizontal leg (Ground Distance) = ?\n\n"
        "Step 3: Apply Pythagoras' Theorem (A^2 + B^2 = C^2):\n"
        "  - Ground Distance = sqrt( Slant Range^2 - Height^2 )\n"
        "  - Ground Distance = sqrt( 5.0^2 - 4.0^2 ) = sqrt( 25.0 - 16.0 ) = sqrt( 9.0 ) = 3.0 NM!\n\n"
        "FINAL ANSWER: The actual horizontal ground distance to the station is ONLY 3.0 Nautical Miles (even though the DME reads 5.0 NM!).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Slant Range Error Vanishes at Distance Trap",
        "- When Slant Range is greater than 10 times the height (e.g. 40 NM range at 4 NM height):\n"
        "- Slant range error is less than 0.5% (negligible)!\n"
        "- Slant range error is ONLY dangerous close to or directly overhead the station.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: What will a DME indicator read when an aircraft is flying directly overhead a sea-level DME beacon at FL 360?",
         "[A] Exactly 0.0 NM\n[B] APPROXIMATELY 6.0 NM (36,000 ft / 6,000 ft/NM = 6.0 NM slant range)\n[C] 36 NM\n[D] The indicator displays dashes",
         "CORRECT: [B]. Because DME measures line-of-sight distance, passing overhead produces a reading equal to the aircraft's vertical altitude in Nautical Miles: 36,000 / 6,000 = 6.0 NM."),
        ("Q2: In which frequency band does Distance Measuring Equipment (DME) operate?",
         "[A] VHF\n[B] UHF (960 to 1215 MHz)\n[C] SHF\n[D] HF",
         "CORRECT: [B]. DME operates in the UHF band, paired with VOR channels so tuning the VOR frequency automatically tunes the DME interrogator."),
        ("Q3: What is the maximum number of aircraft that a standard DME ground transponder can track simultaneously before saturation?",
         "[A] Unlimited\n[B] APPROXIMATELY 100 AIRCRAFT\n[C] 25 aircraft\n[D] 500 aircraft",
         "CORRECT: [B]. DME ground transponders are designed to handle up to 100 aircraft interrogations simultaneously by limiting pulse reply rates to ~2,700 pulse pairs per second.")
    ]

    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 4 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_rnav_ch01()
    build_rnav_ch02()
    build_rnav_ch03()
    build_rnav_ch04()
