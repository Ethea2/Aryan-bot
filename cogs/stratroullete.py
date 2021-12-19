import discord
import random
import json
import os
from discord.ext import commands

class strat(commands.Cog):
	def __init__(self, client):
		self.location = os.path.realpath(
			os.path.join(os.getcwd(), os.path.dirname(__file__)))
		self.json_location = os.path.join(self.location, "jsonFiles")
		self.client = client
		self.json_file = open(os.path.join(self.json_location, "strats.json"), 'r')
		self.strats = json.loads(self.json_file.read())
		

	@commands.Cog.listener()
	async def on_ready(self):
		print("I am Strat Roulette, I'm fully running right now.")
	

	@commands.command(name = "Strat Roulette", aliases = ["stratz", "strat", "sv"], help = "I give you random strats for Valorant :smile_cat:")
	async def strat(self, ctx):
		msg = f'{ctx.author.mention}'
		emoji_list = [
				":cactus:",
				":mouse:",
				":hatching_chick:", 
				":joy:",
				":joy_cat: ",
				":smirk_cat:"
				]
		strat_title, strat_description = random.choice(list(self.strats.items()))
		random_number_emoji = random.randint(0, len(emoji_list))
		random_emoji = emoji_list[random_number_emoji]
		await ctx.send(msg + f"Your strat is >:D... \n***{random_emoji}{strat_title}{random_emoji}*** \n{strat_description}")
	

def setup(client):
	client.add_cog(strat(client))