#!/usr/bin/env python3
"""
Sync Convocatoria 2 topics in SQLite database (atpl.db) with exact generated PDF filepaths.
Sets status to 'completed' and validates all file links.
"""

import os
import sqlite3

DB_PATH = "database/atpl.db"

# Mapping of (subject_code, chapter_num) -> exact generated PDF path
EXACT_FILES = {
    # 021 AGK Airframe, Systems, Powerplant (22 chapters)
    ("021", 1): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch01_fuselage_wings_surfaces.pdf",
    ("021", 2): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch02_basic_hydraulics.pdf",
    ("021", 3): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch03_landing_gear_brakes.pdf",
    ("021", 4): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch04_flight_controls.pdf",
    ("021", 5): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch05_pneumatics_air_conditioning.pdf",
    ("021", 6): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch06_pressurisation_systems.pdf",
    ("021", 7): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch07_ice_rain_protection.pdf",
    ("021", 8): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch08_oxygen_equipment.pdf",
    ("021", 9): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch09_smoke_fire_protection.pdf",
    ("021", 10): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch10_fuel_systems.pdf",
    ("021", 11): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch11_dc_principles_circuits.pdf",
    ("021", 12): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch12_batteries_lead_acid_nicad.pdf",
    ("021", 13): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch13_magnetism_dc_generation.pdf",
    ("021", 14): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch14_ac_generation_csd_idg.pdf",
    ("021", 15): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch15_ac_distribution_inverters.pdf",
    ("021", 16): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch16_semiconductors_logic_buses.pdf",
    ("021", 17): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch17_piston_engines_cycles.pdf",
    ("021", 18): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch18_piston_fuels_carburation.pdf",
    ("021", 19): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch19_propellers_governors.pdf",
    ("021", 20): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch20_gas_turbines_compressors.pdf",
    ("021", 21): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch21_combustion_turbines_exhaust.pdf",
    ("021", 22): "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch22_fadec_engine_monitoring.pdf",

    # 022 Instrumentation (14 chapters)
    ("022", 1): "resumenes/convocatoria_2/022_instrumentation/022_ch01_pitot_static_temperature.pdf",
    ("022", 2): "resumenes/convocatoria_2/022_instrumentation/022_ch02_altimeter_vsi.pdf",
    ("022", 3): "resumenes/convocatoria_2/022_instrumentation/022_ch03_asi_machmeter.pdf",
    ("022", 4): "resumenes/convocatoria_2/022_instrumentation/022_ch04_air_data_computer_adiru.pdf",
    ("022", 5): "resumenes/convocatoria_2/022_instrumentation/022_ch05_magnetism_direct_reading_compass.pdf",
    ("022", 6): "resumenes/convocatoria_2/022_instrumentation/022_ch06_gyroscopic_principles_instruments.pdf",
    ("022", 7): "resumenes/convocatoria_2/022_instrumentation/022_ch07_inertial_navigation_irs.pdf",
    ("022", 8): "resumenes/convocatoria_2/022_instrumentation/022_ch08_radio_altimeter.pdf",
    ("022", 9): "resumenes/convocatoria_2/022_instrumentation/022_ch09_electronic_flight_displays_efis.pdf",
    ("022", 10): "resumenes/convocatoria_2/022_instrumentation/022_ch10_flight_management_system_fms.pdf",
    ("022", 11): "resumenes/convocatoria_2/022_instrumentation/022_ch11_aerodynamic_stall_warning.pdf",
    ("022", 12): "resumenes/convocatoria_2/022_instrumentation/022_ch12_gpws_egpws.pdf",
    ("022", 13): "resumenes/convocatoria_2/022_instrumentation/022_ch13_tcas_ii.pdf",
    ("022", 14): "resumenes/convocatoria_2/022_instrumentation/022_ch14_afcs_autopilot_flight_director.pdf",

    # 081 Principles of Flight (14 chapters)
    ("081", 1): "resumenes/convocatoria_2/081_principles_of_flight/081_ch01_subsonic_airflow_bernoulli.pdf",
    ("081", 2): "resumenes/convocatoria_2/081_principles_of_flight/081_ch02_airfoil_geometry_lift_moments.pdf",
    ("081", 3): "resumenes/convocatoria_2/081_principles_of_flight/081_ch03_lift_drag_polar_curves.pdf",
    ("081", 4): "resumenes/convocatoria_2/081_principles_of_flight/081_ch04_3d_airflow_induced_drag.pdf",
    ("081", 5): "resumenes/convocatoria_2/081_principles_of_flight/081_ch05_total_drag_vmd_ground_effect.pdf",
    ("081", 6): "resumenes/convocatoria_2/081_principles_of_flight/081_ch06_stalling_boundary_layer.pdf",
    ("081", 7): "resumenes/convocatoria_2/081_principles_of_flight/081_ch07_high_lift_devices_flaps_slats.pdf",
    ("081", 8): "resumenes/convocatoria_2/081_principles_of_flight/081_ch08_transonic_mach_mcrit.pdf",
    ("081", 9): "resumenes/convocatoria_2/081_principles_of_flight/081_ch09_swept_wings_area_rule.pdf",
    ("081", 10): "resumenes/convocatoria_2/081_principles_of_flight/081_ch10_stability_fundamentals.pdf",
    ("081", 11): "resumenes/convocatoria_2/081_principles_of_flight/081_ch11_longitudinal_stability_cg.pdf",
    ("081", 12): "resumenes/convocatoria_2/081_principles_of_flight/081_ch12_directional_lateral_stability.pdf",
    ("081", 13): "resumenes/convocatoria_2/081_principles_of_flight/081_ch13_flight_controls_tabs_balance.pdf",
    ("081", 14): "resumenes/convocatoria_2/081_principles_of_flight/081_ch14_flight_mechanics_vn_diagram.pdf",
}

def sync_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    missing_count = 0
    updated_count = 0

    for (subj, ch), fpath in EXACT_FILES.items():
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

    # Also update subjects status
    cursor.execute("UPDATE subjects SET status = 'ready_for_exam' WHERE code IN ('021', '022', '081');")
    cursor.execute("UPDATE sittings SET status = 'completed' WHERE number = 2;")

    conn.commit()
    conn.close()

    print(f"Sync complete. Updated topics: {updated_count}, Missing files: {missing_count}")

if __name__ == "__main__":
    sync_database()
