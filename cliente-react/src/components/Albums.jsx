import React, { useEffect, useState } from 'react';
import { fetchAlbums } from '../wrapper';
import { List, ListItem, ListItemButton, ListItemText } from '@mui/material';

function Albums({ userId, onSelectAlbum }) {
  const [albums, setAlbums] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const getAlbums = async () => {
      setLoading(true);
      const albumsData = await fetchAlbums(userId);
      setAlbums(albumsData);
      setLoading(false);
    };
    getAlbums();
  }, [userId]);

  return (
    <div>
      {loading ? (
        <p>Carregando álbuns...</p>
      ) : (
        <List>
          {albums.map((album) => (
            <ListItem key={album.id} disablePadding>
              <ListItemButton onClick={() => onSelectAlbum(album)}>
                <ListItemText primary={album.title} />
              </ListItemButton>
            </ListItem>
          ))}
        </List>
      )}
    </div>
  );
}

export default Albums;
