#!/usr/bin/env python3
"""
Insert Convocatoria 3 topics into database/atpl.db safely.
Does not touch Convocatoria 1 or Convocatoria 2.
"""

import os
import sqlite3

DB_PATH = "database/atpl.db"

def insert_c3_topics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Ensure sitting 3 and subjects exist
    cursor.execute("""
        INSERT OR IGNORE INTO sittings (id, number, title, description, target_date, status)
        VALUES (3, 3, 'Convocatoria 3: Masa, Rendimiento y Planificación de Vuelo', 
                '031 Mass & Balance, 032 Performance, 033 Flight Planning & Monitoring. Alta concentración de cálculos y cartas aeronáuticas.', 
                '2027-05-31', 'in_progress');
    """)
    cursor.execute("UPDATE sittings SET status = 'in_progress' WHERE number = 3;")

    c3_subjects = [
        ("031", "Mass and Balance", 3, "in_progress", None, None),
        ("032", "Performance", 3, "in_progress", None, None),
        ("033", "Flight Planning and Monitoring", 3, "in_progress", None, None),
    ]
    cursor.executemany("""
        INSERT OR REPLACE INTO subjects (code, name, sitting_id, status, target_date, exam_score)
        VALUES (?, ?, ?, ?, ?, ?)
    """, c3_subjects)

    # 031 Mass and Balance (7 capítulos)
    mb_031_topics = [
        ("031", 1, "Mass Definitions & Structural Limits (BEM, DOM, ZFM, TOM, LM)", "1-22", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/031_mass_and_balance/031_ch01_definitions_mass_limits.pdf"),
        ("031", 2, "Center of Gravity Theory, Datums & Law of the Lever", "23-42", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/031_mass_and_balance/031_ch02_cg_datum_moments.pdf"),
        ("031", 3, "Calculation of CG & % MAC (Mean Aerodynamic Chord, LEMAC, TEMAC)", "43-66", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/031_mass_and_balance/031_ch03_cg_mac_calculations.pdf"),
        ("031", 4, "Mass Shifts, Load Changes & Ballast Calculations (Delta CG Formula)", "67-88", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/031_mass_and_balance/031_ch04_mass_shifts_additions.pdf"),
        ("031", 5, "Fuel Load Planning & Non-Linear CG Movement", "89-106", "Media", "⭐⭐", "resumenes/convocatoria_3/031_mass_and_balance/031_ch05_fuel_management_cg.pdf"),
        ("031", 6, "Standard Passenger & Baggage Masses, Cargo Compartment & Floor Limits", "107-124", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/031_mass_and_balance/031_ch06_standard_passenger_baggage_masses.pdf"),
        ("031", 7, "Load and Trim Sheet Execution & STAB TRIM Setting", "125-144", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/031_mass_and_balance/031_ch07_load_trim_sheet.pdf")
    ]

    # 032 Performance (10 capítulos)
    perf_032_topics = [
        ("032", 1, "General Performance, Atmosphere (ISA), Factored Winds & Slope", "1-44", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/032_performance/032_ch01_general_performance_atmosphere_wind.pdf"),
        ("032", 2, "Single-Engine Piston Aircraft Performance (Class B: Take-off & Climb)", "45-78", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/032_performance/032_ch02_single_engine_piston_performance.pdf"),
        ("032", 3, "Multi-Engine Class B Piston (Take-off, OEI Climb & Asymmetric Flight)", "79-114", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/032_performance/032_ch03_multi_engine_class_b_takeoff_climb.pdf"),
        ("032", 4, "Class B En-Route (Range vs Endurance) & Factorised Landing", "115-148", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/032_performance/032_ch04_class_b_enroute_landing.pdf"),
        ("032", 5, "Class A Take-Off Speeds (Vs, Vmcg, Vmca, V1, Vr, Vmu, V2)", "149-194", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/032_performance/032_ch05_class_a_takeoff_speeds.pdf"),
        ("032", 6, "Class A Take-Off Distances, Declared Distances & Balanced Field", "195-238", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/032_performance/032_ch06_class_a_takeoff_distances_balanced_field.pdf"),
        ("032", 7, "Class A Take-Off Flight Path & 4 Climb Segments (Gross vs Net)", "239-282", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/032_performance/032_ch07_class_a_takeoff_climb_segments.pdf"),
        ("032", 8, "Class A En-Route: Engine-Out Drift Down & Oxygen Altitudes", "283-316", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/032_performance/032_ch08_class_a_enroute_engine_out_driftdown.pdf"),
        ("032", 9, "Class A Landing Performance, Dry/Wet/Contaminated & Factorisation", "317-360", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/032_performance/032_ch09_class_a_landing_performance.pdf"),
        ("032", 10, "Reduced Thrust (Flex Temp / Assumed Temperature) & Derated Thrust", "361-402", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/032_performance/032_ch10_reduced_thrust_flexible_takeoff.pdf")
    ]

    # 033 Flight Planning & Monitoring (8 capítulos)
    fp_033_topics = [
        ("033", 1, "VFR Flight Planning, Vector Triangle & Navigational Calculations", "1-40", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch01_vfr_flight_planning_navigation.pdf"),
        ("033", 2, "EASA IFR Fuel Policy (AIR-OPS: Taxi, Trip, Contingency, Alternate, Final)", "41-82", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch02_ifr_fuel_policy_easa.pdf"),
        ("033", 3, "Critical Points: Point of No Return (PNR) & Equi-Time Point (ETP)", "83-120", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch03_critical_points_pnr_etp.pdf"),
        ("033", 4, "ICAO ATS Flight Plan (FPL) Form: Item-by-Item Decoding & Execution", "121-164", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch04_icao_ats_flight_plan_form.pdf"),
        ("033", 5, "Jeppesen En-Route Charts, Airway Dimensions & Minimum Altitudes", "165-208", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch05_jeppesen_enroute_charts_airspace.pdf"),
        ("033", 6, "Standard Departures (SID), Arrivals (STAR) & Holding Pattern Entries", "209-248", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch06_standard_departures_arrivals_sids_stars.pdf"),
        ("033", 7, "Meteorological Flight Planning Charts (WINTEM & SIGWX Tropopause/Jets)", "249-290", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch07_meteorological_charts_wintem_sigwx.pdf"),
        ("033", 8, "In-Flight Fuel Monitoring, Bogey Curves & Decision Point Procedure (DPP)", "291-340", "Alta", "⭐⭐⭐", "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch08_inflight_monitoring_reộng_dpp.pdf")
    ]

    c3_all = mb_031_topics + perf_032_topics + fp_033_topics
    cursor.executemany("""
        INSERT OR REPLACE INTO topics 
        (subject_code, chapter_num, title, pages, difficulty, priority, summary_file)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, c3_all)

    conn.commit()
    conn.close()
    print(f"Inserted {len(c3_all)} Convocatoria 3 topics into {DB_PATH}.")

if __name__ == "__main__":
    insert_c3_topics()
