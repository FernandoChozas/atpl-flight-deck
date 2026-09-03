#!/usr/bin/env python3
"""
Insert Convocatoria 4 Topics into SQLite Database (atpl.db).
Subjects:
- 050 Meteorology (14 topics)
- 061 General Navigation (12 topics)
- 062 Radio Navigation & PBN (12 topics)
- 070 Operational Procedures (10 topics)
Total: 48 topics.
"""

import sqlite3
import os

DB_PATH = "database/atpl.db"

# 050 Meteorology (14 capítulos)
met_050_topics = [
    ("050", 1, "The Atmosphere: Structure, Composition, Vertical Extent & ISA", "1-32", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch01_atmosphere_structure_composition.pdf"),
    ("050", 2, "Atmospheric Pressure, Altimetry & Q-Codes (QNH, QFE, QNE)", "33-68", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch02_pressure_altimetry_qcodes.pdf"),
    ("050", 3, "Atmospheric Density, Temperature & Thermal Inversions", "69-98", "Media", "⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch03_density_temperature_inversions.pdf"),
    ("050", 4, "Moisture, Humidity, Adiabatic Processes & Atmospheric Stability", "99-136", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch04_moisture_humidity_adiabatic_processes.pdf"),
    ("050", 5, "Wind Dynamics, Global Circulation, Coriolis & Local Wind Systems", "137-174", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch05_wind_dynamics_global_circulation.pdf"),
    ("050", 6, "Global Jet Streams, Clear Air Turbulence (CAT) & Tropopause", "175-208", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch06_jet_streams_cat.pdf"),
    ("050", 7, "Cloud Classification (10 Genera), Fog Formation Mechanisms & Mist", "209-248", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch07_cloud_classification_fog_mist.pdf"),
    ("050", 8, "Precipitation Physics, Bergeron Process & Freezing Rain (FZRA)", "249-278", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch08_precipitation_freezing_rain.pdf"),
    ("050", 9, "Air Masses, Frontal Systems (Warm, Cold, Occluded) & Frontolysis", "279-322", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch09_air_masses_frontal_systems.pdf"),
    ("050", 10, "Pressure Systems: Mid-Latitude Depressions, Anticyclones & Cols", "323-358", "Media", "⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch10_pressure_systems_depressions_anticyclones.pdf"),
    ("050", 11, "Flight Hazards I: Airframe Icing, Turbulence & Mountain Waves", "359-398", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch11_icing_turbulence_mountain_waves.pdf"),
    ("050", 12, "Flight Hazards II: Thunderstorms (CB), Microbursts & Windshear", "399-438", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch12_thunderstorms_microbursts_windshear.pdf"),
    ("050", 13, "Tropical Meteorology, Tropical Revolving Storms & Climatology", "439-472", "Media", "⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch13_tropical_meteorology_climatology.pdf"),
    ("050", 14, "Meteorological Reports, Forecasts & Charts (METAR, TAF, SIGMET)", "473-510", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/050_meteorology/050_ch14_metar_taf_sigmet_charts.pdf")
]

# 061 General Navigation (12 capítulos)
gnav_061_topics = [
    ("061", 1, "The Earth: Geometry, Coordinates, Distance & Departure Formulas", "1-42", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch01_earth_geometry_coordinates_distance.pdf"),
    ("061", 2, "Great Circles, Rhumb Lines, Earth Convergence & Conversion Angle", "43-84", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch02_great_circles_rhumb_lines_convergence.pdf"),
    ("061", 3, "Earth Magnetism, Variation, Deviation & The Compass (ANDS / UNOS)", "85-128", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch03_magnetism_variation_deviation_compass.pdf"),
    ("061", 4, "Aeronautical Charts: Principles, Projections & Scale Properties", "129-166", "Media", "⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch04_aeronautical_charts_principles.pdf"),
    ("061", 5, "Mercator & Transverse Mercator Projections (Scale & Rhumb Lines)", "167-206", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch05_mercator_transverse_projections.pdf"),
    ("061", 6, "Lambert Conformal Conic Projection (Constant of Cone & Meridians)", "207-248", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch06_lambert_conformal_conic.pdf"),
    ("061", 7, "Polar Stereographic Projection (Transpolar Flight Planning)", "249-286", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch07_polar_stereographic_projection.pdf"),
    ("061", 8, "Grid Navigation (High-Latitude & Polar Heading Conversion)", "287-324", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch08_grid_navigation_polar.pdf"),
    ("061", 9, "Dead Reckoning (DR) Navigation & Flight Computer Principles", "325-364", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch09_dead_reckoning_flight_computer.pdf"),
    ("061", 10, "In-Flight Navigation & The 1-in-60 Rule (Track Error & Closing Angle)", "365-408", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch10_inflight_navigation_1in60_rule.pdf"),
    ("061", 11, "Time Systems: UTC, LMT, Zone Time, Equation of Time & Twilight", "409-452", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch11_time_systems_solar_twilight.pdf"),
    ("061", 12, "Inertial Reference Systems (IRS/INS): Schuler Tuning & Triple Mix", "453-498", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/061_general_navigation/061_ch12_inertial_navigation_mechanics.pdf")
]

# 062 Radio Navigation & PBN (12 capítulos)
rnav_062_topics = [
    ("062", 1, "Radio Wave Propagation, Antennas, Frequencies & Modulation", "1-44", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch01_radio_propagation_antennas.pdf"),
    ("062", 2, "Non-Directional Beacon (NDB) & Automatic Direction Finder (ADF)", "45-88", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch02_ndb_adf_principles_errors.pdf"),
    ("062", 3, "VHF Omnidirectional Range (VOR & Doppler DVOR) & Radials", "89-130", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch03_vor_dvor_principles_errors.pdf"),
    ("062", 4, "Distance Measuring Equipment (DME) & Slant Range Geometry", "131-168", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch04_dme_principles_slant_range.pdf"),
    ("062", 5, "Instrument Landing System (ILS: Localizer, Glide Path & Markers)", "169-216", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch05_ils_localizer_glide_path.pdf"),
    ("062", 6, "Microwave Landing System (MLS) & Satellite Landing (GLS/SBAS)", "217-252", "Media", "⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch06_mls_gls_sbas_landing.pdf"),
    ("062", 7, "Primary Pulse Radar Principles & Airborne Weather Radar (AWR)", "253-296", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch07_primary_radar_weather_radar.pdf"),
    ("062", 8, "Secondary Surveillance Radar (SSR), Transponders, Mode S & ADS-B", "297-340", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch08_ssr_transponders_mode_s_adsb.pdf"),
    ("062", 9, "Global Navigation Satellite Systems (GNSS: GPS, Galileo, GLONASS)", "341-384", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch09_gnss_gps_galileo_principles.pdf"),
    ("062", 10, "Satellite Integrity Monitoring: RAIM Algorithms & SBAS/GBAS", "385-424", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch10_raim_satellite_integrity_augmentation.pdf"),
    ("062", 11, "Performance-Based Navigation (PBN): Concept, RNAV vs RNP & Specs", "425-472", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch11_pbn_specifications_rnav_rnp.pdf"),
    ("062", 12, "Area Navigation Systems (RNAV Architecture, FMS Sensors & TSE)", "473-520", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_ch12_rnav_architecture_fms_sensors.pdf")
]

# 070 Operational Procedures (10 capítulos)
ops_070_topics = [
    ("070", 1, "International & European Regulatory Framework (EASA AIR-OPS)", "1-36", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/070_operational_procedures/070_ch01_easa_airops_framework.pdf"),
    ("070", 2, "Crew Composition & Flight Duty Time Limitations (FTL Limits)", "37-76", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/070_operational_procedures/070_ch02_crew_composition_ftl_limits.pdf"),
    ("070", 3, "Aerodrome Operating Minima (AOM) & Low Visibility Operations (LVO)", "77-116", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/070_operational_procedures/070_ch03_aom_lvo_all_weather_ops.pdf"),
    ("070", 4, "PANS-OPS Instrument Flight Procedures (Departures & Circling)", "117-156", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/070_operational_procedures/070_ch04_pans_ops_departures_circling.pdf"),
    ("070", 5, "Long-Range Approvals: ETOPS / EDTO Operations & Diversion Limits", "157-196", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/070_operational_procedures/070_ch05_etops_edto_regulations.pdf"),
    ("070", 6, "Special Approvals: RVSM, NAT HLA & PBCS Contingency Procedures", "197-234", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/070_operational_procedures/070_ch06_rvsm_nat_hla_contingency.pdf"),
    ("070", 7, "In-Flight Emergencies: Emergency Descent, Evacuation & Ditching", "235-272", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/070_operational_procedures/070_ch07_inflight_emergencies_descent_evac.pdf"),
    ("070", 8, "All-Weather Flight Hazards: Windshear, Ash Cloud & Wake Turbulence", "273-310", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/070_operational_procedures/070_ch08_windshear_volcanic_ash_wake_turbulence.pdf"),
    ("070", 9, "Ground De-Icing & Anti-Icing Operations (Holdover Times - HOT)", "311-346", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/070_operational_procedures/070_ch09_ground_deicing_antiicing_holdover.pdf"),
    ("070", 10, "Carriage of Dangerous Goods by Air (ICAO Annex 18 & IATA DGR)", "347-380", "Alta", "⭐⭐⭐", "resumenes/convocatoria_4/070_operational_procedures/070_ch10_dangerous_goods_icao_iata.pdf")
]

def insert_c4_topics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    c4_topics = met_050_topics + gnav_061_topics + rnav_062_topics + ops_070_topics
    print(f"Inserting {len(c4_topics)} Convocatoria 4 topics into {DB_PATH}...")

    inserted = 0
    for subj_code, ch_num, title, pages, diff, prio, summary_file in c4_topics:
        cursor.execute("""
            INSERT OR REPLACE INTO topics 
            (subject_code, chapter_num, title, pages, difficulty, priority, summary_file, status, understanding_level)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'not_started', 0)
        """, (subj_code, ch_num, title, pages, diff, prio, summary_file))
        inserted += 1

    # Update sitting 4 status to 'in_progress' and subjects
    cursor.execute("UPDATE sittings SET status = 'in_progress' WHERE number = 4;")
    cursor.execute("UPDATE subjects SET status = 'in_progress' WHERE code IN ('050', '061', '062', '070');")

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM topics;")
    total_topics = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM topics WHERE subject_code IN ('050', '061', '062', '070');")
    total_c4 = cursor.fetchone()[0]

    conn.close()
    print(f"Successfully inserted {inserted} C4 topics! Total in DB: {total_topics} (C4 topics: {total_c4})")

if __name__ == "__main__":
    insert_c4_topics()
