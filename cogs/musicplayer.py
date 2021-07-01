import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

class play_music(commands.Cog):
	def __init__(self, client):
		self.client = client

		#all the music related stuff
		self.is_playing = False

		# 2d array containing [song, channel]
		self.music_queue = []
		self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
		self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

		self.now_playing = ""

		self.vc = ""


	def search_youtube(self, item):
		with YoutubeDL(self.YDL_OPTIONS) as ydl:
			try:
				info = ydl.extract_info(f"ytsearch:{item}", download = False)['entries'][0]
			except Exception:
				return False

		return {'source': info['formats'][0]['url'], 'title': info['title']}

	def play_next(self):
		if len(self.music_queue) > 0:
			self.is_playing = True

			m_url = self.music_queue[0][0]['source']

			self.music_queue.pop(0)

			self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
			
		else:
			self.is_playing = False

	async def play_music(self):
		if len(self.music_queue) > 0:
			self.is_playing = True

			m_url = self.music_queue[0][0]['source']
			if self.vc == "" or not self.vc.is_connected() or self.vc == None:
				self.vc = await self.music_queue[0][1].connect()

			else:
				await self.vc.move_to(self.music_queue[0][1])

			print(self.music_queue)

			self.music_queue.pop(0)

			self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
			
		else:
			self.is_playing = False

	@commands.command(name = "play", aliases = ['pkay', 'p', 'alexaplay'], help = "Plays a song")
	async def play(self, ctx, *args):
		query = " ".join(args)
		voice_channel = ctx.author.voice.channel

		if voice_channel is None:
			await ctx.send("Please connect to a voice channel u fookin scrub!")

		else:
			song = self.search_youtube(query)
			if type(song) == type(True):
				await ctx.send("Could not play the song. Incorrect format try another `keyword`. This could be due to playlist or a livestream format.")	
			else:
				self.music_queue.append([song, voice_channel])
				await ctx.send(f"`{query}` has been searched and added to the queue")
				
				if self.is_playing == False:
					await self.play_music()



	@commands.command(name = "disconnect", aliases = ['disc', 'd', 'quit'], help = "Disconnects the bot")
	async def leave(self, ctx):
		if self.vc == "" or not self.vc.is_connected() or self.vc == None:
			await ctx.send("I'm not even connected, watcha trynna do?")
		else:
			self.vc.stop()
			await ctx.voice_client.disconnect()



	@commands.command(name = "queue", aliases = ['que', 'q'], help = "Shows you the list of the songs in queue ")
	async def queue(self, ctx):
		retval = ""

		for i in range(0, len(self.music_queue)):
			queue_number = i+1
			retval += f"`{queue_number}:` "+ self.music_queue[i][0]['title'] + "\n"

		print(retval)

		if retval != "":
			# await ctx.send(f"***(now playing)***:{now_playing} \n**The song queue is:**\n{retval}")
			await ctx.send(f"**The song queue is:**\n{retval}")
		else:
			await ctx.send("No music in queue")	

	@commands.command(name = "skip", aliases = ['s'], help = "Skips the current song playing")
	async def skip(self, ctx):
		if self.vc != "" and self.vc:
			self.vc.stop()
			# self.music_queue.pop(0)
			await self.play_music()


def setup(client):
	client.add_cog(play_music(client))