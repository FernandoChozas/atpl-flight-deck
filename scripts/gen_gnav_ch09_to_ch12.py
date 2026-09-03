#!/usr/bin/env python3
"""
Generator for Subject 061: General Navigation
Volume 3: Chapters 9 to 12
- Chapter 9: Dead Reckoning (DR) Navigation & Flight Computer Principles
- Chapter 10: In-Flight Navigation & The 1-in-60 Rule (Track Error & Closing Angle)
- Chapter 11: Time Systems: UTC, LMT, Zone Time, Equation of Time & Twilight
- Chapter 12: Inertial Reference Systems (IRS/INS): Schuler Tuning & Triple Mix

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford General Navigation and EASA ATPL ECQB syllabus.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/061_general_navigation"

def build_gnav_ch09():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch09_dead_reckoning_flight_computer.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 9: DR & Flight Computer")

    pdf.add_title_banner(
        "General Navigation",
        9,
        "Dead Reckoning & Flight Computer Principles (CRP-5)",
        "325-364"
    )

    pdf.add_heading_1("1. Dead Reckoning (DR) Fundamentals")
    pdf.add_paragraph(
        "Dead Reckoning is the navigation method of calculating current and future aircraft position from a previously known position using heading, airspeed, wind, and elapsed time:"
    )
    pdf.add_bullet("The Navigation Vector Triangle", "Heading Vector (True Heading + TAS) + Wind Vector (Wind Direction + Wind Speed) = Track Vector (True Track + Groundspeed).")
    pdf.add_bullet("The CRP-5 / E6B Slide Rule", "Circular slide rule solving: 1. Time-Speed-Distance (Time = Dist / GS); 2. Fuel consumption (Burn = Time x Fuel Flow); 3. TAS from Calibrated Airspeed (CAS), Pressure Altitude, and Temperature (correcting for density error and compressibility).")

    pdf.add_heading_1("2. True Airspeed (TAS) vs Indicated Airspeed (IAS)")
    pdf.add_bullet("Rule of Thumb", "TAS INCREASES by approximately 1.5% to 2.0% per 1,000 ft of altitude above sea level for a given Indicated Airspeed!")
    pdf.add_bullet("Mach Number & Temperature", "Mach = TAS / Speed of Sound (a). Speed of Sound depends SOLELY on Absolute Temperature (Kelvin): a = 38.94 x sqrt(T_K) knots. In colder air, sound travels slower!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Estimating TAS from IAS and Altitude",
        "SCENARIO (Basic Navigation Rule of Thumb Drill):\n"
        "An aircraft climbs to FL 100 (10,000 ft):\n"
        "- Indicated Airspeed (IAS / CAS) = 150 knots\n"
        "- Outside Air Temperature is standard ISA (+15°C - 20°C = -5°C)\n"
        "QUESTION: What is the approximate True Airspeed (TAS)?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Recall the standard rule of thumb for TAS increase with altitude:\n"
        "  - Rule: Add 2% to IAS per 1,000 ft of altitude!\n\n"
        "Step 2: Calculate the total percentage increase for 10,000 ft:\n"
        "  - Altitude = 10,000 ft = 10 x 1,000 ft.\n"
        "  - Total percentage increase = 10 x 2% = +20%!\n\n"
        "Step 3: Calculate the knots to add to IAS:\n"
        "  - 20% of 150 knots = 0.20 x 150 kt = 30 knots.\n\n"
        "Step 4: Add the increase to the IAS:\n"
        "  - TAS = IAS + Increase = 150 kt + 30 kt = 180 knots!\n\n"
        "FINAL ANSWER: True Airspeed (TAS) is approximately 180 knots (a 30 knot gain over indicated speed due to lower air density at 10,000 ft).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Speed of Sound Depends Only on Temperature Trap",
        "- The Speed of Sound DOES NOT depend on pressure or air density!\n"
        "- It depends SOLELY on absolute temperature: a = 38.94 x sqrt(T_Kelvin)!\n"
        "- Exam questions asking if sound speed changes with pressure are traps: the answer is NO, only temperature matters!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch09 = [
        ("Q1: What is the primary physical reason why True Airspeed (TAS) is greater than Indicated Airspeed (IAS) at high altitude?",
         "[A] Engine develops more thrust\n[B] Air density DECREASES with altitude, requiring the aircraft to travel faster through the thin air to produce the same dynamic pressure (q = 0.5 rho V^2)\n[C] Less gravity\n[D] Instrument error",
         "CORRECT: [B]. The ASI measures dynamic impact pressure. At lower density, the aircraft must fly faster to register the same indicated pressure."),
        ("Q2: On which single atmospheric parameter does the local SPEED OF SOUND depend?",
         "[A] Atmospheric pressure\n[B] ABSOLUTE TEMPERATURE (in Kelvin)\n[C] Air density only\n[D] Wind speed",
         "CORRECT: [B]. In a perfect gas, sound speed is given by a = sqrt(gamma x R x T). Only absolute temperature T affects sound velocity."),
        ("Q3: If an aircraft is cruising at FL 300 with an IAS of 240 kt in standard ISA conditions (-45°C), what is the approximate TAS using the 2% rule of thumb?",
         "[A] 300 kt\n[B] Approx 384 kt (240 kt + 60% = 384 kt)\n[C] 240 kt\n[D] 450 kt",
         "CORRECT: [B]. 30,000 ft x 2% / 1,000 ft = +60%. 240 x 1.60 = 384 knots TAS.")
    ]

    for q_text, opts, exp in questions_ch09:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 9 compiled: {pdf_path}")


def build_gnav_ch10():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch10_inflight_navigation_1in60_rule.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 10: In-Flight Nav & 1-in-60")

    pdf.add_title_banner(
        "General Navigation",
        10,
        "In-Flight Navigation & The 1-in-60 Rule",
        "365-408"
    )

    pdf.add_heading_1("1. The Geometry of the 1-in-60 Rule")
    pdf.add_paragraph(
        "The 1-in-60 rule is an empirical trigonometric approximation: An angular displacement of 1 DEGREE produces an off-track distance of exactly 1 NAUTICAL MILE after flying 60 NAUTICAL MILES (tan 1° ~ 1/60):"
    )
    pdf.add_bullet("Track Error Angle (TE)", "The angular divergence between the planned track and the actual track flown so far: Track Error (degrees) = (Distance Off Track / Distance Gone) x 60.")
    pdf.add_bullet("Closing Angle (CA)", "The additional angle required to intercept the next planned waypoint: Closing Angle (degrees) = (Distance Off Track / Distance to Go) x 60.")
    pdf.add_bullet("Heading Alteration (To fly DIRECT to next waypoint)", "Alteration of Heading = Track Error + Closing Angle (Change Heading = TE + CA). (If you only correct by TE, you will fly parallel to the track but never regain it!).")

    pdf.add_heading_1("2. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Correcting Heading In-Flight using 1-in-60 Rule",
        "SCENARIO (Classic ATPL In-Flight Correction Drill):\n"
        "A flight leg from Waypoint A to Waypoint B has a total planned distance of 120 NM on Planned Track 090° True:\n"
        "- After flying 40 NM from Waypoint A, the pilot fixes position and discovers the aircraft is 4 NM to the RIGHT of track\n"
        "- Distance remaining to Waypoint B = 120 NM - 40 NM = 80 NM\n"
        "QUESTION: Calculate (1) Track Error, (2) Closing Angle, and (3) The new heading alteration to fly directly to Waypoint B.\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate Track Error (TE):\n"
        "  - Formula: TE = (Distance Off / Distance Gone) x 60\n"
        "  - Distance Off = 4 NM\n"
        "  - Distance Gone = 40 NM\n"
        "  - TE = (4 / 40) x 60 = 0.10 x 60 = 6° Track Error (drifted 6° to the Right)!\n\n"
        "Step 2: Calculate Closing Angle (CA):\n"
        "  - Formula: CA = (Distance Off / Distance to Go) x 60\n"
        "  - Distance Off = 4 NM\n"
        "  - Distance to Go = 80 NM\n"
        "  - CA = (4 / 80) x 60 = 0.05 x 60 = 3° Closing Angle!\n\n"
        "Step 3: Calculate Total Heading Alteration to fly directly to Waypoint B:\n"
        "  - Total Alteration = Track Error (TE) + Closing Angle (CA)\n"
        "  - Total Alteration = 6° + 3° = 9° to the LEFT!\n\n"
        "Step 4: Determine the New Heading:\n"
        "  - Aircraft is currently drifted to the RIGHT of track.\n"
        "  - The pilot must turn 9° to the LEFT to eliminate track error and intercept Waypoint B!\n"
        "  - If old heading was 090°, New Heading = 090° - 9° = 081° True!\n\n"
        "FINAL ANSWER: Track Error = 6°; Closing Angle = 3°; Alter heading 9° LEFT to 081° True.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The TE Only vs TE + CA Trap",
        "- If you alter heading by TRACK ERROR ONLY (6° Left):\n"
        "- You will fly PARALLEL to the original track, remaining 4 NM off track forever!\n"
        "- To REGAIN THE DESTINATION, you MUST ADD the Closing Angle (TE + CA = 9°)! Examiners frequently test this exact distinction.",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch10 = [
        ("Q1: After flying 30 NM along a planned route of 90 NM, an aircraft is 3 NM left of track. What is the TRACK ERROR (TE)?",
         "[A] 3°\n[B] 6° (TE = (3 NM / 30 NM) x 60 = 0.10 x 60 = 6°)\n[C] 9°\n[D] 1°",
         "CORRECT: [B]. Track error = (Distance Off / Distance Gone) x 60 = (3 / 30) x 60 = 6° left of track."),
        ("Q2: In the scenario above (3 NM off track, 60 NM to go), what is the CLOSING ANGLE (CA)?",
         "[A] 6°\n[B] 3° (CA = (3 NM / 60 NM) x 60 = 3°)\n[C] 9°\n[D] 1.5°",
         "CORRECT: [B]. Closing angle = (Distance Off / Distance to Go) x 60 = (3 / 60) x 60 = 3°."),
        ("Q3: Continuing from above, by how many degrees must the pilot alter heading to fly DIRECTLY to the destination?",
         "[A] 6° Right\n[B] 9° RIGHT (Alteration = TE + CA = 6° + 3° = 9° Right)\n[C] 3° Right\n[D] 12° Right",
         "CORRECT: [B]. To intercept destination, turn into the error by the sum of TE and CA: 6° + 3° = 9° to the Right.")
    ]

    for q_text, opts, exp in questions_ch10:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 10 compiled: {pdf_path}")


def build_gnav_ch11():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch11_time_systems_solar_twilight.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 11: Time & Solar Phenomena")

    pdf.add_title_banner(
        "General Navigation",
        11,
        "Time Systems, Solar Phenomena & Twilight",
        "409-452"
    )

    pdf.add_heading_1("1. Earth Rotation & Arc-to-Time Conversion")
    pdf.add_paragraph(
        "The Earth rotates 360° of longitude in 24 hours (1 mean solar day):"
    )
    pdf.add_bullet("Arc to Time Rates", "360° = 24 hours; 15° = 1 hour (60 min); 1° = 4 minutes; 1' (minute of arc) = 4 seconds.")
    pdf.add_bullet("Coordinated Universal Time (UTC / Z)", "The atomic time standard referenced to the Greenwich Meridian (000° Longitude).")
    pdf.add_bullet("Local Mean Time (LMT)", "The solar time at a specific meridian of longitude: LMT = UTC +- (Longitude in time). Memory rule: Longitude EAST is LATER (ADD to UTC); Longitude WEST is EARLIER (SUBTRACT from UTC) ('East Ahead, West Behind').")
    pdf.add_bullet("International Date Line (IDL)", "Located along the 180° meridian. Crossing WESTBOUND into East longitude: ADVANCE ONE CALENDAR DAY (+1 day). Crossing EASTBOUND into West longitude: GO BACK ONE CALENDAR DAY (-1 day)!")

    pdf.add_heading_1("2. Civil Twilight Definition")
    pdf.add_paragraph(
        "Civil Twilight is defined as the interval of time between sunset and the moment the CENTER OF THE SUN IS 6° BELOW THE CELESTIAL HORIZON (in the morning, from 6° below horizon to sunrise). It marks the legal limit for VFR day operations!"
    )

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Converting UTC to Local Mean Time (LMT)",
        "SCENARIO (Standard EASA Solar Time Drill):\n"
        "At position 40°N 075°W, a pilot wants to know the Local Mean Time (LMT) when it is 16:30 UTC:\n"
        "QUESTION: What is the exact Local Mean Time (LMT)?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Identify Longitude and Hemisphere:\n"
        "  - Longitude = 075° WEST.\n\n"
        "Step 2: Convert Longitude (degrees) into Time:\n"
        "  - Rate: 15° of longitude = 1 hour of time.\n"
        "  - Time difference = 75° / 15° = 5.0 hours (5 hours 00 minutes)!\n\n"
        "Step 3: Apply the East/West Rule to UTC:\n"
        "  - West Longitude is BEHIND Greenwich time ('West is Behind' -> SUBTRACT!).\n"
        "  - LMT = UTC - Time Difference\n"
        "  - LMT = 16:30 - 05:00 = 11:30 LMT!\n\n"
        "FINAL ANSWER: Local Mean Time at 075°W is exactly 11:30 LMT (the sun is nearly overhead at local noon).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Civil Twilight 6° Below Horizon Trap",
        "- Civil Twilight ends when the sun center is 6° BELOW the horizon (legal daylight ends).\n"
        "- Nautical Twilight is 12° below horizon.\n"
        "- Astronomical Twilight is 18° below horizon.\n"
        "- Aviation law uses CIVIL TWILIGHT (6°) exclusively!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch11 = [
        ("Q1: If UTC is 12:00, what is the Local Mean Time (LMT) at longitude 045°E?",
         "[A] 09:00\n[B] 15:00 LMT (45° / 15° = 3 hours East -> ADD 3 hours to 12:00)\n[C] 12:45\n[D] 18:00",
         "CORRECT: [B]. Longitude 45° East is 3 hours ahead of Greenwich (45 / 15 = 3). LMT = 12:00 + 3h = 15:00."),
        ("Q2: In aviation regulations, when does EVENING CIVIL TWILIGHT officially end?",
         "[A] At sunset\n[B] When the center of the sun's disc is 6 DEGREES BELOW the true horizon\n[C] 30 minutes after sunset\n[D] At complete darkness",
         "CORRECT: [B]. Civil twilight is defined astronomically as the period ending when the sun's center reaches 6° below the sensible horizon."),
        ("Q3: An aircraft flies across the International Date Line (180° meridian) from WEST TO EAST (e.g. from Tokyo to Honolulu). What calendar change must be made?",
         "[A] Advance one day\n[B] SUBTRACT ONE DAY (repeat the same calendar date)\n[C] Zero change\n[D] Advance 12 hours",
         "CORRECT: [B]. Crossing eastbound from East longitude to West longitude across the 180° line repeats the current day (subtract 1 day).")
    ]

    for q_text, opts, exp in questions_ch11:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 11 compiled: {pdf_path}")


def build_gnav_ch12():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch12_inertial_navigation_mechanics.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 12: Inertial Systems (IRS)")

    pdf.add_title_banner(
        "General Navigation",
        12,
        "Inertial Reference Systems (IRS/INS) & Schuler Tuning",
        "453-498"
    )

    pdf.add_heading_1("1. Strapdown Inertial Reference Systems (IRS)")
    pdf.add_paragraph(
        "Modern airliners use 'strapdown' IRS units with 3 orthogonal Ring Laser Gyroscopes (RLGs) and 3 quartz accelerometers fixed directly to the aircraft airframe:"
    )
    pdf.add_bullet("Ring Laser Gyro (RLG)", "Measures angular rate of rotation via the Sagnac Effect (interference between two counter-rotating laser beams). No moving mechanical parts, highly reliable.")
    pdf.add_bullet("Accelerometer Integration", "Accelerometers measure raw linear acceleration (a). 1st integration yields VELOCITY (v = integral a dt); 2nd integration yields POSITION (s = integral v dt).")
    pdf.add_bullet("Gyrocompassing Alignment", "On the ground, while stationary for 5 to 10 minutes, the IRS senses the Earth's rotation (15°/hour) to automatically find TRUE NORTH and calculate local LATITUDE without external aid! Longitude MUST be manually entered by the pilot.")

    pdf.add_heading_1("2. The Schuler Tuning Principle (84.4 Minute Period)")
    pdf.add_paragraph(
        "Because the Earth is curved, accelerating over a spherical surface would cause accelerometers to tilt and mistake gravity for acceleration, causing velocity errors to increase exponentially towards infinity:"
    )
    pdf.add_bullet("Schuler Pendulum", "The IRS platform/computer is tuned to oscillate like a pendulum whose length equals the radius of the Earth (R = 6,371 km). Its natural oscillation period is: T = 2 pi x sqrt(R / g) = EXACTLY 84.4 MINUTES!")
    pdf.add_bullet("Error Bounding", "Schuler tuning forces velocity errors to oscillate harmlessly between positive and negative values every 84.4 minutes, preventing unbounded divergence!")

    pdf.add_heading_1("3. IRS Drift & Triple-Mix FMC Integration")
    pdf.add_bullet("Bounded vs Unbounded Errors", "Velocity and tilt errors oscillate with the 84.4 min Schuler cycle (bounded). Position errors creep forward with a steady DRIFT (unbounded, typically 1 to 2 NM per hour of flight).")
    pdf.add_bullet("Triple Mix & Sensor Fusion", "The Flight Management Computer (FMC) averages positions from 3 independent IRS units (Triple-Mix) and continuously updates the hybrid navigation solution using GPS and DME/DME updating.")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch12 = [
        ("Q1: What is the natural period of the SCHULER OSCILLATION in an Inertial Reference System (IRS)?",
         "[A] 24 hours\n[B] EXACTLY 84.4 MINUTES\n[C] 60 minutes\n[D] 4 minutes",
         "CORRECT: [B]. The Schuler period corresponds to an Earth-radius pendulum: T = 2*pi*sqrt(R/g) = 84.4 minutes, bounding acceleration errors."),
        ("Q2: During stationary ground alignment of an IRS, what parameters can the system determine completely automatically WITHOUT pilot input?",
         "[A] Only magnetic variation\n[B] TRUE NORTH and local LATITUDE (by sensing Earth's rotation rate and gravity)\n[C] Longitude and altitude\n[D] Runway heading",
         "CORRECT: [B]. Earth rotation vector (15°/h) provides True North and latitude = arcsin(vertical component / 15°). Longitude has zero rotational signature and must be entered manually."),
        ("Q3: What optical physical effect is utilized by Ring Laser Gyros (RLG) to measure aircraft angular rotation?",
         "[A] Photoelectric effect\n[B] THE SAGNAC EFFECT (frequency difference between counter-rotating laser beams)\n[C] Hall effect\n[D] Coriolis effect",
         "CORRECT: [B]. Rotation of the RLG alters path lengths of clockwise and counter-clockwise laser beams, generating an optical beat frequency proportional to turn rate.")
    ]

    for q_text, opts, exp in questions_ch12:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 12 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_gnav_ch09()
    build_gnav_ch10()
    build_gnav_ch11()
    build_gnav_ch12()
