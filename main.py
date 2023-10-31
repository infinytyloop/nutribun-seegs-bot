import discord
from discord.ext import commands
import builtins

MY_GUILD = discord.Object(id=996688646063271996)
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', description="description", intents=intents)
token = "TOKEN"
builtins.client = client
files = []
nick = str
author = str

from utils import utils

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID {client.user.id})")
    await utils.init_database()

@client.command()
@commands.is_owner()
async def arm(ctx, cog):
    if cog == "nnn":
        await client.load_extension("cogs.nnn_cog")
    await client.load_extension("cogs.cogs")
    await ctx.send(f"bot is armed")
    print("Cogs loaded successfully.")

@client.command()
@commands.is_owner()
async def rearm(ctx):
    await client.reload_extension("cogs.cogs")
    await ctx.send(f"commands reloaded")
    print("Cogs reloaded.")

@client.command()
@commands.is_owner()
async def disarm(ctx):
    await client.unload_extension("cogs.cogs")
    await ctx.send(f"commands unloaded")
    print("Cogs unloaded.")

@client.event
async def on_message_delete(Message):
    global deleted
    global author
    global nick
    global channel
    global files
    global auth
    if Message.attachments:
        for a in Message.attachments:
            files.append(await a.to_file(use_cached=True))
    deleted = Message.content
    auth = Message.author
    author = auth.name
    nick = None   
    if isinstance(auth, discord.Member):
        nick = auth.nick if auth.nick else nick
    channel = Message.channel

@client.command()
async def snipe(ctx):
    global files
    hookname = nick or author    
    if channel != ctx.channel:
        await ctx.send("There are no deleted messages to snipe in this channel.")
        return

    try:
        webhook = await channel.create_webhook(name='Snipe webhook')

        if files:  
            await webhook.send(
                deleted,
                username=hookname,
                avatar_url=str(auth.avatar),
                file=files[0]  
            )
        else:
            await webhook.send(
                deleted,
                username=hookname,
                avatar_url=str(auth.avatar)
            )
        
        await webhook.delete()
        files = []    

    except:
        await ctx.send(f'unable to send through webhook, sniping as bot instead\n\n**{hookname} deleted message:**\n\n{deleted}')
        if files:
            await ctx.send(files=files)
            files = []

client.run(token)