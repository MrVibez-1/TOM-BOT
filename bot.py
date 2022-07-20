import nextcord #pip install nextcord
import os
import random
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN") #pip install dotenv

import nextcord #pip install nextcord
from nextcord import Client #
from nextcord import Intents
from nextcord.ext import commands 
Intents = nextcord.Intents.all()
import time
client = commands.Bot(command_prefix='!', intents=Intents)
Intents = nextcord.Intents.default()

#When the Bot is ready it will print a ready message
@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Game(name="!help"))
    print("\n / _ \ | |   |_   _| |_   _|  _  |  \/  | / __  \|  _  ||___  /\n/ /_\ \| |     | |     | | | | | | .  . | `' / /'| |_| |   / /\n|  _  || |     | |     | | | | | | |\/| |   / /  \____ |  / /  \n| | | || |_____| |_    | | \ \_/ / |  | | ./ /___.___/ /./ /  \n\_| |_/\_____/\___/    \_/  \___/\_|  |_/ \_____/\____/ \_/    \n                   By Alitom297#7175n")
    time.sleep(2)
    print('Bot is ready!')
    print(f'We have logged in as {client.user}')
    


#COGS
#This cog system loads and unloads commands

    
for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        client.load_extension(f"cogs.{fn[:-3]}")


@client.command()
async def load(ctx, extension):
    try:
        client.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension}.")
    except Exception as e:
        await ctx.send(f"Error loading {extension}: {e}")


@client.command()
async def unload(ctx, extension):
    try:
        client.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded {extension}.")
    except Exception as e:
        await ctx.send(f"Error loading {extension}: {e}")


@client.command()
async def reload(ctx, extension):
    try:
        client.reload_extension(f"cogs.{extension}")
        await ctx.send(f"Reloaded {extension}.")
    except Exception as e:
        await ctx.send(f"Error loading {extension}: {e}")
        
#Commands    
@client.command()
async def ping(ctx):
    await ctx.send("Pong! {}ms".format(round(client.latency * 1000)))   

#Command Error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error: {error}")

#JOIN/LEAVE     
@client.event
async def on_member_join(member):
    channel = client.get_channel(909105318276005919)
    Embed = nextcord.embeds.Embed(title="Welcome to the server!", description=f"{member.mention} has joined the server!", color=0x00ff00)
    Embed.add_field(name="Member Count", value=f"{len(member.guild.members)}")
    await channel.send(embed=Embed)


@client.event
async def on_member_leave(member):
    channel = client.get_channel(909105318276005919)
    Embed = nextcord.embeds.Embed(title="Goodbye!", description=f"{member.mention} has left the server!", color=0xFF0000)
    await channel.send(embed=Embed)
    
client.run(TOKEN)