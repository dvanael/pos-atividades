import React, { useEffect, useState } from 'react';
import { fetchUsers } from '../wrapper';
import { Button, List, ListItem, ListItemButton, ListItemText } from '@mui/material';

function Users({ onSelectUser }) {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const getUsers = async () => {
      setLoading(true);
      const usersData = await fetchUsers();
      setUsers(usersData);
      setLoading(false);
    };
    getUsers();
  }, []);

  return (
    <div>
      <Button
        variant="contained"
        color="primary"
        onClick={() => fetchUsers()}
        disabled={loading}
        sx={{ mb: 2 }}
      >
        {loading ? 'Carregando...' : 'Buscar Usuários'}
      </Button>
      <List>
        {users.map((user) => (
          <ListItem key={user.id} disablePadding>
            <ListItemButton onClick={() => onSelectUser(user)}>
              <ListItemText primary={user.name} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </div>
  );
}

export default Users;
