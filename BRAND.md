# Rodmedia — sistema de marca y diseño (vigente)

Referencia rápida para cualquier componente nuevo de Rodmedia. Última actualización: hero de
home (`components/rm-hero-home.html`), validado y aprobado por Alberto.

## Posicionamiento (cerrado, no reinterpretar)

Hub de servicios gestionados con catálogo y precio cerrado (dominio, diseño web, tienda
online, hosting, marketing, correo) — línea IONOS/Hostinger a escala de operador único, sede
en Benicarló (Baix Maestrat, Castellón).

Ya **no** es "agencia creativa de proyectos a medida". Evitar lenguaje de "con alma",
"proyectos a medida" o storytelling emocional de estudio de diseño. El copy vende resolución
y precio cerrado, no artesanía.

## Paleta de marca (cerrada, no reinterpretar)

| Token | Valor | Uso |
|---|---|---|
| `--rm-primary` | `#0f0f1e` | Fondo navy |
| `--rm-blue` | `#3a7bd5` | Azul de marca |
| `--rm-orange` | `#e8531a` | Naranja de marca |
| — | `linear-gradient(135deg, #3a7bd5, #e8531a)` | Gradiente de firma (botones, iconos activos, línea superior) |
| `--rm-light` | `#f8f8fb` | Texto claro sobre navy |
| `--rm-text-muted` | `#9aa3bd` | Subtítulos |
| `--rm-text-muted-2` | `#7d84a0` | Etiquetas pequeñas |

**Obsoleto** (etapa anterior "agencia creativa con alma", no usar salvo petición expresa):
`--rm-primary: #1a1a2e` / `--rm-accent: #e8934a` — sigue presente en `rm-hero.html`,
`rm-hero-seo.html`, `rm-hero-ecommerce.html` (componentes de la etapa anterior).

## Tipografía (cerrada)

**Playfair Display** (titulares) + **Inter** (cuerpo). Única marca del estudio donde Inter
está aprobado explícitamente — para el resto de trabajo (DigitalRod incluido) sigue la regla
general de evitar Inter/Roboto/Arial.

## Sistema de diseño validado

Implementado en `components/rm-hero-home.html` — usar como referencia directa antes de crear
una sección nueva:

- **Fondo vivo**: canvas de partículas conectadas por líneas azules finas + 2 "glows"
  difuminados (azul + naranja) flotando en bucle lento + línea superior de 3px con gradiente
  azul→naranja→azul animado (shimmer).
- **Badge** con punto que parpadea sutilmente (`opacity` 1↔0.25 en bucle).
- **Entradas secuenciadas**: fade + slide-up en cascada (delays escalonados ~0.05s–0.4s), nunca
  todos los elementos apareciendo a la vez.
- **Tarjetas "glass"**: `background: rgba(255,255,255,0.03–0.08)`, `backdrop-filter: blur(14–16px)`,
  `border: 1px solid rgba(255,255,255,0.08–0.12)`, radius grande (16–24px).
- **Patrón "leyenda en pastilla"**: para info contextual/dinámica (ej. al hacer hover sobre un
  icono), tarjeta glass en pastilla con icono circular con gradiente a la izquierda + título en
  negrita (16px) + descripción en texto muted (13px) — no texto plano suelto.
- **Botones**: primario con `background: linear-gradient(135deg, #3a7bd5, #e8531a)` + texto
  blanco; secundario tipo "ghost" (fondo transparente + borde `rgba(255,255,255,0.28)`).

## Empaquetado para Divi

Todo el HTML/CSS/JS de una sección va autocontenido en un único `<section class="rm-...">`
con `<style>` y `<script>` embebidos al final, listo para pegar en **un solo** módulo de
código (`et_pb_code`). No repartir el fondo/interactividad en módulos nativos de Divi 5 por
columnas — se probó y resultó poco fiable (colapsos de layout en grid). Envolver en JSON de
portabilidad clásico (`context: "et_builder"`, shortcodes
`et_pb_section > et_pb_row > et_pb_column > et_pb_code`) para importar desde
Divi → Biblioteca → Portabilidad → Importar.

**Selectores del script**: resolver la sección con `document.querySelector('.rm-...')` (una
instancia por página) — nunca `document.currentScript.closest(...)`: el `<script>` es hermano
de la `<section>` en este patrón (no descendiente), así que `.closest()` nunca la encuentra.
El fallo es silencioso — no lanza error, simplemente el JS no hace nada.
