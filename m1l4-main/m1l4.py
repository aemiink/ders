# İlk Olarak discord kütüphanesini komutumun içine aktarmalıyım.
import discord
# Discord botunu "bot" sınıfı ile oluşturmak isterseniz farklı bir kütüphanenin içindeki fonksiyonu içeri aktarmalısınız.
from discord.ext import commands
# Kendi yazdığımız fonksiyonları içeri aktarmak istiyorsak;
from fonksiyonlar import *
# Dosyalara erişim için kütüphanemi eklemem gerekir.
import os
# Rastgele seçim yapmamızı sağlaya kütüphane
import random


#Ayrıcalık mantığı client sınıfı ile aynı mantıktadır.
intents = discord.Intents.default()
intents.message_content = True

#Bot Sınıfı kullanılarak bot oluşturulması
# commands.Bot() fonksiyonu bir botun özelliklerini belirtmenize yardımcı olur.
# command_prefix='!' --> botun komutları hangi sembolle başlayacak bunu belirtir.
# intents=intents --> botun ayrıcalıkları developer portaldaki gibi olmasını sağlar.
bot = commands.Bot(command_prefix='/', intents=intents)


# @bot.event dekaratörü bot hazır olduğunda konsolda bir mesaj yayınlamaızı sağlayacaktır.
@bot.event
async def on_ready():
    print(f'{bot.user} olarak discorda giriş yaptık!')
    
# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def merhaba(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! Nasılsın?")

# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def iyiyim(ctx):
    await ctx.send(f"{ctx.author.mention}! İyi olduğuna sevindim! Senin için ne yapmamı istersin?")

# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def kotuyum(ctx):
    await ctx.send(f"{ctx.author.mention}! Kötü olduğuna üzüldüm :( ! Senin için ne yapmamı istersin?")

# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def ders(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! 'Yarın ki Ders Programın: '")
    
# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def sifre(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! 20 Haneli Oluşturulan Şifren:{sifre_olusturucu(20)}") 

# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def yazimiturami(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! Parayı attım Tuttum. Çıkan Sonuç:{yazi_tura()}")
    
# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def emoji(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! Moduna göre rastgele bir emoji belirledim. Çıkan Sonuç:{emoji_olusturucu()}")

@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def kurallar(ctx):
    with open("Komutlar.txt", "r", encoding="utf-8") as metindosyasi:
        metin = metindosyasi.read()
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! Botumuzun komutları şunlardır:{metin}")
    
    
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def kedi(ctx):
    # 'rb’ - okumak için metin olmayan bir dosya açar;
    # 'wb’ - yazmak için metin olmayan bir dosya açar.
    with open("images/kediler/cat.jpeg", 'rb') as resim:
        resimdosyasi = discord.File(resim)
    await ctx.send(f"Sevgili {ctx.author.mention}! Kedi Görseliniz:")
    await ctx.send(file=resimdosyasi)
    
@bot.command()
async def mem(ctx):
    resimler_listesi = os.listdir('images/mems') # resimler_listesi = ["mem1.png","mem2.png","mem3.png"]
    resim = random.choice(resimler_listesi)
    with open(f'images/mems/{resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(f"Sevgili {ctx.author.mention}! Senin için seçtiğim Meme Görselin:")
    await ctx.send(file=picture)

bot.run("MTIxMzE3MDQ5NzgxMDg2NjE5Ng.GtX8tc.e4IxutvSf7tdCGhQDXvJ11RhQ0K4sWJ3rtxRKw")
    
    




