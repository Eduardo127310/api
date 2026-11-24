from database.database import consultar, executar


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

    # DESC: as receitas mais novas aparecem primeiro
    receitas = consultar("""
        SELECT r.*, u.nome AS autor
        FROM receitas r
        JOIN usuarios u ON u.id = r.usuario_id
    """ + condicao + """
        ORDER BY r.id DESC
        LIMIT 5 OFFSET %s
    """, parametros + ((pagina - 1) * 5,))

    return receitas, total


def listar_por_usuario(usuario_id):
    return consultar(
        "SELECT * FROM receitas WHERE usuario_id = %s",
        (usuario_id,)
    )


def inserir(receita, usuario_id):
    return executar("""
        INSERT INTO receitas (titulo, descricao, ingredientes, modo_preparo, usuario_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        receita["titulo"],
        receita["descricao"],
        receita["ingredientes"],
        receita["modo_preparo"],
        usuario_id
    ))
