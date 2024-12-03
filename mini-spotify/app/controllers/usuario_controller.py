from app.services.db import ref

def criar_usuario(usuario):
    """
    Cria um novo usuário com um ID incremental.

    Args:
        usuario: Objeto contendo os dados do usuário (nome e email).

    Returns:
        dict: Mensagem de sucesso e ID do usuário criado.
    """
    usuarios_ref = ref.child("usuarios")
    controle_ref = ref.child("last_user_id")

    try:
        # Obtém o último ID gerado
        last_user_id = controle_ref.get()
        if not last_user_id:  # Caso seja o primeiro usuário
            last_user_id = 0

        # Incrementa o ID
        novo_id = last_user_id + 1

        # Verifica se o email já está cadastrado
        usuarios_existentes = usuarios_ref.get()
        if usuarios_existentes:
            for key, value in usuarios_existentes.items():
                if value["email"] == usuario.email:
                    raise ValueError(f"O email '{usuario.email}' já está cadastrado.")

        # Cria o novo usuário com o ID incremental
        usuarios_ref.child(str(novo_id)).set({
            "nome": usuario.nome,
            "email": usuario.email
        })

        # Atualiza o último ID no banco
        controle_ref.set(novo_id)

        return {"id": novo_id, "mensagem": "Usuário criado com sucesso"}

    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        raise ValueError(f"Erro ao criar usuário: {str(e)}")


def listar_usuarios():
    """
    Retorna uma lista de todos os usuários cadastrados.

    Returns:
        list: Lista de usuários ou mensagem indicando que não há usuários.
    """
    usuarios_ref = ref.child("usuarios")

    try:
        usuarios = usuarios_ref.get()

        if not usuarios:
            return {"mensagem": "Nenhum usuário encontrado"}

        # Converte os dados para uma lista de dicionários
        result = [{"id": key, **value} for key, value in usuarios.items()]
        print(f"Usuários encontrados: {result}")
        return result

    except Exception as e:
        print(f"Erro ao listar usuários: {e}")
        raise ValueError(f"Erro ao listar usuários: {str(e)}")
