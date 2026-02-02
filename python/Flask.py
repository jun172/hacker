from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello",methods=["GET"])
def hello():
    return jsonify({"message":"Hello, Flask!"})

@app.route("/add",methods=["POST"])
def add():
    data = request.json
    result = data["a"] + data["b"]
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True,port=5000)