import aiosqlite
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
    sniff smallint(255)
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
