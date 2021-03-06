import discord
import os
import requests
import json


client = discord.Client()



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)










@client.event
async def on_ready():
  print("I'm online! My ID is {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return  

  if message.content.startswith('!quote'):
    randomQuote = get_quote()
    await message.channel.send(randomQuote)

  
client.run(os.getenv('TOKEN'))