website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#1- ' Hello World 'bastaki ve sondaki boslugu sil
result =' Hello World '.strip()
result =' Hello World '.lstrip()
result =' Hello World '.rstrip()

#2-"http://www.sadikturan.com" icindeki sadikturan disinda her ifadeyi silin
result =website.strip("/:htpw.com")
#3-'cource'karekter dizisinin tamamını kücük harfle yazın
result=course.lower()

#4-"website"içinde kaç "a"karekteri vardır 
result=website.count('a')
result=website.count('www',1,10) #1 ile 10 ar5asında kac tane oldugunu bul.iç.
#5-"website" www ile baslayıp com ile bitiyor mu?
result=website.startswith('www')
respons=website.endswith('com')
# print(result)
# print(respons)
#6-websitesi içinde "www"var mı
result=website.find("www")
#7- cource içerisindeki harfler alfabetik mi
result =course.isalpha()
result="hello".isalpha()
result=course.isdigit()#içinde rakam olup olmadıgını kontrol etmek için 
print(result)
#8-"crazy in paradise is easy" ifadesini 50 karekter içine yerleştirip saga sola * ekle
result=" being crazy in paradise is easy".center(50,"*")
result=" being crazy in paradise is easy".rjust(50,"*")
result=" being crazy in paradise is easy".ljust(50,"*")
#9-"course"daki tum boslukları - ile degiştiniz
result=course.replace(" ","-")
result=course.replace(" ","-",5)#sınır belirtmek istersek
result=course.replace(" ","") #bosluk karekteri silinir
#10- "hello world" ifadesindeki world u there yapalım
result= "hello world".replace("world","there")

#11- "course" karekterlerini bosluktan sonra ayırın
result=course.split(" ")
result=result[2]
print(result)