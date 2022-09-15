import json


def ControlSpeaker(message):
    returnValue = None
    if "\\cs" in message:
        messageArray = message.split()
        if "\\cs" == messageArray[0]:
            SpeakerData = {"Speaker": -1}
            ChangeData = ["", "ノーマル"]
            try:
                if messageArray[1] == "0":
                    ChangeData[0] = "四国めたん"
                    if messageArray[2] == "0":
                        ChangeData[1] = "ノーマル"
                        SpeakerData["Speaker"] = 2
                    elif messageArray[2] == "1":
                        ChangeData[1] = "あまあま"
                        SpeakerData["Speaker"] = 0
                    elif messageArray[2] == "2":
                        ChangeData[1] = "ツンツン"
                        SpeakerData["Speaker"] = 6
                    elif messageArray[2] == "3":
                        ChangeData[1] = "セクシー"
                        SpeakerData["Speaker"] = 4
                elif messageArray[1] == "1":
                    ChangeData[0] = "ずんだもん"
                    if messageArray[2] == "0":
                        ChangeData[1] = "ノーマル"
                        SpeakerData["Speaker"] = 3
                    elif messageArray[2] == "1":
                        ChangeData[1] = "あまあま"
                        SpeakerData["Speaker"] = 1
                    elif messageArray[2] == "2":
                        ChangeData[1] = "ツンツン"
                        SpeakerData["Speaker"] = 7
                    elif messageArray[2] == "3":
                        ChangeData[1] = "セクシー"
                        SpeakerData["Speaker"] = 5
                elif messageArray[1] == "5":
                    ChangeData[0] = "九州そら"
                    if messageArray[2] == "0":
                        ChangeData[1] = "ノーマル"
                        SpeakerData["Speaker"] = 16
                    elif messageArray[2] == "1":
                        ChangeData[1] = "あまあま"
                        SpeakerData["Speaker"] = 15
                    elif messageArray[2] == "2":
                        ChangeData[1] = "ツンツン"
                        SpeakerData["Speaker"] = 18
                    elif messageArray[2] == "3":
                        ChangeData[1] = "セクシー"
                        SpeakerData["Speaker"] = 17
                    elif messageArray[2] == "4":
                        ChangeData[1] = "ささやき"
                        SpeakerData["Speaker"] = 19
                elif messageArray[1] == "2":
                    ChangeData[0] = "春日部つむぎ"
                    SpeakerData["Speaker"] = 8
                elif messageArray[1] == "3":
                    ChangeData[0] = "雨晴はう"
                    SpeakerData["Speaker"] = 10
                elif messageArray[1] == "4":
                    ChangeData[0] = "冥鳴ひまり"
                    SpeakerData["Speaker"] = 14
                if SpeakerData["Speaker"] != -1:
                    with open("json/Speaker.json", "wb") as Speaker:
                        Speaker.write(json.dumps(
                            SpeakerData, ensure_ascii=False, indent=2, separators=(",", ": ")).encode("utf-8"))
                        Speaker.write("\n".encode())
                    returnValue = "VOICEROIDを **" + \
                        ChangeData[0] + "** の **" + \
                        ChangeData[1] + "** に切り替えました"
                else:
                    returnValue = "引数が違います"
            except Exception as e:
                returnValue = "エラー：" + str(e)
    return returnValue
