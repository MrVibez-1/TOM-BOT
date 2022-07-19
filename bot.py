from http import client
import json
import sys
from instabot import Bot
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
import config 
import time
client = commands.Bot(command_prefix='!', intents=Intents)
Intents = nextcord.Intents.default()

#When the Bot is ready it will print a ready message
@client.event
async def on_ready():
    print("\n / _ \ | |   |_   _| |_   _|  _  |  \/  | / __  \|  _  ||___  /\n/ /_\ \| |     | |     | | | | | | .  . | `' / /'| |_| |   / /\n|  _  || |     | |     | | | | | | |\/| |   / /  \____ |  / /  \n| | | || |_____| |_    | | \ \_/ / |  | | ./ /___.___/ /./ /  \n\_| |_/\_____/\___/    \_/  \___/\_|  |_/ \_____/\____/ \_/    \n                   By Alitom297#7175n")
    time.sleep(2)
    print('Bot is ready!')
    print(f'We have logged in as {client.user}')


#COGS
#This cog system loads and unloads commands

cogs = ["moderation","music","owner"]
for cog in cogs:
    client.load_extension(f"cogs.{cog}")    #    await ctx.send(f"Loaded {extension}.")

for fn in os.listdir("./cogs") and os.listdir("./cogs/slash"):
    if fn.endswith(".py"):
        client.load_extension(f"cogs.{fn[:-3]}")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension}.") #    await ctx.send(f"Loaded {extension}.")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension}.")

@client.command()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension}.")
        
#Commands    
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
@client.command()
async def headortails(ctx, answer):
    if random.choice(["heads", "tails"]) == answer:
        await ctx.reply("Congratulations")
    else:
        await ctx.reply("Sorry you lost")

client.run(TOKEN)