from flask import Blueprint, jsonify, request, session
from models import receita_model

receitas = Blueprint("receitas", __name__)

# Campos obrigatórios da receita e o tamanho máximo de cada um
CAMPOS = {
    "titulo": 150,
    "descricao": 255,
    "ingredientes": 2000,
    "modo_preparo": 2000,
}


# GET: consulta (Projeto 1)
@receitas.route("/api/receitas")
@receitas.route("/api/receitas/busca/<string:termo>")
def listar(termo=""):
    pagina = max(1, request.args.get("page", 1, type=int))

    resultado, total = receita_model.listar(termo, pagina)

    return jsonify(
        receitas=resultado,
        pagina=pagina,
        paginas=(total + 4) // 5
    )


# POST: inserção (Projeto 2) - só para usuário logado
@receitas.route("/api/receitas", methods=["POST"])
def inserir():
    # Controle de permissão
    if "usuario_id" not in session:
        return jsonify(erro="Faça login para cadastrar receitas."), 401

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify(erro="Envie os dados da receita em JSON."), 400

    # Validação dos campos
    receita = {}
    erros = []

    for campo, limite in CAMPOS.items():
        valor = str(dados.get(campo) or "").strip()

        if not valor:
            erros.append(f"O campo {campo} é obrigatório.")
        elif len(valor) > limite:
            erros.append(f"O campo {campo} deve ter no máximo {limite} caracteres.")

        receita[campo] = valor

    if erros:
        return jsonify(erro=" ".join(erros)), 400

    # O autor vem da sessão, e não do JSON enviado
    novo_id = receita_model.inserir(receita, session["usuario_id"])

    return jsonify(mensagem="Receita cadastrada com sucesso.", id=novo_id), 201
