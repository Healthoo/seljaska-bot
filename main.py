from unittest import case
import discord
from discord.ext import commands
import config as c
import pandas as pd
import functions as f

# Zloudaj vars
discord_token = c.grab_token()
responses = c.responses

# Client functionality, not moraš enablat intente
bot = discord.Client(intents= discord.Intents().all())
bot_cmd = commands.Bot(intents=discord.Intents.all(), command_prefix="!")

# Event 1, bot zalima CHUNGUS
@bot.event
async def on_ready():
   await bot.get_channel(606576973619134495).send("FREŠER = SUPREME OVERLORD", file=discord.File('chungus.png'))
   #print("rdy")

# Event 2, odgovori na keywords
@bot.event
async def on_message(message):
    content = message.content.lower()

    # Pogleda ce je kluc v sporocilu in odgovori
    for x in responses.keys(): 
        
        # Index zacetke kljuca v stringu
        index = content.find(x)
        found = ""

        if index != -1:
            # Substring 
            found = content[index:index+len(x)]
        if found in responses and message.author.bot != True:
            await message.reply(responses[found])

    if "picks" in content:
        if message.author.bot != True:
            await message.reply(f.printChamp())

# Ne dela:(
@bot_cmd.command()
async def copypasta(ctx):
    await ctx.channel.send(c.copypastas)

# Razdeli pickse folku v VC
@bot_cmd.command()
async def champs(ctx, *args):
    if args:
        match args[0]:
            case "vc":
                #print(ctx.message.guild.get_member(ctx.message.author.id).voice.channel.id)
                players = []
                vc = bot_cmd.get_channel(ctx.message.guild.get_member(ctx.message.author.id).voice.channel.id)
                for user in vc.members:
                    if not user.id in c.bot_ids: 
                        players.append(user.name+": ")
                st_igralcev = len(players)
                await ctx.send(f.printChamp(players, st_igralcev))
    else:
        players = ["Igralec 1: ", "Igralec 2: ", "Igralec 3: ", "Igralec 4: ", "Igralec 5: "]
        await ctx.send(f.printChamp(players))

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot_cmd.run(discord_token)
#bot.run(discord_token)