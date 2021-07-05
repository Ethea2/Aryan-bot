import discord
import wikipedia
from discord.ext import commands

class wiki(commands.Cog):
	def __init__(self, client):
		self.client = client


	def wiki_summary(self, query):
		try:
			return wikipedia.summary(query, sentences=2)
		except:
			return "Sorry I couldn't find what you're looking for :c"


	@commands.Cog.listener()
	async def on_ready(self):
		print("Wiki bot is running!")


	@commands.command(name="Search", aliases=['w','wiki','search'], help="Searches wikipedia for whatever you need!")
	async def searc_wiki(self, ctx, *args):
		query = " ".join(args)

		try:
			await ctx.send(wikipedia.summary(query, sentences=2))
		except:
			await ctx.send("Sorry I couldn't find what you're looking for :c")


	@commands.command(name="Suggest", aliases=['suggest','list'], help="Suggests a list of wikipedia searches")
	async def suggest_wiki(self, ctx, *args):
		query = " ".join(args)

		searching = wikipedia.search(query)
		print(searching)
		searched_list = ""
		for item in searching:
			searched_list += f"{item}\n"
		try:
			await ctx.send(f"**You can search for:** \n{searched_list}")
		except:
			await ctx.send("Sorry couldn't find anything about it T-T")




def setup(client):
	client.add_cog(wiki(client))