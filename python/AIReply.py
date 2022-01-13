import subprocess
import requests


def AIReply(message):
    returnValue = None
    if "\\ai " in message:
        try:
            # returnValue = requests.get("http://10.40.3.171:51400/?message="+message).json()
            returnValue = subprocess.run(
                ["sshpass", "-p", "nepgear325", "ssh", "1196316@202.231.44.104", "python", "accessAPI.py", message.replace("\\ai ", "")], encoding="utf-8", stdout=subprocess.PIPE).stdout
        except Exception as e:
            returnValue = "エラー：" + str(e)
    return returnValue
