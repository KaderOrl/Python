tuple =(1,"iki",3)
list=[1,2,"kader"]

print(type(tuple))
print(type(list))
print(len(tuple))

list=["ali","veli"] #güncelleme
# tuple=["sena","polo"]
list[0]="ahmet" #degitirebiliyoruz
#tuple[0]=2 #degiştirilemez
print(tuple.count(1))

names=("nobody","who") +tuple #toplma işlemi yapılabiliyor
print(list)
print(names)