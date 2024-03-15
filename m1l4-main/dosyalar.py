#metin dosyaları

# Metin dosyasını tutacak olan bir değişken oluşturmamız gerekir.
# open()--> fonksiyonu pythonla yerleşik olarak ve bizim bilgisayarımızda depoladığımız belgelere erişim sağlar.
# İlk olarak fonksiyon içeriği metin/görsel(herhangi bir dosyanın) bulunudğu dosya yolunu yazmanızı ister.
# Bu dosyayı hangi modda açılacağını belritmemizi ister:
# 'w’ --> bir metin dosyayısını yazma modunda açar fakat içindeki her şeyi siler;
# ‘r’ --> bir metin dosyayısını salt okunur modda açar;
# ‘a’ --> metin dosyasından hiçbir şey çıkarmadan dosyanın sonuna veri kaydeder;
# encoding metin belgelerinin hangi dil türünde açılacağını söylememizi ister.Türkçe dil ailesi UTF-8 Adını dil ailesinde bulunur.
metindosyasi = open("metin.txt", "r", encoding="utf-8")
# Bu değişken metin dosyasının içindeki metini kullanmak için oluşturulur.
metin = metindosyasi.read()
#konsolda çıktısını al.
print(metin)
# metin belgesiyle işim bittiğine göre bunu kapatmam lazım.
metindosyasi.close()


#bir metin dosyasının içeriğini değişterecek komutlar.
metindosyasi = open("metin.txt", "w", encoding="utf-8")
#text'i hangi metinle değiştireceğimi yazmam lazım.
yenimetin = "Arkadaşlar bakın belgenin içeriğini bu şekilde değiştirdim."
#metin dosyasını yukarıdaki metini yaz
metindosyasi.write(yenimetin)
# metin belgesiyle işim bittiğine göre bunu kapatmam lazım.
metindosyasi.close()


#bir metin dosyasının içeriğini değişterecek komutlar.
metindosyasi = open("metin.txt", "a", encoding="utf-8")
#text'i hangi metinle değiştireceğimi yazmam lazım.
yenimetin = "Gördünüz mü?"
#metin dosyasını yukarıdaki metini yaz
metindosyasi.write(yenimetin)
# metin belgesiyle işim bittiğine göre bunu kapatmam lazım.
metindosyasi.close()


with open("Komutlar.txt", "r", encoding="utf-8") as metindosyasi:
    print(metindosyasi.read())









