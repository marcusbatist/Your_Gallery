document.addEventListener('DOMContentLoaded', () => {
    const photosDiv = document.getElementById('photos');
    const photoForm = document.getElementById('photoForm');

    // Função para carregar as fotos
    async function loadPhotos() {
        photosDiv.innerHTML = '';
        const response = await fetch('/api/photos/');
        const photos = await response.json();
        photos.forEach(photo => {
            const photoElement = document.createElement('div');
            photoElement.classList.add('photo');
            photoElement.innerHTML = `
                <h2>${photo.title}</h2>
                <p>${photo.description}</p>
                <img src="${photo.image}" alt="${photo.title}">
                <button onclick="deletePhoto(${photo.id})">Delete</button>
            `;
            photosDiv.appendChild(photoElement);
        });
    }

    // Função para adicionar uma nova foto
    async function addPhoto(event) {
        event.preventDefault();
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const image = document.getElementById('image').value;
        const response = await fetch('/api/photos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, description, image })
        });
        const newPhoto = await response.json();
        loadPhotos();
        photoForm.reset();
    }

    // Função para excluir uma foto
    async function deletePhoto(id) {
        await fetch(`/api/photos/${id}`, {
            method: 'DELETE'
        });
        loadPhotos();
    }

    // Carregar as fotos quando a página carregar
    loadPhotos();

    // Lidar com o envio do formulário para adicionar uma foto
    photoForm.addEventListener('submit', addPhoto);
});
