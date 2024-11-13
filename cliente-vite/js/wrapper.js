
export async function fetchUsers() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    const users = await response.json();
    return users;
  } catch (error) {
    console.error('Erro ao buscar usuários:', error);
  }
}

export async function fetchAlbums(userId) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}/albums`);
    const albums = await response.json();
    return albums;
  } catch (error) {
    console.error('Erro ao buscar álbuns:', error);
  }
}

export async function fetchPhotos(albumId) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/albums/${albumId}/photos`);
    const photos = await response.json();
    return photos;
  } catch (error) {
    console.error('Erro ao buscar fotos:', error);
  }
}
