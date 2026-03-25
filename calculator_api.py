from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Simple Calculator API is running!"

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    result = data['a'] - data['b']
    return jsonify({"result": result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    result = data['a'] - data['b']
    return jsonify({"result": result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    result = data['a'] * data['b']
    return jsonify({"result": result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.json
    if data['b'] == 0:
        return jsonify({"error": "Division by zero not allowed"}), 400
    result = data['a'] / data['b']
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
