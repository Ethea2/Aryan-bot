import discord
import random
from discord.ext import commands

class AMA(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("I am AMA, I'm fully running right now!")

	@commands.command(aliases = ['AMA', 'ama'])
	async def askme(self, ctx, *, question):
		msg = f'{ctx.author.mention}'
		replies = ['Totoo, walang kaduda-duda!',
					'Kahit hindi na ako mag dalawang isipm, oo >:D',
					'Siguradong sigurado :P',
					'Nagtanong ka pa? Eh, halata namang OO!!!',
					'OO BWUAHAHAHA',
					'malamang HAHAHA!',
					'Ang sabi ng mga bituin ay oo!',
					'Nakikita ko na nga oh',
					'Oo di pa ba halata?',
					'Hindi ko na kailangan mag dalawang isip, oo',
					'Malamang OO >:D',
					#negatives
					'Wag mo nang asahan',
					'Sabi ng mga bituin ay... HINDI >:D',
					'Wala akong tiwalang mangyayare yan :c',
					'Nagtanong ka pa? Eh, halata namang hindi >:c nakakakahiya ka',
					'**SPITS** Hindi **SPITS**',
					#Neutral
					'Mas mabuti nang hindi ko sabihin sayo to ngayon',
					'Subukan mo ulit mag tanong',
					'Hindi ko talaga mahulaan eh',
					'Mamaya mo na ako tanungin',
					'Tinanatamad ako ngayon eh, mamaya na']
		await ctx.send(msg + " :regional_indicator_k: {}".format(random.choice(replies)))
def setup(client):
	client.add_cog(AMA(client))