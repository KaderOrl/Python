# def  changeName(n):
#     n="Kader"
# name ="mustafa"
# changeName(name)
# print(name)


# def change(n):
#     n[0]="istunbul"
# sehirler=["ankara","izmir"]

# # n =sehirler[:] #kopyalama

# change(sehirler[:])

# print(sehirler)

# def add(a,b,c=0):#c belirtilmediği zamna iki deger calısır
#     return sum((a,b,c))
# print(add(10,20,30))

"""5 ten fazla parametre göndermek"""
# def add(*param):
#     print(param)
#     return sum(param)
# print(add(10,20))
# print(add(10,20,30,50,60,40))
# def displayUser(**args):#dictionary iiçn iki tane yildiz
#     for key ,value in args.items():
#         print("{}is {} ".format(key,value))

# displayUser(name="kader",age=2, city ="istanbul")
# displayUser(name="ali",age=12, city ="kars")
# displayUser(name="mehmet",age=2, city ="istanbul")


def myfunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myfunc(10,20,30,40,50,key1="kader",key="ka")
   
    