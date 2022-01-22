import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('bot_token.env')
TOKEN = os.getenv('BOT_TOKEN')

Client = discord.Client()
client = commands.Bot(command_prefix="/")

no_commands_channel = [931414371077345289, 931414371521925120]
commands = ["/hi", "/source"]

client.remove_command("help")


def if_command_channel(message):
    if message.channel.id in no_commands_channel:
        print(f"{message.author} used commands in a no no place (ban-hammer time)")
        return False
    return True


async def bad_person(message):
    await message.channel.send(f"{message.channel.mention} This channel doesn't allow commands!")


@client.event
async def on_member_join(member):
    await client.send_message(f"Welcome {member.mention}! Make sure to read {client.get_channel(934320716948602881)}")


@client.event
async def on_ready():
    print(f"Token: {len(TOKEN) * 'X'}; Bot is ready to operate!")


@client.event
async def on_command_error(ctx, message):
    if isinstance(message, Exception):
        await ctx.send(f"There is no such command!")


@client.command(name='hi', help='The bot will say hi to you!')
async def say_hi(message):
    if if_command_channel(message):
        await message.channel.send(f"Hi {message.author.mention}!")
        return
    await bad_person(message)


@client.command(name='source', help='Do you want to see my code and my progress? Here it is!')
async def get_source(message):
    if if_command_channel(message):
        await message.channel.send(f"{message.author.mention}\nhttps://github.com/KimiGets0FPS/Discord-Bot-For-STEAM"
                                   f"-Club")
        return
    await bad_person(message)


@client.command(name="help", help="Run this command to get help, wait, why do you need help on help?")
async def help(message):
    embed = discord.Embed(
        title="Help",
        description="Here are the commands",
        color=discord.Color.blue())
    embed.set_author(name="KimiGets0FPS (Kimi Wan)", url="https://us-east-1.tixte.net/uploads/kimigets0fps.needs.rest"
                                                         "/home.html",
                     icon_url="https://us-east-1.tixte.net/uploads/kimigets0fps.needs.rest/photo.png?AWSAccessKeyId"
                              "=WHPVCLA8APE07J047F9D&Expires=1642832369&Signature=t9mVdkZPx72bRribpnjcWMv0ALw%3D")
    embed.add_field(name="Help", value="Stop, get some help", inline=False)
    embed.add_field(name="source", value="Get source to see my code (check it out, it's cool)", inline=False)
    embed.add_field(name="hi", value="Say hi to my bot when its online :)", inline=False)
    embed.set_footer(text="Made by KimiGets0FPS (not copy and pasted)")
    await message.channel.send(embed=embed)


client.run(TOKEN)
