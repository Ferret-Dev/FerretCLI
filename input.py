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
  while True:
    #while the bot is ready,
    user_input = input()
    #defines input from terminal as 'user input'
    channel = client.get_channel(1063679016130855004)
    #defines the channel messages are being sent to as 'channel'
    if channel.guild.id == 1063679015547842591:
      #if the channel is in the right server,
      await channel.send(user_input)
      #send 'user_input' to 'channel'

client.run(TOKEN)
#run client
