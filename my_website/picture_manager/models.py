# Create your models here.

# No arquivo models.py do seu aplicativo picture_manager

from pydantic import BaseModel

class Photo(BaseModel):
    title: str
    description: str
    image: str

