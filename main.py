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
#    elif message.content.startswith('$good'):
#        await message.channel.send('BuckaGamin is good')
#    elif message.content.startwith('$test3'):
#      await message.channel.send('The Bot is working!')

client.login(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))