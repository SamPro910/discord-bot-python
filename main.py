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

    if message.content.startswith("$help"):
        await message.channel.send("Parancsok: \n$hello - Köszönés\n$noob - no u\n$good - kiírja egy jó szerver nevét\n$test3 - kiírja, hogy fent van e a bot\n$credits - kiírja a készítőket")
    if message.content.startswith('$hello'):
        await message.channel.send('Helló-Belló!')
    if message.content.startswith("$noob"):
        await message.channel.send("No u.")
    if message.content.startswith('$good'):
        await message.channel.send('BuckaGamin is good')
    if message.content.startswith('$test3'):
        await message.channel.send('The Bot is working!')
    if message.content.startswith("$whois sam"):
        await message.channel.send("A fő fejlesztője ennek a botnak.")
    if message.content.startswith("$whois ben"):
        await message.channel.send("A második fejlesztője a projektnek, ő találta ki.")
    if message.content.startswith("$credits"):
        await message.channel.send("Made by Sam and Ben\nTovábbi inforámció a készítőkről: $whois sam/$whois ben")

client.run(os.getenv('TOKEN'))
