from flask import Blueprint, jsonify, request, session
from werkzeug.security import check_password_hash
from models import usuario_model

login = Blueprint("login", __name__)

# No padrão REST, o login é tratado como o recurso "sessão":
#   POST   /api/sessao -> faz login (cria a sessão)
#   GET    /api/sessao -> mostra quem está logado
#   DELETE /api/sessao -> faz logout (apaga a sessão)


@login.route("/api/sessao", methods=["POST"])
def entrar():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify(erro="Envie e-mail e senha em JSON."), 400

    email = str(dados.get("email") or "").strip()
    senha = str(dados.get("senha") or "")

    if not email or not senha:
        return jsonify(erro="Informe o e-mail e a senha."), 400

    usuario = usuario_model.buscar_por_email(email)

    # Compara a senha digitada com o hash salvo no banco.
    # A mensagem é a mesma nos dois casos para não revelar quais e-mails existem.
    if not usuario or not check_password_hash(usuario[0]["senha"], senha):
        return jsonify(erro="E-mail ou senha inválidos."), 401

    session.clear()
    session["usuario_id"] = usuario[0]["id"]
    session["nome"] = usuario[0]["nome"]

    return jsonify(mensagem="Login realizado com sucesso.", nome=usuario[0]["nome"])


@login.route("/api/sessao")
def usuario_logado():
    if "usuario_id" not in session:
        return jsonify(erro="Nenhum usuário logado."), 401

    return jsonify(id=session["usuario_id"], nome=session["nome"])


@login.route("/api/sessao", methods=["DELETE"])
def sair():
    session.clear()

    return jsonify(mensagem="Logout realizado com sucesso.")
