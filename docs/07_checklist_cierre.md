# Checklist de cierre

Revisa esto **antes de entregar o publicar**. Marca con `x` lo que esté hecho y anota fecha y quién revisó al final.

## 1. Los números

- [ ] Los conteos de filas por etapa coinciden con las cifras de control (`02_calidad_datos.md`, sección 4).
- [ ] Cada métrica clave se validó contra un valor conocido (`04_definiciones_metricas.md`, sección de validación).
- [ ] Recalculé a mano (o en otra herramienta) al menos 2-3 cifras del informe.
- [ ] Las sumas parciales suman el total; los porcentajes suman 100 % donde corresponde.
- [ ] Revisé unidades, moneda y período en cada título y eje.
- [ ] Las cifras del informe y las de `05_hallazgos.md` son idénticas.

## 2. Las decisiones

- [ ] Todas las decisiones que cambian un número están en `03_log_decisiones.md`.
- [ ] Ninguna decisión está en 🟡: están en 🟢 (aplicadas) o 🔴 (descartadas).
- [ ] Cada decisión tiene su **impacto real** medido, no solo esperado.
- [ ] La sensibilidad (`05_hallazgos.md`, sección 4) muestra que las conclusiones no dependen de una sola decisión frágil, o lo dice claramente.

## 3. Reproducibilidad

- [ ] Todo corre de punta a punta con un solo comando o "Run all", partiendo de `data/raw/`.
- [ ] `data/raw/` no fue modificado (compara con `git diff` o con la suma de verificación).
- [ ] Las dependencias y versiones están anotadas (`requirements.txt`, versión de la herramienta).
- [ ] Los notebooks se guardan ejecutados de arriba abajo, sin celdas fuera de orden ni errores.
- [ ] Alguien que no soy yo pudo seguir el README y obtener los mismos números. *(Si nadie puede, hazlo tú desde una carpeta limpia, clonando el repo.)*

## 4. La documentación

- [ ] `README.md`: pregunta, estado, cómo reproducir, fuente de datos, resultados y limitaciones están completos.
- [ ] `00_brief.md` refleja el alcance real final (no el inicial).
- [ ] `01_diccionario_datos.md` cubre todas las columnas usadas y la procedencia de los datos.
- [ ] Quedaron resueltos o descartados todos los `✏️`, textos `[entre corchetes]` y ejemplos de la plantilla.
- [ ] Se borró `docs/GUIA_USO.md` y lo que no aplica al proyecto.
- [ ] Las limitaciones están escritas con claridad (y si los datos son simulados, se dice).

## 5. Comunicación

- [ ] El informe empieza por la respuesta, no por el método.
- [ ] Los títulos de los gráficos dicen la conclusión ("La región Norte concentra el 68 % de las devoluciones"), no solo el tema.
- [ ] Hechos, interpretaciones y recomendaciones están separados.
- [ ] No se afirma causalidad donde solo hay correlación.
- [ ] Los gráficos son legibles en blanco y negro o por personas con daltonismo (no dependen solo del color) y tienen texto alternativo si se publican.

## 6. Privacidad y seguridad

- [ ] No hay datos personales ni confidenciales en el repositorio (nombres, documentos, correos, teléfonos, direcciones).
- [ ] No hay contraseñas, tokens ni cadenas de conexión (busca: `password`, `token`, `secret`, `key`).
- [ ] Si usé herramientas de IA, no les pasé datos sensibles sin autorización, y lo anoté en `05_hallazgos.md`.
- [ ] Tengo permiso para compartir estos datos y este informe.

## 7. Cierre en Git

- [ ] `git status` está limpio (nada pendiente de commit).
- [ ] El `CHANGELOG.md` tiene la entrada de la versión que entrego.
- [ ] Hice `git tag -a v1.0 -m "..."` y `git push --tags`.
- [ ] Revisé el repositorio **desde el navegador** como si fuera un desconocido: el README se entiende solo.

## 8. Revisión en frío

Deja pasar al menos un día y reabre el proyecto como si lo viera por primera vez:

- [ ] ¿Entiendo qué pregunta responde, en menos de un minuto?
- [ ] ¿Puedo explicar de dónde sale cada número principal?
- [ ] ¿Qué es lo primero que cuestionaría una persona escéptica? ¿Está respondido en el documento?

---

**Revisado por:** ✏️ · **Fecha:** AAAA-MM-DD · **Versión entregada:** v✏️
