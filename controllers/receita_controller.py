from flask import Blueprint, jsonify, request
from models import receita_model

receitas = Blueprint("receitas", __name__)


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
