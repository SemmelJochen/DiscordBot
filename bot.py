# -*- coding: utf-8 -*-

"""
Base Projekt by Valentin B: https://gist.github.com/vbe0201/ade9b80f2d3b64643d854938d40a0a2d
Customized by SemmelJochen

Requirements:

Python 3.5+
pip install -U discord.py pynacl youtube-dl python_dotenv

You also need FFmpeg in your PATH environment variable or the FFmpeg.exe binary in your bot's directory on Windows.
"""
 
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from cogs import audio_cog


load_dotenv()

bot = commands.Bot('!', description='DAZN Arschfick bot v.2')

bot.add_cog(audio_cog.Music(bot))


@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

@bot.event
async def on_disconnect():
    bot.run(os.getenv('DISCORD_TOKEN'))
    return


bot.run(os.getenv('DISCORD_TOKEN'))