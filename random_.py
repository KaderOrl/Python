
import random # kütüphane ekleme
sayi = random.randint(1, 100)
print(sayi)
can=int(input("kac hak almak istersiniz:"))
sayac=0
hak=5
hak=can 
while hak>0:
    sayac +=1
    hak -=1
    girSayi =int(input("bir sayi giriniz:"))
   

    if girSayi>sayi :
        print("aşağı!")
    elif girSayi==sayi:
        print(f"tebrikler!{sayac}.defada bildiniz toplam puan:{100-(100/can)*(sayac-1)}")
        break
    else: 
        print("yukarı!")
    if hak==0:
        print(f"hakkınız bitti.tutulan sayı:{sayi}")
            


