from dotenv import load_dotenv
import os
import asyncio
import discord

load_dotenv('secrets.env')
token = os.getenv('DISCORD_KEY')
channel_id = '1339575459578515540'
client = discord.Client(intents=discord.Intents.all())

async def console_to_discord():
    """Waits for bot to be ready, then reads console input and sends it to Discord."""
    await client.wait_until_ready()
    channel = client.get_channel(int(channel_id))
    if not channel:
        print(f"Error: Could not find channel with ID {channel_id}")
        await client.close()
        return

    print("\nBot is ready. Type a message and press Enter to send.")
    print("Type 'quit' or 'exit' to stop the bot.")

    while not client.is_closed():
        try:
            # Run blocking input() in a separate thread
            message_to_send = await asyncio.to_thread(input, "> ")

            if message_to_send.lower() in ['quit', 'exit']:
                break

            if message_to_send:
                await channel.send(message_to_send + "\n-# -Suibuano (got muted becaue he's regarded asf)")

        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+D or Ctrl+C
            break

    await client.close()


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID {client.user.id})")
    # Start the console input loop as a background task
    client.loop.create_task(console_to_discord())


client.run(token)



