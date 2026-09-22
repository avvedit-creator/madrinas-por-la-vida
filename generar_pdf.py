# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable,
    KeepTogether, Table, TableStyle, Image,
)

# ---------- Identidad Renueva Smart ----------
FONTS_DIR = r"C:\Users\Alex\Documents\Cloude\Rehacer webs\Recursos\fonts-renueva-smart"
LOGO = r"C:\Users\Alex\Documents\Cloude\renueva-smart\_fuente\assets\logo-dark.png"

pdfmetrics.registerFont(TTFont("Fraunces-Bold", FONTS_DIR + r"\fraunces-bold.ttf"))
pdfmetrics.registerFont(TTFont("Fraunces-Italic", FONTS_DIR + r"\fraunces-italic-500.ttf"))
pdfmetrics.registerFont(TTFont("PJS-Regular", FONTS_DIR + r"\pjs-regular.ttf"))
pdfmetrics.registerFont(TTFont("PJS-Bold", FONTS_DIR + r"\pjs-bold.ttf"))
pdfmetrics.registerFont(TTFont("PJS-ExtraBold", FONTS_DIR + r"\pjs-extrabold.ttf"))

ORANGE = colors.HexColor("#FF6A00")
INK = colors.HexColor("#0B0C0E")
PAPER = colors.HexColor("#F5F3EE")
WHITE = colors.HexColor("#FFFFFF")
GREY = colors.HexColor("#92979D")
BODY = colors.HexColor("#5A6068")
LINE = colors.HexColor("#DFE0DC")

FILE_NAME = "Temas_para_la_llamada_Madrinas_Por_La_Vida.pdf"

doc = SimpleDocTemplate(
    FILE_NAME,
    pagesize=A4,
    leftMargin=2.4 * cm,
    rightMargin=2.4 * cm,
    topMargin=3.6 * cm,
    bottomMargin=2.2 * cm,
    title="Temas para la llamada - Madrinas Por La Vida",
)

title_style = ParagraphStyle(
    "TitleCustom", fontName="Fraunces-Bold", fontSize=27, leading=30,
    textColor=INK, spaceAfter=2,
)
title_orange_style = ParagraphStyle(
    "TitleOrange", fontName="Fraunces-Italic", fontSize=27, leading=30,
    textColor=ORANGE, spaceAfter=6,
)
subtitle_style = ParagraphStyle(
    "SubtitleCustom", fontName="PJS-Regular", fontSize=11, leading=16,
    textColor=BODY, spaceAfter=16,
)
label_style = ParagraphStyle(
    "LabelCustom", fontName="PJS-ExtraBold", fontSize=9, leading=12,
    textColor=ORANGE, spaceAfter=6, spaceBefore=2,
)
h2_style = ParagraphStyle(
    "H2Custom", fontName="Fraunces-Bold", fontSize=14, leading=18,
    textColor=INK, spaceBefore=0, spaceAfter=6,
)
intro_style = ParagraphStyle(
    "IntroCustom", fontName="PJS-Regular", fontSize=10.5, leading=16,
    textColor=BODY, spaceAfter=4,
)
body_style = ParagraphStyle(
    "BodyCustom", fontName="PJS-Regular", fontSize=10.3, leading=15,
    textColor=INK,
)
body_bold_style = ParagraphStyle(
    "BodyBoldCustom", parent=body_style, fontName="PJS-Bold",
)
note_body_style = ParagraphStyle(
    "NoteBodyCustom", parent=body_style, fontSize=10.2, leading=15.5,
)
foot_style = ParagraphStyle(
    "FootCustom", fontName="PJS-Regular", fontSize=8.5, leading=12,
    textColor=GREY,
)


def header_footer(canvas, doc_):
    canvas.saveState()
    # Fondo papel
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)

    # Logo arriba a la izquierda
    logo_w = 3.4 * cm
    img = ImageReader(LOGO)
    iw, ih = img.getSize()
    logo_h = logo_w * ih / iw
    canvas.drawImage(
        LOGO, 2.4 * cm, A4[1] - 1.4 * cm - logo_h,
        width=logo_w, height=logo_h, mask="auto",
    )

    # Filete naranja bajo el header
    canvas.setStrokeColor(ORANGE)
    canvas.setLineWidth(1.6)
    canvas.line(2.4 * cm, A4[1] - 3.05 * cm, A4[0] - 2.4 * cm, A4[1] - 3.05 * cm)

    # Pie de página
    canvas.setFont("PJS-Regular", 8.5)
    canvas.setFillColor(GREY)
    canvas.drawString(2.4 * cm, 1.3 * cm, "Renueva Smart — renuevasmart.com")
    canvas.drawRightString(A4[0] - 2.4 * cm, 1.3 * cm, f"Página {doc_.page}")
    canvas.restoreState()


