import discord
import os
import random
import datetime
import asyncio

#Token

client = discord.Client()

Alone_words = [
  "solo", "Solo", "Alone", "alone"
]
Alone_Answers = [
  "So, are you alone?. God You are Pathetic.", 
  "Alone aHa, God You are Pathetic.",
  "Hahaha Alone, God You are Pathetic."
]

idChannel = 1

Today = datetime.datetime.today().weekday()

async def AloneOnSaturday():
  await client.wait_until_ready()
  
  global idChannel
  while not client.is_closed():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if Today == 0 and current_time == "01:00:00": # Day: 0, 01:00:00, Saturday in Argentina
      await idChannel.send(file=discord.File("AloneBot.png"))
    await asyncio.sleep(1)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  global idChannel
  if message.author == client.user:
    return

  mgs = message.content

  if message.content.startswith('%Saturday'):
    await message.channel.send(file=discord.File("AloneBot.png"))
  
  if message.content.startswith('%general'):
    idChannel = message.channel
    print(idChannel)
    await message.channel.send("Nice, I got it!")

  if any(word in mgs for word in Alone_words):
    await message.channel.send(random.choice(Alone_Answers))

@client.event
async def on_message_delete(message):
  global idChannel
  await message.channel.send("Ha are you deleting a message?. God you are Pathetic.")

client.loop.create_task(AloneOnSaturday())
client.run(Token)
