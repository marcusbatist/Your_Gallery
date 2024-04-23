from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def register_usuario(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username') 
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('já existe um usuário com esse username')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse('usuário registrado com sucesso')

def login_usuario(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            login_django(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('Email ou Password inválidos')

