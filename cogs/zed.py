import os
import random
import discord
from discord.ext import commands

class zed(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_ready(self):
		print("I am Zeddy, I'm fully running right now!")


	@commands.command(name="Zed", aliases=['zed', 'zeddy'], help="sends a random photo of my cat Zed")
	async def send_zed(self, ctx):
		zed_pic = random.choice(os.listdir("C:\\Users\\Neytan\\Desktop\\Discord Bot\\cogs\\zed"))
		await ctx.send(file=discord.File(f"C:\\Users\\Neytan\\Desktop\\Discord Bot\\cogs\\zed\\{zed_pic}"))


def setup(client):
	client.add_cog(zed(client))