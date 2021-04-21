# sayilar=   [1,3,5,7,9,12,19,21]
#sayilar listesini while ile ekrana yazdırın 
# i=0
# while(i<len(sayilar)):
    
#     print(sayilar[i])
#     i+= 1
#baslangiç ve bitiş degerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
# baslangic=int(input("baslangıc:"))
# bitis=int(input("bitis:"))
# i =baslangic
# while i<bitis:
#     i+=1
#     if(i%2==1):
#      print(i)
#3- 1-100 arasıdaki sayıları azlan sekilde yazdırın
# i=100
# while i>0:
#     print(i)
#     i-=1

#4- kullanıcıdan aldıgınız bes sayıyı ekranda sıralı sekilde yazdırın
# numbers =[]
# i=0
# while i<5:
#    sayi =int(input("bir sayi giriniz:"))
#    numbers.append(sayi)
#    i+=1
# numbers.sort()
# print(numbers)

#5-kullanıcıdan alacagınız sınırsız ürünü listeleyin 
urunler =[]
adet =int(input("kac urun eklemek istiyorsunuz:"))
i=0
while (i<adet):
    name =input("ürün ismi:")
    price =input("ürün fiyati:")
    urunler.append({
        "name":name,
        "price":price
    })
    i+= 1

for urun in urunler :
 print(f"ürün adi:{urun['name']} urun fiyatı:{urun['price']}")