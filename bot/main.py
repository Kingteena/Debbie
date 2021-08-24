import discord
from aternosapi import AternosAPI
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_TOKEN")

headers_cookie = os.getenv("ATERNOS_COOKIE")
ATERNOS_TOKEN = os.getenv("ATERNOS_TOKEN")
server = AternosAPI(headers_cookie, ATERNOS_TOKEN)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='start')
async def start(ctx):
    await ctx.send(server.StartServer())

@bot.command(name="status")
async def status(ctx):
    await ctx.send(server.GetStatus())


bot.run(DISCORD_BOT_TOKEN)
