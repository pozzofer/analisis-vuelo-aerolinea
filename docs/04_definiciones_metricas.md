# Definiciones de métricas

> **El problema que resuelve:** dos personas calculan "tasa de conversión" y obtienen números distintos, y ambas tienen razón porque definieron distinto el denominador. Este archivo es el **contrato** de qué significa cada métrica. Se escribe **antes** de implementarla y se mantiene idéntico en todas las herramientas (SQL, DAX, Python, Excel).

## Índice

| ID | Métrica | Dueño | Estado |
|---|---|---|---|
| M-01 | ✏️ | | 🟡 / 🟢 |

---

## Ficha de métrica (una por métrica)

### M-01 · [Nombre claro, tal como aparecerá en el informe]

| Campo | Contenido |
|---|---|
| **Pregunta que responde** | ✏️ *(en una frase de negocio)* |
| **Definición** | ✏️ *(en lenguaje simple)* |
| **Fórmula** | ✏️ *(numerador / denominador)* |
| **Numerador** | ✏️ *(qué se cuenta o suma, con sus filtros)* |
| **Denominador** | ✏️ *(sobre qué base; ¿incluye o excluye casos especiales?)* |
| **Unidad y formato** | ✏️ *(%, pesos, minutos; cuántos decimales)* |
| **Granularidad / nivel de agregación** | ✏️ *(por día, cliente, producto, región…)* |
| **Ventana de tiempo** | ✏️ *(últimos 30 días, mes calendario, año móvil)* |
| **Tratamiento de nulos** | ✏️ *(se ignoran, se tratan como 0, se excluye la fila entera)* |
| **Casos especiales** | ✏️ *(cancelados, devoluciones, valores atípicos, duplicados)* |
| **Fuente** | ✏️ *(tabla y columnas)* |
| **Decisiones relacionadas** | D-0XX |
| **Cómo validarla** | ✏️ *(valor esperado contra un número conocido o una cifra de control)* |
| **Limitaciones** | ✏️ *(qué NO mide)* |

---

## Ejemplo completo (ilustrativo, bórralo)

### M-02 · Tasa de conversión

| Campo | Contenido |
|---|---|
| **Pregunta que responde** | De las personas que visitan el sitio, ¿cuántas compran? |
| **Definición** | Porcentaje de sesiones que terminan con al menos una compra. |
| **Fórmula** | Sesiones con compra / Sesiones totales |
| **Numerador** | Sesiones con ≥ 1 pedido pagado (excluye pedidos cancelados antes del pago) |
| **Denominador** | Sesiones totales, excluyendo tráfico de bots (D-006) |
| **Unidad y formato** | Porcentaje, 1 decimal |
| **Granularidad** | Por día y por canal de origen |
| **Ventana de tiempo** | Mes calendario |
| **Tratamiento de nulos** | Sesiones sin canal se agrupan como "Directo / desconocido" |
| **Casos especiales** | Una persona con 2 compras en la misma sesión cuenta 1 vez |
| **Fuente** | `sesiones.id_sesion`, `pedidos.id_sesion`, `pedidos.estado` |
| **Decisiones relacionadas** | D-006 |
| **Cómo validarla** | Mayo 2026 debe dar 3,4 % (cifra del reporte oficial del equipo web) |
| **Limitaciones** | No distingue entre una compra pequeña y una grande; no sigue al usuario entre dispositivos. |

**La misma métrica implementada en distintas herramientas** (para que veas cómo se traduce el contrato):

```sql
-- SQL: tasa de conversión mensual (M-02). Excluye bots (D-006).
SELECT
  DATE_TRUNC('month', s.fecha)                               AS mes,
  COUNT(DISTINCT p.id_sesion) * 1.0 / COUNT(DISTINCT s.id_sesion) AS tasa_conversion
FROM sesiones s
LEFT JOIN pedidos p
       ON p.id_sesion = s.id_sesion AND p.estado = 'pagado'
WHERE s.es_bot = FALSE
GROUP BY 1;
```

```dax
// DAX (Power BI): misma regla. DIVIDE evita errores si el denominador es 0.
Tasa de Conversión =
DIVIDE (
    CALCULATE ( DISTINCTCOUNT ( Pedidos[id_sesion] ), Pedidos[estado] = "pagado" ),
    CALCULATE ( DISTINCTCOUNT ( Sesiones[id_sesion] ), Sesiones[es_bot] = FALSE )
)
```

```python
# Python (pandas): misma regla.
ses = sesiones[~sesiones["es_bot"]]
con_compra = ses["id_sesion"].isin(pedidos.loc[pedidos["estado"] == "pagado", "id_sesion"])
tasa_conversion = con_compra.mean()
```

---

## Errores clásicos al definir métricas

- **Denominador ambiguo:** "tasa de cancelación" ¿sobre pedidos realizados o sobre pedidos confirmados? ¿"Retención" sobre clientes activos o sobre todos los alta?
- **Promedio de promedios:** promediar porcentajes de grupos de distinto tamaño da un resultado erróneo. Calcula el cociente de las sumas.
- **Promedio que oculta:** un promedio sobre todos los casos (incluidos los 0) diluye el problema. Reporta también la mediana o el promedio condicionado, y di cuál es cuál.
- **Nulos tratados como 0:** en un cociente sesga el resultado. Decide explícitamente (D-0XX).
- **Ventanas que se solapan o dejan huecos:** "30 días" ¿incluye el día de hoy?
- **Misma métrica, distinto nombre** (o al revés): una palabra, una definición.

## Validación cruzada (completar al implementar)

| Métrica | Valor esperado (fuente) | Valor obtenido | ¿Cuadra? | Observación |
|---|---|---|---|---|
| M-01 | ✏️ | | | |
