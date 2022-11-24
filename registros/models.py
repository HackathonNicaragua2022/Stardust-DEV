from django.db import models
from inventario.models import Bovino

# Create your models here.
class Produccion(models.Model):
    bovino  =  models.ForeignKey(Bovino, on_delete=models.CASCADE)

    def __str__(self):
        return "Registro de prod"