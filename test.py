
#Check Whether a Number Is Even or Odd
num=10
if num%2==0:
  print("even number")
else: 
  print("odd number")

#Check if the Number Is Positive, Negative, or Zero
  num=-5
if num > 0:
  print("positive")
elif num < 0:
  print("negative")
else:
  print("zero")

#reverse the num using for and while both a=12345
a=12345
rev=0
while num> 0:
  digit = num%10
  rev = rev * 10+digit
  num=num // 10
  print(rev)

#check the num is polindrome or not
  num=121
  temp=num
  rev=0
  while num>0:
    digit=num % 10
    rev = rev * 10+digit
    num=num//10
    if temp == rev:
      print("palindrome")
else:
      print("not polondrome")

#check the num is prime or not
num=7
count =0
for i in range(1,num,1):
 if num % i==0:
    count+=1
    if count == 2:
      print("prime number")
    else:
      print("not prime")

 #find factorial     

for num in range(2,101):
  count=0
  for i in range(1,num+1):
   if num % 1==0:
    count +=1
   if count==2:
    print(num)  

#print square and cub of particular number
num=5
fact=1
for i in range(1,num+1):
  fact=fact*i
print(fact)

#list
#print even and odd from list
print
num=5
print("square:",num**2)
print("cube:",num**3)

#count even and odd from list
my_list=[10,15,20,25,30,35]
for i in my_list:
  if i % 2==0:
    print(i,"even")
  else:
    print(i,"odd")

'''my_list=[10,15,20,25,30]
even=0
count=0
for i in my_list:
    if i%2==0:
      even +=1
    else:
        odd+=1
print("even count:",)
print("odd count:", odd)'''

#reverse the ist without using predefind function
my_list=[10,20,30,40]
rev=[]
for i in my_list:
    rev=[i]+rev
print(rev)

#print prime bum from list
my_list=[2,3,4,5,6,7,9]
for num in my_list:
  count=0
  for i in range(1,num +1):
    if num % i==0:
      count+=1
      if count==2:
        print(num)

#print only string from list
my_list=[10,"apple",20,"banana",30]
for i in my_list:
  if isinstance(i,str):
    print(i)
my_list = [10, "Apple", 20, "Banana", 30]

#print int value from list
for i in my_list:
    if isinstance(i, int):
        print(i)   

#tuple
#find max
my_tuple = (10, 20, 30, 40, 50)
maximum = my_tuple[0]
for i in my_tuple:
    if i > maximum:
        maximum = i
print(maximum)      

# find min
my_tuple = (10, 20, 30, 40)
minimum = my_tuple[0]
for i in my_tuple:
    if i < minimum:
        minimum = i
print(minimum ) 

#find sum
my_tuple=(10,20,30,40,50)
total=0
for i in my_tuple:
  total=total+i
  print(total)
  
#find the lengtg of tiple without using len()
my_tuple=(10,20,30,40,50)
count=0
for i in my_tuple: 
  count+=1
print(count) 

#find the sum of tuple element
my_tuple=(5,10,15,20)
total=0
for i in my_tuple:
  total=total+i
  print(total)

 #display only even numbers from tuple
my_tuple=(10,15,20,25,30,35) 
for i in my_tuple:
    if i%2==0:
        print(i)

#dict
# display all keys and values of a dictionary
students = {"Rahul": 85, "Sneha": 90,"Arun": 75, "Priya": 95}
for name, marks in students.items():
    print(name, marks)


#find the total marks of all students
students={"rahul": 85,"sneha":90,"arun":75,"priya":95}
total=sum(students.values())
print("total marks:",marks) 

#highest marks
students={"rahul":85,"priya":75,"amit":45}
highest=0
for marks in students.values():
  if marks > highest:
     highest=marks
print("highest marks:",highest)

#who score above 60
students={"rahul":85,"priya":75,"amit":45}
for name,marks in students.items():
 if marks > 60:
    print(name,marks)

#  Count the Number of Students Who Passed
# students={"rahul":85,"sneha":90,"arun":75,"priya":95}
count=0
for name, marks in students.items():
    if marks >=35:
        count +=1
print("passed students:",count)    










     




