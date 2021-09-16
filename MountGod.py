import discord
import requests
import json
client = discord.Client()
config = json.load(open("config.json", "r"))


@client.event
async def on_ready():
    print("I'm on ready...")


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel and after.channel is not None and after.channel.id in [777032856286396456]:
        if member.id in [413611857778180096]:
            emoji = ":video_game:"
        elif member.id in [731679198615437715]:
            emoji = ":tools:"
        elif member.id in [777105632342966273]:
            emoji = ":underage:"
        elif member.id in [778607585586053127]:
            emoji = ":dog:"
        await client.get_channel(777032730595557389).send(emoji + " __" + member.name + "__ が **" + after.channel.name + "** に参加しました！" + emoji)


@client.event
async def on_message(message):
    if not message.author.bot:
        if "天気" in message.content:
            response = requests.get(
                "https://weather.tsukumijima.net/api/forecast?city=360010")
            data = response.json()
            day = ["今日", 0]
            if "明日" in message.content:
                day = ["明日", 1]
            await message.channel.send(day[0] + "の天気は、" + data["forecasts"][day[1]]["detail"]["weather"] + "\n朝の降水確率は" + data["forecasts"][day[1]]["chanceOfRain"]["T06_12"] + "\n昼の降水確率は" + data["forecasts"][day[1]]["chanceOfRain"]["T12_18"] + "\n夜の降水確率は" + data["forecasts"][day[1]]["chanceOfRain"]["T18_24"])
        else:
            MessageReaction = json.load(
                open("MessageReaction.json", "r", encoding="utf-8"))
            for data in MessageReaction["data"]:
                for keyWord in data["keyWord"]:
                    if keyWord in message.content.lower():
                        if len(data["reaction"]) != 0:
                            for reaction in data["reaction"]:
                                if reaction[:1] == "U":
                                    reaction = chr(
                                        (int("0x"+reaction[2:], 16)))
                                await message.add_reaction(reaction)
                        if len(data["message"]) != 0:
                            await message.channel.send(data["message"])

client.run(config["token"])
