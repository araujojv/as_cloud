import os
import firebase_admin
from firebase_admin import credentials, db

# Configurar Firebase com o JSON da conta de serviço
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Diretório atual
JSON_PATH = os.path.join(BASE_DIR, "mini-spotify-4df49-firebase-adminsdk-zls0r-06224b2578.json")

if not os.path.exists(JSON_PATH):
    raise FileNotFoundError(f"Arquivo JSON não encontrado: {JSON_PATH}")

cred = credentials.Certificate(JSON_PATH)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mini-spotify-4df49-default-rtdb.firebaseio.com/'
})

# Referência à raiz do banco
ref = db.reference('/')

# Funções para Usuários
def criar_usuario(nome, email):
    if not nome or not email:
        print("Nome e email são obrigatórios.")
        return

    usuarios_ref = ref.child("usuarios")
    novo_usuario = usuarios_ref.push({
        "nome": nome,
        "email": email
    })
    print(f"Usuário criado com ID: {novo_usuario.key}")

def listar_usuarios():
    usuarios_ref = ref.child("usuarios")
    usuarios = usuarios_ref.get()
    if usuarios:
        print("Usuários cadastrados:")
        for key, value in usuarios.items():
            print(f"ID: {key}, Nome: {value['nome']}, Email: {value['email']}")
    else:
        print("Nenhum usuário encontrado.")

def atualizar_usuario(usuario_id, novo_email):
    if not usuario_id or not novo_email:
        print("ID do usuário e novo email são obrigatórios.")
        return

    usuarios_ref = ref.child("usuarios")
    if usuarios_ref.child(usuario_id).get() is None:
        print(f"Usuário com ID {usuario_id} não encontrado.")
        return

    usuarios_ref.child(usuario_id).update({
        "email": novo_email
    })
    print(f"Usuário com ID {usuario_id} atualizado com sucesso.")

def excluir_usuario(usuario_id):
    if not usuario_id:
        print("ID do usuário é obrigatório.")
        return

    usuarios_ref = ref.child("usuarios")
    if usuarios_ref.child(usuario_id).get() is None:
        print(f"Usuário com ID {usuario_id} não encontrado.")
        return

    usuarios_ref.child(usuario_id).delete()
    print(f"Usuário com ID {usuario_id} excluído com sucesso.")

# Funções para Playlists
def criar_playlist(nome_playlist, usuario_id):
    if not nome_playlist or not usuario_id:
        print("Nome da playlist e ID do usuário são obrigatórios.")
        return

    playlists_ref = ref.child("playlists")
    nova_playlist = playlists_ref.push({
        "nome": nome_playlist,
        "usuario_id": usuario_id,
        "musicas": []  # Lista de músicas vazia inicialmente
    })
    print(f"Playlist criada com ID: {nova_playlist.key}")

def listar_playlists(usuario_id):
    if not usuario_id:
        print("ID do usuário é obrigatório.")
        return

    playlists_ref = ref.child("playlists")
    playlists = playlists_ref.order_by_child("usuario_id").equal_to(usuario_id).get()
    if playlists:
        print(f"Playlists do Usuário {usuario_id}:")
        for key, value in playlists.items():
            print(f"ID: {key}, Nome: {value['nome']}, Músicas: {len(value['musicas'])}")
    else:
        print("Nenhuma playlist encontrada para este usuário.")

# Funções para Músicas
def adicionar_musica(titulo, artista, album):
    if not titulo or not artista or not album:
        print("Título, artista e álbum são obrigatórios.")
        return

    musicas_ref = ref.child("musicas")
    nova_musica = musicas_ref.push({
        "titulo": titulo,
        "artista": artista,
        "album": album
    })
    print(f"Música adicionada com ID: {nova_musica.key}")

def listar_musicas():
    musicas_ref = ref.child("musicas")
    musicas = musicas_ref.get()
    if musicas:
        print("Músicas disponíveis:")
        for key, value in musicas.items():
            print(f"ID: {key}, Título: {value['titulo']}, Artista: {value['artista']}, Álbum: {value['album']}")
    else:
        print("Nenhuma música encontrada.")

def adicionar_musica_na_playlist(playlist_id, musica_id):
    if not playlist_id or not musica_id:
        print("ID da playlist e ID da música são obrigatórios.")
        return

    playlists_ref = ref.child("playlists")
    playlist = playlists_ref.child(playlist_id).get()
    if not playlist:
        print(f"Playlist com ID {playlist_id} não encontrada.")
        return

    if "musicas" not in playlist:
        playlist["musicas"] = []

    if musica_id in playlist["musicas"]:
        print("Música já está na playlist.")
        return

    playlist["musicas"].append(musica_id)
    playlists_ref.child(playlist_id).update({"musicas": playlist["musicas"]})
    print(f"Música {musica_id} adicionada à playlist {playlist_id}")

# Menu de Operações
if __name__ == "__main__":
    while True:
        print("\nMenu de Operações:")
        print("1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Criar Playlist")
        print("4. Listar Playlists")
        print("5. Adicionar Música")
        print("6. Listar Músicas")
        print("7. Adicionar Música na Playlist")
        print("8. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            criar_usuario(nome, email)
        elif escolha == "2":
            listar_usuarios()
        elif escolha == "3":
            nome_playlist = input("Digite o nome da playlist: ")
            usuario_id = input("Digite o ID do usuário: ")
            criar_playlist(nome_playlist, usuario_id)
        elif escolha == "4":
            usuario_id = input("Digite o ID do usuário: ")
            listar_playlists(usuario_id)
        elif escolha == "5":
            titulo = input("Digite o título da música: ")
            artista = input("Digite o nome do artista: ")
            album = input("Digite o nome do álbum: ")
            adicionar_musica(titulo, artista, album)
        elif escolha == "6":
            listar_musicas()
        elif escolha == "7":
            playlist_id = input("Digite o ID da playlist: ")
            musica_id = input("Digite o ID da música: ")
            adicionar_musica_na_playlist(playlist_id, musica_id)
        elif escolha == "8":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
