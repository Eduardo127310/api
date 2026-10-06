from database.database import consultar


def listar(nome):
    return consultar(
        "SELECT * FROM usuarios WHERE nome LIKE %s",
        ("%" + nome + "%",)
    )


def buscar(usuario_id):
    return consultar(
        "SELECT * FROM usuarios WHERE id = %s",
        (usuario_id,)
    )
