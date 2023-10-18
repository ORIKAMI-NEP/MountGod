import os

from dotenv import load_dotenv

load_dotenv()


def ControlSpeaker(message):
    returnValue = None
    if "!cs" in message:
        messageArray = message.split()
        if "!cs" == messageArray[0]:
            SpeakerNumber = -1
            ChangeData = ["", "ノーマル"]
            try:
                if messageArray[1] == "0":
                    ChangeData[0] = "四国めたん"
                    if messageArray[2] == "0":
                        ChangeData[1] = "ノーマル"
                        SpeakerNumber = 2
                    elif messageArray[2] == "1":
                        ChangeData[1] = "あまあま"
                        SpeakerNumber = 0
                    elif messageArray[2] == "2":
                        ChangeData[1] = "ツンツン"
                        SpeakerNumber = 6
                    elif messageArray[2] == "3":
                        ChangeData[1] = "セクシー"
                        SpeakerNumber = 4
                elif messageArray[1] == "1":
                    ChangeData[0] = "ずんだもん"
                    if messageArray[2] == "0":
                        ChangeData[1] = "ノーマル"
                        SpeakerNumber = 3
                    elif messageArray[2] == "1":
                        ChangeData[1] = "あまあま"
                        SpeakerNumber = 1
                    elif messageArray[2] == "2":
                        ChangeData[1] = "ツンツン"
                        SpeakerNumber = 7
                    elif messageArray[2] == "3":
                        ChangeData[1] = "セクシー"
                        SpeakerNumber = 5
                elif messageArray[1] == "5":
                    ChangeData[0] = "九州そら"
                    if messageArray[2] == "0":
                        ChangeData[1] = "ノーマル"
                        SpeakerNumber = 16
                    elif messageArray[2] == "1":
                        ChangeData[1] = "あまあま"
                        SpeakerNumber = 15
                    elif messageArray[2] == "2":
                        ChangeData[1] = "ツンツン"
                        SpeakerNumber = 18
                    elif messageArray[2] == "3":
                        ChangeData[1] = "セクシー"
                        SpeakerNumber = 17
                    elif messageArray[2] == "4":
                        ChangeData[1] = "ささやき"
                        SpeakerNumber = 19
                elif messageArray[1] == "2":
                    ChangeData[0] = "春日部つむぎ"
                    SpeakerNumber = 8
                elif messageArray[1] == "3":
                    ChangeData[0] = "雨晴はう"
                    SpeakerNumber = 10
                elif messageArray[1] == "4":
                    ChangeData[0] = "冥鳴ひまり"
                    SpeakerNumber = 14
                if SpeakerNumber != -1:
                    os.environ["SPEAKER"] = str(SpeakerNumber)
                    returnValue = (
                        "VOICEROIDを **"
                        + ChangeData[0]
                        + "** の **"
                        + ChangeData[1]
                        + "** に切り替えました"
                    )
                else:
                    returnValue = "引数が違います"
            except Exception as e:
                returnValue = "エラー：" + str(e)
    return returnValue
