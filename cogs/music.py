from nextcord.ext import commands
import nextcord

class test(commands.Cog):
    def __init__(self, client):
        super().__init__()
    
    @commands.command()
    async def hi(self, ctx):
        await ctx.send(f'hi {ctx.author.mention}!')

def setup(client):
    client.add_cog(test(client))