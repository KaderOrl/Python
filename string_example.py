website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#course karekter sayisi
lenght=len(course)
print(lenght)
#www karakterlerini alma
result=website[7:10]
print(result)
#com ifadesini alalım
lengt =len(website)
print(website[lengt-3:lengt])
#course içindeki ilk 15 ve son 15 karekterler
print(course[:15])
print(course[-15:])
#course ifadesindki karekterleri tesrten yazdırma
print(course[::-1])
#bisiler bisiler :)
name,lastname,age,job="kader","oral",20,"student"
print(f"my name is {name} {lastname},i am {age} years old and my job is {job}")
#"hello word "ifadesinideki w yi W iile değiştirelim
s= "Hello word"
s=s[0:6]+"W"+ s[-3:]
print(s)
#"abc"ifadesini yan yana 3 defa yazdırın 
y="abc"*3
print((y[::]))