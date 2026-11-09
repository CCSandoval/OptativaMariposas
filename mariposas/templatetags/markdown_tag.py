from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

# Funcion que sirve para convertir el texto en markdown a HTML para la descripción de las fichas
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text, extensions=['extra', 'codehilite']))
