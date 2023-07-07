import wicked
from env import DISCORD_API_TOKEN
import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

import wicked.bot
bot = wicked.bot.Bot(bot)

@bot.task()
async def test_task():
    print("test_task")

@bot.event
async def on_ready():
    assert bot.user is not None
    print(f"Logged in as {bot.user.name}#{bot.user.discriminator}")

@bot.slash_command()
async def ping(ctx):
    await ctx.respond('pong')

bot.run(DISCORD_API_TOKEN)
