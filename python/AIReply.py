import subprocess
import requests
from python.ExtractJapanese import ExtractJapanese


def AIReply(message):
    returnValue = None
    if "\\ai " in message:
        url = "http://10.40.3.171:51400/?message=" + \
            message.replace("\\ai ", "")
        try:
            # returnValue = requests.get("http://10.40.3.171:51400/?message="+message).json()
            AIReply = subprocess.run(
                ["sshpass", "-p", "nepgear325", "ssh", "1196316@202.231.44.104", "curl", url], encoding="shift-jis", stdout=subprocess.PIPE).stdout
            returnValue = ExtractJapanese(AIReply)
        except Exception as e:
            return "エラー：" + str(e)
    return returnValue
