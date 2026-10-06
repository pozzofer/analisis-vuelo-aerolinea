# Diccionario de datos

> Un diccionario por **tabla o archivo**. Si tienes varias tablas, duplica las secciones 1 a 4 para cada una (y agrega la sección 5 con las relaciones).
> Cómo obtener los valores medidos: ejecuta `python scripts/perfilar_datos.py data/raw/<archivo>` y copia lo útil. Lo que dice cada columna *significa* lo confirmas con quien generó el dato, no con el dato.

## 1. Ficha de la tabla

| Campo | Valor |
|---|---|
| **Nombre / archivo** | ✏️ *(ej. `data/raw/ventas.csv`)* |
| **Descripción** | ✏️ *(qué representa la tabla en el negocio)* |
| **Granularidad** | ✏️ *(1 fila = 1 ...)* |
| **Clave primaria** | ✏️ *(columna(s) que identifican una fila única)* |
| **Filas / columnas** | ✏️ / ✏️ |
| **Período cubierto** | ✏️ |
| **Fuente y sistema de origen** | ✏️ |
| **Fecha de extracción** | AAAA-MM-DD |
| **Frecuencia de actualización** | ✏️ *(diaria, mensual, estática…)* |
| **Responsable / contacto** | ✏️ |
| **Sensibilidad** | ☐ Pública ☐ Interna ☐ Contiene datos personales ☐ Confidencial |
| **Formato técnico** | ✏️ *(separador, codificación como UTF-8/UTF-8 con BOM, formato de fecha, separador decimal)* |

## 2. Columnas

| # | Columna | Tipo original | Tipo objetivo | Descripción (en lenguaje de negocio) | Valores / rango observado | Nulos (n / %) | Problemas conocidos |
|---|---|---|---|---|---|---|---|
| 1 | ✏️ | | | | | | |

**Cómo completar cada campo:**
- **Descripción:** qué significa para el negocio, no el nombre repetido. Mal: "importe: el importe". Bien: "importe neto facturado, sin IVA, en moneda local".
- **Valores / rango:** para categorías, la lista; para números, mínimo y máximo; para fechas, el período.
- **Unidad y moneda:** siempre explícitas (pesos, USD, minutos, kg).
- **Problemas conocidos:** referencia al ID de calidad (`Q-0X`) y a la decisión (`D-0XX`).
- **Columnas que cambiaron de significado:** anótalo con la fecha ("antes de marzo 2024 incluía IVA").

## 3. Reglas de coherencia

*Cosas que **deberían** cumplirse siempre. Son las mejores pruebas de calidad: si fallan, hay un error o un caso especial que hay que entender.*

| Regla | ¿Se cumple? | Excepciones |
|---|---|---|
| ✏️ *(ej. "cantidad × precio unitario = importe")* | ☐ | |
| ✏️ *(ej. "fecha_fin ≥ fecha_inicio")* | ☐ | |
| ✏️ *(ej. "si estado = cancelado → importe = 0")* | ☐ | |

## 4. Códigos y categorías

*Si una columna usa códigos (1, 2, 3 / A, B, C), pon aquí su significado.*

| Columna | Código | Significado |
|---|---|---|
| ✏️ | | |

## 5. Relaciones entre tablas (si hay más de una)

| Tabla A | Columna A | Tabla B | Columna B | Tipo (1:1, 1:N, N:M) | ¿Hay filas huérfanas? |
|---|---|---|---|---|---|
| ✏️ | | | | | |

## 6. Procedencia (muy importante en datos simulados o de terceros)

| Pregunta | Respuesta |
|---|---|
| ¿Cómo se generó o recopiló el dato? | ✏️ |
| ¿Quién lo entregó y cuándo? | ✏️ |
| ¿Hay filtros previos que no controlo? | ✏️ *(ej. "ya excluye devoluciones")* |
| ¿Se introdujeron errores a propósito (para practicar)? | ✏️ |
| ¿Puedo compartir este dato? Licencia / permisos | ✏️ |
