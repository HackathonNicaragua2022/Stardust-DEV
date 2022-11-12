from django.db import models

# Create your models here.
class Raza(models.Model):
    nombre_raza = models.CharField(max_length=50)
    descripcion_raza = models.CharField(max_length=200)

class Vacuna(models.Model):
    nombre_vacuna = models.CharField(max_length=50)
    descripcion_vacuna = models.CharField( max_length=200)

class Hato(models.Model):
    codigo_hato = models.CharField(max_length=10)
    ingreso_hato = models.DateField(auto_now=True)

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
    

    
    
