import os
import discord
from discord.ext import tasks
from Keepalive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("VineMeat"):
        await message.channel.send(file=discord.File('Images/VineMeat.jpg'))
        await message.channel.send(file=discord.File('mp3s/VineMeat.mp3'))

    if message.content.startswith("HappMeat"):
        await message.channel.send(file=discord.File('Images/Meatav.gif'))
        await message.channel.send(file=discord.File('mp3s/HappMeat.mp3'))

    if message.content.startswith("Meat"):
        await message.channel.send(file=discord.File("Images/Meat.webp"))
        await message.channel.send(file=discord.File("mp3s/meat4.mp3"))

    if message.content.startswith("meatFren"):
        await message.channel.send(file=discord.File("Images/FrenMeat.png"))
        await message.channel.send(file=discord.File("mp3s/MeatSweats.mp3"))

    if message.content.startswith("meatPat"):
        await message.channel.send(file=discord.File("Images/MeatPat.gif"))
        await message.channel.send(file=discord.File("mp3s/meat5.mp3"))

    if message.content.startswith("lungimeat"):
        await message.channel.send(file=discord.File("Images/LungiMeat.jpg"))

    if message.content.startswith("!d bump"):
        await message.channel.send(file=discord.File("Images/Bump.png"))

keep_alive()
client.run(os.environ['TOKEN'])
