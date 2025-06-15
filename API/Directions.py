from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta simple de prueba
@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensaje": "¡API Flask funcionando correctamente!"})

# Ruta de ejemplo tipo REST
@app.route('/saludo/<nombre>', methods=['GET'])
def saludar(nombre):
    return jsonify({"saludo": f"Hola, {nombre}!"})

if __name__ == '__main__':
    app.run(debug=True)
