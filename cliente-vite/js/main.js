
import { fetchUsers, fetchAlbums, fetchPhotos } from './wrapper.js';

document.getElementById('fetchUsersBtn').addEventListener('click', async () => {
  const usersList = document.getElementById('usersList');
  usersList.innerHTML = 'Carregando...';
  
  const users = await fetchUsers();
  usersList.innerHTML = '';
  users.forEach(user => {
    usersList.innerHTML += `
      <div data-user-id="${user.id}" data-user-name="${user.name}" class="item user">
        <p class="list-item">${user.name}</p>
      </div>
    `;
  });

  document.querySelectorAll('.user').forEach(userDiv => {
    userDiv.addEventListener('click', async () => {
      const albumsList = document.getElementById('albumsList');
      albumsList.innerHTML = 'Carregando...';
      
      const userId = userDiv.dataset.userId;
      const userName = userDiv.dataset.userName;
      const albums = await fetchAlbums(userId);
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
        albumDiv.addEventListener('click', async () => {
          const photosList = document.getElementById('photosList');
          photosList.innerHTML = 'Carregando...';

          const albumId = albumDiv.dataset.albumId;
          const albumTitle = albumDiv.dataset.albumTitle;
          const photos = await fetchPhotos(albumId);
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
        });
      });
    });
  });
});
