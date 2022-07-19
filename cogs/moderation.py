from nextcord.ext import commands
import nextcord

class Ban(commands.Cog):
    def __init__(self, client):
        super().__init__()
        
    @commands.command() 
    async def ban(ctx, member: nextcord.Member, *, reason=None):
       await member.ban(reason=reason)
       await ctx.send(f"Banned {member.mention}")


def setup(client):
    client.add_cog(Kick(client))
class Kick(commands.Cog):
    def __init__(self, client):
        super().__init__()
        
    @commands.command() 
    async def kick(ctx, member: nextcord.Member, *, reason=None):
       await member.kick(reason=reason)
       await ctx.send(f"Banned {member.mention}")
