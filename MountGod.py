import discord
from discord.ext import commands
import requests
import json
import random
import Levenshtein
import re
client = discord.Client()


@client.event
async def on_ready():
    print("I'm on ready...")


@commands.command()
async def deploy(ctx):
    await ctx.send('Deploy!')


def setup(bot):
    bot.add_command(deploy)


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
        await client.get_channel(890784320149663834).send(emoji + " __" + member.name + "__ が **" + after.channel.name + "** に参加しました！" + emoji)


@client.event
async def on_message(message):
    if not message.author.bot and "\\" not in message.content:
        if "天気" in message.content:
            data = requests.get(
                "https://weather.tsukumijima.net/api/forecast?city=360010").json()
            dateLabel = 0
            if "明日" in message.content:
                dateLabel = 1
            month = data["forecasts"][dateLabel]["date"][5:7]
            if month[:1] == "0":
                month = month[1:]
            day = data["forecasts"][dateLabel]["date"][8:10]
            if day[:1] == "0":
                day = day[1:]
            await message.channel.send(data["forecasts"][dateLabel]["dateLabel"] + "（" + month + "月" + day + "日）の天気は、" + data["forecasts"][dateLabel]["detail"]["weather"] + "\n朝の降水確率は" + data["forecasts"][dateLabel]["chanceOfRain"]["T06_12"] + "\n昼の降水確率は" + data["forecasts"][dateLabel]["chanceOfRain"]["T12_18"] + "\n夜の降水確率は" + data["forecasts"][dateLabel]["chanceOfRain"]["T18_24"])

        else:
            random.seed()
            with open("KeyWordReaction.json", "r", encoding="utf-8") as KeyWordReaction:
                KeyWordReaction = json.load(KeyWordReaction)
                random.shuffle(KeyWordReaction)
                for data in KeyWordReaction:
                    for keyWord in data["keyWord"]:
                        if keyWord in message.content.lower():
                            if len(data["reaction"]) != 0:
                                for reaction in data["reaction"]:
                                    if reaction[:1] == "U":
                                        reaction = chr(
                                            (int("0x" + reaction[2:], 16)))
                                    await message.add_reaction(reaction)
                            if len(data["message"]) != 0:
                                await message.channel.send(data["message"])
                            return

            if random.randrange(0, 200) == 0:
                await message.add_reaction("<a:takahashi_eye:873932638975569991>")
                await message.add_reaction("<a:05:889229500691394720>")
            elif random.randrange(0, 1000) == 0:
                await message.add_reaction("<a:thinking_gif:818883442518655028>")
                await message.add_reaction("<a:01:889229727083155496>")
            elif random.randrange(0, 10000) == 0:
                await message.add_reaction("<a:chuchu_gif:823537847465803868>")
                await message.add_reaction("<a:001:889229735803105280>")

            else:
                messageContent = extractJapanese(message.content)
                if len(messageContent) <= 20 and len(messageContent) >= 5:
                    with open("TrainingData.json", "r", encoding="utf-8") as TrainingData, open("DefaultReaction.json", "r", encoding="utf-8") as DefaultReaction:
                        TrainingData = json.load(TrainingData)
                        random.shuffle(TrainingData)
                        ApproximateWord = ["", 100]
                        for data in TrainingData:
                            distance = Levenshtein.distance(
                                message.content, data["message"])
                            if ApproximateWord[1] > distance:
                                ApproximateWord = [data["reaction"], distance]
                        DefaultReaction = json.load(DefaultReaction)
                        await message.add_reaction(DefaultReaction[ApproximateWord[0]])
                        await message.add_reaction("<a:iikaeshi:889297289401761852>")


@ client.event
async def on_reaction_add(reaction, user):
    if (not user.bot and str(reaction.emoji) in "<a:iikaeshi:889297289401761852>") or "\\fl" in reaction.message.content:
        reactionAlias = str(
            reaction.message.reactions[0])[2:str(reaction.message.reactions[0]).rfind(":")]
        with open("DefaultReaction.json", "r", encoding="utf-8") as DefaultReaction:
            DefaultReaction = json.load(DefaultReaction)
            if reactionAlias not in DefaultReaction:
                return
            message = extractJapanese(reaction.message.content)
            if len(message) > 20 or len(message) < 5:
                return
            with open("TrainingData.json", "r", encoding="utf-8") as TrainingData:
                TrainingData = json.load(TrainingData)
                messageExists = False
                for data in TrainingData:
                    if message == data["message"]:
                        data["reaction"] = reactionAlias
                        messageExists = True
                        break
                if not messageExists:
                    TrainingData.append(
                        dict({"message": message, "reaction": reactionAlias}))
            with open("TrainingData.json", "wb") as TrainingDataFile:
                TrainingDataFile.write(json.dumps(
                    TrainingData, ensure_ascii=False, indent=2, separators=(',', ': ')).encode("utf-8"))
                TrainingDataFile.write("\n".encode())
            if "\\fl" in reaction.message.content:
                relearning = ""
                if messageExists:
                    relearning = "再"
                await reaction.message.channel.send("**\"" + message + "\"** に対するリアクションとして、" + DefaultReaction[reactionAlias] + " が正しい目標値であると" + relearning + "学習しました")


def extractJapanese(message):
    return re.sub(r"[^ぁ-んァ-ンゔヴヵヶ一-龥々〆ー？]", "", message[message.rfind(
        "\n")+1:])


client.run(json.load(open("config.json", "r"))["token"])
