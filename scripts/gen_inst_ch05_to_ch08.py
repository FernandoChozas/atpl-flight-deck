#!/usr/bin/env python3
"""
Generator for Subject 022: AGK - Instrumentation
Volume 2: Chapters 05 to 08 (Magnetism, Gyros, IRS & Radio Altimeter)
- Chapter 05: Terrestrial Magnetism & Direct-Reading Compass
- Chapter 06: Gyroscopic Principles & Basic Gyro Instruments
- Chapter 07: Inertial Reference Systems (IRS) & Ring Laser Gyros (RLG)
- Chapter 08: Low-Altitude Radio Altimeter (FMCW)

Fully aligned with CAE Oxford Book 5 (Instrumentation) and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/022_instrumentation"

def build_inst_ch05():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch05_magnetism_direct_reading_compass.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 5: Magnetism & Compasses")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        5,
        "Terrestrial Magnetism & Direct-Reading Compass",
        "149-188"
    )

    pdf.add_heading_1("1. Terrestrial Magnetism, Variation & Dip Angle")
    pdf.add_paragraph(
        "The Earth behaves like a giant bar magnet with its magnetic South pole located near geographic North. "
        "Aircraft magnetic navigation relies on three fundamental terrestrial parameters:"
    )
    pdf.add_bullet("True North vs Magnetic North", "True North is the geographic rotational axis of the Earth. Magnetic North is the direction indicated by a freely suspended magnetic needle aligned with terrestrial flux lines.")
    pdf.add_bullet("Magnetic Variation (Declination)", "The angular difference between True North and Magnetic North. Varies geographically: Variation West (Magnetic is West of True: True = Mag - Var); Variation East (Magnetic is East of True: True = Mag + Var). Mnemonic: 'East is Least (-), West is Best (+)'.")
    pdf.add_bullet("Isogonals & Agonic Line", "Isogonals are lines joining points of equal magnetic variation. The Agonic line is the line of ZERO variation.")
    pdf.add_bullet("Magnetic Dip (Inclination)", "The angle between the Earth's magnetic flux lines and the horizontal local plane. At the Magnetic Equator (Aclinic line), Dip = 0° (purely horizontal). At the Magnetic Poles, Dip = 90° (purely vertical). Magnetic compasses become completely useless near the magnetic poles!")

    pdf.add_heading_1("2. Direct-Reading Compass Turning & Acceleration Errors")
    pdf.add_paragraph(
        "Direct-reading magnetic compasses use a pendulously suspended magnet system whose center of gravity lies below the pivot point. "
        "Due to magnetic dip, the compass suffers severe turning and acceleration errors in the Northern Hemisphere:"
    )

    compass_errors = [
        ["Acceleration Errors (East/West Headings)", "Accelerate -> Inertia holds weight back -> Card tilts -> Dip pulls needle NORTH! Decelerate -> Card tilts opposite -> Needle pulls SOUTH.", "Mnemonic: ANDS (Accelerate North, Decelerate South). On East or West headings in Northern Hemisphere!"],
        ["Turning Errors (North/South Headings)", "Turning THROUGH North: Centrifugal force tilts card outwards; dip pulls needle in turn direction -> Compass LAGS or turns wrong way! Turning THROUGH South: Dip pulls needle ahead of turn -> Compass LEADS (spins faster than aircraft).", "Mnemonic: UNOS (Undershoot North, Overshoot South). Roll out BEFORE reaching North; roll out PAST South!"]
    ]
    pdf.add_table(["Compass Error Scenario", "Physical Mechanism (Inertia + Magnetic Dip)", "Pilot Operational Correction Rule"], compass_errors, col_widths=[125.0, 205.0, 170.0])

    pdf.add_callout(
        "trap",
        "Northern Hemisphere Compass Errors Rules",
        "- ANDS (Acceleration): When accelerating on East or West heading -> Compass indicates a turn towards NORTH! When decelerating -> Compass indicates a turn towards SOUTH!\n"
        "- UNOS (Turning): When turning to a Northerly heading -> Undershoot roll-out (roll out ~20-30° before heading). When turning to a Southerly heading -> Overshoot roll-out (roll out ~20-30° past heading)!\n"
        "- In the Southern Hemisphere: Acceleration and turning errors are EXACTLY REVERSED (SAND / ONUS)!",
        max_chars=86
    )

    pdf.add_heading_1("3. Aircraft Deviation & Compass Swing")
    pdf.add_paragraph(
        "Aircraft metals and electrical wiring generate local magnetic fields that deflect the compass needle away from Magnetic North to Compass North:"
    )
    pdf.add_bullet("Deviation", "The angular difference between Compass Heading and Magnetic Heading: Magnetic = Compass +/- Deviation.")
    pdf.add_bullet("Compass Swing", "A calibrated ground maintenance procedure conducted on a certified compass rose to align permanent corrector magnets, minimizing residual deviation. Residual errors are recorded on the flight deck Compass Deviation Card (maximum residual deviation <= 5°).")

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: In the Northern Hemisphere, what does a direct-reading magnetic compass indicate when the aircraft ACCELERATES while maintaining an exact heading of EAST (090°)?",
         "[A] A turn towards South\n[B] A turn towards NORTH\n[C] No change in heading\n[D] Rapid 360-degree rotation",
         "CORRECT: [B]. Mnemonic ANDS: Accelerate North, Decelerate South. Accelerating on an East or West heading tilts the pendulous card, allowing the vertical component of Earth's magnetic field (dip) to deflect the card towards North."),
        ("Q2: When making a turn onto a heading of NORTH (360°) in the Northern Hemisphere, how should the pilot roll out using a direct-reading compass?",
         "[A] Exactly when the compass passes 360°\n[B] Roll out BEFORE reaching 360° (Undershoot North), because the compass lags behind the turn\n[C] Roll out past 360° (Overshoot North)\n[D] Increase turn rate to Rate 2",
         "CORRECT: [B]. Mnemonic UNOS: Undershoot North, Overshoot South. When turning through North in the Northern Hemisphere, compass liquid drag and dip cause the card to lag behind the turn, requiring an early rollout."),
        ("Q3: What is the name of the line on an aeronautical chart connecting points of ZERO magnetic variation?",
         "[A] Isogonic line\n[B] Agonic line\n[C] Aclinic line\n[D] Rhumb line",
         "CORRECT: [B]. An isogonal connects points of equal variation; the Agonic line is the specific isogonal of zero magnetic variation (where True North and Magnetic North coincide).")
    ]

    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 5 compiled: {pdf_path}")


def build_inst_ch06():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch06_gyroscopic_principles_instruments.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 6: Gyros & Instruments")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        6,
        "Gyroscopic Principles & Basic Gyro Instruments",
        "189-228"
    )

    pdf.add_heading_1("1. Fundamental Properties of Gyroscopes")
    pdf.add_paragraph(
        "A mechanical gyroscope consists of a heavy symmetrical rotor spinning at high RPM (typically 12,000 to 24,000 RPM) "
        "mounted in gimbal rings providing degrees of freedom:"
    )
    pdf.add_bullet("Rigidity in Space (Gyroscopic Inertia)", "The property of a spinning rotor to resist any force attempting to alter its plane of rotation in space (Newton's 1st Law). Directly proportional to: 1. Rotor Mass (m); 2. Radius of gyration (r); 3. Rotational Speed (omega): Angular Momentum L = I x omega.")
    pdf.add_bullet("Gyroscopic Precession", "When an external torque (force) is applied to deflect the spin axis, the rotor resists in the direction of force and instead tilts at a point 90° LATER in the direction of rotation! Precession rate is inversely proportional to rotor speed.")

    pdf.add_heading_1("2. Classic Gyroscopic Instruments: DI, AI & Turn Coordinator")
    gyro_table = [
        ["Instrument", "Rotor Spin Axis & Degrees of Freedom", "Operating Function & Real/Apparent Errors"],
        ["Directional Gyro (Heading Indicator)", "HORIZONTAL spin axis; 2 degrees of freedom (tied to azimuth).", "Indicates aircraft heading. Free gyro: suffers Apparent Drift due to Earth's rotation: Drift = 15°/hour x sin(Latitude). At 60°N: 15 x sin(60°) = 13°/hour apparent drift. Must be reset to magnetic compass every 10-15 min!"],
        ["Artificial Horizon (Attitude Indicator)", "VERTICAL spin axis; 2 degrees of freedom (tied to vertical).", "Indicates Pitch and Roll attitude. Erected by pendulous vane air jets or electrical torque motors. Acceleration errors (indicates false climb and right roll on take-off acceleration); Turning errors (indicates false climb and opposite bank on rolling out of 180° turn)."],
        ["Turn & Slip Indicator (Turn Coordinator)", "HORIZONTAL spin axis; ONE degree of freedom with calibrated restraining springs.", "Rate gyro: rate of yaw precesses gimbal against spring, deflecting needle. Rate 1 turn = 3°/sec (360° turn in 2 minutes). Slip ball (inclinometer) measures apparent gravity/centrifugal balance (shows slip or skid)."]
    ]
    pdf.add_table(["Instrument", "Rotor Spin Axis & Degrees of Freedom", "Operating Function & Real/Apparent Errors"], gyro_table, col_widths=[110.0, 190.0, 200.0])

    pdf.add_callout(
        "trap",
        "Apparent Drift (Earth Rate Wander) Calculation Formula",
        "- Formula: Apparent Wander = 15° x sin(Latitude) per hour!\n"
        "- At the Equator (Lat 0°): Drift = 15 x sin(0°) = ZERO drift!\n"
        "- At the North Pole (Lat 90°): Drift = 15 x sin(90°) = 15° PER HOUR clockwise!\n"
        "- Direction: In the Northern Hemisphere, a free directional gyro drifts to the RIGHT (clockwise); in the Southern Hemisphere, it drifts to the LEFT!",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: A free directional gyroscope is operated at Latitude 60° North. What is the calculated apparent drift rate due to the Earth's rotation?",
         "[A] 0° per hour\n[B] 7.5° per hour\n[C] 13.0° per hour\n[D] 15.0° per hour",
         "CORRECT: [C]. Formula: Earth Rate Drift = 15° x sin(Lat) per hour = 15° x sin(60°) = 15 x 0.866 = 12.99° per hour (~13.0°/hr)."),
        ("Q2: In a basic air-driven artificial horizon (attitude indicator), what false indication occurs when the aircraft accelerates rapidly down the runway on take-off?",
         "[A] A false nose-down pitch\n[B] A false pitch-UP and a slight roll to the RIGHT\n[C] A false rapid turn to the left\n[D] No error occurs",
         "CORRECT: [B]. Take-off forward acceleration closes the rear pendulous erection vanes under inertia, causing the gyro to precess, generating a false indication of pitch-up and a slight false bank to the right."),
        ("Q3: How many degrees of freedom does the rate gyro inside a Turn and Slip indicator possess?",
         "[A] One degree of freedom (gimbal constrained by springs)\n[B] Two degrees of freedom\n[C] Three degrees of freedom\n[D] Zero degrees of freedom",
         "CORRECT: [A]. A rate gyro has only ONE gimbal ring (one degree of freedom), restrained by calibrated mechanical centering springs. Gyro precession directly measures the rate of angular yaw.")
    ]

    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 6 compiled: {pdf_path}")


def build_inst_ch07():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch07_inertial_navigation_irs.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 7: Inertial Reference Systems")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        7,
        "Inertial Reference Systems & Ring Laser Gyros",
        "229-268"
    )

    pdf.add_heading_1("1. Strapdown IRS Architecture vs Gimballed INS")
    pdf.add_paragraph(
        "Inertial systems calculate present position, velocity, and attitude completely autonomously without receiving external radio signals or satellites:"
    )
    pdf.add_bullet("Gimballed INS (Older Technology)", "Mounted on a stabilized physical gimbal platform kept level with local Earth horizontal by torque motors. Heavy, mechanically complex, prone to gimbal lock during aerobatic maneuvers.")
    pdf.add_bullet("Strapdown IRS (Modern Commercial Standard)", "Three Ring Laser Gyros (RLGs) and three solid-state accelerometers are rigidly 'strapped down' directly to the aircraft fuselage frame. A high-speed digital navigation computer mathematically converts body-axis accelerations into Earth-referenced horizontal navigation coordinates.")

    pdf.add_heading_1("2. Ring Laser Gyro (RLG) & The Sagnac Effect")
    pdf.add_paragraph(
        "Ring Laser Gyros have NO MOVING MECHANICAL ROTORS. Rotation is sensed using laser light optics via the Sagnac Effect:"
    )
    pdf.add_bullet("Operating Principle", "Two monochromatic helium-neon laser beams travel in opposite directions (clockwise and counter-clockwise) around a sealed triangular cavity of Zerodur glass-ceramic via dielectric mirrors.")
    pdf.add_bullet("The Sagnac Effect", "When the aircraft rotates about the gyro axis, the path length for the beam traveling in the direction of rotation INCREASES, while the path length for the counter-rotating beam DECREASES. This path difference creates an optical frequency shift: Delta-f = (4 x Area x Omega) / (Wavelength x Optical Perimeter).")
    pdf.add_bullet("Interference Fringe Detection", "The two beams combine at a photodetector, creating optical interference fringes. The fringe transit rate is directly proportional to angular rotation rate.")
    pdf.add_bullet("Laser Lock-In & Piezo-Dither Motor", "At very low rotation rates (< 0.1°/sec), backscattering causes the two laser frequencies to lock together, producing ZERO output (dead band). To prevent lock-in, a piezo-electric dither motor vibrates the RLG back and forth mechanically at ~400 Hz through the lock-in zone!")

    pdf.add_heading_1("3. IRS Alignment Phase & Schuler Tuning")
    irs_align_table = [
        ["Phase / Principle", "Operational Process & Duration", "Flight Crew Action & Mathematical Feature"],
        ["Initial Alignment (Stationary)", "Takes 5 to 10 minutes (longer at high latitudes, e.g. 15 min at 70°N). AIRCRAFT MUST REMAIN COMPLETELY STATIONARY! (Cargo loading or wind buffeting will abort alignment).", "Crew inputs present gate coordinates into MCDU. IRS measures Earth's rotation (15°/hr) to find TRUE NORTH (gyrocompassing) and senses gravity to level accelerometers."],
        ["Latitude Limitations", "IRS cannot align above Latitude 78° or 82° North/South.", "At extreme polar latitudes, the horizontal component of Earth rotation is too weak for gyrocompassing."],
        ["Schuler Tuning (84.4 Minutes)", "Accelerometers are mathematically tuned to oscillate like an 84.4-minute pendulum whose length equals Earth radius (R = 6,371 km).", "Prevents aircraft acceleration from being mistaken for a tilt of the vertical. Schuler tuning contains navigation position errors within a periodic 84.4-minute bounded oscillation cycle!"]
    ]
    pdf.add_table(["Phase / Principle", "Operational Process & Duration", "Flight Crew Action & Mathematical Feature"], irs_align_table, col_widths=[110.0, 190.0, 200.0])

    pdf.add_callout(
        "trap",
        "IRS Alignment Rules & Lat/Long Verification",
        "- The aircraft MUST NOT BE MOVED during the alignment cycle!\n"
        "- The flight crew must enter present position coordinates into the MCDU. The IRS compares entered latitude with its own internally sensed gyrocompass latitude: if discrepancy > 1°, alignment FAILS!\n"
        "- Note: IRS navigates referenced to TRUE NORTH, not Magnetic North!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: What is the physical optical phenomenon utilized by a Ring Laser Gyro (RLG) to measure angular rotation rate?",
         "[A] Doppler effect\n[B] The Sagnac effect, where optical path lengths differ between counter-propagating laser beams\n[C] Photo-electric emission\n[D] Faraday induction",
         "CORRECT: [B]. The Sagnac effect dictates that rotating the laser cavity creates a path length difference between the clockwise and counter-clockwise beams, producing a frequency difference proportional to rotation rate."),
        ("Q2: What is the purpose of the piezo-electric 'dither motor' installed on a Ring Laser Gyro?",
         "[A] To cool the laser mirrors\n[B] To vibrate the gyro back and forth through the low-speed 'lock-in' threshold, preventing zero-output error\n[C] To level the platform\n[D] To align with magnetic north",
         "CORRECT: [B]. At low rotation rates, internal mirror backscattering locks the two laser frequencies together (laser lock-in). A dither motor mechanically oscillates the gyro at high frequency to keep it out of the dead band."),
        ("Q3: What is the period of the Schuler oscillation cycle in an inertial reference navigation system?",
         "[A] 24.0 hours\n[B] 84.4 minutes\n[C] 12.5 minutes\n[D] 360 seconds",
         "CORRECT: [B]. The Schuler pendulum period is T = 2 x pi x sqrt(R / g) = 84.4 minutes. Tuning the IRS to 84.4 minutes isolates linear accelerations from gravity vectors, preventing unbounded position drift.")
    ]

    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 7 compiled: {pdf_path}")


def build_inst_ch08():
    pdf_path = os.path.join(OUTPUT_DIR, "022_ch08_radio_altimeter.pdf")
    pdf = PDFBuilder("AGK Instrumentation", "022", "Chapter 8: Radio Altimeter")

    # Cover / Header Banner
    pdf.add_title_banner(
        "AGK Instrumentation",
        8,
        "Low-Altitude Radio Altimeter (FMCW)",
        "269-298"
    )

    pdf.add_heading_1("1. Frequency Modulated Continuous Wave (FMCW) Radar")
    pdf.add_paragraph(
        "The Radio Altimeter (Rad Alt) measures the precise absolute geometric clearance of aircraft main landing gear wheels "
        "above underlying terrain from 0 to 2,500 ft AGL:"
    )
    pdf.add_bullet("Frequency Band", "Operates in the SHF aeronautical radionavigation band between 4.2 GHz and 4.4 GHz (typically center frequency 4.3 GHz).")
    pdf.add_bullet("FMCW Modulation Technique", "Instead of high-power pulses, the transmitter outputs a CONTINUOUS signal whose carrier frequency is swept linearly up and down at a constant modulation rate (triangular or sinusoidal frequency sweep).")
    pdf.add_bullet("Beat Frequency Principle", "Signal transmitted downward reflects off the terrain and returns to the receiver antenna after a time delay: Delta-t = (2 x Height) / c. During this transit time, the transmitter has swept to a new frequency! Mixing the received signal with the current transmitted signal produces a BEAT FREQUENCY (Delta-f) that is DIRECTLY PROPORTIONAL to terrain wheel height!")

    pdf.add_heading_1("2. Integration, Decision Height & Autoland Guidance")
    rad_table = [
        ["Height Regime", "Operational Function & Cockpit Indications", "Interfaced Aircraft Systems"],
        ["Above 2,500 ft AGL", "Radio altimeter indication is INHIBITED or flagged OFF. Pointer parked behind mask; digital readout blanked.", "No ground interaction; GPWS radar terrain clearance modes inactive."],
        ["2,500 ft down to 50 ft", "Readout appears on PFD (round dial or digital tape). Dial expansion: 0-500 ft scale is expanded for high visual precision.", "Feeds GPWS Modes 1-4; arms Autoland flare and rollout modes."],
        ["Decision Height (DH)", "Pilot dials DH bug on EFIS control panel (e.g. 200 ft for CAT I, 100 ft or 50 ft for CAT II).", "At DH: Yellow 'DH' annunciates on PFD and synthetic voice announces 'DECISION' or 'MINIMUMS'!"],
        ["Below 50 ft (Autoland)", "Crucial input to autopilot autoland computers.", "At 50-30 ft: Triggers autopilot FLARE mode (throttles retard to idle, pitch increases smoothly for touchdown). Synthetic voice callouts: '50, 40, 30, 20, 10, RETARD'."]
    ]
    pdf.add_table(["Height Regime", "Operational Function & Cockpit Indications", "Interfaced Aircraft Systems"], rad_table, col_widths=[110.0, 195.0, 195.0])

    pdf.add_callout(
        "trap",
        "Radio Altimeter Zero Height Calibration",
        "- The Radio Altimeter antennas are mounted on the fuselage underside.\n"
        "- Calibration Datum: In a level flight landing attitude, when the main landing gear tyres touch the runway concrete, the radio altimeter MUST INDICATE EXACTLY ZERO FEET!\n"
        "- Antenna cable delay lines are built into the receiver harness to compensate for the physical distance between antennas and main wheels.",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: What modulation principle is utilized by a modern low-altitude radio altimeter?",
         "[A] Amplitude Modulation (AM)\n[B] Frequency Modulated Continuous Wave (FMCW) where the beat frequency between transmitted and reflected waves is proportional to wheel height\n[C] Pulsed primary radar with 10 microsecond pulses\n[D] Phase shift keying",
         "CORRECT: [B]. Low-altitude radio altimeters use FMCW. Comparing the transmitted swept frequency against the delayed reflected return frequency produces a beat frequency directly proportional to terrain height."),
        ("Q2: At what radio altitude does the radio altimeter indication normally become active on a transport aircraft Primary Flight Display (PFD)?",
         "[A] 10,000 ft AGL\n[B] 5,000 ft AGL\n[C] 2,500 ft AGL\n[D] 500 ft AGL",
         "CORRECT: [C]. Commercial radio altimeters operate from 0 to 2,500 ft AGL. Above 2,500 ft, the indication is blanked or masked on modern electronic displays."),
        ("Q3: When an aircraft is in the landing flare with its main gear wheels touching the runway surface, what should the radio altimeter indicate?",
         "[A] Negative 5 ft\n[B] Exactly ZERO feet\n[C] Antenna height (approx 10 ft)\n[D] Aerodrome elevation",
         "CORRECT: [B]. Radio altimeters are calibrated with an internal electronic delay line so that with landing gear extended in touchdown attitude, the display reads exactly 0 ft when the tyres touch down.")
    ]

    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"Instrumentation Chapter 8 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_inst_ch05()
    build_inst_ch06()
    build_inst_ch07()
    build_inst_ch08()
