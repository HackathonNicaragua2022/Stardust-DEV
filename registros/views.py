from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def registrosview(request):
    return render(request, "registros/index.html")