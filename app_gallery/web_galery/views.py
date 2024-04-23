# web_galery/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm, PhotoForm
from .models import Photo

# Função para exibir o perfil do usuário
def profile(request):
    # Aqui você pode acessar as informações do usuário autenticado usando request.user
    user = request.user
    return render(request, 'user/profile.html', {'user': user})

# Função para login do usuário
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('web_galery:profile')  # Redireciona para a página de perfil
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

# Função para logout do usuário
def user_logout(request):
    logout(request)
    return redirect('web_galery:login')

# Função para registro de novo usuário
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('web_galery:login')  # Redireciona para a página de login após o registro
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# Nova view para exibir a galeria de fotos
@login_required
def index(request):
    photos = Photo.objects.filter(uploaded_by=request.user)
    return render(request, 'gallery/index.html', {'photos': photos})

# Nova view para adicionar uma foto
@login_required
def add_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            return redirect('web_galery:index')
    else:
        form = PhotoForm()
    return render(request, 'gallery/upload_photo.html', {'form': form})

# Nova view para exibir uma foto específica
@login_required
def view_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'gallery/view_photo.html', {'photo': photo})

# Nova view para excluir uma foto
@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    if photo.uploaded_by == request.user:
        photo.delete()
    return redirect('web_galery:index')
