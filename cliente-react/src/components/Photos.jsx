import React, { useEffect, useState } from 'react';
import { fetchPhotos } from '../wrapper';
import { Grid, Card, CardMedia, CardContent, Typography } from '@mui/material';

function Photos({ albumId }) {
  const [photos, setPhotos] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const getPhotos = async () => {
      setLoading(true);
      const photosData = await fetchPhotos(albumId);
      setPhotos(photosData);
      setLoading(false);
    };
    getPhotos();
  }, [albumId]);

  return (
    <Grid container spacing={2}>
      {loading ? (
        <Typography variant="body1" align="center">
          Carregando fotos...
        </Typography>
      ) : (
        photos.map((photo) => (
          <Grid item xs={12} sm={6} md={4} key={photo.id}>
            <Card>
              <CardMedia
                component="img"
                height="140"
                image={photo.thumbnailUrl}
                alt={photo.title}
              />
              <CardContent>
                <Typography variant="body2">{photo.title}</Typography>
              </CardContent>
            </Card>
          </Grid>
        ))
      )}
    </Grid>
  );
}

export default Photos;
