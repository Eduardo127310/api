from database.database import consultar


def listar(termo, pagina):
    filtro = "%" + termo + "%"
    parametros = (filtro, filtro, filtro)
    condicao = "WHERE titulo LIKE %s OR ingredientes LIKE %s OR descricao LIKE %s"

    total = consultar("SELECT COUNT(*) AS total FROM receitas " + condicao,
                      parametros)[0]["total"]

    receitas = consultar("""
        SELECT r.*, u.nome AS autor
        FROM receitas r JOIN usuarios u ON u.id = r.usuario_id
    """ + condicao + " ORDER BY r.id LIMIT %s OFFSET %s",
        parametros + (5, (pagina - 1) * 5))

    return receitas, total


def buscar(receita_id):
    return consultar("""
        SELECT r.*, u.nome AS autor
        FROM receitas r JOIN usuarios u ON u.id = r.usuario_id
        WHERE r.id = %s
    """, (receita_id,))


def listar_por_usuario(usuario_id):
    return consultar("SELECT * FROM receitas WHERE usuario_id = %s ORDER BY id",
                      (usuario_id,))
