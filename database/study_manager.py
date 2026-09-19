#!/usr/bin/env python3
"""
Study Manager CLI - Gestor Inteligente de Estudio ATPL
Adaptado a la rutina de turnos de 12 horas (2 mañanas + 2 noches) y días libres.
Métricas orientadas al banco de preguntas AviationExam.
"""

import sys
import os
import sqlite3
import argparse
import json
import re  # movido aquí desde importación diferida en exportar_dashboard_interno
from datetime import datetime, timedelta
from contextlib import closing

DB_PATH = os.path.join(os.path.dirname(__file__), "atpl.db")
DASHBOARD_JSON = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dashboard", "data.json")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")  # [CRÍTICO FIX] FK estaban deshabilitadas en runtime
    conn.row_factory = sqlite3.Row
    return conn

def que_estudio_hoy(args):
    conn = get_db()
    c = conn.cursor()

    if args.turno:
        print("\n" + "="*70)
        print("🛑 DÍA DE TURNO DE TRABAJO (12H) - DESCANSO PROGRAMADO")
        print("="*70)
        print("Tu turno de 12h requiere el 100% de tu energía física y mental.")
        print("El plan de estudio está calibrado para que NO estudies en días de turno.")
        print("Cero culpa, cero penalizaciones y sin acumulación ficticia de retrasos.")
        print("👉 Duerme, recupérate y deja la concentración para tus días libres.\n")
        conn.close()
        return

    horas = args.horas if args.horas else 4.0
    print("\n" + "="*70)
    print(f"🎯 PLAN RECOMENDADO PARA HOY (DÍA LIBRE: {horas:.1f} HORAS)")
    print("="*70)

    bloques = []
    tiempo_acumulado = 0.0
    tema_consolidacion = None  # [FIX] Inicialización explícita: elimina el anti-patrón locals()

    # 1. Verificar si hay temas con repetición espaciada vencida
    today_str = datetime.now().strftime("%Y-%m-%d")
    c.execute("""
        SELECT t.id, t.subject_code, s.name as subject_name, t.chapter_num, t.title, t.summary_file, t.last_studied
        FROM topics t
        JOIN subjects s ON t.subject_code = s.code
        WHERE t.status IN ('completed', 'reviewed')
          AND t.next_review IS NOT NULL
          AND t.next_review <= ?
        ORDER BY t.priority DESC, t.next_review ASC
        LIMIT 1
    """, (today_str,))
    repaso = c.fetchone()

    # 2. Verificar temas en progreso o el siguiente por empezar
    c.execute("""
        SELECT t.id, t.subject_code, s.name as subject_name, t.chapter_num, t.title, t.pages, 
               t.difficulty, t.priority, t.status, t.summary_file
        FROM topics t
        JOIN subjects s ON t.subject_code = s.code
        JOIN sittings st ON s.sitting_id = st.id
        WHERE t.status IN ('not_started', 'studying')
        ORDER BY 
            st.number ASC,
            CASE t.status WHEN 'studying' THEN 1 ELSE 2 END,
            s.code ASC,
            t.chapter_num ASC
        LIMIT 1
    """)
    siguiente_tema = c.fetchone()

    # Si todos los temas están completados, seleccionar el tema de mayor prioridad para consolidación
    if not siguiente_tema and not repaso:
        c.execute("""
            SELECT t.id, t.subject_code, s.name as subject_name, t.chapter_num, t.title, t.pages, 
                   t.difficulty, t.priority, t.status, t.summary_file, t.last_studied
            FROM topics t
            JOIN subjects s ON t.subject_code = s.code
            WHERE t.status IN ('completed', 'reviewed')
            ORDER BY t.priority DESC, t.last_reviewed ASC, t.id ASC
            LIMIT 1
        """)
        tema_consolidacion = c.fetchone()
        if tema_consolidacion:
            bloques.append({
                "fase": "FASE DE MAESTRÍA — Consolidación y Simulacros Oficiales",
                "duracion": f"{min(horas, 2.0):.1f} h",
                "accion": f"Repaso de consolidación de alta prioridad: [{tema_consolidacion['subject_code']} {tema_consolidacion['subject_name']}] Cap. {tema_consolidacion['chapter_num']}: {tema_consolidacion['title']}",
                "recurso": tema_consolidacion['summary_file']
            })
            bloques.append({
                "fase": "PRÁCTICA EN BANCO — AviationExam Modo Examen (≥ 90%)",
                "duracion": f"{min(horas - 2.0, 1.5) if horas > 2.0 else 1.0:.1f} h",
                "accion": f"Hacer simulación de 40 preguntas en AviationExam del bloque [{tema_consolidacion['subject_code']}].",
                "recurso": f"Registrar test: python3 database/study_manager.py registrar-test --tema {tema_consolidacion['id']} --aciertos [X] --total [Y]"
            })
            tiempo_acumulado += horas

    # 3. Verificar si hay puntos débiles (< 80% en AviationExam)
    c.execute("""
        SELECT t.id, t.subject_code, t.chapter_num, t.title, 
               AVG(qs.score_percentage) as avg_score
        FROM topics t
        JOIN question_sessions qs ON t.id = qs.topic_id
        GROUP BY t.id
        HAVING avg_score < 80.0
        ORDER BY avg_score ASC
        LIMIT 1
    """)
    punto_debil = c.fetchone()

    bloques = [] if not tema_consolidacion else bloques
    tiempo_acumulado = 0.0 if not tema_consolidacion else tiempo_acumulado

    # Si hay repaso espaciado urgente
    if repaso:
        bloques.append({
            "fase": "FASE 3 — Consolidar (Repetición Espaciada)",
            "duracion": "45 min",
            "accion": f"Repaso rápido del resumen: [{repaso['subject_code']} {repaso['subject_name']}] Cap. {repaso['chapter_num']}: {repaso['title']}",
            "recurso": repaso['summary_file']
        })
        tiempo_acumulado += 0.75

    # Estudio troncal de tema nuevo o en progreso
    if siguiente_tema:
        tiempo_teoria = min(2.0, horas - tiempo_acumulado - 1.0)
        tiempo_banco = 1.0
        bloques.append({
            "fase": "FASE 1 — Comprender (Teoría Troncal)",
            "duracion": f"{tiempo_teoria:.1f} h",
            "accion": f"Estudio a fondo: [{siguiente_tema['subject_code']} {siguiente_tema['subject_name']}] Cap. {siguiente_tema['chapter_num']}: {siguiente_tema['title']} (Págs. {siguiente_tema['pages']})",
            "recurso": siguiente_tema['summary_file'] if siguiente_tema['summary_file'] else "Manual CAE Oxford"
        })
        bloques.append({
            "fase": "FASE 2 — Practicar (AviationExam)",
            "duracion": f"{tiempo_banco:.1f} h (35-50 preguntas)",
            "accion": f"Hacer el banco del tema en AviationExam (modo Study). Tras cada pregunta, analiza las explicaciones.",
            "recurso": f"Tema ID: {siguiente_tema['id']} -> python3 database/study_manager.py registrar-test --tema {siguiente_tema['id']} --aciertos [X] --total [Y]"
        })
        tiempo_acumulado += tiempo_teoria + tiempo_banco

    # Si sobra tiempo o hay punto débil detectado
    if punto_debil and (horas - tiempo_acumulado) >= 0.75:
        bloques.append({
            "fase": "ZONA DE RIESGO — Refuerzo de Fallos",
            "duracion": "45 min",
            "accion": f"Reforzar [{punto_debil['subject_code']}] Cap. {punto_debil['chapter_num']}: {punto_debil['title']} (Media actual: {punto_debil['avg_score']:.1f}%)",
            "recurso": "Revisar preguntas erradas en AviationExam"
        })

    for i, b in enumerate(bloques, 1):
        print(f"\n[{i}] {b['fase']} ({b['duracion']})")
        print(f"    👉 {b['accion']}")
        print(f"    📁 {b['recurso']}")

    print("\n" + "-"*70)
    print("💡 RECUERDA: El objetivo mínimo de seguridad para examen es ≥ 90% en AviationExam.")
    print("="*70 + "\n")
    conn.close()

