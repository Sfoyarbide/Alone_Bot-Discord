import discord
import os
import random
import datetime
import asyncio

Token = os.environ['TOKEN']

client = discord.Client()

Alone_words = [
  "solo", "Solo", "Alone", "alone"
]
Alone_Answers = [
  "So, are you alone?. God You are Pathetic.", 
  "Alone aHa, God You are Pathetic.",
  "Hahaha Alone, God You are Pathetic."
]

Today = datetime.datetime.today().weekday()

async def AloneOnSaturday():
  await client.wait_until_ready()
  channel = client.get_channel() # Put id channel
  while not client.is_closed():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    if Today == 0 and current_time == "01:00:00":
      await channel.send(file=discord.File("AloneBot.png"))
    await asyncio.sleep(1)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  mgs = message.content
    
  if message.content.startswith('%Saturday'):
    await message.channel.send(file=discord.File("AloneBot.png"))

  if any(word in mgs for word in Alone_words):
    await message.channel.send(random.choice(Alone_Answers))

@client.event
async def on_message_delete(message):
  await message.channel.send("Ha are you deleting a message?. God you are Pathetic.")

client.loop.create_task(AloneOnSaturday())
client.run(Token)