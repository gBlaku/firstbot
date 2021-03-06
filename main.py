import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("I don't like this place....")

@client.event
async def on_message(message):
  if message.author == client.user:
    return  

  if message.content.startswith('!'):
    await message.channel.send('You summoned me')

  
client.run(os.getenv('TOKEN'))
