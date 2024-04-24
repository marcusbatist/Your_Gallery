from django.shortcuts import render
from .models import Photo

def gallery_view(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/gallery.html', {'photos': photos})

