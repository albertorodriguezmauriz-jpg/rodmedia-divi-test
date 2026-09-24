# CLAUDE.md

Contexto e instrucciones de trabajo para este repositorio. No se ha
sobrescrito nada existente al crear este archivo — `.claude/skills/` ya
tenía 7 skills instaladas antes de esta sección y siguen intactas (ver
`.claude/skills/_ORIGEN.md` para las nuevas).

## Contexto del proyecto

Trabajo de agencia (Rodmedia) sobre WordPress + Divi 5, para varios clientes.
Todo el código entregado va en un **Módulo de Código** de Divi: un bloque
HTML + `<style>` + `<script>` autocontenido, vanilla JS, sin build tools.

## Reglas para código de Módulo de Código Divi

- **Un único bloque autocontenido**: HTML + `<style>` + `<script>` juntos,
  pensado para pegar en un solo Módulo de Código de Divi.
- **Prefijo CSS obligatorio según cliente** — todas las clases, IDs y
  variables `--` del módulo llevan el prefijo de su cliente:

  | Prefijo | Cliente |
  |---|---|
  | `rm-` | Rodmedia |
  | `ks-` | Kränzle |
  | `ac-` | Alquimia de Color |
  | `fa-` | Fundación Acércate |
  | `jp-` | Jardín del Papagayo |
  | `gp-` | Geniotipo |
  | `bh-` | Apartamentos Boho |
  | `dr-` | DigitalRod |
  | `cp-` | Coopmunity |
  | `po-` | ProyectOrienta |

- **JS siempre al final del bloque**. Librerías externas solo por CDN
  (cdnjs o jsdelivr) — nada de React, npm ni bundlers.
- **Mobile-first**. Sin `!important` salvo que se justifique en un
  comentario por qué es necesario (conflicto real con el CSS de Divi/el
  tema, no pereza).
- **Respetar siempre `prefers-reduced-motion`** — toda animación de
  entrada/scroll necesita su variante sin movimiento (contenido visible de
  inmediato, no honeypot en opacity:0 permanente).
- **Animar solo `transform` y `opacity`** para mantener 60fps — nunca
  `width`, `height`, `top`, `left`, `margin`, etc. en una animación.
- **Nunca inicializar Lenis ni ninguna librería de smooth scroll sin
  avisar antes** — puede romper el header fijo y los anclajes internos de
  Divi. Si una skill instalada (p. ej. `gsap-web`) sugiere Lenis, es una
  opción a proponer, no a aplicar directamente.
- **Antes de diseñar, definir la dirección de arte** con la skill
  `awwwards` (emoción, arquetipo, tipografía, color, motion) — nunca
  saltar directo al código.
- **Comentarios del código en español.**
- **Guardar cada módulo generado en `/modulos/<prefijo-cliente>/`** con
  nombre descriptivo, ej. `modulos/po-/po-hero-geniotipo.html`.

## Skills de animación y 3D (instaladas 2026-09-24)

Instaladas desde 5 repos de GitHub — detalle completo, commits exactos y
notas de instalación en `.claude/skills/_ORIGEN.md`. Todas viven en
`.claude/skills/`, ninguna requiere red ni ejecuta nada por sí sola.

**Prioridad cuando varias skills se solapan:**

- **GSAP**: usar primero las 8 skills oficiales de GreenSock
  (`gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-plugins`,
  `gsap-utils`, `gsap-performance`) para la API — son la fuente
  canónica. `gsap-web` (de `web-animation-skills`) se solapa en tweens/
  ScrollTrigger con las oficiales; úsala solo para lo que ellas no
  cubren: sincronizar ScrollTrigger con Lenis/Locomotive. `gsap-react`
  y `gsap-frameworks` no aplican a este stack (Divi es vanilla) — solo
  útiles si algún día se entrega un componente fuera de Divi.
- **Three.js**: usar `threejs-*` (10 skills, `CloudAI-X/threejs-skills`)
  para la API real y actual — están al día. `3D-frontend` fija
  **Three.js r128** (obsoleto, de 2021) en su propio código de ejemplo:
  úsala solo por su arquitectura de alto nivel (cámara en scroll, room
  walkthroughs, overlays de contenido, los 40+ patrones de
  `PATTERNS.md`), pero reescribe cualquier snippet de Three.js que
  genere con la API moderna de `threejs-*`, nunca con r128.
- **Dirección de arte**: `awwwards` va primero siempre (ver regla
  arriba) — sus referencias de WebGL/motion son de criterio, no de
  implementación; para el código real usar las skills técnicas.

## Compatibilidad con Divi (vanilla JS + CDN, sin npm/React)

**Directamente vanilla/CDN, sin cambios:**
`gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-plugins`,
`gsap-utils`, `gsap-performance`, `gsap-web` (salvo Lenis, ver regla
arriba), `60fps-animation`, `svg-animation`, `glassmorphism`,
`ascii-animation` (el generador de campos ASCII es CSS/canvas puro; el
script `img-to-ascii.mjs` es una herramienta aparte que necesita
Node + `npm i sharp` a mano — no afecta al módulo final), `threejs-*`
(las 10), `3D-frontend`, `awwwards`.

**Asumen React/Next.js/npm — adaptar antes de usar en un módulo Divi:**
- `gsap-react` — hook `useGSAP`, JSX. No aplica a Divi.
- `gsap-frameworks` — Vue/Svelte (`onMounted`/`onMount`). No aplica a Divi.
- `micro-interaction` — Framer Motion (`motion/react`). Para Divi, tomar
  solo su parte de CSS moderno y reescribir la interacción en vanilla JS.
- `page-transition-animation` — Next.js App Router + Framer Motion. Su
  patrón de View Transitions API es vanilla y sí sirve; ignorar la parte
  de Framer Motion/Next.js.
- `accessible-animation` — mayormente CSS/JS agnóstico; un único ejemplo
  usa un hook de React (`useState`/`useEffect`) a título ilustrativo, el
  resto de patrones (CSS, JS vanilla) sí sirven tal cual.
- `lottie-animation` — el SKILL.md abre con `npm i @lottiefiles/dotlottie-web`.
  Para Divi, cargar la build UMD/CDN del mismo paquete
  (`https://cdn.jsdelivr.net/npm/@lottiefiles/dotlottie-web/dist/dotlottie-web.js`)
  en un `<script type="module">` en vez de instalar por npm — la API
  (`new DotLottie({...})`) es idéntica.

**Tres.js: versión moderna recomendada para CDN**

`3D-frontend` fija Three.js r128 vía
`https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js`
(script clásico global `THREE.*`). Es obsoleto — le faltan años de
mejoras y faltan APIs que las skills `threejs-*` sí documentan
(`CapsuleGeometry`, `WebGPURenderer`, etc. no existen en r128). Para
cualquier módulo nuevo, usar Three.js moderno vía ES modules + import map
en vez del script clásico:

```html
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.180.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.180.0/examples/jsm/"
  }
}
</script>
<script type="module">
  import * as THREE from "three";
  import { OrbitControls } from "three/addons/controls/OrbitControls.js";
  // ...
</script>
```

(Verificar el número de versión más reciente en https://www.jsdelivr.com/package/npm/three
antes de cada módulo nuevo — la API de `threejs-*` está escrita contra
Three.js moderno, no r128.)
