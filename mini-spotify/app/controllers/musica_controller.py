from app.services.db import ref


def adicionar_musica_na_playlist(playlist_id, musica):
    """
    Adiciona uma música diretamente a uma playlist.

    Args:
        playlist_id: ID da playlist onde a música será adicionada.
        musica: Objeto contendo o título da música.

    Returns:
        dict: Mensagem de sucesso ou erro.
    """
    playlists_ref = ref.child("playlists").child(playlist_id)

    try:
        # Verifica se a playlist existe
        playlist = playlists_ref.get()
        if not playlist:
            raise ValueError(f"Playlist com ID {playlist_id} não encontrada.")

        # Adiciona a música na lista de músicas da playlist
        musicas = playlist.get("musicas", [])
        nova_musica = {
            "titulo": musica.titulo
        }
        musicas.append(nova_musica)

        # Atualiza a playlist no banco
        playlists_ref.update({"musicas": musicas})

        return {"mensagem": f"Música '{musica.titulo}' adicionada com sucesso à playlist {playlist_id}."}

    except Exception as e:
        print(f"Erro ao adicionar música: {e}")
        raise ValueError(f"Erro ao adicionar música: {str(e)}")
