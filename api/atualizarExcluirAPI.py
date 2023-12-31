from flask import Flask, jsonify, request

app = Flask(__name__)

filmes = [
    {
        "id": 1,
        "ano": 2022,
        "atores": [
            "Alice Johnson",
            "Bob Anderson",
            "Charlie Williams"
        ],
        "id": 2,
        "diretor": "John Smith",
        "genero": "Ação",
        "sinopse": "Um ex-militar se vê forçado a enfrentar uma organização criminosa para salvar sua família.",
        "titulo": "Ação Explosiva"
    },
    {
        "id": 3,
        "ano": 2023,
        "atores": [
            "Eva Lee",
            "Frank White",
            "Grace Parker"
        ],
        "id": 4,
        "diretor": "Emily Brown",
        "genero": "Comédia",
        "sinopse": "Um grupo de amigos se envolve em situações hilárias enquanto tentam abrir uma empresa de organização de festas.",
        "titulo": "Rir é o Melhor Remédio"
    }
]

# Atualizar
@app.route("/filmes/<int:id>",methods=["PUT"])
def atualizar_filmes_id(id):
    filme_alterado = request.get_json()
    for indice,filme in enumerate(filmes):
        if filme.get("id") == id:
            filmes[indice].update(filme_alterado)
            return jsonify(filmes[indice])

# Excluir
@app.route("/filmes/<int:id>",methods=["DELETE"])
def excluir_filme(id):
    for indice,filme in enumerate(filmes):
        if filme.get("id") == id:
            del filmes[indice]
            return jsonify(filmes)