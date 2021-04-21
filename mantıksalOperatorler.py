#x=6
# result=5<x<10
# #and
# result=x>5 and x<10
#or 
# result= x<5 or x%5==1
# #not
# result=not(x>0) #cevabı degiştirir
# print(result)
#ÖRNEKLER 
#girilen bir sayınn 0-100 arasında olup olmadıgını kontrol ediniz
# x=int(input("bir sayi giriniz:"))
# result=x>0 and x<100
# print(result)
# #girilen sayının pozitif bir çift sayi olup olmadıgını kontrol ediniz
# x=int(input("bir sayi giriniz:"))
# result=x>0 and x%2==0
# print(result)
#girilen 3 sayıyı büyüklük olrak karsılastırınız 
# x=int(input("bir sayi giriniz:"))
# y=int(input("bir sayi giriniz:"))
# z=int(input("bir sayi giriniz:"))
# result=( x>y and x>z) 
# print(f"x en büyük sayıdır:{result}")

# result=(y>x and y>z) 
# print(f"y en büyük sayıdır:{result}")

# result=( z>x and z>y) 
# print(f"z en büyük sayıdır:{result}")

# #kullanıcıdan 2 vize (%30)ve final notunu alıp ortalamayı hesaplayınız 
# #eger ortalama 50 üstüyse gecti altıysa kaldı yazsın
# #a-ortalama 50 olsa bile final en az 50 olmalıdır
# #b-finalden 70 aldıgında ortalmanın onemi olmasın 
# vize1 = float(input('vize 1: '))
# vize2 = float(input('vize 2: '))
# final = float(input('final : '))

# ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)

# #a result = (ortalama>=50) and (final>=50)

# #b result = (ortalama >=50) or (final>=70)

# print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: {result}')

#kulllanıcının ad,kilo ve boy bilgilerini alıp kilo indeksini hesaplayınız
#formul=kilo/ boy uzunlugunun karesi
#asagıdaki tabloya göre kişi hangi gruba girmektedir
#0-18.4  =>zayıf
#18.5--24.9 =>normal
#25-29.9 =>fazla kilolu
#30-34.9    =>şişman

ad =input("adınız:")
kilo=float(input("kilonuz:"))
boy=float(input("boyunuz"))
index=kilo/boy**2

print(f"zayıf:{index<18.4} \n normal:{index>18.4 and index<24.9} \n fazla kilolu:{index>24.9 and index<29.9}\n şişman: {index>30} " )
