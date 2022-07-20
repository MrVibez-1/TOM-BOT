from nextcord.ext import commands
import nextcord
import random

class Fun(commands.Cog):
    def __init__(self, client):
        super().__init__()

    @commands.command(aliases=['esay', 'say'])
    async def embed(self, ctx, *, message):
        await ctx.send(embed=nextcord.embeds.Embed(title="Embed", description=message, color=0x00ff00))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong!")

    @commands.command()
    async def weather(self, ctx, *, city):
        await ctx.send(f"Weather for {city}")


def setup(client):
    client.add_cog(Fun(client))