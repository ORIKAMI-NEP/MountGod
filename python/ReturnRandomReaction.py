import random


def ReturnRandomReaction():
    returnValue = [None, None]
    random.seed()
    if random.randrange(0, 10000) == 0:
        returnValue[0] = "<a:chuchu_gif:823537847465803868>"
        returnValue[1] = "<a:001:889229735803105280>"
    elif random.randrange(0, 1000) == 0:
        returnValue[0] = "<a:thinking_gif:818883442518655028>"
        returnValue[1] = "<a:01:889229727083155496>"
    elif random.randrange(0, 200) == 0:
        returnValue[0] = "<a:takahashi_eye:873932638975569991>"
        returnValue[1] = "<a:05:889229500691394720>"
    return returnValue
