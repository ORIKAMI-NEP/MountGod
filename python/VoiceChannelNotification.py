def VoiceChannelNotification(member, beforeChannel, afterChannel):
    returnValue = None
    if beforeChannel != afterChannel and afterChannel is not None and afterChannel.id in [777032856286396456]:
        if member.id in [413611857778180096]:
            emoji = ":banana:"
        elif member.id in [731679198615437715]:
            emoji = ":robot:"
        elif member.id in [777105632342966273]:
            emoji = ":u7981:"
        elif member.id in [778607585586053127]:
            emoji = ":pig:"
        returnValue = emoji + " __" + member.name + "__ が **" + \
            afterChannel.name + "** に参加しました！" + emoji
    return returnValue
