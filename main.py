from flask import Flask, jsonify, request
import json
app = Flask(__name__)

with open("anilist.json", "r") as archivo_json:
    datos = json.load(archivo_json)

@app.route("/anime", methods = ['GET'])
def get_all_anime():
    return datos

@app.route("/anime/<int:id>", methods = ['GET'])
def get_id_anime(id):
    get_by_id= None
    for i in datos:
        if i["id"]==id:
            get_by_id = i
            break
    if get_by_id:
        return get_by_id
    else:
        return "no se encontro el objeto"


@app.route("/anime",methods = ['POST'])
def post_anime():
    new_anime = {
    "id": request.json['id'],
    "titulo": request.json['titulo'],
    "puntaje": request.json['puntaje'],
    "tipo": request.json['tipo'],
    "genero": request.json['genero']
    }
    datos.append(new_anime)
    return jsonify({"mensaje": "anime agregado", "new_anime" : datos})

@app.route("/anime/<int:id>", methods = ['PUT'])
def put_id_anime(id):
    put_by_id= None
    for i in datos:
        if i["id"]==id:
            put_by_id = i
            break
    if put_by_id:
        put_by_id['id'] = request.json['id']
        put_by_id['titulo'] = request.json['titulo']
        put_by_id['puntaje'] = request.json['puntaje']
        put_by_id['tipo'] = request.json['tipo']
        put_by_id['genero'] = request.json['genero']
        return jsonify({"mensaje":"anime actualizado", "anime": put_by_id})
    else:
        return "no se encontro el objeto"

@app.route("/anime/<int:id>", methods = ['DELETE'])
def delete_by_id(id):
    delete_by_id = None
    for i in datos:
        if i["id"] == id:
            delete_by_id = i
            break
    if delete_by_id:
        datos.remove(delete_by_id)
        return jsonify({"mensaje":"anime eliminado", "lista animes":datos})
    else:
        return "no se encontro el objeto"

if __name__ == '__main__':
    app.run(debug=True)


