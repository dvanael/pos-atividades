import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Albums from './pages/Albums';
import Posts from './pages/Posts';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';

function App() {
  return (
    <Router>
      <AppBar position="static" sx={{ mb: 4 }}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Galeria de Álbuns e Posts
          </Typography>
          <Button color="inherit" component={Link} to="/">
            Home
          </Button>
          <Button color="inherit" component={Link} to="/albums">
            Álbuns
          </Button>
          <Button color="inherit" component={Link} to="/posts">
            Posts
          </Button>
        </Toolbar>
      </AppBar>
      <Box sx={{ px: 2 }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/albums" element={<Albums />} />
          <Route path="/posts" element={<Posts />} />
        </Routes>
      </Box>
    </Router>
  );
}

function Home() {
  return (
    <Typography variant="h3" align="center">
      Meu deus que prequiça e tristeza
    </Typography>
  );
}

export default App;
