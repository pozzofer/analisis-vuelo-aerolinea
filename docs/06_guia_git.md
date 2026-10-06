# Guía de Git para proyectos de análisis

Git guarda el historial de **qué cambió, cuándo y por qué**. Junto con la documentación te permite volver atrás ante un error y demostrar cómo llegaste a cada resultado.

## 1. Configuración inicial (una sola vez por computadora)

```bash
git config --global user.name  "Tu Nombre o usuario"
git config --global user.email "el-correo-de-tu-cuenta-de-github@ejemplo.com"
git --version     # si dice "no se reconoce", instala Git y abre una terminal NUEVA
```

El correo debe ser uno que tengas agregado en GitHub (*Settings → Emails*) para que tus commits aparezcan en tu perfil.

## 2. Iniciar y publicar un proyecto

```bash
cd carpeta-del-proyecto           # la carpeta donde están README.md y docs/
git init -b main
git add .
git commit -m "Inicia proyecto desde la plantilla"
```

Luego crea en GitHub un repositorio **vacío** (sin README, .gitignore ni license) y conéctalo:

```bash
git remote add origin https://github.com/TU-USUARIO/nombre-del-repo.git
git push -u origin main
```

> ⚠️ Los símbolos `< >` en las guías marcan "reemplaza esto" y **no se escriben**. `<tu-usuario>` se convierte en `mi-usuario`, no en `<mi-usuario>`.
> Si te equivocas en la dirección: `git remote set-url origin <dirección correcta>` y compruébalo con `git remote -v`.

## 3. Ciclo de trabajo diario

```bash
git status                          # ¿qué cambió?
git diff                            # ver los cambios línea por línea
git add docs/03_log_decisiones.md   # elegir qué guardar (mejor archivo por archivo)
git commit -m "Aplica D-003: normaliza ciudades con el catálogo oficial (245 filas)"
git push
```

**Un commit = un cambio con sentido.** No mezcles "limpié fechas" con "armé el gráfico de ventas".

## 4. Mensajes de commit

Fórmula: **verbo en presente + qué + dato de impacto**, y cita la decisión si corresponde.

| ✅ Bien | ❌ Mal |
|---|---|
| `Aplica D-001: elimina 30 duplicados (2.480 → 2.450 filas)` | `cambios` |
| `Agrega métrica M-02 tasa de conversión (SQL y DAX)` | `update` |
| `Documenta nulos de precio en diccionario` | `listo` |

## 5. Qué se versiona y qué no

| Se versiona | No se versiona |
|---|---|
| Todo `docs/` | Contraseñas, claves, tokens (`.env`) |
| Código: SQL, notebooks, scripts | Datos personales o confidenciales |
| Datos pequeños y no sensibles de `data/raw/` | Archivos grandes (> 50 MB) |
| Capturas e informes finales | `.pbix` binarios (usa `.pbip`), temporales, cachés |

**Antes del primer `push`, pregúntate:** ¿hay algo aquí que no quiera que vea alguien más? Lo que se sube a un repositorio público queda público, y borrarlo después no lo borra del historial.

Si los datos pesan o son sensibles: descomenta las líneas de `data/` en `.gitignore` y escribe en el README de dónde descargarlos.

## 6. Ramas (para experimentar sin riesgo)

```bash
git switch -c prueba-segmentacion     # crea y cambia a una rama nueva
# ...trabajas y haces commits...
git switch main
git merge prueba-segmentacion         # si salió bien, la incorporas
```

En un proyecto individual puedes trabajar en `main`. Usa ramas cuando vayas a probar algo que podría salir mal.

## 7. Etiquetas para versiones entregadas

```bash
git tag -a v1.0 -m "Entrega final al equipo comercial"
git push --tags
```
Registra la versión también en `CHANGELOG.md`.

## 8. Deshacer errores

| Situación | Qué hacer |
|---|---|
| Quiero descartar cambios de un archivo (aún sin commit) | `git restore archivo` |
| Me equivoqué en el **último** commit (aún sin `push`) | `git commit --amend` |
| Ya hice `push` de algo con datos sensibles | Cambia la credencial/da de baja el dato **primero** y pide ayuda: el historial conserva el contenido |
| No sé en qué estado quedó todo | `git status` y `git log --oneline` |

## 9. Problemas frecuentes

| Mensaje | Causa probable | Solución |
|---|---|---|
| `git no se reconoce` | Git recién instalado, terminal abierta antes | Cierra todas las terminales y abre una nueva |
| `not a git repository` | Estás en la carpeta equivocada, o al descomprimir quedó una carpeta dentro de otra | `dir -Force` (Windows) o `ls -a`; entra a la carpeta que contiene `.git` |
| `remote origin already exists` | Ya tenías un remoto guardado | `git remote set-url origin <dirección>` |
| `rejected ... non-fast-forward` | El repositorio remoto tiene commits que tú no | `git pull --rebase` y luego `git push` |
| Aparece un editor de texto raro al hacer commit | Falta el `-m "mensaje"` | Agrégalo; para salir de `vim`: `Esc`, escribe `:q!` y Enter |

## 10. Convertir tu proyecto en plantilla en GitHub

*Settings → marca **Template repository**.* Aparece el botón **"Use this template"** para crear proyectos nuevos desde cero, sin arrastrar el historial.
