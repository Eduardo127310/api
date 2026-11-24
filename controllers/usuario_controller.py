from flask import Blueprint, jsonify
from models import usuario_model, receita_model

usuarios = Blueprint("usuarios", __name__)


@usuarios.route("/api/usuarios/busca/<string:nome>")
def listar(nome):
    return jsonify(usuario_model.listar(nome))


@usuarios.route("/api/usuarios/<int:usuario_id>")
def perfil(usuario_id):
    usuario = usuario_model.buscar(usuario_id)

    if not usuario:
        return jsonify(erro="Usuário não encontrado"), 404

    receitas = receita_model.listar_por_usuario(usuario_id)

    return jsonify(
        usuario=usuario[0],
        receitas=receitas
    )
