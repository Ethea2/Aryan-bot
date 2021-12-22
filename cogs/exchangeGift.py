import discord
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
        database = Database(f"{server}")
        database.add_person(userID, str(userName), pseudonym, wishes)
        await ctx.author.send(f"<@{str(userID)}> You have successfully registered!\n **Your Pseudonym**:\n `{pseudonym}`\n **Your Wishes**:\n {wishes}")



    @commands.command(name="xlsjpair", help="Special pair command!")
    async def xlsjpair(self, ctx):
        server = ctx.message.guild.name
        database = Database(server)
        database.pair_people()


#sending a DM:
    #ctx.author.send(f"hello there: {user}")
def setup(client):
    client.add_cog(ExchangeGift(client))