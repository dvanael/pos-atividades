import React, { useEffect, useState } from 'react';
import { fetchUsers, fetchPosts, fetchComments } from '../wrapper';
import { List, ListItem, ListItemText, Typography, CircularProgress, Box, Divider } from '@mui/material';

function Posts() {
  const [users, setUsers] = useState([]);
  const [posts, setPosts] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [selectedPost, setSelectedPost] = useState(null);
  const [comments, setComments] = useState([]);
  const [loadingUsers, setLoadingUsers] = useState(false);
  const [loadingPosts, setLoadingPosts] = useState(false);
  const [loadingComments, setLoadingComments] = useState(false);

  // Carregar a lista de usuários
  useEffect(() => {
    const getUsers = async () => {
      setLoadingUsers(true);
      const usersData = await fetchUsers();
      setUsers(usersData);
      setLoadingUsers(false);
    };
    getUsers();
  }, []);

  // Carregar os posts do usuário selecionado
  const handleUserClick = async (userId) => {
    setSelectedUser(userId);
    setLoadingPosts(true);
    const postsData = await fetchPosts(userId);
    setPosts(postsData);
    setSelectedPost(null); // Resetar post selecionado
    setLoadingPosts(false);
  };

  // Carregar os comentários do post selecionado
  const handlePostClick = async (post) => {
    setSelectedPost(post);
    setLoadingComments(true);
    const commentsData = await fetchComments(post.id);
    setComments(commentsData);
    setLoadingComments(false);
  };

  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h4" gutterBottom>
        Posts de Usuários
      </Typography>

      {/* Lista de usuários */}
      <Box>
        <Typography variant="h6">Usuários:</Typography>
        {loadingUsers ? (
          <CircularProgress />
        ) : (
          <List>
            {users.map((user) => (
              <ListItem
                key={user.id}
                component="button"
                sx={{ cursor: 'pointer' }}
                onClick={() => handleUserClick(user.id)}
              >
                <ListItemText primary={user.name} />
              </ListItem>
            ))}
          </List>
        )}
      </Box>

      {/* Mostrar posts do usuário selecionado */}
      {selectedUser && (
        <Box sx={{ marginTop: 4 }}>
          <Typography variant="h5" gutterBottom>
            Posts de {users.find((user) => user.id === selectedUser)?.name}
          </Typography>
          {loadingPosts ? (
            <CircularProgress />
          ) : (
            <List>
              {posts.map((post) => (
                <ListItem
                  key={post.id}
                  component="button"
                  sx={{ cursor: 'pointer' }}
                  onClick={() => handlePostClick(post)}
                >
                  <ListItemText
                    primary={post.title}
                    secondary={post.body}
                  />
                </ListItem>
              ))}
            </List>
          )}
        </Box>
      )}
      {/* Mostrar comentários do post selecionado */}
      {selectedPost && (
        <Box sx={{ marginTop: 4 }}>
          <Typography variant="h5" gutterBottom>
            Comentários do Post: {selectedPost.title}
          </Typography>
          {loadingComments ? (
            <CircularProgress />
          ) : (
            <List>
              {comments.map((comment, index) => (
                <React.Fragment key={comment.id}>
                  <ListItem alignItems="flex-start">
                    <ListItemText
                      primary={comment.name}
                      secondary={
                        <>
                          <Typography component="span" variant="body2" color="textPrimary">
                            {comment.email}
                          </Typography>
                          {' — '}
                          {comment.body}
                        </>
                      }
                    />
                  </ListItem>
                  {/* Adicionando Divider fora do ListItem */}
                  {index < comments.length - 1 && <Divider variant="inset" component="li" />}
                </React.Fragment>
              ))}
            </List>
          )}
        </Box>
      )}
    </Box>
  );
}

export default Posts;
