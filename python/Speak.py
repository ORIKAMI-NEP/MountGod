import requests


def Speak(message):
    returnValue = None
    try:
        with open("message.wav", "wb") as messageData:
            messageData.write(requests.get(
                "http://localhost:51401/?message="+message).content)
        returnValue = "Success"
    except:
        pass
    return returnValue
