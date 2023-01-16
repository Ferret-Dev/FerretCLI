import os
import discord
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  while True:
    user_input = input()
    channel = client.get_channel(1063679016130855004)
    if channel.guild.id == 1063679015547842591:
      await channel.send(user_input)

client.run(TOKEN)
