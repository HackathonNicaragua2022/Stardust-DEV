from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inventarioview(request):
    return render(request,"inventario/index.html")

def getHatos(request):
    pass

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
        return HttpResponse("Aqui deberia haber una plantilla")
    else:
        pass
