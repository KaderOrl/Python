name= 'kader'
lastname= 'oral'

age='20' #çünkü burda string toplama yapacağız
print('my name is:'+ name + lastname +' '+ ' \n i am '+ " "+age +' ' +'years old')
#yada
#print('my name is:'+ name + lastname +' ' + '\n i am '+ " "+str(age) +' ' +'years old')
greeting = ('my name is:'+ name + lastname +' ' + '\n i am '+ " "+str(age) +' ' +'years old')
lenght=len(greeting)
print(greeting[0]) #ilk karekteri yazdırır
print(greeting[1])
print(len(greeting))#karekter sayisini verir
print(greeting[lenght-1])#son karekteri verir
print(greeting[-1])#son karekteri verir
print(greeting[1:10])#1 den 10 kadar olanlari yazdirir
print(greeting[6:])#6.karekterden sona kadar dewamm eder 
print(greeting[:15])#bastan basla son karekter 5 olsun
print(greeting[1:40:2])#1 den başlar 40 ka kadar 2 ser atlayark gider