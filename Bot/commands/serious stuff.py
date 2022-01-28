from discord.ext import commands


class SeriousStuff(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="new", help="Custom Schedule")
    async def new(self, message):
        ...


def setup(client):
    client.add_cog(SeriousStuff(client))
