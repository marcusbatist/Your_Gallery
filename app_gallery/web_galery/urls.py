# web_galery/urls.py
from django.urls import path
from . import views

app_name = 'web_galery'

urlpatterns = [
    # URLs para a galeria de fotos
    path('', views.index, name='index'),  # Página inicial
    path('gallery/', views.view_gallery, name='view_gallery'),  # Página da galeria
    path('add_photo/', views.add_photo, name='add_photo'),      # Adicionar foto
    path('delete_photo/<int:photo_id>/', views.delete_photo, name='delete_photo'),  # Deletar foto

    # URLs para autenticação de usuários
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),       # URL para a página de login
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),  # URL para a página de registro
]
