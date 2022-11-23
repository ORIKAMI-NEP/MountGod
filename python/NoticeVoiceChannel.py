def NoticeVoiceChannel(member, beforeChannel, afterChannel, voiceChannelID):
    returnValue = None
    if beforeChannel != afterChannel and afterChannel is not None and afterChannel.id in [voiceChannelID]:
        if member.id in [778607585586053127]:
            emoji = ":fire:"
        elif member.id in [413611857778180096]:
            emoji = ":face_with_symbols_over_mouth:"
        elif member.id in [977381730312941600]:
            emoji = ":roll_of_paper:"
        elif member.id in [673065366595043329]:
            emoji = ":nerd:"
        elif member.id in [574152502774071298]:
            emoji = ":man_student:"
        elif member.id in [731679198615437715]:
            emoji = ":nut_and_bolt:"
        elif member.id in [777105632342966273]:
            emoji = ":syringe:"

        returnValue = emoji + " __" + member.name + "__ が **" + \
            afterChannel.name + "** に参加しました！" + emoji
    return returnValue
