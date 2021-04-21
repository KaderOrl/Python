#value types=>string,number
          
#   deger tuttugu için atamadan sonra yapılan degişiklik
#    sadece yapılanı degiştirir.adresler aynı degil.
             
x=10
y=25 
x=y
y=30
#print(x,y)
#referance =>list,class
#Since the addresses are the same, they both change after assignment
a=["apple","banana"]
b=["apple","banana"]
a=b
b[0]="grades"
print(a,b)