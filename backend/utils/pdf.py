from django.http import HttpResponse
from django.views.generic import ListView, View
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
import os
from django.conf import settings


def link_callback(uri, rel):
    """
    Convierte URIs de HTML a rutas absolutas del sistema para que xhtml2pdf pueda acceder a los recursos.
    """
    sUrl = settings.STATIC_URL
    sRoot = settings.STATIC_ROOT
    mUrl = settings.MEDIA_URL
    mRoot = settings.MEDIA_ROOT

    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri

    if not os.path.isfile(path):
        raise Exception(f"No se encontró el archivo: {path}")
    return path

def render_to_pdf(template_src, context_dict):
    """
    Renderiza una plantilla HTML a un archivo PDF.
    """
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, link_callback=link_callback)
    if not pdf.err:
        return result.getvalue()
    return None
