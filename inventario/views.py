from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Raza, Vacuna, Hato, Bovino
from .helpers import getValidRaza, getvalidVacuna, getvalidFrecuencia
import json as js

# Create your views here.

def inventarioview(request):
    return render(request,"inventario/index.html")

def getHatos(request):
    
    hatos = Hato.objects.all()
    parametro = request.GET.get("q")

    if parametro:
        hatos = hatos.filter(codigo_hato__contains = parametro)

    data = []
    hatos = list(hatos)

    for hato in hatos:
        temp = {"codigo":hato.codigo_hato}
        data.append(temp)    
    
    data = js.dumps(data)

    return HttpResponse(data)

def getRazas(request):

    razas =Raza.objects.all()
    parametro = request.GET.get("q")

    if parametro:
        razas = razas.filter(nombre_raza__contains=parametro)
    
    data = []
    razas = list(razas)

    for raza in razas:
        temp = {"nombre": raza.nombre_raza}
        data.append(temp)
    
    data = js.dumps(data)

    return HttpResponse(data)


def getVacunas(request):

    vacunas = Vacuna.objects.all()
    parametro = request.GET.get("q")

    if parametro:
        vacunas = vacunas.filter(nombre_vacuna__contains=q)
    
    data = []
    vacunas = list(vacunas)

    for vacuna in vacunas:
        temp = {"nombre":vacuna.nombre_vacuna}
        data.append(temp)

    data = js.dumps(data)

    return HttpResponse(data)

def getBovinos(request):

    hato = request.GET.get("hato")
    hato = Hato.objects.filter(codigo_hato = hato).first()

    bovinos = list(Bovino.objects.filter(hato_bovino = hato))
    data = []

    for bovino in bovinos:
        temp = {
            "codigo": bovino.codigo_bovino,
            "hato": bovino.hato_bovino.codigo_hato,
            "vacunas": bovino.display_vacunas(),
            "partos": bovino.partos,
            "ultimo_parto": bovino.display_ultimo_parto(),
            "celos": bovino.display_fecha_celos()
        }

        data.append(temp)
        
    print(data)
    data = js.dumps(data)

    return HttpResponse(data)
    

def agregar_raza(request):
    if request.method == "GET":
        return HttpResponse("Aqui deberia haber una plantilla de raza")
    else:
        pass

def agregar_vacuna(request):
    if request.method == "GET":
        return HttpResponse("Aqui deberia haber una plantilla de vacunas")
    else:
        pass

def agregar_hato(request):
    if request.method == "GET":
        return HttpResponse("Aqui deberia haber una plantilla de ")
    else:
        pass


def agregar_bovino(request):
    if request.method == "GET":
        return render(request, "inventario/agregarbovino.html")
    else:
        # Variables obtenidas de formulario
        codigo = request.POST.get("codigobovino")

        # validar y obtener Hato
        hato_codigo = request.POST.get("hatosbovino")
        hato = getvalidHato(hato_codigo)

        if not hato or len(hato_codigo) == 0:
            return HttpResponseBadRequest("El hato no es valido")

        # Validar y obtener raza
        raza_nombre = request.POST.get("razabovino")
        raza = getValidRaza(raza_nombre)

        if not raza or len(raza_nombre) == 0:
            return HttpResponseBadRequest("La raza escogida no es valida")

        # Valida r y obtener vacuna 
        vacuna_nombre = request.POST.get("vacunasbovino")
        vacuna  =  getvalidVacuna(vacuna_nombre)

        if not vacuna or len(vacuna_nombre) == 0:
            return HttpResponseBadRequest(f"La vacuna {vacuna_nombre} es invalida")

        fecha_vacuna = request.POST.get("fechavacunabovino")
        fecha_ultimop = request.POST.get("fechaultimopartobovino")
        fecha_ultimo_celos = request.POST.get("fechaultimocelobovino")

        NBovino = Bovino()
        NBovino.codigo_bovino = codigo
        NBovino.raza_bovino = raza
        NBovino.hato = hato
        NBovino.partos = 1
        NBovino.ultima_vacuna = fecha_vacuna
        NBovino.ultimo_parto = fecha_ultimop
        NBovino.fecha_celos = NBovino.fecha_ultimo_celos

        NBovino.save()

        return HttpResponse(f"Bovino {codigo} agregado")


