#1-gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonk yaz

# def yazdır(word,adet):
   
#     print(word *adet)
# yazdır("kader \n",10)

#2-kendine gönderilen sınırsız sayıdaki pArametreyi bir listeye cevireen func yazınız.

# def listeyeCevir(*param):
#     list= []

#     for par in param:
#         list.append(par)

#     return list
# result=listeyeCevir(10,20,30,"kader")   
# print(result)
#3-girilen 2 sayi arasındaki tüm asal sayıları bulun

# sayi1=int(input("sayi1:"))
# sayi2=int(input("sayi2:"))
# def asalSayiBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):#+1 cünkü range sayi2-1 e kadar getirir
#         if sayi>1 :
#             for i in range(2,sayi):
#                 if sayi%i==0:
#                     break
#             else:
#                 print(sayi)

# asalSayiBul(sayi1,sayi2)


# sayi1 = int(input("Sayı 1: "))
# sayi2 = int(input("Sayı 2: "))
 
# print(sayi1,"ile",sayi2,"arasındaki asal sayılar:")
 
# for sayi in range(sayi1,sayi2 + 1):
#    if sayi > 1:
#        for i in range(2,sayi):
#            if (sayi % i) == 0:
#                break
#        else:
#            print(sayi)

#4-kendisine gönderilen bir sayının tam bölenlerini bir liste seklinde gönderen func.
sayi=int(input("Sayi:"))    
def listeyeCevir(*tambölen):
    list= []   
    for tam in range(1,sayi+1):
         if sayi %tam==0:
           list.append(tam)
    return list
           
print(listeyeCevir(sayi))
