from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.

def acceuil(request):
    #si utilisateur connecté, retourner carte
    if request.user.is_authenticated:
        return redirect('/carte')
    #sinon, retourner page de connexion
    else:
        return render(request,'login/acceuil.html')

def carte(request):
    #return render(request,'carte.html')
    pass

def connexion(request):
    if request.method == 'POST' and not request.user.is_authenticated:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/carte')

        else:
            error= {"error":"Les identifiants ne sont pas reconnus"}
    
            return render(request, 'login/acceuil.html', error)
    else:
        return(acceuil(request))

def inscription(request):
    return render(request,'login/inscription.html')

def deconnexion(request):
    try:
        if request.user.is_authenticated:
            logout(request)
            return(acceuil(request))
        else:
            return(acceuil(request))
    except NameError:
        return(acceuil(request))


def valider_inscription(request):
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.first_name=request.POST['first_name']
    user.last_name=request.POST['last_name']
    user.save()
    return (acceuil(request))

def compte(request):
    return render(request,'login/compte.html')