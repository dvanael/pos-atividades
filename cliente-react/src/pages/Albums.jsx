import React, { useState } from 'react';
import Users from '../components/Users';
import Albums from '../components/Albums';
import Photos from '../components/Photos';
import { Typography, Box } from '@mui/material';

function AlbumsPage() {
  const [selectedUser, setSelectedUser] = useState(null);
  const [selectedAlbum, setSelectedAlbum] = useState(null);

  return (
    <Box>
      <Users onSelectUser={(user) => {
        setSelectedUser(user);
        setSelectedAlbum(null);
      }} />
      {selectedUser && (
        <Box>
          <Typography variant="h5" sx={{ mt: 4 }}>
            Álbuns de {selectedUser.name}
          </Typography>
          <Albums
            userId={selectedUser.id}
            onSelectAlbum={(album) => setSelectedAlbum(album)}
          />
        </Box>
      )}
      {selectedAlbum && (
        <Box>
          <Typography variant="h6" sx={{ mt: 4 }}>
            Fotos do Álbum: {selectedAlbum.title}
          </Typography>
          <Photos albumId={selectedAlbum.id} />
        </Box>
      )}
    </Box>
  );
}

export default AlbumsPage;