def registrar_test(args):
    # [CRÍTICO FIX] Validación de entrada: evitar ZeroDivisionError y valores imposibles
    if args.total <= 0:
        print(f"❌ Error: --total debe ser un número positivo (recibido: {args.total})")
        return
    if args.aciertos < 0 or args.aciertos > args.total:
        print(f"❌ Error: --aciertos ({args.aciertos}) debe estar entre 0 y --total ({args.total})")
        return

    conn = get_db()
    try:
        c = conn.cursor()

        c.execute("SELECT subject_code, title, chapter_num FROM topics WHERE id = ?", (args.tema,))
        row = c.fetchone()
        if not row:
            print(f"❌ Error: No se encontró ningún tema con ID {args.tema}")
            return

        subject_code = row["subject_code"]
        pct = round((args.aciertos * 100.0) / args.total, 1)

        c.execute("""
            INSERT INTO question_sessions 
            (subject_code, topic_id, session_date, platform, mode, total_questions, correct_answers, duration_minutes, notes)
            VALUES (?, ?, date('now'), 'AviationExam', ?, ?, ?, ?, ?)
        """, (subject_code, args.tema, args.modo, args.total, args.aciertos, args.tiempo, args.notas))

        # Actualizar estado del tema y calcular repetición espaciada
        status = "completed" if pct >= 75.0 else "studying"
        stars = 5 if pct >= 90 else (4 if pct >= 85 else (3 if pct >= 75 else 2))
        
        # Próximo repaso: 3 días si aprobado, 1 día si suspenso
        interval_days = 3 if pct >= 75 else 1
        next_rev = (datetime.now() + timedelta(days=interval_days)).strftime("%Y-%m-%d")

        c.execute("""
            UPDATE topics
            SET status = ?,
                understanding_level = ?,
                last_studied = date('now'),
                next_review = ?
            WHERE id = ?
        """, (status, stars, next_rev, args.tema))

        conn.commit()
    finally:
        conn.close()  # [CRÍTICO FIX] Garantiza cierre del recurso en cualquier ruta de ejecución

    # Feedback semáforo
    color = "🟢" if pct >= 90 else ("🟡" if pct >= 85 else ("🟠" if pct >= 75 else "🔴"))
    print(f"\n{color} Sesión registrada con éxito en AviationExam!")
    print(f"   Tema: [{subject_code}] Cap. {row['chapter_num']}: {row['title']}")
    print(f"   Resultado: {args.aciertos}/{args.total} ({pct}%)")
    print(f"   Nivel asignado: {'⭐'*stars}")
    print(f"   Próximo repaso programado para: {next_rev}")
    if pct < 75:
        print("   ⚠️ Puntuación por debajo del 75%: se recomienda releer el resumen técnico antes del próximo test.\n")
    else:
        print("   ✅ ¡Buen trabajo! Sigue consolidando.\n")
    
    exportar_dashboard_interno()

