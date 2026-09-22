import discord
from discord.ext import commands

class LosTrumpet(discord.Client):
    async def on_ready(self):
        print('logged in as', self.user)
    
    async def on_message(self, message):
        userid = self.user.id

        def loop(voice):
            if not voice.is_connected():
                return

            trumpet = discord.FFmpegPCMAudio("l4d2trumpet.mp3")
            voice.play(trumpet, after=lambda e:(
                print(f"{e}")
                if e
                else self.loop.create_task(loopmyass(voice))
             ),
            )        

        async def loopmyass(voice):
            loop(voice)

        if message.content == f"<@{userid}> trumpet":
            # set this to your own userid... or don't! let everyone access it
            if message.author.id != 1:
                await message.reply("kiss my ass")
            else:
                if message.author.voice and message.author.voice.channel:
                    channel = message.author.voice.channel
                    voice = await channel.connect()
                    loop(voice)
        if message.content == f"<@{userid}> shut the fuck up":
            # do the same here
            if message.author.id != 1:
                await message.reply("kiss my ass")
            else:
                if message.guild:
                    voice = discord.utils.get(self.voice_clients, guild__id=message.guild.id)
                else:
                    voice = discord.utils.get(self.voice_clients, channel__id=message.channel.id)
                if voice and voice.is_connected():
                    await voice.disconnect()
                else:
                    print("EAT DICK")
                    

trumpet = LosTrumpet()
trumpet.run('SMEGMABALLS')
