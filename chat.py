import os
import discord
import asyncio
from discord.ext import commands
import threading

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  channel = client.get_channel(1063679016130855004)
  messages = []
  async for message in channel.history(limit=10):
    messages.append(message)
  for message in messages[::-1]:
    print('(' + message.author.name + '): ' + message.content)
  return

@client.event
async def on_message(message):
  if message.guild.id == 1063679015547842591:
    print('(' + message.author.name + '): ' + message.content)

client.run(TOKEN)
