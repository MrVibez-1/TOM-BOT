# Python-Disord-Bot
 This is a bot that will be created in python, I will be learning how to code along the way.
 client = commands.bot(command_prefix='!', intents=intents)



 from http import client
import json
import sys
import nextcord #pip install nextcord
import os
import random
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

import nextcord
from nextcord import Client
from nextcord import Intents
from nextcord.ext import commands 
Intents = nextcord.Intents.all()
import config 
import time
client = commands.Bot(command_prefix='!', intents=Intents)
Intents = nextcord.Intents.default()

@client.event
async def on_ready():
    print("\n / _ \ | |   |_   _| |_   _|  _  |  \/  | / __  \|  _  ||___  /\n/ /_\ \| |     | |     | | | | | | .  . | `' / /'| |_| |   / /\n|  _  || |     | |     | | | | | | |\/| |   / /  \____ |  / /  \n| | | || |_____| |_    | | \ \_/ / |  | | ./ /___.___/ /./ /  \n\_| |_/\_____/\___/    \_/  \___/\_|  |_/ \_____/\____/ \_/    \n                   By Alitom297#7175n")
    time.sleep(2)
    print('Bot is ready!')
    print(f'We have logged in as {client.user}')

#COGS
for fn in os.listdir("./cogs/normal") and os.listdir("./cogs/slash"):
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

#More Cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

cogs = ["moderation", "fun", "music", "owner"]
if __name__ == "__main__":
    for cog in cogs:
        client.load_extension(f"cogs.{cog}")
        print(f"Loaded {cog}")
        time.sleep(1)
        
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