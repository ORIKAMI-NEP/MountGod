import os
import subprocess

from dotenv import load_dotenv

load_dotenv()


def AIReply(message):
    returnValue = None
    if "!ai " in message:
        try:
            returnValue = subprocess.run(
                [
                    "sshpass",
                    "-p",
                    os.getenv("PASSWORD"),
                    "ssh",
                    "1196316@202.231.44.104",
                    "python",
                    "AccessAPI.py",
                    message.replace("!ai ", ""),
                ],
                encoding="utf-8",
                stdout=subprocess.PIPE,
            ).stdout
        except Exception as e:
            returnValue = "エラー：" + str(e)
    return returnValue
