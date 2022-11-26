from django.contrib import admin
from .models import Tiempo, Produccion, Venta

# Register your models here.
@admin.register(Tiempo)
class TiempoAdmin(admin.ModelAdmin):
    list_display = ("periodo_registro", "fecha_ingreso")

@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ("bovino", "cantidad_producida", "fecha_registro", "registrado_por")

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ("bovino", "cantidad_vendida", "fecha_registro", "registrado_por")
