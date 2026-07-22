from flask import Flask, render_template,request
from converter import converter

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/converter", methods = ["POST"])
def rota_converter():
    valor = float(request.form["valor"])
    origem = request.form["unidade_origem"]
    destino = request.form["unidade_destino"]

    try:
        resultado = converter(valor, origem, destino)
        return render_template("index.html", resultado=round(resultado, 4), erro=None)
    except ValueError as e:
        return render_template("index.html", resultado=None, erro=str(e))

if __name__ == "__main__":
    app.run(debug=True)