import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv('bot_token.env')
TOKEN = os.getenv('BOT_TOKEN')

Client = discord.Client()
client = commands.Bot(command_prefix="/")

client.remove_command("help")


@client.event
async def on_member_join(member):
    channel = client.get_channel(931602389134377020)
    await channel.send(f"Welcome {member.mention}! Make sure to read {client.get_channel(931602389134377020)}")


@client.event
async def on_ready():
    print(f"Token: {len(TOKEN) * 'X'}; Bot is ready to go brrrrrrrrrrrrrrrrr!")


@client.event
async def on_command_error(ctx, message):
    if isinstance(message, Exception):
        await ctx.send(f"There is no such command!")


cog_files = [
    "commands.basic_commands",
    "commands.fun_stuff",
            ]

for file in cog_files:
    client.load_extension(file)

client.run(TOKEN)
