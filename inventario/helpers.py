from .models import Raza, Frecuencia, Hato, Vacuna

def getValidRaza(nombre):
    raza = Raza.objects.filter(nombre_raza = nombre)

    if not raza or len(raza) == 0:
        return None

    return raza.first()

def getvalidVacuna(nombre):
    vacuna = Vacuna.objects.filter(nombre_vacuna = nombre)

    if not vacuna or len(vacuna) == 0:
        return None
    
    return vacuna.first()


def getvalidFrecuencia(nombre):
    frecuencia = Frecuencia.objects.filter(nombre_frecuencia = nombre)

    if not frecuencia or len(frecuencia) == 0:
        return None
    
    return frecuencia

def getvalidHato(codigo):
    hato = Hato.objects.filter(codigo_hato)

    if not hato or len(hato) == 0:
        return None
    
    return hato.first()