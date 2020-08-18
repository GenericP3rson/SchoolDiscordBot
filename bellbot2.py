import discord
from datetime import datetime
import pandas as pd
import numpy as np
import asyncio


client = discord.Client()


async def alerts():
    await client.wait_until_ready()
    df = pd.read_excel("Book1.xlsx")
    row = df.iloc[3]
    col = np.array(df[["Bell Time", "Final Bell", "Classes"]])
    times_normal = []

    for i in col:
        place = [int(x) for x in i[0].split(',')]
        if (not i[1]):
            times_normal.append([place[0], place[1], i[2].split(","), ":bell:"])
            if place[1]+4 >= 60:
                times_normal.append([place[0]+1, (place[1]+4) %
                                    60, i[2].split(","), ":bell:"])
            else:
                times_normal.append(
                    [place[0], place[1]+4, i[2].split(","), ":bell:"])
            if place[1]+5 >= 60:
                times_normal.append([place[0]+1, (place[1]+5) %
                                     60, i[2].split(","), ":one:"])
            else:
                times_normal.append(
                    [place[0], place[1]+5, i[2].split(","), ":one:"])
        else:
            times_normal.append([place[0], place[1], i[2].split(","), ":the_great_demise:"])
    k = 0
    curr = datetime.now()
    while times_normal[k][0] < curr.hour:
        # print(k)
        k += 1
        if k == len(times_normal):
            k -= 1
            break
    if (times_normal[k][0] == curr.hour):
        while times_normal[k][1] < curr.minute:
            k += 1
            if k == len(times_normal):
                k = 0
                break
    k -= 1
    while not client.is_closed:
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
                    k += 1
                    await client.get_channel(691639020094095420).send(times_normal[k+1][3])
                    await client.get_channel(691639020094095420).send("\n".join([i.strip() for i in times_normal[k][2]]))

@client.event
async def on_message(m):
    print(m.content[:13])
    if (m.content[:13] == "!addhomework "):
        df = pd.read_excel("HW.xlsx")
        hw = np.array(df["Homework"])
        hw = np.array(list(hw) + [m.content[13:] + ", Added by user " + m.author.name])
        print(m.content[13:])
        print(hw)
        df["Homework"] = hw 
        df.to_excel("HW.xlsx", index = False)
        print(df)
        await m.channel.send("Successfully added the homework " + m.content[13:])
    elif (m.content[:14] == "!viewhomework "):
        df = pd.read_excel("HW.xlsx")
        hw = np.array(df["Homework"])
        print(hw)
        await m.channel.send("\n".join(hw))
        
@client.event 
async def on_ready():
    print(f"We have logged in as {client.user}")

client.loop.create_task(alerts())
client.run("NjkxNjUxMjgzMTAyMjAzOTE0.XnjEeQ.LKKalsXwSydMbyv4dBS8ZjKhqcE")
