import requests


def AIReply(message):
    returnValue = None
    if "\\ai" in message:
        returnValue = requests.get(
            "http://10.40.3.171:51400/?message="+message).json()
    return returnValue
