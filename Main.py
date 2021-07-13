import discord
import os
import random
import datetime
import asyncio

#Token

client = discord.Client()


activeMessages = False
idChannel = 1

Today = datetime.datetime.today().weekday()

async def AloneOnSaturday():
  await client.wait_until_ready()
  #Global
  global activeMessages
  global idChannel

  while not client.is_closed():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Debug Logs
    #channel = client.get_channel(id=idChannel)
    #print(current_time)
    #print(idChannel)
    #print(activeMessages)
    
    if Today == 6 and current_time == "01:00:00": # Day: 0, 01:00:00
      await idChannel.send(file=discord.File("AloneBot.png"))
    await asyncio.sleep(1)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  global activeMessages
  global idChannel

  if message.author == client.user:
    return

  mgs = message.content

  if message.content.startswith('%saturday'):
    await message.channel.send(file=discord.File("AloneBot.png"))

  if message.content.startswith('%activeMessages'):
      if activeMessages == False:
        activeMessages = True
        await message.channel.send("I active it!")
      elif activeMessages == True:
        activeMessages = False
        await message.channel.send("I deactive it!")

  if message.content.startswith('%help'):
    await message.channel.send("You can use this commads:")
    await message.channel.send("1: %saturday")
    await message.channel.send("2: %activeMessages")
    #ask time left to saturday 

  if message.content.startswith('%general'):
    idChannel = message.channel
    print(idChannel)
    await message.channel.send("Nice, I got it!")

  if activeMessages == True:
    if any(word in mgs for word in Alone_words):
      await message.channel.send(random.choice(Alone_Answers))

@client.event
async def on_message_delete(message):
  global activeMessages
  global idChannel

  print(message.author)
  print(activeMessages)

  if activeMessages == True:
    if message.author == "Rythm#3722":
      return
    if message.author == "Rythm 2#2000":
      return
    if message.author == "Dank Memer#5192":
       return
    if message.author == "Groovy#7254":
      return
    else:
      await message.channel.send("Ha are you deleting a message?. God you are Pathetic.")

keep_alive()
client.loop.create_task(AloneOnSaturday())
client.run() #Token
