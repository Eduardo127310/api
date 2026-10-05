from flask import Flask, render_template
from controllers.receita_controller import receitas
from controllers.usuario_controller import usuarios

app = Flask(__name__)
app.register_blueprint(receitas)
app.register_blueprint(usuarios)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/perfil/<int:usuario_id>")
def perfil(usuario_id):
    return render_template("perfil.html", usuario_id=usuario_id)


if __name__ == "__main__":
    app.run(debug=True)
