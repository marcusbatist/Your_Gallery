from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Photo(BaseModel):
    id: int
    title: str
    description: str
    image: str

photos_db = []

@app.get("/photos/", response_model=List[Photo])
async def read_photos():
    return photos_db

@app.post("/photos/", response_model=Photo)
async def create_photo(photo: Photo):
    photos_db.append(photo)
    return photo

@app.get("/photos/{photo_id}", response_model=Photo)
async def read_photo(photo_id: int):
    for photo in photos_db:
        if photo.id == photo_id:
            return photo
    raise HTTPException(status_code=404, detail="Photo not found")

@app.put("/photos/{photo_id}", response_model=Photo)
async def update_photo(photo_id: int, photo: Photo):
    for index, existing_photo in enumerate(photos_db):
        if existing_photo.id == photo_id:
            photos_db[index] = photo
            return photo
    raise HTTPException(status_code=404, detail="Photo not found")

@app.delete("/photos/{photo_id}")
async def delete_photo(photo_id: int):
    for index, photo in enumerate(photos_db):
        if photo.id == photo_id:
            del photos_db[index]
            return {"message": "Photo deleted successfully"}
    raise HTTPException(status_code=404, detail="Photo not found")
