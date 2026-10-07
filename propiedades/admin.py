from django.contrib import admin

from .models import Propiedad


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "operacion", "ciudad", "precio", "estado")
    list_filter = ("tipo", "operacion", "estado")
    search_fields = ("titulo", "direccion", "ciudad")
