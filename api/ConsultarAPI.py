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

# Consultar(todos)
@app.route("/filmes",methods=["GET"])
def consultar_filmes():
    return jsonify(filmes)

# Consultar(id)
@app.route("/filmes/<int:id>",methods=["GET"])
def consultar_filmes_id(id):
    for filme in filmes:
        if filme.get("id") == id:
            return jsonify(filme)

app.run(port=8080,host="localhost",debug=True)