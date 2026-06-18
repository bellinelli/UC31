import os
from flask import Flask, render_template, request, redirect, url_for, session

if not os.path.exists("templates"):
    os.makedirs("templates")


app = Flask(__name__)
app.secret_key = "chave_definitiva_123"

@app.route("/")
def index():
    if "comidas" not in session:
        session["comidas"] = []
    
    total = sum(item["calorias"] for item in session["comidas"])
    return render_template("index.html", alimentos=session["comidas"], total=total)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form.get("nome", "").strip()
    calorias_texto = request.form.get("calorias", "0")

    try:
        calorias = int(calorias_texto)
    except ValueError:
        calorias = 0

    lista_atualizada = list(session.get("comidas", []))
    lista_atualizada.append(
        {"nome": nome if nome else "Alimento", "calorias": calorias}
    )

    session["comidas"] = lista_atualizada
    session.modified = True

    return redirect(url_for("index"))

@app.route("/zerar")
def zerar():
    session["comidas"] = []
    session.modified = True
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)