def seccion(numero, titulo, items):
    """Arma un bloque TEMA (label + título + bullets) que viaja junto, para que el
    título nunca quede solo al final de una página."""
    bullets = [
        ListItem(Paragraph(item, body_style), leftIndent=14, bulletColor=ORANGE)
        for item in items
    ]
    bloque = [
        Paragraph(f"TEMA {numero}", label_style),
        Paragraph(titulo, h2_style),
        ListFlowable(bullets, bulletType="bullet", start="circle", leftIndent=10, spaceAfter=4),
        HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=8, spaceAfter=2),
    ]
    return KeepTogether(bloque)


def nota_permisos():
    """Bloque final, destacado en una caja: permisos de acceso al dominio/web."""
    contenido = Paragraph(
        "El dominio y la web son propiedad de Madrinas Por La Vida — nunca dejan de serlo. "
        "Antes de tocar nada, voy a necesitar que me den <b>permiso explícito y por escrito</b> "
        "para intervenir el sitio, el dominio y los accesos relacionados. "
        "Para que quede todo claro y en regla, les voy a pasar un <b>formulario de autorización</b> "
        "(ya lo tenemos armado en Renueva Smart) para que lo firmen antes de empezar.",
        note_body_style,
    )
    tabla = Table([[contenido]], colWidths=[doc.width])
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WHITE),
        ("BOX", (0, 0), (-1, -1), 1, ORANGE),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    bloque = [
        Paragraph("TEMA 06", label_style),
        Paragraph("Permisos para intervenir la web", h2_style),
        tabla,
    ]
    return KeepTogether(bloque)


story = []

story.append(Paragraph("Temas para la llamada", title_style))
story.append(Paragraph("<i>Madrinas Por La Vida</i>", title_orange_style))
story.append(Paragraph(
    "Reconstrucción de la página web — guía preparada por Renueva Smart",
    subtitle_style
))
story.append(HRFlowable(width="100%", thickness=0.8, color=LINE, spaceAfter=14))

story.append(Paragraph(
    "Esta es una guía de los puntos que conviene conversar en la llamada, para entender bien "
    "qué necesita la organización y poder armar la nueva web de la mejor manera. No hace falta "
    "preparar nada especial de antemano: es simplemente una charla para conocerse y entender el proyecto.",
    intro_style
))
story.append(Spacer(1, 6))

secciones = [
    (
        "01", "Dominio y accesos",
        [
            "Preguntarles qué pasó con la web: ¿sabían que estaba caída? ¿saben por qué "
            "(el dominio venció, cambio de proveedor, falta de pago, etc.)?",
            "¿Quién compró originalmente el dominio (www.madrinasporlavida.com) y el hosting?",
            "¿Tienen acceso a esas cuentas, o hay que gestionar todo de nuevo?",
            "Definir quién quedará como responsable de pagar la renovación del dominio a futuro, "
            "para que no vuelva a vencer.",
        ],
    ),
    (
        "02", "Contenido que quieren mantener o actualizar",
        [
            "Contarles que gran parte del contenido de la web anterior se pudo recuperar a través "
            "de archivos históricos de internet, así que no se pierde aunque ellos no tengan "
            "un respaldo propio guardado.",
            "Historia y misión de la organización (quién la fundó, cuándo, por qué).",
            "Localidades donde trabajan actualmente (¿siguen siendo las mismas de antes: Malvín, "
            "Aeroparque, Artigas, Colombia, u otras?).",
            "Testimonios de madres y madrinas.",
            "Noticias o novedades recientes.",
            "Fotos y galería de actividades.",
        ],
    ),
    (
        "03", "Formas de ayudar y donar",
        [
            "¿Qué formas de colaboración quieren mostrar? (ser madrina, donar dinero, donar "
            "ropa/artículos, voluntariado, etc.)",
            "¿Tienen datos bancarios, Mercado Pago, o algún medio de pago online para recibir "
            "donaciones?",
            "¿Quieren un botón de \"Donar\" bien visible en la web?",
        ],
    ),
    (
        "04", "Imagen y estilo",
        [
            "Aclarar que hay cosas de la web anterior que se pueden recuperar (textos, estructura, "
            "fotos si las comparten) — o, si prefieren, se les puede dar una identidad visual "
            "nueva de cero.",
        ],
    ),
    (
        "05", "Mantenimiento futuro",
        [
            "¿Quién va a encargarse de subir noticias o fotos nuevas más adelante?",
            "¿Prefieren que sea alguien de la organización con un panel simple, o que quede a "
            "cargo tuyo?",
        ],
    ),
]

for numero, titulo, items in secciones:
    story.append(seccion(numero, titulo, items))

story.append(nota_permisos())

story.append(Spacer(1, 10))
story.append(Paragraph(
    "Documento preparado como guía informal para la llamada — no requiere conocimientos técnicos.",
    foot_style
))

# Logo grande centrado en el espacio en blanco al final de la última página
story.append(Spacer(1, 60))
_logo_img = ImageReader(LOGO)
_iw, _ih = _logo_img.getSize()
_logo_w = 9.5 * cm
_logo_h = _logo_w * _ih / _iw
closing_logo = Image(LOGO, width=_logo_w, height=_logo_h)
closing_logo.hAlign = "CENTER"
story.append(closing_logo)

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("PDF generado:", FILE_NAME)
