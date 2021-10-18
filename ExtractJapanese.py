import re


def ExtractJapanese(message):
    return re.sub(r"[^ぁ-んァ-ンゔヴヵヶ一-龥々〆ー？]", "", message[message.rfind(
        "\n")+1:])
