""" ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }
 """
ogrenciler={}
number=input("ogrenci no:")
name =input("ogrenci adi:")
soyad =input("ogrenci soyadi:")
phone =input("ogrenci phone:")

# ogrenciler[number]={
#    "ad":name,
#    "soyadı":soyad,
#    "phone":phone
# }
ogrenciler.update({
    number:{
        "ad":name,
        "soyad":soyad,
        "phone":phone
    }
})

number=input("ogrenci no:")
name =input("ogrenci adi:")
soyad =input("ogrenci soyadi:")
phone =input("ogrenci phone:")

ogrenciler.update({
    number:{
        "ad":name,
        "soyad":soyad,
        "phone":phone
    }
})


number=input("ogrenci no:")
name =input("ogrenci adi:")
soyad =input("ogrenci soyadi:")
phone =input("ogrenci phone:")

ogrenciler.update({
    number:{
        "ad":name,
        "soyad":soyad,
        "phone":phone
    }
})
print("*"*50)

input("ogrenci no:")
ogrenci=ogrenciler[number]
print(f"aradıgınız {number} numarali ögrencinin \n adi:{name} \n soyadi:{soyad} \ntelefon no:{phone}")