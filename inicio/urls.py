
from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.index),
    path("login", views.login_view),
    path("logout", views.logout_view)
]
