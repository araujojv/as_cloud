import requests

BASE_URL = "http://127.0.0.1:8000"  # URL base da API

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    payload = {"nome": nome, "email": email}
    response = requests.post(f"{BASE_URL}/usuarios/", json=payload)
    print(response.json())

def listar_usuarios():
    response = requests.get(f"{BASE_URL}/usuarios/")
    print(response.json())

def criar_playlist():
    nome_playlist = input("Digite o nome da playlist: ")
    usuario_id = input("Digite o ID do usuário: ")
    payload = {"nome": nome_playlist, "usuario_id": usuario_id, "musicas": []}
    response = requests.post(f"{BASE_URL}/playlists/", json=payload)
    print(response.json())

def listar_playlists():
    usuario_id = input("Digite o ID do usuário: ")
    response = requests.get(f"{BASE_URL}/playlists/{usuario_id}")
    print(response.json())

def adicionar_musica():
    titulo = input("Digite o título da música: ")
    artista = input("Digite o artista da música: ")
    album = input("Digite o álbum da música: ")
    payload = {"titulo": titulo, "artista": artista, "album": album}
    response = requests.post(f"{BASE_URL}/musicas/", json=payload)
    print(response.json())

def listar_musicas():
    response = requests.get(f"{BASE_URL}/musicas/")
    print(response.json())

def menu():
    while True:
        print("\nMenu de Operações:")
        print("1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Criar Playlist")
        print("4. Listar Playlists")
        print("5. Adicionar Música")
        print("6. Listar Músicas")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_usuario()
        elif escolha == "2":
            listar_usuarios()
        elif escolha == "3":
            criar_playlist()
        elif escolha == "4":
            listar_playlists()
        elif escolha == "5":
            adicionar_musica()
        elif escolha == "6":
            listar_musicas()
        elif escolha == "7":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
