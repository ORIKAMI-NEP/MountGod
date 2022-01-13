import re


def ExtractJapanese(text):
    return re.sub(r"[^ｦ-ﾟぁ-ゟァ-ー亜-腕弌-熙？]", "", text)
