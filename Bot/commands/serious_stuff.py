from discord.ext import commands
import random
import string


no_commands_channel = [931414371077345289, 931414371521925120]
poll_ids = {}


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

    @commands.command(name="poll", help="Just pings everyone")
    @commands.has_permissions(administrator=True)
    async def poll(self, ctx):
        content = ctx.message.content[6:]
        generated = gen_id(ctx.message.author)
        path = "C:/Users/zhewe/OneDrive/Documents/Coding " \
               "Projects/Discord-Bot-For-STEAM-Club/Bot/commands/resources/poll_id.txt"
        with open(path, 'a') as f:
            print(f"{generated}&&&{ctx.message.author}&&&{content}", file=f)
        await ctx.send(f"{content}\nPoll ID: ||{generated}||")
        return

    @commands.command(name="respond", help="Gets response to a poll")
    async def respond(self, ctx):
        message = ctx.message.content
        given_id = message[8:23]
        response = message[23:]
        print(given_id, response)
        path = "C:/Users/zhewe/OneDrive/Documents/Coding " \
               "Projects/Discord-Bot-For-STEAM-Club/Bot/commands/resources/poll_id.txt"
        with open(path, 'r') as f:
            polls = {}
            while True:
                line = f.readline().split('&&&')
                if not line:
                    break
                polls[line[0]] = [line[1], line[2]]
        await ctx.send(f"{polls}")
        return


def setup(client):
    client.add_cog(SeriousStuff(client))
