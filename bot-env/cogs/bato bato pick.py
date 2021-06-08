import discord
import random
from discord.ext import commands

class bbp(commands.Cog):
		def __init__(self, client):
			self.client = client

		@commands.Cog.listener()
		async def on_ready(self):
			print("I am BBP, I'm fully running right now!")

		@commands.command(aliases = ['bbp', 'BBP'])
		async def bato_bato_pick(self, ctx, *,choice = '-'):
			msg = f'{ctx.author.mention}'
			my_turn = ['gunting',
						'papel',
						'bato']
			emoji = [':scissors:',
						':newspaper:',
						':rock:']
			if choice == 'gunting':
				random_attack = random.randint(0,2)
				attack = my_turn[random_attack]
				if attack == my_turn[0]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nNAG TIE TAYO! :face_with_symbols_over_mouth:".format(emoji[0],my_turn[0]))
				elif attack == my_turn[1]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nNANALO KA WTF, U NERD :nerd:!".format(emoji[1],my_turn[1]))
				elif attack == my_turn[2]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nI FOOKIN WIN U SCRUB :innocent:!".format(emoji[2],my_turn[2]))
			elif choice == 'papel':
				random_attack = random.randint(0,2)
				attack = my_turn[random_attack]
				if attack == my_turn[0]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nTALO KA NGAYON NUB :smiling_imp:!".format(emoji[0],my_turn[0]))
				elif attack == my_turn[1]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nANG CORNY NAG TIE PA TAYO :unamused:!".format(emoji[1],my_turn[1]))
				elif attack == my_turn[2]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nTAE KA NATALO MO KO :cry:!".format(emoji[2],my_turn[2]))
			elif choice == 'bato':
				random_attack = random.randint(0,2)
				attack = my_turn[random_attack]
				if attack == my_turn[0]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nTANGINA TALO PA AKO :face_with_symbols_over_mouth:!".format(emoji[0],my_turn[0]))
				elif attack == my_turn[1]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nEZ MO NAMAN KALABAN :joy:!".format(emoji[1],my_turn[1]))
				elif attack == my_turn[2]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nBAKIT YAN PINILI MO? WALA TULOY NANALO :confounded:!".format(emoji[2],my_turn[2]))
			else:
				await ctx.send(msg + " u gotta pick something scrub \nbato \npapel \ngunting")


def setup(client):
	client.add_cog(bbp(client))