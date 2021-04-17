import discord
import os
import requests
import json
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="$")

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


randompar = ["$inspiráció", "$bonk", "$hello", "$noob", "$pokol", "$joke"]
randomvicc = ["\nMit mondasz amikor legyőződ félig Flameheartot?\nMegvan már fél-heart!",
              "\n– Szomszéd, használhatnám a "
              "fűnyíróját?\n– Persze, "
              "csak ne vigye ki a "
              "kertemből…"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("A verzió: " + discord.__version__)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


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
    if message.content == ('$createvc'):
        channel = await create_text_channel("name=autovc", category=overflow)
    if message.content.startswith('$embed'):
        embed1 = discord.Embed(title="Helló!", description="Ez a legjobb szerver az egész magyar discord közösségben.", color=0000000)
        embed1.add_field(name="A szerverről: ", value="Ez egy magyar discord szerver, amit nagyon jófej emberek "
                                                      "futtatnak. Ez nem egy szponzorált üzenet.", inline=False)
        embed1.add_field(name="Erről a botról: ", value="A szervernek dedikált bot, ami fejlesztésben van.", inline=False)
        await message.channel.send(embed=embed1)


client.run(os.getenv('TOKEN'))
