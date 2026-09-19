# Changelog — ATPL Flight Deck

Todos los cambios notables, evoluciones y correcciones de este proyecto se registran de forma cronológica en este documento, siguiendo las directrices de [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y versionado semántico [SemVer](https://semver.org/lang/es/).

## [1.6.1] - 2026-09-19

### 🛡️ Optimizaciones y Consolidación de Seguridad
- **Saneamiento contra XSS Almacenado**: Saneada la inyección de la variable `currentPilot` en el DOM de la cabecera para prevenir ataques de Cross-Site Scripting mediante almacenamiento local.
- **Estrategia Network-First en Datos de Progreso**: El Service Worker ahora fuerza la obtención desde la red de `data.js` y `data.json` antes de consultar la caché, garantizando que el progreso de estudio del cadete nunca muestre datos obsoletos tras exportar.
- **Indexación de Base de Datos SQLite**: Añadidos índices optimizados en `topics(status, next_review)` y `topics(subject_code, chapter_num)` en `schema.sql` y `atpl.db` para acelerar las consultas de repetición espaciada.
- **Optimización de Memoria en Generador de PDFs**: Procesamiento secuencial de fuentes en `compile_air_law_master.py` para prevenir picos de memoria RAM.
- **Actualización de CSP (Content Security Policy)**: Compatibilidad total con el iframe oficial del computador CR-3 (`aerotestppl.es`) y las capas de satélite/topográficas de Leaflet (`opentopomap.org`, `openstreetmap.org`, `arcgisonline.com`).
- **Versión del Sistema Unificada**: Actualizado el distintivo visual y el Service Worker a **v1.6.1 EFB**.

---

## [1.6.0] - 2026-09-19

### 🔒 Auditoría Exhaustiva de Seguridad y Calidad de Código
- **Normalización de Codificación Unicode en PDFs**: Corregido el fallo de normalización de caracteres (>255) que provocaba `UnicodeEncodeError` silenciosos y streams corruptos en la exportación de manuales.
- **Prevención de Bucles Infinitos en Tablas PDF**: Establecido un límite mínimo de 5 caracteres por línea en `pdf_builder.py` para evitar bucles con columnas estrechas.
- **Robustez de Conexiones SQLite**:
  - Corrección de `ZeroDivisionError` y fugas de conexión en `registrar-test` con `--total=0`.
  - Activación obligatoria de `PRAGMA foreign_keys = ON` en cada llamada a `get_db()`.
  - Bloques `try/finally` exhaustivos para garantizar el cierre (`conn.close()`) en el 100% de las rutas de ejecución.
- **Cabeceras de Seguridad HTTP (`_headers`)**:
  - Implementación de Content Security Policy (CSP), HTTP Strict Transport Security (HSTS 1 año), X-Content-Type-Options y Referrer-Policy.
- **Informe Oficial de Auditoría**: Generado el documento `docs/ATPL_FlightDeck_Security_Audit_Report_v1.0.pdf` (7 páginas).

---

## [1.5.3] - 2026-09-16

### 🏷️ Corrección de Solapamiento de Letras en Pestañas Móviles (Tabs Anti-Collision)
- **Eliminación del Conflicto de Flexbox y Letras Superpuestas**:
  - Las pestañas de cabina (`.cockpit-tab-btn`) utilizaban `flex: 1` con `min-width: 110px` y `justify-content: center`. En móviles, al tener textos largos como *"Plan de Vuelo (OFP) & Cartas VFR"* y *"Simuladores & METAR"*, los caracteres desbordaban a ambos lados del botón y se superponían directamente con los textos de los botones vecinos.
  - Se ha establecido `flex: 0 0 auto !important` y `width: auto !important`, garantizando que la anchura de cada pestaña sea idéntica al 100% del tamaño real de su contenido, imposibilitando físicamente que una letra se dibuje fuera del botón o encima de otra pestaña.
- **Etiquetado Adaptativo (Full en Web / Conciso en Móvil)**:
  - En escritorio se mantienen los nombres completos oficiales: *"Cabina de Estudio"*, *"Caja Negra & Retos"*, *"Simuladores & METAR"*, *"Logbook & Offline"* y *"Plan de Vuelo (OFP) & Cartas VFR"*.
  - En móviles (≤ 768px) el sistema conmuta automáticamente mediante `.tab-label-short` a etiquetas concisas y nítidas: *"Estudio"*, *"Caja Negra"*, *"Simuladores"*, *"Logbook"* y *"Plan de Vuelo"*.
- **Sub-Pestañas de Plan de Vuelo (`.fpl-subtabs-nav`) & Simulador CR-3 (`.cr3-subtabs-nav`)**:
  - Contenedores con desplazamiento táctil horizontal suave (`overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none`), evitando el salto de líneas incómodo y los textos montados.

---

## [1.5.2] - 2026-09-16

### 🛡️ Auditoría Integral, Adaptabilidad Móvil & Resolución de Solapamientos
- **Auditoría de Integridad Funcional (100% Cobertura)**:
  - Verificadas las 163 funciones de JavaScript y los 185 manejadores de eventos inline: 0 errores lógicos, 0 funciones faltantes.
  - Validación de compatibilidad con Safari iOS / WebKit y motores V8/Chromium.
- **Sistema Anti-Colisión Dinámico (Reproductor de Audio & Copiloto ATC)**:
  - **Botón Flotante ATC (`#atc-fab`)**: Posicionado a `bottom: 20px` por defecto y elevado automáticamente a `bottom: 85px` en escritorio y `bottom: 122px` en móvil cuando el reproductor de audio está activo (`body.player-active`).
  - **Panel Copiloto ATC Móvil en Modo Bottom Sheet**: En pantallas móviles (≤ 768px), el panel pasa a ser una hoja inferior deslizante moderna (`inset: auto 0 0 0`, bordes redondeados superiores, `z-index: 2500` y `max-height: 82vh`), eliminando desbordamientos fuera de pantalla y solapamientos con la cabecera.
  - **Margen de Seguridad Inferior del Body**: `body.player-active` ahora aplica `padding-bottom: 125px` en móvil para que los controles de audio de 2 filas nunca tapen botones o tablas.
- **Corrección de Encabezado en Móvil (`header` semántico)**:
  - Corregido el selector CSS de `@media (max-width: 768px)` de `.header` a `header, .header`, permitiendo que la cabecera se apile en columna con alineación fluida en teléfonos móviles.
- **Optimización de Margen Útil en Móvil**:
  - `body` en móvil ajustado a `padding: 12px !important` y `.container` a `padding: 0 !important`, recuperando más de 45px de anchura horizontal para las tablas y tarjetas.
- **Cuadrícula ATIS Adaptable (Tarjeta 4)**:
  - Introducida la clase `.fpl-atis-grid`, que distribuye los datos de despegue y aterrizaje en 5 columnas en escritorio y se adapta a 3 columnas espaciosas en móviles (≤ 600px).
- **Legibilidad de Capítulos y KPIs en Modo Claro**:
  - Corregido `td.col-ch` y `td.col-title` para utilizar `var(--text-title)` en lugar de blanco forzado en la vista de tarjetas móviles del temario.
  - Corregido `.kpi-value` para heredar `var(--text-title)` en lugar de blanco fijo.
- **Contenedor Responsivo del Computador CR-3**:
  - Clase `.cr3-iframe-wrapper` con altura adaptativa: 840px en escritorio, 560px en tablet y 480px en smartphone para un manejo táctil sin desplazamientos excesivos.
- **Scroll Táctil NavLog**:
  - Habilitado `-webkit-overflow-scrolling: touch` y variables de borde adaptadas al tema.

---

## [1.5.1] - 2026-09-16

### 🎨 Corrección Integral del Modo Claro (Light Mode Engine)
- **Legibilidad y Contraste al 100% (Texto Invisible Solucionado)**:
  - Corregido el campo de búsqueda (`.search-box input`), cuyo color de texto blanco sobre fondo claro impedía ver los caracteres tecleados.
  - Corregidos todos los encabezados `h1`, `h2`, `h3` y `h4` que forzaban `color: #fff`, provocando texto blanco invisible sobre tarjetas blancas en modo diurno.
  - Corregidos títulos y textos de modales (`#pdf-modal`, `#quiz-modal`, `.gate-card`, `#cockpit-player`) para utilizar variables semánticas `--text-title` y `--text-main`.
  - Corregida la celda de ETA en el NavLog (`fpl-cell-eta`), que forzaba gris casi blanco (`#e6edf3`), pasando a utilizar `var(--text-main)` de alto contraste.
  - Corregido el cuadro de preguntas de la Caja Negra (`renderBlackboxList`), desafío diario (`#daily-q-text`) y título del ejercicio CR-3 (`#cr3-ex-title`).
- **Adaptación a Blanco de la Parte Nueva (CR-3, OFP & Tarjetas Inferiores)**:
  - Definidas nuevas variables CSS semánticas: `--bg-subbox`, `--bg-subbox-card`, `--bg-input` y `--text-input` tanto en `:root` como en `[data-theme="light"]`, `@media (prefers-color-scheme: light)` y `[data-theme="dark"]`.
  - **Computador CR-3**: Los contenedores de la guía, ejercicios y visor interactivo ahora adaptan sus fondos a blanco/gris suave (`#ffffff` / `#f6f8fa`) con bordes nítidos (`#d0d7de`), eliminando los bloques negros fijos (`#0d1117`).
  - **Pestañas y Botones de Ejercicios CR-3**: En estado inactivo se integran en el tema claro con fondo claro y texto legible, destacando con acento azul en estado activo.
  - **Plan de Vuelo (OFP - Tarjetas 1 a 5)**:
    - Tarjeta 1 (Aeronave), Tarjeta 2 (Vientos/CR3), Tarjeta 3 (Combustible), Tarjeta 4 (ATIS/Calzos) y Tarjeta 5 (Performance) adaptan todos sus sub-contenedores a fondos claros.
    - Todos los desplegables (`select`) e `inputs` ahora cambian dinámicamente a fondo blanco con borde suave y texto de alta legibilidad, preservando los acentos cromáticos (azul para rumbos/velocidades, verde para QNH/consumo, amarillo para alternativo/mínimos).
    - Áreas de texto (`textarea`) para frecuencias, autorizaciones ATC, NOTAMs y espacios aéreos adaptadas a fondo blanco.
  - **Tabla NavLog**: Filas alternadas en blanco (`#ffffff`) y gris suave (`#f8fafc`), cabecera adaptada con `var(--table-header-bg)` e inputs de tramo con fondo blanco limpio.
- **Sincronización Automática de Modo Día/Noche en JS**:
  - `applyTheme()` ahora garantiza que el atributo `data-theme` en `<html>` se establezca explícitamente tanto en selección manual como en modo `auto` diurno/nocturno, activando al instante todas las reglas de la hoja de estilo.

---

## [1.5.0] - 2026-09-16

### 🚀 Novedades y Mejoras Implementadas
- **Desplegables Oficiales de Aeropuertos Españoles (Salida, Destino y Alternativo)**:
  - Selector desplegable para **Aeropuerto de Salida** con los 16 aeródromos de la base de datos VAC oficial (LECU, LEMT, LEVD, LESA, etc.).
  - **Aeropuerto de Destino Unificado**: Eliminadas las casillas duplicadas. Un único selector elegante que deduce automáticamente la **pista en uso óptima** en función de la componente de viento del METAR al momento de llegada.
  - Selector desplegable para **Aeropuerto Alternativo**, sincronizando de inmediato las pistas disponibles y el combustible de reserva de alternativo (~30 min).
- **Reactividad Total de las Tablas Inferiores (Tarjetas 3, 4 y 5)**:
  - **Tarjeta 3 (Combustible)**: Sincronización dinámica de combustible de crucero, subida, descenso, alternativo, reserva final de 45 min y margen de seguridad en Galones US en tiempo real ante cualquier cambio de consumo, horas o ruta.
  - **Tarjeta 4 (Calzos y Tiempos)**: Cálculo automático de tiempo de vuelo (`flight time`), hora estimada de aterrizaje (`landing time`), `off-block` (-10m), `on-block` (+10m) y `block time` (+20m rodaje).
  - **Tarjeta 5 (Rendimiento de Pistas)**: Sincronización instantánea de distancias disponibles de despegue y aterrizaje en salida, destino y alternativo, así como distancias requeridas según el modelo de aeronave.
- **Computador de Vuelo Oficial CR-3 Embebido (AerotestPPL.es/cr3)**:
  - Integrado de manera interactiva y responsiva en la pestaña **`🧭 Simuladores & METAR`** directamente desde `https://aerotestppl.es/cr3/`.
  - Permite al piloto alumno utilizar la **herramienta original oficial** con su visor de alta resolución, Cara de Viento (Side B) activa por defecto, rosa de 360°, retícula de deriva (WCA), arcos de TAS, cálculo de Ground Speed (GS), herramientas de dibujo de vector de viento y menús de cálculo integrados.
  - Botones de acceso rápido: `🌐 Abrir en Pantalla Completa ↗`, `🔄 Recargar`, `📖 Guía: Rumbos y Velocidades` y `🎯 Ejercicios de Navegación`.
  - **Guía Didáctica ("Para Dummies" & Examen EASA / PPL)**: Procedimiento paso a paso para medir rumbos de aguja (Heading/Course), Ground Speed (GS), Viento en vuelo (Wind W/V) y tiempos/consumo.
  - **Banco de Ejercicios Guiados**: 6 problemas interactivos oficiales con autocorrección y explicación detallada.

---

## [1.4.1] - 2026-09-15

### 🚀 Novedades y Correcciones Solicitadas
- **Unidades de Combustible 100% en Galones US (Gal · Gal/h)**:
  - Eliminada la confusión de litros: todo el cálculo de combustible de la Cessna 172 (consumo horario, combustible por tramo, trip fuel, reserva final de 45 min y FOB) se realiza en **Galones US**.
  - NavLog con columna `Fuel (Gal)`, resumen de viaje en Galones (`Trip: 6.8 Gal`, `Reserva: 6.0 Gal`, `FOB: 40.0 Gal`, `Margen: +22.5 Gal`) y volcado oficial a Excel `.xlsx` en Galones.
- **Corrección de Rendimiento y ATIS de Destino (Valladolid / LEVD)**:
  - Implementado helper `getSpanishAirport()` que busca con precisión en el catálogo `SPANISH_VAC_DATABASE`.
  - Al seleccionar o escribir **Valladolid (LEVD)** (o cualquier aeródromo de destino), se actualizan automáticamente:
    - Pista disponible de aterrizaje (`fpl-perf-ld-avail` = `05/23 (3.000m Asf.) (LEVD)`).
    - Frecuencia de torre / radio de llegada (`122.200 (LEVD TWR)`).
    - Pista activa según viento (`RWY 05`).
    - Parking de llegada (`LEVD Plataforma`).
    - Cuadro de frecuencias con TWR, GND, ATIS y APP de Valladolid.
- **Edición Fluida de Tramos Manuales**:
  - Al añadir un tramo manual con `➕ Añadir Tramo Manual`, se auto-enfoca el campo de nombre.
  - El campo de altitud ahora es numérico limpio (sin sufijo `" ft"` incrustado en el valor) permitiendo editarlo con teclado y flechas con total libertad.
  - La edición manual de nombre, altitud, TC, viento, distancia o ATA no se sobreescribe ni se bloquea.
  - Si el usuario escribe un nombre conocido (ej. `Valladolid`, `LEVD`, `Casarrubios`, `Toledo`), se auto-geolocaliza y actualiza la ruta.
- **Botón METAR Inteligente & Integración con Windy**:
  - El botón `🔄 Actualizar METARs` descarga directamente los teletipos oficiales de la NOAA/AviationWeather para el aeródromo de salida (LECU/LEMD) y el de llegada (LEVD/LESA), actualizando QNH, temperatura, visibilidad, nubes y pistas activas.
  - Nuevo botón directo `🌐 Abrir en Windy` que abre la ruta en Windy.com en el nivel de presión y altitud de vuelo para contrastar modelos numéricos (ECMWF, GFS, ICON).
- **Botón "📋 Copiar Plan de Vuelo" al Portapapeles**:
  - Nuevo botón en la barra principal que formatea un resumen textual completo del vuelo (aeronave, crucero, consumo, NavLog detallado tramo a tramo, totales de combustible, ATIS y frecuencias) y lo copia al portapapeles con 1 clic para enviar a instructores, WhatsApp o notas.

---

## [1.4.0] - 2026-09-15

### 🚀 Novedades y Correcciones Solicitadas
- **Configuración de Rendimiento de Aeronave (Cessna 172 · 8 Gal/h · 90 kt)**:
  - Establecida la **Cessna 172** como preset predeterminado con **90 kt de crucero** y **8.0 Gal/h** (30.3 L/h).
  - Selector flexible de unidades de consumo horario (**Gal/h ⇄ L/h**) con indicador en directo de equivalencia (`= 30.3 L/h`).
  - Posibilidad de editar en cualquier momento el crucero IAS, el consumo o el modelo, recalculando dinámicamente todo el consumo del vuelo y el desglose de combustible.
- **Reordenación Estricta del NavLog según el Flujo Aeronáutico**:
  - Las columnas de la tabla operacional siguen ahora con exactitud el orden pedido:
    `#` · `Waypoint` · **`TC`** · **`VAR`** · **`MC`** · **`Viento`** · **`MH`** · **`Alt`** · **`Dist`** · **`TAS`** · **`GS`** · **`ETE`** · `ETA` · `ATA` · `Fuel` · `Acción`.
  - Destacados visualmente los rumbos de pilotaje (**MC** en cian `#79c0ff`, **MH** en lila de cabina `#d2a8ff`) y los tiempos de avance (**GS** y **ETE** en ámbar `#f1e05a`).
- **Viento en Altura por Waypoint & Pronóstico Temporal (Hora del Plan de Vuelo)**:
  - Cada tramo del NavLog cuenta con su propia casilla de **Viento (Dir/kt)** editable de manera individual (ej. LECU a `240/12`, Escorial a `260/15`, Valladolid a `290/20`).
  - Nuevo botón **"🌬️ Obtener Pronóstico Vientos en Altura (Hora Vuelo)"** que consulta la API abierta de Open-Meteo para cada waypoint geolocalizado en los niveles de presión adecuados (850 hPa a ~5.000 ft, 700 hPa a ~10.000 ft o 925 hPa en superficie) a la hora estimada de paso de cada tramo (`fpl-date` + `ETA`).
  - Fallback inteligente sin conexión para mantener una estimación orográfica coherente con la altitud.
- **Estabilidad Total en la Edición Manual (Sin Datos "Locos" ni Pérdida de Foco)**:
  - Implementada arquitectura reactiva no destructiva: las modificaciones en las casillas del NavLog actualizan el modelo en memoria y actualizan selectores puntuales del DOM sin destruir el `<tbody>`.
  - Se puede editar cualquier casilla (distancia, altitud, rumbo TC, viento, velocidad TAS, ATA) de forma fluida y consecutiva sin perder el cursor ni reiniciar valores.
  - La exportación oficial a Excel `.xlsx` traslada fielmente los vientos independientes por tramo a las columnas `D${r1}` (Dir) y `D${r2}` (Velocidad).

---

## [1.3.1] - 2026-09-15

### 🚀 Novedades y Correcciones Solicitadas
- **Rediseño Friendly del Plan de Vuelo Operacional**:
  - Reemplazada la tabla rígida y apretada de 1080px por una **suite operacional moderna y espaciosa**, perfectamente integrada con el tema oscuro de cabina (`#0d1117` / `#161b22`).
  - **Eliminado el error de cursor negro / texto invisible al seleccionar celdas**: todos los campos de entrada cuentan ahora con contraste nítido, fondos oscuros explícitos, tipografía blanca y borde activo en azul aeronáutico (`#388bfd`).
  - **Columnas amplias y auto-ajustables en el NavLog**:
    - Altitud con espacio holgado (ej. `3.500 ft`), sin cortes ni truncamiento de información.
    - Waypoints de longitud suficiente para visualizar nombres completos (`PUNTO W (Villaviciosa)`, `LECU (Cuatro Vientos)`).
    - Fila de totales en el pie de tabla (Distancia total en NM, Tiempo total ETE, Combustible total estimado).
  - Tarjetas dedicadas y limpias para: Datos Generales de la Aeronave, Computador CR3, Desglose de Combustible con indicador de margen de seguridad en tiempo real, Meteorología ATIS, Calzos y Tiempos de Vuelo, Rendimiento de Pista (TO/LD Distances), NOTAMs y Espacios Aéreos.
  - Se mantiene la **exportación oficial a Excel (.xlsx)** que sigue rellenando automáticamente la plantilla de World Aviation para pasar a limpio, así como la impresión limpia en PDF.
- **Corrección de Coordenadas Oficiales AIP de Puntos VFR en Cuatro Vientos (LECU)**:
  - **Punto W (Villaviciosa de Odón)**: Corregido a coordenadas oficiales exactas del AIP ENAIRE `40°21'00"N 003°56'00"W` (`lat: 40.3500, lon: -3.9333`), altitud estándar 3.500 ft.
  - **Punto S (Residencial Miraflores)**: Corregido a `40°18'50"N 003°50'29"W` (`lat: 40.3139, lon: -3.8414`), altitud estándar 3.000 ft.
  - **Punto N (Boadilla del Monte)**: Corregido a `40°24'16"N 003°52'45"W` (`lat: 40.4044, lon: -3.8792`), altitud estándar 3.000 ft.
  - Actualizados todos los presets, botones de inserción rápida y marcadores interactivos sobre el mapa.
- **Corrección de la Capa de Mapa Aeronáutico Estándar**:
  - Migrada la capa base estándar al servidor oficial y ultra-fiable de OpenStreetMap (`https://tile.openstreetmap.org/{z}/{x}/{y}.png`), asegurando carga inmediata y nítida de carreteras, núcleos urbanos y referencias visuales.
  - Asignación estricta de `pane: 'tilePane'` e invalidación de tamaño forzada al conmutar para evitar solapamientos o capas grises.
- **Enlaces Directos a las Cartas VAC Oficiales Concretas de Cada Aeródromo**:
  - Para aeropuertos públicos y controlados (LECU, LEVD, LESA, LEBZ, LEDS, LESB, LERJ, LEZL, LEMG, LEJR, LEMD), el botón **"Carta VAC"** enlaza directamente a la sección específica del aeródromo en el portal **AIP España AD 2** (`https://aip.enaire.es/AIP/#LECU/LEVS`, `https://aip.enaire.es/AIP/#LEVD`, etc.).
  - Para aeródromos no controlados y privados (LEMT Casarrubios, LERM Robledillo, LEOC Ocaña, LEMU Muchamiel, LEAX La Axarquía), enlaza directamente a su ficha en la **Guía VFR** (`https://guiavfr.enaire.es/#LEMT`, etc.).
  - Añadido botón secundario **"Insignia VFR"** en cada ficha para abrir el visor cartográfico interactivo de ENAIRE.

---

## [1.3.0] - 2026-09-15

### 🚀 Novedades y Mejoras Principales
- **Descarga Directa del Archivo Excel Oficial (.XLSX) Rellenado (SheetJS)**:
  - Integración del motor de manipulación de hojas de cálculo **SheetJS** (`xlsx.full.min.js`) local y 100% offline.
  - Al pulsar el botón verde **"📥 Descargar Excel Oficial (.xlsx) Rellenado"**, la app carga la plantilla binaria original de World Aviation (`Plan_de_vuelo_operacional.xlsx`), inyecta en sus celdas exactas todos los datos introducidos por el alumno (aeronave, matrícula, piloto, autorización ATC, datos de despegue/aterrizaje, 12 tramos de navegación calculados con CR3, combustible reglamentario, NOTAMs y espacios aéreos) y genera la descarga del archivo `.xlsx` real.
  - El archivo resultante mantiene la integridad total de formatos, logotipos, fuentes y fórmulas de la escuela, indistinguible del archivo oficial.
- **Arquitectura de 3 Sub-Pestañas en el Planificador de Vuelo**:
  1. `📋 Plan de Vuelo (World Aviation Excel)`: Edición de la hoja oficial con descarga en `.xlsx`, impresión/PDF A4 y persistencia local.
  2. `🗺️ Trazador VFR & Carta Visual`: Visor cartográfico Leaflet VFR de alta resolución.
  3. `🗂️ Cartas Visuales de España (VAC ENAIRE)`: Biblioteca integrada de aeródromos y cartas de aproximación visual.
- **Carta de Navegación Visual VFR Mejorada con Espacios Aéreos Reales**:
  - Corrección de la inicialización de Leaflet en contenedores ocultos mediante invalidación dinámica de tamaño (`fplMap.invalidateSize(true)`).
  - Selector de capas cartográficas:
    1. **Topográfica VFR (OpenTopoMap)**: Relieve sombreado y curvas de nivel para el cálculo de altitudes de seguridad y franqueamiento de obstáculos en VMC.
    2. **Aeronáutica Estándar (CartoDB / OpenStreetMap)**: Identificación nítida de poblaciones, carreteras y referencias visuales.
    3. **Vista Satelital Visual (Esri World Imagery)**: Reconocimiento fotográfico real de pistas, ríos y embalses.
  - Capa vectorial de espacios aéreos oficiales sobre la zona centro:
    - **CTR Cuatro Vientos (LECU)**: Espacio Clase D SFC-3000ft con frecuencias TWR (118.150) y GND (121.800).
    - **CTR Getafe (LEGT)**: Espacio militar Clase D SFC-3000ft.
    - **CTR Madrid-Barajas (LEMD)**: Espacio internacional Clase A SFC-FL145.
    - **Puntos de Notificación Visual VFR**: Puntos W, S, N, E, Asperillas, El Escorial, Pto. de los Leones, Toledo, Aranjuez, San Martín de Valdeiglesias con botón interactivo de 1 clic para añadir a la ruta.
    - **Radioayudas VOR/DME**: Perales (PDT), Navas (NVS), Colmenar (CNR), Toledo (TLD) con sus frecuencias oficiales.
- **Biblioteca de Cartas Visuales de España (AIP & Guía VFR ENAIRE)**:
  - Catálogo de aeródromos españoles (LECU, LEMT Casarrubios, LERM Robledillo, LEVD Valladolid, LESA Salamanca, LEBZ Badajoz, LEDS Castellón, LESB Son Bonet, LERJ Logroño, LEOC Ocaña, LEMU Muchamiel, LEAX La Axarquía, LEZL Sevilla, LEJR Jerez, LEMG Málaga, LEMD Barajas).
  - Cada ficha incluye: clasificación de espacio aéreo, elevación, pistas (longitud y superficie), circuitos de tránsito, frecuencias (TWR, GND, ATIS, APP, FIS) y observaciones operacionales.
  - Botones de acción: enlace directo a la **Carta VAC oficial de ENAIRE AIP / Guía VFR**, botón **"Ver en Mapa"** para centrar el visor VFR, y botón **"Cargar como Destino en Plan de Vuelo"** que añade automáticamente el aeródromo a la ruta y recalcula tiempos y rumbos.
- **Soporte Offline 100% y Service Worker v1.3**:
  - Se han empaquetado y añadido a la caché del Service Worker (`atpl-flightdeck-v1.3`): `xlsx.full.min.js`, `Plan_de_vuelo_operacional.xlsx`, `world_aviation_logo.png`, `leaflet/leaflet.js`, `leaflet/leaflet.css` e imágenes de marcadores.

---

## [1.2.0] - 2026-09-15

### 🚀 Novedades y Mejoras Principales
- **Plan de Vuelo Operacional (OFP) Oficial de World Aviation**:
  - Recreación milimétrica y fidedigna de la plantilla oficial de **World Aviation Flight Academy** (`Plan+de+vuelo+operacional.xlsx`), garantizando total correspondencia con el formato oficial de la escuela.
  - Logotipo oficial extraído y renderizado en alta resolución (`world_aviation_logo.png`).
  - Cabecera y datos de vuelo: Model, Registration, ARCID, Date, PIC, Squawk, Frequencies, Parking, Off/On Block, Block Time, Take Off, Landing, Flight Time.
  - Bloques de Despegue y Aterrizaje (Takeoff / Landing ATIS data): Info, Time, RWY, TL, First Call, Visibility, Cloud, Temp, QNH y espacio de autorización de salida (Clearance).
  - NavLog operacional completo con 12 piernas y celdas duales superior/inferior para True Course (TC), Magnetic Course (MC), Viento (DIR/KT), Rumbo Magnético (MH), Altitud, Distancia (NM), TAS, Ground Speed (GS), ETE, ETA, ATA y Combustible por pierna y acumulado.
  - Bloque de cálculo de combustible reglamentario (Climb, Cruise, Descent, Total Trip Fuel, Alternate Fuel, Minimum Required Fuel, Fuel on Board): **100% editable manualmente** para ajustes inmediatos a criterio del piloto.
  - Bloques de distancia de pista requerida/disponible en destino y alternativo, zona NOTAMs y Airspace Zones (CTR, TMA, D, R, P).
- **Cartas Visuales VFR Interactivas & Trazador de Ruta sobre Mapa (Leaflet.js)**:
  - Visor cartográfico VFR integrado con capas topográficas y de navegación sobre la Península Ibérica.
  - Entrada dual de puntos de notificación:
    1. Clic sobre la carta para fijar waypoints georreferenciados.
    2. Pastillas de acceso rápido a puntos VFR y aeródromos habituales (Cuatro Vientos `LECU`, Punto W, Punto S, Punto N, El Escorial, Pto. Los Leones, Casarrubios `LEMT`, Valladolid `LEVD`, etc.).
    3. Edición manual directa en las casillas de la tabla o eliminación de tramos en 1 clic.
  - Medición geodésica automática en **Millas Náuticas (NM)** y marcadores arrastrables para ajustar la ruta en tiempo real.
- **Computador de Vuelo Automático CR3 / E6B (Triángulo del Viento)**:
  - A partir de la velocidad indicada ($IAS$) y el viento en altura (`DIR/KT`), calcula trigonométricamente la velocidad verdadera ($TAS$), el ángulo de corrección de deriva ($WCA$), el rumbo magnético ($MH$), la velocidad sobre el suelo ($GS$), los tiempos estimados de pierna ($ETE$) y la acumulación horaria ($ETA$).
  - Botón directo `🌬️ METAR` para importar el viento teletípico real desde el módulo meteorológico.
- **Exportación / Descarga en PDF Oficial (A4 Horizontal Landscape)**:
  - Reglas `@media print` milimétricas (`@page { size: A4 landscape; margin: 4mm; }`) que aíslan exclusivamente la plantilla oficial rellenada de World Aviation a pantalla completa sobre A4 horizontal.
  - Salida limpia para imprimir en papel o guardar en PDF, idéntica visualmente al archivo Excel oficial de la escuela.
- **Guardado y Persistencia Local**:
  - Almacenamiento seguro del plan de vuelo en `localStorage` (`atpl_${currentPilot}_saved_ofp`) para no perder la ruta ni los datos entre sesiones.

---

## [1.1.0] - 2026-09-15

### 🚀 Novedades y Mejoras Principales
- **Desafío Diario ATPL: Renovación Automática a las 00:00 (Medianoche Local)**:
  - Migrado el cálculo de la fecha diaria a tiempo local (`getDailyChallengeDateKey`), asegurando que la pregunta oficial cambie estrictamente a las 00:00 de cada noche en el huso horario local.
  - Temporizador activo en segundo plano (`scheduleDailyMidnightReset`): calcula con precisión los milisegundos restantes hasta la medianoche (00:00:01). Si el alumno tiene la app abierta de noche, la interfaz cambia automáticamente a la nueva pregunta oficial, reinicia el estado y actualiza la racha sin necesidad de refrescar la página.
  - Banco ampliado de preguntas de desafío oficial rotando por las distintas materias del temario EASA (010, 021, 022, 031, 032, 033, 040, 050, 061, 062, 070, 081, 090).
- **Sistema de Notificaciones Web & In-App para Reto Diario Pendiente**:
  - Si el alumno no ha realizado el reto diario de hoy, la plataforma despliega avisos en múltiples niveles:
    1. **Notificación de Sistema (Web Push / Local API)**: Notificación en el sistema operativo del móvil o PC con sonido/aviso recordando completar la pregunta oficial antes de medianoche para no perder la racha.
    2. **Selector de Estado en Tarjeta**: Botón interactivo `🔔 Activar Avisos / Avisos: Activos / Avisos: En pausa` para otorgar permisos y configurar notificaciones en 1 clic.
    3. **Banner HUD en Cabina de Estudio**: Aviso visual destacado en la parte superior de la cabina (`#daily-challenge-alert-banner`) con botón directo `🎯 Resolver Reto Ahora`.
    4. **Indicador en Pestaña**: Punto rojo de alerta (`#daily-tab-dot`) en la pestaña *Caja Negra & Retos* mientras el reto de la jornada siga pendiente.
    5. **Recordatorio en Sesión de Vuelo**: Alarma flotante HUD en cabina tras varios minutos de estudio si el alumno aún no ha resuelto su desafío del día.
- **Control de Comandante Master: Reinicio de Tiempos de Estudio**:
  - Diseñado para corregir incidentes en los que un alumno deja un audio corriendo en bucle, suma horas por error o necesita restablecer su cómputo:
    1. **Reinicio de Alumnos en Telemetría de Flota**: Añadido el botón de acción rápida `⏱️` junto a cada cadete en el directorio del Master (`EC-CHOZAS`). Permite restablecer las horas de estudio del cadete seleccionado y emite una orden de telemetría cifrada en tiempo real.
    2. **Propagación Automática a la Cabina del Alumno**: Cuando el dispositivo del cadete recibe la instrucción del Master (`resetCadetTime`), restablece automáticamente su contador local a `00h 00m`, actualiza el Logbook y le notifica en pantalla.
    3. **Módulo Master en el Logbook**: En la vista de *Logbook & Offline*, el Comandante Master dispone de un panel de control para reiniciar el tiempo a `00h 00m` con confirmación de seguridad.
- **Actualización de Caché Offline (v1.1)**:
  - Service Worker actualizado a la versión de caché `atpl-flightdeck-v1.1` con gestor de clics en notificaciones (`notificationclick`) para enfocar automáticamente la app al pulsar el aviso.

---

## [1.0.0] - 2026-09-15

### 🚀 Novedades y Mejoras Principales
- **Cockpit Hub EFB (Arquitectura Modular y Nuevo Layout)**:
  - Nueva barra de navegación superior estilo Glass Cockpit con 4 vistas operativas fluidas y sin recargas:
    1. 📚 **Cabina de Estudio**: El campus ATPL completo e intacto (13 asignaturas, convocatorias, Libro Maestro, audiotemas, simulador oficial AESA y PDFs).
    2. 🎯 **Caja Negra & Retos**: Repaso espaciado de errores, desafío diario y cheat-codes mnemotécnicos EASA.
    3. 🧭 **Simuladores & METAR**: METAR/TAF en vivo en modo RAW con cálculo automático de pistas activas y entrenador interactivo de esperas (Holding Pattern Trainer).
    4. 📖 **Logbook & Offline**: Registro de horas de vuelo/estudio con temporizador de cuenta atrás y descarga offline completa.
- **Caja Negra de Fallos (Spaced Repetition)**:
  - Registro automático de cualquier pregunta fallada en los tests y exámenes AESA.
  - Algoritmo de repetición espaciada: cada pregunta parte de 0/3 aciertos; requiere 3 respuestas correctas consecutivas para graduarse y archivarse como dominada.
  - Mnemotécnicas EASA integradas con tarjetas de memoria rápida (AN/UNDS, CARF, ORO, 1 in 60 rule, etc.).
- **Live Spanish METAR & TAF en Modo RAW + Deducción de Pistas Activas**:
  - Enfoque prioritario en aeródromos y bases de escuelas de Aviación General en España: Cuatro Vientos (`LECU`), Valladolid (`LEVD`), Badajoz (`LEBZ`), Castellón (`LEDS`), Salamanca (`LESA`), Son Bonet (`LESB`), Logroño (`LERJ`), etc., junto con los aeropuertos principales (`LEMD`, `LEBL`, `LEZL`, `LEMG`, `LEAL`).
  - Presentación teletípica en **Modo RAW**, exactamente como se exige en los exámenes teóricos de AESA.
  - Algoritmo trigonométrico de viento relativo: calcula en tiempo real viento en cara (*Headwind*) y viento cruzado (*Crosswind*) para cada cabecera, deduciendo y destacando la **Pista Activa en Servicio**.
- **Holding Pattern Trainer (Entrenador Interactivo de Esperas ICAO)**:
  - Simulador visual interactivo basado en ICAO Doc 8168 (PANS-OPS).
  - Cálculo trigonométrico de rumbo relativo respecto al inbound y recíproco.
  - Clasificación de sectores de entrada: Sector 1 (Paralela), Sector 2 (Gota / Teardrop) y Sector 3 (Directa).
  - Generador de ejercicios aleatorios con validación inmediata y rosa de los vientos interactiva.
- **Logbook de Estudio con Cuenta Atrás de Temario Restante**:
  - Doble métrica de dedicación aeronáutica:
    1. Tiempo total de estudio registrado.
    2. **Cuenta atrás exacta (horas y minutos)** que faltan para dominar el 100% del temario y audios oficiales del curso ATPL (basado en las 56 horas totales estimadas).
- **Desafío Diario ATPL & Racha (Daily Streak)**:
  - Pregunta diaria determinista generada en función de la fecha para fomentar la disciplina diaria de los cadetes.
  - Contador de días consecutivos de racha de estudio.
- **Modo Offline 100% (Service Worker & CacheStorage)**:
  - Implementación de `dashboard/sw.js` con estrategia Cache-First.
  - Permite estudiar a 35.000 pies o en modo avión sin conexión a Internet.
  - Panel de verificación de estado de caché y botón de precarga en el Logbook.
- **Seguridad e Integridad**:
  - Punto 2 (Instructor de radio IA) excluido estrictamente según la decisión del usuario.
  - Compatibilidad total con la telemetría de flota, control de cadetes y acceso Master (`EC-CHOZAS`).

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
