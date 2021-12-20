import discord
import json
from discord.ext import commands
from youtube_dl import YoutubeDL

class ExchangeGift(commands.Cog):
    def __init__(self,client):
        self.client = client


    #def addPerson(self, serverID, userID, name, wish):


    @commands.command(name="register", aliases=['reg', 'regi'], help="Registers you to an exchange gift.")
    async def register(self, ctx, *args):
        message = ' '.join(args)
        user = ctx.author #gets username and tag
        userID = user.id #gets userID
        if len(args) == 2:
            await ctx.channel.send(f"<@{str(userID)}> Mentioned you!\n **Your Pseudonym**:\n `{args[0]}`\n **Your Wishes**:\n {args[1]}")
        else:
            await ctx.channel.send("wrong format scrub")

#sending a DM:
    #ctx.author.send(f"hello there: {user}")
def setup(client):
    client.add_cog(ExchangeGift(client))