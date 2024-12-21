// URL base da API Django
const API_URL = 'http://127.0.0.1:8000/';  // Substitua com a URL real da sua API

// Função para pegar todos os artistas
function getArtistas() {
    fetch(`${API_URL}artistas/`)
        .then(response => response.json())
        .then(data => {
            displayArtistas(data);
        })
        .catch(error => {
            console.error('Erro ao buscar artistas:', error);
        });
}

// Função para exibir os artistas na tela
function displayArtistas(artistas) {
    const container = document.getElementById('artistas-container');
    container.innerHTML = '';  // Limpar qualquer conteúdo anterior

    if (artistas.length === 0) {
        container.innerHTML = '<p>Nenhum artista encontrado.</p>';
        return;
    }

    artistas.forEach(artista => {
        // Criar um novo elemento HTML para cada artista
        const artistaDiv = document.createElement('div');
        artistaDiv.classList.add('item');
        artistaDiv.onclick = () => getAlbuns(artista.id);

        // Adicionar conteúdo ao elemento
        artistaDiv.innerHTML = `
            <h3>${artista.nome}</h3>
            <p><strong>Local:</strong> ${artista.local}</p>
            <p><strong>Ano de Criação:</strong> ${artista.ano_criacao}</p>
        `;

        // Adicionar o novo elemento ao container
        container.appendChild(artistaDiv);
    });
}

// Função para pegar os álbuns de um artista
function getAlbuns(artistaId) {
    const albunsContainer = document.getElementById('albuns-container');
    albunsContainer.innerHTML = 'Carregando álbuns...';  // Mensagem enquanto carrega

    fetch(`${API_URL}albuns/?artista=${artistaId}`)
        .then(response => response.json())
        .then(data => {
            displayAlbuns(data);
        })
        .catch(error => {
            console.error('Erro ao buscar álbuns:', error);
            albunsContainer.innerHTML = 'Erro ao carregar álbuns.';
        });
}

// Função para exibir os álbuns de um artista na tela
function displayAlbuns(albuns) {
    const albunsContainer = document.getElementById('albuns-container');
    albunsContainer.innerHTML = '';  // Limpar mensagem de carregamento

    if (albuns.length === 0) {
        albunsContainer.innerHTML = '<p>Este artista não possui álbuns.</p>';
        return;
    }

    albuns.forEach(album => {
        const albumDiv = document.createElement('div');
        albumDiv.classList.add('album');
        albumDiv.onclick = () => getMusicas(album.id);
        albumDiv.innerHTML = `
            <h3>${album.nome}</h3>
            <p><strong>Ano:</strong> ${album.ano}</p>
        `;
        albunsContainer.appendChild(albumDiv);
    });
}

// Função para pegar as músicas de um álbum
function getMusicas(albumId) {
    const musicasContainer = document.getElementById('musicas-container');
    musicasContainer.innerHTML = 'Carregando músicas...';  // Mensagem enquanto carrega

    fetch(`${API_URL}musicas/?album=${albumId}`)
        .then(response => response.json())
        .then(data => {
            displayMusicas(data);
        })
        .catch(error => {
            console.error('Erro ao buscar músicas:', error);
            musicasContainer.innerHTML = 'Erro ao carregar músicas.';
        });
}

// Função para exibir as músicas de um álbum na tela
function displayMusicas(musicas) {
    const musicasContainer = document.getElementById('musicas-container');
    musicasContainer.innerHTML = '';  // Limpar mensagem de carregamento

    if (musicas.length === 0) {
        musicasContainer.innerHTML = '<p>Este álbum não possui músicas.</p>';
        return;
    }

    musicas.forEach(musica => {
        const musicaDiv = document.createElement('div');
        musicaDiv.classList.add('musica');
        musicaDiv.innerHTML = `
            <p><strong>Música:</strong> ${musica.nome}</p>
            <p><strong>Duração:</strong> ${musica.segundos} segundos</p>
        `;
        musicasContainer.appendChild(musicaDiv);
    });
}

// Função para enviar o formulário de cadastro de artista
function submitForm(event) {
    event.preventDefault();

    const nome = document.getElementById('nome').value;
    const local = document.getElementById('local').value;
    const anoCriacao = document.getElementById('ano_criacao').value;

    const artistaData = {
        nome: nome,
        local: local,
        ano_criacao: anoCriacao
    };

    fetch(`${API_URL}artistas/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(artistaData)
    })
    .then(response => response.json())
    .then(data => {
        alert('Artista cadastrado com sucesso!');
        document.getElementById('form-artista').reset();  // Limpar formulário
        getArtistas();  // Atualizar lista de artistas
    })
    .catch(error => {
        console.error('Erro ao cadastrar artista:', error);
        alert('Erro ao cadastrar artista.');
    });
}

// Chamar a função para obter os artistas quando a página carregar
window.onload = getArtistas;