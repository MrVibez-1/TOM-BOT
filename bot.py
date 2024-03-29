#Imports
from ast import alias
import nextcord
import os
import random
import dotenv
from dotenv import load_dotenv

#Loading .env file
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN") #pip install dotenv

#Bot Intents
from nextcord import Client , Intents, Embed
from nextcord.ext import commands 
Intents = nextcord.Intents.all()
client = commands.Bot(command_prefix='-', intents=Intents)
client.remove_command('help')

@client.command()
async def meme(ctx, subreddit: str):
    subreddit = reddit.subreddit(subreddit.lower())
    posts = subreddit.hot(limit=100)
    post = random.choice([post for post in posts if post.url.endswith(".jpg") or post.url.endswith(".png")])
    await ctx.send(post.url)



#When the Bot is ready it will print a ready message
@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Activity(name="pornhub", type=nextcord.ActivityType.streaming, url="https://www.twitch.tv/mrvibez_1"))
    print("\n / _ \ | |   |_   _| |_   _|  _  |  \/  | / __  \|  _  ||___  /\n/ /_\ \| |     | |     | | | | | | .  . | `' / /'| |_| |   / /\n|  _  || |     | |     | | | | | | |\/| |   / /  \____ |  / /  \n| | | || |_____| |_    | | \ \_/ / |  | | ./ /___.___/ /./ /  \n\_| |_/\_____/\___/    \_/  \___/\_|  |_/ \_____/\____/ \_/    \n                   By Alitom297#7175")
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
        Embed = nextcord.embeds.Embed(title="Loaded", description=f"Loaded {extension}", color=0x00ff00)
        await ctx.send(embed=Embed)
    except Exception as e:
        Embed = nextcord.embeds.Embed(title="Error", description=f"Error loading {extension}: {e}", color=0xFF0000)
        await ctx.send(embed=Embed)


@client.command()
async def unload(ctx, extension):
    try:
        client.unload_extension(f"cogs.{extension}")
        Embed = nextcord.embeds.Embed(title="Unloaded", description=f"Unloaded {extension}", color=0x00ff00)
        await ctx.send(embed=Embed)
    except Exception as e:
        Embed = nextcord.embeds.Embed(title="Error", description=f"Error loading {extension}: {e}", color=0xFF0000)
        await ctx.send(embed=Embed)


@client.command()
async def reload(ctx, extension):
    try:
        client.reload_extension(f"cogs.{extension}")
        Embed = nextcord.embeds.Embed(title="Reloaded", description=f"Reloaded {extension}", color=0x00ff00)
        await ctx.send(embed=Embed)
    except Exception as e:
        Embed = nextcord.embeds.Embed(title="Error", description=f"Error loading {extension}: {e}", color=0xFF0000)
        await ctx.send(embed=Embed)
        

#Command Error
@client.event
async def on_command_error(ctx, error):
    Embed = nextcord.embeds.Embed(title="Error", description=f"Error: {error}", color=0xFF0000)
    await ctx.send(embed=Embed)

#Help Command
@client.command()
async def help(ctx):
    Embed = nextcord.embeds.Embed(title="Help", description="This is a list of commands for **Council of Goombingo**", color=random.randint(0, 0xffffff))
    Embed.add_field(name="👑 ADMIN", value="```Prefix, DM, Roleadd, Roleremove```", inline=False)
    Embed.add_field(name="🔧 MODERATION", value="```Kick, Ban, Embed, Warn, Mute, Unmute```", inline=False)
    await ctx.send(embed=Embed)


#JOIN/LEAVE     
@client.event
async def on_member_join(member):
    channel = client.get_channel(909105318276005919)
    Embed = nextcord.embeds.Embed(title="Welcome to the server!", description=f"{member.mention} has joined the server!", color=0x00ff00)
    Embed.set_thumbnail(url="https://media.tenor.com/GIjIHvf3tq0AAAAC/my-nigga-high-five.gif")
    Embed.add_field(name="Member Count", value=f"{len(member.guild.members)}")
    await channel.send(embed=Embed)

@client.event
async def on_member_leave(member):
    channel = client.get_channel(909105318276005919)
    Embed = nextcord.embeds.Embed(title="Goodbye!", description=f"{member.mention} has left the server!", color=0xFF0000)
    await channel.send(embed=Embed)

#Change Prefix
@client.command()
async def prefix(ctx, new_prefix: str):
    if not ctx.author.guild_permissions.manage_guild:
        return

    client.command_prefix = new_prefix

    Embed = nextcord.embeds.Embed(title="Changed prefix", description=f"Changed prefix to {new_prefix}", color=0x00ff00)
    await ctx.send(embed=Embed)

client.run(TOKEN)