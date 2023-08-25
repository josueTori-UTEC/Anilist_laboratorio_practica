from flask import Flask, jsonify
import json
app = Flask(__name__)
def leer_datos():
    with open("anilist.json", "r") as archivo_json:
        datos = json.load(archivo_json)
    return datos

@app.route("/anime", methods = ['GET'])
def get_all_anime():
    return leer_datos()

@app.route("/anime/<int:id>", methods = ['GET'])
def get_id_anime(id):
    datos = leer_datos()
    get_by_id= None
    for i in datos:
        if i["id"]==id:
            get_by_id = i
            break
    if get_by_id:
        return get_by_id
    else:
        return "no se encontro el objeto"



if __name__ == '__main__':
    app.run(debug=True)


