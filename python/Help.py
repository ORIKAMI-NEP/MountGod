import json


def Help(message):
    returnValue = None
    if "\\help" in message:
        with open("json/HelpData.json", "r", encoding="utf-8") as HelpData:
            HelpData = json.load(HelpData)
            returnValue = ""
            for data in HelpData:
                returnValue += "\n・" + data["title"] + "\n"
                for command in data["command"]:
                    returnValue += "    ・" + command + "\n"
    return returnValue
