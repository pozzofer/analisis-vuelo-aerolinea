# Calidad de datos: diagnóstico y cifras de control

**Dato:** ✏️ · **Perfilado realizado:** AAAA-MM-DD · **Sobre el archivo original, sin modificar**

Este documento cumple dos funciones:
1. **Diagnóstico:** qué problemas tiene el dato, cuántas filas afecta cada uno y qué se decidió.
2. **Cifras de control:** números de referencia para comprobar que tu limpieza quedó bien. Si tus conteos finales no coinciden, algo falló en un paso.

> **Atajo:** `python scripts/perfilar_datos.py data/raw/<archivo> -o docs/perfil_automatico.md` genera un borrador con la mayoría de los chequeos de la sección 1. Úsalo como punto de partida y confírmalo con tus ojos: encuentra patrones, no entiende el negocio.
> **Lo que NO detecta:** abreviaturas o nombres alternativos de una misma cosa (`Bs As` vs `Buenos Aires`), errores de tipeo, reglas de negocio (¿el total cuadra con las partes?) ni valores centinela (`9999`, `-1`). Para eso revisa a mano la lista de valores únicos de cada categoría.

## 1. Los 6 chequeos estándar

Recorre estas seis dimensiones en **todas** las tablas. Cada una responde una pregunta distinta.

| Dimensión | Pregunta | Cómo revisarlo (ejemplos) | Señales típicas |
|---|---|---|---|
| **Completitud** | ¿Faltan datos? | Contar nulos y vacíos por columna. SQL: `COUNT(*) - COUNT(col)`. Python: `df.isna().sum()` | Nulos concentrados en un período o categoría; "N/A", "-", "0", "9999" usados como nulo |
| **Unicidad** | ¿Hay duplicados? | SQL: `GROUP BY ... HAVING COUNT(*) > 1`. Python: `df.duplicated()` | Filas idénticas; mismo ID con datos distintos (más grave) |
| **Validez** | ¿Los valores tienen el formato/tipo/rango correcto? | Tipos, mínimos y máximos, patrones (regex), listas de valores permitidos | Fechas en texto con formatos mezclados; negativos donde no corresponden; categorías fuera de lista |
| **Consistencia** | ¿El dato concuerda consigo mismo y con otras columnas/tablas? | Reglas de coherencia del diccionario; claves foráneas | Totales que no cuadran; "Córdoba", "Cordoba" y "CORDOBA" como valores distintos |
| **Razonabilidad** | ¿Los valores son creíbles? | Outliers (regla del rango intercuartil), comparar con el orden de magnitud esperado | Un valor 10× mayor que el resto; fechas futuras; edades de 200 años |
| **Vigencia** | ¿Está actualizado y cubre lo que creo? | Fecha mínima y máxima; huecos por mes; comparar con la fuente | Faltan meses; el último registro es de hace un año; cambio de definición a mitad de serie |

## 2. Problemas detectados

*Una fila por problema. Numéralos `Q-01`, `Q-02`… y enlázalos con la decisión que los resuelve.*

| ID | Problema | Columnas | Filas afectadas (n / %) | Gravedad | Decisión |
|---|---|---|---|---|---|
| Q-01 | ✏️ | | | Alta / Media / Baja | D-001 |

**Criterio de gravedad:**
- **Alta:** cambia el resultado de las métricas principales o impide calcular algo.
- **Media:** afecta casos acotados; hay que decidir y documentar.
- **Baja:** cosmético o de formato; se corrige sin debate.

## 3. Lo que está bien

*Anota también lo que verificaste y salió limpio. Evita que el siguiente lector repita el chequeo.*

- ✏️ *(ej. "`id_cliente`: sin duplicados ni nulos")*
- ✏️ *(ej. "fechas entre 2024-01-01 y 2025-12-31 sin huecos")*

## 4. Cifras de control

> Se calculan **sobre el dato original** y después de **cada etapa** de limpieza. Sirven para validar tu proceso y para que otra persona confirme que reprodujo lo mismo.

### 4.1 Conteo de filas por etapa

| Etapa | Filas esperadas | Filas obtenidas | ¿Cuadra? |
|---|---|---|---|
| Archivo original | ✏️ | | |
| Tras eliminar duplicados | ✏️ | | |
| Tras aplicar filtros de alcance | ✏️ | | |
| Tabla final del análisis | ✏️ | | |

> Cada fila que sale entre etapas debe poder explicarse: *"2.480 − 30 duplicados = 2.450"*. Si no suma, hay filas perdidas sin explicación.

### 4.2 Totales de referencia

*Sumas, conteos o promedios simples que no dependen de interpretaciones.*

| Indicador | Valor sobre el dato original | Valor tras la limpieza | Diferencia | Decisión responsable |
|---|---|---|---|---|
| ✏️ *(ej. total de ventas)* | | | | D-0XX |

### 4.3 Nulos por columna clave

| Columna | Nulos antes | Nulos después | Tratamiento |
|---|---|---|---|
| ✏️ | | | *(se mantienen / se imputan / se excluyen: ver D-0XX)* |

## 5. Cómo repetir este diagnóstico

*Explica los pasos para que otra persona obtenga los mismos números.*

- **Herramienta y versión:** ✏️
- **Pasos / consulta / script:** ✏️ *(ej. `analisis/sql/00_perfilado.sql` o "Power Query → Vista → Perfil de columna, basado en el conjunto completo")*
- ⚠️ En Power Query y otras herramientas, el perfil por defecto mira solo las primeras 1.000 filas. Cámbialo a "conjunto de datos completo".
