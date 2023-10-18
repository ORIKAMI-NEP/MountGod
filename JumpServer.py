import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def JumpServer():
    return requests.get(
        "http://10.40.3.171:51400/?message=" + request.args.get("message")
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=51400, debug=True)
