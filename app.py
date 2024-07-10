import os 
from flask import Flask, jsonify, request, json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def root():
    return jsonify({ "message": "API FLASK" }), 200 # OK

@app.route('/<name>/<lastname>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def process_name(name, lastname):
    return jsonify({ "name": name, "lastname": lastname }), 200


@app.route('/recibir-info/<modulo>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def recibir_info(modulo):
    """ 
    if request.method == 'POST':
        return jsonify({ "method": "POST"})
    
    if request.method == 'PUT':
        return jsonify({ "method": "PUT"}) 
    """
    # Recibir informacion en el headers
    headers = request.headers

    # Recibir informacion como parametros (query)
    query = request.args

    # Recibir informacion en el Body
    # 1ra Forma de Leer
    datos = json.loads(request.data)

    # 2da Forma de Leer
    datos = request.json

    # 3ra Forma de Leer
    datos = request.get_json()
    print(datos["name"])

    datos = {
        "clave": headers['clave'],
        "estado": query["estado"],
        "modulo": modulo,
        "name": request.json.get("name"),
        "lastname": request.json.get("lastname")
    }

    return jsonify(datos)


@app.route('/users', methods=['GET'])
def get_users():
    pass

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    pass

@app.route('/users', methods=['POST'])
def create_user(id):
    pass

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    pass

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    pass

@app.route('/env', methods=['GET'])
def leer_info_env():
    DATABASE = os.getenv('DATABASE')
    APP_NAME = os.getenv('APP_NAME')
    datos_env = {
        "DATABASE": DATABASE,
        "APP_NAME": APP_NAME
    }

    return jsonify(datos_env), 200


if __name__ == '__main__':
    app.run(debug=True)