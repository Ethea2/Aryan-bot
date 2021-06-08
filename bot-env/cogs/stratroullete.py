import discord
import random
from discord.ext import commands

class strat(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("Strat Roulette is running")

	@commands.command()
	async def strat(self, ctx):
		msg = f'{ctx.author.mention}'
		strat_title = [
						#0
						"***One mic***",
						#1
						"***Sound effects***",
						#2
						"***Retakes are fun",
						#3
						"***Smoke break***",
						#4
						"***One at a time***"
						#5
						"***Gambling***"
						#6
						"***Just here in my garage***"
						#7
						"***Glass cannon***"
						#8
						"***Where are they coming from?***"
						#9
						"***No abilities***"
						#10
						"***Only abilities***"
						#11
						"***Knives out***"
						#12
						"***Doppelgänger***"
						#13
						"***Gunswap***"
						#14
						"***I think my W key is stuck***"
						#15
						"***How do I stand up?***"
						#16
						"***Is that a tornado?***"
						#17
						"***Follow the leader***"
						#18
						"***Wild west***"
						]
		strat_description = [
		#one mic
		"""Whoever is at the bottom of the scoreboard for your team is the only person allowed to use their mic this round. They must attempt to make callouts 
for all of their teammates. They clearly aren't getting kills anyway, so don't worry if this hinders their playing.""",

		#sound effects
		"""You must make sound effects for every action that you do in game, such as shooting guns, using abilities, and of course: taking the teleporter.
Try to use the teleporter as much as possible this round, ideally making a different sound each time.""",

		#retakes are fun
		"""Your whole team must hide in spawn until the spike has been planted. 
You are then allowed to leave spawn and play normally.""",

		#Smoke break
		"""Your whole team must start the round in Hookah and hold it for as long as possible. 
You may only leave if the spike has been planted.""",

		#One at a time
		"""Only one player can leave spawn at a time, the rest of the team must do their best to hide in spawn.""",

		#Gambling
		"""Your whole team must go to one spikesite to defend. You've got a 1/3 chance to choose the right one, goodluck.""",
		
		#Just here in my garage
		"""Your whole team must make it into garage and are not allowed to leave unless the spike is planted. For motivation, 
remember you are protecting your KNOWLEDGE and brand-new lamborghini.""",

		#Glass cannon
		"""Each teammate must buy the most expensive weapon they can afford, but they are not allowed to have any armor.""",

		#Where are they coming from?
		"""Everyone on your team must put their headset on backwards for the entire round.""",

		#No abilities 
		"""Players must not use their abilities for the entire round""",

		#Abilities only
		"""Players cannot shoot their guns for the entire round. ONLY ABILITIES ARE ALLOWED!""",

		#Knives out
		"""You are only allowed to move if you are currently holding your knife. If you would like to shoot, 
		you must stand stationary and cannot make any movement until you pull your knife back out.""",

		#Doppelgänger
		"""If there is an enemy on the other team with the same agent as you, you must ignore all other enemies until you have killed your doppelgänger.
 If you don't have a doppelgänger, try to let your teammates kill theirs before killing anyone.""",

 		#Gunswap
		"""Everytime you kill an enemy, you must pick up their gun and use it for your next kill. 
It doesn't matter what gun they had or how hard it will be to pick up, you cannot get a kill with the exact same gun more than once.""",
		
		#I think my W key is stuck
		"""you must hold the W key for the entire round and you are not allowed to walk or stop""",
		
		#How do I stand up?
		"""Everyone on your team must play the entire round crouched, you can not standup at any time for any reason.""",
		
		#Is that a tornado?
		"""Everytime a teammate dies, they must constantly blow into their mic simulating a wind sound. They cannot stop until the round is over.""",

		#Follow the leader
		"""Elect a teammate to be the leader, your whole team must move in a line everywhere that they travel following the leader. No one can stray away from the line.""",

		#Wild west
		"""Your whole team must buy only Sheriffs. Armor is allowed, but no other guns. Extra points if you can use a western accent while making callouts."""
		]

		random_number = random.randint(0, len(strat_title))
		await ctx.send(msg + f"Your strat is >:D... \n{strat_title[random_number]} \n{strat_description[random_number]}")





def setup(client):
	client.add_cog(strat(client))