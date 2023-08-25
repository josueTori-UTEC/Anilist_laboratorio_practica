from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route("/anime")
def get_all_anime():
    with open("anilist.json", "r") as archivo_json:
        datos = json.load(archivo_json)
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)


