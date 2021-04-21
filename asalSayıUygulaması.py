girSayi=int(input("bir sayi giriniz:"))
asalMı=True
if  girSayi==1:
    asalMı=False

for i in range(2,girSayi):
   if  girSayi%i==0:
        asalMı=False
        break
 
if asalMı:
    print("sayi asal")
else:
    print("asal degil")


