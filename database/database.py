import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="api_receitas"
    )


# Usada para SELECT: devolve as linhas encontradas
def consultar(sql, parametros=()):
    conexao = conectar()

    cursor = conexao.cursor(dictionary=True)
    cursor.execute(sql, parametros)

    dados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return dados


# Usada para INSERT: grava no banco (commit) e devolve o id criado
def executar(sql, parametros=()):
    conexao = conectar()

    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    conexao.commit()

    novo_id = cursor.lastrowid

    cursor.close()
    conexao.close()

    return novo_id
