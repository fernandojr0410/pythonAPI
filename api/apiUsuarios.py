from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {
        "id": 1,
        "nome": "Fernando da Silva Junior",
        "idade": 20,
        "curso": "Engenharia de Software",
    },
    {
        "id": 2,
        "nome": "Matheus Henrique",
        "idade": 32,
        "curso": "Engenharia Civil",
    },
    {
        "id": 3,
        "nome": "Maria Clara",
        "idade": 26,
        "curso": "Direito"
    },
]

#Consultar(todos)
@app.route("/usuarios",methods=["GET"])
def consultar_usuario():
    return jsonify(usuarios)

#Consultar(id)
@app.route("/usuario/<int:id>",methods=["GET"])
def consultar_usuario_id(id):
    for usuario in usuarios:
        if usuario.get("id") == id:
            return jsonify(usuario)

#Atualizar
@app.rout("/usuarios/<int:id>",methods=["PUT"])
def usuario_atualizado_id(id):
    usuario_alterado = request.get_json()
    for indice,usuario in enumerate(usuarios):
        if usuario.get("id") == id:
            usuarios[indice].update(usuario_alterado)
            return jsonify(usuarios[indice])
        
#Criar
@app.rout("/usuarios",methods=["POST"])
def criar_usuario_novo():
    usuario_novo = request.get_json()
    usuarios.append(usuario_novo)
    return jsonify(usuarios)

#Excluir
@app.route("/usuarios/<int:id>",methods=["DELETE"])
def excluir_usuarios(id):
    for indice,usuario in enumerate(usuarios):
        if usuario.get("id") == id:
            del usuarios[indice]
            return jsonify(usuarios)

app.run(port=5000,host="localhost",debug=True)