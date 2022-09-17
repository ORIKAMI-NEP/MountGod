import discord
from discord.ext import tasks, commands
import asyncio
import json
from python.AIReaction import LearnAIReaction, ReturnAIReaction
from python.AIReply import AIReply
from python.ControlSpeaker import ControlSpeaker
from python.ControlVoiceChannel import ControlVoiceChannel
from python.Help import Help
from python.NoticeVoiceChannel import NoticeVoiceChannel
from python.Reminder import SetReminder, GetReminder, RemoveReminder, RunReminder
from python.ReturnKeyWordReaction import ReturnKeyWordReaction
from python.ReturnRandomReaction import ReturnRandomReaction
from python.Speak import Speak
from python.WeatherForecast import WeatherForecast
client = discord.Client()


@client.event
async def on_ready():
    print("I'm on ready...")
    await client.change_presence(activity=discord.Activity(name="木香井芽衣の憂鬱", type=discord.ActivityType.watching))
    loop.start()


@commands.command()
async def deploy(ctx):
    await ctx.send("Deploy!")


def setup(bot):
    bot.add_command(deploy)


@client.event
async def on_voice_state_update(member, before, after):
    if not member.bot:
        returnValue = NoticeVoiceChannel(
            member, before.channel, after.channel)
        if returnValue is not None:
            await client.get_channel(890784320149663834).send(returnValue)


@client.event
async def on_message(message):
    if not message.author.bot:
        returnValue = AIReply(message.content)
        if returnValue is not None:
            await message.channel.send(returnValue)

        returnValue = Help(message.content)
        if returnValue is not None:
            await message.channel.send(returnValue)

        returnValue = ReturnKeyWordReaction(message.content)
        if returnValue[0] is not None:
            await message.add_reaction(returnValue[0])
        if returnValue[1] is not None:
            await message.channel.send(returnValue[1])

        returnValue = ReturnRandomReaction()
        if returnValue[0] is not None:
            await message.add_reaction(returnValue[0])
            await message.add_reaction(returnValue[1])

        returnValue = SetReminder(message.content)
        if returnValue is not None:
            await message.channel.send(returnValue)

        returnValue = GetReminder(message.content)
        if returnValue is not None:
            await message.channel.send(returnValue)

        returnValue = RemoveReminder(message.content)
        if returnValue is not None:
            await message.channel.send(returnValue)

        try:
            if type(message.channel) == discord.DMChannel and client.user == message.channel.me and client.get_guild(777032730595557387).voice_client is not None:
                returnValue = Speak(message.content)
                if returnValue is not None:
                    while client.get_guild(777032730595557387).voice_client.is_playing():
                        await asyncio.sleep(0.1)
                    client.get_guild(777032730595557387).voice_client.play(
                        discord.FFmpegPCMAudio("message.wav"))
        except:
            pass

        returnValue = ControlSpeaker(message.content)
        if returnValue is not None:
            await message.channel.send(returnValue)

        returnValue = ControlVoiceChannel(message)
        if returnValue is not None:
            if returnValue:
                try:
                    await message.author.voice.channel.connect()
                except:
                    pass
            else:
                try:
                    await message.guild.voice_client.disconnect()
                except:
                    pass

        returnValue = WeatherForecast(message.content)
        if returnValue is not None:
            await message.channel.send(returnValue)

        if message.channel.id in [887849368772804678]:
            returnValue = ReturnAIReaction(message.content)
            if returnValue[0] is not None:
                await message.add_reaction(returnValue[0])
                await message.add_reaction(returnValue[1])


@client.event
async def on_reaction_add(reaction, user):
    if not user.bot:
        returnValue = LearnAIReaction(reaction)
        if returnValue is not None:
            await reaction.message.channel.send(returnValue)


@tasks.loop(seconds=60.0)
async def loop():
    returnValue = RunReminder()
    if returnValue is not None:
        await client.get_channel(777032730595557389).send(returnValue)


client.run(json.load(open("./json/config.json", "r"))["token"])
