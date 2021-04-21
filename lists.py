#my_list=[1,2,3]
# my_list=[1,"kader",True,23.1]
# print(my_list)
#toplama işlemi
my_list=["one","true","three"]
your_list=["four","five","six"]
list=my_list+your_list
print(list)
print(len(list))#eleman sayısı

message="hi.i am ka"
print(message[0]) #h gelir 
#ama eger...
message="hi there.i am ka".split()
print(message[0]) #hi gelir 
#tek bir liste altında toplama
user_K=["kader","oral"]
user_Y=["nobody","know"]
user=user_K +user_Y
print(user)
#iki listeyi tek liste altında toplama
user=[user_K,user_Y]
print(user)
print(user[1])