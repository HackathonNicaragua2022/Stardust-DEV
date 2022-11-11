from django.contrib import admin

# Register your models here.
@admin.register(Raza)
class RazaAdmin(admin.ModelAdmin):
    list_display = ('NombreRaza', 'DescripcionRaza')

@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ('NombreVacuna', 'DescripcionVacuna')
    
@admin.register(Hato)
class HatoAdmin(admin.ModelAdmin):
    list_display = ('CodigoHato', 'IngresoHato')

@admin.register(Bovino)
class BovinoAdmin(admin.ModelAdmin):
    list_display = ('CodigoBovino', 'RazaBovino', 'HatoBovino', 'display_vacunas', 'Partos', 'UltimoParto', 'FechaCelos')
