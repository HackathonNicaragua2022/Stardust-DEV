from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def reportesview(request):
    return render(request, "reportes/index.html")