import discord
import random
from discord.ext import commands

class EightBall(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.fil_replies = [
					'Totoo, walang kaduda-duda :sob:!',
					'Kahit hindi na ako mag dalawang isip, ***OO*** :smiling_imp:',
					'Siguradong sigurado :zany_face: ',
					'Kahit man gusto kong sabihing hind, *oo* talaga eh :weary: :weary:',
					'oo',
					'SO TRULALOOOOOO :rofl: :rofl:',
					'Shatap, I need to pokus...\n :regional_indicator_o: :regional_indicator_o: ',
					'Yep :regional_indicator_o: :regional_indicator_o: Totoo',
					'**OO** AYAN SINABI KO NA YUNG GUSTO MONG MARINIG :face_with_symbols_over_mouth:',
					'duhh, oo :wink:',
					'**OO**, kaya tigilan mo na ako :confounded: yaw q na :confounded:',
					#negatives
					'Wag mo nang asahan :frowning:',
					'Sabi ng mga kaibigan mo hindi daw eh :ghost: :ghost: :ghost:',
					'Dahil boring tanong mo, hinde :skull:',
					'Hindi :pensive:',
					'**SPITS** Hindi **SPITS**',
					#Neutral
					'Wait brb, mag tiktok muna ako :v:',
					'Gamit na gamit na ako, mamaya ulit rest lang me :smiling_face_with_tear: ',
					'Busy ako eh, mamaya mo na ako guluhin :face_with_symbols_over_mouth: ',
					'Mamaya mo na ako guluhin :confounded: ',
					'Nakakatamad yung tanong mo, mamaya nalang ulit :crying_cat_face:']

		self.eng_replies = [
					'i\'m surer than a sewer :sweat_drops: :sweat_drops: ',
					'Without a doubt!! :punch: ',
					'Yes duh :rolling_eyes:! Why even ask :face_with_symbols_over_mouth:?',
					'Boring question gets a boring \'yes\' :yawning_face: ',
					'It\' true :eyes:',
					'I don\'t want to admit it, but yes :expressionless:',
					'Yes cutie :pleading_face: :point_right: :point_left:',
					':regional_indicator_y: :regional_indicator_e: :regional_indicator_s: \n:regional_indicator_s: :regional_indicator_c: :regional_indicator_r: :regional_indicator_u: :regional_indicator_b:',
					'If it\'s not too obvious, ye :cold_face: ',
					'Sadly, yes :pensive:',
					'Appa, **YEP YEP** :man_bald: ',
					#negatives
					':regional_indicator_n: :regional_indicator_o: \n:regional_indicator_s: :regional_indicator_c: :regional_indicator_r: :regional_indicator_u: :regional_indicator_b: ',
					'NO. POOR U :rofl:',
					'No :eye: :lips: :eye:',
					'You\'re a disgrace. No :smirk_cat: ',
					'**SPITS** NOPE **SPITS**',
					#Neutral
					'Give me a break, I need 30 seconds so I can finish :sweat_drops: :sweat_drops: giving you your destiny',
					'FUCK OFF :face_with_symbols_over_mouth: :face_with_symbols_over_mouth:, ask me later teehee :laughing:',
					'I really can\'t guess, what you asked is too hard to answer. Ask me again later',
					'I can\'t be bothered to even tell you :yawning_face: ',
					'Not feeling it right now, ask again later :no_mouth:']


	@commands.Cog.listener()
	async def on_ready(self):
		print("I am 8ball, I'm fully running right now!")


	@commands.command(name = "Filipino 8ball", aliases = ['eytbol', '8ballf', '8f'], help = "8ball ako sa filipino :8ball:")
	async def eytbol(self, ctx, *, question):
		msg = f'{ctx.author.mention}'
		await ctx.send(msg + "{}".format(random.choice(self.fil_replies)))


	@commands.command(name = "8ball", aliases = ['eightball', '8e'], help = "I'm 8ball in english :8ball:")
	async def eightbol(self, ctx, *, question):
		msg = f'{ctx.author.mention}'
		await ctx.send(msg + "{}".format(random.choice(self.eng_replies)))

		
def setup(client):
	client.add_cog(EightBall(client))