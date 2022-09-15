def ControlVoiceChannel(message):
    returnValue = None
    if "\\come" in message.content and message.author.voice is not None:
        returnValue = True
    elif "\\bye" in message.content:
        returnValue = False
    return returnValue
