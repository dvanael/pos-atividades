document.getElementById('fetchUsersBtn').addEventListener('click', fetchUsers);

async function fetchUsers() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    const users = await response.json();
    const usersList = document.getElementById('usersList');
    usersList.innerHTML = '';
    users.forEach(user => {
      usersList.innerHTML += `
        <div data-user-id="${user.id}" data-user-name="${user.name}" class="item user">
          <p class="list-item" >${user.name}</p>
        </div>
      `;
    });
    document.querySelectorAll('.user').forEach(userDiv => {
      userDiv.addEventListener('click', () => fetchAlbums(userDiv.dataset.userId, userDiv.dataset.userName));
    });
  } catch (error) {
    console.error('Erro ao buscar usuários:', error);
  }
}

async function fetchAlbums(userId, userName) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}/albums`);
    const albums = await response.json();
    const albumsList = document.getElementById('albumsList');
    const userNameSpan = document.getElementById('userName');
    albumsList.innerHTML = '';
    userNameSpan.textContent = userName;
    albums.forEach(album => {
      albumsList.innerHTML += `
        <div data-album-id="${album.id}" data-album-title="${album.title}" class="item album">
          <p class="list-item">${album.title}</p>
        </div>
      `;
    });
    document.querySelectorAll('.album').forEach(albumDiv => {
      albumDiv.addEventListener('click', () => fetchPhotos(albumDiv.dataset.albumId, albumDiv.dataset.albumTitle));
    });
  } catch (error) {
    console.error('Erro ao buscar álbuns:', error);
  }
}

async function fetchPhotos(albumId, albumTitle) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/albums/${albumId}/photos`);
    const photos = await response.json();
    const photosList = document.getElementById('photosList');
    const albumTitleSpan = document.getElementById('albumTitle');
    photosList.innerHTML = '';
    albumTitleSpan.textContent = albumTitle;
    photos.forEach(photo => {
      const img = new Image();
      img.src = photo.thumbnailUrl;
      img.alt = photo.title;
      img.onload = () => {
        photosList.innerHTML += `<img src="${photo.thumbnailUrl}" alt="${photo.title}">`;
      };
    });
  } catch (error) {
    console.error('Erro ao buscar fotos:', error);
  }
}
