import discord
from discord.ext import commands
import builtins
import time

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', description="description", intents=intents)
token = "MTAxMzY3MzI1NjUyNTUwODYyOA.Gf9K_r.VDGk_im7LhQBj0_JVuMv9HWnYt89cVRgJ9hO1s"
builtins.client = client
owner = 859360668826337291
client.block_commands = False
from utils import utils

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID {client.user.id})")
    await utils.init_database()

#TODO: arm, disarm, rearm
@client.command()
async def arm(ctx):
    if ctx.author.id == owner:
        await client.load_extension("cogs.cogs")
        await ctx.send("loaded")
    else:
        await ctx.reply(f"You do not own this bot. <@{owner}>, crush his skull.")

@client.command()
async def rearm(ctx):
    if ctx.author.id == owner:
        await client.reload_extension("cogs.cogs")
        await ctx.send("loaded")
    else:
        await ctx.reply(f"You do not own this bot. <@{owner}>, crush his skull.")


@client.event
async def on_message_delete(Message):
    global deleted, author, nick, channel, files
    files = []
    if Message.attachments:
        for a in Message.attachments:
            files.clear()
            files.append(await a.to_file(use_cached=True))
    deleted = Message.content
    author = Message.author.name
    nick = Message.author.nick if Message.author.nick else nick
    channel = Message.channel

    t = time.strftime("%H:%M:%S %D %B %y", time.localtime())
    print(f"Message deleted ({t}):\nAuthor: {nick or author} ({author}) in channel {channel.name}\nMessage Content: {deleted if deleted else None}\nHas Attachment?: {True if files else False}\nHas embed?: {True if Message.embeds else False}")

@client.command()
async def snipe(ctx):
    hookname = nick or author    
    if channel != ctx.channel:
        await ctx.send("There are no deleted messages to snipe in this channel.")
        return

    await ctx.send(f'**{hookname} deleted message:**\n\n{deleted}')
    if files:
        await ctx.send(files=files)
    files.clear()

@client.event
async def on_raw_typing(self):
    guild = client.get_guild(996688646063271996)
    ninoy = guild.get_member(762500367812132894)
    if ninoy.raw_status != "offline":
        client.block_commands = True
    if ninoy.raw_status == "offline":
        client.block_commands = False

client.run(token)