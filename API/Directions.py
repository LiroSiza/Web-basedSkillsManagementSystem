from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hola, esta es una ruta básica!"})

if __name__ == '__main__':
    app.run(debug=True)
