import discord 
from datetime import datetime

client = discord.Client()

times_normal = [[8, 25], [8, 29, True], [8, 30],
                [9, 20], [9, 24, True], [9, 25],
                [10, 15], [10, 19, True], [10, 20],
                [11, 10], [11, 14, True], [11, 15],
                [12, 5], [12, 9, True], [12, 10],
                [13, 0], [13, 4, True], [13, 5],
                [13, 55], [13, 59, True], [14, 0],
                [14, 50], [14, 54, True], [14, 55],
                [15, 45, False]]

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    k = 0
    curr = datetime.now()
    while times_normal[k][0] < curr.hour:
        print(k)
        k+=1
        if k == len(times_normal):
            k-=1
            break
    if (times_normal[k][0] == curr.hour):
        while times_normal[k][1] < curr.minute:
            k+=1
            if k == len(times_normal):
                k = 0
                break
    k-=1
    while True:
        # print(client.channels.find('name', "virtual-bells"))
        # print(client.get_channel(691639020094095420))
        curr = datetime.now()
        # print(curr)
        if (datetime.today().weekday() < 5):
            if not datetime.today().weekday() == 2:
                # print(curr.hour, curr.minute)
                # print(times_normal[k])
                if times_normal[k+1][0] == curr.hour and times_normal[k+1][1] == curr.minute:
                    # print("in")
                    k+=1
                    if k > len(times_normal): k = -1
                    if len(times_normal[k]) == 3:
                        if times_normal[k][2]:
                            await client.get_channel(691639020094095420).send(":one:")
                        else:
                            await client.get_channel(691639020094095420).send(":the_great_demise:")
                    await client.get_channel(691639020094095420).send(":bell:")

client.run("NjkxNjUxMjgzMTAyMjAzOTE0.XnjEeQ.LKKalsXwSydMbyv4dBS8ZjKhqcE")
