
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

export async function fetchPosts(userId) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}/posts`);
    const posts = await response.json();
    return posts;
  } catch (error) {
    console.error('Erro ao buscar posts do usuário:', error);
    return [];
  }
}


export async function fetchComments(postId) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}/comments`);
    const comments = await response.json();
    return comments;
  } catch (error) {
    console.error('Erro ao buscar comentários do post:', error);
    return [];
  }
}
