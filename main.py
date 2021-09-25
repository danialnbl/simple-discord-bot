import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

#import all of the cogs
from music import music

bot = commands.Bot(command_prefix="?", intent = discord.Intents.all())

bot.add_cog(music(bot))

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

keep_alive()
bot.run(os.getenv('TOKEN'))