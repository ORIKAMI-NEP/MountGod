import subprocess
import requests


def AIReply(message):
    returnValue = None
    if "\\ai " in message:
        url = "http://10.40.3.171:51400/?message=" + \
            message.replace("\\ai ", "")
        try:
            # returnValue = requests.get("http://10.40.3.171:51400/?message="+message).json()
            returnValue = subprocess.run(
                ["sshpass", "-p", "nepgear325", "ssh", "1196316@202.231.44.104", "curl", url], encoding='utf-8', stdout=subprocess.PIPE)
            returnValue = returnValue.stdout.replace("ãããããã1ã ", "")
        except Exception as e:
            return "エラー：" + e
    return returnValue
