import random
import string


def gen_id():
    poll_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
    # poll_ids[poll_id] = author
    return poll_id


path = "C:/Users/zhewe/OneDrive/Documents/Coding Projects/Discord-Bot-For-STEAM-Club/Bot/testing/test.txt"

with open(path, 'a') as f:
    print(f"{gen_id()}&&&KimiGets0FPS&&&test", file=f)

with open(path, 'r') as f:
    polls = {}
    while True:
        line = f.readline().split('&&&')
        if line == ['']:
            break
        polls[line[0]] = [line[1], line[2][:-1]]

message = input()
given_id = message[9:24]
response = message[24:]
print(polls)
if given_id in polls:
    print(given_id, response)
else:
    print("invalid poll id")
