import discord
from discord.ext import commands

import datetime


no_commands_channel = [931414371077345289, 931414371521925120]


def if_command_channel(message):
    if message.channel.id in no_commands_channel:
        print(f"{message.author} used commands in a no no place (ban-hammer time)")
        return False
    return True


async def bad_person(message):
    await message.channel.send(f"{message.channel.mention} This channel doesn't allow commands! D:<")


class BasicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Gets schedule
    @commands.command(name="schedule", help="See whens the next meeting")
    async def schedule(self, ctx):
        today = int(datetime.date.today().weekday())
        days = 0
        while today != 3:
            today += 1
            if today > 6:
                today = 0
            days += 1
        if days:
            await ctx.send(f"There are still {days} days until the next meeting")
            return
        await ctx.send("The next meeting is TODAY")

    # Gives users my progress for the discord bbot
    @commands.command(name='source', help='Do you want to see my code and my progress? Here it is!')
    async def get_source(self, message):
        if if_command_channel(message):
            await message.channel.send(f"|| {message.author.mention} ||\n"
                                       f"https://github.com/KimiGets0FPS/Discord-Bot-For-STEAM-Club")
            return
        await bad_person(message)

    # Gives help to those who needs them
    @commands.command(name="help", help="Run this command to get help, wait, why do you need help on help?")
    async def help(self, message):
        embed = discord.Embed(
            title="Help",
            description="Here are the commands\n",
            color=discord.Color.blue())
        embed.set_author(name="KimiGets0FPS (Kimi Wan)",
                         url="https://us-east-1.tixte.net/uploads/kimigets0fps.needs.rest"
                             "/home.html",
                         icon_url="https://us-east-1.tixte.net/uploads/kimigets0fps.needs.rest/photo.png?AWSAccessKeyId"
                                  "=WHPVCLA8APE07J047F9D&Expires=1642832369&Signature=t9mVdkZPx72bRribpnjcWMv0ALw%3D")
        embed.add_field(name="Help", value="> Stop, get some help", inline=False)
        embed.add_field(name="source", value="> Get source to see my code (check it out, it's cool)", inline=False)
        embed.add_field(name="hi", value="> Say hi to my bot when its online :)", inline=False)
        embed.add_field(name="schedule", value="> Tells you when the next meeting is.", inline=False)
        embed.add_field(name="wisdom", value="> You get the wisdom from the one and only **dog** (friend inspired)",
                        inline=False)
        embed.add_field(name="rickroll", value="> Gives you the rick roll video! (friend inspired)", inline=False)
        embed.add_field(name="slap", value="> Why? I have no idea...", inline=False)
        embed.add_field(name="rps", value="> Rock Paper Scissors, /rps [choice]", inline=False)
        embed.add_field(name="gay", value="> How gay are you? (joke and just a random number generator)", inline=False)
        embed.set_footer(text="Made by KimiGets0FPS (not copy and pasted)")
        await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(BasicCommands(client))