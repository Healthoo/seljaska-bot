import discord
from discord.ext import commands
import config as c
import functions as f
# Zloudaj vars
discord_token = c.grab_token()

def bot_z_komandami(discord_token):
    bot_cmd = commands.Bot(intents=discord.Intents.all(), command_prefix="!")

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
#bot_z_komandami(discord_token)