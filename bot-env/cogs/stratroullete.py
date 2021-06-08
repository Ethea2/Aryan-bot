import discord
import random
from discord.ext import commands

class strat(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("I am Strat Roulette, I'm fully running right now.")

	@commands.command()
	async def strat(self, ctx):
		msg = f'{ctx.author.mention}'
		strat_title = [
						#0
						"One mic",
						#1
						"Sound effects",
						#2
						"Retakes are fun",
						#3
						"Smoke break",
						#4
						"One at a time",
						#5
						"Gambling",
						#6
						"Just here in my garage",
						#7
						"Glass cannon",
						#8
						"Where are they coming from?",
						#9
						"No abilities",
						#10
						"Only abilities",
						#11
						"Knives out",
						#12
						"Doppelgänger",
						#13
						"Gunswap",
						#14
						"I think my W key is stuck",
						#15
						"How do I stand up?",
						#16
						"Is that a tornado?",
						#17
						"Follow the leader",
						#18
						"Wild west",
						#19
						"Trickshot",
						#20
						"Confusing callouts",
						#21
						"Fnatic on Inferno",
						#22
						"The fakeout",
						#23
						"Woah a teleporter",
						#24
						"Evasive maneuvers",
						#25
						"Sneaky-Beaky like",
						#26
						"Odin rush",
						#27
						"Motivational speech",
						#28
						"Ropes scare me",
						#29
						"Protect the president"
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
		"""Your whole team must buy only Sheriffs. Armor is allowed, but no other guns. Extra points if you can use a western accent while making callouts.""",
		
		#Trickshots
		"""Everytime you encounter an enemy, you must 360 before you are allowed to shoot them.""",
		
		#Confusing callouts
		"""Play the round normally, however, you cannot use any normal callouts. Preferably use callouts that don't exist on this map, callouts from other games/maps,
or just very broadly describe what you are trying to callout. Sounding confident is key for this strat.""",
		
		#Fnatic on Inferno
		"""Each teammate can only have a Classic and armor. They must crouch walk the entire way to A site going long. You may play normally if you get the bomb planted.""",

		#The fakeout
		"""Each teammate must buy every ability that they possibly can. Rush towards one of the sites, and use all of your abilities as fast as you can on the site. 
Then quickly retreat and plant the spike at a different site.""",

		#Woah a teleporter
		"""Everyone on your team must have used a teleporter at least 3 times each before you are allowed to plant the spike.""",

		#Evasive maneuvers
		"""You must jump every time you turn or peak a corner.""",

		#Sneaky-Beaky like
		"""Your team can only buy surpresssed weapons and no one on the team is allowed to speak for the entire round.""",

		#Odin rush
		"""If your team has the funds to support this, every player must buy an Odin and rush the enemy team as a group, doesn't matter if you are attacking or defending.
Buy an Ares if you can't afford an Odin.""",

		#Motivational speech
		"""Elect one player on your team to give a motivational speech at the start of the round. No one is allowed to leave spawn until the speech is finished. 
Once the speech is over, your whole team must rush one of the sites.""",

		#Ropes scare me
		"""You must play the entire round without using the ropes at all.""",

		#Protect the president
		"""Elect one teammate to be the 'President' and this player must carry the spike. The President is not allowed to have any guns or abilities, 
just armor. Your team must surround the president and protect him/her for the entire round."""
		]

		random_number = random.randint(0, len(strat_title))
		await ctx.send(msg + f"Your strat is >:D... \n***{strat_title[random_number]}*** \n{strat_description[random_number]}")

def setup(client):
	client.add_cog(strat(client))