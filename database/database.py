import mysql.connector


def consultar(sql, parametros=()):
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="api_receitas"
    )

    cursor = conexao.cursor(dictionary=True)
    cursor.execute(sql, parametros)

    dados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return dados
