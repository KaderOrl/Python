# a,b,c,d =5,5,10,9
# result= a==b #true
# result= a==c #false
# result = a!=b #false
# password="123"
# username="kader"
# result =("kdr"== username)#false

# print(result)
#1-girilen 2 sayıdan hangisi büyüktür 
# x=int(input("bir sayi giriniz:"))
# y=int(input("bir sayi giriniz:"))
# result= x>y
# print(x>y)
# print(f"{x} büyüktür {y}den:{result}")
#kullanıcıdan girilen 2 vize(%40)ve final(%60) alıp ortalama notunu hesaplayınız 
# a=int(input("1.vize notu:"))
# b=int(input("2.vize notu:"))
# c=int(input("final notu:"))
# result=((a+b)*0.2)+c*0.6

# print(f"oratlamanız:{result}  {result>50}:gectiniz " ) 

#girilen sayının tek mi çift mi oldugunu bul 
# k=int(input("bir sayı girniz:"))
# result=k%2
# print(result==0)
#girilen sayının negatif pozitif durumunu yazdrın 

# a=int(input("bir sayı girniz:"))
# print(a>0)
#e mail ve sifre kontrol
email="kaderoral"
password="12345"
girilenEmail=(input("e mail giriniz:"))
girilenPassword=(input("bir sayı girniz:"))
isMail= email==girilenEmail.lower().strip()#kücük büyük har duyarlılgını ve bosluk kaldırma
isPassword=password==girilenPassword.lower().strip()
print(f"email bilgisi dogru mu:{isMail} password dogrumu:{isPassword}")

#kulllanıcının ad,kilo ve boy bilgilerini alıp kilo indeksini hesaplayınız
#formul=kilo/ boy uzunlugunun karesi
#asagıdaki tabloya göre kişi hangi gruba gitmektedir
#0-18.4  =>zayıf
#18.5--24.9 =>normal
#25-29.9 =>fazla kilolu
#30-34.9    =>şişman