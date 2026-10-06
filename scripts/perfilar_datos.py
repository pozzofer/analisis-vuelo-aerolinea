#!/usr/bin/env python3
"""
Perfilado rápido de una tabla -> borrador en Markdown para docs/02_calidad_datos.md

Uso:
    python scripts/perfilar_datos.py data/raw/archivo.csv
    python scripts/perfilar_datos.py data/raw/archivo.xlsx -o docs/perfil_automatico.md
    python scripts/perfilar_datos.py data/raw/archivo.csv --sep ";" --encoding latin-1

Qué revisa (los 6 chequeos de docs/02_calidad_datos.md):
    - Completitud : nulos y vacíos por columna
    - Unicidad    : filas duplicadas, posibles claves, IDs repetidos
    - Validez     : formatos de fecha mezclados, números guardados como texto, espacios sobrantes
    - Consistencia: variantes de escritura de una misma categoría (Córdoba / Cordoba / CORDOBA)
    - Razonabilidad: negativos, ceros y valores extremos (regla 3 x rango intercuartil)
    - Vigencia    : rango de fechas

IMPORTANTE: es un BORRADOR. Detecta patrones, no entiende tu negocio. Revisa cada hallazgo.
Requisitos: pandas (openpyxl para .xlsx, pyarrow para .parquet).
"""
import argparse
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

import pandas as pd

MAX_CATEGORIAS = 200  # revisar variantes de escritura solo en columnas con pocos valores distintos

PATRONES_FECHA = {
    "aaaa-mm-dd": r"^\d{4}-\d{2}-\d{2}$",
    "aaaa/mm/dd": r"^\d{4}/\d{2}/\d{2}$",
    "NN/NN/aaaa (dd/mm o mm/dd)": r"^\d{1,2}/\d{1,2}/\d{4}$",
    "NN-NN-aaaa (dd-mm o mm-dd)": r"^\d{1,2}-\d{1,2}-\d{4}$",
    "NN.NN.aaaa": r"^\d{1,2}\.\d{1,2}\.\d{4}$",
    "aaaa-mm-dd hh:mm": r"^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}",
}


# ───────────────────────── utilidades ─────────────────────────
def num(x, decimales=2):
    """Formato numérico con separadores en español (1.234,56)."""
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return "—"
    if float(x).is_integer():
        s = f"{x:,.0f}"
    else:
        s = f"{x:,.{decimales}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def pct(parte, total):
    return f"{(parte / total * 100):.1f} %".replace(".", ",") if total else "—"


def normalizar(texto):
    """Minúsculas, sin tildes y sin espacios repetidos: para detectar variantes de una misma categoría."""
    t = unicodedata.normalize("NFKD", str(texto))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", t).strip().lower()


def tabla_md(cabeceras, filas):
    out = ["| " + " | ".join(cabeceras) + " |", "|" + "|".join("---" for _ in cabeceras) + "|"]
    for f in filas:
        out.append("| " + " | ".join(str(x).replace("|", "\\|") for x in f) + " |")
    return "\n".join(out)


def leer(ruta, sep, encoding):
    ext = ruta.suffix.lower()
    if ext in (".csv", ".txt", ".tsv"):
        sep = sep or ("\t" if ext == ".tsv" else ",")
        return pd.read_csv(ruta, sep=sep, encoding=encoding)
    if ext in (".xlsx", ".xlsm", ".xls"):
        return pd.read_excel(ruta)
    if ext == ".parquet":
        return pd.read_parquet(ruta)
    sys.exit(f"Formato no soportado: {ext}. Usa CSV, Excel o Parquet.")


def ejemplos(serie, n=3):
    vals = serie.dropna().astype(str).unique()[:n]
    return ", ".join(f"`{v[:25]}`" for v in vals) or "—"


# ───────────────────────── chequeos ─────────────────────────
def detectar_fechas(serie):
    """Si la columna de texto parece fechas, devuelve conteo por formato y advertencias."""
    s = serie.dropna().astype(str).str.strip()
    s = s[s != ""]
    if s.empty:
        return None
    conteos = {nombre: int(s.str.match(p).sum()) for nombre, p in PATRONES_FECHA.items()}
    conteos = {k: v for k, v in conteos.items() if v > 0}
    if sum(conteos.values()) < 0.8 * len(s):
        return None
    aviso = None
    if "NN/NN/aaaa (dd/mm o mm/dd)" in conteos:
        partes = s[s.str.match(PATRONES_FECHA["NN/NN/aaaa (dd/mm o mm/dd)"])].str.split("/", expand=True).astype(int)
        max1, max2 = partes[0].max(), partes[1].max()
        if max1 > 12 and max2 <= 12:
            aviso = "el primer número llega a más de 12: es **día/mes/año**"
        elif max2 > 12 and max1 <= 12:
            aviso = "el segundo número llega a más de 12: es **mes/día/año**"
        else:
            aviso = "⚠️ **ambiguo** (no se puede saber si es día/mes o mes/día solo con los valores); confírmalo con la fuente"
    return conteos, aviso


