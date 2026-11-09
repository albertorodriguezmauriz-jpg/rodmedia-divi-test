#!/usr/bin/env python3
"""Genera los JSON de importación de Divi (Portabilidad) con todos los bloques.

Crea dos archivos en alquimia-asesorias/:
  · ac-ase-pagina-divi.json                 → bloques + módulo Contact Form con los campos de la ficha
  · ac-ase-pagina-divi-sin-formulario.json  → solo los bloques (por si prefieres crear el formulario a mano)

Formato: shortcodes de Divi 4 (context "et_builder"). Divi 5 los importa y los convierte.
Uso:  python3 _herramientas/build_divi_json.py
"""
import json
import uuid
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
VB = "4.27.4"  # _builder_version de referencia (Divi 5 lo migra)

ANTES = [
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
DESPUES = ["ac-ase-09-cierre.html"]

CERO = "0px||0px||false|false"


def codificar_codigo(html: str) -> str:
    """Prepara el contenido como lo guarda el Módulo de Código de Divi:
    corchetes como entidades (para no romper los shortcodes) y saltos de
    línea como marcadores (para que WordPress no meta <p> ni <br>)."""
    html = html.strip("\n")
    html = html.replace("[", "&#91;").replace("]", "&#93;")
    return html.replace("\n", "<!-- [et_pb_line_break_holder] -->")


def seccion_codigo(nombre: str) -> str:
    contenido = codificar_codigo((RAIZ / nombre).read_text(encoding="utf-8"))
    etiqueta = nombre.replace(".html", "")
    return (
        f'[et_pb_section fb_built="1" admin_label="{etiqueta}" _builder_version="{VB}" '
        f'custom_padding="{CERO}" custom_margin="{CERO}" theme_builder_area="post_content"]'
        f'[et_pb_row _builder_version="{VB}" width="100%" max_width="100%" '
        f'custom_padding="{CERO}" custom_margin="{CERO}" theme_builder_area="post_content"]'
        f'[et_pb_column type="4_4" _builder_version="{VB}" theme_builder_area="post_content"]'
        f'[et_pb_code admin_label="{etiqueta}" _builder_version="{VB}" '
        f'custom_padding="{CERO}" custom_margin="{CERO}" theme_builder_area="post_content"]'
        f"{contenido}"
        "[/et_pb_code][/et_pb_column][/et_pb_row][/et_pb_section]"
    )


def opciones(valores):
    """Opciones de radio/casillas/desplegable en el formato de Divi (%91 %93 %22)."""
    lista = [{"value": v, "checked": 0, "dragID": i} for i, v in enumerate(valores)]
    txt = json.dumps(lista, ensure_ascii=False, separators=(",", ":"))
    return txt.replace("[", "%91").replace("]", "%93").replace('"', "%22")


def campo(field_id, titulo, tipo="input", obligatorio=True, ancho_completo=True, extra=""):
    return (
        f'[et_pb_contact_field field_id="{field_id}" field_title="{titulo}" field_type="{tipo}" '
        f'required_mark="{"on" if obligatorio else "off"}" '
        f'fullwidth_field="{"on" if ancho_completo else "off"}" {extra}'
        f'_builder_version="{VB}" theme_builder_area="post_content"][/et_pb_contact_field]'
    )


def seccion_formulario() -> str:
    campos = [
        campo("nombre", "Nombre", ancho_completo=False),
        campo("email", "Email", tipo="email", ancho_completo=False),
        campo("telefono", "Teléfono (opcional, por si prefieres WhatsApp)", obligatorio=False),
        campo("color_natural", "¿Cuál es tu color natural?", tipo="radio",
              extra=f'radio_options="{opciones(["Rubio", "Castaño claro", "Castaño oscuro", "Moreno", "Pelirrojo", "No lo sé"])}" '),
        campo("canas", "¿Cuántas canas tienes, más o menos?", tipo="radio",
              extra=f'radio_options="{opciones(["Ninguna o casi ninguna", "Pocas, sueltas", "Alrededor de la mitad", "Más de la mitad"])}" '),
        campo("aplicado", "¿Qué te has aplicado en el pelo en el último año?", tipo="checkbox",
              extra=f'checkbox_options="{opciones(["Nada", "Tinte de peluquería o de caja", "Mechas o decoloración", "Alisado o permanente", "Henna o plantas"])}" '),
        campo("ultima_vez", "¿Cuándo fue la última vez?", tipo="radio", obligatorio=False,
              extra=f'radio_options="{opciones(["Hace menos de 1 mes", "Entre 1 y 3 meses", "Entre 3 y 6 meses", "Hace más de 6 meses"])}" '),
        campo("asesoria", "¿Qué asesoría te interesa?", tipo="radio",
              extra=f'radio_options="{opciones(["Empezar con coloración vegetal · 50 €", "Mejorar mi proceso · 30 €", "Aún no lo sé"])}" '),
        campo("objetivo", "Cuéntame qué te gustaría conseguir", tipo="text"),
        campo("privacidad", "Privacidad", tipo="checkbox",
              extra=f'checkbox_options="{opciones(["He leído y acepto la política de privacidad"])}" '),
    ]
    form = (
        f'[et_pb_contact_form admin_label="Ficha de diagnóstico" module_class="ac-ase-form" '
        f'email="info@alquimiadecolor.com" title="" '
        f'success_message="Gracias, he recibido tu ficha. Te responderé por email en un plazo de 48 a 72 horas." '
        f'submit_button_text="Enviar mi ficha" '
        f'_unique_id="{uuid.uuid5(uuid.NAMESPACE_URL, "alquimiadecolor.com/asesoria-ficha")}" '
        f'_builder_version="{VB}" theme_builder_area="post_content"]'
        + "".join(campos)
        + "[/et_pb_contact_form]"
    )
    return (
        f'[et_pb_section fb_built="1" admin_label="08 · Formulario (Contact Form Helper)" '
        f'_builder_version="{VB}" background_color="#F5F2ED" custom_padding="{CERO}" '
        f'custom_margin="{CERO}" theme_builder_area="post_content"]'
        f'[et_pb_row _builder_version="{VB}" custom_padding="{CERO}" theme_builder_area="post_content"]'
        f'[et_pb_column type="4_4" _builder_version="{VB}" theme_builder_area="post_content"]'
        f"{form}[/et_pb_column][/et_pb_row][/et_pb_section]"
    )


def exportar(nombre_archivo: str, con_formulario: bool):
    partes = [seccion_codigo(b) for b in ANTES]
    if con_formulario:
        partes.append(seccion_formulario())
    partes += [seccion_codigo(b) for b in DESPUES]
    datos = {
        "context": "et_builder",
        "data": {"1": "".join(partes)},
        "presets": [],
        "global_colors": [],
        "images": [],
        "thumbnails": [],
    }
    destino = RAIZ / nombre_archivo
    destino.write_text(json.dumps(datos, ensure_ascii=False), encoding="utf-8")
    print("OK ->", destino, f"({destino.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    exportar("ac-ase-pagina-divi.json", con_formulario=True)
    exportar("ac-ase-pagina-divi-sin-formulario.json", con_formulario=False)
