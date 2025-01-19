import asyncio

import discord
from discord.ext import commands, tasks
# import random
from itertools import cycle
import os

# import asyncle

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

bot_status = cycle(["Online", "Status Two", "Status Three", "Status Four"])


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))


@client.event
async def on_ready():
    print("Sucess: Bot is connected to Discord")
    change_status.start()


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded")


async def main():
    async with client:
        await load()
        await client.start("MTMzMDIxODgzNTk0NDQxMTE3Nw.Gjlm2q.pS8o9T15YvVzaFga10gsUJ-LmZM8z4E6soqtVs")


# @client.command()
# async def ping(ctx):
#     bot_latency = round(client.latency * 1000)
#     await ctx.send(f"Pong! {bot_latency} ms.")


# @client.command()
# async def ball(ctx, *, question):
#     otazky = ["Jak se máš?", "Mám se dobře."]
#     response = random.choice(otazky)
#
#     await ctx.send(response)

# client.run("MTMzMDIxODgzNTk0NDQxMTE3Nw.Gjlm2q.pS8o9T15YvVzaFga10gsUJ-LmZM8z4E6soqtVs")
asyncio.run(main())