def variantes(serie):
    """Grupos de valores distintos que serían iguales al normalizar (mayúsculas, tildes, espacios)."""
    valores = serie.dropna().astype(str).unique()
    if len(valores) > MAX_CATEGORIAS:
        return []
    grupos = {}
    for v in valores:
        grupos.setdefault(normalizar(v), []).append(v)
    conteo = serie.astype(str).value_counts()
    res = []
    for _, lista in grupos.items():
        if len(lista) > 1:
            res.append((lista, int(sum(conteo.get(v, 0) for v in lista))))
    return res


def perfilar(df, nombre):
    n = len(df)
    L = []
    L.append(f"# Perfil automático: `{nombre}`")
    L.append(f"\n_Generado el {date.today().isoformat()} con `scripts/perfilar_datos.py`. "
             "Es un **borrador**: revisa y completa a mano antes de pasarlo a `02_calidad_datos.md`._\n")

    # ── Resumen
    dup = int(df.duplicated().sum())
    L.append("## 1. Resumen\n")
    L.append(f"- Filas: **{num(n)}** · Columnas: **{df.shape[1]}**")
    L.append(f"- Filas duplicadas exactas (todas las columnas iguales): **{num(dup)}**"
             + (f" → tras eliminarlas quedarían **{num(n - dup)}** filas" if dup else ""))
    L.append(f"- Filas completamente vacías: **{num(int(df.isna().all(axis=1).sum()))}**\n")

    # ── Columnas
    L.append("## 2. Columnas (completitud y tipo)\n")
    filas = []
    for c in df.columns:
        s = df[c]
        vacios = 0
        if s.dtype == object or str(s.dtype) in ("str", "string"):
            vacios = int((s.dropna().astype(str).str.strip() == "").sum())
        nulos = int(s.isna().sum()) + vacios
        filas.append([f"`{c}`", str(s.dtype), num(nulos), pct(nulos, n), num(s.nunique(dropna=True)), ejemplos(s)])
    L.append(tabla_md(["Columna", "Tipo leído", "Nulos/vacíos", "% nulos", "Valores únicos", "Ejemplos"], filas))

    # ── Unicidad
    L.append("\n## 3. Unicidad: posibles claves e IDs repetidos\n")
    posibles = [c for c in df.columns if df[c].notna().all() and df[c].is_unique and n > 1]
    ids = [c for c in df.columns if re.search(r"(^id|_id$|^id_|codigo|código|\bid\b)", str(c), re.I)]
    L.append("- Columnas sin nulos y con valores todos distintos (candidatas a clave primaria): "
             + (", ".join(f"`{c}`" for c in posibles) if posibles else "ninguna"))
    for c in ids:
        rep = int(df[c].dropna().duplicated().sum())
        if rep:
            mismo = df.drop_duplicates()[c].dropna().duplicated().sum()
            L.append(f"- `{c}` tiene **{num(rep)}** valor(es) repetido(s)"
                     + (" y **siguen repetidos** tras quitar filas idénticas (mismo ID con datos distintos: más grave)"
                        if mismo else " y todos corresponden a filas idénticas (duplicados exactos)"))

    # ── Texto: espacios, números como texto, fechas, variantes
    texto = [c for c in df.columns if df[c].dtype == object or str(df[c].dtype) in ("str", "string")]
    L.append("\n## 4. Columnas de texto (validez y consistencia)\n")
    hallazgos = 0
    for c in texto:
        s = df[c].dropna().astype(str)
        if s.empty:
            continue
        # espacios sobrantes
        sobrantes = int((s != s.str.strip()).sum())
        if sobrantes:
            hallazgos += 1
            L.append(f"- `{c}`: **{num(sobrantes)}** valores con espacios al inicio o al final.")
        # números guardados como texto
        conv = pd.to_numeric(s.str.replace(",", ".", regex=False), errors="coerce")
        if conv.notna().mean() >= 0.9 and conv.notna().any():
            hallazgos += 1
            L.append(f"- `{c}`: parece **numérica guardada como texto** ({pct(int(conv.notna().sum()), len(s))} se puede convertir).")
            continue
        # fechas
        f = detectar_fechas(df[c])
        if f:
            conteos, aviso = f
            hallazgos += 1
            if len(conteos) > 1:
                detalle = "; ".join(f"{k}: {num(v)}" for k, v in conteos.items())
                L.append(f"- `{c}`: **fechas en {len(conteos)} formatos mezclados** → {detalle}.")
            else:
                k = next(iter(conteos))
                L.append(f"- `{c}`: fechas guardadas como texto, formato único `{k}`.")
            if aviso:
                L.append(f"  - Lectura de `NN/NN/aaaa`: {aviso}.")
            continue
        # variantes de escritura
        v = variantes(df[c])
        if v:
            hallazgos += 1
            L.append(f"- `{c}`: **variantes de escritura** de lo que parece el mismo valor:")
            for lista, total in v[:8]:
                L.append(f"  - {' / '.join(f'`{x}`' for x in lista)} ({num(total)} filas)")
            if len(v) > 8:
                L.append(f"  - … y {len(v) - 8} grupos más.")
    if not hallazgos:
        L.append("Sin hallazgos automáticos en columnas de texto.")

    # ── Numéricas
    numericas = df.select_dtypes(include="number").columns
    L.append("\n## 5. Columnas numéricas (razonabilidad)\n")
    if len(numericas):
        filas = []
        usa_alternativa = []
        for c in numericas:
            s = df[c].dropna()
            if s.empty:
                continue
            base = s
            q1, q3 = base.quantile(0.25), base.quantile(0.75)
            if q3 - q1 == 0:
                # Más de la mitad de los valores son iguales (ej. muchos ceros): el rango intercuartil
                # sería 0 y todo parecería extremo. Se calcula sobre los valores distintos de la moda.
                base = s[s != s.mode().iloc[0]]
                if len(base) >= 4:
                    q1, q3 = base.quantile(0.25), base.quantile(0.75)
                    usa_alternativa.append(c)
            iqr = q3 - q1
            extremos = int(((s > q3 + 3 * iqr) | (s < q1 - 3 * iqr)).sum()) if iqr > 0 else 0
            marca = "*" if c in usa_alternativa else ""
            filas.append([f"`{c}`", num(s.min()), num(s.median()), num(s.mean()), num(s.max()),
                          num(int((s < 0).sum())), num(int((s == 0).sum())), num(extremos) + marca])
        L.append(tabla_md(["Columna", "Mín", "Mediana", "Media", "Máx", "Negativos", "Ceros", "Extremos (3×IQR)"], filas))
        L.append("\n_«Extremos» no significa error: revisa si son casos reales (ver `03_log_decisiones.md`). "
                 "Una gran diferencia entre media y mediana indica distribución con cola larga._")
        if usa_alternativa:
            L.append("\n_(*) Más de la mitad de los valores de "
                     + ", ".join(f"`{c}`" for c in usa_alternativa)
                     + " son iguales; el límite de extremos se calculó solo sobre los valores distintos del más frecuente._")
    else:
        L.append("No hay columnas numéricas.")

    # ── Fechas ya tipadas
    fechas = df.select_dtypes(include=["datetime", "datetimetz"]).columns
    if len(fechas):
        L.append("\n## 6. Columnas de fecha (vigencia)\n")
        filas = [[f"`{c}`", str(df[c].min())[:10], str(df[c].max())[:10], num(df[c].dt.to_period("M").nunique())]
                 for c in fechas]
        L.append(tabla_md(["Columna", "Mínima", "Máxima", "Meses con datos"], filas))

    L.append("\n## Siguientes pasos\n")
    L.append("1. Pasa cada problema real a la tabla de `docs/02_calidad_datos.md` con su ID `Q-0X`.")
    L.append("2. Por cada uno, decide qué hacer y anótalo en `docs/03_log_decisiones.md`.")
    L.append("3. Guarda los conteos de este perfil como **cifras de control** (sección 4 de `02_calidad_datos.md`).")
    L.append("4. Lo que este script no ve: reglas de negocio (¿el total cuadra con las partes?), "
             "coherencia entre columnas y sentido común. Eso lo revisas tú.")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Genera un borrador de perfil de calidad de datos en Markdown.")
    ap.add_argument("archivo", type=Path, help="CSV, Excel o Parquet")
    ap.add_argument("-o", "--salida", type=Path, help="archivo .md de salida (si se omite, imprime en pantalla)")
    ap.add_argument("--sep", default=None, help="separador del CSV (por defecto ',')")
    ap.add_argument("--encoding", default="utf-8-sig", help="codificación del CSV (por defecto utf-8-sig, que maneja el BOM)")
    args = ap.parse_args()

    if not args.archivo.exists():
        sys.exit(f"No encuentro el archivo: {args.archivo}")
    df = leer(args.archivo, args.sep, args.encoding)
    informe = perfilar(df, args.archivo.name)

    if args.salida:
        args.salida.parent.mkdir(parents=True, exist_ok=True)
        args.salida.write_text(informe, encoding="utf-8")
        print(f"Perfil guardado en {args.salida}")
    else:
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
        print(informe)


if __name__ == "__main__":
    main()
