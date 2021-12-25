import discord
import random
from cogs.backend.backenddb import Database
from discord.ext import commands
from youtube_dl import YoutubeDL

class ExchangeGift(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.command(name="register", aliases=['reg', 'regi'], help="Registers you to an exchange gift.")
    async def register(self, ctx, *args):
        message = ' '.join(args)
        pseudonym = args[0]
        wishes = [wish for wish in args if wish != args[0]]
        server = ctx.message.guild.name #gets server name
        userName = ctx.message.author #gets username
        userID = ctx.author.id #gets userID
        print("*********************************************")
        print(f"{userName} has tried to register.")
        print("*********************************************")
        database = Database(f"{server}")
        database.add_person(userID, str(userName), pseudonym, wishes)
        await ctx.author.send(f"<@{str(userID)}> You have successfully registered!:confetti_ball: \n **Your Pseudonym**:sunglasses::\n `{pseudonym}`\n `Your Wishes`:star2::\n {wishes}")
        await ctx.message.delete()


    @commands.command(name="xlsjpair", help="Special pair command!")
    async def xlsjpair(self, ctx):
        server = ctx.message.guild.name
        database = Database(server)
        database.pair_people()
        await ctx.message.delete()

    
    @commands.command(name="getpair", help="Gets your pair's wishes and pseudonym")
    async def get_pair(self, ctx):
        server = ctx.message.guild.name
        userID = ctx.author.id
        database = Database(server)
        pair_dictionary = database.get_pair(userID)
        if pair_dictionary == False:
            await ctx.author.send("You do not have a pair")
        elif type(pair_dictionary) == type('hello'):
            await ctx.send("Pairings have not been made at this moment!")
        else:
            await ctx.author.send(f"<@{str(userID)}> Your pair is: \n:sunglasses:`{pair_dictionary['pseudonym']}`:sunglasses: \n And his/her wishes are: \n :star2:`{pair_dictionary['wishes']}`:star2:")
        await ctx.message.delete()


    @commands.command(name="xmas")
    async def xmas(self, ctx):
        userID = ctx.author.id
        hate = ['FOOKIN RETARD', 'FOOKIN ASSHOLE', 'FOOKIN CRAP', 'KEK LMAO']
        merry_blank = ['CRISIS', 'XMAS', 'CHRISTMAS']
        random_hate = random.choice(hate)
        await ctx.send(f"<@{str(userID)}> MERRY {random.choice(merry_blank)} YOU {random_hate}. :low_brightness:")

#sending a DM:
    #ctx.author.send(f"hello there: {user}")
def setup(client):
    client.add_cog(ExchangeGift(client))