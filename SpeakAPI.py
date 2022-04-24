from flask import Flask, request, send_file
import requests
import json
import wave

app = Flask(__name__)


@app.route("/", methods=["GET"])
def SpeakAPI():
    message = request.args.get("message")
    params = (
        ("text", message),
        ("speaker", 1),
    )
    audio_query = requests.post(
        f"http://localhost:50021/audio_query",
        params=params
    )
    headers = {"Content-Type": "application/json", }
    synthesis = requests.post(
        f"http://localhost:50021/synthesis",
        headers=headers,
        params=params,
        data=json.dumps(audio_query.json())
    )
    messageData = wave.open("./message.wav", "wb")
    messageData.setnchannels(1)
    messageData.setsampwidth(2)
    messageData.setframerate(24000)
    messageData.writeframes(synthesis.content)
    messageData.close()
    return send_file("./message.wav")


if __name__ == "__main__":
    app.run(host="localhost", port=51401, debug=True)
