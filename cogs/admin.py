from ast import alias
from nextcord.ext import commands
import nextcord
import random


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()

    @commands.command()
    @commands.has_any_role("KING", "ADMIN", "CABBAGE")
    async def dm(self, ctx, user: nextcord.Member, *, message):
        Embed = nextcord.Embed(title=f"{user.name} has been dm'd", color=nextcord.Color.blue())
        Embed.add_field(name="Message", value=message, inline=False)
        Embed.set_footer(text=f"DM'd by {ctx.author}")
        Embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        Embed.set_thumbnail(url=user.avatar)
        await ctx.send(embed=Embed)
        Embed = nextcord.Embed(title=f"You have been dm'd by {ctx.author}", color=nextcord.Color.blue())
        Embed.add_field(name="Message", value=message, inline=False)
        Embed.set_footer(text=f"DM'd by {ctx.author}")
        Embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        Embed.set_thumbnail(url=user.avatar)
        await user.send(embed=Embed)


    @commands.command(aliass=[''])
    @commands.has_any_role("KING", "ADMIN", "CABBAGE")
    async def roleadd(self, ctx, role: nextcord.Role, user: nextcord.Member):
        await user.add_roles(role)
        Embed = nextcord.Embed(title=f"{user.name} has been added to {role.name}", color=nextcord.Color.blue())
        Embed.set_footer(text=f"Added by {ctx.author}")
        Embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        Embed.set_thumbnail(url=user.avatar)
        await ctx.send(embed=Embed)

    @commands.command(aliass=[''])
    @commands.has_any_role("KING", "ADMIN", "CABBAGE")
    async def roleremove(self, ctx, role: nextcord.Role, user: nextcord.Member):
        await user.remove_roles(role)
        Embed = nextcord.Embed(title=f"{user.name} has been removed from {role.name}", color=nextcord.Color.blue())
        Embed.set_footer(text=f"Removed by {ctx.author}")
        Embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        Embed.set_thumbnail(url=user.avatar)
        await ctx.send(embed=Embed)


def setup(client):
    client.add_cog(Admin(client))