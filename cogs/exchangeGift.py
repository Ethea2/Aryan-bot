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
        user = ctx.author #gets username and tag
        userID = user.id #gets userID
        #if len(args) == 2:
        database = Database(f"{server}")
        database.add_person(userID, user, pseudonym, wishes)
        await ctx.author.send(f"<@{str(userID)}> You have successfully registered!\n **Your Pseudonym**:\n `{pseudonym}`\n **Your Wishes**:\n {wishes}")
        #else:
           # await ctx.channel.send("wrong format scrub")

#sending a DM:
    #ctx.author.send(f"hello there: {user}")
def setup(client):
    client.add_cog(ExchangeGift(client))