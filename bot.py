# -*- coding: utf-8 -*-

"""
Copyright (c) 2019 Valentin B.

A simple music bot written in discord.py using youtube-dl.

Though it's a simple example, music bots are complex and require much time and knowledge until they work perfectly.
Use this as an example or a base for your own bot and extend it as you want. If there are any bugs, please let me know.

Requirements:

Python 3.5+
pip install -U discord.py pynacl youtube-dl

You also need FFmpeg in your PATH environment variable or the FFmpeg.exe binary in your bot's directory on Windows.
"""

import os
from discord.ext import commands
from dotenv import load_dotenv
from cogs import audio_cog


load_dotenv()

bot = commands.Bot('!', description='DAZN Arschfick bot v.2')

bot.add_cog(audio_cog.Music(bot))


@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

bot.run(os.getenv('DISCORD_TOKEN'))