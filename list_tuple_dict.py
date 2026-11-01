#largest of there numbers
a=10
b=25
c=15
if a>b and a>c:
    print(a,"is largest")
elif b>a and b>c:
    print(b,"is largest")
else:
    print(c,"is largest")  


 #smallest of three numbers
a=10
b=25  
c=5
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:    
 print(c) 


#divisiblie by 5
num=25
if num % 5==0:
    print("divisible by 5")
else:
    print("not divisible by 5") 


#multiplication table
num=5
for i in range(1,11):
    print(num, "x",i, "=", num*i) 

#String Palindrome
# text = "madam"
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#sum of digits
num=1234
total=0
while num>0:
    digit=num%10
    total=total+digit
    num=num//10
print(total)   

#count number of digits
num=12345
count=0
while num>0:
    count=count+1
    num=num//10
print(count)

#fibonacci series
a=10
b=5
for i in range(7):
    print(a)
a,b=b,a+b

#Reverse a Number
num = 1234
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)

#list


#find the maximum number
a=[10,20,30,40,50]
print(max(a))

#print even numbers
'''for num in numbers:
    if num % 2 != 0:
        print(num)'''

#odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)

#reverse list
a=[10,20,30,40]
a.reverse()  
print(a) 

#remove duplicate element in a list
list=[10,20,30,40]
list=[]
for i in list:
    if i not in list:
        list.append(i)
print(list)

#Separate positive and negative numbers
list=[1,2,-3,4,-5,6,-7]
positive=[]
negative=[]
for i in list:
    if i >=0:
       positive.append(i)
    elif i <=1:
         negative.append(i)
print("Positive", positive)
print("Negative", negative) 


#Sort a list without using sort()
mylist = [40, 10, 30, 20, 50]

for i in range(len(mylist)):
    for j in range(i + 1, len(mylist)):
        if mylist[i] > mylist[j]:
            mylist[i], mylist[j] = mylist[j], mylist[i]
print(mylist)


#tuple
#Access elements using indexing
mytuple = ("Python", 100, 25.5, True)
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(mytuple[3])


#check even number
a = (10, 15, 20, 25, 30)
for i in a:
    if i % 2 == 0:
        print(i)

#Print only string values        
a = ("Apple", 10, "Mango", 20, "Orange")
for i in a:
    if type(i) == str:
        print(i)

#Find the length of a tuple without using len()
tuple=(20,40,60,80,40,10)
count=0
for i in tuple:
    count=count+1
print("Length of tuple:",count) 

#find the max
my_tuple=(10,54,23,25,43,42,40,60)
print(max(my_tuple))

#find the min
my_tuple=(23,65,23,87,56,9,6,24)
print(min(my_tuple))

#sum of  tuple
my_tuple=(10,54,23,25,43,42,40,60)
print(sum(my_tuple))

