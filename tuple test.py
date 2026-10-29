#Create a tuple containing five integers and print it.
tuple=(10,20,30,40,50)
print(tuple)

#Create a tuple containing a string, integer, float, and Boolean value.
t = ("Python", 42, 3.14, True)
print(t)

#Create a single-element tuple and verify its datatype.
tuple=(40)
print(type(tuple))
print(tuple)

#Print the first, middle, and last elements of a tuple.
numbers=(10,20,30,40,50)
first,*middle,last=numbers
print(first)
print(middle)
print(last)

#Reverse a tuple using slicing.
tuple=(1,2,3,4,5)
print(tuple[::-1])

#Print every second element using slicing.
tuple=(10,20,3,4,5,6,9,1,0)
print(tuple[::-2])

#Count how many times 25 occurs in a tuple.
tuple=(10,20,30,40,50,60,10)
tuple1=tuple.count(10)
print(tuple1)

#Find the index of a given element.
tuple=(1,2,3,6,8,5,9,6)
tuple1=tuple.index(2)
print(tuple1)

#Calculate the sum and average of numeric tuple elements.
tuple = (10,20,30,40, 50)
total = sum(tuple)
average = total / len(tuple)
print("Sum:", total)
print("Average:", average)

#Count even and odd numbers in a tuple.
tup=(1,2,3,4,5,6,7,8,9,10)
for i in tup:
    if(i%2==0):
        print(i)

#Find the maximum and minimum values.
tuple=(1,2,3,4,5,6,7,8)
tuple=max(tuple)
print(tuple)

 #Check whether a particular value exists in a tuple.
tup=(43,76,23,87,34,12)
value=76
if  value in tup:
    print("value is  find")

tuple=(1,2,3,4,5,6,7,8)
tuple=min(tuple)
print(tuple)


#Convert a list into a tuple.
'''t = (10, 20, 30)
temp = list(t)
temp[0] = 100
temp.append(40)
t =tuple(temp)
print(t)'''

#Unpack a tuple into four variables.
students=("ram", 20,"pune", 1)
name,age,city,id=students
print(name)
print(age)
print(city)
print(id)

#Swap two variables using tuple unpacking.
a=10
b=10
a,b=b,a
print(a)
print(b)

#Access a specific value from a nested tuple.
students=(("ram",80),("sham", 90),("raj",70))
for name,marks in students:
    print(name,marks)

#Sort a tuple in ascending order and convert the result back into a tuple.
tup=(23,4,23,65,54,87)
lis2=list(tup)
lis1=lis2.sort()
print(lis1)

#Create a tuple of student names and marks, then print each student's details.
tup=(("name",89),("ram",67),("syam",56))
print(tup[0])
print(tup[1])
print(tup[2])