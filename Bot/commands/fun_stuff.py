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
        if if_command_channel(ctx.message):
            choice = ctx.message.content[5:]
            cc = random.choice(["rock", "paper", "scissors"])  # Computer's choice
            wl = 0
            if cc == choice.lower():
                wl = None
            elif choice.lower() == "rock":
                if cc == "paper":
                    wl = False
                elif cc == "scissors":
                    wl = True
            elif choice.lower() == "paper":
                if cc == "rock":
                    wl = True
                elif cc == "scissors":
                    wl = False
            elif choice.lower() == "scissors":
                if cc == "rock":
                    wl = False
                elif cc == "paper":
                    wl = True
            if wl:
                await ctx.send(f"{ctx.message.author.mention} You win! PC choice: {cc}")
            elif wl is False:
                await ctx.send(f"{ctx.message.author.mention} You lost! PC choice: {cc}")
            elif wl is None:
                await ctx.send(f"{ctx.message.author.mention} You tied!")
            else:
                await ctx.send(f"{ctx.message.author.mention}, that's not a valid choice!")
            return
        await bad_person(ctx.message)

    @commands.command(name="gamer", help="How gay are you?")
    async def gamer(self, message):
        if if_command_channel(message):
            await message.channel.send(f"||{message.author.mention}||\nYou are {random.randint(0, 100)}% a gamer!")
            return
        await bad_person(message)
        return


def setup(client):
    client.add_cog(Fun(client))
