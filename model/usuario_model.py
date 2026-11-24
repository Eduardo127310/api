from database.database import consultar


# Nunca selecionamos a coluna "senha" nas rotas públicas
def listar(nome):
    return consultar(
        "SELECT id, nome FROM usuarios WHERE nome LIKE %s",
        ("%" + nome + "%",)
    )


def buscar(usuario_id):
    return consultar(
        "SELECT id, nome, email FROM usuarios WHERE id = %s",
        (usuario_id,)
    )


# Usada só no login, porque precisa do hash da senha para comparar
def buscar_por_email(email):
    return consultar(
        "SELECT id, nome, senha FROM usuarios WHERE email = %s",
        (email,)
    )
