#1-"Bmw,Mercedes,Opel,Mazda" elemalerina sahip bir liste olustur
my_car=['Bmw','Mercedes','Opel','Mazda']
print(my_car)
#2-liste kaç elemanlıdır
print(len(my_car))
#3-listenin ilk ve son elemanı?
print(my_car[0])
print(my_car[3])
#4-Mazda degrni toyota ile degiştirin 
#my_car[3]='Toyota'
#print(my_car)
#5-mercedes listenin bir elmenı mıdır ?
result=  "Mercedes" in my_car
print(result)
#6-listenin -2 indeksindeki eleman nedir?
print(my_car[-2])

#7-listenin ilk üç elemanını alın
print(my_car[0:3]) 
#8-listenin son iki elemanı yerine "Totoya" ve" Renault" ekleyin
my_car[-2:]="TOtoya","Renault"
print(my_car)
#9- listenin üzerine "Audi"ve "Nissan"ı ekleyin
car =my_car +["Audi","Nissan"]
print(car)
#10- listenin son elemnını silin 
# del my_car[-1]
# print(my_car)
#11- liste elenlarını tersten yazdırın
print(my_car[::-1])
#12- aşagıdaki verileri bir liste içnde saklayınız 
# studentA: Yiğit Bilgi 2010, (70,60,70)
# studentB: Sena Turan 1999, (80,80,70)
# studentC: Ahmet Turan 1998, (80,70,90)
studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]
result =f"{studentA[0]},{studentB[1]},{studentC[1]},{2021-studentA[2]},{(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(result)