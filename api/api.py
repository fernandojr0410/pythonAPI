from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {
        "id": 1,
        "marca": "Apple",
        "Categoria": "Iphone",
        "descricao": "Iphone 13, 258GB, Preto",
        "preco": "5.300,00"
    },
    {
        "id": 2,
        "marca": "Apple",
        "Categoria": "Macboook",
        "descricao": "Macbook Air 2017, 128GB SSD, Prata",
        "preco": "6.300,00"
    },
    {
        "id": 3,
        "marca": "Apple",
        "Categoria": "Fone de Ouvido",
        "descricao": "Air Pod 2° Geração, Branco",
        "preco": "1.700,00"
    }
]

#Consultar(Todos)
@app.route("/produtos",methods=["GET"])
def consultar_produtos():
    return jsonify(produtos)

#Consultar(ID)
@app.route("/produtos/<int:id>",methods=["GET"])
def consultar_produto_id(id):
    for produto in produtos:
        if produto.get("id") == id:
            return jsonify(produto)
        
#Atualizar
@app.route("/produtos/<int:id>",methods=["PUT"])
def atualizar_produto_id(id):
    produto_atualizado = request.get_json()
    for indice,produto in enumerate(produtos):
        if produto.get("id") == id:
            produtos[indice].update(produto_atualizado)
            return jsonify(produtos[indice])
        
#Criar
@app.route("/produtos",methods=["POST"])
def criar_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    return jsonify(produtos)

#Excluir
@app.route("/produtos/<int:id>",methods=["DELETE"])
def excluir_produto_id(id):
    for indice,produto in enumerate(produtos):
        if produto.get("id") == id:
            del produtos[indice]
            return jsonify(produtos)

app.run(port=5000,host="localhost",debug=True)