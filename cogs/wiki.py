import discord
import wikipedia
from discord.ext import commands

class wiki(commands.Cog):
	def __init__(self, client):
		self.client = client


	def get_image(self, query):
		for image in wikipedia.WikipediaPage(query).images:
			if image.endswith('jpg') or image.endswith('jpeg') or image.endswith('PNG') or image.endswith('JPG'):
				return image
				break
			else:
				return "**Could not find an image for the page.**"


	@commands.Cog.listener()
	async def on_ready(self):
		print("Wiki bot is running!")


	@commands.command(name="Search", aliases=['w','wiki','search'], help="Searches wikipedia for whatever you need!")
	async def search_wiki(self, ctx, *args):
		query = " ".join(args)

		try:
			await ctx.send(f">>> {wikipedia.summary(query, sentences=2, auto_suggest=False)}\n {self.get_image(query)}")
		except:
			await ctx.send(">>> Sorry I couldn't find what you're looking for :c")


	@commands.command(name="Image", aliases=["image", 'isearch'], help="Gives you the first 3 images in the wikipage you searched.")
	async def search_image(self, ctx, *args):
		query = " ".join(args)
		try:
			wiki_images = wikipedia.WikipediaPage(query).images
			images = [image for image in wiki_images if image.endswith('gif') or image.endswith('PNG') or image.endswith('JPG') or image.endswith('jpg')]
			searched_images = '\n'.join(images[:3])
			await ctx.send(searched_images)
		except:
			await ctx.send(">>> I couldn't find the images you're searching for! :c")


	@commands.command(name="Suggest", aliases=['suggest','list'], help="Suggests a list of wikipedia searches.")
	async def suggest_wiki(self, ctx, *args):
		query = " ".join(args)

		searching = wikipedia.search(query)
		print(searching)
		searched_list = ""
		for item in searching:
			searched_list += f"{item}\n"
		try:
			await ctx.send(f">>> **You can search for:** \n{searched_list}")
		except:
			await ctx.send(">>> Sorry couldn't find anything about it T-T")
			


	@commands.command(name="Language Set", aliases=["setlang", "langset"], help="Changes the wikipedia language.")
	async def language_set(self, ctx, lang_key):
		wiki_keys = wikipedia.languages().keys()
		if lang_key in wiki_keys:
			wikipedia.set_lang(lang_key)
			await ctx.send(f">>> The language has successfully been set to **{wikipedia.languages()[lang_key]}**")
		else:
			await ctx.send(">>> The language you tried to choose, does not exist!\n If you don't know the languages available \\helplang")


	@commands.command(name="Language Help", aliases=["helplang", "langhelp"], help="Gives you the url to the language pages.")
	async def help_lang(self, ctx):
		language_list = list(wikipedia.languages().items())
		key_lang_list = []
		for key, lang in language_list[:10]:
			key_lang = key + " " + lang
			key_lang_list.append(key_lang)

		top10 = '\n'.join(key_lang_list)

		await ctx.send(f">>> **The first 10 available languages in Wikipedia:**\n{top10}\nto see all the language available go here https://meta.wikimedia.org/wiki/List_of_Wikipedias")
		#await ctx.send("https://meta.wikimedia.org/wiki/List_of_Wikipedias")



def setup(client):
	client.add_cog(wiki(client))