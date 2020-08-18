import discord
from datetime import datetime
import pandas as pd
import numpy as np
import asyncio


client = discord.Client()

@client.event
async def on_message(m):
    print(m.content[:13])
    if (m.content[:13] == "!addhomework " or m.content[:7] == "!addhw "):
        print("ADDED")
        dist = 7 if m.content[:7] == "!addhw " else 13
        df = pd.read_excel("HW.xlsx")
        hw = np.array(df["Homework"])
        print(m.content[dist:dist+8])
        if (m.content[dist:dist+8] == "tomorrow"):
            m.content = m.content[:dist] + "May " + \
                str(datetime.today().day+1) + m.content[dist+8:]
        x = m.content[dist:].split()
        x[0] = x[0][:3]
        if len(x[1]) == 1:
            x[1] = "0" + x[1]
        x = ' '.join(x)
        hw = np.array(list(hw) + [x +
                                  ", Added by user " + m.author.name])
        print(m.content[dist:])
        print(hw)
        # df["Homework"] = hw
        df = pd.DataFrame(hw, columns=["Homework"])
        df.to_excel("HW.xlsx", index=False)
        print(df)
        await m.channel.send("Successfully added the homework " + m.content[dist:])
    elif (m.content == "!viewhomework" or m.content == "!viewhw"):
        print("VIEWED")
        df = pd.read_excel("HW.xlsx")
        hw = list(df["Homework"])
        hw.sort()
        print(hw)
        if (len(hw) == 0):
            await m.channel.send("No Homework!!")
        else:
            beta = []
            for i in range(len(hw)):
                beta.append("#" + str(i) + ": " + hw[i])
            await m.channel.send("\n".join(beta))
    elif (m.content[:16] == "!removehomework " or m.content[:10] == "!removehw "):
        print("REMOVES")
        dist = 9 if m.content[:10] == "!removehw " else 15
        df = pd.read_excel("HW.xlsx")
        hw = list(df["Homework"])
        hw.sort()
        if (type(int(m.content[dist:])) == int):
            x = hw.pop(int(m.content[dist:]))
            df = pd.DataFrame(hw, columns=["Homework"])
            df.to_excel("HW.xlsx", index=False)
            await m.channel.send("Removed " + x)
        else:
            await m.channel.send("There's an error.")
    elif (m.content == "!clearhomework" or m.content == "!clearhw"):
        print("CLEAR")
        df = pd.DataFrame([""], columns=["Homework"])
        df.to_excel("HW.xlsx", index=False)
        print(df)
        await m.channel.send("Cleared the Homework")
    elif (m.content[:11] == "!setchannel"):
        with open("channels.txt", "a") as f:
            f.write(str(m.channel.id)+"\n")
            f.close()
        await m.channel.send("You will now recieve bell notifications on " + str(m.channel))
    elif (m.content[:9] == "!getbells"):
        print("BELLS")
        curr = datetime.now()
        # if datetime.today().weekday() == 2:
        if True:
            ans = []
            df = pd.read_excel("Special_Schedule.xlsx")
            col = np.array(df[["Bell Time", "Final Bell", "Classes"]])
            schedule = []
            for i in col:
                x = i[2].split(',')
                hold = []
                for z in x:
                    if z.find('(') > -1:
                        hold.append(z[:z.find('(')].strip())
                    else:
                        hold.append(z.strip())
                test = ', '.join(hold)
                if i[1]:
                    schedule.append(
                        str(int(i[0].split(",")[0])) + ":" + str('{:0>2}'.format(int(i[0].split(",")[1]))) + "— " + test)
                else:
                    if int(i[0].split(",")[1]) + 5 >= 60:
                        schedule.append(
                            str(int(i[0].split(",")[0])+1) + ":" + str('{:0>2}'.format((int(i[0].split(",")[1])+5) % 60)) + "— " + test)
                    else:
                        schedule.append(
                            str(int(i[0].split(",")[0])) + ":" + str('{:0>2}'.format((int(i[0].split(",")[1])+5) % 60)) + "— " + test)
            await m.channel.send("```" + '\n'.join(schedule) + "```")
        # else:
        #     ans = []
        #     df = pd.read_excel("Normal_Schedule.xlsx")
        #     col = np.array(df[["Bell Time", "Final Bell", "Classes"]])
        #     schedule = []
        #     for i in col:
        #         x = i[2].split(',')
        #         hold = []
        #         for z in x:
        #             if z.find('(') > -1:
        #                 hold.append(z[:z.find('(')].strip())
        #             else:
        #                 hold.append(z.strip())
        #         test = ', '.join(hold)
        #         if i[1]:
        #             schedule.append(
        #                 str(int(i[0].split(",")[0])) + ":" + str('{:0>2}'.format(int(i[0].split(",")[1]))) + "— " + test)
        #         else:
        #             if int(i[0].split(",")[1]) + 5 >= 60:
        #                 schedule.append(
        #                     str(int(i[0].split(",")[0])+1) + ":" + str('{:0>2}'.format((int(i[0].split(",")[1])+5) % 60)) + "— " + test)
        #             else:
        #                 schedule.append(
        #                     str(int(i[0].split(",")[0])) + ":" + str('{:0>2}'.format((int(i[0].split(",")[1])+5) % 60)) + "— " + test)
        #     await m.channel.send("```" + '\n'.join(schedule) + "```")


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# client.loop.create_task(alerts())
client.run("NjkxNjUxMjgzMTAyMjAzOTE0.XnjEeQ.LKKalsXwSydMbyv4dBS8ZjKhqcE")
