from nextcord.ext import commands
import nextcord


class Staff(commands.Cog):
    def __init__(self, client):
        super().__init__()

    @commands.command()
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def kick(self, ctx, member: None, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')
        await member.send(f'You have been kicked from {ctx.guild.name} for {reason}')
        print(f'{member.name} has been kicked from {ctx.guild.name} for {reason}')

    @commands.command()
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def ban(self, ctx, member: None, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')
        await member.send(f'You have been banned from {ctx.guild.name} for {reason}')
        print(f'{member.name} has been banned from {ctx.guild.name} for {reason}')

    @commands.command()
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def unban(self, ctx, member: None, *, reason=None):
        await ctx.guild.unban(member, reason=reason)
        await ctx.send(f'Unbanned {member.mention}')
        await member.send(f'You have been unbanned from {ctx.guild.name} for {reason}')
        print(f'{member.name} has been unbanned from {ctx.guild.name} for {reason}')

    @commands.command()
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def embed(self, ctx, *, message):
        await ctx.send(embed=nextcord.embeds.Embed(title="Embed", description=message, color=0x00ff00))


def setup(client):
    client.add_cog(Staff(client))