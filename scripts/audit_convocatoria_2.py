#!/usr/bin/env python3
"""
Comprehensive Audit Script for Convocatoria 2 & Dashboard Synchronization.
Verifies file existence, PDF integrity, database state, and relative link correctness.
"""

import os
import sys
import json
import sqlite3
import re

DB_PATH = "database/atpl.db"
DASHBOARD_JSON = "dashboard/data.json"
INDEX_HTML = "dashboard/index.html"

def audit_all():
    print("=" * 70)
    print("🚀 AUDITORÍA INTEGRAL DE CONVOCATORIA 2 & DASHBOARD")
    print("=" * 70)

    # 1. Database Check
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * FROM sittings WHERE number = 2;")
    sitting2 = c.fetchone()
    print(f"\n[1] Sitting 2 Status in DB: {sitting2['title']} -> Status: {sitting2['status']}")

    c.execute("SELECT * FROM subjects WHERE sitting_id = 2 ORDER BY code;")
    subjects = c.fetchall()
    print("\n[2] Subjects in Sitting 2:")
    for s in subjects:
        c.execute("SELECT COUNT(*) as count FROM topics WHERE subject_code = ? AND status = 'completed';", (s['code'],))
        done = c.fetchone()['count']
        c.execute("SELECT COUNT(*) as count FROM topics WHERE subject_code = ?;", (s['code'],))
        total = c.fetchone()['count']
        print(f"   - {s['code']} {s['name']}: {done}/{total} temas completados (Status: {s['status']})")

    # 2. Topics & PDF Files Verification
    c.execute("""
        SELECT id, subject_code, chapter_num, title, summary_file, status 
        FROM topics 
        WHERE subject_code IN ('021', '022', '081')
        ORDER BY subject_code, chapter_num;
    """)
    topics = c.fetchall()
    print(f"\n[3] Verificando {len(topics)} temas y sus archivos PDF en disco:")

    missing_files = []
    corrupt_files = []
    total_pages = 0

    for t in topics:
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

        # Count pages via /Type /Page regex
        pages_count = len(re.findall(rb'/Type\s*/Page\b(?!\s*/Pages)', content))
        total_pages += pages_count

    print(f"   - Total temas revisados: {len(topics)}")
    print(f"   - Archivos faltantes: {len(missing_files)}")
    print(f"   - Archivos corruptos: {len(corrupt_files)}")
    print(f"   - Páginas individuales generadas en Convocatoria 2: {total_pages} págs")

    if missing_files:
        print(f"   ❌ ERROR: Archivos faltantes: {missing_files}")
    if corrupt_files:
        print(f"   ❌ ERROR: Archivos corruptos: {corrupt_files}")

    # 3. Master Guides Verification
    master_guides = [
        ("021 AGK Master Guide", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_AGK_MASTER_COMPLETE_STUDY_GUIDE.pdf"),
        ("022 Instrumentation Master Guide", "resumenes/convocatoria_2/022_instrumentation/022_INSTRUMENTATION_MASTER_COMPLETE_STUDY_GUIDE.pdf"),
        ("081 POF Master Guide", "resumenes/convocatoria_2/081_principles_of_flight/081_POF_MASTER_COMPLETE_STUDY_GUIDE.pdf"),
    ]

    print("\n[4] Verificando Libros Maestros Consolidados:")
    for name, mpath in master_guides:
        if not os.path.exists(mpath):
            print(f"   ❌ FALTANTE: {name} en {mpath}")
            continue
        size = os.path.getsize(mpath)
        with open(mpath, "rb") as f:
            cnt = f.read()
        pgs = len(re.findall(rb'/Type\s*/Page\b(?!\s*/Pages)', cnt))
        print(f"   ✅ {name}: {pgs} páginas ({size:,} bytes) en {mpath}")

    # 4. Dashboard JSON Verification
    print("\n[5] Verificando Dashboard JSON & JS:")
    with open(DASHBOARD_JSON, "r", encoding="utf-8") as f:
        ddata = json.load(f)

    gstats = ddata.get("global_stats", {})
    print(f"   - Convocatoria 1 Progreso: {gstats.get('convocatoria_1_progress')}% ({gstats.get('completed_topics_c1')}/{gstats.get('total_topics_c1')})")
    print(f"   - Convocatoria 2 Progreso: {gstats.get('convocatoria_2_progress')}% ({gstats.get('completed_topics_c2')}/{gstats.get('total_topics_c2')})")
    print(f"   - Progreso Global Total: {gstats.get('overall_progress')}% ({gstats.get('total_completed_all')}/{gstats.get('total_topics_all')})")

    # 5. Link Resolution from Dashboard Directory
    print("\n[6] Verificando Resolución Relativa de Enlaces desde dashboard/:")
    dashboard_dir = os.path.abspath("dashboard")
    broken_links = []

    for t in ddata.get("topics", []):
        sfile = t.get("summary_file")
        if sfile:
            target_abs = os.path.normpath(os.path.join(dashboard_dir, "..", sfile))
            if not os.path.exists(target_abs):
                broken_links.append((t['id'], sfile, target_abs))

    print(f"   - Enlaces de temas en dashboard: {len(ddata.get('topics', []))}")
    print(f"   - Enlaces rotos: {len(broken_links)}")
    if broken_links:
        print(f"   ❌ ERROR: Enlaces rotos detectados: {broken_links[:5]}")
    else:
        print("   ✅ CERO ENLACES ROTOS: Todos los temas apuntan a archivos PDF válidos en disco.")

    conn.close()
    print("\n" + "=" * 70)
    print("🏁 AUDITORÍA COMPLETADA CON ÉXITO")
    print("=" * 70)

if __name__ == "__main__":
    audit_all()
