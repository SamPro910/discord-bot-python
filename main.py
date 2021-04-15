import discord
import os
import requests
import json
import random

client = discord.Client()
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote
randompar = ["$inspiráció", "$bonk", "$hello", "$noob", "$pokol", "$joke"]
randomvicc = ["\nMit mondasz amikor legyőződ félig Flameheartot?\nMegvan már fél-heart!", "\n– Szomszéd, használhatnám a "
                                                                                        "fűnyíróját?\n– Persze, "
                                                                                        "csak ne vigye ki a "
                                                                                        "kertemből…"]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    kuld = message.channel.send

    if message.content.startswith("$pokol"):
        await kuld("Ez a szerver...")
    if message.content.startswith("$random"):
        await kuld("A random parancs: " + random.choice(randompar))
    if message.content.startswith("$inspiráció"):
        quote = get_quote()
        await kuld(quote)
    if message.content.startswith("$bonk"):
        await kuld("https://steamuserimages-a.akamaihd.net/ugc/1618439156949856647"
                                   "/EBFE6D18C67B0599FFA3F25DA20F020E6C9854C8/?imw=637&imh=358&ima=fit&impolicy"
                                   "=Letterbox&imcolor=%23000000&letterbox=true")
    if message.content.startswith("$help"):
        await message.channel.send("Parancsok: \n$hello - Köszönés\n$noob - no u\n$test - kiírja, hogy fent van e a "
                                   "bot\n$bonk - BONK!\n$inspiráció - egy inspiráló üzenet...\n$random - kiír egy "
                                   "random parancsot.\n$joke - add egy random viccet")
    if message.content.startswith("$inspiráció"):
        quote = get_quote()
        await kuld(quote)
    if message.content.startswith("$joke"):
        await kuld(random.choice(randomvicc))

client.run(os.getenv('TOKEN'))
