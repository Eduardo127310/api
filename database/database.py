import mysql.connector


def consultar(sql, parametros=()):
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA_AQUI",
        database="api_receitas"
    )
    try:
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute(sql, parametros)
            return cursor.fetchall()
        finally:
            cursor.close()
    finally:
        conexao.close()
