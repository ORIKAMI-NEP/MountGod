import subprocess
import requests


def AIReply(message):
    returnValue = None
    if "\\ai" in message:
        try:
            # returnValue = requests.get("http://10.40.3.171:51400/?message="+message).json()
            subprocess.run(["sshpass", "-p", "nepgear325", "ssh", "1196316@202.231.44.104", "&&", "curl", "http://10.40.3.171:51400/?message="+message])
            #returnValue = subprocess.run(["curl", "http://10.40.3.171:51400/?message="+message])
        except Exception as e:
            return "エラー：" + e
    return returnValue
