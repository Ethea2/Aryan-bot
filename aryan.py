import discord
import os
import json
from discord.ext import commands

client = commands.Bot(command_prefix = '\\')

@client.event
async def on_ready():
	print("MAIN BOT IS RUNNING!")


@client.event
async def load(ctx, extension):
	client.load_extension('cogs.{}'.format(extension))


@client.event
async def unload(ctx, extension):
	client.unload_extension('cogs.{}'.format(extension))


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')


token = open("token\\token.txt", 'r')

client.run(token.read())
