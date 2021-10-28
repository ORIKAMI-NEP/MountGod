import discord
from discord.ext import commands
import json
from VoiceChannelNotification import VoiceChannelNotification
from RandomReaction import RandomReaction
from DefaultReaction import LearnReaction, ReturnReaction
from KeyWordReaction import KeyWordReaction
from WeatherForecast import WeatherForecast
client = discord.Client()


@client.event
async def on_ready():
    print("I'm on ready...")
    await client.change_presence(activity=discord.Activity(name="木香井芽衣の憂鬱", type=discord.ActivityType.watching))


@commands.command()
async def deploy(ctx):
    await ctx.send('Deploy!')


def setup(bot):
    bot.add_command(deploy)


@client.event
async def on_voice_state_update(member, before, after):
    if not member.bot:
        if after.channel is None:
            await member.guild.voice_client.disconnect()

        returnValue = VoiceChannelNotification(
            member, before.channel, after.channel)
        if(returnValue is not None):
            await client.get_channel(890784320149663834).send(returnValue)


@client.event
async def on_message(message):
    if not message.author.bot:
        if "芽衣ちゃんおいで" in message.content:
            await client.get_channel(777032856286396456).connect()

        returnValue = RandomReaction()
        if(returnValue[0] is not None):
            await message.add_reaction(returnValue[0])
            await message.add_reaction(returnValue[1])

        if(message.channel.id in [887849368772804678]):
            returnValue = ReturnReaction(message.content)
            if(returnValue[0] is not None):
                await message.add_reaction(returnValue[0])
                await message.add_reaction(returnValue[1])

            returnValue = KeyWordReaction(message.content)
            if(returnValue[0] is not None):
                await message.add_reaction(returnValue[0])
            if(returnValue[1] is not None):
                await message.channel.send(returnValue[1])

            returnValue = WeatherForecast(message.content)
            if(returnValue is not None):
                await message.channel.send(returnValue)


@client.event
async def on_reaction_add(reaction, user):
    if not user.bot:
        returnValue = LearnReaction(reaction)
        if(returnValue is not None):
            await reaction.message.channel.send(returnValue)


client.run(json.load(open("config.json", "r"))["token"])
