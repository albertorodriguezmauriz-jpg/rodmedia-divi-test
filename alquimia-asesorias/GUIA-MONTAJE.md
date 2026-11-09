# Página de asesorías · Alquimia de Color · Guía de montaje en Divi 5

Entorno de pruebas: **staging2.alquimiadecolor.com** (nunca en producción).
Página: **borrador**, slug `/asesoria-coloracion-vegetal/`.

---

## 1. Orden de montaje

Un Módulo de Código por bloque, cada uno en su propia sección de Divi, en este orden:

| # | Tipo | Archivo / módulo | Fondo de la sección de Divi |
|---|---|---|---|
| 0 | Código | `ac-ase-00-base.html` | Sin fondo (no muestra nada) |
| 1 | Código | `ac-ase-01-hero.html` | Sin fondo (lo pone el bloque) |
| 1b | Código · *nuevo, opcional* | `ac-ase-01b-confianza.html` (franja de 4 garantías) | Sin fondo |
| 2 | Código | `ac-ase-02-ficha-intro.html` | Sin fondo |
| 3 | Código | `ac-ase-03-proceso.html` | Sin fondo |
| 4 | Código | `ac-ase-04-asesorias.html` | Sin fondo |
| 5 | Código | `ac-ase-05-guia.html` | Sin fondo |
| 6 | Código | `ac-ase-06-reserva.html` | Sin fondo |
| 6b | Código · *nuevo, opcional* | `ac-ase-06b-preguntas.html` (preguntas frecuentes + JSON-LD FAQPage) | Sin fondo |
| 7 | Código | `ac-ase-07-cta-ficha.html` (ancla `#ac-ase-ficha`) | Sin fondo |
| 8 | **Divi** | Módulo **Contact Form** + Contact Form Helper, con la clase **`ac-ase-form`** | **Crudo `#F5F2ED`** |
| 9 | Código | `ac-ase-09-cierre.html` | Sin fondo |

Bloque opcional: `ac-ase-hueco.html`, para poner un título o una introducción justo antes de un módulo nativo futuro, como el calendario de BookingPress. Las instrucciones están en el propio archivo.

**No se pega en Divi:** `ac-ase-preview.html`, que solo sirve para revisar en local, ni la carpeta `_herramientas/`.

## 2. Ajustes de Divi recomendados

**Secciones con Módulo de Código (bloques 0 a 7 y 9):**
- Sección: padding superior e inferior a **0**. Sin color de fondo.
- Fila: padding a **0**. Recomendado: **ancho 100 % y ancho máximo 100 %**. El bloque también funciona dentro de una fila normal, porque los fondos salen a ancho completo y el contenido se mantiene en 1100 px.
- Columna: una sola columna, sin padding.
- Módulo de Código: margen y padding a 0.
- Puedes poner varios bloques seguidos en una misma sección/fila si te resulta más cómodo, porque cada bloque crea su propia sección HTML.

**Sección del formulario (hueco 8):**
- Sección: **fondo Crudo `#F5F2ED`**, padding superior **0** e inferior **0**. El bloque 9 aporta el aire de abajo.
- Fila: ancho normal. El formulario se limita a 780 px y se centra.
- Módulo Contact Form → **Avanzado → ID y clases CSS → Clase CSS: `ac-ase-form`**.
- En la pestaña **Diseño** del módulo **no cambies** colores, fuentes ni el botón. Así manda el CSS de la marca. Si Divi genera estilos propios del módulo, ganarían a los nuestros.
- Activa la opción de **mostrar etiquetas** si Contact Form Helper la ofrece. El CSS ya las muestra, porque mejoran la accesibilidad frente a usar solo el placeholder.

**Para cualquier módulo nativo futuro** (por ejemplo, BookingPress), pon la clase `ac-ase-modulo`.

**Página:**
- Cabecera fija: el JS mide la cabecera de Divi y deja ese margen al saltar a las anclas. Si aun así queda corto o largo, ajusta `margenExtra` en `AC_ASE_CONFIG` (bloque 00).
- Caché: después de guardar, purga la caché de SiteGround (SG Optimizer → Purgar caché).

## 3. Destino de los botones (bloque 00)

Al principio del `<script>` del bloque 00:

```js
const AC_ASE_CONFIG = {
  urlFicha: '#ac-ase-ficha',            // botón del bloque 2
  urlBotonMejorar: '#ac-ase-ficha',     // tarjeta de 30 €
  urlBotonEmpezar: '#ac-ase-ficha',     // tarjeta de 50 €
  urlFormulario: '#ac-ase-formulario',  // botón de «¿Empezamos?», baja al formulario
  margenExtra: 24
};
```

Si en el futuro la asesoría de 30 € se puede reservar directamente, basta con cambiar `urlBotonMejorar` por la URL de la reserva.

## 4. Fotos reales (muy recomendable)

Las ilustraciones son provisionales y originales, sin imágenes de stock. Lo que más confianza transmite es ver a Lidia. Para cambiar cualquier ilustración por una foto:
- **Hero (`ac-ase-01-hero.html`):** dentro de `<figure class="ac-ase-arco">`, sustituye el `<svg>` entero por `<img src="URL" alt="Lidia Marín preparando una mezcla de plantas" width="800" height="1000">`. Mejor una foto vertical (4:5). El arco la recorta solo.
- Sirve igual para cualquier otro sitio donde se use un `<figure class="ac-ase-arco">`.
- Fotos sugeridas a Lidia: ella preparando una mezcla, sus manos con el cuenco y las plantas en polvo, y un antes y después real (solo si tiene permiso de la clienta).

