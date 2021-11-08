import requests


def AIReply(message):
    returnValue = None
    if "AI" in message:
        returnValue = requests.get(
            "http://localhost:51401/?message="+message).json()["reply"]
    return returnValue
