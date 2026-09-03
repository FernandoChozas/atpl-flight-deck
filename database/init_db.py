#!/usr/bin/env python3
"""
Inicializador de la Base de Datos SQLite ATPL.
Crea el esquema y puebla las 4 convocatorias, las 14 asignaturas y los capítulos de la Convocatoria 1.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "atpl.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Ejecutar esquema completo
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        cursor.executescript(f.read())

    # Limpiar tablas maestras para evitar duplicados al re-inicializar
    cursor.execute("DELETE FROM topics;")
    cursor.execute("DELETE FROM subjects;")
    cursor.execute("DELETE FROM sittings;")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('topics', 'subjects', 'sittings');")

    # 1. Insertar Convocatorias (Alineadas con la progresión óptima ATPL)
    sittings = [
        (1, 1, "Convocatoria 1: Normativa, Factores Humanos y Comunicaciones", 
         "010 Air Law, 040 Human Performance, 090 Communications. Ideal para ganar tracción y confianza con alta tasa de éxito.", 
         "2026-11-30", "in_progress"),
        (2, 2, "Convocatoria 2: Sistemas, Instrumentación y Aerodinámica", 
         "021 AGK Sistemas/Motores/Electricidad, 022 Instrumentación, 081 Principios de Vuelo. Bloque técnico y aerodinámico central.", 
         "2027-02-28", "pending"),
        (3, 3, "Convocatoria 3: Masa, Rendimiento y Planificación de Vuelo", 
         "031 Mass & Balance, 032 Performance, 033 Flight Planning & Monitoring. Alta concentración de cálculos y cartas aeronáuticas.", 
         "2027-05-31", "pending"),
        (4, 4, "Convocatoria 4: Meteorología, Navegación y Procedimientos Operacionales", 
         "050 Meteorología, 061 General Navigation, 062 Radio Navigation & PBN, 070 Operational Procedures. Bloque de navegación y operaciones en ruta.", 
         "2027-08-31", "pending"),
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO sittings (id, number, title, description, target_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, sittings)

    # 2. Insertar Asignaturas
    subjects = [
        # Convocatoria 1
        ("010", "Air Law", 1, "in_progress", None, None),
        ("040", "Human Performance and Limitations", 1, "not_started", None, None),
        ("090", "Communications (VFR + IFR)", 1, "not_started", None, None),
        
        # Convocatoria 2
        ("021", "AGK - Airframes, Systems, Electrics & Powerplant", 2, "not_started", None, None),
        ("022", "AGK - Instrumentation", 2, "not_started", None, None),
        ("081", "Principles of Flight", 2, "not_started", None, None),
        
        # Convocatoria 3
        ("031", "Mass and Balance", 3, "not_started", None, None),
        ("032", "Performance", 3, "not_started", None, None),
        ("033", "Flight Planning and Monitoring", 3, "not_started", None, None),
        
        # Convocatoria 4
        ("050", "Meteorology", 4, "not_started", None, None),
        ("061", "General Navigation", 4, "not_started", None, None),
        ("062", "Radio Navigation & PBN", 4, "not_started", None, None),
        ("070", "Operational Procedures", 4, "not_started", None, None),
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO subjects (code, name, sitting_id, status, target_date, exam_score)
        VALUES (?, ?, ?, ?, ?, ?)
    """, subjects)

    # 3. Insertar Temas de Convocatoria 1
    # 010 Air Law (25 capítulos según manual oficial CAE Oxford)
    air_law_topics = [
        ("010", 1, "International Agreements and Organizations (Chicago Convention & ICAO)", "21-52", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch01_international_agreements.pdf"),
        ("010", 2, "Airworthiness of Aircraft (Certificate of Airworthiness)", "53-58", "Media", "⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch02_airworthiness.pdf"),
        ("010", 3, "Aircraft Nationality and Registration Marks", "59-66", "Baja", "⭐", "resumenes/convocatoria_1/010_air_law/010_ch03_registration_marks.pdf"),
        ("010", 4, "Personnel Licensing (Part-FCL, Medicals, Ratings)", "67-100", "Media", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch04_flight_crew_licensing.pdf"),
        ("010", 5, "Rules of the Air (SERA, VFR & IFR Rules, Interception)", "101-156", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch05_rules_of_the_air.pdf"),
        ("010", 6, "Instrument Procedures - Departures (PANS-OPS, SID)", "157-172", "Media", "⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch06_departures.pdf"),
        ("010", 7, "Approach Procedures (Precision, Non-precision, Obstacle Clearance)", "173-206", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch07_approach_procedures.pdf"),
        ("010", 8, "Circling Approach (Visual Maneuvering, Minima, Sectors)", "207-214", "Media", "⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch08_circling_approach.pdf"),
        ("010", 9, "Holding Procedures (Entry Sectors, Speeds, Buffers)", "215-226", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch09_holding_procedures.pdf"),
        ("010", 10, "Altimeter Setting Procedures (QNH, QFE, Standard, Transition Level/Alt)", "227-238", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch10_altimeter_setting.pdf"),
        ("010", 11, "Parallel or Near-Parallel Runway Operations", "239-252", "Media", "⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch11_parallel_runways.pdf"),
        ("010", 12, "SSR and ACAS (Transponder Modes, TCAS II Resolution Advisories)", "253-262", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch12_ssr_acas.pdf"),
        ("010", 13, "Airspace Organization and Classification (Classes A to G)", "263-278", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch13_airspace.pdf"),
        ("010", 14, "Air Traffic Services (ATC, FIS, Alerting Service, INCERFA/ALERFA/DETRESFA)", "279-296", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch14_air_traffic_services.pdf"),
        ("010", 15, "Separation (Vertical, Horizontal, Radar & Wake Turbulence)", "297-330", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch15_separation.pdf"),
        ("010", 16, "Control of Aircraft (Radar, Vectors, Emergencies)", "331-356", "Media", "⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch16_control_aircraft.pdf"),
        ("010", 17, "Aeronautical Information Service (AIP, NOTAM, SNOWTAM, ASHTAM, AIC)", "357-374", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch17_ais.pdf"),
        ("010", 18, "Aerodromes - Physical Characteristics (Code Numbers, Runways, Taxiways)", "375-398", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch18_aerodromes_characteristics.pdf"),
        ("010", 19, "Aerodromes - Visual Aids, Markings and Signs (Runway & Taxiway Markings)", "399-424", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch19_visual_aids_markings.pdf"),
        ("010", 20, "Aerodrome Lighting (Approach Lighting Systems, Runway Lights, PAPI)", "425-446", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch20_aerodrome_lighting.pdf"),
        ("010", 21, "Obstacle Marking and Aerodrome Services (RFFS Rescue Categories)", "447-460", "Media", "⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch21_obstacle_marking_services.pdf"),
        ("010", 22, "Facilitation (Annex 9, Customs, Entry/Departure)", "461-470", "Baja", "⭐", "resumenes/convocatoria_1/010_air_law/010_ch22_facilitation.pdf"),
        ("010", 23, "Search and Rescue (Annex 12, Procedures, Signals)", "471-480", "Media", "⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch23_sar.pdf"),
        ("010", 24, "Security (Annex 17, Acts of Unlawful Interference)", "481-494", "Media", "⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch24_security.pdf"),
        ("010", 25, "Aircraft Accident and Incident Investigation (Annex 13, Definitions)", "495-504", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/010_air_law/010_ch25_accident_investigation.pdf")
    ]

    # 040 Human Performance and Limitations
    hpl_topics = [
        ("040", 1, "Human Factors - Basic Concepts, Safety Culture & Accident Statistics", "1-22", "Media", "⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch01_human_factors_concepts.pdf"),
        ("040", 2, "Aviation Physiology - Atmosphere, Respiration & Gas Laws", "23-56", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch02_aviation_physiology_gas_laws.pdf"),
        ("040", 3, "Hypoxia and Hyperventilation (Symptoms, TUC, Countermeasures)", "57-82", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch03_hypoxia_hyperventilation.pdf"),
        ("040", 4, "Decompression Sickness and Barotrauma (Trapped Gases, Diving Rules)", "83-108", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch04_dcs_barotrauma.pdf"),
        ("040", 5, "Vision (Eye Anatomy, Night Vision, Visual Illusions in Flight)", "109-158", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch05_vision_illusions.pdf"),
        ("040", 6, "Hearing and the Vestibular System (The Ear, Spatial Disorientation, Semicircular Canals)", "159-204", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch06_hearing_vestibular.pdf"),
        ("040", 7, "Toxic Hazards & Health (Hypothermia, Carbon Monoxide, Drugs, Alcohol)", "205-236", "Media", "⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch07_toxic_hazards_health.pdf"),
        ("040", 8, "Information Processing (Memory Models, Perception, Attention)", "237-278", "Media", "⭐⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch08_information_processing_memory.pdf"),
        ("040", 9, "Human Error & Reliability (SHELL Model, Reason's Swiss Cheese, Error Types)", "279-318", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch09_human_error_reliability.pdf"),
        ("040", 10, "Decision Making and Judgement in Aviation (Bias, Risk Assessment)", "319-354", "Media", "⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch10_decision_making_judgement.pdf"),
        ("040", 11, "Stress and Workload (Arousal, Yerkes-Dodson Law, Burnout)", "355-392", "Media", "⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch11_stress_workload.pdf"),
        ("040", 12, "Fatigue, Sleep and Circadian Rhythms (REM/NREM Sleep, Jet Lag Management)", "393-432", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch12_fatigue_sleep_circadian.pdf"),
        ("040", 13, "Communication, CRM and Cockpit Teamwork (Authority Gradient, Synergism)", "433-464", "Media", "⭐⭐", "resumenes/convocatoria_1/040_human_performance/040_ch13_communication_crm.pdf")
    ]

    # 090 Communications (VFR + IFR)
    comms_topics = [
        ("090", 1, "General Operating Procedures, Phraseology & Phonetics", "1-32", "Media", "⭐⭐⭐", "resumenes/convocatoria_1/090_communications/090_ch01_general_procedures_phraseology.pdf"),
        ("090", 2, "General Principles, Propagation & Frequency Bands (VHF, HF, 8.33 kHz Spacing)", "33-60", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/090_communications/090_ch02_propagation_frequency_bands.pdf"),
        ("090", 3, "Aerodrome Control Communications (VFR Departures, Taxi, Take-off & Landing)", "61-88", "Media", "⭐⭐", "resumenes/convocatoria_1/090_communications/090_ch03_aerodrome_control.pdf"),
        ("090", 4, "Approach and En-route Control Communications (IFR Clearances, Radar Vectors, SRA)", "89-118", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/090_communications/090_ch04_approach_enroute_control.pdf"),
        ("090", 5, "Weather Broadcasts & Information (ATIS, VOLMET, SIGMET, METAR/SPECI)", "119-142", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/090_communications/090_ch05_weather_broadcasts.pdf"),
        ("090", 6, "Distress and Urgency Procedures (MAYDAY vs PAN PAN, Frequencies, Squawks)", "143-168", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/090_communications/090_ch06_distress_urgency_procedures.pdf"),
        ("090", 7, "Communications Failure (Radio Failure VMC vs IMC, Transponder 7600)", "169-194", "Alta", "⭐⭐⭐", "resumenes/convocatoria_1/090_communications/090_ch07_communications_failure.pdf")
    ]

    # --- CONVOCATORIA 2 ---
    # 021 Aircraft General Knowledge: Airframe, Systems, Electrics & Powerplant (22 capítulos)
    agk_021_topics = [
        ("021", 1, "Fuselage, Wings and Stabilizing Surfaces", "1-46", "Media", "⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch01_fuselage_wings_surfaces.pdf"),
        ("021", 2, "Basic Hydraulics (Fluids, Pumps, Actuators & Accumulators)", "47-98", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch02_basic_hydraulics.pdf"),
        ("021", 3, "Landing Gear, Wheels, Tyres & Brakes", "99-148", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch03_landing_gear_brakes.pdf"),
        ("021", 4, "Flight Control Systems (Primary, Secondary & Powered)", "149-198", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch04_flight_controls.pdf"),
        ("021", 5, "Pneumatic Systems & Air Conditioning (Bleed Air & Packs)", "199-216", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch05_pneumatics_air_conditioning.pdf"),
        ("021", 6, "Pressurisation Systems (Outflow Valves & Pressure Regimes)", "217-234", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch06_pressurisation_systems.pdf"),
        ("021", 7, "Ice and Rain Protection (Thermal, Pneumatic & Electrical)", "235-258", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch07_ice_rain_protection.pdf"),
        ("021", 8, "Aircraft Oxygen Equipment (Crew Demand & Passenger Chemical)", "259-280", "Media", "⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch08_oxygen_equipment.pdf"),
        ("021", 9, "Smoke & Fire Detection and Protection Systems", "281-308", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch09_smoke_fire_protection.pdf"),
        ("021", 10, "Aircraft Fuel Systems (Tanks, Pumps, Crossfeed & Jettison)", "309-338", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch10_fuel_systems.pdf"),
        ("021", 11, "DC Electrical Principles, Components & Circuit Protection", "1-38", "Media", "⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch11_dc_principles_protection.pdf"),
        ("021", 12, "Batteries (Lead-Acid, Ni-Cad & Thermal Runaway)", "39-56", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch12_batteries_lead_nicad.pdf"),
        ("021", 13, "Magnetism, DC Generation & Starter-Generators", "57-102", "Media", "⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch13_dc_generation_starters.pdf"),
        ("021", 14, "AC Generation, Alternators & Constant Speed Drives (CSD/IDG)", "159-218", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch14_ac_generation_csd_idg.pdf"),
        ("021", 15, "AC Distribution, Transformers, TRUs & Inverters", "219-248", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch15_ac_distribution_inverters.pdf"),
        ("021", 16, "Semiconductors, Logic Gates & Aircraft Data Buses", "249-274", "Media", "⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch16_semiconductors_data_buses.pdf"),
        ("021", 17, "Piston Engines: Mechanical Structure, Principles & 4-Stroke Cycle", "1-48", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch17_piston_engine_principles.pdf"),
        ("021", 18, "Piston Engine Systems: Fuels, Carburation, Injection & Lubrication", "49-132", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch18_piston_systems_carburation.pdf"),
        ("021", 19, "Piston Engine Propellers & Constant Speed Governors", "133-196", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch19_propellers_governors.pdf"),
        ("021", 20, "Gas Turbine Engines: Fundamentals, Inlets & Compressors", "197-244", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch20_gas_turbines_compressors.pdf"),
        ("021", 21, "Gas Turbine Engines: Combustion Chambers, Turbines & Exhaust", "245-306", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch21_combustion_turbines_exhaust.pdf"),
        ("021", 22, "Gas Turbine Systems: Fuel Control, FADEC, Starting & Bleed Air", "307-400", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_ch22_fadec_systems_starting.pdf")
    ]

    # 022 Aircraft General Knowledge: Instrumentation (14 capítulos)
    inst_022_topics = [
        ("022", 1, "Pitot-Static Systems & Air Temperature Measurement (TAT/SAT)", "1-38", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch01_pitot_static_temperature.pdf"),
        ("022", 2, "Pressure Altimeters & Vertical Speed Indicators (VSI/IVSI)", "39-78", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch02_altimeters_vsi.pdf"),
        ("022", 3, "Airspeed Indicators (ASI) & Machmeters (IAS, CAS, EAS, TAS)", "79-114", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch03_asi_machmeters.pdf"),
        ("022", 4, "Air Data Computers (ADC / ADIRU Architecture)", "115-136", "Media", "⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch04_air_data_computers.pdf"),
        ("022", 5, "Terrestrial Magnetism & Direct/Remote Indicating Compasses", "137-168", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch05_magnetism_compasses.pdf"),
        ("022", 6, "Gyroscopic Principles & Primary Gyro Instruments (DG, AH, Turn)", "169-224", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch06_gyroscopic_instruments.pdf"),
        ("022", 7, "Inertial Navigation & Reference Systems (INS / IRS, RLG & FOG)", "225-260", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch07_inertial_reference_systems.pdf"),
        ("022", 8, "Radio Altimeters (FMCW Operation & Low Minima Decisions)", "261-268", "Media", "⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch08_radio_altimeters.pdf"),
        ("022", 9, "Electronic Flight Information Systems (EFIS - PFD & ND)", "269-304", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch09_efis_pfd_nd.pdf"),
        ("022", 10, "Flight Management Systems (FMS, CDU, Cost Index & Performance)", "305-332", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch10_flight_management_systems.pdf"),
        ("022", 11, "Flight Warning Systems, Aerodynamic Warnings & Stall Systems", "423-446", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch11_warning_stall_systems.pdf"),
        ("022", 12, "Ground Proximity Warning Systems (GPWS & EGPWS / TAWS)", "447-476", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch12_gpws_egpws.pdf"),
        ("022", 13, "Airborne Collision Avoidance Systems (ACAS II / TCAS II v7.1)", "477-494", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch13_tcas_acas.pdf"),
        ("022", 14, "Automatic Flight Control Systems (AFCS: FD, AP, AT, Yaw Damper)", "333-422", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/022_instrumentation/022_ch14_afcs_autopilot_autothrottle.pdf")
    ]

    # 081 Principles of Flight (14 capítulos)
    pof_081_topics = [
        ("081", 1, "Subsonic Airflow, Continuity Equation & Bernoulli's Principle", "1-26", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch01_subsonic_airflow_bernoulli.pdf"),
        ("081", 2, "Airfoil Geometry, Lift Generation & Pitching Moments", "27-52", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch02_airfoil_geometry_lift.pdf"),
        ("081", 3, "Lift & Drag Coefficients, The Lift Formula & Polar Curves", "53-78", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch03_coefficients_polar_curves.pdf"),
        ("081", 4, "Three-Dimensional Wing Airflow, Aspect Ratio & Induced Drag", "79-106", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch04_3d_airflow_induced_drag.pdf"),
        ("081", 5, "Total Drag, Minimum Drag Speed (Vmd) & Ground Effect", "107-134", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch05_total_drag_ground_effect.pdf"),
        ("081", 6, "Stalling Mechanics, Boundary Layer & Flow Separation", "135-162", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch06_stall_boundary_layer.pdf"),
        ("081", 7, "High-Lift Devices (Flaps & Slats) & Airframe Contamination", "163-194", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch07_high_lift_contamination.pdf"),
        ("081", 8, "Transonic Aerodynamics: Mach Number & Critical Mach (Mcrit)", "195-218", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch08_transonic_mcrit_shockwaves.pdf"),
        ("081", 9, "Transonic Design Features: Swept Wings & Area Rule", "219-238", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch09_swept_wings_area_rule.pdf"),
        ("081", 10, "Static & Dynamic Stability Fundamentals (Short Period & Phugoid)", "239-254", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch10_stability_fundamentals.pdf"),
        ("081", 11, "Longitudinal Stability & Center of Gravity Margins (Neutral Point)", "255-270", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch11_longitudinal_stability_cg.pdf"),
        ("081", 12, "Directional & Lateral Stability, Dutch Roll & Spiral Divergence", "271-284", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch12_directional_lateral_dutch_roll.pdf"),
        ("081", 13, "Flight Controls, Control Tabs & Aerodynamic Balance", "285-298", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch13_flight_controls_tabs.pdf"),
        ("081", 14, "Flight Mechanics, Maneuvers, V-n Diagram & Asymmetric Flight", "299-304", "Alta", "⭐⭐⭐", "resumenes/convocatoria_2/081_principles_of_flight/081_ch14_flight_mechanics_vn_diagram.pdf")
    ]

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

    all_topics = (
        air_law_topics + hpl_topics + comms_topics + 
        agk_021_topics + inst_022_topics + pof_081_topics + 
        mb_031_topics + perf_032_topics + fp_033_topics
    )
    cursor.executemany("""
        INSERT OR REPLACE INTO topics 
        (subject_code, chapter_num, title, pages, difficulty, priority, summary_file)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, all_topics)

    conn.commit()
    conn.close()
    print(f"Base de datos creada exitosamente en: {DB_PATH}")
    print(f"Total convocatorias: {len(sittings)}")
    print(f"Total asignaturas: {len(subjects)}")
    print(f"Total temas Convocatoria 1: {len(air_law_topics + hpl_topics + comms_topics)}")
    print(f"Total temas Convocatoria 2: {len(agk_021_topics + inst_022_topics + pof_081_topics)}")
    print(f"Total temas Convocatoria 3: {len(mb_031_topics + perf_032_topics + fp_033_topics)}")
    print(f"Total temas Global: {len(all_topics)}")

if __name__ == "__main__":
    init_database()

