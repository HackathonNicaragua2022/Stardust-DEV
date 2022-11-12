from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request, "inicio/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("NODO")
        return HttpResponse("TODO")
    
    return render(request, "inicio/login.html")

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect("/login")



