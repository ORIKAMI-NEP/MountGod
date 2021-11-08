import re


def ExtractJapanese(message):
    return re.sub(r"[^ｦ-ﾟぁ-ゟァ-ー亜-腕弌-熙？]", "", message[message.rfind(
        "\n")+1:])
