import discord
from discord.ext import commands
import builtins

MY_GUILD = discord.Object(id=996688646063271996)
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', description="description", intents=intents)
token = "MTA0OTY0NjkzMzI0NzAwMDU4Ng.GUigM0.7J1BiJL6s-fHe9JniNA8FdcexV44tv8FxddMoU"
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

@client.event
async def on_command_error(message,error):
    if isinstance(error, commands.CommandNotFound):
        await message.send("not yet implemented")

client.run(token)