## 4b. Imagen de fondo del hero (opcional)

En `ac-ase-01-hero.html`, dentro de la etiqueta `<section>`:
- Cambia `--ac-ase-hero-img: none;` por `--ac-ase-hero-img: url('https://…/imagen.jpg');`.
- Añade la clase `ac-ase-hero--con-imagen`. Oculta las formas decorativas y refuerza la veladura para que el texto se siga leyendo bien.

## 5. Campos de la ficha (Contact Form Helper)

| Campo | Tipo | Obligatorio | Opciones / notas |
|---|---|---|---|
| Nombre | Texto | Sí | ID del campo: `nombre`, que permite usar `%%nombre%%` en el email |
| Email | Email | Sí | |
| Teléfono | Texto | No | Etiqueta: «Teléfono (opcional, por si prefieres WhatsApp)» |
| ¿Cuál es tu color natural? | Radio | Sí | Rubio · Castaño claro · Castaño oscuro · Moreno · Pelirrojo · No lo sé |
| ¿Cuántas canas tienes, más o menos? | Radio | Sí | Ninguna o casi ninguna · Pocas, sueltas · Alrededor de la mitad · Más de la mitad |
| ¿Qué te has aplicado en el pelo en el último año? | Casillas | Sí | Nada · Tinte de peluquería o de caja · Mechas o decoloración · Alisado o permanente · Henna o plantas |
| ¿Cuándo fue la última vez? | Radio o desplegable | No | Hace menos de 1 mes · Entre 1 y 3 meses · Entre 3 y 6 meses · Hace más de 6 meses |
| ¿Qué asesoría te interesa? | Radio | Sí | Empezar con coloración vegetal · 50 € · Mejorar mi proceso · 30 € · Aún no lo sé |
| Cuéntame qué te gustaría conseguir | Área de texto | Sí | |
| Fotos | Subida de archivos (Contact Form Helper) | Sí | 3 archivos JPG/PNG, máx. 5 MB cada uno. Guardar **en base de datos o como adjunto del email, NUNCA en la biblioteca de medios** |
| He leído y acepto la política de privacidad | Casilla | Sí | Con enlace a la política de privacidad |

- No incluir preguntas de salud ni casilla de suscripción.
- **Email automático a la clienta:**
  - Asunto: «He recibido tu ficha».
  - Texto: «Hola, %%nombre%%: ya tengo tu ficha y tus fotos. Voy a estudiar tu cabello con calma y te responderé por email en un plazo de 48 a 72 horas. Si ves que no te llega, revisa la carpeta de correo no deseado. Un abrazo, Lidia».
  - El formato exacto de la variable del nombre (`%%nombre%%`) depende del ID del campo. Se confirmará en el plugin.
- Remitente de todos los emails: **info@alquimiadecolor.com**.
- Una ayuda para las fotos, como «junto a una ventana, de día, sin flash…», puede ir como descripción del propio campo si Lidia lo aprueba. No se ha incluido en la página porque no está en sus textos.

## 6. SEO

- **Meta title (57 caracteres):** Asesoría de coloración vegetal online | Alquimia de Color
- **Meta description (146 caracteres):** Asesoría personalizada de coloración vegetal y henna con Lidia Marín. Envía tu ficha de diagnóstico gratuita y aprende a cubrir canas con plantas.
- **Slug:** `/asesoria-coloracion-vegetal/`
- Un solo H1 (hero). Las secciones van en H2 y las tarjetas en H3.
- El JSON-LD `Service` con los dos servicios (30 € y 50 €, EUR, `provider` = Alquimia de Color) va en el bloque 00.

## 7. Textos nuevos pendientes del visto bueno de Lidia

Salen de sus propios textos o del email automático, pero no están escritos tal cual por ella:
- **Hero:** antetítulo «Asesoría online con Lidia Marín», botón «Rellenar la ficha de diagnóstico gratuita» y nota «Primera valoración sin coste».
- **Bloque 01b (franja):** los 4 títulos y sus subtítulos.
- **Bloque 06 (reserva):** distintivos «Pago online», «Bizum» y «Cita reservada al pagar».
- **Bloque 06b (preguntas frecuentes):** las 6 preguntas y respuestas. Si cambia alguna, hay que cambiarla también en el JSON-LD del mismo bloque.
- **Bloque 07:** las 3 fotos («La raíz, de cerca», «La melena, de espaldas», «Tu perfil») y el consejo «Junto a una ventana, de día y sin flash, con el pelo seco y sin filtros».
- **Bloque 07:** «Tus fotos solo se usan para estudiar tu caso». **Debe confirmarlo Lidia**, porque es un compromiso de privacidad.
- **Bloque 09:** firma «Lidia Marín · Alquimia de Color».
- **Proceso:** etiqueta «Sin coste».

## 8. Notas

- **Fuentes:** el bloque 00 carga Playfair Display 700 y Montserrat 300/500 desde Google Fonts. Si la web ya las aloja en local (opción de Divi o plugin), se puede quitar el `<link>` del bloque 00.
- **Marrón Raíz `#8C7B6A`:** se usa solo en elementos decorativos. Para texto pequeño se usa un tono oscurecido (`--ac-raiz-texto: #6B5D50`) que cumple AA.
- **Subida de archivos:** el estilo del campo de Contact Form Helper es genérico. Al montarlo en staging se revisará su HTML real y se afinará.
- **Para regenerar la vista previa** después de editar un bloque:

```bash
python3 _herramientas/build_preview.py
```
