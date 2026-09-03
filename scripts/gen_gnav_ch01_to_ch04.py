#!/usr/bin/env python3
"""
Generator for Subject 061: General Navigation
Volume 1: Chapters 1 to 4
- Chapter 1: The Earth: Geometry, Coordinates, Distance & Departure Formulas
- Chapter 2: Great Circles, Rhumb Lines, Earth Convergence & Conversion Angle
- Chapter 3: Earth Magnetism, Variation, Deviation & The Compass (ANDS / UNOS)
- Chapter 4: Aeronautical Charts: Principles, Projections & Scale Properties

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford General Navigation and EASA ATPL ECQB syllabus.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/061_general_navigation"

def build_gnav_ch01():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch01_earth_geometry_coordinates_distance.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 1: Earth Geometry & Distance")

    pdf.add_title_banner(
        "General Navigation",
        1,
        "The Earth: Geometry, Coordinates & Distances",
        "1-42"
    )

    pdf.add_heading_1("1. Earth Dimensions & Coordinate System")
    pdf.add_paragraph(
        "The Earth is an oblate spheroid (flattened at the poles, bulging at the equator) modeled by the WGS-84 ellipsoid:"
    )
    pdf.add_bullet("Dimensions & Flattening", "Equatorial Diameter = 12,756 km (6,888 NM); Polar Diameter = 12,714 km (6,865 NM). Compression / Flattening = (Equatorial - Polar) / Equatorial = 1 / 298.25.")
    pdf.add_bullet("Latitude (Parallels)", "Angular distance North or South of Equator (0° to 90°). Colatitude = 90° - Latitude. Parallels are SMALL CIRCLES (except the Equator, which is a Great Circle).")
    pdf.add_bullet("Longitude (Meridians)", "Angular distance East or West of Prime Meridian (Greenwich 000°) (0° to 180°). All meridians are SEMI-GREAT CIRCLES.")
    pdf.add_bullet("The Nautical Mile Definition", "1 Nautical Mile (NM) is legally defined as EXACTLY 1,852 METERS (6,076.1 ft). Physically, 1 NM = the length of 1 MINUTE OF ARC ALONG A MERIDIAN of latitude!")

    pdf.add_heading_1("2. The Departure Formula (Distance along a Parallel)")
    pdf.add_paragraph(
        "Because meridians converge toward the poles, the linear east-west distance between two meridians decreases as latitude increases:"
    )
    pdf.add_bullet("The Master Departure Formula", "Departure (NM) = Change of Longitude (in minutes of arc) x cos(Latitude)")
    pdf.add_bullet("Change of Longitude (dlong)", "dlong (minutes) = Departure (NM) / cos(Latitude) = Departure x sec(Latitude)")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating East-West Distance (Departure)",
        "SCENARIO (Fundamental ATPL Navigation Drill):\n"
        "Two aircraft waypoints are located on the same parallel of latitude:\n"
        "- Waypoint A: 60°00'N 010°00'W\n"
        "- Waypoint B: 60°00'N 025°00'W\n"
        "QUESTION: What is the exact distance in Nautical Miles along the 60°N parallel between Waypoint A and Waypoint B?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Change in Longitude (dlong):\n"
        "  - Longitude A = 010°W\n"
        "  - Longitude B = 025°W\n"
        "  - Both are in the same hemisphere (West), so subtract: dlong = 25° - 10° = 15°.\n\n"
        "Step 2: Convert degrees of longitude into minutes of arc:\n"
        "  - Rule: 1 degree = 60 minutes of arc.\n"
        "  - dlong (minutes) = 15° x 60 = 900 minutes of arc!\n\n"
        "Step 3: Recall the Master Departure Formula:\n"
        "  - Formula: Departure (NM) = dlong (minutes) x cos(Latitude)\n\n"
        "Step 4: Plug in the numbers and calculate:\n"
        "  - Latitude = 60°N. (Notice: cos(60°) = 0.50 exactly!).\n"
        "  - Departure = 900 minutes x cos(60°) = 900 x 0.50 = 450 Nautical Miles!\n\n"
        "FINAL ANSWER: The distance along the 60°N parallel is exactly 450 Nautical Miles (half of the 900 NM it would be at the equator!).",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The cos(60°) = 0.50 Shortcut Trap",
        "- At 60° latitude (North or South), cos(60°) is EXACTLY 0.50!\n"
        "- This means at 60° latitude, 1° of longitude equals EXACTLY 30 NM (half of the 60 NM at the equator)!\n"
        "- Examiners LOVE 60° latitude questions because they can be solved instantly in your head without a calculator.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: What is the distance in Nautical Miles along the parallel of 60°S between longitudes 020°E and 040°E?",
         "[A] 1,200 NM\n[B] 600 NM (20° x 60 min = 1,200 min x cos(60°) = 600 NM)\n[C] 300 NM\n[D] 1,852 NM",
         "CORRECT: [B]. Change of longitude = 20° = 1,200 minutes. Departure = 1,200 x cos(60°) = 1,200 x 0.5 = 600 NM."),
        ("Q2: Which line on the Earth's surface is BOTH a parallel of latitude and a GREAT CIRCLE?",
         "[A] Tropic of Cancer\n[B] THE EQUATOR (0° Latitude)\n[C] Greenwich Meridian\n[D] Arctic Circle",
         "CORRECT: [B]. The Equator is the only parallel of latitude whose plane passes directly through the center of the Earth, making it a Great Circle."),
        ("Q3: What is the international legal definition of ONE NAUTICAL MILE?",
         "[A] 6,000 feet\n[B] Exactly 1,852 METERS (approx 6,076.1 ft)\n[C] 1,609 meters\n[D] 2,000 yards",
         "CORRECT: [B]. By international agreement in 1929 (adopted by ICAO), 1 NM is defined as exactly 1,852 meters.")
    ]

    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 1 compiled: {pdf_path}")


def build_gnav_ch02():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch02_great_circles_rhumb_lines_convergence.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 2: Great Circles & Convergence")

    pdf.add_title_banner(
        "General Navigation",
        2,
        "Great Circles, Rhumb Lines & Convergence",
        "43-84"
    )

    pdf.add_heading_1("1. Great Circles vs Rhumb Lines")
    pdf.add_paragraph(
        "Navigators navigate using two fundamental geometric curves on the Earth's sphere:"
    )
    pdf.add_bullet("Great Circle (Orthodrome)", "The intersection of the sphere with a plane passing through the CENTER of the Earth. SHORTEST DISTANCE between two points. It crosses successive meridians at constantly CHANGING ANGLES!")
    pdf.add_bullet("Rhumb Line (Loxodrome)", "A line on the Earth's surface that crosses all meridians at the SAME CONSTANT ANGLE. Easy to fly (constant heading), but physically LONGER than a Great Circle!")
    pdf.add_bullet("Relative Path", "A Great Circle always curves TOWARDS THE POLE relative to the Rhumb Line connecting the same two points (curves North in N Hemisphere, curves South in S Hemisphere).")

    pdf.add_heading_1("2. Earth Convergence & Conversion Angle Formulas")
    pdf.add_paragraph(
        "Because meridians converge at the poles, the true direction of a Great Circle changes continuously along its track:"
    )
    pdf.add_bullet("Earth Convergence Formula", "Earth Convergence (degrees) = Change of Longitude (dlong) x sin(Mean Latitude)")
    pdf.add_bullet("Conversion Angle Formula", "Conversion Angle (CA) = 0.5 x Earth Convergence = 0.5 x dlong x sin(Mean Latitude)")
    pdf.add_bullet("Great Circle to Rhumb Line Relationship", "Rhumb Line Track = Great Circle Track +- Conversion Angle. In Northern Hemisphere: Great Circle Track from West to East starts HIGHER than Rhumb Line Track and finishes LOWER!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Great Circle Initial Track and Convergence",
        "SCENARIO (Classic EASA Exam Question):\n"
        "An oceanic flight is planned between two waypoints in the Northern Hemisphere:\n"
        "- Point A: 50°N 010°W\n"
        "- Point B: 50°N 030°W\n"
        "- The Rhumb Line Track between A and B is 270° True (due West along 50°N parallel)\n"
        "QUESTION: What is the Earth Convergence, Conversion Angle, and INITIAL Great Circle Track from Point A to Point B?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Change of Longitude (dlong) and Mean Latitude:\n"
        "  - dlong = 030°W - 010°W = 20°.\n"
        "  - Mean Latitude = 50°N (both points are at 50°N).\n\n"
        "Step 2: Calculate Earth Convergence:\n"
        "  - Formula: Earth Convergence = dlong x sin(Mean Latitude)\n"
        "  - Convergence = 20° x sin(50°) = 20° x 0.766 = 15.32° (~15.3°).\n\n"
        "Step 3: Calculate Conversion Angle (CA):\n"
        "  - Formula: Conversion Angle = 0.5 x Convergence\n"
        "  - CA = 0.5 x 15.32° = 7.66° (~7.7°).\n\n"
        "Step 4: Determine Initial Great Circle Track from Point A:\n"
        "  - Flying Westbound in Northern Hemisphere: The Great Circle curves towards the North Pole (curves to the right of the Rhumb Line)!\n"
        "  - Therefore, the initial track points further North (towards 360°/clockwise):\n"
        "  - Initial GC Track = Rhumb Line Track + CA = 270° + 7.7° = 277.7° True!\n"
        "  - (And at Point B, the final GC track will be 270° - 7.7° = 262.3° True!).\n\n"
        "FINAL ANSWER: Earth Convergence = 15.3°; Conversion Angle = 7.7°; Initial Great Circle Track = 277.7° True.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Convergence Zero at Equator Trap",
        "- Earth Convergence = dlong x sin(lat).\n"
        "- At the EQUATOR (lat 0°), sin(0) = 0. Earth Convergence is ZERO! (Meridians are parallel).\n"
        "- At the POLES (lat 90°), sin(90) = 1. Earth Convergence equals dlong!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: What is the Earth Convergence between longitudes 015°W and 045°W at a mean latitude of 30°N?",
         "[A] 30°\n[B] 15° (dlong = 30°, Convergence = 30° x sin(30°) = 30° x 0.5 = 15°)\n[C] 7.5°\n[D] Zero",
         "CORRECT: [B]. dlong = 45° - 15° = 30°. sin(30°) = 0.5. Earth Convergence = 30° x 0.5 = 15°."),
        ("Q2: In the Northern Hemisphere, how does a GREAT CIRCLE track curve relative to the RHUMB LINE connecting the same two points?",
         "[A] Curves towards the South Pole\n[B] CURVES TOWARDS THE NORTH POLE (lies North of the Rhumb Line)\n[C] It is perfectly straight\n[D] Curves randomly",
         "CORRECT: [B]. On a Mercator chart, Great Circles always bow towards the nearer geographic pole relative to the straight rhumb line."),
        ("Q3: What is the relationship between Conversion Angle and Earth Convergence?",
         "[A] Conversion Angle = 2 x Convergence\n[B] CONVERSION ANGLE = HALF OF EARTH CONVERGENCE (CA = 0.5 x Convergence)\n[C] They are identical\n[D] Conversion Angle = sin(lat)",
         "CORRECT: [B]. Conversion Angle is defined as exactly half the Earth Convergence between two positions.")
    ]

    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 2 compiled: {pdf_path}")


def build_gnav_ch03():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch03_magnetism_variation_deviation_compass.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 3: Magnetism & The Compass")

    pdf.add_title_banner(
        "General Navigation",
        3,
        "Earth Magnetism, Deviation & The Direct-Reading Compass",
        "85-128"
    )

    pdf.add_heading_1("1. Earth's Magnetic Field & Terminology")
    pdf.add_paragraph(
        "The Earth behaves as a giant magnetic dipole whose magnetic poles are offset from the true geographic poles:"
    )
    pdf.add_bullet("Magnetic Variation (Declination)", "The angular difference between True North (TN) and Magnetic North (MN). Lines connecting points of equal variation are ISOGONALS. The line of zero variation is the AGONIC LINE.")
    pdf.add_bullet("Compass Deviation", "The angular error between Magnetic North and Compass North caused by internal aircraft magnetism (radios, engines, steel structure). Lines of equal deviation: Isoclinals.")
    pdf.add_bullet("The Navigation Master Chain", "Compass Heading (CH) +- Deviation = Magnetic Heading (MH) +- Variation = True Heading (TH) ('Cadbury Dairy Milk Very Tasty': C -> D -> M -> V -> T). Variation/Deviation West is ADDED; East is SUBTRACTED when converting Compass to True!")

    pdf.add_heading_1("2. Direct-Reading Compass Dynamic Turning & Acceleration Errors")
    pdf.add_paragraph(
        "Due to magnetic dip (the magnetic needle wants to tilt towards the ground), the center of gravity of the magnet is weighted, creating dynamic errors in the Northern Hemisphere:"
    )
    pdf.add_bullet("Turning Errors (UNOS Rule)", "'Undershoot North, Overshoot South'. When turning THROUGH NORTH, the compass leads and turns ahead; you must ROLL OUT EARLY (undershoot). When turning THROUGH SOUTH, the compass lags; you must ROLL OUT LATE (overshoot)!")
    pdf.add_bullet("Acceleration Errors on E/W Headings (ANDS Rule)", "'Accelerate North, Decelerate South'. When accelerating on an East or West heading, the compass swings NORTH; when decelerating, the compass swings SOUTH!")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Complete Compass to True Heading Conversion",
        "SCENARIO (Fundamental Flight Deck Navigation Drill):\n"
        "A pilot reads the direct-reading standby magnetic compass:\n"
        "- Compass Heading (CH) = 085°\n"
        "- Compass Deviation Card indicates: For 090°, Deviation is -3° (3° West)\n"
        "- En-route chart shows local Magnetic Variation = 7° East\n"
        "- Wind drift correction applied: Drift is 5° to the Right\n"
        "QUESTION: Calculate (1) Magnetic Heading, (2) True Heading, and (3) True Track.\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Convert Compass Heading to Magnetic Heading (Apply Deviation):\n"
        "  - Rule: Deviation West is SUBTRACTED when going Compass -> Magnetic? CAUTION!\n"
        "  - Memory Verse: 'Deviation West, Magnetic Best' -> Magnetic is BIGGER (ADD West Deviation)!\n"
        "  - CH (085°) + Dev West (3°) = MH 088° Magnetic!\n\n"
        "Step 2: Convert Magnetic Heading to True Heading (Apply Variation):\n"
        "  - Variation is 7° East.\n"
        "  - Memory Verse: 'Variation East, Magnetic Least' -> Magnetic is SMALLER (True is BIGGER, so ADD East Variation)!\n"
        "  - True Heading = MH (088°) + Var East (7°) = 095° True!\n\n"
        "Step 3: Calculate True Track (Apply Wind Drift):\n"
        "  - True Heading = 095°\n"
        "  - Wind pushes aircraft 5° to the RIGHT (+5° Drift)\n"
        "  - True Track = True Heading + Drift = 095° + 5° = 100° True!\n\n"
        "FINAL ANSWER: Magnetic Heading = 088°; True Heading = 095°; True Track = 100°.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The UNOS Turning Rule Trap",
        "- Turning through NORTH in Northern Hemisphere: Roll out 20° to 30° BEFORE the compass heading (UNDERSHOOT)!\n"
        "- Turning through SOUTH: Roll out 20° to 30° AFTER the compass heading (OVERSHOOT)!\n"
        "- In the Southern Hemisphere, the rules are inverted (USON: Undershoot South, Overshoot North)!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: In the Northern Hemisphere, an aircraft is flying on a heading of 090° (East) and accelerates. What will the direct-reading magnetic compass indicate?",
         "[A] A turn towards South\n[B] A TURN TOWARDS NORTH (ANDS: Accelerate North, Decelerate South)\n[C] It remains stationary\n[D] It oscillates 180°",
         "CORRECT: [B]. Acceleration forces the pendulous compass weight backwards, tilting the needle so the vertical component of Earth's magnetic field pulls the north needle towards the north."),
        ("Q2: What is the name of a line on an aeronautical chart connecting points of ZERO MAGNETIC VARIATION?",
         "[A] Isogonal\n[B] AGONIC LINE\n[C] Isocline\n[D] Aclinic line",
         "CORRECT: [B]. An isogonal is a line of equal variation; the specific isogonal of 0° variation is called the agonic line."),
        ("Q3: If Compass Heading is 320°, Deviation is 2°W, and Variation is 12°W, what is the TRUE HEADING?",
         "[A] 334°\n[B] 306° (West is best: MH = 320 - 2? No, CH + Dev = MH. 320 - 2 = 318 - 12 = 306° True)\n[C] 320°\n[D] 340°",
         "CORRECT: [B]. From Compass to True: CH 320° - 2°W Dev = 318° MH - 12°W Var = 306° True.")
    ]

    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 3 compiled: {pdf_path}")


def build_gnav_ch04():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch04_aeronautical_charts_principles.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 4: Chart Principles & Scale")

    pdf.add_title_banner(
        "General Navigation",
        4,
        "Aeronautical Charts: Principles, Projections & Scale",
        "129-166"
    )

    pdf.add_heading_1("1. The Cartographic Challenge & Conformality")
    pdf.add_paragraph(
        "Because a curved sphere cannot be flattened onto a 2D plane without distortion, chart projections must compromise between shape, area, and scale:"
    )
    pdf.add_bullet("Conformal (Orthomorphic) Charts", "ESSENTIAL FOR AVIATION! At any point, the scale is the same in all directions. Angles and bearings measured on the chart equal angles on the Earth's surface! Meridians and parallels always intersect at 90° right angles.")
    pdf.add_bullet("Equivalent (Equal-Area) Charts", "Preserves relative land areas at the expense of severe angular distortion. UNACCEPTABLE for aviation navigation!")

    pdf.add_heading_1("2. Chart Scale & Representative Fraction (RF)")
    pdf.add_bullet("Representative Fraction (RF)", "Ratio of chart distance to earth distance: Scale = Chart Distance / Earth Distance (both in the SAME units!).")
    pdf.add_bullet("Scale Factor (SF)", "SF = Actual Chart Scale / Nominal Chart Scale. SF = 1.0 along standard parallels/tangent lines where chart touches the globe.")
    pdf.add_bullet("Large Scale vs Small Scale", "Large Scale (e.g. 1:250,000 / 1:500,000): Shows small area with high detail (VFR charts). Small Scale (e.g. 1:2,000,000 / 1:5,000,000): Shows massive area with low detail (En-route / Oceanic charts).")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Earth Distance from Chart Scale",
        "SCENARIO (AviationExam Scale Conversion Problem):\n"
        "On an aeronautical chart with a scale of 1:1,000,000:\n"
        "- The measured distance between two navigation beacons is 7.4 centimeters\n"
        "QUESTION: What is the actual Earth distance between the two beacons in NAUTICAL MILES?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Earth Distance in centimeters using the scale:\n"
        "  - Scale = 1 : 1,000,000 (1 cm on chart = 1,000,000 cm on Earth).\n"
        "  - Earth Distance = 7.4 cm x 1,000,000 = 7,400,000 centimeters.\n\n"
        "Step 2: Convert centimeters to meters:\n"
        "  - 1 meter = 100 cm.\n"
        "  - Earth Distance (meters) = 7,400,000 cm / 100 = 74,000 meters (74.0 km).\n\n"
        "Step 3: Convert meters to Nautical Miles:\n"
        "  - Rule: 1 Nautical Mile = exactly 1,852 meters.\n"
        "  - Earth Distance (NM) = 74,000 meters / 1,852 meters per NM\n"
        "  - Earth Distance = 39.956 NM (~40.0 Nautical Miles)!\n\n"
        "FINAL ANSWER: The actual Earth distance between the two beacons is 40 Nautical Miles.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Scale Ratio Units Trap",
        "- The Representative Fraction (1:1,000,000) has NO UNITS!\n"
        "- 1 cm = 1,000,000 cm. 1 inch = 1,000,000 inches.\n"
        "- Always convert Earth units into meters first, then divide by 1,852 to get Nautical Miles!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch04 = [
        ("Q1: What is the primary characteristic of an 'ORTHOMORPHIC' (conformal) aeronautical chart?",
         "[A] True areas are preserved everywhere\n[B] ANGLES AND BEARINGS are accurately preserved, and meridians and parallels intersect at 90° angles\n[C] Scale is identical across the entire map\n[D] Great circles are curved",
         "CORRECT: [B]. Conformal charts preserve local shapes and angular relationships, allowing pilots to measure true bearings directly on the chart with a protractor."),
        ("Q2: On a chart with a scale of 1:500,000, what Earth distance in Nautical Miles is represented by a chart measurement of 18.52 cm?",
         "[A] 50 NM (18.52 cm x 500,000 = 9,260,000 cm = 92,600 m / 1,852 m = 50 NM)\n[B] 100 NM\n[C] 25 NM\n[D] 18.5 NM",
         "CORRECT: [A]. 18.52 cm x 500,000 = 92,600 meters. Dividing by 1,852 m/NM yields exactly 50 NM."),
        ("Q3: What happens to the detail and geographic coverage in a 'LARGE SCALE' chart compared to a 'SMALL SCALE' chart?",
         "[A] Covers a large area with low detail\n[B] Covers a SMALL GEOGRAPHIC AREA with HIGH DETAIL and features\n[C] It has no coordinates\n[D] Only used for space flight",
         "CORRECT: [B]. Large scale means a large fraction (e.g. 1/250,000 > 1/2,000,000), covering small areas in rich detail.")
    ]

    for q_text, opts, exp in questions_ch04:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 4 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_gnav_ch01()
    build_gnav_ch02()
    build_gnav_ch03()
    build_gnav_ch04()
