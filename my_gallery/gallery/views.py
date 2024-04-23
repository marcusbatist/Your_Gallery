from django.shortcuts import render

def visualizar_gallery(request):
    return render(request, 'gallery.html')