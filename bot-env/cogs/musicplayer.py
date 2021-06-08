import discord
from discord.ext import commands

class play_music(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("I'm music player, I am fully running right now!")

	@commands.command()
	async def play(self, ctx, url : str):
		voice_channel = discord.utils.get(ctx.guild.voice_channels, name = "General")
		voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
		await voiceChannel.connect()


def setup(client):
	client.add_cog(play_music(client))