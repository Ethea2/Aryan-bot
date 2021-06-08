import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = 'KNS')

@client.event
async def on_ready():
	print("MAIN BOT IS RUNNING!")

@client.command()
async def load(ctx, extension):
	client.load_extension('cogs.{}'.format(extension))

@client.command()
async def unload(ctx, extension):
	client.unload_extension('cogs.{}'.format(extension))

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODUxNjExMzkxODQ0MTU1Mzky.YL6y6Q.fXxdKlWYudMLaDOxwUASGXjsC5w')
