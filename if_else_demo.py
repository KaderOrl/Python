#kullanıcıdan isim yas egitim bilgileri isteyip ehiliyet alabilme durumunu kontrol ediniz.
#yas en az 18 ve egitim durumu :lise vaya üniversite 
# ad=input("adınızı giriniz:")
# egitim=input("eğitim giriniz:")
# yas=int(input("yaşınızı giriniz:"))
# if (yas>18):
#     if (egitim=="lise" or egitim=="üni") :
#         print("ehliyyet alabilirsiniz")
#     else:
#         print("egitim durumunuz boktan ehliyet alamazsınız")
# else:
#     print("ehliyet alamazsınız")
#trafiğe cıkıs tarihi alınan bir aracın zmanı asagıdaki 
#bilgilere göre hesaplayınız
#1. bakım =>1.yıl
#2.bakım=>2.yil
#3.bakım =>3.yıl
#süre hesabına alınan gün,ay,yıl, bilgisine göre gün bazlı hesaplayınız
#datatime modülünü kul.gerekiyor 
#(simdi)-(2018/8/1)
""" import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
     print('1.servis aralığı')
elif days>365 and days<=365*2:
     print('2.servis aralığı')
elif days>365*2 and days<=365*3:
    print('3.servis aralığı')
else:
    print('hatalı süre.') """

# if days <=365:
#     print("1.servis aralığı")
# elif days>365 and days<=365*2:
#     print("2.servis aralıgı ")
# elif days>365*2 and days<=365*3 :
#     print("3.servis aralıgı")
# else:
#     print("hatalı süre")

# email="kaderko"
# password="12345"
# girMail= input("email:")
# girPass=input("password:")
# if(email==girMail)and (password==girPass):
#     print(f"uygulamaya giriş basarılı")
# else:
#     print("giriş basarısız")

