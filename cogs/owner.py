from nextcord.ext import commands
import nextcord

class CHEESE(commands.Cog):
    def __init__(self, client):
        super().__init__()
    
    @commands.command()
    async def bye(self, ctx):
        await ctx.send(f'bye {ctx.author.mention}!')

def setup(client):
    client.add_cog(CHEESE(client))