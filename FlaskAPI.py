from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello world"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=51401, debug=True)
