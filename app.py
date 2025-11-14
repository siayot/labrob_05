from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add")
def add():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=a + b)

@app.route("/sub")
def sub():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=a - b)

@app.route("/mul")
def mul():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=a * b)

@app.route("/div")
def div():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 1))
    return jsonify(result=a / b if b != 0 else "Error")

if name == "__main__":
    app.run(debug=True)
