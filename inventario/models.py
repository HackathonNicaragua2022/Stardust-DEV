from django.db import models

# Create your models here.
class Raza(models.Model):
    NombreRaza = models.CharField(max_length=50)
    DescripcionRaza = models.CharField(max_length=200)

class Vacuna(models.Model):
    NombreVacuna = models.CharField(max_length=50)
    DescripcionVacuna = models.CharField( max_length=200)

class Hato(models.Model):
    CodigoHato = models.CharField(max_length=10)
    IngresoHato = models.DateField(auto_now=True)

class Bovino(models.Model):
    CodigoBovino = models.CharField( max_length=50)

    RazaBovino = models.ForeignKey(Raza, on_delete=models.CASCADE)
    HatoBovino = models.ForeignKey(Hato, on_delete=models.CASCADE)
    VacunasBovino = models.ManyToManyField(Vacuna)

    Partos = models.IntegerField()
    UltimoParto = models.DateField(auto_now=False, auto_now_add=False, null=True)
    FechaCelos =  models.DateField(auto_now=False, auto_now_add=False, null=True)

    def display_vacunas(self):
        """Create a string for the Vacuna. This is required to display Vacuna in Admin."""
        return ', '.join(vacuna.NombreVacuna for vacuna in self.VacunasBovino.all())

    display_vacunas.short_description = 'Vacunas'
    
    def NuevoBovino(datos):
        pass    

    
    
