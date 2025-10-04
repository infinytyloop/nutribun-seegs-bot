import aiosqlite
from discord import Embed, colour
from random import choice
from builtins import client

errors = 0
error_code = 0

async def init_database():
    db = await aiosqlite.connect("seex.db")
    await db.execute("""CREATE TABLE IF NOT EXISTS seegs (
    user text,
    bodycount smallint(255),
    swordfights smallint(255),
    swordfight_win smallint(255),
    swordfight_loss smallint(255),
    boys smallint(255),
    girls smallint(255),
    femboys smallint(255),
    unsuccessful smallint(255),
    miscarriage smallint(255),
    gex smallint(255),
    sniff smallint(255),
    peg smallint(255)
    )""")
    await db.close()
    print("Database is initialized and ready.")

async def query_database(query: str):
    db = await aiosqlite.connect("seex.db")
    cur = await db.cursor()

    await cur.execute(query)
    result = await cur.fetchone()
    await db.close()
    print("Database query success.")

    return result

async def query_database_fetchall(query: str):
    db = await aiosqlite.connect("seex.db")
    cur = await db.cursor()

    await cur.execute(query)
    result = await cur.fetchall()
    await db.close()
    print("Database query success.")

    return result

async def update_database(query: str):
    db = await aiosqlite.connect("seex.db")
    cur = await db.cursor()

    await cur.execute(query)
    await db.commit()
    await db.close()

    print("Database update success.")


async def error_report(e,channel):
        global errors, error_code
        ch = await client.fetch_channel(channel)
        me = await client.fetch_user("859360668826337291")
        error_msg = []
        
        with open("error_responses.txt", "rt") as f:
            error_msg.clear()
            for line in f:
                error_msg.append(line.strip())
            f.close()

        if error_code >= 10:
            error_code = 0
        msg = error_msg[error_code]

        await ch.send(f"**An error occurred.**\n\n{msg}\nErrors since last reload/restart: {errors}")
        await me.send(f"```{e}```")
        error_code = error_code + 1
        errors = errors + 1
        print("Error occurred, please check DMs")

async def construct_statsembed(author, avatar, bodycount, swordfights, swordfight_win, swordfight_loss, boys, girls, femboys, unsuccessful, miscarriage, gex, sniff, peg):
    footer_msg = []
    with open("footer_message.txt", "rt") as f:
        footer_msg.clear()
        for line in f:
            footer_msg.append(line.strip())
        f.close() 

    embed = Embed(title=f"Sex Bot Statistics for {author}", color= colour.Color.red())
    avatar = str(avatar)

    embed.set_thumbnail(url=avatar)
    embed.add_field(name="Bodycount", value=bodycount, inline=True)
    embed.add_field(name="Swordfights", value=swordfights, inline=True)
    embed.add_field(name="Swordfight Wins", value=swordfight_win, inline=True)
    embed.add_field(name="Swordfight Losses", value=swordfight_loss, inline=True)
    embed.add_field(name="Times Gexxed", value=gex, inline=True)
    embed.add_field(name="PE clothes sniffed", value=sniff,inline=True)
    embed.add_field(name="People pegged", value=peg,inline=True)
    embed.add_field(name="\n**IMPREGNATE STATS**", value="",inline= False)
    embed.add_field(name="Boys", value=boys, inline=True)
    embed.add_field(name="Girls", value=girls, inline=True)
    embed.add_field(name="Femboys", value=femboys, inline=True)
    embed.add_field(name="Unsuccessful Attempts", value=unsuccessful, inline=True)
    embed.add_field(name="Miscarriages", value=miscarriage, inline=True)

    embed.set_footer(text=choice(footer_msg))

    return embed
