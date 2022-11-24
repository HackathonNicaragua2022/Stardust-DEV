
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inventarioview),
    path("get_hatos", views.getHatos),
    path("get_razas", views.getRazas),
    path("get_vacunas", views.getVacunas),
    path("get_bovinos", views.getBovinos),
    path("agregarbovino", views.agregar_bovino),

]
