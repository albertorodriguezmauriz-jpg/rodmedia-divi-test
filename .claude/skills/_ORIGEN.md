# Origen de las skills instaladas (animación y 3D)

Instaladas el 2026-09-24. Para actualizar una skill: volver a clonar el repo de
origen en `tmp-skills/` (no está en git, `.gitignore` lo excluye), copiar la
carpeta correspondiente sobre `.claude/skills/<nombre>/` y anotar aquí el
nuevo commit.

Las 7 skills instaladas antes de esta tanda (`banner-design`, `brand`,
`design`, `design-system`, `slides`, `ui-styling`, `ui-ux-pro-max`) no están
en esta tabla — vinieron de un zip subido manualmente, no de un repo git.

| Skill | Repo de origen | Commit clonado | Fecha instalación |
|---|---|---|---|
| `gsap-core` | github.com/greensock/gsap-skills | `aed9cfd` | 2026-09-24 |
| `gsap-frameworks` | github.com/greensock/gsap-skills | `aed9cfd` | 2026-09-24 |
| `gsap-performance` | github.com/greensock/gsap-skills | `aed9cfd` | 2026-09-24 |
| `gsap-plugins` | github.com/greensock/gsap-skills | `aed9cfd` | 2026-09-24 |
| `gsap-react` | github.com/greensock/gsap-skills | `aed9cfd` | 2026-09-24 |
| `gsap-scrolltrigger` | github.com/greensock/gsap-skills | `aed9cfd` | 2026-09-24 |
| `gsap-timeline` | github.com/greensock/gsap-skills | `aed9cfd` | 2026-09-24 |
| `gsap-utils` | github.com/greensock/gsap-skills | `aed9cfd` | 2026-09-24 |
| `60fps-animation` | github.com/iart-ai/web-animation-skills | `b6dba3e` | 2026-09-24 |
| `accessible-animation` | github.com/iart-ai/web-animation-skills | `b6dba3e` | 2026-09-24 |
| `ascii-animation` | github.com/iart-ai/web-animation-skills | `b6dba3e` | 2026-09-24 |
| `glassmorphism` | github.com/iart-ai/web-animation-skills | `b6dba3e` | 2026-09-24 |
| `gsap-web` | github.com/iart-ai/web-animation-skills | `b6dba3e` | 2026-09-24 |
| `lottie-animation` | github.com/iart-ai/web-animation-skills | `b6dba3e` | 2026-09-24 |
| `micro-interaction` | github.com/iart-ai/web-animation-skills | `b6dba3e` | 2026-09-24 |
| `page-transition-animation` | github.com/iart-ai/web-animation-skills | `b6dba3e` | 2026-09-24 |
| `svg-animation` | github.com/iart-ai/web-animation-skills | `b6dba3e` | 2026-09-24 |
| `threejs-animation` | github.com/CloudAI-X/threejs-skills | `b1c6230` | 2026-09-24 |
| `threejs-fundamentals` | github.com/CloudAI-X/threejs-skills | `b1c6230` | 2026-09-24 |
| `threejs-geometry` | github.com/CloudAI-X/threejs-skills | `b1c6230` | 2026-09-24 |
| `threejs-interaction` | github.com/CloudAI-X/threejs-skills | `b1c6230` | 2026-09-24 |
| `threejs-lighting` | github.com/CloudAI-X/threejs-skills | `b1c6230` | 2026-09-24 |
| `threejs-loaders` | github.com/CloudAI-X/threejs-skills | `b1c6230` | 2026-09-24 |
| `threejs-materials` | github.com/CloudAI-X/threejs-skills | `b1c6230` | 2026-09-24 |
| `threejs-postprocessing` | github.com/CloudAI-X/threejs-skills | `b1c6230` | 2026-09-24 |
| `threejs-shaders` | github.com/CloudAI-X/threejs-skills | `b1c6230` | 2026-09-24 |
| `threejs-textures` | github.com/CloudAI-X/threejs-skills | `b1c6230` | 2026-09-24 |
| `3D-frontend` | github.com/zyliu0/3d-frontend | `5e79671` | 2026-09-24 |
| `awwwards` | github.com/tponscr-debug/claude-skill-awwwards | `d18aa0c` | 2026-09-24 |

## Notas de instalación (desviaciones del contenido original)

- **`threejs-skills`**: el README de este repo indica clonar desde
  `github.com/pinkforest/threejs-playground` — se ignoró esa URL tal y como
  se pidió, y se usó el contenido tal cual está en `CloudAI-X/threejs-skills`
  (el repo que realmente se clonó).
- **`3D-frontend`**: el repo de origen NO guarda la skill en una carpeta
  `skills/` — el propio archivo `3D-frontend.md` en la raíz del repo es el
  SKILL.md (con frontmatter `name`/`description` válido). Se copió
  renombrado a `SKILL.md` dentro de `.claude/skills/3D-frontend/`, junto con
  `references/PATTERNS.md` y las 4 páginas de `demo/` (HTML estático, sin
  scripts de build).
- **`awwwards`**: coincide exactamente con lo pedido —
  `.claude/skills/awwwards/` con `SKILL.md` + `references/` (7 ficheros).

## Revisión de seguridad (resumen)

Antes de instalar, se revisó cada repo completo (READMEs, todos los
`SKILL.md`, y cualquier `.sh`/`.py`/`.js`/`.mjs`) buscando: hooks que se
ejecuten solos, llamadas de red no documentadas, borrado de archivos o
cambios de configuración fuera de la carpeta del repo.

- Ningún repo define hooks de Claude Code (los `.claude-plugin/plugin.json`
  de `gsap-skills` y `web-animation-skills` solo declaran metadatos y la
  ruta `skills/`, sin clave `hooks`).
- `web-animation-skills/scripts/*.sh` (3 scripts: `probe-mp4.sh`,
  `seek-shot.sh`, `contact-sheet.sh`) son herramientas de verificación
  manual (comprobar un .mp4, capturar una animación HTML en momentos
  concretos, unir capturas en una sola imagen). Viven en la raíz del repo,
  no dentro de ninguna carpeta de skill — no se copiaron. Ninguno se
  autoejecuta; `seek-shot.sh` usa `npx playwright` (puede descargar
  Chromium la primera vez que se invoca manualmente, comportamiento
  documentado, no oculto).
- `web-animation-skills/skills/ascii-animation/scripts/img-to-ascii.mjs` sí
  se copió (vive dentro de la carpeta de esa skill). Es un conversor de
  imagen a ASCII que requiere `node` + el paquete npm `sharp` instalado a
  mano — no se ejecuta solo, no hace llamadas de red.
- No se encontró ningún `curl`, `wget`, `rm -rf`, `eval()` ni llamada a
  `child_process`/`exec()` fuera de contexto de ejemplo/documentación en
  ninguno de los 5 repos.

**Conclusión: se instalaron las 29 skills sin descartar ninguna por motivos
de seguridad.**
