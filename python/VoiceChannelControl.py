def VoiceChannelControl(message):
    returnValue = None
    if "芽衣ちゃんおいで" in message.content and message.author.voice is not None:
        returnValue = True
    elif "芽衣ちゃんさよなら" in message.content:
        returnValue = False
    return returnValue
