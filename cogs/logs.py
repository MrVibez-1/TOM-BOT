from nextcord.ext import commands
import nextcord
from config import alertsChannel


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = nextcord.Embed(title=f"{message.author.name} deleted a message | User ID: <{message.author.id}>",
                               description=f"{message.content}", color=nextcord.Color.blue())
        channel = self.client.get_channel(alertsChannel)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        embed = nextcord.Embed(
            title=f"{message_before.author.name} edited a message. | User ID: <{message_before.author.id}>", color=nextcord.Color.blue())
        embed.add_field(name="Before edit:",
                        value=f"{message_before.content}", inline=False)
        embed.add_field(name="After edit:",
                        value=f"{message_after.content}", inline=False)
        channel = self.client.get_channel(alertsChannel)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = nextcord.Embed(title=f"{member.name} joined the server", color=nextcord.Color.green())
        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(text=f"User ID: <{member.id}>")
        channel = self.client.get_channel(alertsChannel)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = nextcord.Embed(title=f"{member.name} left the server", color=nextcord.Color.red())
        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(text=f"User ID: <{member.id}>")
        channel = self.client.get_channel(alertsChannel)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, member):
        embed = nextcord.Embed(title=f"{member.name} was banned", color=nextcord.Color.red())
        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(text=f"User ID: <{member.id}>")
        channel = self.client.get_channel(alertsChannel)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, member):
        embed = nextcord.Embed(title=f"{member.name} was unbanned", color=nextcord.Color.green())
        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(text=f"User ID: <{member.id}>")
        channel = self.client.get_channel(alertsChannel)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.nick != after.nick:
            embed = nextcord.Embed(title=f"{before.name} changed their nickname to {after.nick}", color=nextcord.Color.blue())
            embed.set_thumbnail(url=before.avatar)
            embed.set_footer(text=f"User ID: <{before.id}>")
            channel = self.client.get_channel(alertsChannel)
            await channel.send(embed=embed)

def setup(client):
    client.add_cog(Logs(client))