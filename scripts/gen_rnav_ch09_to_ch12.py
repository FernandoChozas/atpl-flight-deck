#!/usr/bin/env python3
"""
Generator for Subject 062: Radio Navigation & PBN
Volume 3: Chapters 9 to 12
- Chapter 9: Global Navigation Satellite Systems (GNSS: GPS, Galileo, GLONASS)
- Chapter 10: Satellite Integrity Monitoring: RAIM Algorithms & SBAS/GBAS
- Chapter 11: Performance-Based Navigation (PBN): Concept, RNAV vs RNP & Specs
- Chapter 12: Area Navigation Systems (RNAV Architecture, FMS Sensors & TSE)

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford Radio Navigation and EASA ATPL ECQB syllabus.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/062_radio_navigation_pbn"

def build_rnav_ch09():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch09_gnss_gps_galileo_principles.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 9: GNSS Principles & GPS")

    pdf.add_title_banner(
        "Radio Navigation",
        9,
        "Global Navigation Satellite Systems (GNSS & GPS)",
        "341-384"
    )

    pdf.add_heading_1("1. The NAVSTAR GPS Architecture")
    pdf.add_paragraph(
        "GPS is a satellite-based radio navigation system operated by the US Space Force, structured into three segments:"
    )
    pdf.add_bullet("Space Segment", "Baseline of 24 operational satellites distributed in 6 orbital planes inclined at 55° to the equator at an altitude of 20,200 km (semi-synchronous 12-hour orbit). Transmits on L1 (1575.42 MHz) and L2 (1227.60 MHz).")
    pdf.add_bullet("Control Segment", "Master Control Station (Schriever AFB, Colorado) and global monitor stations tracking orbits, updating clock corrections, and uploading ephemeris data.")
    pdf.add_bullet("User Segment", "Airborne receiver measuring Time of Arrival (TOA) of pseudo-random noise (PRN) codes from each satellite.")

    pdf.add_heading_1("2. The 4 Satellites Fix & Clock Bias")
    pdf.add_paragraph(
        "Because the aircraft receiver clock is an inexpensive quartz crystal (not an atomic clock), it contains an unknown time error (clock bias):"
    )
    pdf.add_bullet("Mathematical Requirement", "There are 4 unknown variables to solve: Latitude (X), Longitude (Y), Altitude (Z), and Receiver Clock Error (Delta t). Therefore, A MINIMUM OF 4 SATELLITES IS MANDATORY FOR A 3D POSITION FIX!")
    pdf.add_bullet("Dilution of Precision (DOP)", "Measures the geometric strength of satellite distribution. Best geometry (Low PDOP < 3): One satellite directly overhead, and three satellites spaced 120° apart near the horizon. Poor geometry (High PDOP > 6): Satellites bunched close together in the sky.")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Satellite Ranging & Pseudo-Range Correction",
        "SCENARIO (GNSS Clock Bias Principle Drill):\n"
        "A GPS receiver measures time of signal arrival from a satellite:\n"
        "- The raw measured transit time indicates a distance of 21,000,000 meters (Pseudo-range)\n"
        "- The receiver clock has an internal bias of +0.000010 seconds (10 microseconds fast)\n"
        "- Speed of light c = 300,000,000 m/s\n"
        "QUESTION: What is the distance error caused by this 10 microsecond clock bias, and what is the true corrected range?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the distance error created by the clock bias:\n"
        "  - Formula: Distance Error = Speed of Light (c) x Clock Bias (Delta t)\n"
        "  - Distance Error = 300,000,000 m/s x 0.000010 s = 3,000 meters (3.0 km)!\n\n"
        "Step 2: Understand why 4 satellites are needed:\n"
        "  - A tiny clock error of only 10 microseconds causes a massive 3-kilometer position error!\n"
        "  - The 4th satellite provides the algebraic equation that solves for this exact 10 microsecond bias, eliminating the 3,000 m error completely!\n\n"
        "Step 3: Calculate the True Range:\n"
        "  - True Range = Measured Pseudo-range - Distance Error\n"
        "  - True Range = 21,000,000 m - 3,000 m = 20,997,000 meters.\n\n"
        "FINAL ANSWER: Distance error = 3,000 meters. True range = 20,997 km. The 4th satellite eliminates receiver clock bias.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "3 Satellites vs 4 Satellites Trap",
        "- 3 satellites provide a 2D FIX (Latitude and Longitude ONLY), assuming altitude is already known!\n"
        "- 4 satellites are REQUIRED FOR A FULL 3D FIX (Latitude, Longitude, Altitude, and Clock Bias)!\n"
        "- Never answer 3 satellites when the question asks for a full 3D fix.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch09 = [
        ("Q1: What is the MINIMUM number of satellites required by an unaugmented airborne GPS receiver to compute a full 3D position fix (latitude, longitude, altitude) and time?",
         "[A] 3 satellites\n[B] AT LEAST 4 SATELLITES (to resolve X, Y, Z coordinates and receiver clock bias)\n[C] 5 satellites\n[D] 24 satellites",
         "CORRECT: [B]. The 4 unknowns (latitude, longitude, altitude, and receiver clock offset) require at least 4 independent pseudo-range equations from 4 visible satellites."),
        ("Q2: In satellite navigation, what does a LOW value of Position Dilution of Precision (PDOP < 3) indicate?",
         "[A] Weak satellite signals\n[B] EXCELLENT SATELLITE GEOMETRY (satellites widely spaced across the sky), yielding high navigational accuracy\n[C] Clock failure\n[D] High ionospheric delay",
         "CORRECT: [B]. Lower DOP values represent stronger geometric triangulation. PDOP < 3 represents ideal geometry with wide angular separation."),
        ("Q3: What is the primary source of pseudo-range ERROR in standard unaugmented single-frequency GPS?",
         "[A] Rain attenuation\n[B] IONOSPHERIC DELAY (refraction of radio waves through charged free electrons in the ionosphere)\n[C] Relativistic error\n[D] Antenna drag",
         "CORRECT: [B]. Ionospheric delay introduces unmodeled propagation delays of 5 to 30 meters, representing the largest single pseudo-range error source.")
    ]

    for q_text, opts, exp in questions_ch09:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 9 compiled: {pdf_path}")


def build_rnav_ch10():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch10_raim_satellite_integrity_augmentation.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 10: RAIM & Augmentation")

    pdf.add_title_banner(
        "Radio Navigation",
        10,
        "Satellite Integrity Monitoring (RAIM & SBAS/GBAS)",
        "385-424"
    )

    pdf.add_heading_1("1. Receiver Autonomous Integrity Monitoring (RAIM)")
    pdf.add_paragraph(
        "GPS satellites can transmit erroneous ranging signals without immediate warning. RAIM is an internal airborne algorithm that cross-checks satellite ranges for consistency:"
    )
    pdf.add_bullet("Fault Detection (FD)", "REQUIRES A MINIMUM OF 5 SATELLITES (or 4 satellites + Barometric VNAV aiding). Detects if a faulty satellite is providing corrupt data, alerting the pilot with an integrity warning.")
    pdf.add_bullet("Fault Detection and Exclusion (FDE)", "REQUIRES A MINIMUM OF 6 SATELLITES (or 5 satellites + Baro-VNAV). Identifies WHICH satellite is faulty, excludes it from the navigation solution, and continues navigation without interruption!")
    pdf.add_bullet("Mask Angle", "Satellites within 5° of the horizon are rejected (masked) due to excessive tropospheric refraction.")

    pdf.add_heading_1("2. Satellite-Based Augmentation Systems (SBAS)")
    pdf.add_paragraph(
        "SBAS uses ground reference networks and geostationary satellites to broadcast wide-area differential corrections:"
    )
    pdf.add_bullet("Systems", "EGNOS (Europe), WAAS (USA), MSAS (Japan), GAGAN (India).")
    pdf.add_bullet("Capability", "Eliminates ionospheric delay errors. Enables LPV (Localizer Performance with Vertical Guidance) approaches down to ILS Cat I decision height (200 ft) without ground ILS equipment!")

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch10 = [
        ("Q1: What is the MINIMUM number of operational satellites required for RAIM to perform FAULT DETECTION (FD)?",
         "[A] 4 satellites\n[B] AT LEAST 5 SATELLITES (or 4 with Barometric Altimeter aiding)\n[C] 6 satellites\n[D] 3 satellites",
         "CORRECT: [B]. Fault Detection requires 5 visible satellites with suitable geometry to detect an anomalous pseudo-range error."),
        ("Q2: How many satellites are required for RAIM to perform FAULT DETECTION AND EXCLUSION (FDE)?",
         "[A] 5 satellites\n[B] AT LEAST 6 SATELLITES (or 5 with Baro-VNAV aiding)\n[C] 8 satellites\n[D] 4 satellites",
         "CORRECT: [B]. FDE requires 6 satellites: 4 to solve the 3D position/time, a 5th to detect the fault, and a 6th to isolate and exclude the corrupt satellite."),
        ("Q3: What is the European Satellite-Based Augmentation System (SBAS) called?",
         "[A] WAAS\n[B] EGNOS (European Geostationary Navigation Overlay Service)\n[C] Galileo\n[D] GLONASS",
         "CORRECT: [B]. EGNOS is the European SBAS system that augments GPS signals to provide safety-of-life LPV approach capabilities.")
    ]

    for q_text, opts, exp in questions_ch10:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 10 compiled: {pdf_path}")


def build_rnav_ch11():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch11_pbn_specifications_rnav_rnp.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 11: PBN & RNAV vs RNP")

    pdf.add_title_banner(
        "Radio Navigation",
        11,
        "Performance-Based Navigation (PBN) & Specifications",
        "425-472"
    )

    pdf.add_heading_1("1. The PBN Revolution: RNAV vs RNP")
    pdf.add_paragraph(
        "Performance-Based Navigation specifies aircraft Required Navigation Performance rather than mandating specific ground sensors:"
    )
    pdf.add_bullet("The Fundamental Distinction", "RNP REQUIRES ON-BOARD PERFORMANCE MONITORING AND ALERTING (OPMA)! RNAV DOES NOT! Under RNP, the system continuously monitors containment and alerts the crew if Total System Error exceeds the containment boundary.")
    pdf.add_bullet("Containment Standard", "The aircraft navigation system must keep the aircraft within the designated accuracy value (e.g. +-1.0 NM for RNP 1) for AT LEAST 95% OF TOTAL FLIGHT TIME, and within twice that value (2 x RNP) for 99.999% of time!")

    pdf.add_heading_1("2. Summary of Official PBN Specifications")
    pbn_table = [
        ["PBN Specification", "Accuracy Limit (95% Containment)", "Flight Phase & Operational Application"],
        ["RNAV 10 (RNP 10)", "+- 10 Nautical Miles", "Oceanic and remote continental airspace (e.g. Pacific routes)."],
        ["RNAV 5 (B-RNAV)", "+- 5 Nautical Miles", "En-route continental airspace (Mandatory in European airspace)."],
        ["RNAV 1 & RNAV 2 (P-RNAV)", "+- 1 NM or +- 2 NM", "Terminal arrivals (STAR) and departures (SID) with radar coverage."],
        ["RNP 4", "+- 4 Nautical Miles", "Oceanic operations with reduced separation (30/30 NM)."],
        ["RNP 1", "+- 1 Nautical Mile", "Terminal arrivals (STAR) and departures (SID) without radar."],
        ["RNP APCH", "+- 0.3 NM on final approach", "Non-precision approaches: LNAV, LNAV/VNAV, and LPV."],
        ["RNP AR APCH", "Down to +- 0.1 NM (Authorisation Required)", "Complex terrain procedures with constant Radius-to-Fix (RF) curved legs!"]
    ]
    pdf.add_table(["PBN Specification", "Accuracy Limit (95% Containment)", "Flight Phase & Operational Application"], pbn_table, col_widths=[115.0, 150.0, 230.0])

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch11 = [
        ("Q1: What is the fundamental operational difference between an 'RNAV' specification and an 'RNP' specification?",
         "[A] RNP uses only satellites\n[B] RNP REQUIRES ON-BOARD PERFORMANCE MONITORING AND ALERTING (OPMA), whereas RNAV does not\n[C] RNAV is more accurate than RNP\n[D] RNAV is for military only",
         "CORRECT: [B]. Under ICAO Doc 9613, the presence of real-time on-board performance monitoring and alerting (OPMA) is the sole distinguishing feature that defines an RNP specification."),
        ("Q2: In European en-route airspace, what is the mandatory minimum navigation specification known as Basic RNAV (B-RNAV)?",
         "[A] RNAV 1\n[B] RNAV 5 (requiring aircraft to maintain track within +- 5 NM for at least 95% of flight time)\n[C] RNP 4\n[D] RNAV 10",
         "CORRECT: [B]. B-RNAV in Europe is formally designated as RNAV 5, mandating a lateral accuracy of 5 NM for 95% of the flight duration."),
        ("Q3: What unique procedure design capability is enabled by RNP AR APCH (Authorisation Required)?",
         "[A] Vertical take-offs\n[B] RADIUS-TO-FIX (RF) CURVED LEGS in the final approach and missed approach segments to skirt around high terrain\n[C] Supersonic flight\n[D] Zero fuel reserves",
         "CORRECT: [B]. RNP AR allows precise curved RF turns in mountainous terrain with containment down to RNP 0.1.")
    ]

    for q_text, opts, exp in questions_ch11:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 11 compiled: {pdf_path}")


def build_rnav_ch12():
    pdf_path = os.path.join(OUTPUT_DIR, "062_ch12_rnav_architecture_fms_sensors.pdf")
    pdf = PDFBuilder("Radio Navigation", "062", "Chapter 12: RNAV & FMS Sensors")

    pdf.add_title_banner(
        "Radio Navigation",
        12,
        "RNAV Architecture, FMS Sensors & Total System Error",
        "473-520"
    )

    pdf.add_heading_1("1. FMS Multi-Sensor Position Updating Hierarchy")
    pdf.add_paragraph(
        "Modern Flight Management Systems (FMS) compute a continuous best-estimate position by fusing inputs from multiple sensors:"
    )
    pdf.add_bullet("1. GNSS (GPS / Galileo)", "Primary sensor offering highest continuous accuracy (< 5 m).")
    pdf.add_bullet("2. DME / DME Updating", "Secondary terrestrial sensor. Requires at least two DME stations whose intersecting radials cross at an angle between 30° and 150° (optimal 90°)! Sub-mile accuracy.")
    pdf.add_bullet("3. VOR / DME Updating", "Single VOR/DME co-located station providing bearing and distance. Lower accuracy due to VOR angular divergence at range.")
    pdf.add_bullet("4. Inertial Reference Systems (IRS)", "Provides continuous dead-reckoning position during GNSS or DME reception loss. IRS position drifts over time.")

    pdf.add_heading_1("2. Total System Error (TSE) Components")
    pdf.add_paragraph(
        "Under ICAO PBN definitions, the lateral error of an aircraft relative to the intended track consists of three statistically independent errors combined using root-sum-square:"
    )
    pdf.add_bullet("The TSE Master Formula", "TSE = sqrt( PDE^2 + FTE^2 + NSE^2 )")
    pdf.add_bullet("Path Definition Error (PDE)", "Discrepancy between the defined path in the navigation database and the intended true flight path (virtually zero in modern digital databases).")
    pdf.add_bullet("Flight Technical Error (FTE)", "Pilot or autopilot accuracy in tracking the indicated path on the flight director/CDI.")
    pdf.add_bullet("Navigation System Error (NSE)", "The difference between actual aircraft position and the position computed by the navigation sensors.")

    pdf.add_heading_1("3. Fly-By vs Fly-Over Waypoints")
    pdf.add_bullet("Fly-By Waypoint (Standard)", "Depicted as an open 4-point star. The FMS initiates turn anticipation BEFORE reaching the waypoint, cutting the corner smoothly without overshoot.")
    pdf.add_bullet("Fly-Over Waypoint", "Depicted as a 4-point star enclosed in a circle. The aircraft MUST FLY DIRECTLY OVERHEAD the waypoint before initiating the turn, followed by an overshoot and intercept.")

    pdf.add_heading_1("4. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Total System Error (TSE)",
        "SCENARIO (EASA PBN Total System Error Drill):\n"
        "During an RNP 1 terminal departure, the FMS computes the error components:\n"
        "- Path Definition Error (PDE) = 0.10 NM\n"
        "- Flight Technical Error (FTE) = 0.50 NM\n"
        "- Navigation System Error (NSE) = 0.60 NM\n"
        "QUESTION: What is the Total System Error (TSE), and is it compliant with the RNP 1 specification (+- 1.0 NM)?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Recall the Master TSE Root-Sum-Square Formula:\n"
        "  - Formula: TSE = sqrt( PDE^2 + FTE^2 + NSE^2 )\n\n"
        "Step 2: Square each error component:\n"
        "  - PDE^2 = 0.10^2 = 0.01\n"
        "  - FTE^2 = 0.50^2 = 0.25\n"
        "  - NSE^2 = 0.60^2 = 0.36\n\n"
        "Step 3: Sum the squared values:\n"
        "  - Sum = 0.01 + 0.25 + 0.36 = 0.62.\n\n"
        "Step 4: Take the square root:\n"
        "  - TSE = sqrt(0.62) = 0.787 NM (~0.79 NM)!\n\n"
        "Step 5: Compare with RNP 1 Containment Limit (1.0 NM):\n"
        "  - 0.79 NM <= 1.0 NM -> COMPLIANT!\n\n"
        "FINAL ANSWER: Total System Error is 0.79 NM, which is well within the 1.0 NM legal limit for RNP 1.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The DME/DME Intersection Angle Trap",
        "- For an FMS to accept a DME/DME position update:\n"
        "- The angle between the two DME station lines of position MUST be between 30° and 150°!\n"
        "- Angles under 30° or over 150° create severe geometric dilution and are automatically rejected.",
        max_chars=86
    )

    pdf.add_heading_1("5. AviationExam Practice Questions (with Explanations)")
    questions_ch12 = [
        ("Q1: What are the acceptable intersection angles between two DME stations for an FMS DME/DME position update?",
         "[A] Exactly 90° only\n[B] BETWEEN 30 DEGREES AND 150 DEGREES (with optimal geometry at 90°)\n[C] Any angle\n[D] Less than 15°",
         "CORRECT: [B]. The FMS rejects DME pairs intersecting at angles shallower than 30° or wider than 150° to avoid geometric position stretching."),
        ("Q2: In Performance-Based Navigation, what are the three components of TOTAL SYSTEM ERROR (TSE)?",
         "[A] Wind error, drift error, clock error\n[B] PATH DEFINITION ERROR (PDE), FLIGHT TECHNICAL ERROR (FTE), and NAVIGATION SYSTEM ERROR (NSE)\n[C] Altimeter error, speed error, heading error\n[D] Magnetic error only",
         "CORRECT: [B]. By ICAO definition, TSE = sqrt(PDE^2 + FTE^2 + NSE^2), combining database, pilot/autopilot tracking, and sensor errors."),
        ("Q3: What symbol on an instrument flight chart depicts a 'FLY-OVER' waypoint?",
         "[A] A plain 4-point star\n[B] A 4-point star ENCLOSED WITHIN A CIRCLE\n[C] A solid black triangle\n[D] An open square",
         "CORRECT: [B]. A fly-by waypoint is an unenclosed star; enclosing the star in a circle mandates flying directly overhead before turning.")
    ]

    for q_text, opts, exp in questions_ch12:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Radio Navigation Chapter 12 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_rnav_ch09()
    build_rnav_ch10()
    build_rnav_ch11()
    build_rnav_ch12()
