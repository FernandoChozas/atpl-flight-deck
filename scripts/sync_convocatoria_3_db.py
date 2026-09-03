#!/usr/bin/env python3
"""
Sync Convocatoria 3 topics in SQLite database (atpl.db) with exact generated PDF filepaths.
Sets status to 'completed' and validates all file links.
"""

import os
import sqlite3

DB_PATH = "database/atpl.db"

EXACT_FILES_C3 = {
    # 031 Mass & Balance (7 chapters)
    ("031", 1): "resumenes/convocatoria_3/031_mass_and_balance/031_ch01_definitions_mass_limits.pdf",
    ("031", 2): "resumenes/convocatoria_3/031_mass_and_balance/031_ch02_cg_datum_moments.pdf",
    ("031", 3): "resumenes/convocatoria_3/031_mass_and_balance/031_ch03_cg_mac_calculations.pdf",
    ("031", 4): "resumenes/convocatoria_3/031_mass_and_balance/031_ch04_mass_shifts_additions.pdf",
    ("031", 5): "resumenes/convocatoria_3/031_mass_and_balance/031_ch05_fuel_management_cg.pdf",
    ("031", 6): "resumenes/convocatoria_3/031_mass_and_balance/031_ch06_standard_passenger_baggage_masses.pdf",
    ("031", 7): "resumenes/convocatoria_3/031_mass_and_balance/031_ch07_load_trim_sheet.pdf",

    # 032 Performance (10 chapters)
    ("032", 1): "resumenes/convocatoria_3/032_performance/032_ch01_general_performance_atmosphere_wind.pdf",
    ("032", 2): "resumenes/convocatoria_3/032_performance/032_ch02_single_engine_piston_performance.pdf",
    ("032", 3): "resumenes/convocatoria_3/032_performance/032_ch03_multi_engine_class_b_takeoff_climb.pdf",
    ("032", 4): "resumenes/convocatoria_3/032_performance/032_ch04_class_b_enroute_landing.pdf",
    ("032", 5): "resumenes/convocatoria_3/032_performance/032_ch05_class_a_takeoff_speeds.pdf",
    ("032", 6): "resumenes/convocatoria_3/032_performance/032_ch06_class_a_takeoff_distances_balanced_field.pdf",
    ("032", 7): "resumenes/convocatoria_3/032_performance/032_ch07_class_a_takeoff_climb_segments.pdf",
    ("032", 8): "resumenes/convocatoria_3/032_performance/032_ch08_class_a_enroute_engine_out_driftdown.pdf",
    ("032", 9): "resumenes/convocatoria_3/032_performance/032_ch09_class_a_landing_performance.pdf",
    ("032", 10): "resumenes/convocatoria_3/032_performance/032_ch10_reduced_thrust_flexible_takeoff.pdf",

    # 033 Flight Planning & Monitoring (8 chapters)
    ("033", 1): "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch01_vfr_flight_planning_navigation.pdf",
    ("033", 2): "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch02_ifr_fuel_policy_easa.pdf",
    ("033", 3): "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch03_critical_points_pnr_etp.pdf",
    ("033", 4): "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch04_icao_ats_flight_plan_form.pdf",
    ("033", 5): "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch05_jeppesen_enroute_charts_airspace.pdf",
    ("033", 6): "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch06_standard_departures_arrivals_sids_stars.pdf",
    ("033", 7): "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch07_meteorological_charts_wintem_sigwx.pdf",
    ("033", 8): "resumenes/convocatoria_3/033_flight_planning_monitoring/033_ch08_inflight_monitoring_reộng_dpp.pdf",
}

def sync_c3_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    missing_count = 0
    updated_count = 0

    for (subj, ch), fpath in EXACT_FILES_C3.items():
        if not os.path.exists(fpath):
            print(f"ERROR: Generated file missing on disk: {fpath}")
            missing_count += 1
            continue

        cursor.execute("""
            UPDATE topics 
            SET summary_file = ?, status = 'completed', understanding_level = 5
            WHERE subject_code = ? AND chapter_num = ?;
        """, (fpath, subj, ch))
        updated_count += 1

    # Also update subjects and sitting 3 status
    cursor.execute("UPDATE subjects SET status = 'ready_for_exam' WHERE code IN ('031', '032', '033');")
    cursor.execute("UPDATE sittings SET status = 'completed' WHERE number = 3;")

    conn.commit()
    conn.close()

    print(f"Sync C3 complete. Updated topics: {updated_count}, Missing files: {missing_count}")

if __name__ == "__main__":
    sync_c3_database()
