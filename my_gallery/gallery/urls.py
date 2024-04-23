from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualizar_gallery, name='visualizar_gallery'),

]
