from ast import alias
from discord import Embed
from nextcord.ext import commands
import nextcord
from config import alertsChannel


class Staff(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()

    @commands.command(aliases=['boot'])
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        embed = nextcord.Embed(title="Kicked Player", color=nextcord.Color.red())
        embed.add_field(name="Player", value=member.mention, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text=f"Kicked by {ctx.author}")
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.set_thumbnail(url=member.avatar)
        await ctx.send(embed=embed)
        
        await member.kick(reason=reason)
        channel = self.client.get_channel(alertsChannel)
        await channel.send(f'{member.mention} has been kicked by {ctx.author.mention} for {reason}')

    @commands.command(aliases=['smite'])
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        embed = nextcord.Embed(title="Banned Player", color=nextcord.Color.red())
        embed.add_field(name="Player", value=member.mention, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text=f"Banned by {ctx.author}")
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.set_thumbnail(url=member.avatar)
        await ctx.send(embed=embed)
        
        await member.ban(reason=reason)
        
        channel = self.client.get_channel(alertsChannel)
        await channel.send(f'{member.mention} has been banned by {ctx.author.mention} for {reason}')

    @commands.command(aliases=['clear'])
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        channel = self.client.get_channel(alertsChannel)
        await channel.send(f'{ctx.author.mention} has purged {amount} messages')


def setup(client):
    client.add_cog(Staff(client))