numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']
val = min(numbers)
val=max(numbers)
val=min(letters)
val=max(letters)

val =numbers[3:6]
print(val)

numbers[4]=40 #index 4 ekleme yapar
numbers.append(110) #sona ekleme yapar
numbers.insert(3,50) #istediğimiz konuma eklme yapma
numbers.pop(0) # indexteki elemani siler 
numbers.remove(16)

numbers.sort() #büyükten küçüğe yAda alfebetik olarak sıralar
letters.sort()
numbers.reverse()#ters yazzdırır
letters.reverse()
print(letters)

print(len(numbers))#eleman sayisi
print(len(letters))
print(numbers.count(10)) #kac tane 10 old bulmak için 
print(letters.count("a"))
numbers.clear() #bütün listeyi siler
print(numbers)