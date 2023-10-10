import discord
from discord.ext import commands
from random import randint

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Hai fatto l\\'accesso come {bot.user}")

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def random(ctx):
    await ctx.send(randint(1, 10))


bot.run("MTE1ODc5MjMxMDk1NjQ5ODk4NA.G63wI2.G2yfztsODG_g0nC6axx21ezN80YSnKvMCDeXeg")
