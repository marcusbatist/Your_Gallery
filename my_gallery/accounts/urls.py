from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_usuario, name='register_usuario'),
    path('login/',views.login_usuario, name='login_usuario'),
    #ANCHOR - como fica para logout?
]

