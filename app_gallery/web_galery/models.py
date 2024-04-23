# web_gallery/models.py
from django.contrib.auth.models import User
from django.db import models

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo {self.id} - Uploaded by {self.user.username}'
