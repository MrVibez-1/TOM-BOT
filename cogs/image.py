from nextcord.ext import commands
import nextcord

class Image(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()




def setup(client):
    client.add_cog(Image(client))