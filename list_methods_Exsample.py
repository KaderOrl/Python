names=["Ali","yağmur","hakan","Deniz"]
years= [1998,2000,1998,1987]
# "cenk"ismini listenin sonuna ekleyin
names.append("Cenk")
#"sena"ismini listenin basına ekleyin
names.insert(0,"Sena")
#'deniz'ismini listeden siliniz
#names.remove("deniz")
# index=names.index("Deniz")
# print(index)
# names.pop(index)
# print(names)
#"deniz" isminin indexsi nedir 
# result="Deniz" in names
# print(result)
#"ali "listenin bir elemnı mıdır
respons="kader"in names
respons=names.index("Ali")
print(respons)
#liste elemanlarını ters cevirin
names.reverse()
#liste elemanlarını alfetik olrak sıralayınız 
names.sort()
#years listesini rakamsal büyüklüğe göre sıralayınız 
years.sort()
print(years)
print(names)
#str ="Chevrolet,Dacia" karekter dizisini listeye ceviriniz
str ="Chevrolet,Dacia".split(" ")
print(str)
#kulllanıcıdan alacagınız üç marka degerini bir listede toplayınız
markalar=[] 

marka=input("marka giriniz:")
markalar.append(marka)
marka=input("marka giriniz:")
markalar.append(marka)
marka=input("marka giriniz:")
markalar.append(marka)
print(markalar)
