from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title
