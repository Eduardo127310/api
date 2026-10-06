from database.database import consultar


def listar(termo, pagina):
    busca = "%" + termo + "%"
    parametros = (busca, busca, busca)

    condicao = """
        WHERE titulo LIKE %s
        OR ingredientes LIKE %s
        OR descricao LIKE %s
    """

    total = consultar(
        "SELECT COUNT(*) AS total FROM receitas " + condicao,
        parametros
    )[0]["total"]

    receitas = consultar("""
        SELECT r.*, u.nome AS autor
        FROM receitas r
        JOIN usuarios u ON u.id = r.usuario_id
    """ + condicao + """
        ORDER BY r.id
        LIMIT 5 OFFSET %s
    """, parametros + ((pagina - 1) * 5,))

    return receitas, total


def listar_por_usuario(usuario_id):
    return consultar(
        "SELECT * FROM receitas WHERE usuario_id = %s",
        (usuario_id,)
    )
