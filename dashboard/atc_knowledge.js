// ═════════════════════════════════════════════════════════════════════════════════
//  ATPL FLIGHT DECK — ATC COPILOT KNOWLEDGE BASE (EASA ECQB / OACI / SERA)
// ═════════════════════════════════════════════════════════════════════════════════

window.ATC_KNOWLEDGE = {
  // Fórmulas de Navegación y Vuelo
  "descenso": {
    topic: "Régimen y Distancia de Descenso (Regla 3:1)",
    answer: `📐 <strong>Cálculo de Descenso 3:1 (Regla Operacional EASA):</strong><br>
• <strong>Distancia TOP OF DESCENT (TOD):</strong> <code>Distancia (NM) = (Altitud a perder en ft / 1.000) × 3</code>.<br>
  <em>Ejemplo:</em> De FL300 a FL100 (perder 20.000 ft) = 20 × 3 = <strong>60 NM antes</strong> (añadir 5-10 NM para desaceleración a 250 kt por debajo de FL100).<br>
• <strong>Régimen de Descenso vertical (V/S en ft/min para senda 3°):</strong><br>
  <code>V/S = Ground Speed (GS) × 5</code> (o GS/2 × 10).<br>
  <em>Ejemplo:</em> GS 140 kt = 140 × 5 = <strong>700 ft/min</strong>.<br>
  <em>Ejemplo:</em> GS 420 kt = 420 × 5 = <strong>2.100 ft/min</strong>.`
  },

  "1 in 60": {
    topic: "Regla 1 in 60 (Error de Derrota y Corrección)",
    answer: `🧭 <strong>Regla 1 in 60 (1 in 60 Rule):</strong><br>
Un desvío de 1 NM a una distancia de 60 NM equivale a <strong>1° de error</strong>.<br>
• <strong>Ángulo de Error de Derrota (Track Error Angle - TE):</strong><br>
  <code>TE (grados) = (Distancia Fuera de Ruta en NM × 60) / Distancia Volada (NM)</code><br>
• <strong>Ángulo de Corrección de Cierre (Closing Angle - CA):</strong><br>
  <code>CA (grados) = (Distancia Fuera de Ruta en NM × 60) / Distancia Restante (NM)</code><br>
• <strong>Corrección Total de Rumbo (Heading Alteration):</strong> <code>Alteración = TE + CA</code> hacia el track nominal.`
  },

  "qnh": {
    topic: "Altimetría: QNH vs QFE vs QNE & Temperatura",
    answer: `🌡️ <strong>Altimetría Aeronáutica (ICAO Doc 8168):</strong><br>
• <strong>QNH:</strong> Presión reducida a nivel medio del mar (MSL) según atmósfera estándar local. Con QNH calado en ventana Kollsman, el altímetro lee <strong>ALTITUD</strong> (en el suelo indica la elevación del campo).<br>
• <strong>QFE:</strong> Presión medida en la estación / umbral de pista. Indica <strong>ALTURA sobre el terreno (AGL)</strong> (en el suelo lee 0 ft).<br>
• <strong>QNE / Estándar (1013.25 hPa / 29.92 inHg):</strong> Se cala al cruzar la Altitud de Transición (TA). Lee <strong>NIVELES DE VUELO (FL)</strong>.<br>
• <strong>Corrección por Temperatura:</strong> <em>"From High to Low, look out below"</em>. Aire frío = altímetro sobreestima (vuelas más bajo de lo que indica). Corrección = <code>4 ft por cada 1°C de desviación ISA por cada 1.000 ft de altura</code>.`
  },

  "transponder": {
    topic: "Códigos Transpondedor de Emergencia OACI",
    answer: `🚨 <strong>Códigos SSR (Modo A) de Emergencia Mundial:</strong><br>
• <strong>7500:</strong> Interferencia Ilícita / Secuestro (<em>"Seven-five, man with knife"</em>).<br>
• <strong>7600:</strong> Fallo de Comunicaciones Radio (<em>"Seven-six, radio need fix"</em>).<br>
• <strong>7700:</strong> Emergencia General / MAYDAY o PAN PAN (<em>"Seven-seven, going to heaven / falling from heaven"</em>).<br>
• <strong>2000:</strong> Código por defecto en espacio no controlado IFR/NAT HLA.<br>
• <strong>7000:</strong> Código conspicuo VFR estándar en Europa (ICAO EUR).`
  },

  "vfr": {
    topic: "Mínimos VFR en Espacio Aéreo (SERA.5005)",
    answer: `☁️ <strong>Mínimos de Visibilidad y Distancia de Nubes VFR (SERA / OACI):</strong><br>
• <strong>Por encima de 3.000 ft AMSL (o 1.000 ft AGL):</strong><br>
  - Visibilidad de vuelo: <strong>5 km</strong> (por debajo de FL100) / <strong>8 km</strong> (en y por encima de FL100).<br>
  - Nubes: 1.500 m horizontal y 1.000 ft (300 m) vertical.<br>
• <strong>En o por debajo de 3.000 ft AMSL (o 1.000 ft sobre terreno en Clase F y G):</strong><br>
  - Visibilidad: <strong>5 km</strong> (reducibles a <strong>1.5 km</strong> para aeronaves volando a ≤140 kt para ver y esquivar tráfico).<br>
  - Nubes: Libre de nubes y con la superficie a la vista permanente.<br>
• <strong>VFR Especial en CTR:</strong> Mínimo 1.5 km visibilidad y techo de nubes ≥600 ft.`
  },

  "etops": {
    topic: "ETOPS / EDTO (Operaciones de Alcance Extendido)",
    answer: `🌊 <strong>ETOPS (Extended Twin-engine Operations):</strong><br>
Aplica a aeronaves de dos motores turbina cuando su ruta supera los <strong>60 minutos</strong> a velocidad de crucero con un motor inoperativo (OEI) en atmósfera calma.<br>
• <strong>Umbrales típicos:</strong> ETOPS 120 min, 180 min y hasta 240+ min (ej: A350, B787, A330).<br>
• <strong>Área de Operación ETOPS:</strong> Círculos de radio <code>Distancia OEI = TAS(OEI) × Tiempo ETOPS</code> centrados en aeródromos alternativos en ruta adecuados y aprobados.<br>
• Requiere combustible crítico ETOPS (despresurización simultánea con fallo motor).`
  },

  "tuc": {
    topic: "Tiempo Útil de Consciencia (TUC) & Hipoxia (040 HPL)",
    answer: `🧠 <strong>Tiempos Útiles de Consciencia (TUC / EPT) ante Despresurización:</strong><br>
• <strong>FL200 (20.000 ft):</strong> 10 minutos.<br>
• <strong>FL250 (25.000 ft):</strong> 3 a 5 minutos.<br>
• <strong>FL300 (30.000 ft):</strong> 1 a 2 minutos.<br>
• <strong>FL350 (35.000 ft):</strong> <strong>30 a 60 segundos</strong>.<br>
• <strong>FL400 (40.000 ft):</strong> 15 a 20 segundos.<br>
• <strong>FL450+ (45.000 ft):</strong> 9 a 12 segundos.<br>
<em>¡Ojo Examen!:</em> En una descompresión explosiva o rápida, el TUC se reduce a la <strong>MITAD</strong> (50%) inmediatamente debido a la espiración forzada y difusión retrógrada de gases en los alvéolos.`
  },

  "mel": {
    topic: "Categorías de Reparación de la MEL (070 OPS)",
    answer: `📋 <strong>Categorías de Inoperatividad MEL (EASA ORO.GEN):</strong><br>
• <strong>Categoría A:</strong> Sin intervalo fijo. Debe repararse en el plazo especificado en la columna "Observaciones" (ej: 3 vuelos, 24 horas, etc.).<br>
• <strong>Categoría B:</strong> Reparación obligatoria en un plazo de <strong>3 días naturales consecutivos</strong> (72 h sin contar el día del reporte).<br>
• <strong>Categoría C:</strong> Reparación obligatoria en un plazo de <strong>10 días naturales consecutivos</strong>.<br>
• <strong>Categoría D:</strong> Reparación obligatoria en un plazo de <strong>120 días naturales consecutivos</strong> (elementos de confort o redundancias secundarias).<br>
<em>Nota:</em> Las Cat B y C admiten una sola extensión bajo autorización técnica CAMO.`
  },

  "rvsm": {
    topic: "Espacio Aéreo RVSM (Separación Vertical Reducida)",
    answer: `🛫 <strong>RVSM (Reduced Vertical Separation Minima):</strong><br>
• Espacio aéreo comprendido entre <strong>FL290 y FL410</strong>.<br>
• La separación vertical mínima se reduce de 2.000 ft a <strong>1.000 ft</strong>.<br>
• <strong>Equipamiento Mínimo Obligatorio:</strong><br>
  1. Dos sistemas primarios independientes de medición de altitud (ADC).<br>
  2. Un sistema automático de control de altitud (Piloto Automático con función Altitude Hold ±65 ft).<br>
  3. Un sistema de alerta de desviación de altitud (aviso sonoro/visual ±200 ft).<br>
  4. Un transpondedor de altitud (Modo C o S).`
  },

  "metar": {
    topic: "Guía de Decodificación Rápida METAR / TAF",
    answer: `🌦️ <strong>Estructura Estándar METAR (050 MET):</strong><br>
<code>LEMD 112000Z 24015G25KT 9999 FEW025 BKN080 18/10 Q1018 NOSIG=</code><br>
• <strong>Viento:</strong> 240° geográfico a 15 kt con ráfagas de 25 kt.<br>
• <strong>Visibilidad:</strong> 9999 = 10 km o más (visibilidad óptima). CAVOK = Visibilidad ≥10 km, sin nubes por debajo de 5.000 ft o MSA y sin fenómenos de tiempo significativo.<br>
• <strong>Nubes:</strong> FEW (1-2 octas a 2.500 ft), BKN (5-7 octas a 8.000 ft = TECHO DE NUBES / CEILING).<br>
• <strong>Temperatura/Rocío:</strong> 18°C aire / 10°C punto de rocío (si se tocan = niebla inminente).<br>
• <strong>QNH:</strong> 1018 hPa.`
  },

  "etp": {
    topic: "Punto de Igual Tiempo (ETP / Critical Point)",
    answer: `⚖️ <strong>Cálculo de ETP (Equi-Time Point / Critical Point):</strong><br>
El punto en la ruta donde el tiempo de vuelo para continuar al destino es igual al tiempo para regresar a la base:<br>
<code>Distancia ETP (desde salida) = (D × H) / (O + H)</code><br>
• <strong>D:</strong> Distancia total entre origen y destino (NM).<br>
• <strong>H:</strong> Groundspeed de regreso a la base (Homebound GS en kt).<br>
• <strong>O:</strong> Groundspeed hacia el destino (Outbound GS en kt).<br>
<em>Propiedad de examen:</em> Si hay viento de cara en la ida, el ETP se desplaza hacia adelante (más cerca del destino). Si hay viento de cola, el ETP se desplaza hacia atrás (más cerca del origen).`
  }
};

