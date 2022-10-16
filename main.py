from unittest import case
import discord
from discord.ext import commands
import config as c
import pandas as pd
import functions as f
import bot_client
import bot_command

# Zloudaj vars
discord_token = c.grab_token()
responses = c.responses

bot_client.bot_brez_komand(discord_token, responses)
bot_command.bot_z_komandami(discord_token)

