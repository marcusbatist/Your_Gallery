from django.shortcuts import render
from .models import Photo
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login")
def gallery_view(request):
    if request.method == 'POST':
        
        photo = request.FILES.get('photo')

        
        new_photo = Photo(image=photo)
        new_photo.save()

    
    photos = Photo.objects.all()

    
    return render(request, 'gallery/gallery.html', {'photos': photos})

