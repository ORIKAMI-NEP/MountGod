import requests


def AIReply(message):
    returnValue = None
    if "AI" in message:
        returnValue = requests.get(
            "http://10.40.3.171:443/?message="+message).json()["reply"]
    return returnValue
