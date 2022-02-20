import discord
from discord.ext import commands

import datetime

no_commands_channel = [931414371077345289, 931414371521925120]

# path = "/home/kimiw/Documents/Discord-Bot-For-STEAM-Club/Bot/Commands/resources/suggestions.txt"


path = "C:/Users/zhewe/OneDrive/Documents/Coding " \
       "Projects/Discord-Bot-For-STEAM-Club/Bot/commands/resources/suggestions.txt"


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

    @commands.command(name="suggestion", help="Give me suggestions now ")
    async def suggestion(self, ctx):
        if if_command_channel(ctx):
            suggestion = ctx.message.content[12:]
            with open(path, 'a') as f:
                print(f"{ctx.message.author} suggested: {suggestion}", file=f)
                await ctx.send(f"{ctx.message.author.mention} Thank you for the suggestion!")
                f.close()
                return
        await bad_person(ctx)
        return

    # Gets schedule
    @commands.command(name="schedule", help="See whens the next meeting")
    async def schedule(self, ctx):
        if if_command_channel(ctx):
            today = int(datetime.date.today().weekday())
            days = 0
            while today != 3:
                today += 1
                if today > 6:
                    today = 0
                days += 1
            if days:
                if days == 1:
                    await ctx.send(f"Tomorrow is the next meeting!!!")
                else:
                    await ctx.send(f"There are still {days} days until the next meeting")
                return
            await ctx.send("The next meeting is TODAY")
            return
        await bad_person(ctx)
        return

    # Gives users my progress for the discord bbot
    @commands.command(name='source', help='Do you want to see my code and my progress? Here it is!')
    async def get_source(self, message):
        if if_command_channel(message):
            await message.channel.send(f"|| {message.author.mention} ||\n"
                                       f"https://github.com/KimiGets0FPS/Discord-Bot-For-STEAM-Club")
            return
        await bad_person(message)

    @commands.command(name="creator", help="Maybe you are wondering who created this bot?")
    async def creator(self, message):
        if if_command_channel(message):
            print(f"{message.author} doesn't know who created this bot :(")
            await message.channel.send(f"{message.author.mention}, this bot was created by Kimi!\n"
                                       f"His main Github page is: https://github.com/KimiGets0FPS")
            return
        await bad_person(message)
        return

    # Gives help to those who needs them
    @commands.command(name="help", help="Run this command to get help, wait, why do you need help on help?")
    async def help(self, message):
        if if_command_channel(message):
            embed = discord.Embed(
                title="Help",
                description="Here are the commands\n",
                color=discord.Color.blue())
            embed.set_author(name="KimiGets0FPS (Kimi Wan)",
                             url="https://us-east-1.tixte.net/uploads/kimigets0fps.needs.rest"
                                 "/home.html",
                             icon_url="https://us-east-1.tixte.net/uploads/kimigets0fps.needs.rest/photo.png?"
                                      "AWSAccessKeyId=WHPVCLA8APE07J047F9D&Expires=1642832369&"
                                      "Signature=t9mVdkZPx72bRribpnjcWMv0ALw%3D")
            # Basic Commands
            embed.add_field(name="Help", value="> Stop, get some help", inline=False)
            embed.add_field(name="suggestion", value="> Give me some suggestions! I'm counting on you!!!")
            embed.add_field(name="source", value="> Get source to see my code (check it out, it's cool)", inline=False)
            embed.add_field(name="hi", value="> Say hi to my bot when its online :)", inline=False)
            embed.add_field(name="schedule", value="> Tells you when the next meeting is.", inline=False)

            # Fun!
            embed.add_field(name="wisdom", value="> You get the wisdom from the one and only **dog** (friend inspired)",
                            inline=False)
            embed.add_field(name="rickroll", value="> Gives you the rick roll video! (friend inspired)", inline=False)
            embed.add_field(name="slap", value="> Why? I have no idea...", inline=False)
            embed.add_field(name="rps", value="> Rock Paper Scissors, /rps [choice] (friend inspired)", inline=False)
            embed.add_field(name="gamer", value="> How gamer are you? (joke and just a random number generator; "
                                                "friend inspired)", inline=False)
            embed.add_field(name="ping", value="> Pong! Gives you your ping (supposed to be very low)", inline=False)

            # Serious Stuff
            embed.add_field(name="poll", value="> Gives a poll of how many people are going to join for the next "
                                               "meeting. (Only bot testers, teacher, and creator can use this "
                                               "*unique* command)", inline=False)
            embed.add_field(name="respond", value="> You can respond to a poll by typing: "
                                                  "'/poll [poll id] [response]'", inline=False)
            embed.set_footer(text="Made by KimiGets0FPS (not copy and pasted)")
            await message.channel.send(embed=embed)
            return
        await bad_person(message)
        return


def setup(client):
    client.add_cog(BasicCommands(client))
