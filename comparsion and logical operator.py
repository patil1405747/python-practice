#comparsion operator
#Take two numbers from the user and check whether they are equala.
num1=int(input("Enter the first number"))
num2=int(input("Enter the seond number"))

print(num1==num2)

#Take two numbers check comparsion result true.


a=int(input("enter your first number"))
b=int(input("enter your second number"))

print(a==b)

#Take a person age and check wheter the age is greater than 18.
age=24
if(age > 18):
  print("age is greater than 18")
else:
    print("age is less than 18")

      
#Take two numbers and check whether first number is greater than or equal than.
number=80
number=70
print(number>=number)

#Take two numbers and check whether they are different.
num_1=74
num_2=14
print(num_1!=num_2)
      
#Take a student marks and check wheter marks are greather than or equal to 40.
stu_marks=45
if(stu_marks > 40):
   print("students is pass")
else:
   print("students is fail")

#Take two numbers and display the result of all six comparsion operators.
print(a == b)
print(a != b)
print(a > b)
print(a <b )
print(a >= b)
print(a <= b)


#Logical operator  

a=10
b=20
print(a<b and b>30)
print(a>b or a<b)
print(not(a>b))

age=25
print(age>=18 and age<=60)

marks=35
print(marks>=40 or marks==35)


#Take age and salary from the user and check:age >=18 AND salary >=20000
age=int(input("enter your age;"))
salary=int(input("enter your salary:"))
print(age>=18 and salary>=20000)

#Take two numbers from the user and check whether:first number is greather than
first=int(input("enter the first number:"))
second=int(input("enter your second number:"))
print(first>10 and second>10)

print(not(True)and 31>=34 or not(32>21 and (True)and not (True) or 56!=0))
print(not(0==0) and 34>=34 or not (32>=21)and not (False)) and not(False or 0!=0)
print(("Ram"=="Ram") and (0>0) and 34!=34or not(32>=21 and not(True)) and not(True or 56!=0))