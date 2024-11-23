import React, { useEffect, useState } from 'react';
import { fetchPostsByUser, fetchComments } from '../wrapper';
import { List, ListItem, ListItemText, Typography, CircularProgress, Box, Divider } from '@mui/material';

function Posts({ userId }) {
  const [posts, setPosts] = useState([]);
  const [selectedPost, setSelectedPost] = useState(null);
  const [comments, setComments] = useState([]);
  const [loadingPosts, setLoadingPosts] = useState(false);
  const [loadingComments, setLoadingComments] = useState(false);

  useEffect(() => {
    const getPosts = async () => {
      setLoadingPosts(true);
      const postsData = await fetchPostsByUser(userId);
      setPosts(postsData);
      setLoadingPosts(false);
    };
    getPosts();
  }, [userId]);

  const handlePostClick = async (post) => {
    setSelectedPost(post);
    setLoadingComments(true);
    const commentsData = await fetchComments(post.id);
    setComments(commentsData);
    setLoadingComments(false);
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Posts de {userId ? `Usuário ${userId}` : 'Todos os Usuários'}
      </Typography>
      {loadingPosts ? (
        <CircularProgress />
      ) : (
        <List>
          {posts.map((post) => (
            <ListItem button key={post.id} onClick={() => handlePostClick(post)}>
              <ListItemText primary={post.title} secondary={post.body} />
            </ListItem>
          ))}
        </List>
      )}
      {selectedPost && (
        <Box sx={{ mt: 4 }}>
          <Typography variant="h5" gutterBottom>
            Comentários do Post: {selectedPost.title}
          </Typography>
          {loadingComments ? (
            <CircularProgress />
          ) : (
            <List>
              {comments.map((comment) => (
                <ListItem key={comment.id} alignItems="flex-start">
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
                  <Divider variant="inset" component="li" />
                </ListItem>
              ))}
            </List>
          )}
        </Box>
      )}
    </Box>
  );
}

export default Posts;
