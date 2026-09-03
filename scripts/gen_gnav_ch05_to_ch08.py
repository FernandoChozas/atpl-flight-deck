#!/usr/bin/env python3
"""
Generator for Subject 061: General Navigation
Volume 2: Chapters 5 to 8
- Chapter 5: Mercator & Transverse Mercator Projections (Scale & Rhumb Lines)
- Chapter 6: Lambert Conformal Conic Projection (Constant of Cone & Meridians)
- Chapter 7: Polar Stereographic Projection (Transpolar Flight Planning)
- Chapter 8: Grid Navigation (High-Latitude & Polar Heading Conversion)

Features Step-by-Step Worked Examples ("For Dummies" / Paso a Paso) for all calculation types.
Fully aligned with CAE Oxford General Navigation and EASA ATPL ECQB syllabus.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_4/061_general_navigation"

def build_gnav_ch05():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch05_mercator_transverse_projections.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 5: Mercator Projections")

    pdf.add_title_banner(
        "General Navigation",
        5,
        "Mercator & Transverse Mercator Projections",
        "167-206"
    )

    pdf.add_heading_1("1. The Direct Mercator Projection Architecture")
    pdf.add_paragraph(
        "The Direct Mercator is a cylindrical conformal projection where the cylinder is tangent to the globe along the Equator:"
    )
    pdf.add_bullet("Meridians & Parallels", "Meridians are parallel, equidistant straight vertical lines. Parallels are straight horizontal lines whose spacing EXPANDS rapidly away from the Equator!")
    pdf.add_bullet("Rhumb Lines (The Great Benefit)", "RHUMB LINES ARE STRAIGHT LINES! A straight line drawn between any two points represents a constant compass track. This made Mercator the supreme marine and navigation chart for centuries.")
    pdf.add_bullet("Great Circles on Mercator", "Great Circles are CURVED LINES, bowing towards the nearer pole (lying on the polar side of the rhumb line).")
    pdf.add_bullet("Scale Variation", "Scale is correct at the Equator (SF = 1.0), and expands with the secant of latitude: Scale at Latitude = Scale at Equator x sec(Latitude) = Scale at Equator / cos(Latitude)!")

    pdf.add_heading_1("2. Transverse Mercator Projection")
    pdf.add_paragraph(
        "The cylinder is rotated 90° so it is tangent along a SINGLE MERIDIAN (the Central Meridian):"
    )
    pdf.add_bullet("Usage", "Ideal for North-South flight corridors, topographical national grid surveys (OSGB, UTM), and high-latitude strip charts within 3° of the Central Meridian.")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Calculating Mercator Chart Scale at High Latitude",
        "SCENARIO (Standard EASA Chart Scale Problem):\n"
        "A Direct Mercator chart has a nominal scale of 1:2,000,000 at the Equator:\n"
        "QUESTION: What is the actual chart scale at 60° North latitude?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Recall the Mercator Scale Expansion Formula:\n"
        "  - Scale at Latitude = Scale at Equator x sec(Latitude)\n"
        "  - Or in Representative Fraction (RF) denominator terms:\n"
        "  - Denominator at Latitude = Denominator at Equator x cos(Latitude)!\n\n"
        "Step 2: Plug in the numbers for 60° Latitude:\n"
        "  - Denominator at Equator = 2,000,000\n"
        "  - Latitude = 60°N -> cos(60°) = 0.50 exactly!\n"
        "  - Denominator at 60°N = 2,000,000 x 0.50 = 1,000,000!\n\n"
        "Step 3: State the New Scale:\n"
        "  - New Scale at 60°N = 1 : 1,000,000!\n\n"
        "Step 4: Physical Meaning for Dummies:\n"
        "  - The scale is twice as large (features appear twice as big on paper) at 60°N than at the Equator, because land masses are stretched by a factor of 1/cos(60°) = 2.0!\n\n"
        "FINAL ANSWER: The scale at 60°N is 1:1,000,000.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Scale Fraction vs Denominator Trap",
        "- When scale 'EXPANDS' (gets larger), the DENOMINATOR GETS SMALLER!\n"
        "- 1:1,000,000 is a LARGER scale than 1:2,000,000.\n"
        "- Do not multiply the denominator by sec(lat); multiply the denominator by cos(lat)!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch05 = [
        ("Q1: On a Direct Mercator chart, how do RHUMB LINES appear?",
         "[A] Complex sine curves\n[B] STRAIGHT LINES\n[C] Circles centered on the pole\n[D] Parabolas",
         "CORRECT: [B]. The unique defining property of the Mercator projection is that any straight line drawn across it intersects all meridians at a constant angle, representing a rhumb line."),
        ("Q2: How does a GREAT CIRCLE track between two airports in the Northern Hemisphere appear on a Direct Mercator chart?",
         "[A] A straight line\n[B] A CURVED LINE curving towards the North Pole (convex to the Equator)\n[C] A curved line convex to the pole\n[D] A vertical line",
         "CORRECT: [B]. Because the Mercator projection stretches higher latitudes, a Great Circle curves northward, bowing away from the Equator towards the pole."),
        ("Q3: At what latitude on a Direct Mercator chart is the scale exactly DOUBLE the scale at the Equator?",
         "[A] 30°\n[B] 60° (sec(60°) = 1 / cos(60°) = 1 / 0.50 = 2.0)\n[C] 45°\n[D] 90°",
         "CORRECT: [B]. Since scale expands as sec(lat), at 60° latitude sec(60°) = 2.0, meaning the scale is exactly twice as large as at the Equator.")
    ]

    for q_text, opts, exp in questions_ch05:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 5 compiled: {pdf_path}")


def build_gnav_ch06():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch06_lambert_conformal_conic.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 6: Lambert Conformal Conic")

    pdf.add_title_banner(
        "General Navigation",
        6,
        "Lambert Conformal Conic Projection",
        "207-248"
    )

    pdf.add_heading_1("1. The Standard Aviation Chart Architecture")
    pdf.add_paragraph(
        "The Lambert Conformal Conic is the primary chart used for aeronautical plotting and mid-latitude IFR airways. It uses a secant cone intersecting the globe at two Standard Parallels (SP1 and SP2):"
    )
    pdf.add_bullet("Meridians & Parallels", "Meridians are straight lines converging at the pole vertex. Parallels are concentric circular arcs centered on the vertex.")
    pdf.add_bullet("Great Circles on Lambert", "GREAT CIRCLES ARE VIRTUALLY STRAIGHT LINES! (Maximum deviation from a straight line over 1,000 NM is negligible).")
    pdf.add_bullet("Rhumb Lines on Lambert", "Rhumb lines are CURVED LINES, concave to the pole of projection.")
    pdf.add_bullet("Scale Factor (SF)", "SF = 1.0 along the two Standard Parallels. SF < 1.0 between the standard parallels (chart is compressed). SF > 1.0 outside the standard parallels (chart expands).")

    pdf.add_heading_1("2. Constant of the Cone & Chart Convergence")
    pdf.add_bullet("Constant of the Cone (n)", "The convergence factor of the cone: n = sin(Parallel of Origin) = sin(mean latitude of standard parallels). E.g. For standard parallels at 30° and 60°, mean lat = 45°, n = sin(45°) = 0.7071.")
    pdf.add_bullet("Chart Convergence Formula", "Chart Convergence (degrees) = Change of Longitude (dlong) x n = dlong x sin(Parallel of Origin)")

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Finding Chart Convergence & Great Circle Bearing on Lambert",
        "SCENARIO (Classic ATPL Lambert Chart Drill):\n"
        "A Lambert Conformal Conic chart has standard parallels at 37°N and 65°N, giving a constant of the cone n = 0.788:\n"
        "- Waypoint A: 50°N 020°W\n"
        "- Waypoint B: 50°N 060°W\n"
        "- A straight line is drawn on the chart from A to B\n"
        "- The measured track angle on the chart at meridian 020°W (Point A) is 260° True\n"
        "QUESTION: What is the chart convergence between A and B, and what will be the measured track angle at Point B (060°W)?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Change in Longitude (dlong):\n"
        "  - dlong = 060°W - 020°W = 40°.\n\n"
        "Step 2: Calculate Chart Convergence using the Constant of the Cone (n):\n"
        "  - Formula: Chart Convergence = dlong x n\n"
        "  - Chart Convergence = 40° x 0.788 = 31.52° (~31.5°)!\n\n"
        "Step 3: Determine Track Direction Evolution from Point A to Point B:\n"
        "  - You are flying WESTBOUND in the Northern Hemisphere.\n"
        "  - Meridians converge towards the North Pole at the top of the chart.\n"
        "  - As you fly West along a straight line on a Lambert chart, the track angle relative to meridians DECREASES:\n"
        "  - Track at Point B = Track at Point A - Chart Convergence\n"
        "  - Track at Point B = 260.0° - 31.5° = 228.5° True!\n\n"
        "FINAL ANSWER: Chart Convergence = 31.5°. Measured track at Point B = 228.5° True.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "Earth Convergence vs Chart Convergence Trap",
        "- Earth Convergence = dlong x sin(lat). It varies with every degree of latitude!\n"
        "- Chart Convergence on Lambert = dlong x n. It is CONSTANT EVERYWHERE on the chart because 'n' is fixed!\n"
        "- On the parallel where sin(lat) = n, Earth Convergence equals Chart Convergence.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch06 = [
        ("Q1: On a Lambert Conformal Conic chart, what type of line does a STRAIGHT LINE represent?",
         "[A] A rhumb line\n[B] A GREAT CIRCLE (with negligible deviation)\n[C] A parallel of latitude\n[D] An isogonal",
         "CORRECT: [B]. The Lambert projection is constructed so that a straight line drawn between any two points closely approximates a Great Circle track."),
        ("Q2: A Lambert chart has a constant of the cone n = 0.75. Between longitudes 010°E and 030°E, what is the CHART CONVERGENCE?",
         "[A] 20°\n[B] 15° (dlong = 20° x 0.75 = 15°)\n[C] 7.5°\n[D] 30°",
         "CORRECT: [B]. Chart Convergence = dlong x n = (30° - 10°) x 0.75 = 20° x 0.75 = 15°."),
        ("Q3: Where on a Lambert Conformal Conic chart is the Scale Factor (SF) LESS THAN 1.0?",
         "[A] North of the northern standard parallel\n[B] BETWEEN THE TWO STANDARD PARALLELS\n[C] Outside both standard parallels\n[D] Exactly along the standard parallels",
         "CORRECT: [B]. Because the cone cuts inside the sphere between the two standard parallels, the map features are slightly compressed (SF < 1.0). Along the standard parallels, SF = 1.0.")
    ]

    for q_text, opts, exp in questions_ch06:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 6 compiled: {pdf_path}")


def build_gnav_ch07():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch07_polar_stereographic_projection.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 7: Polar Stereographic")

    pdf.add_title_banner(
        "General Navigation",
        7,
        "Polar Stereographic Projection (Polar Navigation)",
        "249-286"
    )

    pdf.add_heading_1("1. The Polar Stereographic Architecture")
    pdf.add_paragraph(
        "The Polar Stereographic is an azimuthal conformal projection where the projection plane is tangent at the geographic pole, with the perspective projection point at the opposite pole:"
    )
    pdf.add_bullet("Meridians & Parallels", "Meridians are straight lines radiating outward from the pole at their true angular spacing (360°). Parallels are concentric circles centered on the pole.")
    pdf.add_bullet("Constant of the Cone", "The convergence factor n = 1.0! Chart Convergence = dlong x 1.0 = dlong. Chart convergence equals the full change of longitude everywhere on the chart!")
    pdf.add_bullet("Great Circles on Polar Stereographic", "Great Circles are virtually STRAIGHT LINES near the pole (technically circular arcs concave to the pole).")
    pdf.add_bullet("Scale Factor (SF)", "SF = 1.0 at the pole. Scale expands away from the pole: Scale Factor = 2 / (1 + sin(lat)). At 60°N, SF = 2 / (1 + 0.866) = 1.07 (+7% expansion).")

    pdf.add_heading_1("2. Transpolar Flight Operations")
    pdf.add_paragraph(
        "Polar Stereographic charts are mandatory for transpolar airline routes (e.g. Europe to Far East over the Arctic Ocean), where standard magnetic compasses and Mercator charts become completely unusable."
    )

    pdf.add_heading_1("3. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Track Change on Polar Stereographic Chart",
        "SCENARIO (Transpolar Flight Planning Drill):\n"
        "An aircraft is flying a straight track across a North Polar Stereographic chart:\n"
        "- Crossing Meridian 030°W, the measured true track is 080° True\n"
        "QUESTION: What will be the true track of the aircraft when it crosses Meridian 050°E along the same straight line?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Calculate the Change in Longitude (dlong):\n"
        "  - Longitude 1 = 030°W\n"
        "  - Longitude 2 = 050°E\n"
        "  - Points are in opposite hemispheres, so ADD: dlong = 30° + 50° = 80°.\n\n"
        "Step 2: Calculate Chart Convergence on Polar Stereographic (n = 1.0):\n"
        "  - Chart Convergence = dlong x n = 80° x 1.0 = 80.0°!\n\n"
        "Step 3: Calculate the New Track crossing 050°E:\n"
        "  - Flying from West longitude to East longitude across the pole, the track angle decreases:\n"
        "  - Track at 050°E = Initial Track - Convergence\n"
        "  - Track = 080° - 80° = 000° True (due North)!\n\n"
        "FINAL ANSWER: True track at 050°E is 000° True.",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The Polar Stereographic n = 1.0 Trap",
        "- On a Polar Stereographic chart, n is ALWAYS 1.0!\n"
        "- Chart Convergence ALWAYS equals Change of Longitude (dlong)!\n"
        "- This is the simplest chart calculation in ATPL navigation.",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch07 = [
        ("Q1: On a Polar Stereographic chart, what is the value of the Convergence Factor (Constant of the Cone n)?",
         "[A] 0.50\n[B] EXACTLY 1.0\n[C] 0.707\n[D] Zero",
         "CORRECT: [B]. The plane is tangent at the pole (latitude 90°); sin(90°) = 1.0. Therefore n = 1.0, and chart convergence equals dlong."),
        ("Q2: How do parallels of latitude appear on a Polar Stereographic projection?",
         "[A] Straight parallel lines\n[B] CONCENTRIC CIRCLES centered on the pole\n[C] Curved lines concave to equator\n[D] Hyperbolas",
         "CORRECT: [B]. Parallels form concentric circles around the pole, with spacing increasing slightly away from the center."),
        ("Q3: Where is the Scale Factor (SF) equal to exactly 1.0 on a direct Polar Stereographic chart?",
         "[A] At the Equator\n[B] AT THE POLE (Point of Tangency)\n[C] At 60° latitude\n[D] At the opposite pole",
         "CORRECT: [B]. The projection plane is tangent to the Earth at the pole, where there is zero scale distortion (SF = 1.0).")
    ]

    for q_text, opts, exp in questions_ch07:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 7 compiled: {pdf_path}")


def build_gnav_ch08():
    pdf_path = os.path.join(OUTPUT_DIR, "061_ch08_grid_navigation_polar.pdf")
    pdf = PDFBuilder("General Navigation", "061", "Chapter 8: Grid Navigation")

    pdf.add_title_banner(
        "General Navigation",
        8,
        "Grid Navigation (Polar Heading Conversion & Isogrivs)",
        "287-324"
    )

    pdf.add_heading_1("1. Why Grid Navigation?")
    pdf.add_paragraph(
        "Near the geographic poles, magnetic compasses are useless due to vertical magnetic dip, and true meridians converge so rapidly that a straight flight path experiences massive changes in true heading every few minutes:"
    )
    pdf.add_bullet("The Grid Concept", "A rectangular grid is superimposed over the polar chart. All grid vertical lines are drawn parallel to the Greenwich Meridian (000° Longitude). The direction towards the North Pole along the Greenwich Meridian is defined as GRID NORTH.")
    pdf.add_bullet("Grid Heading / Track Formula (Northern Hemisphere)", "Grid Track = True Track +- Longitude. Memory rule: In West Longitude, Grid Track = True Track - West Longitude. In East Longitude, Grid Track = True Track + East Longitude ('Grid North Is Less In West' -> G = T - W; G = T + E).")
    pdf.add_bullet("Isogrivs & Grivation", "Grivation is the angle between Compass/Magnetic North and Grid North: Grivation = Variation +- Convergence. Lines connecting points of equal grivation are ISOGRIVS.")

    pdf.add_heading_1("2. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Converting True Track to Grid Track",
        "SCENARIO (Polar Navigation Route Clearance Drill):\n"
        "An aircraft is flying over northern Canada:\n"
        "- Current position: 75°N 110°W\n"
        "- Aircraft True Track = 060° True\n"
        "QUESTION: What is the corresponding GRID TRACK to select on the autopilot/FMC?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Identify the Longitude and Hemisphere:\n"
        "  - Longitude = 110° WEST.\n\n"
        "Step 2: Recall the Grid Conversion Formula for the Northern Hemisphere:\n"
        "  - Memory Rule: 'Grid Is Less In West' (Subtract West Longitude!)\n"
        "  - Formula: Grid Track = True Track - West Longitude\n\n"
        "Step 3: Plug in the numbers:\n"
        "  - True Track = 060°\n"
        "  - Longitude = 110°\n"
        "  - Grid Track = 060° - 110° = -050°.\n\n"
        "Step 4: Normalize negative angles to standard 360° compass format:\n"
        "  - Add 360°: -050° + 360° = 310° Grid!\n\n"
        "FINAL ANSWER: Grid Track = 310° Grid. Flying 310° Grid will keep the aircraft flying in a perfectly straight line over the pole without touching heading knobs!",
        max_chars=86
    )

    pdf.add_callout(
        "trap",
        "The West Longitude Subtraction Trap",
        "- Northern Hemisphere: Grid = True - West Longitude (or True + East Longitude).\n"
        "- If the result is negative, simply add 360°!\n"
        "- In the Southern Hemisphere, the rule reverses: Grid = True + West Longitude.",
        max_chars=86
    )

    pdf.add_heading_1("3. AviationExam Practice Questions (with Explanations)")
    questions_ch08 = [
        ("Q1: On a Polar Grid chart in the Northern Hemisphere, what meridian defines the direction of GRID NORTH?",
         "[A] The 180° Antimeridian\n[B] The GREENWICH MERIDIAN (000° Longitude)\n[C] Magnetic North Pole\n[D] The Equator",
         "CORRECT: [B]. Grid North is defined by lines parallel to the Prime Meridian (000°), pointing towards the North Pole along the Greenwich Meridian."),
        ("Q2: In the Northern Hemisphere at position 80°N 040°W, an aircraft is flying on a True Track of 120°. What is the GRID TRACK?",
         "[A] 160°\n[B] 080° (Grid = True - West Longitude = 120° - 40° = 080° Grid)\n[C] 040°\n[D] 200°",
         "CORRECT: [B]. Using the rule 'Grid is Less in West': Grid Track = True Track - West Longitude = 120° - 40° = 080° Grid."),
        ("Q3: What are lines on an aeronautical chart connecting points of EQUAL GRIVATION called?",
         "[A] Isogonals\n[B] ISOGRIVS\n[C] Isoclines\n[D] Agonic lines",
         "CORRECT: [B]. Isogrivs are lines of equal grivation (the angular difference between magnetic direction and grid direction).")
    ]

    for q_text, opts, exp in questions_ch08:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"General Navigation Chapter 8 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_gnav_ch05()
    build_gnav_ch06()
    build_gnav_ch07()
    build_gnav_ch08()
