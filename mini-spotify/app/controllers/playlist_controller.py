from app.services.db import ref


def criar_playlist(playlist):
    """
    Cria uma nova playlist no Firebase Realtime Database.

    Args:
        playlist: Objeto Playlist contendo nome, usuario_id e lista de músicas.

    Returns:
        dict: Mensagem de sucesso e ID da playlist criada.
    """
    playlists_ref = ref.child("playlists")

    try:
        # Criação de uma nova playlist
        nova_playlist = playlists_ref.push({
            "nome": playlist.nome,
            "usuario_id": playlist.usuario_id,
            "musicas": playlist.musicas or []  # Garante que "musicas" seja uma lista
        })

        print(f"Playlist criada com ID: {nova_playlist.key}")
        return {"id": nova_playlist.key, "mensagem": "Playlist criada com sucesso"}
    except Exception as e:
        print(f"Erro ao criar playlist: {e}")
        raise ValueError(f"Erro ao criar playlist: {str(e)}")


def listar_playlists(usuario_id):
    """
    Lista todas as playlists associadas a um usuário.

    Args:
        usuario_id (str): ID do usuário.

    Returns:
        list: Lista de playlists do usuário.
    """
    playlists_ref = ref.child("playlists")
    try:
        playlists = playlists_ref.order_by_child("usuario_id").equal_to(usuario_id).get()

        # Se nenhuma playlist for encontrada
        if not playlists:
            return {"mensagem": f"Nenhuma playlist encontrada para o usuário {usuario_id}"}

        # Retorna as playlists no formato correto
        result = [{"id": key, **value} for key, value in playlists.items()]
        print(f"Playlists encontradas para o usuário {usuario_id}: {result}")
        return result

    except Exception as e:
        print(f"Erro ao listar playlists para o usuário {usuario_id}: {e}")
        raise ValueError(f"Erro ao listar playlists: {str(e)}")


def deletar_playlist(playlist_id):
    """
    Deleta uma playlist com base no ID fornecido.

    Args:
        playlist_id (str): ID da playlist a ser deletada.

    Returns:
        dict: Mensagem de sucesso.
    """
    playlists_ref = ref.child("playlists")
    try:
        playlist = playlists_ref.child(playlist_id).get()
        if not playlist:
            raise ValueError(f"Playlist com ID {playlist_id} não encontrada.")

        playlists_ref.child(playlist_id).delete()
        print(f"Playlist com ID {playlist_id} deletada com sucesso.")
        return {"mensagem": f"Playlist com ID {playlist_id} deletada com sucesso."}
    except Exception as e:
        print(f"Erro ao deletar playlist {playlist_id}: {e}")
        raise ValueError(f"Erro ao deletar playlist: {str(e)}")
