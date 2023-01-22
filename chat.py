import os
#allows filesystem access
import discord
#imports discord.py
from dotenv import load_dotenv
#imports load_dotenv for storing tokens in .env file
load_dotenv()
#loads .env file in current directory

TOKEN = os.getenv('TOKEN')
#defines 'TOKEN' as the bot's token using the .env file (should look something like 'TOKEN=bottoken12345' in the .env)
intents = discord.Intents.all()
#defines discord bot intents
client = discord.Client(intents=intents)
#sets intents

@client.event
#event handler
async def on_ready():
  #when bot is ready,
  channel = client.get_channel(1063679016130855004)
  #defines the channel messages are being sent to as 'channel'
  messages = []
  #defines 'messages' as an empty library
  async for message in channel.history(limit=30):
   #for every message in the channel's history with a limit of 30 (can be changed),
    messages.append(message)
    #add message to library
  for message in messages[::-1]:
  #for message in library 'messages',
    print('(' + message.author.name + '): ' + message.content)
    #print the authors name in parenthesis, with the message's content afterwards
  return
  #end execution

@client.event
#event handler
async def on_message(message):
  #when a sent message is detected,
  if message.guild.id == 1063679015547842591:
  #if the message is in the defined channel,
    print('(' + message.author.name + '): ' + message.content)
    #print the message with author

client.run(TOKEN)
#run client
