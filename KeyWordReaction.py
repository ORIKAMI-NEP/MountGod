import random
import json


def KeyWordReaction(message):
    returnValue = [None, None]
    random.seed()
    with open("KeyWordReaction.json", "r", encoding="utf-8") as KeyWordReaction:
        KeyWordReaction = json.load(KeyWordReaction)
        random.shuffle(KeyWordReaction)
        for data in KeyWordReaction:
            for keyWord in data["keyWord"]:
                if keyWord in message.lower():
                    if len(data["reaction"]) != 0:
                        for reaction in data["reaction"]:
                            if reaction[:1] == "U":
                                reaction = chr(
                                    (int("0x" + reaction[2:], 16)))
                            returnValue[0] = reaction
                    if len(data["message"]) != 0:
                        returnValue[1] = data["message"]
                    return returnValue
    return returnValue
