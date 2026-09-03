#!/usr/bin/env python3
"""
Comprehensive Audit Script for Convocatoria 3 & Total Global Project (120 Topics).
"""

import os
import sys
import json
import sqlite3
import re

DB_PATH = "database/atpl.db"
DASHBOARD_JSON = "dashboard/data.json"

def audit_c3():
    print("=" * 70)
    print("🚀 AUDITORÍA INTEGRAL: CONVOCATORIA 3 Y ESTADO GLOBAL (120 TEMAS)")
    print("=" * 70)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # 1. Sittings
    c.execute("SELECT * FROM sittings ORDER BY number;")
    sittings = c.fetchall()
    print("\n[1] Estado de Convocatorias (Sittings) en SQLite:")
    for s in sittings:
        print(f"   - Convocatoria {s['number']}: {s['title']} -> Estado: {s['status']}")

    # 2. Convocatoria 3 Subjects
    c.execute("SELECT * FROM subjects WHERE sitting_id = 3 ORDER BY code;")
    subjects_c3 = c.fetchall()
    print("\n[2] Asignaturas de Convocatoria 3:")
    for sub in subjects_c3:
        c.execute("SELECT COUNT(*) as count FROM topics WHERE subject_code = ? AND status = 'completed';", (sub['code'],))
        done = c.fetchone()['count']
        c.execute("SELECT COUNT(*) as count FROM topics WHERE subject_code = ?;", (sub['code'],))
        total = c.fetchone()['count']
        print(f"   - {sub['code']} {sub['name']}: {done}/{total} temas completados (Status: {sub['status']})")

    # 3. Topic PDFs Verification for C3
    c.execute("""
        SELECT id, subject_code, chapter_num, title, summary_file, status 
        FROM topics 
        WHERE subject_code IN ('031', '032', '033')
        ORDER BY subject_code, chapter_num;
    """)
    topics_c3 = c.fetchall()
    print(f"\n[3] Verificando los {len(topics_c3)} temas de Convocatoria 3 y sus PDFs en disco:")

    missing_files = []
    corrupt_files = []
    total_pages_c3 = 0

    for t in topics_c3:
        fpath = t['summary_file']
        if not fpath or not os.path.exists(fpath):
            missing_files.append((t['subject_code'], t['chapter_num'], fpath))
            continue

        size = os.path.getsize(fpath)
        with open(fpath, "rb") as f:
            header = f.read(8)
            content = f.read()

        if b"%PDF" not in header or size < 1000:
            corrupt_files.append((t['subject_code'], t['chapter_num'], fpath, size))

        pages_count = len(re.findall(rb'/Type\s*/Page\b(?!\s*/Pages)', content))
        total_pages_c3 += pages_count

    print(f"   - Total temas C3: {len(topics_c3)}")
    print(f"   - Archivos faltantes: {len(missing_files)}")
    print(f"   - Archivos corruptos: {len(corrupt_files)}")
    print(f"   - Páginas individuales generadas en C3: {total_pages_c3} págs")

    if missing_files:
        print(f"   ❌ ERROR: Archivos faltantes: {missing_files}")
    if corrupt_files:
        print(f"   ❌ ERROR: Archivos corruptos: {corrupt_files}")

    # 4. Master Guides Verification
    master_guides_c3 = [
        ("031 Mass & Balance Master Guide", "resumenes/convocatoria_3/031_mass_and_balance/031_MASS_AND_BALANCE_MASTER_COMPLETE_STUDY_GUIDE.pdf"),
        ("032 Performance Master Guide", "resumenes/convocatoria_3/032_performance/032_PERFORMANCE_MASTER_COMPLETE_STUDY_GUIDE.pdf"),
        ("033 Flight Planning Master Guide", "resumenes/convocatoria_3/033_flight_planning_monitoring/033_FLIGHT_PLANNING_MASTER_COMPLETE_STUDY_GUIDE.pdf"),
    ]

    print("\n[4] Verificando Libros Maestros Consolidados de Convocatoria 3:")
    for name, mpath in master_guides_c3:
        if not os.path.exists(mpath):
            print(f"   ❌ FALTANTE: {name} en {mpath}")
            continue
        size = os.path.getsize(mpath)
        with open(mpath, "rb") as f:
            cnt = f.read()
        pgs = len(re.findall(rb'/Type\s*/Page\b(?!\s*/Pages)', cnt))
        print(f"   ✅ {name}: {pgs} páginas ({size:,} bytes) en {mpath}")

    # 5. Global Link Resolution from Dashboard Directory
    print("\n[5] Verificando Resolución Relativa de Enlaces desde dashboard/ (Todos los temas):")
    dashboard_dir = os.path.abspath("dashboard")
    with open(DASHBOARD_JSON, "r", encoding="utf-8") as f:
        ddata = json.load(f)

    broken_links = []
    for t in ddata.get("topics", []):
        sfile = t.get("summary_file")
        if sfile:
            target_abs = os.path.normpath(os.path.join(dashboard_dir, "..", sfile))
            if not os.path.exists(target_abs):
                broken_links.append((t['id'], sfile, target_abs))

    print(f"   - Total temas en base de datos & dashboard: {len(ddata.get('topics', []))}")
    print(f"   - Enlaces rotos: {len(broken_links)}")
    if broken_links:
        print(f"   ❌ ERROR: Enlaces rotos detectados: {broken_links[:5]}")
    else:
        print("   ✅ CERO ENLACES ROTOS: Todos los temas apuntan a archivos PDF válidos en disco.")

    gstats = ddata.get("global_stats", {})
    print(f"\n[6] Estadísticas Globales del Dashboard:")
    print(f"   - Convocatoria 1: {gstats.get('convocatoria_1_progress')}% ({gstats.get('completed_topics_c1')}/{gstats.get('total_topics_c1')})")
    print(f"   - Convocatoria 2: {gstats.get('convocatoria_2_progress')}% ({gstats.get('completed_topics_c2')}/{gstats.get('total_topics_c2')})")
    print(f"   - Convocatoria 3: {gstats.get('convocatoria_3_progress')}% ({gstats.get('completed_topics_c3')}/{gstats.get('total_topics_c3')})")
    print(f"   - Progreso Global: {gstats.get('overall_progress')}% ({gstats.get('total_completed_all')}/{gstats.get('total_topics_all')})")

    conn.close()
    print("\n" + "=" * 70)
    print("🏁 AUDITORÍA COMPLETADA CON ÉXITO")
    print("=" * 70)

if __name__ == "__main__":
    audit_c3()
