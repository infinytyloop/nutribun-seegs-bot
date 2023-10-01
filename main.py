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
async def arm(ctx):
    await client.load_extension("cogs.cogs")
    await ctx.send(f"bot is armed")
    print("Cogs loaded successfully.")

@client.command()
@commands.is_owner()
async def rearm(ctx):
    await client.reload_extension("cogs.cogs")
    await ctx.send(f"commands reloaded")
    print("Cogs reloaded.")


client.run(token)
