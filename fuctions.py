# def SayHello(name="user"):
#     print(" hello "+ name)
# SayHello("kader")
# SayHello()

# def Say(name="user"):
#     return "hello "+ name 

# msg= Say("Kader")
# msg=Say("EOS")
# print(msg)

# def total(num1,num2):
#     return num1+ num2
# result=total(10,30)
# print(result)

def yasHesapla(dogumTarihi):
    return 2021-dogumTarihi
# yas=yasHesapla(2001)
# print(yas)

def emeklilikTarihi(dogumTarihi,isim):
    '''
     DOCSTRING:Dogum yiliniza göre ememkliliginize kac yil kaldi
     INPUT:Dogum yili
     OUTPUT:Hesaplanan yil bilgisi
    '''
    yas=yasHesapla(dogumTarihi)
    emeklilik=65-int(yas)

    if emeklilik>0:
        print(f"emekliliğinize {emeklilik} yıl kaldi")
    else:
        print("zaten emekli oldunuz")
emeklilikTarihi(1983,"ali")
print(help(emeklilikTarihi))
list=[1,2,3]
print(help(list.append()))