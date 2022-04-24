import discord
from discord.ext import tasks, commands
import json
import asyncio
from python.AIReply import AIReply
from python.DefaultReaction import LearnReaction, ReturnReaction
from python.Help import Help
from python.KeyWordReaction import KeyWordReaction
from python.RandomReaction import RandomReaction
from python.Reminder import SetReminder, GetReminder, RemoveReminder, RunReminder
from python.Speak import Speak
from python.SpeakerControl import SpeakerControl
from python.VoiceChannelControl import VoiceChannelControl
from python.VoiceChannelNotification import VoiceChannelNotification
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
        returnValue = VoiceChannelNotification(
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

        returnValue = KeyWordReaction(message.content)
        if returnValue[0] is not None:
            await message.add_reaction(returnValue[0])
        if returnValue[1] is not None:
            await message.channel.send(returnValue[1])

        returnValue = RandomReaction()
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

        returnValue = SpeakerControl(message.content)
        if returnValue is not None:
            await message.channel.send(returnValue)

        returnValue = VoiceChannelControl(message)
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
            returnValue = ReturnReaction(message.content)
            if returnValue[0] is not None:
                await message.add_reaction(returnValue[0])
                await message.add_reaction(returnValue[1])


@client.event
async def on_reaction_add(reaction, user):
    if not user.bot:
        returnValue = LearnReaction(reaction)
        if returnValue is not None:
            await reaction.message.channel.send(returnValue)


@tasks.loop(seconds=60.0)
async def loop():
    returnValue = RunReminder()
    if returnValue is not None:
        await client.get_channel(777032730595557389).send(returnValue)


client.run(json.load(open("./json/config.json", "r"))["token"])
