# Hallazgos y conclusiones

> Se completa al final, pero **se alimenta durante todo el análisis**: anota los hallazgos cuando aparecen, con su cifra, y reordénalos después.
> Regla: **un hallazgo = afirmación + cifra + dónde verlo + qué se recomienda.** Si no tiene cifra, no es un hallazgo: es una impresión.

⚠️ *Si los datos son simulados, parciales o de práctica, repítelo aquí: los hallazgos describen esos datos, no la realidad.*

## 1. Pregunta que se respondía

*(Copia la pregunta principal de `00_brief.md`.)* ✏️

## 2. Respuesta en una frase

*Si quien decide solo leyera esto, ¿qué debería saber? Escribe primero la respuesta y después la justificación (no al revés).* ✏️

## 3. Hallazgos

| # | Hallazgo (afirmación concreta) | Cifra | Dónde verlo | Confianza | Recomendación |
|---|---|---|---|---|---|
| H-1 | ✏️ | | *(página, gráfico o archivo)* | Alta / Media / Baja | |

**Cómo asignar la confianza:**
- **Alta:** muestra grande, datos limpios, resultado estable ante distintas decisiones de limpieza (ver sección 4).
- **Media:** el patrón es claro pero hay nulos, pocos casos o una decisión discutible que lo afecta.
- **Baja:** pocos datos, mucha dependencia de supuestos o datos con problemas serios. Se reporta como pista, no como conclusión.

**Cómo redactar un buen hallazgo:**

| Débil | Fuerte |
|---|---|
| "Las ventas bajaron" | "Las ventas del T3 cayeron 12 % vs. T2, concentradas en la región Norte (−31 %); las otras tres regiones variaron menos de ±3 %." |
| "Hay clientes que no vuelven" | "El 42 % de los clientes captados por el canal X no recompra en 90 días, frente al 18 % del canal Y." |
| "El proceso es lento" | "La mediana de resolución es 3 días, pero el 10 % de los casos tarda más de 15 días." |

## 4. Análisis de sensibilidad

*Muestra cuánto dependen las conclusiones de tus decisiones de limpieza. Es lo que más confianza genera.*

| Métrica | Sin tratar | Con la limpieza completa | Diferencia | Decisión responsable |
|---|---|---|---|---|
| ✏️ | | | | D-0XX |

*¿Alguna conclusión cambia de signo o de orden según la decisión? Si es así, díselo al lector.* ✏️

## 5. Hechos, interpretaciones y recomendaciones

Mantenlos separados para que el lector sepa qué es dato y qué es opinión tuya:

| Tipo | Ejemplo |
|---|---|
| **Hecho** (lo dice el dato) | "El margen es negativo en 10 de 36 sucursales." |
| **Interpretación** (tu lectura) | "Probablemente por estacionalidad: se concentra en meses de baja demanda." |
| **Recomendación** (qué hacer) | "Revisar esas sucursales antes de la próxima planificación." |

## 6. Limitaciones

- Qué no pude medir por falta de datos: ✏️
- Supuestos que sostienen las conclusiones: ✏️
- Decisiones de limpieza que podrían cambiar el resultado (ver sensibilidad): ✏️
- Correlación vs. causalidad: ✏️ *(¿alguna conclusión sugiere causa sin haberla probado?)*
- Sesgos posibles en los datos (quién queda fuera, cómo se recogieron): ✏️

## 7. Próximos pasos

- Datos que pediría: ✏️
- Análisis que haría con más tiempo: ✏️
- Cómo se mantendría actualizado: ✏️

## 8. Uso de IA en este proyecto

*Cada vez más organizaciones piden transparencia. Anota brevemente:*

- Qué partes se apoyaron en asistentes de IA (código, borradores de documentación, ideas): ✏️
- Cómo validaste los resultados (cifras de control, revisión manual, pruebas): ✏️
- Qué datos NO se compartieron con herramientas externas por ser sensibles: ✏️
