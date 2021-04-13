import discord
import os

client = discord.Client()

client.login(os.getenv('TOKEN'))
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.login(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))