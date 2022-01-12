import subprocess
import requests


def AIReply(message):
    returnValue = None
    if "\\ai" in message:
        try:
            # returnValue = requests.get("http://10.40.3.171:51400/?message="+message).json()
            subprocess.call("ssh 1196316@202.231.44.104")
            subprocess.call("nepgear325")
            returnValue = subprocess.check_output("curl http://10.40.3.171:51400/?message="+message)
        except Exception as e:
            return "エラー：" + str(e.args[0])
    return returnValue
