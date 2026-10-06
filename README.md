# [Título del proyecto: verbo + objeto + contexto]

> **Una frase:** qué pregunta responde este análisis, para quién y con qué datos.
> *(Ej.: "Identifica qué canales de venta tienen peor retención de clientes en 2025, para el equipo comercial, a partir del CRM.")*

⚠️ *Si los datos son simulados, de práctica o parciales, dilo aquí en una línea. Evita que alguien tome tus conclusiones como evidencia real.*

## Estado del proyecto

| Etapa | Estado |
|---|---|
| Brief y definición de métricas (`docs/00_brief.md`) | ⬜ |
| Diccionario de datos (`docs/01_diccionario_datos.md`) | ⬜ |
| Diagnóstico de calidad (`docs/02_calidad_datos.md`) | ⬜ |
| Limpieza y transformación | ⬜ |
| Modelo / métricas (`docs/04_definiciones_metricas.md`) | ⬜ |
| Visualización / informe | ⬜ |
| Hallazgos y recomendaciones (`docs/05_hallazgos.md`) | ⬜ |
| Revisión en frío y cierre (`docs/07_checklist_cierre.md`) | ⬜ |

*Estados: ⬜ pendiente · 🟨 en curso · ✅ hecho. Actualiza esta tabla al cerrar cada sesión de trabajo.*

## Estructura del repositorio

```
├── README.md                    ← estás aquí
├── CHANGELOG.md                 ← versiones del análisis
├── requirements.txt             ← dependencias (si usas Python)
├── docs/
│   ├── GUIA_USO.md              ← cómo usar esta plantilla (borra al terminar)
│   ├── 00_brief.md              ← pregunta, decisión, alcance, métricas
│   ├── 01_diccionario_datos.md  ← qué significa cada columna
│   ├── 02_calidad_datos.md      ← problemas detectados + cifras de control
│   ├── 03_log_decisiones.md     ← qué decidiste, por qué y con qué impacto
│   ├── 04_definiciones_metricas.md
│   ├── 05_hallazgos.md          ← conclusiones y limitaciones
│   ├── 06_guia_git.md           ← flujo de trabajo con Git
│   └── 07_checklist_cierre.md   ← qué revisar antes de entregar
├── data/
│   ├── raw/                     ← dato original. NO SE EDITA NUNCA
│   ├── processed/               ← dato limpio generado por tu código
│   └── external/                ← datos de terceros (calendarios, catálogos…)
├── analisis/                    ← notebooks, SQL, BI, Excel
├── scripts/perfilar_datos.py    ← genera un borrador de calidad de datos
└── outputs/                     ← figuras e informes finales
```

## Cómo reproducir el análisis

1. Clona el repositorio: `git clone <URL>`
2. *(Python)* `pip install -r requirements.txt`
3. Coloca/obtén los datos en `data/raw/` → *dónde conseguirlos:* ✏️
4. Ejecuta, en orden: ✏️ *(ej. `analisis/notebooks/01_...` → `02_...` → `03_...`)*
5. Verifica que tus conteos coinciden con las **cifras de control** de `docs/02_calidad_datos.md`.

## Fuente de los datos

| Dato | Origen | Fecha de extracción | Responsable | Sensibilidad |
|---|---|---|---|---|
| ✏️ | | | | pública / interna / personal |

## Resultados principales

*(Completar al final. 3 a 5 puntos, cada uno con su cifra y el enlace a la sección de `docs/05_hallazgos.md`.)*

## Limitaciones

*(Resumen de 2-3 líneas; el detalle va en `docs/05_hallazgos.md`.)*

## Autoría

- Autor/a: ✏️
- Creado: AAAA-MM-DD · Última actualización: AAAA-MM-DD
