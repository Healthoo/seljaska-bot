import discord
# Import the os module.
import os
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
discord_token = os.getenv(key="key")

intents = discord.Intents().all()
intents.members = True
intents.messages = True
bot = discord.Client(intents= intents)


@bot.event
async def on_ready():
   await bot.get_channel(606576973619134495).send("KI STE PIČKE")

@bot.event
async def on_message(message):
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if "frešer" in message.content.lower() and message.author.bot != True:
    # SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.reply("classic frešer W")
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if "vilec" in message.content.lower():
    # SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.reply("L + ratio")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run(discord_token)