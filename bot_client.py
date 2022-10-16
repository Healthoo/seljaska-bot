import discord
import config as c

discord_token = c.grab_token()
responses = c.responses

def bot_brez_komand(discord_token, responses):
    bot = discord.Client(intents= discord.Intents().all())

    @bot.event
    async def on_ready():
       await bot.get_channel(606576973619134495).send("FREŠER = SUPREME OVERLORD", file=discord.File('chungus.png'))
       #print("rdy")


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
                found = content[index:index + len(x)]
            if found in responses and message.author.bot != True:
                await message.reply(responses[found])

    bot.run(discord_token)