window.findATCAnswer = function(query) {
  if (!query) return null;
  const q = query.toLowerCase().trim();
  
  // Direct keyword matching
  for (const key of Object.keys(window.ATC_KNOWLEDGE)) {
    if (q.includes(key)) {
      return window.ATC_KNOWLEDGE[key].answer;
    }
  }

  // Synonyms & Concepts
  if (q.includes('descen') || q.includes('regimen') || q.includes('top of descent') || q.includes('tod')) {
    return window.ATC_KNOWLEDGE["descenso"].answer;
  }
  if (q.includes('60') || q.includes('derrota') || q.includes('error de rumbo') || q.includes('desvio')) {
    return window.ATC_KNOWLEDGE["1 in 60"].answer;
  }
  if (q.includes('altim') || q.includes('qfe') || q.includes('qne') || q.includes('presion') || q.includes('isobar')) {
    return window.ATC_KNOWLEDGE["qnh"].answer;
  }
  if (q.includes('7500') || q.includes('7600') || q.includes('7700') || q.includes('transponder') || q.includes('squawk') || q.includes('radio fallo')) {
    return window.ATC_KNOWLEDGE["transponder"].answer;
  }
  if (q.includes('vfr') || q.includes('ifr') || q.includes('visual') || q.includes('clase g') || q.includes('minimos')) {
    return window.ATC_KNOWLEDGE["vfr"].answer;
  }
  if (q.includes('etops') || q.includes('edto') || q.includes('bimotor') || q.includes('60 minutos')) {
    return window.ATC_KNOWLEDGE["etops"].answer;
  }
  if (q.includes('tuc') || q.includes('hipoxia') || q.includes('oxigeno') || q.includes('descompresion') || q.includes('fl350')) {
    return window.ATC_KNOWLEDGE["tuc"].answer;
  }
  if (q.includes('mel') || q.includes('master mel') || q.includes('inoperat') || q.includes('cat b') || q.includes('cat c')) {
    return window.ATC_KNOWLEDGE["mel"].answer;
  }
  if (q.includes('rvsm') || q.includes('separacion vertical') || q.includes('fl290')) {
    return window.ATC_KNOWLEDGE["rvsm"].answer;
  }
  if (q.includes('metar') || q.includes('taf') || q.includes('cavok') || q.includes('bkn') || q.includes('rvr')) {
    return window.ATC_KNOWLEDGE["metar"].answer;
  }
  if (q.includes('etp') || q.includes('pnr') || q.includes('punto critico') || q.includes('equi-time')) {
    return window.ATC_KNOWLEDGE["etp"].answer;
  }

  // Fallback
  const pilotName = (typeof currentPilot !== 'undefined' && currentPilot) ? currentPilot : 'Piloto';
  return `📡 <strong>ATC Torre en escucha activa para ${pilotName}:</strong><br>
Recibido tu mensaje: <em>"${query}"</em>.<br><br>
Puedo resolver consultas operacionales inmediatas sobre:<br>
• <strong>Altimetría & Presión:</strong> Calados QNH, QFE, QNE y cálculo de error de temperatura.<br>
• <strong>Navegación EASA:</strong> Regla 3:1 de descenso, regla 1 in 60, puntos críticos ETP / PNR.<br>
• <strong>Reglamento SERA/OACI:</strong> Mínimos VFR por clase de espacio, códigos Squawk 7500/7600/7700.<br>
• <strong>Meteorología 050:</strong> Decodificación METAR, TAF, nubes y gradientes ISA.<br>
• <strong>Factores Humanos 040:</strong> Tiempos de consciencia útil TUC, leyes de gases e ilusiones sensoriales.<br>
• <strong>Operaciones 070:</strong> Plazos de reparación MEL (Cat A, B, C, D) y requisitos ETOPS.<br><br>
<em>Selecciona una de las frecuencias de acceso rápido o pulsa ⚙️ para conectar Gemini AI en vivo.</em>`;
};
