from django.contrib import admin

from .models import Ficha


@admin.register(Ficha)
class FichaAdmin(admin.ModelAdmin):
    list_display = ('cientifico', 'comun', 'familia', 'resumen_nivel', 'licencia')
    list_filter = ('familia', 'resumen_nivel', 'licencia')
    search_fields = ('cientifico', 'comun')
