from flask import Blueprint, jsonify, request
from models import receita_model

receitas = Blueprint("receitas", __name__)


@receitas.route("/api/receitas")
@receitas.route("/api/receitas/busca/<string:termo>")
def listar(termo=""):
    pagina = max(1, request.args.get("page", default=1, type=int))
    resultado, total = receita_model.listar(termo, pagina)
    return jsonify(
        receitas=resultado,
        termo=termo,
        pagina_atual=pagina,
        por_pagina=5,
        total_resultados=total,
        total_paginas=(total + 4) // 5
    )


@receitas.route("/api/receitas/<int:receita_id>")
def buscar(receita_id):
    resultado = receita_model.buscar(receita_id)
    if not resultado:
        return jsonify(erro="Receita não encontrada"), 404
    return jsonify(resultado[0])
