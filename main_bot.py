import discord, random, os, requests
#requests gives u library to access links online
from discord.ext import commands
from bot_logic import pass_gen

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def passgen(ctx):
    await ctx.send('Heres ur password! ')
    await ctx.send(pass_gen(10))
    
@bot.command()
async def pangkatdua(ctx):
    await ctx.send('Masukin angka bebas, aku itungin pangkat duanya B)')
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    await ctx.send(f'angka kamu dipangkat dua adalah {(int(message.content))**2}' )
    
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('memes'))
    with open(f'memes/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#@bot.command()
#async def moods(ctx):
 #   img_name = random.choice(os.listdir('moodmemes'))
 #   with open(f'moodmemes/{img_name}', 'rb')as f:
  #      picture = discord.File(f)
#    await ctx.send(file=picture)
    
@bot.command()
async def moods(ctx):
    num = random.randint(1,3)
    if num <= 2:
        ar = os.listdir('moodmemes')
        ar.remove('dead.png')
        img_name = random.choice(ar)
    else:
        img_name = 'dead.png'
    with open(f'moodmemes/{img_name}', 'rb')as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

daur_ulang = [
    'botol plastik', 'sedotan plastik',  'piring sekali pakai',
    'kemasan makanan', 'karton telur', 'aluminium', 
    'pakaian', 'kertas', 'karton', 
    'kaleng', 'koran', 'majalah',
    'kertas kantor', 'botol minuman', 'kaca', 
    'ban bekas', 'selang karet', 'pallet kayu'
]

@bot.command()
async def cek_sampah(ctx):
    await ctx.send('Sampah apa yang ingin diperiksa?')
    message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message.content)

    #check
    if message.lower() in daur_ulang:
        await ctx.send('Jangan dibuang dulu, sampah itu bisa didaur ulang! Ini beberapa ide yang dapat digunakan!')
        await ctx.send('https://waste4change.com/blog/panduan-lengkap-benda-yang-bisa-didaur-ulang/')
        await ctx.send('https://blog.eigeradventure.com/kerajinan-daur-ulang/')
    else:
        await ctx.send('Sampah itu tidak bisa didaur ulang! Anda harus buang dengan bijak dan kurangi atau kelola penggunaanhnya. Berikut beberapa artikel yang dapat membantu! ')
        await ctx.send('https://dlh.semarangkota.go.id/solusi-asyik-kurangi-sampah-plastik/')
        await ctx.send('https://mutucertification.com/cara-mengatasi-limbah-anorganik/')

bot.run(FILL WITH UR TOKEN!!!)
