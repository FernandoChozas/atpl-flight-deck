#!/usr/bin/env python3
"""
Generator for Subject 021: AGK - Airframe, Systems, Electrics & Powerplant
Volume 4: Chapters 20 to 22 (Powerplant - Gas Turbines & Engine Control)
- Chapter 20: Gas Turbines: Inlets & Compressors (Axial/Centrifugal & Stalls)
- Chapter 21: Combustion Chambers, Turbines & Exhaust Systems
- Chapter 22: FADEC, Starting Systems & Engine Instruments (N1, EGT, EPR)

Fully aligned with CAE Oxford Book 4 (Powerplant) and EASA ECQB / AviationExam.
"""

import os
import sys
from pdf_builder import PDFBuilder

OUTPUT_DIR = "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant"

def build_agk_ch20():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch20_gas_turbines_compressors.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 20: Gas Turbines & Compressors")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        20,
        "Gas Turbines: Inlets & Compressors",
        "139-194 (Pwr)"
    )

    pdf.add_heading_1("1. The Brayton Cycle & Engine Inlets")
    pdf.add_paragraph(
        "Gas turbine engines operate on the open Brayton cycle (continuous combustion at constant pressure). "
        "Intake ducts must deliver undisturbed, subsonic air uniformly to the first compressor stage at approximately Mach 0.4 to 0.5:"
    )
    pdf.add_bullet("Subsonic Air Inlets", "CONVERGENT-DIVERGENT geometry on supersonic aircraft, but a simple DIVERGENT DUCT on subsonic airliners. As subsonic air flows through a divergent intake: Air velocity DECREASES while static pressure and temperature INCREASE (diffuser effect).")
    pdf.add_bullet("Ram Recovery", "At high forward airspeed, ram compression inside the intake restores total pressure above ambient atmospheric pressure, enhancing mass airflow and engine thrust.")

    pdf.add_heading_1("2. Compressor Types: Centrifugal vs Axial Flow")
    pdf.add_paragraph(
        "Compressors compress air prior to combustion to maximize thermal efficiency (Pressure Ratio = P_exit / P_inlet):"
    )

    comp_table = [
        ["Design Elements", "Impeller (rotor), Diffuser (stator), Manifold.", "Alternating rows of rotating Rotor Blades and stationary Stator Vanes."],
        ["Airflow Path", "Air enters eye, accelerated radially outwards 90°.", "Air flows parallel to engine centerline; cross-sectional annulus tapers."],
        ["Stage Pressure Ratio", "High per single stage (~4:1 to 5:1).", "Low per stage (~1.2:1), but cumulative multi-stage pressure ratio exceeds 30:1 to 45:1!"],
        ["Frontal Area & Drag", "Large frontal area; high aerodynamic drag.", "Small frontal area; low drag; ideal for high-speed transonic flight."],
        ["FOD Resistance", "High resistance to foreign object damage and ice.", "Susceptible to blade damage, tip rubbing, and aerodynamic stalls."]
    ]
    pdf.add_table(["Feature", "Centrifugal Flow Compressor", "Axial Flow Compressor"], comp_table, col_widths=[90.0, 205.0, 205.0])

    pdf.add_heading_1("3. Compressor Stall & Compressor Surge")
    pdf.add_paragraph(
        "Compressor blades are miniature aerodynamic airfoils operating at an angle of attack (Alpha = Vector sum of rotational velocity and axial airflow):"
    )
    pdf.add_bullet("Compressor Stall", "Localized aerodynamic stall of one or more rotor blades. Airflow separates from the suction side of the blade, forming rotating stall cells that propagate around the annulus in the direction opposite to rotation relative to the blades.")
    pdf.add_bullet("Compressor Surge", "Complete catastrophic breakdown of airflow across the entire compressor! High-pressure air from the combustion chamber rushes violently forward in reverse out the engine intake with loud bangs, violent airframe vibrations, rapid EGT spikes, and power loss!")
    pdf.add_bullet("Anti-Stall / Anti-Surge Devices", "1. Multi-Spool Design (separates N1 Low Pressure and N2 High Pressure shafts so each spool runs at optimal aerodynamic speed); 2. Variable Stator Vanes (VSVs) and Variable Inlet Guide Vanes (VIGVs) that modulate stator vane angles; 3. Compressor Bleed Valves that dump excess intermediate stage air overboard at low RPM.")

    pdf.add_callout(
        "trap",
        "Axial Compressor Blade Angle of Attack Dynamics",
        "- Blade Angle of Attack depends on: 1. Rotational Speed (RPM); 2. Axial Airflow Velocity (V_axial).\n"
        "- STALL RISK: If axial airflow DECREASES (e.g. crosswinds, inlet distortion) or if rotational RPM INCREASES rapidly, blade Angle of Attack INCREASES toward critical stall angle!\n"
        "- High stage compression causes compressor rear stages to be prone to choke at low RPM, while front stages are prone to stall!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch20 = [
        ("Q1: In an axial flow compressor of a gas turbine engine, what happens to the velocity and static pressure of the air as it passes through the stationary stator vanes?",
         "[A] Velocity increases and static pressure decreases\n[B] Velocity decreases (diffuser action) and static pressure increases\n[C] Both velocity and static pressure increase\n[D] Velocity remains constant while pressure drops",
         "CORRECT: [B]. The passages between stator vanes form divergent ducts. As air passes through, kinetic energy is converted into static pressure: air velocity decreases while static pressure increases."),
        ("Q2: What is the primary operational difference between a compressor stall and a compressor surge?",
         "[A] A stall occurs on the turbine, a surge occurs on the fan\n[B] A stall is a localized aerodynamic breakdown on individual compressor blades, while a surge is a complete reversal of airflow across the entire engine\n[C] A surge occurs only when descending\n[D] A stall increases engine thrust",
         "CORRECT: [B]. A stall affects isolated blades or rotating cells. Surge is the complete loss of pressure containment, where combustion chamber pressure forces air explosively backward out the intake."),
        ("Q3: What device prevents front-stage compressor stalling during engine acceleration or low RPM operation?",
         "[A] Fuel jettison valves\n[B] Variable Stator Vanes (VSVs) and compressor inter-stage bleed valves\n[C] Thrust reversers\n[D] Active clearance control",
         "CORRECT: [B]. At low RPM, rear stages restrict flow, backing up air and causing front stages to stall. Bleed valves open to vent air overboard, while VSVs tilt to maintain optimum blade angle of attack.")
    ]

    for q_text, opts, exp in questions_ch20:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 20 compiled: {pdf_path}")


