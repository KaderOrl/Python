# x,y,z=5,10,20

# # x,y=y,x
# x=x+5 # x+=5 same 
# #x*=5,x/=5,x%=5,x//=5 tam bölme

# values =1,5,6#atama yapılabilir
# x,y,z=values
# print(values)
# print(type(values))
# print(x,y,z)
#exsamples
x,y,z=2,5,10
number=1,5,7,10,6
#1-
""" a=input("bir sayi giriniz:")
b=input("bir sayi giriniz:")
result=(x+y+z)-int(a)*int(b)
print(result) """
#2-
print(y//x)
#3-
print((x+y+z)%3)
#4-
print(y**x)
#5-
x,*y,z=number #x bastakini ve z de sondakine esit kalanlar da y nin olur 
print(x,y,z)
#6-
x,*y,z=number 
result=y[0]+y[1]+y[2]
print(result)

