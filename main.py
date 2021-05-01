import discord
import time
import re
import random
import asyncio
owobot_fuse = True
seralin = False
owobot_running=True
owobot_sleep=[16,24]
owobot_delay=[2,4]
client=discord.Client()
class bot:
  owoid=408785106942164992
  channel=id of the channel here
  token=" user token here "
  commands=[
    "owo hunt",
    "owo battle"
    ]
  funcom=[
    "owo zoo",
    "owo money",
    "owo sell all",
    "owo cf 2",
    "owo sell uncommonweapons",
    "owo sell commonweapons",
    "owo sell epicweapons",
    "owo sell mythicweapons",
    "owo level",
    "owo lb all",
    "owo crate all",
    ]
  class find:
    def money(text):
      return re.search('\**__(.*?)\__**', text).group(1).replace(',', '')
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
async def typing():
  await client.wait_until_ready()
  await asyncio.sleep(2)
  chan=client.get_channel(bot.channel)
  x=True
  with chan.typing():
    while x:
      await asyncio.sleep(3600)
async def owobot2():
  await client.wait_until_ready()
  channelob=client.get_channel(bot.channel)
  print(f"{at()}{bot.color.okgreen} [AÇILIYOR] {bot.color.reset} bot2 çağırıldı (owobot2())")
  global owobot_fuse, owobot_running
  while owobot_running:
       if owobot_fuse:
         fc=random.choice(bot.funcom)
         print(f"{at()}{bot.color.okblue} [SENT] {bot.color.reset} {fc}")
         await channelob.send(fc)
         x=random.randint(80, 300)
         print(f"{at()}{bot.color.okcyan} [BEKLİYOR] {bot.color.reset} bot2, {bot.color.warning}{bot.color.bold}{x}{bot.color.reset} saniye bekliyor")
         await asyncio.sleep(x)
  print(f"{at()}{bot.color.fail} [SONLANDIRILDI] {bot.color.reset} bot2 çöktü / kapatıldı (owobot2())")
async def owobot():
  await client.wait_until_ready()
  await asyncio.sleep(2)
  channelob=client.get_channel(bot.channel)
  print(f"{at()}{bot.color.okgreen} [AÇILIYOR] {bot.color.reset} bot1 çağırıldı (owobot())")
  global owobot_fuse, owobot_running, owobot_delay, owobot_sleep
  while owobot_running:
       if owobot_fuse:
        command=random.choice(bot.commands)
        print(f"{at()}{bot.color.okblue} [SENT] {bot.color.reset} {command}")
        await channelob.send(command)
        x=random.randint(owobot_delay[0], owobot_delay[1])
        print(f"{at()}{bot.color.okcyan} [BEKLİYOR] {bot.color.reset} bot1, {bot.color.warning}{bot.color.bold}{x}{bot.color.reset} saniye bekliyor")
        await asyncio.sleep(x)
        time.sleep(random.randint(100,999)/1000)
        if owobot_fuse:
          command=random.choice(bot.commands)
          print(f"{at()}{bot.color.okblue} [SENT] {bot.color.reset} {command}")
          await channelob.send(command)
          x=int(random.randint(int(owobot_sleep[0]), int(owobot_sleep[1])))
          print(f"{at()}{bot.color.okcyan} [BEKLİYOR] {bot.color.reset} bot1, {bot.color.warning}{bot.color.bold}{x}{bot.color.reset} saniye bekliyor")
          await asyncio.sleep(x)
          time.sleep(random.randint(100,999)/1000)
  print(f"{at()}{bot.color.fail} [SONLANDIRILDI] {bot.color.reset} bot1 çöktü / kapatıldı (owobot())")
  
  
async def owodead():
  await client.wait_until_ready()
  await asyncio.sleep(3)
  channelob=client.get_channel(bot.channel)
  print(f"{at()}{bot.color.okgreen} [AÇILIYOR] {bot.color.reset} bot3 çağırıldı (owodead())")
  global owobot_fuse
  while owobot_running:
    if owobot_fuse:
        messages=0
        print(f"{at()}{bot.color.okcyan} [BEKLİYOR] {bot.color.reset} bot3, 10 saniye bekliyor")
        await asyncio.sleep(10)
        async for x in channelob.history(limit=6):
            if x.author.id == bot.owoid:
              messages=messages+1
        if messages==0:
          exit()
          print('sigorta attı')
  print(f"{at()}{bot.color.fail} [SONLANDIRILDI] {bot.color.reset} bot2 çöktü / kapatıldı (owodead())")
