# Registro de Auditoría y Lecciones Aprendidas (ATPL Flight Deck)

Este documento registra los fallos detectados, las causas técnicas y las soluciones definitivas implementadas para garantizar la estabilidad y evitar recurrencias en futuras sesiones.

---

## 1. Dashboard y Experiencia de Usuario (UI/UX)

### A. Barra de desplazamiento horizontal en "Visión Global"
- **Fallo:** Al añadir la 5ª pestaña ("Visión Global"), apareció una barra de scroll horizontal antiestética en la cabecera.
- **Causa:** El contenedor `.tabs` tenía la propiedad `overflow-x: auto;` con ancho restringido.
- **Regla permanente:** Utilizar siempre `flex-wrap: wrap;` en las barras de pestañas y controles para adaptarse elásticamente a cualquier pantalla sin forzar barras de desplazamiento.

### B. Confusión de Progreso al 100% y Columnas Estáticas
- **Fallo:** La cabecera ponía "100% Temario Oficial Completado" y las columnas "Estado" (Completado) y "Nivel" (5 estrellas) estaban fijas en todos los temas, generando confusión sobre el avance real.
- **Causa:** Reflejaban el estado de redacción del temario, no el estudio activo del alumno.
- **Regla permanente:**
  - Separar conceptualmente la *disponibilidad del contenido* del *progreso de estudio*.
  - Eliminar columnas estáticas y sustituirlas por utilidades activas: `⏱️ T. Estimado` y `✅ Ticks` interactivos con persistencia en `LocalStorage`.

### C. Ámbito de las Puntuaciones de AviationExam
- **Fallo:** Se intentó ubicar un campo de nota por cada capítulo individual.
- **Causa:** En la preparación oficial EASA, los bancos de test se realizan a nivel de asignatura completa (ej. 010 Air Law), no por capítulos aislados.
- **Regla permanente:** Ubicar las notas oficiales en las tarjetas de los Libros Maestros Consolidados con semáforo dinámico (Verde ≥85%, Ámbar 75-84%, Rojo <75%).

---

## 2. Precisión de Tiempos de Estudio

### A. Error en el Cálculo de Páginas y Horas Absurdas (95h)
- **Fallo:** Para un capítulo de 2 páginas aparecían estimaciones de 95 horas de estudio.
- **Causa doble:**
  1. El campo `pages` de la base de datos contenía rangos de Oxford (ej. `"476-478"`), y `parseInt()` leía solo el número inicial (`476`), multiplicando 476 páginas por 12 minutos.
  2. Las páginas de los manuales de Oxford (12.000 páginas en total) no representan el material real de estudio, ya que el alumno estudia directamente de los resúmenes técnicos generados.
- **Regla permanente:**
  - El tiempo de estudio debe calcularse **estrictamente sobre las páginas de los PDFs de resumen generados**, nunca sobre los libros de origen.
  - El comando `exportar-dashboard` en `database/study_manager.py` analiza directamente los archivos PDF en disco con expresiones regulares (`/Type /Page`), guardando el campo `summary_pages` real para alimentar el cálculo del frontend.

---

## 3. Despliegue en la Nube y Alojamiento (Netlify)

### A. Error "Page Not Found" (404)
- **Fallo:** Al desplegar el proyecto en Netlify, la URL raíz mostraba un error 404.
- **Causa:** El archivo principal estaba ubicado en `dashboard/index.html` y no existía ningún punto de entrada en la raíz del repositorio.
- **Regla permanente:** Mantener siempre en la raíz un `index.html` de redirección inmediata y un archivo `netlify.toml` que declare `publish = "."` y la regla de redirección correspondiente.

### B. Bloqueo por Volumen de Archivos (300 MB)
- **Fallo:** La subida manual o por Git se ralentizaba debido a los PDFs originales de Oxford ubicados en la raíz.
- **Regla permanente:** Mantener en `.gitignore` la exclusión de `*.pdf` en la raíz (`!resumenes/**/*.pdf`), manteniendo el repositorio por debajo de 3 MB para despliegues instantáneos en menos de 10 segundos.

---

## 4. Progressive Web App (PWA) e Icono en iOS 18 (iPhone 16 Pro)

### A. Fallo del Icono Monograma ("A") en la Pantalla de Inicio
- **Fallo:** Al añadir la web a la pantalla de inicio del iPhone, aparecía un icono con la letra "A" en lugar del diseño aeronáutico.
- **Causa 1 (Canal Alfa):** Apple exige que los `apple-touch-icon` sean imágenes **RGB de 24 bits totalmente opacas (sin canal alfa)**. Las imágenes RGBA son descartadas por SpringBoard.
- **Causa 2 (Bug de `manifest.json` en iOS 17/18):** Cuando se enlaza un archivo `manifest.json`, el daemon de SpringBoard intenta procesar una PWA moderna; si falla la descarga asíncrona del icono en segundo plano, sustituye el icono previsualizado por la letra inicial del título.
- **Causa 3 (Caché agresiva de iOS):** El archivo interno `IconsCache.db` de iOS retiene el icono fallido para una misma URL aunque se elimine el marcador.
- **Regla permanente:**
  1. Generar iconos exclusivamente en formato **RGB opaco de 24 bits** (`hasAlpha: no`).
  2. Prescindir de `manifest.json` para iOS WebClips y confiar en las meta etiquetas nativas de Apple (`apple-mobile-web-app-capable: yes` y `apple-touch-icon`).
  3. **Incrustar el icono en Base64 directamente en el HTML** (`data:image/png;base64,...`) para que la imagen esté cargada sincrónicamente en memoria sin depender de peticiones de red del sistema.
  4. En caso de pruebas de cambio de icono en iOS, utilizar parámetros de URL frescos (ej. `?app=1`) para invalidar la caché del sistema.

---

## 5. Auditoría de Cierre de Sesión (04/09/2026)

- **Total Asignaturas EASA:** 14 disciplinas oficiales (13 códigos).
- **Total Capítulos:** 168 capítulos completados (100% verificados).
- **Total Libros Maestros Consolidados:** 13 volúmenes (427 páginas continuas).
- **Integridad de Base de Datos:** 168 registros en nivel 5 en `database/atpl.db`.
- **Integridad de Enlaces:** 0 enlaces rotos (181 archivos PDF verificados).
- **Control de Versiones (Git):** Árbol de trabajo 100% limpio y sincronizado con `origin/main` en GitHub.
- **Despliegue Continuo:** Operativo y probado en Netlify.
