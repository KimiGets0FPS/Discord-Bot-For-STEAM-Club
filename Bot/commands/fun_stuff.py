from discord.ext import commands

import random

no_commands_channel = [931414371077345289, 931414371521925120]


def if_command_channel(message):
    if message.channel.id in no_commands_channel:
        print(f"{message.author} used commands in a no no place (ban-hammer time)")
        return False
    return True


async def bad_person(message):
    await message.channel.send(f"{message.channel.mention} This channel doesn't allow commands! D:<")


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="rickroll", help="rick roll")
    async def rickroll(self, message):
        if if_command_channel(message):
            await message.channel.send(f"|| {message.author.mention} ||\n "
                                       f"|| https://www.youtube.com/watch?v=dQw4w9WgXcQ||")
            return
        await bad_person(message)

    @commands.command(name="hi", help="The bot will say hi to you!")
    async def hi(self, message):
        if if_command_channel(message):
            await message.channel.send(f"Hi {message.author.mention}!")
            print(f"{message.author} says hi!")
            return
        await bad_person(message)

    @commands.command(name="wisdom", help="The wisdom from the one and only **dog**")
    async def wisdom(self, message):
        if if_command_channel(message):
            await message.channel.send(f"|| {message.author.mention} ||\n "
                                       f"||https://www.youtube.com/watch?v=D-UmfqFjpl0||")
            return
        await bad_person(message)

    @commands.command(name="slap", help="epic")
    async def slap(self, message):
        if if_command_channel(message):
            await message.channel.send(f"{message.author.mention} u slap")
            return
        await bad_person(message)
        return

    @commands.command(name="rps", help="Rock Paper Scissors")
    async def rps(self, ctx):
        if if_command_channel(ctx):
            cc = random.choice(["rock", "paper", "scissors"])  # Computer's choice
            wl = 0
            content = ctx.message.content[5:]
            if cc == content.lower():
                wl = None
            elif content.lower() == "rock":
                if cc == "paper":
                    wl = False
                elif cc == "scissors":
                    wl = True
            elif content.lower() == "paper":
                if cc == "rock":
                    wl = True
                elif cc == "scissors":
                    wl = False
            elif content.lower() == "scissors":
                if cc == "rock":
                    wl = False
                elif cc == "paper":
                    wl = True
            if wl:
                await ctx.send(f"{ctx.author.mention} You won!\nComputer choice: {cc}")
            elif wl is False:
                await ctx.send(f"{ctx.author.mention} You Lost!\nComputer choice: {cc}")
            elif wl is None:
                await ctx.channel.send(f"{ctx.author.mention} You tied!")
            else:
                await ctx.channel.send(f"{ctx.author.mention} that's not a valid choice! "
                                       f"(do you know how to play rock paper and scissors?)")
            return
        await bad_person(ctx)

    @commands.command(name="gay", help="How gay are you?")
    async def gay(self, message):
        if if_command_channel(message):
            await message.channel.send(f"||{message.author.mention}||\nYou are {random.randint(0, 100)}% gay!")
            return
        await bad_person(message)
        return


def setup(client):
    client.add_cog(Fun(client))
