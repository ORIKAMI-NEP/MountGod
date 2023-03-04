import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def GPTReply(message):
    returnValue = None
    if "!gpt " in message:
        try:
            # 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
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "100文字以内で返答してください。"
                    },
                    {
                        "role": "user",
                        "content": message.replace("!gpt ", "")
                    },
                ],
            )
            returnValue = response["choices"][0]["message"]["content"]
        except Exception as e:
            returnValue = "エラー：" + str(e)
    return returnValue