async def owogems():
  global owobot_fuse, owobot_running
  await client.wait_until_ready()
  channelob=client.get_channel(bot.channel)
  while owobot_running:
    if owobot_fuse:
       x =50
       while x<=80:
         print(f"{at()}{bot.color.okcyan} [BEKLİYOR] {bot.color.reset} bot4, 12 saniye bekliyor")
         await asyncio.sleep(12)
         print(f"{at()}{bot.color.okblue} [SENT] {bot.color.reset} owo use {x}")
         await channelob.send(f"owo use {x}")
         x=x+1
       print(f"{at()}{bot.color.okcyan} [BEKLİYOR] {bot.color.reset} bot4, 2400 saniye bekliyor")
       await asyncio.sleep(2400)
async def waitor():
 y=True
 while y:
  await asyncio.sleep(900)
  owobot_fuse=False
  print(f"{at()}{bot.color.warning} [BEKLİYOR] {bot.color.reset} bütün eylemler, 5 dk mola")
  await asyncio.sleep(300)
  owobot_fuse=True
@client.event
async def on_connect():
 bot_running=True
 print(f"{at()}{bot.color.purple}{bot.color.bold} [BAĞLANILDI]{bot.color.reset} {bot.color.bold}{client.user}{bot.color.reset} olarak giriş yapıldı")
    
@client.event
async def on_message(message: discord.Message):
  global owobot_fuse, owobot_sleep, owobot_delay
  if message.channel.id == bot.channel:
    #if message is sent to owo channel
    if message.author.id == client.user.id:
      if message.content.startswith("x!i"):
        mesaj=message.content[4:]
        if mesaj.startswith("stop"):
          bot_fuse=False
        if mesaj.startswith("start"):
          bot_fuse=True
        if mesaj.startswith("sleep"):
          mesaj=mesaj.split()
          if len(mesaj) != 3:
            return
          if mesaj[0] == 'sleep':
            print(f"{at()}{bot.color.okcyan} [UPDATE] owobot sleep ({owobot_sleep[0]} -> {mesaj[1]} | {owobot_sleep[1]} -> {mesaj[2]})")
            owobot_sleep = [ mesaj[1], mesaj[2] ]
          
          if mesaj[0] == "delay":
            mesaj=mesaj.split()
            if len(mesaj) != 3:
              return
            print(f"{at()}{bot.color.okcyan} [UPDATE] owobot delay ({owobot_delay[0]} -> {mesaj[1]} | {owobot_delay[1]} -> {mesaj[2]})")
            owobot_delay = [ int(mesaj[1]), int(mesaj[2]) ]

    elif message.author.id == bot.owoid:
      #if message author is owobot
      print(f"{at()}{bot.color.okblue} [owobot yanıtı] {bot.color.reset}")
      if "(3/5)" in message.content:
          exit()
      if client.user.name in message.content:
      #if owo bot speaks about us
        if 'banned' in message.content:
          exit()
          owobot_fuse=False
          print(f'{at()}{bot.color.fail} !!! [BANLANDI] !!! {bot.color.reset} {str(client.user)} owobotdan banlandı, eğer botun bir sorunu olduğunu düşüyorsanız https://github.com/sudo-do/auto-owo-bot adresinden sorun raporu açın')
        elif 'complete your captcha' in message.content:
          owobot_fuse=False
          print(f'{at()}{bot.color.warning} !! [CAPTCHA] !! {bot.color.reset} CAPTCHA DOĞRULAMASI GEREKLİ {message.content[-6:]}')
          exit()
client.loop.create_task(owobot())
client.loop.create_task(owobot2())
client.loop.create_task(owodead())
client.loop.create_task(owogems())
client.loop.create_task(waitor())
client.run(bot.token, bot=False)
