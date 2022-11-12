from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def reportesview(request):
    return HttpResponse("Plantilla de reportes")