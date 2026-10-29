#list
# list=[20,40,50,30]
print(list)


#types of ways to iterating a list
list=[23,45,60,70,20,80,20,10]
for i in list:
    print(i)

for i in range(len(list)):
    print(list[i])

#while loop 
while i<len(list):
   print(list[i])
   i+=1  

 # method of list      
#append.list
numbers=[10,20,30,40,50]
numbers.append(60)
print(numbers)

#extend.list
numbers=[10,20,30]
numbers.extend([3,5])
print(numbers)

#insert.list
numbers=[10,20,30]
numbers.insert(1,15)
print(numbers)

#remove.list
numbers=[10,3,5,8,9,6]
numbers.remove(3)
print(numbers)


#pop().list
numbers=[10,20,30,40,50]
numbers.pop()
print(numbers)


#sort().list
numbers=[3,4,7,8,2,9,]
numbers.sort()
print(numbers)


#reverse().list
numbers=[9,8,5,6,7,3,5,]
numbers.reverse()
print(numbers)


#count().list
numbers=[3,45,8,45,34]
numbers.count(2)
print(numbers)

#index().list
numbers=[3,7,9,6,]
numbers.index(3)
print(numbers)

#clear.list
numbers=[30,40,20]
numbers.clear()
print(numbers)


