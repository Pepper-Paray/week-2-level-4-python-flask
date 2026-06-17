print("HELLO — app.py is running!")

from flask import Flask, request, jsonify 

app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"message": "API is running!"})


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return jsonify({"greeting": f"Hello, {name}!"})


@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    return

