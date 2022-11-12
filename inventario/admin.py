from django.contrib import admin
from .models import Raza, Vacuna, Hato, Bovino

# Register your models here.
@admin.register(Raza)
class RazaAdmin(admin.ModelAdmin):
    list_display = ('nombre_raza', 'descripcion_raza')

@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ('nombre_vacuna', 'descripcion_vacuna')
    
@admin.register(Hato)
class HatoAdmin(admin.ModelAdmin):
    list_display = ('codigo_hato', 'ingreso_hato')

@admin.register(Bovino)
class BovinoAdmin(admin.ModelAdmin):
    list_display = ('codigo_bovino', 'raza_bovino', 'hato_bovino', 'display_vacunas', 'partos', 'ultimo_parto', 'fecha_celos')
