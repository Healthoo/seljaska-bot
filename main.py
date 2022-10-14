import discord
from discord.ext import commands
import config as c
import pandas as pd

# Zloudaj vars
discord_token = c.grab_token()
copypasta = c.copypasta
responses = c.responses

# Client functionality, not moraš enablat intente
bot = discord.Client(intents= discord.Intents().all())
bot_2 =commands.Bot(intents=discord.Intents.all(), command_prefix="%")

def printChamp():
#    string = ""
#    rands = random.sample(range(0, 161), 5)
#    for x in rands:
#        string += c.champs[x] + " "
#    return string
    df1 = pd.read_csv("champs.txt", names=["picks"])
    sample = df1.sample(5)
    igralci = ["Igralec 1: ", "Igralec 2: ", "Igralec 3: ", "Igralec 4: ", "Igralec 5: "]
    sample["igralec"] = igralci
    sample = sample[["igralec", "picks"]].to_string(header=False, index=False)
    return sample


# Event 1, bot pozdravi
@bot.event
async def on_ready():
   await bot.get_channel(606576973619134495).send("FREŠER = SUPREME OVERLORD", file=discord.File('chungus.png'))

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
            await message.reply(printChamp())
            
    #if str(ctx.message.author == "bicmac the police man#4039"):
        #await message.reply("Ti nisi moj šef")
    #elif content in responses and message.author.bot != True:
        #await message.reply(responses[content])

@bot_2.command(name="unleashthekraken")
async def lol(ctx):
    await ctx.channel.send(copypasta)

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run(discord_token)
