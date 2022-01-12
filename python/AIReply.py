import subprocess
import requests


def AIReply(message):
    returnValue = None
    if "\\ai" in message:
        try:
            # returnValue = requests.get("http://10.40.3.171:51400/?message="+message).json()
            subprocess.call("ssh orikami@202.231.44.104")
            subprocess.call("nepgear325")
            returnValue = subprocess.check_output("wget http://10.40.3.171:51400/?message="+message)
        except Exception as e:
            return "エラー：" + e.args[0]
    return returnValue
