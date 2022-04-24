import requests

message = "こんにちは"
with open("./message.wav", "wb") as messageData:
    messageData.write(requests.get(
        "http://localhost:51401/?message="+message).content)
returnValue = "Success"
