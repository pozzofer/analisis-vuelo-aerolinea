# Guía de uso de esta plantilla

Esta plantilla sirve para **cualquier análisis de datos**, con cualquier herramienta (Excel, SQL, Python, R, Power BI, Tableau…). Los documentos son los mismos; lo que cambia es el contenido.

## Cómo empezar un proyecto nuevo

**Si usas GitHub (recomendado):** en el repositorio de la plantilla, ve a *Settings → marca "Template repository"*. Desde entonces aparece el botón verde **"Use this template"**, que crea un repositorio nuevo con todo esto ya copiado y sin arrastrar el historial.

**Si trabajas en local:** copia la carpeta, bórrale la subcarpeta oculta `.git` y ejecuta `git init -b main` dentro de la copia.

Luego:
1. Renombra la carpeta con el nombre del proyecto (`analisis-retencion-clientes-2025`).
2. Reemplaza los `✏️` y los textos entre `[corchetes]` a medida que avanzas. Un `✏️` significa "esto lo decides tú".
3. Haz el primer commit: `Inicia proyecto desde la plantilla`.
4. Borra este archivo cuando ya no lo necesites.

## ¿Cuánta documentación necesito?

No todos los proyectos necesitan todo. Elige según el tamaño:

| Tipo de proyecto | Mínimo recomendado |
|---|---|
| **Ejercicio rápido** (horas) | `README.md` + `00_brief.md` (versión corta) + `03_log_decisiones.md` |
| **Proyecto de portafolio o informe** (días) | Lo anterior + `01_diccionario_datos.md` + `02_calidad_datos.md` + `05_hallazgos.md` |
| **Análisis que otros usarán o mantendrán** (semanas) | Todo, incluidas `04_definiciones_metricas.md` y `07_checklist_cierre.md` |

Regla práctica: **el log de decisiones y el README nunca se omiten.** Son lo que más ayuda y menos cuesta.

## En qué orden se completa

| Fase | Qué haces | Documento que completas |
|---|---|---|
| 1. Entender | Aclaras la pregunta con quien decide | `00_brief.md` |
| 2. Conocer los datos | Perfilas la tabla (puedes usar `scripts/perfilar_datos.py`) | `01_diccionario_datos.md`, `02_calidad_datos.md` |
| 3. Preparar | Limpias y transformas | `03_log_decisiones.md` (una entrada por decisión) |
| 4. Medir | Defines y calculas las métricas | `04_definiciones_metricas.md` |
| 5. Interpretar | Sacas conclusiones con su incertidumbre | `05_hallazgos.md` |
| 6. Cerrar | Revisas, pruebas en frío y entregas | `07_checklist_cierre.md`, `CHANGELOG.md` |

Los documentos **no se escriben en secuencia estricta**: el brief se vuelve a tocar cuando aprendes algo, y el log crece durante todo el proyecto.

## Ritual de cierre de sesión (5 minutos)

1. Anoto la decisión del día en `03_log_decisiones.md`.
2. Actualizo lo que cambió (diccionario, métricas, tabla de estado del README).
3. `git add` + `git commit` con un mensaje que explique el cambio.
4. `git push`.

## Qué pasa si el proyecto cambia de rumbo

No borres: **anota**. Si la pregunta cambia, deja la versión anterior tachada en el brief y escribe en el log por qué cambió. El historial de decisiones es parte del resultado.

## Convenciones de esta plantilla

- ✏️ = lo completas tú.
- 🟡 Propuesta · 🟢 Aceptada · 🔴 Descartada = estados de las decisiones.
- `D-001`, `Q-01`, `M-01`, `H-1` = IDs de decisiones, problemas de calidad, métricas y hallazgos. Se citan entre documentos y en el código para poder rastrear.
- Los **ejemplos** están marcados como tales. Bórralos o reemplázalos por los tuyos.
