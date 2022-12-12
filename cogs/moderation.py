from ast import alias
from nextcord.ext import commands
import nextcord
from config import alertsChannel


class Staff(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()

    @commands.command()
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
        embed = nextcord.Embed(title=f"{member.name} was kicked", color=nextcord.Color.red())
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Kicked by", value=ctx.author.mention, inline=False)
        await channel.send(embed=embed)

    @commands.command()
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
        embed = nextcord.Embed(title=f"{member.name} was banned", color=nextcord.Color.red())
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Banned by", value=ctx.author.mention, inline=False)
        await channel.send(embed=embed)

    @commands.command()
    @commands.has_any_role("KING", "ADMIN", "CABBAGE", "HELPER")
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        channel = self.client.get_channel(alertsChannel)
        Embed = nextcord.Embed(title=f"{ctx.author.name} purged {amount} messages", color=nextcord.Color.red())
        Embed.set_thumbnail(url=ctx.author.avatar)
        await channel.send(embed=Embed)

    @commands.command(alias=["-esay, e, quote"])
    async def embed(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(embed=nextcord.embeds.Embed(title="", description=message, color=0x00ff00))

    @commands.command()
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

    @commands.command()
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