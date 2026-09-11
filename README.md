# ✈️ ATPL Flight Deck — Suite Integral de Estudio EASA / AESA (NotebookLM v2)

[![EASA ECQB2024](https://img.shields.io/badge/Syllabus-EASA%20ECQB2024-blue.svg)](https://www.easa.europa.eu/)
[![Status](https://img.shields.io/badge/Status-100%25%20Completed%20%26%20Audited-success.svg)]()
[![Deliverables](https://img.shields.io/badge/Deliverables-724%20Files-orange.svg)]()
[![Bilingual](https://img.shields.io/badge/Language-English%20%7C%20Español%20(1:1)-green.svg)]()

Repositorio oficial y plataforma de preparación teórica para la licencia de **Piloto de Transporte de Línea Aérea (ATPL-A)** conforme al banco oficial de preguntas **ECQB (European Central Question Bank)** de EASA y la Agencia Estatal de Seguridad Aérea (AESA).

El ecosistema integra **13 asignaturas oficiales**, **168 capítulos**, **26 Libros Maestros en PDF** y **362 briefings de audio podcast bilingües** maquetados específicamente bajo el estándar **NotebookLM v2** de Google.

---

## 🗺️ Mapa de Arquitectura del Repositorio

El proyecto se encuentra organizado en una estructura limpia, modular y totalmente desacoplada:

```text
PROYECTO ATPL/
├── README.md                          # Guía central del repositorio y mapa de navegación
├── index.html                         # Punto de entrada web y redirección PWA
├── netlify.toml                       # Configuración de despliegue continuo en la nube
├── .gitignore                         # Control de exclusiones git
│
├── 📂 notebooklm_pilot/               # 🎓 SUITE DE ESTUDIO NOTEBOOKLM v2 (POR CONVOCATORIAS)
│   ├── 📂 convocatoria_1/             # Air Law (010), Human Perf (040), Comms (090)
│   ├── 📂 convocatoria_2/             # AGK Systems (021), Instrumentation (022), POF (081)
│   ├── 📂 convocatoria_3/             # Mass & Balance (031), Performance (032), Flight Planning (033)
│   ├── 📂 convocatoria_4/             # Meteorology (050), Gen Nav (061), Radio Nav (062), Ops Proc (070)
│   └── 📂 _archive_pilot_v1/          # Pruebas iniciales y muestras de voz archivadas
│
├── 📂 libros_oxford_fuente/           # 📚 BIBLIOTECA FUENTE: MANUALES ORIGINALES
│   ├── CAE Oxford Aviation Academy - 010 Air Law.pdf
│   ├── CAE Oxford Aviation Academy - 020 Airframes and Systems.pdf
│   ├── CAE Oxford Aviation Academy - 020 Electrics and Electronics.pdf
│   ├── CAE Oxford Aviation Academy - 020 Powerplant.pdf
│   ├── CAE Oxford Aviation Academy - 021 Instrumentation.pdf
│   ├── CAE Oxford Aviation Academy - 031 & 032 Mass and Balance & Performance.pdf
│   ├── CAE Oxford Aviation Academy - 033 Flight Planning and Monitoring.pdf
│   ├── CAE Oxford Aviation Academy - 040 Human Performance and Limitations.pdf
│   ├── CAE Oxford Aviation Academy - 061 General Navigation.pdf
│   ├── CAE Oxford Aviation Academy - 062 Radio Navigation.pdf
│   ├── CAE Oxford Aviation Academy - 062-07 PBN.pdf
│   ├── CAE Oxford Aviation Academy - 070 Operational Procedures.pdf
│   ├── Copia de CAE Oxford Aviation Academy - 090 Communications.pdf
│   ├── Principles of Flight complete.pdf
│   ├── GENERAL NAVIGATION - BGS.pdf
│   ├── 08 Climatología (1).pdf
│   ├── Libro de Meteo.pdf
│   └── Meteorology.pdf
│
├── 📂 resumenes/                      # 📝 RESÚMENES TEÓRICOS FUENTE EN MARKDOWN
│   ├── convocatoria_1/                # Air Law, HPL, Comms
│   ├── convocatoria_2/                # Principles of Flight, Instrumentation, AGK Systems
│   ├── convocatoria_3/                # Mass & Balance, Performance, Flight Planning
│   └── convocatoria_4/                # Meteorology, General Nav, Radio Nav, Operational Procedures
│
├── 📂 dashboard/                      # 📊 APLICACIÓN WEB ATPL FLIGHT DECK
│   ├── index.html                     # Tablero interactivo de seguimiento de estudio
│   ├── data.js / data.json            # Estructura de datos y progreso
│   └── apple-touch-icon-*.png         # Iconos de aplicación para iOS/Android
│
├── 📂 database/                       # 🗄️ BASE DE DATOS Y GESTOR DE PROGRESO
│   ├── atpl.db                        # Base de datos SQLite
│   ├── init_db.py                     # Inicializador del esquema
│   ├── schema.sql                     # Esquema relacional de asignaturas y temas
│   └── study_manager.py               # Lógica de gestión de estudio y repasos
│
├── 📂 scripts/                        # ⚙️ MOTORES DE COMPILACIÓN Y AUTOMATIZACIÓN
│   ├── pdf_builder.py                 # Motor gráfico de maquetación FPDF con paleta EASA
│   ├── notebooklm/                    # Orquestadores activos v2 (4 Convocatorias)
│   ├── raw_content_generators/        # Generadores modulares de contenido temático
│   └── archive_v1/                    # Scripts heredados de compilaciones iniciales
│
└── 📂 docs/                           # 📋 REGISTROS DE AUDITORÍA Y CERTIFICACIÓN
    └── AUDIT_LOG_AND_LESSONS_LEARNED.md
```

---

## 📊 Resumen de las 4 Convocatorias Oficiales

| Convocatoria | Asignaturas Incluidas | Capítulos | PDFs Capítulo | Libros Maestros | Podcasts Capítulo | Podcasts Maestros | Total Entregables |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **Conv. 1** | 010 Air Law, 040 HPL, 090 Communications | 45 | 90 (45 EN / 45 ES) | 6 (3 EN / 3 ES) | 90 (45 EN / 45 ES) | 6 (3 EN / 3 ES) | **192** |
| **Conv. 2** | 081 POF, 022 Instrumentation, 021 AGK | 50 | 100 (50 EN / 50 ES)| 6 (3 EN / 3 ES) | 100 (50 EN / 50 ES)| 6 (3 EN / 3 ES) | **214** |
| **Conv. 3** | 031 Mass & Balance, 032 Performance, 033 Flight Planning | 25 | 50 (25 EN / 25 ES) | 6 (3 EN / 3 ES) | 50 (25 EN / 25 ES) | 6 (3 EN / 3 ES) | **108** |
| **Conv. 4** | 050 Meteorology, 061 Gen Nav, 062 Radio Nav, 070 Ops | 48 | 96 (48 EN / 48 ES) | 8 (4 EN / 4 ES) | 96 (48 EN / 48 ES) | 8 (4 EN / 4 ES) | **208** |
| **TOTAL** | **13 Asignaturas Oficiales del Currículo ATPL** | **168** | **336 PDFs** | **26 Libros** | **336 MP3s** | **26 Podcasts** | **724 Archivos** |

---

## 🧠 Características Pedagógicas del Estándar NotebookLM v2

1. **Autosuficiencia Total de Estudio**:
   - Cada tema contiene la teoría completa exigida por los Learning Objectives (LOs) de EASA, evitando depender de fuentes externas durante la sesión de estudio.
2. **Guía para Dummies (Algoritmos Paso a Paso)**:
   - Recuadros específicos de color verde suave (`box_type="step"`) que desglosan de forma cuantitativa e infalible el método de resolución de problemas de examen (cálculo de masa y centrado, puntos críticos PNR/ETP, velocidades V, mínimos de aproximación, desvíos, etc.).
3. **Preguntas de Examen ECQB Justificadas**:
   - Opciones claramente delimitadas (`[A]`, `[B]`, `[C]`, `[D]`) sin apelotonamiento de texto, con recuadros de justificación técnica oficial (`box_type="summary"`).
4. **Briefings de Audio en Formato Conversación Dinámica**:
   - Diálogos bilingües con voces neurales diferenciadas:
     - **Español**: Álvaro (`es-ES-AlvaroNeural`) y Elvira (`es-ES-ElviraNeural`, rate `-2%`, pitch `+2Hz`).
     - **Inglés**: Ryan (`en-GB-RyanNeural`) y Sonia (`en-GB-SoniaNeural`).
   - Transcripciones limpias sin etiquetas markdown para una locución fluida y natural.

---

## 🛠️ Comandos de Uso Frecuente

### Compilación de PDFs de una Asignatura
```bash
python3 scripts/notebooklm/build_050_suite.py pdf
```

### Síntesis de Audio Neural con Edge-TTS
```bash
python3 scripts/notebooklm/build_050_suite.py audio
```

### Ejecución de Auditorías Multicapa
```bash
python3 scratch/audit_convocatoria_4_suite.py
```

---

## 📜 Licencia y Derechos
Material pedagógico compilado con fines formativos aeronáuticos para aspirantes a la licencia ATPL comercial. Contenidos alineados con la normativa EASA AIR-OPS y los manuales de referencia de CAE Oxford Aviation Academy y Bristol Groundschool.
