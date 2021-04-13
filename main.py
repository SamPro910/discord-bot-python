import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv
('ODMxNTAyOTY1MDQyMTg0Mjcy.YHWLew.ZntLxuwlk2KtC81aHu5fd4bDahQ'))