import json


def SpeakerControl(message):
    returnValue = None
    if "\\cs" in message:
        messageArray = message.split()
        if "\\cs" == messageArray[0]:
            SpeakerData = {"Speaker": -1}
            try:
                if messageArray[1] == "四国めたん":
                    if messageArray[2] == "ノーマル":
                        SpeakerData["Speaker"] = 2
                    elif messageArray[2] == "あまあま":
                        SpeakerData["Speaker"] = 0
                    elif messageArray[2] == "ツンツン":
                        SpeakerData["Speaker"] = 6
                    elif messageArray[2] == "セクシー":
                        SpeakerData["Speaker"] = 4
                elif messageArray[1] == "ずんだもん":
                    if messageArray[2] == "ノーマル":
                        SpeakerData["Speaker"] = 3
                    elif messageArray[2] == "あまあま":
                        SpeakerData["Speaker"] = 1
                    elif messageArray[2] == "ツンツン":
                        SpeakerData["Speaker"] = 7
                    elif messageArray[2] == "セクシー":
                        SpeakerData["Speaker"] = 5
                elif messageArray[1] == "九州そら":
                    if messageArray[2] == "ノーマル":
                        SpeakerData["Speaker"] = 16
                    elif messageArray[2] == "あまあま":
                        SpeakerData["Speaker"] = 15
                    elif messageArray[2] == "ツンツン":
                        SpeakerData["Speaker"] = 18
                    elif messageArray[2] == "セクシー":
                        SpeakerData["Speaker"] = 17
                    elif messageArray[2] == "ささやき":
                        SpeakerData["Speaker"] = 19
                elif messageArray[1] == "春日部つむぎ":
                    SpeakerData["Speaker"] = 8
                elif messageArray[1] == "雨晴はう":
                    SpeakerData["Speaker"] = 10
                elif messageArray[1] == "冥鳴ひまり":
                    SpeakerData["Speaker"] = 14
                if SpeakerData["Speaker"] != -1:
                    with open("json/Speaker.json", "wb") as Speaker:
                        Speaker.write(json.dumps(
                            SpeakerData, ensure_ascii=False, indent=2, separators=(",", ": ")).encode("utf-8"))
                        Speaker.write("\n".encode())
                    returnValue = "VOICEROIDを切り替えました"
                else:
                    returnValue = "引数が違います"
            except Exception as e:
                returnValue = "エラー：" + str(e)
    return returnValue
