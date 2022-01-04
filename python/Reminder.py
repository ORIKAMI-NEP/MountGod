import json
import datetime


def SetReminder(message):
    returnValue = None
    messageArray = message.split()
    if "\\sr" == messageArray[0]:
        returnValue = "引数の長さが違います"
        if len(messageArray) == 7:
            with open("json/ReminderData.json", "r", encoding="utf-8") as ReminderData:
                ReminderData = json.load(ReminderData)
                date = messageArray[1] + "/" + messageArray[2].zfill(2) + "/" + messageArray[3].zfill(
                    2) + " " + messageArray[4].zfill(2) + ":" + messageArray[5].zfill(2)
                for data in ReminderData:
                    if date == data["date"]:
                        return "その時間には既にリマインダーがセットされています"
                ReminderData.append(
                    dict({"date": date, "message": messageArray[6]}))
            with open("json/ReminderData.json", "wb") as ReminderDataFile:
                ReminderDataFile.write(json.dumps(
                    ReminderData, ensure_ascii=False, indent=2, separators=(",", ": ")).encode("utf-8"))
                ReminderDataFile.write("\n".encode())
            returnValue = "リマインダーをセットしました"
    return returnValue


def GetReminder(message):
    returnValue = None
    if "\\gr" in message:
        with open("json/ReminderData.json", "r", encoding="utf-8") as ReminderData:
            ReminderData = json.load(ReminderData)
            if len(ReminderData) == 0:
                return "リマインダーが存在しません"
            returnValue = ""
            for data, i in zip(ReminderData, range(len(ReminderData))):
                returnValue += str(i) + ":  " + \
                    data["date"] + "  " + data["message"]+"\n"
    return returnValue


def RemoveReminder(message):
    returnValue = None
    messageArray = message.split()
    if "\\rr" == messageArray[0]:
        returnValue = "引数の長さが違います"
        if len(messageArray) == 2:
            with open("json/ReminderData.json", "r", encoding="utf-8") as ReminderData:
                ReminderData = json.load(ReminderData)
                if len(ReminderData) == 0:
                    return "リマインダーが存在しません"
                try:
                    del ReminderData[int(messageArray[1])]
                except Exception as e:
                    return "エラー：" + e.args[0]
            with open("json/ReminderData.json", "wb") as ReminderDataFile:
                ReminderDataFile.write(json.dumps(
                    ReminderData, ensure_ascii=False, indent=2, separators=(",", ": ")).encode("utf-8"))
                ReminderDataFile.write("\n".encode())
            returnValue = "リマインダーを削除しました"
    return returnValue


def RunReminder():
    returnValue = None
    elementNumber = -1
    with open("json/ReminderData.json", "r", encoding="utf-8") as ReminderData:
        ReminderData = json.load(ReminderData)
        for data, i in zip(ReminderData, range(len(ReminderData))):
            if data["date"] == datetime.datetime.now().strftime("%Y/%m/%d %H:%M"):
                returnValue = data["message"]
                elementNumber = i
    if elementNumber != -1:
        RemoveReminder("\\rr " + str(elementNumber))
    return returnValue
