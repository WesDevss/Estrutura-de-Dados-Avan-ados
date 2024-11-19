from flask import Flask, request, jsonify, render_template
import networkx as nx

app = Flask(__name__)

# Criar o grafo para o sistema de recomendação
grafo = nx.Graph()

conteudos = {
    "Stranger Things": {"genero": "ficção científica", "subgeneros": ["suspense", "anos 80"]},
    "Dark": {"genero": "ficção científica", "subgeneros": ["viagem no tempo", "mistério"]},
    "The Witcher": {"genero": "fantasia", "subgeneros": ["aventura", "magia"]},
    "Game of Thrones": {"genero": "fantasia", "subgeneros": ["guerra", "dragões"]},
    "Black Mirror": {"genero": "ficção científica", "subgeneros": ["tecnologia", "distopia"]},
    "Love, Death & Robots": {"genero": "ficção científica", "subgeneros": ["animação", "futurismo"]},
    "Altered Carbon": {"genero": "ficção científica", "subgeneros": ["cyberpunk", "futurismo"]},
    "The Mandalorian": {"genero": "aventura", "subgeneros": ["guerra nas estrelas", "ação"]},
    "Star Wars: The Clone Wars": {"genero": "aventura", "subgeneros": ["guerra nas estrelas", "animação"]},
}

for conteudo, info in conteudos.items():
    grafo.add_node(conteudo, genero=info["genero"], subgeneros=info["subgeneros"])

grafo.add_edge("Stranger Things", "Dark", peso=8)
grafo.add_edge("Stranger Things", "The Witcher", peso=5)
grafo.add_edge("Dark", "Black Mirror", peso=7)
grafo.add_edge("Black Mirror", "Love, Death & Robots", peso=9)
grafo.add_edge("The Witcher", "Game of Thrones", peso=6)
grafo.add_edge("Love, Death & Robots", "Altered Carbon", peso=8)
grafo.add_edge("Game of Thrones", "The Mandalorian", peso=4)
grafo.add_edge("The Mandalorian", "Star Wars: The Clone Wars", peso=7)

# Função para recomendar conteúdos
def recomendar_conteudo(conteudo_inicial, profundidade=3):
    if conteudo_inicial not in grafo.nodes:
        return []
    
    recomendacoes = []
    for conteudo_destino in grafo.nodes:
        if conteudo_destino != conteudo_inicial:
            custo = nx.dijkstra_path_length(grafo, conteudo_inicial, conteudo_destino, weight="peso")
            recomendacoes.append((conteudo_destino, custo))
    
    recomendacoes.sort(key=lambda x: x[1])
    return [rec[0] for rec in recomendacoes[:profundidade]]

# Rota principal
@app.route("/")
def index():
    return render_template("index.html")

# Rota para recomendar
@app.route("/recomendar", methods=["POST"])
def recomendar():
    dados = request.get_json()
    serie = dados.get("serie")
    if not serie:
        return jsonify({"erro": "Nenhuma série foi selecionada"}), 400

    recomendacoes = recomendar_conteudo(serie)
    return jsonify({"recomendacoes": recomendacoes})

if __name__ == "__main__":
    app.run(debug=True)
