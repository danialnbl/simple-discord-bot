import discord
import os
from discord.ext import commands
import music
from keep_alive import keep_alive

cogs = [music]

client = commands.Bot(command_prefix="!", intent = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

    
keep_alive()
client.run(os.getenv('TOKEN'))