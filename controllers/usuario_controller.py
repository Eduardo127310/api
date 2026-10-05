from flask import Blueprint, jsonify, request
from models import usuario_model, receita_model

usuarios = Blueprint("usuarios", __name__)


@usuarios.route("/api/usuarios")
@usuarios.route("/api/usuarios/busca/<string:nome>")
def listar(nome=""):
    nome = nome or request.args.get("nome", "")
    resultado = usuario_model.listar(nome)
    return jsonify(usuarios=resultado, total=len(resultado), termo=nome)


@usuarios.route("/api/usuarios/<int:usuario_id>")
@usuarios.route("/api/usuarios/<int:usuario_id>/receitas")
def perfil(usuario_id):
    resultado = usuario_model.buscar(usuario_id)
    if not resultado:
        return jsonify(erro="Usuário não encontrado"), 404
    receitas = receita_model.listar_por_usuario(usuario_id)
    return jsonify(usuario=resultado[0], receitas=receitas,
                   total_receitas=len(receitas))
