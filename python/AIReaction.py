import json
import random

import Levenshtein

from python.ExtractJapanese import ExtractJapanese


def LearnAIReaction(reaction):
    returnValue = None
    if str(reaction.emoji) in "<a:iikaeshi:889297289401761852>" or "!fl" in reaction.message.content:
        reactionAlias = str(
            reaction.message.reactions[0])[2:str(reaction.message.reactions[0]).rfind(":")]
        with open("json/DefaultReaction.json", "r", encoding="utf-8") as DefaultReaction:
            DefaultReaction = json.load(DefaultReaction)
            if reactionAlias not in DefaultReaction:
                return
            message = ExtractJapanese(reaction.message.content[reaction.message.content.rfind(
                "\n")+1:])
            if len(message) > 20 or len(message) < 5:
                return
            with open("json/LearnedData.json", "r", encoding="utf-8") as LearnedData:
                LearnedData = json.load(LearnedData)
                messageExists = False
                for data in LearnedData:
                    if message == data["message"]:
                        data["reaction"] = reactionAlias
                        messageExists = True
                        break
                if not messageExists:
                    LearnedData.append(
                        dict({"message": message, "reaction": reactionAlias}))
            with open("json/LearnedData.json", "wb") as LearnedDataFile:
                LearnedDataFile.write(json.dumps(
                    LearnedData, ensure_ascii=False, indent=2, separators=(",", ": ")).encode("utf-8"))
                LearnedDataFile.write("\n".encode())
            if "!fl" in reaction.message.content:
                relearning = ""
                if messageExists:
                    relearning = "再"
                returnValue = "**\"" + message + "\"** に対するリアクションとして、" + \
                    DefaultReaction[reactionAlias] + \
                    " が正しい目標値であると" + relearning + "学習しました"
    return returnValue


def ReturnAIReaction(message):
    returnValue = [None, None]
    random.seed()
    if "!fl" not in message:
        messageContent = ExtractJapanese(message)
        if len(messageContent) <= 20 and len(messageContent) >= 5:
            with open("json/LearnedData.json", "r", encoding="utf-8") as LearnedData, open("json/DefaultReaction.json", "r", encoding="utf-8") as DefaultReaction:
                LearnedData = json.load(LearnedData)
                random.shuffle(LearnedData)
                ApproximateWord = ["", 100]
                for data in LearnedData:
                    distance = Levenshtein.distance(
                        message, data["message"])
                    if ApproximateWord[1] > distance:
                        ApproximateWord = [data["reaction"], distance]
                DefaultReaction = json.load(DefaultReaction)
                returnValue[0] = DefaultReaction[ApproximateWord[0]]
                returnValue[1] = "<a:iikaeshi:889297289401761852>"
    return returnValue
