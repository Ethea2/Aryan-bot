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

token = open("C:\\Users\\Neytan\\Desktop\\Discord Bot\\bot-env\\token\\token.txt", 'r')

client.run(token.read())
