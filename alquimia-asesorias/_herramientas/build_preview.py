#!/usr/bin/env python3
"""Genera ac-ase-preview.html uniendo los bloques en orden.

Simula la estructura de Divi (sección > fila > columna > módulo de código),
con algunos estilos por defecto de Divi, una cabecera fija y un formulario
de ejemplo con el HTML del Contact Form de Divi, para comprobar que los
bloques aguantan dentro de Divi. Solo sirve para revisar: no se pega en Divi.

Uso:  python3 _herramientas/build_preview.py
"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

BLOQUES_ANTES = [
    "ac-ase-00-base.html",
    "ac-ase-01-hero.html",
    "ac-ase-01b-confianza.html",
    "ac-ase-02-ficha-intro.html",
    "ac-ase-03-proceso.html",
    "ac-ase-04-asesorias.html",
    "ac-ase-05-guia.html",
    "ac-ase-06-reserva.html",
    "ac-ase-06b-preguntas.html",
    "ac-ase-07-cta-ficha.html",
]
BLOQUES_DESPUES = ["ac-ase-09-cierre.html"]

# Aproximación de estilos por defecto de Divi para poner a prueba la especificidad
DIVI_SIMULADO = r"""
body { margin:0; font-family:'Open Sans',Arial,sans-serif; font-size:14px; color:#666; line-height:1.7em; font-weight:500; background:#fff; }
h1,h2,h3,h4,h5,h6 { color:#333; padding-bottom:10px; line-height:1em; font-weight:500; font-style:italic; }
p { padding-bottom:1em; }
a { color:#2ea3f2; text-decoration:none; }
.et-l--body ul { list-style-type:disc; padding:0 0 23px 1em; line-height:26px; }
.et-l--body ol { list-style-type:decimal; list-style-position:inside; padding:0 0 23px; line-height:26px; }
#page-container { padding-top:80px; overflow-y:hidden; }
#main-header { position:fixed; top:0; left:0; right:0; height:80px; z-index:99999; background:#fff;
  box-shadow:0 1px 0 rgba(0,0,0,.1); display:flex; align-items:center; justify-content:space-between; padding:0 5%; box-sizing:border-box; }
#main-header .logo { font-family:'Playfair Display',serif; font-weight:700; font-style:normal; color:#2C2C2B; font-size:20px; }
#main-header .aviso { font-size:12px; color:#8C7B6A; }
.et_pb_section { position:relative; background-color:#fff; padding:0; }
.et_pb_row { width:80%; max-width:1080px; margin:auto; position:relative; padding:0; }
.et_pb_row.et_pb_row_fullwidth, .et_pb_specialty_fullwidth { width:100%; max-width:100%; }
.et_pb_module { position:relative; }
.et_pb_button { font-size:20px; font-weight:500; padding:.3em 1em; line-height:1.7em; background:transparent; border:2px solid #2ea3f2;
  border-radius:3px; color:#2ea3f2; position:relative; transition:all .2s; cursor:pointer; }
.et_pb_button:after { content:"→"; position:absolute; margin-left:-1em; opacity:0; transition:all .2s; }
.et_pb_button:hover { padding-right:2em; padding-left:.7em; background:rgba(0,0,0,.05); }
.et_pb_button:hover:after { opacity:1; margin-left:0; }
.et_pb_contact_form_container .et_pb_contact_main_title { font-size:26px; }
.et_pb_contact_form_label { display:none; }
.et_pb_contact p input, .et_pb_contact p textarea, .et_pb_contact_select { background-color:#eee; border:none; border-radius:0;
  color:#999; font-size:14px; padding:16px; width:100%; box-sizing:border-box; }
.et_pb_contact_field { position:relative; float:left; width:100%; padding-left:3%; box-sizing:border-box; }
.et_pb_contact_field_half { width:50%; }
.et_pb_contact_form { margin-left:-3%; }
.et_pb_contact_field_radio input, .et_pb_contact_field_checkbox input { display:none; }
.et_pb_contact_field_radio label i, .et_pb_contact_field_checkbox label i { display:inline-block; width:14px; height:14px; background:#eee; margin-right:6px; }
.et_contact_bottom_container { float:right; text-align:right; margin-top:-1.5%; }
.clearfix:after { content:""; display:block; clear:both; }
"""

FORMULARIO = r"""
<!-- ======= HUECO 8 · Simulación del módulo Contact Form de Divi + Contact Form Helper ======= -->
<div class="et_pb_section et_pb_section_form" style="background-color:#F5F2ED; padding:0 20px;">
 <div class="et_pb_row">
  <div class="et_pb_column">
   <div id="et_pb_contact_form_0" class="et_pb_module et_pb_contact_form_0 et_pb_contact_form_container clearfix ac-ase-form" data-form_unique_num="0">
    <div class="et-pb-contact-message"><ul><li>Rellena los campos obligatorios.</li><li>Introduce un email válido.</li></ul></div>
    <div class="et_pb_contact">
     <form class="et_pb_contact_form clearfix" method="post" action="#" onsubmit="return false;">
      <p class="et_pb_contact_field et_pb_contact_field_0 et_pb_contact_field_half" data-id="nombre" data-type="input">
        <label for="et_pb_contact_nombre_0" class="et_pb_contact_form_label">Nombre</label>
        <input type="text" id="et_pb_contact_nombre_0" class="input" name="et_pb_contact_nombre_0" placeholder="Nombre" data-required_mark="required">
      </p>
      <p class="et_pb_contact_field et_pb_contact_field_1 et_pb_contact_field_half et_pb_contact_field_last" data-id="email" data-type="email">
        <label for="et_pb_contact_email_0" class="et_pb_contact_form_label">Email</label>
        <input type="email" id="et_pb_contact_email_0" class="input et_contact_error" name="et_pb_contact_email_0" placeholder="Email" value="lidia@">
      </p>
      <p class="et_pb_contact_field et_pb_contact_field_2" data-id="telefono" data-type="input">
        <label for="et_pb_contact_telefono_0" class="et_pb_contact_form_label">Teléfono (opcional, por si prefieres WhatsApp)</label>
        <input type="tel" id="et_pb_contact_telefono_0" class="input" name="et_pb_contact_telefono_0" placeholder="Teléfono (opcional, por si prefieres WhatsApp)">
      </p>
      <p class="et_pb_contact_field et_pb_contact_field_3" data-id="color" data-type="radio">
        <span class="et_pb_contact_field_options_wrapper">
          <span class="et_pb_contact_field_options_title">¿Cuál es tu color natural?</span>
          <span class="et_pb_contact_field_options_list">
            __RADIOS_COLOR__
          </span>
        </span>
      </p>
      <p class="et_pb_contact_field et_pb_contact_field_4" data-id="canas" data-type="radio">
        <span class="et_pb_contact_field_options_wrapper">
          <span class="et_pb_contact_field_options_title">¿Cuántas canas tienes, más o menos?</span>
          <span class="et_pb_contact_field_options_list">
            __RADIOS_CANAS__
          </span>
        </span>
      </p>
      <p class="et_pb_contact_field et_pb_contact_field_5" data-id="aplicado" data-type="checkbox">
        <span class="et_pb_contact_field_options_wrapper">
          <span class="et_pb_contact_field_options_title">¿Qué te has aplicado en el pelo en el último año?</span>
          <span class="et_pb_contact_field_options_list">
            __CHECKS_APLICADO__
          </span>
        </span>
      </p>
      <p class="et_pb_contact_field et_pb_contact_field_6" data-id="ultima" data-type="select">
        <label for="et_pb_contact_ultima_0" class="et_pb_contact_form_label">¿Cuándo fue la última vez?</label>
        <select id="et_pb_contact_ultima_0" class="et_pb_contact_select input" name="et_pb_contact_ultima_0">
          <option value="">¿Cuándo fue la última vez?</option>
          <option>Hace menos de 1 mes</option><option>Entre 1 y 3 meses</option>
          <option>Entre 3 y 6 meses</option><option>Hace más de 6 meses</option>
        </select>
      </p>
      <p class="et_pb_contact_field et_pb_contact_field_7" data-id="asesoria" data-type="radio">
        <span class="et_pb_contact_field_options_wrapper">
          <span class="et_pb_contact_field_options_title">¿Qué asesoría te interesa?</span>
          <span class="et_pb_contact_field_options_list">
            __RADIOS_ASESORIA__
          </span>
        </span>
      </p>
      <p class="et_pb_contact_field et_pb_contact_field_8" data-id="objetivo" data-type="text">
        <label for="et_pb_contact_objetivo_0" class="et_pb_contact_form_label">Cuéntame qué te gustaría conseguir</label>
        <textarea id="et_pb_contact_objetivo_0" class="et_pb_contact_message input" name="et_pb_contact_objetivo_0" placeholder="Cuéntame qué te gustaría conseguir"></textarea>
      </p>
      <p class="et_pb_contact_field et_pb_contact_field_9" data-id="fotos" data-type="file">
        <label for="et_pb_contact_fotos_0" class="et_pb_contact_form_label">Fotos (3 archivos JPG o PNG, máx. 5 MB cada uno)</label>
        <input type="file" id="et_pb_contact_fotos_0" name="et_pb_contact_fotos_0[]" accept="image/jpeg,image/png" multiple>
        <small>Simulación: el HTML real del campo de Contact Form Helper se revisará en staging.</small>
      </p>
      <p class="et_pb_contact_field et_pb_contact_field_10" data-id="privacidad" data-type="checkbox">
        <span class="et_pb_contact_field_options_wrapper">
          <span class="et_pb_contact_field_options_list">
            <span class="et_pb_contact_field_checkbox">
              <input type="checkbox" id="et_pb_contact_privacidad_0" class="input" value="acepto">
              <label for="et_pb_contact_privacidad_0"><i></i>He leído y acepto la <a href="#">política de privacidad</a></label>
            </span>
          </span>
        </span>
      </p>
      <div class="et_contact_bottom_container">
        <button type="submit" class="et_pb_contact_submit et_pb_button">Enviar mi ficha</button>
      </div>
     </form>
    </div>
   </div>
   <!-- Simulación del mensaje de éxito (en Divi sustituye al formulario) -->
   <div class="et_pb_module et_pb_contact_form_container clearfix ac-ase-form" style="margin-top:32px;">
     <div class="et-pb-contact-message"><p>Gracias, he recibido tu ficha. Te responderé por email en un plazo de 48 a 72 horas.</p></div>
   </div>
  </div>
 </div>
</div>
"""


def opciones(tipo, grupo, valores, marcado=None):
    clase = "et_pb_contact_field_radio" if tipo == "radio" else "et_pb_contact_field_checkbox"
    out = []
    for i, v in enumerate(valores):
        id_ = f"et_pb_{grupo}_{i}"
        chk = " checked" if marcado == i else ""
        out.append(
            f'<span class="{clase}"><input type="{tipo}" id="{id_}" class="input" name="et_pb_{grupo}" value="{v}"{chk}>'
            f'<label for="{id_}"><i></i>{v}</label></span>'
        )
    return "\n            ".join(out)


def envolver(html, nombre):
    """Simula: sección Divi (padding 0) > fila normal (80 %) > módulo de código."""
    return (
        f'\n<!-- ======= {nombre} ======= -->\n'
        '<div class="et_pb_section"><div class="et_pb_row"><div class="et_pb_column">'
        '<div class="et_pb_module et_pb_code"><div class="et_pb_code_inner">\n'
        f'{html}\n'
        '</div></div></div></div></div>\n'
    )


def main():
    form = FORMULARIO
    form = form.replace("__RADIOS_COLOR__", opciones("radio", "color", ["Rubio", "Castaño claro", "Castaño oscuro", "Moreno", "Pelirrojo", "No lo sé"], 2))
    form = form.replace("__RADIOS_CANAS__", opciones("radio", "canas", ["Ninguna o casi ninguna", "Pocas, sueltas", "Alrededor de la mitad", "Más de la mitad"]))
    form = form.replace("__CHECKS_APLICADO__", opciones("checkbox", "aplicado", ["Nada", "Tinte de peluquería o de caja", "Mechas o decoloración", "Alisado o permanente", "Henna o plantas"], 1))
    form = form.replace("__RADIOS_ASESORIA__", opciones("radio", "asesoria", ["Empezar con coloración vegetal · 50 €", "Mejorar mi proceso · 30 €", "Aún no lo sé"]))

    cuerpo = "".join(envolver((RAIZ / b).read_text(encoding="utf-8"), b) for b in BLOQUES_ANTES)
    cuerpo += form
    cuerpo += "".join(envolver((RAIZ / b).read_text(encoding="utf-8"), b) for b in BLOQUES_DESPUES)

    pagina = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Asesorías · Vista previa local</title>
<meta name="robots" content="noindex">
<!-- SOLO PARA REVISAR EN LOCAL. NO SE PEGA EN DIVI. Generado por _herramientas/build_preview.py -->
<style>{DIVI_SIMULADO}</style>
</head>
<body class="et_fixed_nav">
<header id="main-header"><span class="logo">Alquimia de Color</span><span class="aviso">Vista previa local · cabecera fija simulada</span></header>
<div id="page-container"><div id="et-main-area"><div id="main-content"><div class="et-l et-l--body">
{cuerpo}
</div></div></div></div>
</body>
</html>
"""
    (RAIZ / "ac-ase-preview.html").write_text(pagina, encoding="utf-8")
    print("OK ->", RAIZ / "ac-ase-preview.html")


if __name__ == "__main__":
    main()
