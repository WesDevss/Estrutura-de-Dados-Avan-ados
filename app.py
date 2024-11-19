from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Função de recomendação
def gerar_recomendacoes(serie):
    # Lógica fictícia de recomendação
    recomendacoes = [f"Série Recomendada {i}" for i in range(1, 6)]
    return recomendacoes

# Rota principal para servir a página
@app.route("/")
def index():
    return render_template("index.html")  # Corrigido para usar render_template

# Rota para recomendações
@app.route("/recomendar", methods=["POST"])
def recomendar():
    dados = request.get_json()
    serie = dados.get("serie")
    if not serie:
        return jsonify({"erro": "Nenhuma série foi selecionada"}), 400

    recomendacoes = gerar_recomendacoes(serie)
    return jsonify({"recomendacoes": recomendacoes})

# Rota para evitar erro 404 do favicon
@app.route("/favicon.ico")
def favicon():
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
