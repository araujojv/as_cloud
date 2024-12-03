from fastapi import FastAPI, HTTPException
from app.controllers import usuario_controller, playlist_controller, musica_controller
from app.models.usuario import Usuario
from app.models.playlist import Playlist
from app.models.musica import Musica

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem": "Bem-vindo ao Míni Spotify API!"}

# Endpoints de Usuários
@app.post("/usuarios/")
def criar_usuario(usuario: Usuario):
    try:
        return usuario_controller.criar_usuario(usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/usuarios/")
def listar_usuarios():
    try:
        return usuario_controller.listar_usuarios()
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoints de Playlists
@app.post("/playlists/")
def criar_playlist(playlist: Playlist):
    try:
        return playlist_controller.criar_playlist(playlist)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/playlists/{usuario_id}")
def listar_playlists(usuario_id: str):
    try:
        return playlist_controller.listar_playlists(usuario_id)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para adicionar músicas diretamente em uma playlist
@app.post("/playlists/{playlist_id}/musicas/")
def adicionar_musica_na_playlist(playlist_id: str, musica: Musica):
    try:
        return musica_controller.adicionar_musica_na_playlist(playlist_id, musica)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
