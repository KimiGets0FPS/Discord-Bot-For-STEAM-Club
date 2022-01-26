from discord.ext import commands


class SeriousStuff(commands.Cog):
    def __init__(self, client):
        self.client = client

    ...


def setup(client):
    client.add_cog(SeriousStuff(client))
