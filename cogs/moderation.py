from ast import alias
from discord import Embed, Guild, Role
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

    @commands.command(aliases=['esay', 'say', 'quote'])
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def embed(self, ctx, *, message):
        await ctx.send(embed=nextcord.embeds.Embed(title="Embed", description=message, color=0x00ff00))

    @commands.command(aliases=[''])
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def warn(self, ctx, member: nextcord.Member, *, reason=None):
        embed = nextcord.Embed(title="Warned Player", color=nextcord.Color.red())
        embed.add_field(name="Player", value=member.mention, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text=f"Warned by {ctx.author}")
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.set_thumbnail(url=member.avatar)
        await ctx.send(embed=embed)
        channel = self.client.get_channel(alertsChannel)
        await channel.send(f'{member.mention} has been warned by {ctx.author.mention} for {reason}')

    @commands.command(aliass=['shush'])
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def mute(self, ctx, member: nextcord.Member, *, reason=None):
        Guild = ctx.guild
        await member.add_roles(Guild.get_role(909158897577754634))
        embed = nextcord.Embed(title="Muted Player", color=nextcord.Color.red())
        embed.add_field(name="Player", value=member.mention, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text=f"Muted by {ctx.author}")
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.set_thumbnail(url=member.avatar)
        await ctx.send(embed=embed)
        channel = self.client.get_channel(alertsChannel)
        await channel.send(f'{member.mention} has been muted by {ctx.author.mention} for {reason}')

    @commands.command()
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def unmute(self, ctx, member: nextcord.Member, *, reason=None):
        Guild = ctx.guild
        await member.remove_roles(Guild.get_role(909158897577754634))
        embed = nextcord.Embed(title="Unmuted Player", color=nextcord.Color.red())
        embed.add_field(name="Player", value=member.mention, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text=f"Unmuted by {ctx.author}")
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.set_thumbnail(url=member.avatar)
        await ctx.send(embed=embed)
        channel = self.client.get_channel(alertsChannel)
        await channel.send(f'{member.mention} has been unmuted by {ctx.author.mention} for {reason}')



def setup(client):
    client.add_cog(Staff(client))