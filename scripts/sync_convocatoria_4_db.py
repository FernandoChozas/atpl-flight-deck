#!/usr/bin/env python3
"""
Sync Convocatoria 4 progress to atpl.db.
Updates topics 121 to 168 to status 'completed' with understanding_level 5 and completion timestamps.
Updates subjects 050, 061, 062, 070 to status 'ready_for_exam'.
Updates sitting 4 to status 'completed'.
"""

import sqlite3
import datetime

DB_PATH = "database/atpl.db"

def sync_c4():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update topics 121 to 168
    cur.execute("""
        UPDATE topics
        SET status = 'completed', understanding_level = 5, last_studied = ?, last_reviewed = ?
        WHERE id BETWEEN 121 AND 168
    """, (now_str, now_str))
    updated_topics = cur.rowcount
    print(f"Updated {updated_topics} topics in Convocatoria 4 to 'completed'.")

    # Update subjects
    c4_subjects = ['050', '061', '062', '070']
    for s_code in c4_subjects:
        cur.execute("""
            UPDATE subjects
            SET status = 'ready_for_exam'
            WHERE code = ?
        """, (s_code,))
    print(f"Updated subjects {c4_subjects} to 'ready_for_exam'.")

    # Update sitting 4
    cur.execute("""
        UPDATE sittings
        SET status = 'completed'
        WHERE number = 4
    """)
    print("Updated sitting 4 to 'completed'.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    sync_c4()
