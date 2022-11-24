from django.db import models

# Create your models here.
class Raza(models.Model):
    nombre_raza = models.CharField(max_length=50)
    descripcion_raza = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_raza

class Vacuna(models.Model):
    nombre_vacuna = models.CharField(max_length=50)
    descripcion_vacuna = models.CharField( max_length=200)

    def __str__(self):
        return self.nombre_vacuna

class Hato(models.Model):
    codigo_hato = models.CharField(max_length=10)
    ingreso_hato = models.DateField(auto_now=True)

    def __str__(self):
        return self.codigo_hato

class Bovino(models.Model):
    codigo_bovino = models.CharField( max_length=50)

    raza_bovino = models.ForeignKey(Raza, on_delete=models.CASCADE)
    hato_bovino = models.ForeignKey(Hato, on_delete=models.CASCADE)
    vacunas_bovino = models.ManyToManyField(Vacuna)

    partos = models.IntegerField()
    ultimo_parto = models.DateField(auto_now=False, auto_now_add=False, null=True)
    fecha_celos =  models.DateField(auto_now=False, auto_now_add=False, null=True)

    def display_vacunas(self):
        """Create a string for the Vacuna. This is required to display Vacuna in Admin."""
        return ', '.join(vacuna.nombre_vacuna for vacuna in self.vacunas_bovino.all())
    
    display_vacunas.short_description = 'Vacunas'
    
    def display_ultimo_parto(self):
        """Mostrar el ultimo parto como texto plano"""
        fecha = self.ultimo_parto
        return f"{fecha.day}/{fecha.month}/{fecha.year}"

    def display_fecha_celos(self):
        """Mostrar LA fecha celos como texto plano"""
        fecha = self.fecha_celos
        return f"{fecha.day}/{fecha.month}/{fecha.year}"    
        
    
