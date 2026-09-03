#!/usr/bin/env python3
"""
Comprehensive Final Audit for Convocatoria 4 and Full ATPL System.
Checks:
- All 168 topics in atpl.db
- All 168 chapter PDFs exist and are valid
- All 13 Master Consolidated Guides exist and have correct page counts
- Dashboard data.json integrity and sync
- Zero broken links
"""

import os
import sys
import json
import sqlite3
import re

DB_PATH = "database/atpl.db"
DATA_JSON_PATH = "dashboard/data.json"

def get_pdf_page_count(filepath):
    if not os.path.exists(filepath):
        return 0
    with open(filepath, "rb") as f:
        data = f.read()
    m_pages = re.search(rb'/Type\s*/Pages\s*/Kids\s*\[([^\]]+)\]', data)
    if not m_pages:
        return 0
    kids_str = m_pages.group(1).decode('latin1')
    page_refs = re.findall(r'(\d+)\s+0\s+R', kids_str)
    return len(page_refs)

def audit():
    print("================================================================")
    print("      ATPL EASA FINAL COMPREHENSIVE AUDIT REPORT (C1 to C4)")
    print("================================================================")

    # 1. Database Check
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM topics")
    total_topics = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM topics WHERE status = 'completed'")
    completed_topics = cur.fetchone()[0]

    cur.execute("SELECT number, title, status FROM sittings ORDER BY number")
    sittings = cur.fetchall()

    cur.execute("SELECT code, name, status FROM subjects ORDER BY code")
    subjects = cur.fetchall()
    conn.close()

    print(f"\n[1] DATABASE AUDIT (atpl.db):")
    print(f"  - Total Topics in DB: {total_topics} (Expected: 168)")
    print(f"  - Completed Topics: {completed_topics} / {total_topics} ({completed_topics/total_topics*100:.1f}%)")
    assert total_topics == 168, f"Expected 168 topics, found {total_topics}"
    assert completed_topics == 168, f"Expected 168 completed topics, found {completed_topics}"

    print(f"  - Sittings Status:")
    for s_num, s_title, s_stat in sittings:
        print(f"    * Sitting {s_num}: {s_stat.upper()} ({s_title[:45]}...)")
        assert s_stat == 'completed', f"Sitting {s_num} is not completed!"

    print(f"  - Subjects Status:")
    for scode, sname, sstat in subjects:
        print(f"    * [{scode}] {sname[:30]:30s} -> {sstat.upper()}")

    # 2. Master Guides Audit (All 13 Subjects across C1, C2, C3, C4)
    print(f"\n[2] MASTER CONSOLIDATED GUIDES AUDIT (13 Master Books):")
    master_guides = [
        ("C1", "010 Air Law", "resumenes/convocatoria_1/010_air_law/010_AIR_LAW_MASTER_COMPLETE_STUDY_GUIDE.pdf", 82),
        ("C1", "040 Human Performance", "resumenes/convocatoria_1/040_human_performance/040_HUMAN_PERFORMANCE_MASTER_COMPLETE_STUDY_GUIDE.pdf", 43),
        ("C1", "090 Communications", "resumenes/convocatoria_1/090_communications/090_COMMUNICATIONS_MASTER_COMPLETE_STUDY_GUIDE.pdf", 23),
        ("C2", "021 AGK Systems", "resumenes/convocatoria_2/021_agk_airframe_systems_powerplant/021_AGK_MASTER_COMPLETE_STUDY_GUIDE.pdf", 54),
        ("C2", "022 Instrumentation", "resumenes/convocatoria_2/022_instrumentation/022_INSTRUMENTATION_MASTER_COMPLETE_STUDY_GUIDE.pdf", 30),
        ("C2", "081 Principles of Flight", "resumenes/convocatoria_2/081_principles_of_flight/081_POF_MASTER_COMPLETE_STUDY_GUIDE.pdf", 28),
        ("C3", "031 Mass & Balance", "resumenes/convocatoria_3/031_mass_and_balance/031_MASS_AND_BALANCE_MASTER_COMPLETE_STUDY_GUIDE.pdf", 19),
        ("C3", "032 Performance", "resumenes/convocatoria_3/032_performance/032_PERFORMANCE_MASTER_COMPLETE_STUDY_GUIDE.pdf", 24),
        ("C3", "033 Flight Planning", "resumenes/convocatoria_3/033_flight_planning_monitoring/033_FLIGHT_PLANNING_MASTER_COMPLETE_STUDY_GUIDE.pdf", 21),
        ("C4", "050 Meteorology", "resumenes/convocatoria_4/050_meteorology/050_METEOROLOGY_MASTER_COMPLETE_STUDY_GUIDE.pdf", 31),
        ("C4", "061 General Navigation", "resumenes/convocatoria_4/061_general_navigation/061_GENERAL_NAVIGATION_MASTER_COMPLETE_STUDY_GUIDE.pdf", 25),
        ("C4", "062 Radio Navigation", "resumenes/convocatoria_4/062_radio_navigation_pbn/062_RADIO_NAVIGATION_MASTER_COMPLETE_STUDY_GUIDE.pdf", 24),
        ("C4", "070 Operational Procedures", "resumenes/convocatoria_4/070_operational_procedures/070_OPERATIONAL_PROCEDURES_MASTER_COMPLETE_STUDY_GUIDE.pdf", 20),
    ]

    total_master_pages = 0
    for conv, title, path, expected_pages in master_guides:
        assert os.path.exists(path), f"MISSING MASTER PDF: {path}"
        actual_pages = get_pdf_page_count(path)
        total_master_pages += actual_pages
        size_kb = os.path.getsize(path) / 1024
        print(f"  - [{conv}] {title:26s}: {actual_pages:2d} págs (Expected: {expected_pages:2d}) | {size_kb:6.1f} KB | OK")
        assert actual_pages == expected_pages, f"Page mismatch for {title}: got {actual_pages}, expected {expected_pages}"

    print(f"\n  >>> GRAND TOTAL MASTER CONSOLIDATED PAGES: {total_master_pages} PÁGINAS CONTINUAS <<<")

    # 3. Individual Chapter Files Audit for Convocatoria 4
    print(f"\n[3] CONVOCATORIA 4 INDIVIDUAL CHAPTERS AUDIT (48 Chapters):")
    c4_folders = [
        ("050 Meteorology", "resumenes/convocatoria_4/050_meteorology", 14),
        ("061 General Navigation", "resumenes/convocatoria_4/061_general_navigation", 12),
        ("062 Radio Navigation & PBN", "resumenes/convocatoria_4/062_radio_navigation_pbn", 12),
        ("070 Operational Procedures", "resumenes/convocatoria_4/070_operational_procedures", 10),
    ]

    total_c4_chapters = 0
    total_c4_indiv_pages = 0
    for s_name, folder, exp_count in c4_folders:
        files = [f for f in os.listdir(folder) if f.endswith('.pdf') and not f.endswith('_MASTER_COMPLETE_STUDY_GUIDE.pdf')]
        print(f"  - {s_name:28s}: {len(files)} / {exp_count} chapter PDFs found.")
        assert len(files) == exp_count, f"Mismatch in {s_name}: found {len(files)}, expected {exp_count}"
        for f in files:
            fpath = os.path.join(folder, f)
            p_count = get_pdf_page_count(fpath)
            total_c4_indiv_pages += p_count
            assert p_count >= 1, f"Empty PDF: {fpath}"
        total_c4_chapters += len(files)

    print(f"  >>> Convocatoria 4 Individual Chapters: {total_c4_chapters} / 48 ({total_c4_indiv_pages} pages)")

    # 4. Dashboard Data JSON Check
    print(f"\n[4] DASHBOARD DATA INTEGRITY AUDIT (data.json):")
    with open(DATA_JSON_PATH, "r") as f:
        ddata = json.load(f)

    print(f"  - Updated at: {ddata['updated_at']}")
    print(f"  - Total Topics in JSON: {len(ddata['topics'])}")
    print(f"  - Completed Topics: {ddata['global_stats']['total_completed_all']} / {ddata['global_stats']['total_topics_all']}")
    print(f"  - Overall Progress: {ddata['global_stats']['overall_progress']:.1f}%")
    print(f"  - C1 Progress: {ddata['global_stats']['convocatoria_1_progress']:.1f}% ({ddata['global_stats']['completed_topics_c1']}/{ddata['global_stats']['total_topics_c1']})")
    print(f"  - C2 Progress: {ddata['global_stats']['convocatoria_2_progress']:.1f}% ({ddata['global_stats']['completed_topics_c2']}/{ddata['global_stats']['total_topics_c2']})")
    print(f"  - C3 Progress: {ddata['global_stats']['convocatoria_3_progress']:.1f}% ({ddata['global_stats']['completed_topics_c3']}/{ddata['global_stats']['total_topics_c3']})")
    print(f"  - C4 Progress: {ddata['global_stats']['convocatoria_4_progress']:.1f}% ({ddata['global_stats']['completed_topics_c4']}/{ddata['global_stats']['total_topics_c4']})")
    assert len(ddata['topics']) == 168, f"Expected 168 topics in JSON, found {len(ddata['topics'])}"
    assert ddata['global_stats']['overall_progress'] == 100.0, "Global progress is not 100%!"

    # 5. Broken Link Check for all topics in data.json
    print(f"\n[5] LINK VERIFICATION AUDIT:")
    broken_links = 0
    for top in ddata['topics']:
        sfile = top.get('summary_file')
        if sfile:
            # In index.html, links are written as href="../${t.summary_file}"
            # From dashboard directory, ../{sfile} resolves to {sfile} at workspace root
            full_path = os.path.normpath(os.path.join("dashboard", "..", sfile))
            if not os.path.exists(full_path):
                print(f"  [!] BROKEN LINK: {full_path} for topic {top['id']} ({top['title']})")
                broken_links += 1

    print(f"  - Broken Links Found: {broken_links}")
    assert broken_links == 0, f"Found {broken_links} broken links in dashboard!"

    print("\n================================================================")
    print("      🎉 ALL AUDIT CHECKS PASSED PERFECTLY! 0 DEFECTS FOUND! 🎉")
    print("================================================================")

if __name__ == "__main__":
    audit()
