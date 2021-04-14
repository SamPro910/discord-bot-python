#ez a benedek gépéről van.
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
    if message.content.startswith("$bonk"):
        await message.channel.send("https://steamuserimages-a.akamaihd.net/ugc/1618439156949856647/EBFE6D18C67B0599FFA3F25DA20F020E6C9854C8/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true")
    if message.content.startswith("$help"):
        await message.channel.send("Parancsok: \n$hello - Köszönés\n$noob - no u\n$test - kiírja, hogy fent van e a bot\n$bonk - BONK!")
    if message.content.startswith('$hello'):
        await message.channel.send('Helló!')
    if message.content.startswith("$noob"):
        await message.channel.send("No u.")
    if message.content.startswith('$test'):
        await message.channel.send('Működik!')

client.run(os.getenv('TOKEN'))
