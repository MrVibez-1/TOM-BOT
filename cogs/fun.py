from nextcord.ext import commands
import nextcord
import random
import requests

class Fun(commands.Cog):
    def __init__(self, client):
        super().__init__()
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong!")



def setup(client):
    client.add_cog(Fun(client))