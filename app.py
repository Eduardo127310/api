import secrets

from flask import Flask, render_template, jsonify
from controllers.receita_controller import receitas
from controllers.usuario_controller import usuarios
from controllers.login_controller import login

app = Flask(__name__)

# Segurança da sessão de login
app.secret_key = secrets.token_hex(32)         # chave aleatória que assina o cookie da sessão
app.config["SESSION_COOKIE_HTTPONLY"] = True   # o JavaScript não consegue ler o cookie
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"  # outro site não consegue usar o cookie (CSRF)

app.register_blueprint(receitas)
app.register_blueprint(usuarios)
app.register_blueprint(login)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/perfil/<int:usuario_id>")
def perfil(usuario_id):
    return render_template("perfil.html", usuario_id=usuario_id)


# Erros sempre respondidos em JSON, sem mostrar detalhes internos
@app.errorhandler(404)
def nao_encontrado(erro):
    return jsonify(erro="Recurso não encontrado."), 404


@app.errorhandler(405)
def metodo_nao_permitido(erro):
    return jsonify(erro="Método não permitido nesta rota."), 405


@app.errorhandler(500)
def erro_interno(erro):
    return jsonify(erro="Erro interno no servidor."), 500


if __name__ == "__main__":
    # debug desligado: o modo debug mostra o código e os erros para qualquer visitante
    app.run(debug=False)
