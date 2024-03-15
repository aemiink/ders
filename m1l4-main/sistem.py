# Bilgisayardaki dosyalara erişim sağlamak için gerekli olan kütüphane
import os
# dosayalra erişim sağlamak için "os" komutunu kullanıyorum.
# listdir metodu/donksiyonu bir klasörün içerisindeki tüm dosyaları bir listeye koyar. 
resimlerl = ["cat.jpeg", "mem1.png"]
print(resimlerl)
resimler = os.listdir('images')
print(resimler)

