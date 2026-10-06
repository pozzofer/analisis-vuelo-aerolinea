# Log de decisiones

Registro de cada decisión que afecta los resultados. **Regla de oro: si cambia un número del informe, tiene que tener una entrada acá.**

Es lo que más separa a un analista junior de uno senior: el código muestra *qué* hiciste; este archivo explica *por qué* y *cuánto importó*.

**Estados:** 🟡 Propuesta (falta confirmar) · 🟢 Aceptada (aplicada) · 🔴 Descartada o reemplazada

## Índice

| ID | Decisión | Estado | Impacto en una línea |
|---|---|---|---|
| D-001 | ✏️ | 🟡 | |

---

## Qué tipo de cosas se registran

Si dudas si algo merece una entrada, revisa esta lista. Casi seguro que sí si:

- **Filas:** eliminar duplicados, excluir registros (pruebas, cancelados, fuera de período), filtros de alcance.
- **Valores:** tratamiento de nulos, imputaciones, corrección de errores, recorte o mantenimiento de outliers.
- **Formato:** conversión de tipos y fechas, normalización de categorías, unificación de monedas o unidades.
- **Definiciones:** cómo se calcula una métrica, qué entra en el numerador y denominador, ventanas de tiempo.
- **Uniones:** qué tipo de join, qué se hace con los que no emparejan.
- **Muestreo y segmentación:** por qué ese corte, ese umbral, esa categoría "Otros".
- **Método:** modelo estadístico elegido, nivel de confianza, tratamiento de estacionalidad.
- **Cambios de rumbo:** de pregunta, de alcance o de fuente.

**No necesita entrada:** renombrar una columna por claridad, cambiar un color, reordenar un gráfico (sí un commit claro).

---

## D-001 · [Título corto en forma de acción: "Eliminar duplicados exactos"] 🟡

- **Fecha:** AAAA-MM-DD
- **Problema:** *qué situación del dato, con ID de calidad (`Q-0X`) y cuántas filas.*
- **Decisión:** *qué se hace exactamente, de forma que otra persona pueda repetirlo.*
- **Motivo:** *por qué esta opción y no otra. Incluye la evidencia (lo que verificaste).*
- **Alternativas descartadas:** *qué otras opciones consideraste y por qué no.*
- **Impacto esperado:** *qué número cambiará y cuánto (una estimación).*
- **Impacto real:** *filas afectadas y cómo cambió una métrica, de ____ a ____.* ✏️
- **Riesgo / sensibilidad:** *¿qué pasaría con las conclusiones si esta decisión fuera distinta?*
- **Dónde se aplica:** *archivo, consulta, paso o medida donde está implementada.*
- **Confirmada con:** *quién del negocio o del equipo lo validó (si aplica).*

---

## Ejemplo completo (ilustrativo, bórralo)

## D-004 · Excluir pedidos de prueba del análisis de ventas 🟢

- **Fecha:** 2026-03-12
- **Problema:** Q-03. 312 pedidos con monto = 0 y cliente "TEST_INTERNO".
- **Decisión:** Filtrar filas donde `monto = 0` **y** `cliente` empieza con `TEST_`. Se aplica antes de cualquier agregación.
- **Motivo:** El equipo de ventas confirmó (mensaje del 2026-03-10) que son pruebas de integración. Mantenerlos reduciría el ticket promedio.
- **Alternativas descartadas:** Imputar el monto con la mediana (inventa ventas que no existieron). Filtrar solo `monto = 0` (también eliminaría bonificaciones reales, 41 filas).
- **Impacto esperado:** −0,8 % de filas; ticket promedio sube.
- **Impacto real:** 38.920 → 38.608 filas; ticket promedio de $12.410 a $12.508 (+0,8 %).
- **Riesgo / sensibilidad:** Bajo. Las conclusiones por canal no cambian.
- **Dónde se aplica:** `analisis/notebooks/02_limpieza.ipynb`, celda 7.
- **Confirmada con:** Marta (Ventas).

---

## Plantilla en blanco (copia y pega)

```markdown
## D-0XX · Título en forma de acción 🟡
- **Fecha:**
- **Problema:**
- **Decisión:**
- **Motivo:**
- **Alternativas descartadas:**
- **Impacto esperado:**
- **Impacto real:**
- **Riesgo / sensibilidad:**
- **Dónde se aplica:**
- **Confirmada con:**
```

## Consejos de redacción

- **Títulos en forma de acción:** "Normalizar nombres de ciudad", no "Ciudades".
- **Con números:** "−312 filas (−0,8 %)", no "algunas filas".
- **Una decisión por entrada.** Si hay dos, son dos entradas.
- **No reescribas el pasado.** Si cambias de opinión, pon 🔴 en la antigua y crea una nueva que la reemplaza, explicando por qué.
- **Cita el ID** (`D-004`) en el comentario del código y en el mensaje del commit para poder rastrearla.
