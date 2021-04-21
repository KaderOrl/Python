""" sehirler=["kocaeli","istanbul"]
plakalar=["41","34"]
# print(plakalar[(sehirler.index("kocaeli"))])
# print(plakalar[(sehirler.index("istanbul"))])

city={"mardin" :47,"amed":21}
print(city["mardin"])
print(city["amed"])
city ["ankara"]=6
city["mardin"]="54564" #güncelleyebiliyoruz
print(city) """
users={
        "kaderOral":{
            "age":21,
            "address":"mardin",
            "telno" :65135646,
            "roles":["admin","users"]
        },
        "leyladogan":{
            "age":31,
            "address":"amed",
            "telno" :516355646,
            "roles" :["user"]
        }
}
print(users["kaderOral"]["age"])#yas bilgisine ulasma 
print(users["leyladogan"]["roles"][0])
print(users)