def ver_estado(args):
    conn = get_db()
    c = conn.cursor()

    print("\n" + "="*75)
    print("📊 ESTADO GENERAL DE PREPARACIÓN ATPL EASA (14 ASIGNATURAS)")
    print("="*75)

    c.execute("SELECT id, number, title FROM sittings ORDER BY number ASC")
    sittings = c.fetchall()

    grand_total_topics = 0
    grand_comp_topics = 0

    for sit in sittings:
        print(f"\nCONVOCATORIA {sit['number']}: {sit['title'].upper()}")
        print("-" * 75)
        c.execute("""
            SELECT 
                s.code, s.name,
                COUNT(t.id) as total_topics,
                SUM(CASE WHEN t.status IN ('completed', 'reviewed') THEN 1 ELSE 0 END) as completed_topics,
                ROUND(AVG(CASE WHEN t.understanding_level > 0 THEN t.understanding_level ELSE NULL END), 1) as avg_stars
            FROM subjects s
            LEFT JOIN topics t ON s.code = t.subject_code
            WHERE s.sitting_id = ?
            GROUP BY s.code
            ORDER BY s.code ASC
        """, (sit["id"],))
        rows = c.fetchall()
        for r in rows:
            total = r["total_topics"] or 0
            comp = r["completed_topics"] or 0
            grand_total_topics += total
            grand_comp_topics += comp
            pct = round((comp * 100.0 / total), 1) if total > 0 else 0
            stars = f"{r['avg_stars']}⭐" if r["avg_stars"] else "Sin datos"
            bar = "█" * int(pct // 5) + "░" * (20 - int(pct // 5))
            print(f"[{r['code']}] {r['name']:<35} |{bar}| {pct:>5.1f}% ({comp}/{total}) | Nivel: {stars}")

    # Balance global
    grand_pct = round((grand_comp_topics * 100.0 / grand_total_topics), 1) if grand_total_topics > 0 else 0
    grand_bar = "█" * int(grand_pct // 5) + "░" * (20 - int(grand_pct // 5))
    print("\n" + "=" * 75)
    print(f"TOTAL GLOBAL EASA: |{grand_bar}| {grand_pct:>5.1f}% ({grand_comp_topics}/{grand_total_topics} Temas Completados)")
    print("13 Libros Maestros Consolidados Compilados (427 Páginas Continuas)")
    print("=" * 75)

    # Últimas 5 sesiones de AviationExam
    c.execute("""
        SELECT qs.session_date, qs.subject_code, t.title, qs.correct_answers, qs.total_questions, qs.score_percentage
        FROM question_sessions qs
        LEFT JOIN topics t ON qs.topic_id = t.id
        ORDER BY qs.id DESC
        LIMIT 5
    """)
    tests = c.fetchall()
    print("\nÚLTIMAS SESIONES DE AVIATIONEXAM:")
    print("-" * 75)
    if not tests:
        print("  (Aún no hay tests registrados. Usa 'registrar-test' tras tus sesiones)")
    else:
        for t in tests:
            sym = "🟢" if t["score_percentage"] >= 90 else ("🟡" if t["score_percentage"] >= 80 else "🔴")
            print(f"  {sym} {t['session_date']} | [{t['subject_code']}] {t['title'][:30]:<30} | {t['correct_answers']}/{t['total_questions']} ({t['score_percentage']}%)")

    print("="*75 + "\n")
    conn.close()

def exportar_dashboard_interno():
    conn = get_db()
    try:
        c = conn.cursor()

        # 1. Sittings
        c.execute("SELECT * FROM sittings ORDER BY number ASC")
        sittings = [dict(row) for row in c.fetchall()]

        # 2. Subjects
        c.execute("SELECT * FROM subjects ORDER BY sitting_id, code ASC")
        subjects = [dict(row) for row in c.fetchall()]

        # 3. Topics
        c.execute("SELECT * FROM topics ORDER BY subject_code, chapter_num ASC")
        topics = [dict(row) for row in c.fetchall()]

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        for t in topics:
            t["summary_pages"] = 0
            if t.get("summary_file"):
                pdf_path = os.path.join(base_dir, t["summary_file"])
                if os.path.exists(pdf_path):
                    try:
                        with open(pdf_path, "rb") as f:
                            content = f.read()
                            pages = len(re.findall(rb'/Type\s*/Page\b', content))
                            t["summary_pages"] = pages if pages > 0 else 1
                    except Exception:
                        pass

        # 4. Recent tests
        c.execute("""
            SELECT qs.*, t.title as topic_title
            FROM question_sessions qs
            LEFT JOIN topics t ON qs.topic_id = t.id
            ORDER BY qs.id DESC LIMIT 20
        """)
        tests = [dict(row) for row in c.fetchall()]
    finally:
        conn.close()  # [FIX] Cerrar conexión antes de operaciones de disco

    # Estadísticas globales
    total_topics_c1 = len([t for t in topics if t["subject_code"] in ["010", "040", "090"]])
    comp_topics_c1 = len([t for t in topics if t["subject_code"] in ["010", "040", "090"] and t["status"] in ["completed", "reviewed"]])
    pct_c1 = round((comp_topics_c1 * 100.0 / total_topics_c1), 1) if total_topics_c1 > 0 else 0

    total_topics_c2 = len([t for t in topics if t["subject_code"] in ["021", "022", "081"]])
    comp_topics_c2 = len([t for t in topics if t["subject_code"] in ["021", "022", "081"] and t["status"] in ["completed", "reviewed"]])
    pct_c2 = round((comp_topics_c2 * 100.0 / total_topics_c2), 1) if total_topics_c2 > 0 else 0

    total_topics_c3 = len([t for t in topics if t["subject_code"] in ["031", "032", "033"]])
    comp_topics_c3 = len([t for t in topics if t["subject_code"] in ["031", "032", "033"] and t["status"] in ["completed", "reviewed"]])
    pct_c3 = round((comp_topics_c3 * 100.0 / total_topics_c3), 1) if total_topics_c3 > 0 else 0

    total_topics_c4 = len([t for t in topics if t["subject_code"] in ["050", "061", "062", "070"]])
    comp_topics_c4 = len([t for t in topics if t["subject_code"] in ["050", "061", "062", "070"] and t["status"] in ["completed", "reviewed"]])
    pct_c4 = round((comp_topics_c4 * 100.0 / total_topics_c4), 1) if total_topics_c4 > 0 else 0

    total_all = len(topics)
    comp_all = len([t for t in topics if t["status"] in ["completed", "reviewed"]])
    pct_all = round((comp_all * 100.0 / total_all), 1) if total_all > 0 else 0

    data = {
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "global_stats": {
            "convocatoria_1_progress": pct_c1,
            "completed_topics_c1": comp_topics_c1,
            "total_topics_c1": total_topics_c1,
            "convocatoria_2_progress": pct_c2,
            "completed_topics_c2": comp_topics_c2,
            "total_topics_c2": total_topics_c2,
            "convocatoria_3_progress": pct_c3,
            "completed_topics_c3": comp_topics_c3,
            "total_topics_c3": total_topics_c3,
            "convocatoria_4_progress": pct_c4,
            "completed_topics_c4": comp_topics_c4,
            "total_topics_c4": total_topics_c4,
            "overall_progress": pct_all,
            "total_completed_all": comp_all,
            "total_topics_all": total_all,
            "tests_logged": len(tests)
        },
        "sittings": sittings,
        "subjects": subjects,
        "topics": topics,
        "recent_tests": tests
    }

    os.makedirs(os.path.dirname(DASHBOARD_JSON), exist_ok=True)
    with open(DASHBOARD_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Escribir también data.js para compatibilidad total offline con file:// (doble clic)
    js_path = os.path.join(os.path.dirname(DASHBOARD_JSON), "data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("window.ATPL_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

def exportar_dashboard_cmd(args):
    exportar_dashboard_interno()
    print(f"✅ Dashboard actualizado: {DASHBOARD_JSON}")

def main():
    parser = argparse.ArgumentParser(description="ATPL Study Manager")
    subparsers = parser.add_subparsers(dest="command", help="Comando a ejecutar")

    # Comando que-estudio-hoy
    p_hoy = subparsers.add_parser("que-estudio-hoy", help="Plan de estudio inteligente para hoy")
    p_hoy.add_argument("--horas", type=float, help="Horas disponibles hoy (ej: 4 o 5)")
    p_hoy.add_argument("--turno", action="store_true", help="Indica si hoy estás en turno de 12 horas")

    # Comando registrar-test
    p_test = subparsers.add_parser("registrar-test", help="Registrar resultado de sesión de AviationExam")
    p_test.add_argument("--tema", type=int, required=True, help="ID del tema evaluado")
    p_test.add_argument("--aciertos", type=int, required=True, help="Preguntas correctas")
    p_test.add_argument("--total", type=int, required=True, help="Total de preguntas del test")
    p_test.add_argument("--tiempo", type=int, default=30, help="Minutos dedicados")
    p_test.add_argument("--modo", choices=["Study", "Test", "Exam_Mock"], default="Study", help="Modo del banco")
    p_test.add_argument("--notas", type=str, default="", help="Observaciones o preguntas dudosas")

    # Comando estado
    subparsers.add_parser("estado", help="Ver estado y progreso del temario")

    # Comando exportar-dashboard
    subparsers.add_parser("exportar-dashboard", help="Exportar datos actualizados para el dashboard web")

    args = parser.parse_args()
    if args.command == "que-estudio-hoy":
        que_estudio_hoy(args)
    elif args.command == "registrar-test":
        registrar_test(args)
    elif args.command == "estado":
        ver_estado(args)
    elif args.command == "exportar-dashboard":
        exportar_dashboard_cmd(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
