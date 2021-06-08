import discord
from discord.ext import commands

class ping(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("I am PING, I'm fully running right now!")

	@commands.command()
	async def ping(self, ctx):
		msg = f'{ctx.author.mention}'
		latency = self.client.latency
		true_latency = latency * 1000
		await ctx.send(msg + ' YOUR PONG IS {}ms!'.format(round(true_latency)))
def setup(client):
	client.add_cog(ping(client))