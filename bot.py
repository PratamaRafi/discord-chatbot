import discord
from discord.ext import commands
import random
import os
import requests

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True

# Membuat bot di variabel bot dan mentransfernya hak istimewa
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Halo nama saya adalah bot {bot.user}!")

# @bot.command()
# async def jumlah(ctx,left=0, right=0):
#     await ctx.send(f"hasil penjumlahan nya adalah: {int(left)+int(right)}")

@bot.command()
async def hehe(ctx, count=5):
    await ctx.send("he" * count)

# command kirim meme
@bot.command()
async def meme(ctx):
    list_meme = os.listdir('meme') #['meme2.jpeg', 'meme3.jpeg', 'meme1.jpeg']
    sent_meme = random.choice(list_meme)
    with open(f'meme/{sent_meme}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    list_animlas = os.listdir('animals')
    sent_animal = random.choice(list_animlas)
    with open(f'animals/{sent_animal}','rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def bye(ctx):
    await ctx.send(f"bot {bot.user} mengucapkan selamat tinggal!")

bot.run("TOKEN")