import random


def yazi_tura():
    para =random.randint(0,2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
    
def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre


def emoji_olusturucu():
     emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
     secilen_emoji = random.choice(emoji)
     return secilen_emoji
 


