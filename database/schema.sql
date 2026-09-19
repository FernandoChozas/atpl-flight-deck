-- Esquema de la Base de Datos ATPL
-- Diseñada para seguimiento del progreso, repetición espaciada y sesiones de AviationExam

PRAGMA foreign_keys = ON;

-- 1. Convocatorias (Sittings)
CREATE TABLE IF NOT EXISTS sittings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER UNIQUE NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    target_date TEXT,
    status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'in_progress', 'completed'))
);

-- 2. Asignaturas (Subjects)
CREATE TABLE IF NOT EXISTS subjects (
    code TEXT PRIMARY KEY,               -- ej: '010', '040', '090'
    name TEXT NOT NULL,                  -- ej: 'Air Law'
    sitting_id INTEGER NOT NULL,
    status TEXT DEFAULT 'not_started' CHECK(status IN ('not_started', 'in_progress', 'reviewing', 'ready_for_exam', 'passed')),
    target_date TEXT,
    exam_score REAL,                     -- Calificación final si ya se presentó
    FOREIGN KEY (sitting_id) REFERENCES sittings(id)
);

-- 3. Temas / Capítulos (Topics)
CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_code TEXT NOT NULL,
    chapter_num INTEGER NOT NULL,
    title TEXT NOT NULL,
    pages TEXT,                          -- ej: '21-52'
    difficulty TEXT DEFAULT 'Media' CHECK(difficulty IN ('Baja', 'Media', 'Alta')),
    priority TEXT DEFAULT '⭐⭐' CHECK(priority IN ('⭐', '⭐⭐', '⭐⭐⭐')),
    status TEXT DEFAULT 'not_started' CHECK(status IN ('not_started', 'studying', 'completed', 'reviewed')),
    understanding_level INTEGER DEFAULT 0 CHECK(understanding_level BETWEEN 0 AND 5), -- 0 a 5 estrellas
    last_studied TEXT,
    last_reviewed TEXT,
    next_review TEXT,                   -- Fecha calculada para repetición espaciada
    summary_file TEXT,                  -- Ruta relativa al PDF del resumen
    notes TEXT,
    UNIQUE(subject_code, chapter_num),
    FOREIGN KEY (subject_code) REFERENCES subjects(code)
);

-- 4. Sesiones de Test (AviationExam)
CREATE TABLE IF NOT EXISTS question_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_code TEXT NOT NULL,
    topic_id INTEGER,
    session_date TEXT NOT NULL DEFAULT (date('now')),
    platform TEXT DEFAULT 'AviationExam',
    mode TEXT DEFAULT 'Study' CHECK(mode IN ('Study', 'Test', 'Exam_Mock')),
    total_questions INTEGER NOT NULL,
    correct_answers INTEGER NOT NULL,
    score_percentage REAL GENERATED ALWAYS AS (ROUND((correct_answers * 100.0) / total_questions, 1)) STORED,
    duration_minutes INTEGER,
    notes TEXT,
    FOREIGN KEY (subject_code) REFERENCES subjects(code),
    FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- 5. Puntos Débiles y Trampas de Examen (Weak Spots & Traps)
CREATE TABLE IF NOT EXISTS weak_spots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_code TEXT NOT NULL,
    topic_id INTEGER,
    concept TEXT NOT NULL,
    trap_explanation TEXT NOT NULL,
    failure_count INTEGER DEFAULT 1,
    is_resolved INTEGER DEFAULT 0 CHECK(is_resolved IN (0, 1)),
    created_at TEXT DEFAULT (date('now')),
    FOREIGN KEY (subject_code) REFERENCES subjects(code),
    FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- 6. Registro Diario de Actividad (Study Logs)
CREATE TABLE IF NOT EXISTS study_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_date TEXT DEFAULT (date('now')),
    is_shift_day INTEGER DEFAULT 0,      -- 1 si fue día de turno (12h), 0 si fue día libre
    hours_dedicated REAL DEFAULT 0,
    topics_covered TEXT,
    questions_completed INTEGER DEFAULT 0,
    reflection TEXT
);

-- Índices para optimizar consultas frecuentes
CREATE INDEX IF NOT EXISTS idx_topics_status_review ON topics(status, next_review);
CREATE INDEX IF NOT EXISTS idx_topics_subject_chapter ON topics(subject_code, chapter_num);
