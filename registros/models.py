from django.db import models
from inventario.models import Bovino
from django.contrib.auth.models import User


# Create your models here.
class Tiempo(models.Model):
    periodo_registro = models.CharField(max_length = 100, default="")
    
    fecha_ingreso = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.mes_registro}"
    

class Produccion(models.Model):
    bovino  =  models.ForeignKey(Bovino, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Tiempo, on_delete=models.CASCADE)

    cantidad_producida = models.FloatField()
    

    fecha_registro = models.DateField(auto_now=True)
    registrado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Registro de prod"

class Venta(models.Model):
    bovino = models.ForeignKey(Bovino, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Tiempo, on_delete=models.CASCADE)

    cantidad_vendida = models.FloatField()
    precio_de_venta = models.FloatField()

    fecha_registro = models.DateField(auto_now=True)
    registrado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Sobres"


