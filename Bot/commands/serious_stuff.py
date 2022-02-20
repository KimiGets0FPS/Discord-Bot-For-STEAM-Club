# import discord
from discord.ext import commands
# from discord.ext.commands import MemberConverter
import random
import string


no_commands_channel = [931414371077345289, 931414371521925120]
poll_ids = {}


# path for raspberry pi lol
# path = "/home/kimiw/Documents/Discord-Bot-For-STEAM-Club/Bot/Commands/resources/poll_id.txt"

path = "C:/Users/zhewe/OneDrive/Documents/Coding " \
       "Projects/Discord-Bot-For-STEAM-Club/Bot/commands/resources/poll_id.txt"


def gen_id(author):
    poll_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
    poll_ids[poll_id] = author
    return poll_id


def if_command_channel(message):
    if message.channel.id in no_commands_channel:
        print(f"{message.author} used commands in a no no place (ban-hammer time)")
        return False
    return True


async def bad_person(message):
    await message.channel.send(f"{message.channel.mention} This channel doesn't allow commands! D:<")


class SeriousStuff(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="mention", help="Just pings everyone")
    @commands.has_permissions(administrator=True)
    async def mention(self, ctx):
        if if_command_channel(ctx):
            content = ctx.message.content[6:]
            generated = gen_id(ctx.message.author)
            if content:
                with open(path, 'a') as f:
                    print(f"{generated}&&&{ctx.message.author}&&&{content}", file=f)
                await ctx.send(f"{content}\nPoll ID: ||{generated}||")
            else:
                await ctx.send(f"{ctx.message.author.mention}, you should put a title for your poll!")
            return
        await bad_person(ctx)

    @commands.command(name="respond", help="Gets response to a poll")
    async def respond(self, message):
        if if_command_channel(message):
            print(message.content)
            message = message.content
            given_id = message[9:24]
            response = message[24:]
            print(given_id, response)
            with open(path, 'r') as f:
                polls = {}
                while True:
                    line = f.readline().split('&&&')
                    if line == ['']:
                        f.close()
                        break
                    polls.get(line[0], [line[1], line[2]])
            if given_id in polls:
                print(f"{message.author} responded: {response}")
                # RoboticsMaster#6075, KimiGets0FPS#4400
                # user = await MemberConverter.convert(message, "RoboticsMaster#6075")
                await message.author.send(f"{message.author} responded: {response}")
                # user = await MemberConverter.convert(message, "KimiGets0FPS#4400")
                # await user.send(f"{ctx.message.author} responded: {response}")

                await message.channel.send(f"{message.author.mention} thanks for responding to the poll!")
                return
            await message.channel.send(f"{message.author.mention} that's not a valid poll id!")
            return
        await bad_person(message)


def setup(client):
    client.add_cog(SeriousStuff(client))
