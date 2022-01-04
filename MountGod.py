import discord
from discord.ext import commands
import json
from python.AIReply import AIReply
from python.DefaultReaction import LearnReaction, ReturnReaction
from python.KeyWordReaction import KeyWordReaction
from python.RandomReaction import RandomReaction
from python.Reminder import Reminder
from python.VoiceChannelControl import VoiceChannelControl
from python.VoiceChannelNotification import VoiceChannelNotification
from python.WeatherForecast import WeatherForecast
client = discord.Client()


@client.event
async def on_ready():
    print("I'm on ready...")
    await client.change_presence(activity=discord.Activity(name="木香井芽衣の憂鬱", type=discord.ActivityType.watching))


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
        returnValue = KeyWordReaction(message.content)
        if returnValue[0] is not None:
            await message.add_reaction(returnValue[0])
        if returnValue[1] is not None:
            await message.channel.send(returnValue[1])

        returnValue = RandomReaction()
        if returnValue[0] is not None:
            await message.add_reaction(returnValue[0])
            await message.add_reaction(returnValue[1])

        returnValue = Reminder()

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
            returnValue = AIReply(message.content)
            if returnValue is not None:
                await message.channel.send(returnValue)

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


client.run(json.load(open("./json/config.json", "r"))["token"])
