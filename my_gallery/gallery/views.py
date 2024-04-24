from django.shortcuts import render
from .models import Photo
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login")
def gallery_view(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/gallery.html', {'photos': photos})

