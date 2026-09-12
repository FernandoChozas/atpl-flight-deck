# Changelog — ATPL Flight Deck

Todos los cambios notables, evoluciones y correcciones de este proyecto se registran de forma cronológica en este documento, siguiendo las directrices de [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y versionado semántico [SemVer](https://semver.org/lang/es/).

---

## [0.9.2] - 2026-09-12

### 🚀 Novedades y Mejoras Principales
- **Bloqueo Estricto de Materiales hasta Identificación de Usuario**:
  - Los materiales de estudio, audios, temarios y simuladores (`.container`) se inician completamente ocultos (`display: none;`) y bloqueados para cualquier invitado hasta que se identifique formalmente.
  - Eliminado por completo cualquier estado o visualización de "Piloto Invitado".
  - Al abrir un enlace de invitación, la única pantalla visible es el panel de identificación de cadete, impidiendo cualquier acceso o lectura previa de contenidos.
- **Selector Rápido de Perfiles y Nuevo Registro**:
  - Si en el dispositivo o en la red ya existen cadetes registrados (ej: `ALEX`, `CARLOS`), aparecen botones tipo píldora para identificarse y entrar con un solo toque.
  - Si es un nuevo alumno, introduce su nombre o Call Sign en el campo de texto y pulsa "Desbloquear Cabina de Estudio".
- **Garantía de Acceso Master Directo**:
  - El acceso de Comandante Master (`EC-CHOZAS`) vía `?master=1` o entorno local continúa funcionando de forma directa, sin popups y con todos los privilegios administrativos.

---

## [0.9.1] - 2026-09-12

### 🚀 Novedades y Mejoras Principales
- **Popup de Onboarding e Identificación de Cadete ("¿Quién eres?")**:
  - Al acceder a través de un enlace de invitación (`?invite=friend&pin=...`), se despliega de inmediato un modal de bienvenida que solicita al alumno su nombre o Call Sign (ej: `CARLOS`, `ALEX`, `MARTA`).
  - Muestra pastillas de selección rápida (`pills`) si ya existen perfiles de alumnos previos guardados en el dispositivo para facilitar el acceso en 1 solo clic.
  - El cadete se registra automáticamente en la telemetría de flota en tiempo real con su dispositivo y hora de última conexión.
- **Aislamiento Estricto de Enlaces de Invitado vs Enlace Master**:
  - Un enlace de invitación jamás hereda o auto-asigna la identidad del Comandante Master (`EC-CHOZAS`), incluso si se abre en el mismo navegador o móvil de Fernando.
  - Bloqueo de seguridad: si un invitado intenta reclamar el nombre `EC-CHOZAS` desde el popup de cadetes, el sistema lo rechaza y exige autenticación Master mediante PIN.
  - Acceso directo para el Comandante Master a través de `?master=1` o mediante el botón de identificación exclusivo al pie del popup.
- **Botón de Cambio Rápido de Cadete en Perfil**:
  - Añadido el botón `🔄 Cambiar de Cadete / Alumno` en el panel de perfil para alternar perfiles en dispositivos compartidos en cualquier momento.

---

## [0.9.0] - 2026-09-12

### 🚀 Novedades y Mejoras Principales
- **Simulador de Examen Oficial EASA/AESA**:
  - Incorporado en cada tarjeta de **Libro Maestro** un botón reglamentario `🎓 Examen Oficial AESA`.
  - Configurado con las cuotas y tiempos oficiales de examen EASA (Reglamento UE 1178/2011 / ECQB):
    - `010 Air Law`: 44 preguntas · 60 minutos
    - `021 AGK Sistemas`: 80 preguntas · 120 minutos
    - `022 AGK Instrumentación`: 60 preguntas · 90 minutos
    - `031 Masa y Centrado`: 25 preguntas · 75 minutos
    - `032 Rendimiento (Performance)`: 35 preguntas · 60 minutos
    - `033 Planificación de Vuelo`: 42 preguntas · 120 minutos
    - `040 Factores Humanos`: 35 preguntas · 45 minutos
    - `050 Meteorología`: 84 preguntas · 120 minutos
    - `061 Navegación General`: 55 preguntas · 135 minutos
    - `062 Radio Navegación`: 66 preguntas · 90 minutos
    - `070 Procedimientos Operacionales`: 42 preguntas · 75 minutos
    - `081 Principios de Vuelo`: 44 preguntas · 60 minutos
    - `090 Comunicaciones`: 36 preguntas · 60 minutos
  - Temporizador oficial en cuenta regresiva con aviso visual.
  - Corte oficial de aprobado fijado al **75%** y volcado automático de la nota en la tarjeta del Libro Maestro.

- **AeroQuiz por Capítulos Aislados**:
  - Refactorizado el motor de tests rápidos para que cada capítulo tenga sus propias preguntas exclusivas sin mezclarse con otros temas de la misma asignatura.
  - Barajado aleatorio Fisher-Yates de opciones [A, B, C, D] y preguntas en cada reintento.

- **Telemetría de Cadetes de Flota 2.0**:
  - **Sincronización Read-Merge-Write**: Solucionado el bug que provocaba la desaparición de alumnos en refresco. El sistema ahora lee el directorio remoto, fusiona los datos y evita sobreescrituras destructivas entre alumnos y Master.
  - **Actualización Inmediata de Nombre**: Cuando un cadete personaliza su Call Sign o nombre, se limpia su identificador previo en la nube y se propaga instantáneamente a la consola del Master.
  - **Borrado Administrativo de Cadetes**: El Comandante Master (`EC-CHOZAS`) dispone de un botón `🗑️` en cada fila de telemetría para eliminar cadetes de prueba con diálogo de confirmación.
  - **Compatibilidad Total en Móvil**: Optimización de peticiones asíncronas para Safari iOS y Chrome Android.

- **Persistencia de Sesión sin Registro Repetido**:
  - Si un usuario ya ha configurado su nombre (ej: `ALEX`), el sistema lo recordará permanentemente en el navegador o PWA móvil sin reiniciar a `PILOTO INVITADO`, incluso si abre de nuevo enlaces de invitación.
  - El Comandante Master (`EC-CHOZAS`) mantiene sus credenciales autorizadas permanentemente.

- **Validación de Calificaciones (0 a 100%)**:
  - Limitación estricta de las casillas de notas en los Libros Maestros: valores mayores a 100 o negativos son automáticamente corregidos y recortados.

- **Pulido de Interfaz en Modal de Perfil**:
  - Eliminado el botón duplicado de cierre al pie del panel; se mantiene el botón superior `✕` optimizado para toques táctiles.
  - Corregido el desbordamiento lateral del botón `💾 Guardar Nombre` en pantallas de smartphone mediante maquetación fluida y adaptativa.
  - Corrección de badges de rol: los invitados siempre visualizan `👨‍✈️ CADETE INVITADO` y únicamente `EC-CHOZAS` accede a los privilegios y corona de `👑 COMANDANTE MASTER`.

---

## [0.8.2] - 2026-09-11
- Corrección de error de inicialización *Temporal Dead Zone* (`ReferenceError`) en la variable de timeout de telemetría.
- Soporte para parámetro URL `?master=1` para forzar el rol Master en cualquier navegador.
- Detección automática y persistencia de URL pública en despliegues sobre Netlify y GitHub Pages.

---

## [0.8.1] - 2026-09-11
- Auditoría técnica al 100% de la base de datos de 168 temas y 13 manuales maestros.
- Validación de integridad de los 336 podcasts bilingües y enlaces de descarga a manuales NotebookLM.

---

## [0.8.0] - 2026-09-11
- **Optimización Móvil**: Conversión responsive de la tabla técnica en tarjetas ergonómicas verticales para smartphones (< 768px), eliminando la necesidad de scroll horizontal.
- **Soporte PWA Android e iOS**: Creación de `manifest.json` e iconos táctiles de alta resolución para instalación directa en la pantalla de inicio sin barra de navegación.

---

## [0.7.0] - 2026-09-11
- Implementación de **AeroQuiz ECQB**: Banco de preguntas de alta frecuencia de examen europeo.
- Algoritmo de permutación aleatoria de opciones de respuesta [A, B, C, D] y explicaciones oficiales EASA.

---

## [0.6.0] - 2026-09-11
- Integración de sistema de sincronización en la nube multi-dispositivo y telemetría de flota vía API REST.
- Monitorización de progreso por alumno y registro de último acceso.

---

## [0.5.0] - 2026-09-10
- **Cockpit Gatekeeper**: Barrera de seguridad con PIN de vuelo privado (`ATPL-2026`) para distribución controlada a beta testers.
- Función para compartir enlaces directos pre-autorizados por WhatsApp.

---

## [0.4.0] - 2026-09-10
- Tema estético inspirado en cabina de vuelo nocturna de aeronave moderna (Dark Glassmorphism).
- Selector de temas Día / Noche / Automático según la hora local.

---

## [0.3.0] - 2026-09-09
- Integración del reproductor de audio para resúmenes bilingües (Inglés: Ryan & Sonia; Español: Álvaro & Elvira).
- Modal bilingüe para selección y lectura de PDFs técnicos generados con NotebookLM.

---

## [0.2.0] - 2026-09-08
- Base de datos relacional de las 13 asignaturas teóricas oficiales EASA ATPL (A) y sus 168 capítulos con tiempos estimados y niveles de dificultad.

---

## [0.1.0] - 2026-09-07
- Prototipo inicial de panel de control de estudio de aviación comercial.
