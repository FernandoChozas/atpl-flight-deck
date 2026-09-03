#!/usr/bin/env python3
"""
Generator for Subject 021: AGK - Airframe, Systems, Electrics & Powerplant
Volume 1: Chapters 01 to 03
- Chapter 01: Fuselage, Wings and Stabilizing Surfaces
- Chapter 02: Basic Hydraulics (Fluids, Pumps, Actuators & Accumulators)
- Chapter 03: Landing Gear, Wheels, Tyres & Brakes

Fully aligned with CAE Oxford Book 2 (Airframes and Systems) and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant"

def build_agk_ch01():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch01_fuselage_wings_surfaces.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 1: Fuselage, Wings and Stabilizing Surfaces")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        1,
        "Fuselage, Wings and Stabilizing Surfaces",
        "1-46"
    )

    pdf.add_heading_1("1. Structural Loads, Stresses & Combination Forces")
    pdf.add_paragraph(
        "Aircraft structures must withstand five primary mechanical stresses during flight and ground maneuvers. "
        "Every structural component is engineered to maintain aerodynamic integrity without permanent deformation up to the "
        "Limit Load, and without catastrophic structural failure up to the Ultimate Load (Ultimate Load = 1.5 x Limit Load):"
    )

    loads_data = [
        ["Tension", "Forces acting along the same axis pulling apart (stretching).", "Lower wing skin during positive-g flight (+2.5g); fuselage skin under cabin pressurization."],
        ["Compression", "Forces acting along the same axis pushing together (shortening).", "Upper wing skin during positive-g flight; landing gear shock struts on touchdown."],
        ["Shear", "Forces acting in opposite parallel directions causing sliding of adjacent planes.", "Riveted joints and bolts securing skin panels to spar booms; wing spar webs."],
        ["Torsion", "Twisting moment caused by an externally applied torque.", "Wing structure when ailerons deflect; propeller blades; engine torque reaction on engine mounts."],
        ["Bending", "Combination of tension on one side and compression on the opposite side.", "Wing flexure in flight: upper skin experiences compression (buckling risk), lower skin experiences tension (fatigue cracking risk)."]
    ]
    pdf.add_table(["Stress Type", "Mechanical Action", "Aircraft Structural Examples & Occurrence"], loads_data, col_widths=[90.0, 190.0, 220.0])

    pdf.add_callout(
        "trap",
        "Structural Safety Margins (CS-25 / FAR-25)",
        "- Limit Load: The maximum load anticipated in normal operational service. The structure must withstand limit load without PERMANENT DEFORMATION.\n"
        "- Ultimate Load: Limit Load multiplied by the Factor of Safety (Factor of Safety = 1.50). The structure must withstand ultimate load for AT LEAST 3 SECONDS without failure/rupture, though permanent deformation is permitted!\n"
        "- Positive Limit Load Factor for Transport Category (CS-25): Clean configuration = +2.5g; Flaps extended = +2.0g.",
        max_chars=86
    )

    pdf.add_heading_1("2. Fuselage Construction & Pressurization Features")
    pdf.add_paragraph(
        "Modern transport aircraft utilize semi-monocoque construction to achieve an optimal balance between structural rigidity, "
        "useful cabin internal volume, and damage tolerance:"
    )
    pdf.add_bullet("Truss (Framework)", "Welded steel-tubing structure with non-structural fabric covering. Used only in vintage or light aerobatic aircraft.")
    pdf.add_bullet("True Monocoque", "The skin carries all tensile, compressive, and shear loads. Light formers provide cross-sectional shape, but there are no longitudinal stringers. Highly vulnerable: any localized dent or scratch causes catastrophic buckling under compression.")
    pdf.add_bullet("Semi-Monocoque", "The modern commercial standard. The thin metal or composite skin carries shear and cabin hoop stress, while longitudinal stringers and longerons carry bending/axial tension and compression. Transverse frames and bulkheads maintain cross-sectional circular profile.")

    fuse_table = [
        ["Longerons & Stringers", "Longitudinal stiffeners running along the fuselage.", "Longerons carry heavy bending loads; stringers prevent skin wrinkling and divide skin into smaller panels."],
        ["Frames & Formers", "Transverse structural rings maintaining fuselage shape.", "Distribute concentrated floor, wing, and tail loads into the skin."],
        ["Pressure Bulkheads", "Dome-shaped (spherical/toroidal) front and rear pressure caps.", "Converts internal cabin differential air pressure into pure membrane TENSION (domed shape prevents bending stresses)."],
        ["Plug-Type Doors", "Passenger and cargo doors designed larger than the fuselage frame cutout.", "Internal cabin pressure forces the door firmly into its tapered surround. Impossible to open in flight when cabin is pressurized. Inward-moving or rotating stops mandatory."],
        ["Pressurized Windows", "Multi-layer acrylic window assemblies.", "Consists of outer structural pane (holds 1.5x max diff), inner structural pane (also holds 1.5x max diff), and non-structural scratch pane. A small breather hole in the inner pane ensures outer pane carries normal pressure load."]
    ]
    pdf.add_table(["Component", "Structural Role", "Operational & Failure Nuance"], fuse_table, col_widths=[120.0, 180.0, 200.0])

    pdf.add_heading_1("3. Wing Structural Architecture & Cantilever Design")
    pdf.add_paragraph(
        "Commercial transport wings are cantilever beams (internally supported without external bracing struts or wires). "
        "The wing internal structure consists of three principal structural members:"
    )
    pdf.add_bullet("Wing Spars", "Primary longitudinal structural members extending root-to-tip. Composed of upper and lower spar booms (caps) that resist wing bending moments, connected by a vertical shear web that resists vertical aerodynamic shear loads.")
    pdf.add_bullet("Wing Ribs", "Transverse chordwise members that maintain aerodynamic camber, transfer skin airloads into the spars, and act as tank surge baffles to prevent dynamic fuel sloshing during turbulence and maneuvers.")
    pdf.add_bullet("Torsion Box (Wing Box)", "Enclosed structural cell formed by front spar, rear spar, ribs, and upper/lower skins. Resists severe torsional twisting moments generated by ailerons, spoilers, and aerodynamic center-of-pressure shifts.")

    pdf.add_heading_1("4. Structural Design Philosophies: Safe-Life vs Fail-Safe vs Damage Tolerant")
    philosophy_data = [
        ["Safe-Life", "Component is certified to operate for a fixed, predetermined number of flight hours/landings, after which it MUST BE DISCARDED regardless of condition.", "Applies to high-stress landing gear components, engine mounts, and helicopter rotor hubs where alternate load paths are physically impossible."],
        ["Fail-Safe", "Structure incorporates multiple redundant load paths or structural dividers.", "If one structural element fractures (e.g. one cap of a multi-part spar), the remaining structure carries the load safely until the next scheduled maintenance check."],
        ["Damage Tolerant", "Modern CS-25/FAR-25 philosophy. Assumes micro-cracks and flaws WILL develop in service.", "Structure incorporates crack-stoppers and low crack-propagation materials. Crack growth rates are scientifically calculated to guarantee cracks remain detectable before reaching critical length."]
    ]
    pdf.add_table(["Design Concept", "Engineering Principle", "Maintenance & Operational Criterion"], philosophy_data, col_widths=[105.0, 195.0, 200.0])

    pdf.add_heading_1("5. Aircraft Materials, Composites & Corrosion Mechanisms")
    pdf.add_paragraph(
        "Modern airframes blend aluminum alloys, titanium, and advanced composite materials (CFRP, GFRP, Kevlar):"
    )
    pdf.add_bullet("Aluminum Alloys", "2000 series (Copper) and 7000 series (Zinc). Excellent strength-to-weight ratio, but highly susceptible to corrosion. Protected by Alclad (pure aluminum protective skin coating) and anodizing.")
    pdf.add_bullet("Titanium Alloys", "High tensile strength, exceptional corrosion resistance, and retains structural strength at elevated temperatures (up to 400°C). Used for engine firewalls, pylon attachments, and heavy landing gear truck beams.")
    pdf.add_bullet("Composites (CFRP / Kevlar)", "Carbon fibers embedded in epoxy resin matrix. High specific strength, zero corrosion, and fatigue-resistant. Disadvantages: low impact resistance (internal delamination without visible surface damage from tool drops) and non-conductive (requires embedded bronze/copper wire mesh for lightning dissipation).")
    pdf.add_bullet("Galvanic Corrosion", "Occurs when two dissimilar metals (e.g. aluminum and steel or carbon composite) are in electrical contact in the presence of an electrolyte (moisture). The more active metal (anode, e.g. aluminum) corrodes rapidly.")

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch01 = [
        ("Q1: What is the primary operational advantage of a 'plug-type' passenger cabin door in a pressurized transport aircraft?",
         "[A] It opens faster in an emergency evacuation\n[B] Cabin internal pressure forces the door firmly into its tapered frame, preventing accidental opening in flight\n[C] It requires no mechanical hinges\n[D] It allows lower fuselage aerodynamic drag",
         "CORRECT: [B]. Plug-type doors are sized larger than their frame cutouts. Internal cabin differential pressure pushes the door outwards against the fuselage frame stops, making mechanical opening physically impossible at cruising altitude."),
        ("Q2: Under CS-25 certification specifications, what is the definition of 'Ultimate Load'?",
         "[A] Limit load multiplied by a safety factor of 1.50\n[B] The maximum load expected in normal operational life\n[C] The load at which permanent deformation first occurs\n[D] Twice the limit load",
         "CORRECT: [A]. Ultimate Load = Limit Load x 1.50 (Factor of Safety). The airframe must withstand ultimate load for at least 3 seconds without catastrophic structural failure."),
        ("Q3: What is the primary structural function of wing ribs in a transport category aircraft?",
         "[A] Carrying the primary wing bending moment\n[B] Giving the wing its aerodynamic profile and transferring skin loads to the spar booms\n[C] Acting as engine pylon attachments only\n[D] Preventing flutter at high Mach numbers",
         "CORRECT: [B]. Wing ribs define the camber/profile of the airfoil, support the skin against buckling, and transmit distributed aerodynamic lift forces directly to the spar webs and booms."),
        ("Q4: Which design philosophy is characterized by mandating the retirement of a component after a specified number of flight hours, even if free of defects?",
         "[A] Damage Tolerant\n[B] Fail-Safe\n[C] Safe-Life\n[D] On-Condition",
         "CORRECT: [C]. The Safe-Life philosophy requires mandatory component retirement upon reaching a specified service life (hours or cycles), regardless of physical appearance or condition."),
        ("Q5: In a pressurized aircraft passenger window, what is the operational purpose of the tiny breather hole in the inner pane?",
         "[A] To let fresh air into the passenger cabin\n[B] To equalize pressure so the outer pane carries normal cabin differential pressure and prevent misting\n[C] To allow flight attendants to clean between panes\n[D] To relieve cabin overpressure during rapid ascent",
         "CORRECT: [B]. The breather hole vents the cavity between panes to cabin pressure, ensuring the thicker outer pane carries the full differential load while keeping the space dry and clear of condensation."),
        ("Q6: Why must an electrical conductive wire mesh be embedded in the outer composite skin of modern aircraft (e.g. Boeing 787 / Airbus A350)?",
         "[A] To increase cabin Wi-Fi reception\n[B] To conduct and dissipate lightning strike currents safely to the static dischargers, preventing explosive delamination\n[C] To heat the skin for de-icing\n[D] To add tensile strength to the carbon fibers",
         "CORRECT: [B]. Carbon fiber composite has high electrical resistance. A lightning strike without a protective conductive surface mesh (copper/bronze) would cause explosive vaporization of the epoxy resin matrix.")
    ]

    for q_text, opts, exp in questions_ch01:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 1 compiled: {pdf_path}")


def build_agk_ch02():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch02_basic_hydraulics.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 2: Basic Hydraulics")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        2,
        "Basic Hydraulics (Fluids, Pumps & Accumulators)",
        "47-98"
    )

    pdf.add_heading_1("1. Fundamental Hydraulic Principles & Pascal's Law")
    pdf.add_paragraph(
        "Hydraulic systems transmit power through the medium of an incompressible liquid. Under Pascal's Law, "
        "pressure applied to an enclosed liquid is transmitted equally and undiminished in all directions, acting at right angles to the container walls:"
    )
    pdf.add_bullet("Formula for Pressure", "Pressure (P) = Force (F) / Area (A). Units: PSI (Pounds per Square Inch) or Bar (1 bar = 14.5 psi). Standard commercial aircraft operate at 3,000 psi (e.g. A320, B737, B777) or 5,000 psi (A380, B787, A350).")
    pdf.add_bullet("Mechanical Advantage", "Force Out = Pressure x Area Out. By using a small input piston and a large actuator piston, massive output forces are generated, allowing effortless movement of primary flight controls under heavy aerodynamic loads.")
    pdf.add_bullet("Work & Displacement", "Work In = Work Out (Force x Distance). Liquid displaced by the small piston equals liquid moved into the large actuator: a small force moved over a long distance creates a large force moved over a short distance.")

    pdf.add_heading_1("2. STEP-BY-STEP WORKED EXAMPLE (FOR DUMMIES / PASO A PASO)")
    pdf.add_callout(
        "definition",
        "PRACTICAL CALCULATION: Pascal's Law and Hydraulic Force Multiplier",
        "SCENARIO (Fundamental Aviation Hydraulic Calculation):\n"
        "A transport aircraft hydraulic system operates at 3,000 PSI (Pounds per Square Inch):\n"
        "- A flight control actuator cylinder has a piston face area A = 5 square inches (sq in)\n"
        "- The pilot commands an elevator deflection under high dynamic pressure cruise\n"
        "QUESTION: What is the total linear mechanical force generated by this hydraulic actuator on the flight control surface?\n\n"
        "SOLUTION PASO A PASO (FOR DUMMIES):\n"
        "Step 1: Identify Pascal's Master Equation:\n"
        "  - Pressure = Force / Area  -->  Force = Pressure x Area\n\n"
        "Step 2: Plug in the Known Operating Values:\n"
        "  - Hydraulic Operating Pressure (P) = 3,000 PSI\n"
        "  - Actuator Working Area (A) = 5 sq in\n\n"
        "Step 3: Calculate the Resulting Output Force:\n"
        "  - Force = 3,000 lb/sq in x 5 sq in = 15,000 POUNDS OF FORCE (lbf)!\n"
        "  - In metric conversion (1 lbf = 4.448 N):\n"
        "  - Force = 15,000 x 4.448 N = 66,720 Newtons (~66.7 kN)!\n\n"
        "FINAL ANSWER: The actuator exerts 15,000 lbs (over 6.8 tonnes) of force on the elevator surface! This demonstrates how a compact 5-inch piston under 3,000 PSI effortlessly deflects massive flight surfaces against high-speed aerodynamic slipstream loads that no human pilot could move manually!",
        max_chars=86
    )

    pdf.add_heading_1("3. Hydraulic Fluids: Mineral vs Synthetic (Skydrol)")
    pdf.add_paragraph(
        "Aviation hydraulic fluids must possess low viscosity change across extreme temperature ranges (-55°C to +130°C), "
        "high flash points, anti-foaming characteristics, and high lubricity. Two incompatible fluid types exist:"
    )
    fluids_table = [
        ["Base Composition", "Refined petroleum mineral base with chemical additives.", "Synthetic phosphate-ester chemical base."],
        ["Color Code", "DYED RED (to prevent servicing errors).", "DYED PURPLE (or green in older Type IV formulations)."],
        ["Flammability", "Flammable! Flash point ~105°C; auto-ignition ~230°C.", "Fire-resistant! Flash point > 175°C; auto-ignition > 475°C."],
        ["Seal Compatibility", "Nitrile rubber (Buna-N), Neoprene.", "Ethylene Propylene Diene Monomer (EPDM), Butyl, Teflon. DESTROYS natural rubber and Neoprene!"],
        ["Toxicity & Hazards", "Low toxicity; mild skin irritation.", "HIGHLY TOXIC & CORROSIVE! Causes severe eye pain/stinging; damages aircraft acrylics and paint (requires polyurethane paint). Flush immediately with copious water!"]
    ]
    pdf.add_table(["Parameter", "Mineral Fluid (MIL-PRF-5606)", "Synthetic Phosphate-Ester (Skydrol / HyJet)"], fluids_table, col_widths=[90.0, 195.0, 215.0])

    pdf.add_callout(
        "trap",
        "Fluid Incompatibility & Seal Destruction",
        "- NEVER MIX hydraulic fluids! If Skydrol is inadvertently serviced into a mineral system, the Nitrile/Neoprene seals swell, soften, and dissolve within minutes, causing total system failure.\n"
        "- If mineral oil is added to a Skydrol system, the EPDM seals rapidly degrade and fail.\n"
        "- Contaminated systems must be completely drained, flushed with chemical solvent, and have all seals replaced!",
        max_chars=86
    )

    pdf.add_heading_1("3. Reservoirs & Pressurization Methods")
    pdf.add_paragraph(
        "The hydraulic reservoir stores fluid, accommodates thermal expansion, compensates for volume changes during jack extension/retraction, "
        "and permits air bubbles to separate out. In commercial aircraft, reservoirs MUST BE PRESSURIZED:"
    )
    pdf.add_bullet("Why Pressurize?", "At high flight altitudes (FL 350+), low atmospheric ambient pressure would cause the hydraulic fluid to boil and cause cavitation (vapor pocket collapse) in the hydraulic pump suction inlet, leading to immediate pump destruction!")
    pdf.add_bullet("Pressurization Sources", "1. Engine bleed air regulated to 30-50 psi; 2. Bootstrap reservoir (differential area piston utilizing system hydraulic pressure to pressurize the return fluid).")

    pdf.add_heading_1("4. Hydraulic Pumps: Constant vs Variable Displacement")
    pump_data = [
        ["Gear / Hand Pump", "Constant volume displacement. Output flow is directly proportional to RPM.", "Requires an Automatic Cut-Out Valve (ACOV) and system pressure relief valve to unseat and return fluid to reservoir when no actuators are moving."],
        ["Axial Piston Pump (EDP)", "Variable volume displacement. Rotating cylinder block with angled swashplate (cam plate).", "Swashplate angle modulates automatically via an internal pressure-compensating servo spool. At 3,000 psi demand satisfied, swashplate moves to 0° (zero delivery, zero power draw). Standard engine-driven pump (EDP)."]
    ]
    pdf.add_table(["Pump Type", "Operational Characteristics", "Control Mechanism & Aircraft Use"], pump_data, col_widths=[120.0, 190.0, 190.0])

    pdf.add_heading_1("5. Hydraulic Accumulators & Emergency Power Sources")
    pdf.add_paragraph(
        "A hydraulic accumulator is a rigid pressure vessel divided into two chambers by a floating piston, flexible diaphragm, or bladder:"
    )
    pdf.add_bullet("Gas Chamber", "Pre-charged with DRY NITROGEN (never compressed air or oxygen, which would cause an explosion in contact with hydraulic fluid mist!). Pre-charge is typically 1,000 to 1,500 psi.")
    pdf.add_bullet("Functions of Accumulator", "1. Dampens pressure spikes and hydraulic hammering from rapid valve closure; 2. Supplements pump delivery during high transient flow demand (e.g. gear retraction); 3. Provides emergency pressure reserve to operate brakes or deploy gear following complete engine pump failure.")
    pdf.add_bullet("Power Transfer Unit (PTU)", "A hydraulic motor driven by one system mechanically coupled to a pump in another system. Transfers HYDRAULIC POWER without any fluid transfer or intermixing!")
    pdf.add_bullet("Ram Air Turbine (RAT)", "A deployable slipstream-driven air turbine that drives an emergency hydraulic pump, supplying essential flight controls in the event of dual engine flameout or total AC electrical failure.")

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch02 = [
        ("Q1: Why must hydraulic reservoirs in jet transport aircraft operating at high altitudes be pressurized?",
         "[A] To prevent fluid freezing at -50°C\n[B] To prevent hydraulic pump cavitation caused by low atmospheric ambient pressure at high altitudes\n[C] To force fluid through the return filters\n[D] To operate the landing gear emergency extension",
         "CORRECT: [B]. At high altitudes, low ambient pressure can cause the fluid to vaporize at the pump inlet. Pressurizing the reservoir (with engine bleed air to 30-50 psi) provides a positive head of pressure, preventing destructive cavitation."),
        ("Q2: What gas must be used to pre-charge a hydraulic accumulator, and why?",
         "[A] Pure oxygen, to improve compressibility\n[B] Compressed ambient air\n[C] Dry nitrogen, because it is inert and will not support combustion or explode in contact with hydraulic oil\n[D] Carbon dioxide",
         "CORRECT: [C]. Accumulators are pre-charged exclusively with dry nitrogen. Using compressed air or oxygen could cause diesel-effect auto-ignition or catastrophic explosion when mixed with hydraulic fluid mist."),
        ("Q3: What occurs if a mineral-based hydraulic fluid is accidentally serviced into an aircraft system using Skydrol?",
         "[A] The fluid turns yellow but functions normally\n[B] The seals (EPDM) in the Skydrol system swell, dissolve, and fail, causing rapid fluid loss and system destruction\n[C] System operating pressure increases to 5,000 psi\n[D] The fluid boils at 0°C",
         "CORRECT: [B]. Mineral oil and phosphate-ester (Skydrol) fluids are completely chemically incompatible. Adding mineral oil to a Skydrol system rapidly attacks and destroys the Ethylene Propylene seals."),
        ("Q4: What is the primary operational function of a Power Transfer Unit (PTU)?",
         "[A] Transferring hydraulic fluid from a full system to a leaking system\n[B] Transferring power between two independent hydraulic systems without transferring or mixing fluid\n[C] Charging the nitrogen bottle\n[D] Disconnecting the EDP during engine start",
         "CORRECT: [B]. A PTU consists of a hydraulic motor in one system connected via a mechanical shaft to a pump in another system. It allows power transfer without any fluid mixing."),
        ("Q5: In a variable displacement axial-piston hydraulic pump, what happens to the swashplate angle as system pressure reaches 3,000 psi with no actuators moving?",
         "[A] Swashplate angle increases to maximum\n[B] Swashplate moves to approximately zero angle (perpendicular to piston axis), reducing pump output flow to zero\n[C] Swashplate reverses rotation direction\n[D] Swashplate disconnects from the driveshaft",
         "CORRECT: [B]. When system pressure satisfies the demand (3,000 psi), the pressure compensator moves the swashplate to near 0°, reducing piston stroke and output flow to zero, minimizing engine load.")
    ]

    for q_text, opts, exp in questions_ch02:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 2 compiled: {pdf_path}")


def build_agk_ch03():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch03_landing_gear_brakes.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 3: Landing Gear, Wheels, Tyres & Brakes")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        3,
        "Landing Gear, Wheels, Tyres & Brakes",
        "99-148"
    )

    pdf.add_heading_1("1. Oleo-Pneumatic Shock Strut Mechanics")
    pdf.add_paragraph(
        "Modern transport aircraft undercarriages use oleo-pneumatic shock absorber struts. The strut absorbs the kinetic energy of "
        "landing touchdown and dissipates it, while providing resilient cushioning during surface taxiing:"
    )
    pdf.add_bullet("Operating Mediums", "Strut contains two distinct fluids: 1. Hydraulic fluid (oil) in the lower cylinder; 2. Compressed dry nitrogen gas in the upper chamber.")
    pdf.add_bullet("Compression Stroke (Touchdown)", "During landing impact, the strut telescopes. The lower piston forces hydraulic oil upward through a small calibrated metering orifice into the upper cylinder, compressing the nitrogen. Oil forced through the restricted orifice transforms kinetic energy into heat (dissipated damping), while nitrogen compression cushions the impact.")
    pdf.add_bullet("Rebound Damping", "A recoil valve or tapered metering pin restricts the return flow of oil as the strut extends, preventing violent spring-back oscillations.")
    pdf.add_bullet("Maintenance Servicing Order", "CRITICAL EXAM POINT: Oleo struts must always be serviced with HYDRAULIC OIL FIRST until full to the level plug, and then inflated with DRY NITROGEN to achieve the specified chrome extension height!")

    pdf.add_heading_1("2. Retraction Systems, Locks & Emergency Extension")
    pdf.add_paragraph(
        "Landing gears are retracted hydraulically into aerodynamically sealed wheel wells in flight, locked mechanically, and provided with emergency extension backup:"
    )
    pdf.add_bullet("Uplocks & Downlocks", "Hydraulic actuators hold the gear in transit. Once fully retracted or extended, over-center mechanical locks (uplocks and downlocks) engage. The gear is held down by MECHANICAL LOCKS, not hydraulic pressure!")
    pdf.add_bullet("Ground Safety Pins", "Mechanical lock pins inserted into gear drag struts while parked on ground to physically prevent accidental gear retraction.")
    pdf.add_bullet("Emergency Extension Methods", "1. Gravity Free-Fall: Uplocks are mechanically or electrically released; gear doors open and the gear falls and locks down under gravity and aerodynamic airflow; 2. Emergency pneumatic nitrogen blow-down.")
    pdf.add_bullet("Nose Wheel Centering", "Nose gear shock struts feature an internal mechanical centering cam. As the nose strut extends after take-off, the internal cams align the nose wheels perfectly fore-and-aft before entering the wheel well, preventing catastrophic jamming.")

    pdf.add_heading_1("3. Aircraft Wheels, Tyres & Thermal Fusible Plugs")
    wheel_table = [
        ["Wheel Construction", "Two-piece split-hub design made of forged aluminum or magnesium alloy.", "Sealed by an elastomer O-ring. Assembled with tie-bolts. Always deflate tyre before loosening wheel tie-bolts!"],
        ["Thermal Fusible Plugs", "Hollow threaded brass bolts filled with a eutectic metal alloy plug.", "Melt at a predetermined high temperature (~150°C to 180°C) resulting from heavy or rejected take-off (RTO) braking. Releases tyre nitrogen pressure slowly into the brake assembly, PREVENTING CATASTROPHIC TYRE EXPLOSION and shrapnel damage!"],
        ["Tyre Inflation Gas", "Nitrogen is mandatory for all commercial transport aircraft tyres.", "Nitrogen is inert and contains no moisture; will not support combustion, maintains stable pressure across temperature extremes, and prevents oxidation of the inner tyre carcass rubber."],
        ["Tyre Wear & Creep", "Chine tyres used on nose wheels to deflect runway water away from rear-mounted jet engines.", "Tyre creep (slipping of tyre around the rim under heavy braking) is monitored by matching white creep marks painted across tyre and rim."]
    ]
    pdf.add_table(["Feature", "Engineering Design", "Operational & Safety Rule"], wheel_table, col_widths=[105.0, 195.0, 200.0])

    pdf.add_heading_1("4. Hydroplaning (Aquaplaning) Formulas & Phenomena")
    pdf.add_paragraph(
        "Hydroplaning occurs when aircraft tyres become separated from the paved runway surface by a continuous fluid film of water, "
        "reducing braking coefficient of friction and directional control to virtually zero:"
    )
    hydro_table = [
        ["Dynamic Hydroplaning", "Standing water on runway (> 3 mm depth). Water inertia builds up a hydrodynamic wedge that lifts tyre completely off pavement.", "Rotating Tyre: V_p = 9 x sqrt(P [psi])\nNon-Rotating (Skidding): V_p = 7.7 x sqrt(P [psi])"],
        ["Viscous Hydroplaning", "Very thin film of moisture (< 0.1 mm) on smooth pavement (paint markings, rubber deposits). Oil and dust create a soapy lubricating film.", "Can occur at MUCH LOWER SPEEDS than dynamic hydroplaning; persists down to low taxi speeds!"],
        ["Reverted Rubber", "Prolonged wheel lockup during skid. Friction heat boils trapped water into high-pressure steam, vulcanizing and burning tyre rubber into soft white seal.", "Steam cushion supports aircraft; tyre shows distinctive burnt/scalded oval rubber patch."]
    ]
    pdf.add_table(["Hydroplaning Type", "Physics & Water Depth", "Critical Speed Formula (Knots)"], hydro_table, col_widths=[110.0, 210.0, 180.0])

    pdf.add_callout(
        "trap",
        "Dynamic Hydroplaning Calculation Examples",
        "- Example 1 (Rotating Tyre): Tyre pressure = 144 psi. Dynamic hydroplaning speed = 9 x sqrt(144) = 9 x 12 = 108 KNOTS!\n"
        "- Example 2 (Non-Rotating Tyre / Spin-up on Touchdown): Tyre pressure = 100 psi. Speed = 7.7 x sqrt(100) = 7.7 x 10 = 77 KNOTS!\n"
        "- Note: A skidding (locked) wheel hydroplanes at a LOWER speed (7.7) than a rolling wheel (9.0)!",
        max_chars=86
    )

    pdf.add_heading_1("5. Anti-Skid Systems & Carbon Brake Packs")
    pdf.add_paragraph(
        "Modern multi-disc brakes use multiple rotating discs keyed to the wheel and stationary stator discs keyed to the axle torque tube. "
        "Carbon brake discs provide superior heat capacity, lighter weight, and wear less at high operating temperatures compared to steel brakes:"
    )
    pdf.add_bullet("Anti-Skid Operating Principle", "Wheel speed transducers monitor rotational deceleration. If wheel deceleration exceeds a predetermined threshold (indicating imminent skid), the anti-skid valve dumps hydraulic brake pressure instantly, allowing the wheel to spin back up, then smoothly reapplies modulated pressure.")
    pdf.add_bullet("Anti-Skid Functions", "1. Normal skid control; 2. Touchdown protection (prevents brake pressure application before touchdown, even if pilot presses pedals, until wheel spin-up reaches 30-50 kt or squat switch signals ground mode); 3. Locked wheel crossover protection; 4. Gear retraction braking (automatically applies low pressure to stop wheel rotation before entering wheel well).")

    pdf.add_heading_1("6. AviationExam Practice Questions (with Explanations)")
    questions_ch03 = [
        ("Q1: What is the primary purpose of thermal fusible plugs installed in aircraft wheels?",
         "[A] To melt and rapidly inflate the tyre during high-speed take-offs\n[B] To melt and release tyre pressure safely if brake and wheel temperatures exceed limits, preventing catastrophic tyre explosion\n[C] To lock the brakes when parked\n[D] To indicate brake pad wear limits",
         "CORRECT: [B]. Fusible plugs contain a low-melting-point alloy (150-180°C). During severe braking or an RTO, high brake heat conducts to the wheel rim; the plug melts, venting tyre nitrogen harmlessly before the tyre explodes."),
        ("Q2: An aircraft has a main tyre pressure of 144 psi. What is the calculated dynamic hydroplaning speed for a rotating tyre upon landing?",
         "[A] 77 kt\n[B] 95 kt\n[C] 108 kt\n[D] 144 kt",
         "CORRECT: [C]. Formula for rotating tyre: Vp = 9 x sqrt(P) = 9 x sqrt(144) = 9 x 12 = 108 knots."),
        ("Q3: In an oleo-pneumatic shock absorber strut, what primary medium absorbs and dissipates the initial impact energy of landing?",
         "[A] Nitrogen gas compression\n[B] Hydraulic oil forced through a restricted metering orifice\n[C] Steel coil springs\n[D] Rubber snubber blocks",
         "CORRECT: [B]. Nitrogen compression stores energy and provides spring cushioning, but the initial impact energy is absorbed and DISSIPATED as heat by hydraulic oil being forced through the calibrated metering orifice."),
        ("Q4: Why are commercial aircraft tyres inflated with dry nitrogen rather than compressed ambient air?",
         "[A] Nitrogen is lighter than air\n[B] Nitrogen is completely inert, dry (prevents rim corrosion and pressure fluctuations), and eliminates the risk of tyre explosion at high temperatures\n[C] Nitrogen increases braking friction\n[D] Nitrogen is cheaper than air",
         "CORRECT: [B]. Nitrogen contains no oxygen or moisture. It prevents rim corrosion, avoids high internal steam pressure rises from moisture at high brake temperatures, and eliminates internal combustion/explosion risks."),
        ("Q5: How does the anti-skid 'touchdown protection' feature function?",
         "[A] It deploys the ground spoilers automatically\n[B] It inhibits brake application until the main wheels have spun up to a minimum speed or ground squat switches confirm weight on wheels\n[C] It lowers the nose wheel gently to the runway\n[D] It disconnects nose wheel steering",
         "CORRECT: [B]. Touchdown protection prevents hydraulic pressure from reaching the brakes even if the pilot inadvertently presses the brake pedals before touchdown, ensuring the tyres do not blow out upon contacting the runway.")
    ]

    for q_text, opts, exp in questions_ch03:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 3 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_agk_ch01()
    build_agk_ch02()
    build_agk_ch03()