def build_agk_ch21():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch21_combustion_turbines_exhaust.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 21: Combustion, Turbines & Exhaust")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        21,
        "Combustion, Turbines & Exhaust / Reversers",
        "195-256 (Pwr)"
    )

    pdf.add_heading_1("1. Combustion Chamber Architecture & Air Distribution")
    pdf.add_paragraph(
        "Combustion chambers burn fuel continuously to add thermal energy at constant pressure. Air entering from the compressor (at ~150 m/s) "
        "is slowed down by a diffuser to ~25 m/s to prevent blowing the flame out (flame speed is only ~2 to 5 m/s!):"
    )

    comb_air_table = [
        ["Primary Air", "20% to 25%", "Enters flame tube snout through swirl vanes to create a toroidal recirculation vortex. Mixes stoichiometrically (~15:1 air-fuel ratio) to support sustained ignition and stable core burning."],
        ["Secondary Air", "15% to 20%", "Enters through intermediate liner holes to complete combustion of unburned hydrocarbons."],
        ["Tertiary / Dilution Air", "55% to 60% (The Majority!)", "Enters downstream liner holes. Cools burning gases from ~2,000°C down to acceptable turbine entry temperatures (~1,200°C to 1,600°C) and forms an insulating film along chamber walls."]
    ]
    pdf.add_table(["Airflow Division", "Percentage of Total Bleed Air", "Operational Combustion Function"], comb_air_table, col_widths=[110.0, 160.0, 230.0])

    pdf.add_heading_1("2. Axial Flow Turbines & Blade Cooling")
    pdf.add_paragraph(
        "Turbines extract kinetic and heat energy from hot expanding combustion gases to drive the compressor and engine accessories:"
    )
    pdf.add_bullet("Nozzle Guide Vanes (NGVs)", "Stationary vanes positioned immediately upstream of the turbine rotor. Passages form CONVERGENT DUCTS that accelerate the gas to high velocity and deflect it at the optimum angle onto the turbine blades. Experiences highest thermal and aerodynamic stresses in the entire engine!")
    pdf.add_bullet("Impulse vs Reaction Blading", "Impulse: Gas pressure drops exclusively across NGVs, expanding as high-speed jets against curved blades. Reaction: Pressure drops across BOTH the NGVs and the rotating turbine blades (convergent blade passages). Modern engines use impulse blade roots transitioning to reaction blade tips.")
    pdf.add_bullet("Turbine Blade Cooling", "Blades are cast from single-crystal nickel superalloys. Cooled by compressor bleed air: 1. Internal convection passages; 2. Transpiration/film cooling where bleed air bleeds out through laser-drilled leading-edge holes, forming a protective microscopic thermal air cushion over the blade surface.")
    pdf.add_bullet("Active Clearance Control (ACC)", "Engine casing cooling system that blows fan bypass air onto the turbine casing, matching thermal casing shrinkage to turbine rotor growth, maintaining microscopic blade-tip clearances (minimizing gas leakage).")

    pdf.add_heading_1("3. Exhaust Systems & Thrust Reversers")
    pdf.add_paragraph(
        "Exhaust nozzles accelerate combustion gases overboard to create forward thrust (Gross Thrust F = m_dot x V_jet):"
    )
    pdf.add_bullet("Convergent Nozzle", "Used on all commercial subsonic airliners. Accelerates subsonic exhaust gas up to sonic velocity (Mach 1.0) at the nozzle throat (choked nozzle condition).")
    pdf.add_bullet("Thrust Reversers", "Redirect fan bypass air (or core exhaust) forward to provide aerodynamic deceleration on landing: 1. Clamshell / Bucket doors (deflects core exhaust); 2. Cascade Vane / Translating Sleeves (aerodynamic blocker doors block fan duct, directing bypass air forward through cascade vanes). In-flight deployment is physically blocked by multiple mechanical and electrical interlocks.")

    pdf.add_callout(
        "trap",
        "Thrust Reverser Interlocks & In-Flight Safety",
        "- Deployment on Ground: Requires weight-on-wheels (squat switch confirmation), throttle levers at idle, and reverse levers pulled.\n"
        "- In-Flight Protection: Features dual mechanical latches, hydraulic isolation valves, and auto-restow circuitry. If a reverser unlatches inadvertently in flight (e.g. Lauda Air 004 scenario), FADEC automatically reduces that engine's fuel flow to flight idle!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch21 = [
        ("Q1: What percentage of total compressor air entering a gas turbine combustion chamber is used as 'primary air' for combustion?",
         "[A] 10% to 15%\n[B] 20% to 25%\n[C] 50% to 60%\n[D] 85% to 90%",
         "CORRECT: [B]. Only about 20-25% of the total air is primary air used directly for burning fuel at stoichiometric ratio. The remaining 75-80% is used for combustion completion and cooling dilution."),
        ("Q2: What is the primary operational function of turbine Nozzle Guide Vanes (NGVs)?",
         "[A] To cool the exhaust gases\n[B] To accelerate the hot gases through convergent passages and direct them at the optimum angle onto the rotating turbine blades\n[C] To drive the engine oil pump\n[D] To reverse engine thrust",
         "CORRECT: [B]. NGVs are stationary nozzles ahead of the turbine rotor. Their convergent shape converts gas pressure into high-velocity kinetic energy, directing the jet at the ideal impingement angle onto the blades."),
        ("Q3: How are modern high-pressure turbine blades protected against melting at temperatures exceeding the alloy melting point?",
         "[A] By thermal paint only\n[B] By internal convection passages and external film cooling using relatively cool compressor bleed air\n[C] By injecting water into the fuel\n[D] By flying only in sub-zero ambient air",
         "CORRECT: [B]. Bleed air from the HP compressor is routed through internal labyrinth passages in the blade and exits through micro-holes to create a boundary film of cooler air shielding the metal from 1,500°C gases.")
    ]

    for q_text, opts, exp in questions_ch21:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 21 compiled: {pdf_path}")


