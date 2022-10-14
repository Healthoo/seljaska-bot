import discord
from discord.ext import commands
import config as c

# Zloudaj vars
discord_token = c.grab_token()
copypasta = c.copypasta
responses = c.responses

# Client functionality, not moraš enablat intente
bot = discord.Client(intents= discord.Intents().all())
bot_2 =commands.Bot(intents=discord.Intents.all(), command_prefix="%")

# Event 1, bot pozdravi
@bot.event
async def on_ready():
   await bot.get_channel(606576973619134495).send("FREŠER = SUPREME OVERLORD", file=discord.File('chungus.png'))

# Event 2, odgovori na keywords
@bot.event
async def on_message(message, ctx):
    content = message.content.lower()
    if str(ctx.message.author == "bicmac the police man#4039"):
        await message.reply("Ti nisi moj šef")
    elif content in responses and message.author.bot != True:
        await message.reply(responses[content])

@bot_2.command(name="unleashthekraken")
async def lol(ctx):
    await ctx.channel.send(copypasta)

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run(discord_token)