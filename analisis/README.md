# Carpeta `analisis/`

Aquí vive **tu trabajo**: notebooks, consultas, proyecto de BI, hojas de cálculo. La plantilla no impone herramienta; usa la que corresponda y borra lo que no uses.

## Organización sugerida

```
analisis/
├── notebooks/     # Jupyter / Quarto / marimo     → 01_exploracion, 02_limpieza, 03_analisis
├── sql/           # consultas numeradas           → 01_extraccion.sql, 02_limpieza.sql
├── bi/            # Power BI (.pbip), Tableau, Looker Studio, etc.
└── excel/         # libros de trabajo (si no hay alternativa, trátalos como fuente de código: nombra y documenta)
```

## Reglas de oro

1. **Numera los archivos** en el orden en que se ejecutan (`01_`, `02_`…). Quien llegue después sabrá por dónde empezar.
2. **Todo corre de punta a punta** con un solo comando o "Run all". Si hay pasos manuales, se escriben en el README.
3. **Nunca se edita `data/raw/`.** Toda transformación queda en código o en pasos visibles (Power Query, SQL).
4. **Cada decisión que cambia un número** tiene su entrada en `docs/03_log_decisiones.md`, con el ID (`D-0XX`) citado en un comentario o nombre de paso.
5. **Comenta el porqué**, no el qué: `# Excluyo pedidos de prueba (D-004)` y no `# filtro filas`.

## Ejemplo de comentario útil

```python
# D-004: excluyo pedidos internos de prueba (monto = 0 y cliente = 'TEST'). Impacto: -0,8 % de filas.
df = df[~((df["monto"] == 0) & (df["cliente"] == "TEST"))]
```