def build_agk_ch22():
    pdf_path = os.path.join(OUTPUT_DIR, "021_ch22_fadec_engine_monitoring.pdf")
    pdf = PDFBuilder("Airframe & Systems", "021", "Chapter 22: FADEC & Engine Monitoring")

    # Cover / Header Banner
    pdf.add_title_banner(
        "Airframe & Systems",
        22,
        "FADEC, Starting Systems & Parameters (N1, EGT, EPR)",
        "257-310 (Pwr)"
    )

    pdf.add_heading_1("1. Full Authority Digital Engine Control (FADEC)")
    pdf.add_paragraph(
        "FADEC has complete, unrestricted digital electronic control over all engine fuel metering, geometry, and operational functions with NO MECHANICAL BACKUP:"
    )
    pdf.add_bullet("Dual-Channel Redundancy", "Consists of an Electronic Engine Controller (EEC) with two identical, independent digital channels (Channel A and Channel B). One channel is active while the other is in hot standby. Channels alternate control automatically on each engine start.")
    pdf.add_bullet("Dedicated Power (PMA)", "FADEC is completely self-powered above ~10-15% N2 by its own engine-driven Permanent Magnet Alternator (PMA). Even if aircraft dual AC/DC electrical systems fail completely, FADEC continues operating with zero interruption!")
    pdf.add_bullet("FADEC Control Functions", "1. Fuel metering (FMV); 2. Idle speed control (Flight idle, Ground idle, Reverse idle); 3. Transient bleed valves & VSVs; 4. Turbine active clearance control (ACC); 5. Thrust reverser deployment; 6. Engine limit protection (prevents N1/N2 over-speed and EGT over-temperature during auto-starts).")

    pdf.add_heading_1("2. Engine Starting Systems & Abnormal Start Drills")
    pdf.add_paragraph(
        "Modern jet engines use a pneumatic starter motor powered by APU, crossbleed, or ground air cart to spin the HP spool (N2):"
    )
    pdf.add_bullet("Standard Start Sequence", "1. Pneumatic starter valve opens -> Starter cranks HP spool (N2 rotation); 2. At maximum motoring speed (typically 15% to 25% N2), fuel flow and ignition are switched on; 3. Light-off occurs -> EGT rises rapidly; 4. At self-sustaining idle speed (~50% N2), starter valve closes and ignition turns off.")

    start_table = [
        ["Hot Start", "EGT rises rapidly and threatens or exceeds maximum start limit before reaching idle speed.", "ABORT START! Cut off fuel immediately; continue dry motoring engine with starter to blow cooling air through core."],
        ["Hung Start", "Engine lights off and EGT rises, but RPM stabilizes well below self-sustaining idle speed (N2 hangs).", "ABORT START! Cut off fuel; starter alone cannot overcome compressor drag."],
        ["Wet Start", "Fuel is injected and flows into engine, but NO IGNITION occurs within specified time (EGT does not rise).", "ABORT START! Cut off fuel; motor engine for at least 30-60 seconds to clear unburned fuel vapor before reattempt!"]
    ]
    pdf.add_table(["Abnormal Start Condition", "Cockpit Instrument Symptoms", "Immediate Flight Crew Emergency Action"], start_table, col_widths=[105.0, 195.0, 200.0])

    pdf.add_heading_1("3. Primary Engine Thrust Parameters: N1, EPR & EGT")
    pdf.add_paragraph(
        "Turbine thrust cannot be measured directly in flight. Cockpit instruments indicate computed thrust indicators:"
    )
    pdf.add_bullet("N1 (Low Pressure Spool / Fan Speed %)", "PRIMARY thrust setting parameter on high-bypass turbofan engines (CFM56, GE90, LEAP). Because 80% of total thrust is produced by the cold bypass fan, N1 RPM correlates directly with aerodynamic thrust.")
    pdf.add_bullet("Engine Pressure Ratio (EPR)", "PRIMARY thrust setting parameter on Rolls-Royce (Trent) and Pratt & Whitney engines. EPR = Total Pressure at Turbine Exhaust (P_t7) / Total Pressure at Engine Compressor Inlet (P_t2). An EPR of 1.50 means exhaust pressure is 1.5 times inlet ram pressure.")
    pdf.add_bullet("Exhaust Gas Temperature (EGT)", "Measured between turbine stages or at turbine exhaust by chromel-alumel thermocouples. Indicates the thermal stress and health of the turbine. The primary life-limiting factor of gas turbine engines.")

    pdf.add_callout(
        "trap",
        "N1 vs EPR Engine Pressure Probe Icing Trap",
        "- EPR engines rely on a heated P_t2 pitot probe in the engine intake nose cone.\n"
        "- If the P_t2 probe inlet blocks with ice in icing conditions: The probe senses artificially high pressure -> EPR indicates ERRONEOUSLY HIGH -> Pilot throttles back -> Engine delivers dangerously insufficient take-off thrust!\n"
        "- (This was the fatal primary cause of the Air Florida Flight 90 crash in Washington D.C.)!",
        max_chars=86
    )

    pdf.add_heading_1("4. AviationExam Practice Questions (with Explanations)")
    questions_ch22 = [
        ("Q1: What is a 'hung start' on a jet transport engine?",
         "[A] The starter motor fails to engage\n[B] The engine ignites normally, but rotational RPM fails to accelerate up to self-sustaining idle speed, stabilizing at an intermediate sub-idle value\n[C] EGT exceeds limits immediately\n[D] The propeller fails to unfeather",
         "CORRECT: [B]. In a hung start, fuel lights off and EGT rises, but the engine lacks sufficient torque to accelerate past starter cut-out speed up to self-sustaining idle, hanging at low RPM."),
        ("Q2: In a Full Authority Digital Engine Control (FADEC) system, what is the dedicated source of electrical power once the engine is running above sub-idle speeds?",
         "[A] The aircraft main 28V DC battery\n[B] An engine-driven Permanent Magnet Alternator (PMA) mounted on the engine accessory gearbox\n[C] The aircraft TRU\n[D] The APU generator",
         "CORRECT: [B]. FADEC incorporates its own dedicated PMA generator on the gearbox. Once above ~10-15% N2, FADEC is 100% self-powered, immune to any aircraft electrical failures."),
        ("Q3: On an aircraft that uses Engine Pressure Ratio (EPR) as its primary thrust indication, what is the mathematical definition of EPR?",
         "[A] Ratio of compressor exit pressure to burner pressure\n[B] Ratio of turbine exhaust total pressure (P_t7) to compressor inlet total pressure (P_t2)\n[C] Ratio of fan speed to core speed\n[D] Fuel flow divided by air flow",
         "CORRECT: [B]. EPR is defined as the total pressure at the turbine discharge / exhaust nozzle divided by the total pressure at the engine intake face (P_t7 / P_t2).")
    ]

    for q_text, opts, exp in questions_ch22:
        pdf.add_heading_2(q_text)
        pdf.add_paragraph(opts, max_chars=88)
        pdf.add_callout("definition", "Detailed Answer Explanation", exp, max_chars=86)

    pdf.compile_pdf(pdf_path)
    print(f"AGK Chapter 22 compiled: {pdf_path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_agk_ch20()
    build_agk_ch21()
    build_agk_ch22()
