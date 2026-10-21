'''number=30
if(number>10):
 print("number is greater than 10")
#writep m to check whether a person is eligible to vote (age must be 18 or above)
age=22
if(age>=18):
  print("A person is eligible to vote")
# . Write a program to check whether a number is divisible by 5.
number=10
if(number%5==0):
   print("number is divisible by 5")

#Write a program to check whether a student has scored at least 35 marks
marks=10
if("marks>=35"):
   print(f" The student scored {marks} and has passed (at least 35 marks)")

# Write a program to check whether a character is an uppercase letter. 35 marks 
name="gayatri"
if(name.isupper()):
   print("name is upper case")

# Write a program to check whether a number is even or odd
number=8
if(number%2==0):
  print(f"{number} is odd")
else:
  (f"{number} is odd")

# Write a program to check whether a number is positive or non-positive
num=-23 
if(num>0):
     print("number is positive")
else:
  print("number is negative")

# Write a program to check voting eligibility using if-else
age=int(input("enter your age:"))
if(age>=18 and age<100):
     print("your aligible for voting")
else: 
    print("your not eligible for voting")
#. Write a program to check whether a number is divisible by both 3 and 5
num=15
if(num%3==0 and num%5==0):
    print(f"{num} is divisible by 3 and 5")
else:
   print( "not divisible by 3 and 5")

# Write a program to check whether two numbers are equal or different
num1=23
num2=23
if(num1==num2):
   print (f"{num1} and {num2} are equal")
else:
   print(f"{num1} and {num2} are difference")

#Write a program to display Pass if marks are 35 or above; otherwise display Fail
# Simple Pass/Fail Program for Practice
marks = int(input("Enter your marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")
    print("Pass") 

# Write a program to check whether a year is a leap year
year=24
if(year % 4==0 and year % 100 !=0) or (year % 400==0):
   print(f"{year}is a leap year.")
else:
   print(f"{year} is not leap year.")

   # if-elif-else statements
# Write a program to identify whether a number is positive, negative, or zero
num=0
if(num==0):
   print("number is zero")
elif(num>0):
   print("number is positive ")
else:
   print("number is negative")

#Write a program to find the greatest of three numbers
num1=65
num2=34
num3=76
if num1 >=num2 and num1 >=num3:
   print(f"{num1} is the greatest number:")
elif num2 >= num1 and num2 >= num3:
   print(f"{num2} is the greatest number:")
else:
   print(f"{ num3} is the greatest number:")

#Write a program to display a grade using these ranges: A = 90–100, B = 75–89, C = 60–74, Pass = 35–59,
#ail = below 35. Also handle marks outside 0–100 as invalid
marks=78
if(marks>=90 and marks<=100):
   print("grade is A")
elif(marks>=75 and marks<=89):
   print("grade is B")
elif(marks>=60 and marks<=74):
    print("grade is c")
elif(marks>=35 and marks<=59):
     print("pass")
else:
    print("fail")


#  Write a program to classify a character as an uppercase letter, lowercase letter, digit, or special character
char="d"
if len(char)==1:
   if char.isupper():
      print(f"'{char}'is an uppercase letter.")
   elif char.islower():
      print(f"'{char}' is a lowercase letter.")
   elif char.isdigit():
      print(f"{char}' is a digit.")
   else:
      print(f"' {char}' is a special character.")
else:
      print("please enter exactly one character.")

# Write a program to display the weekday for a number from 1 to 7; display Invalid for any other number.
# Get input from the user
day_num = int(input("Enter a number from 1 to 7: "))

if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Invalid")

#. Write a program to display the number of days in a month, assuming February has 28 days

month = int(input("Enter month number (1-12): "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
elif month == 2:
    print("28 days")
else:
    print("Invalid month number")

#    Write a program to calculate a discount: 20% for a purchase of n5,000 or more, 10% for n2,000 or more,
#otherwise no discount  
 
# Get the purchase amount from the user
amount = float(input("Enter the purchase amount: "))

if amount >= 5000:
    discount = 0.20
    print("20% discount applied!")
elif amount >= 2000:
    discount = 0.10
    print("10% discount applied!")
else:
    discount = 0.0
    print("No discount applied.")

# Calculate final amount
discount_amount = amount * discount
final_amount = amount - discount_amount

print(f"Discount Amount: {discount_amount:.2f}")
print(f"Final Amount to Pay: {final_amount:.2f}")

#20.# Simple Triangle Classification Program for Practice
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# Nested if statement
#. Write a program to check a username first and then check the password only if the username is correct
 # Predefined correct username and password
username_correct = "admin"
password_correct = "1234"

username = input("Enter username: ")

if username == "correct_username":
    print("Username correct!")
    
    password = input("Enter password: ")
    
    if password == "correct_password":
        print("Login Successful!")
    else:
        print("Incorrect Password!")
else:
    print("Incorrect Username!")

#Write a program to check whether a person is at least 18 years old and then check whether they are
#registered to vote     
# Simple Voting Eligibility Check Program
age = int(input("Enter your age: "))

if age >= 18:
    registered = input("Are you registered to vote? (yes/no): ")
    
    if registered.lower() == "yes":
        print("Eligible to vote!")
    else:
        print("Not registered to vote.")
else:
    print("Not eligible to vote (Under 18).")

# Write a program to check whether a student has passed; if passed, check whether the student has scored at
#least 75 marks for distinction
# Pass and Distinction Check Program
marks = int(input("Enter student marks (0-100): "))

marks = int(input("Enter student marks (0-100): "))

if marks >= 35:
    print("Result: Pass")
    
    if marks >= 75:
        print("Status: Distinction! ")
    else:
        print("Status: Regular Pass")
else:
    print("Result: Fail")
  
# Write a program to check whether a number is positive; if positive, check whether it is even or odd
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("the number is not positive.")

#. logical operator
#Write a program to check whether a number is between 10 and 50 inclusive
number =45
if(number>10 and number<50):
    print(f"{number} is between 10 and 50")

 # 28=num=21
if(num%3==0  or num%7==0):
    print(f"{num} is divisible by 3 and 7")


#29
# age=35
# qualification="bca"
# if(age>=21 and age<=35 and qualifcation=="bca"):
    print("eligible for job")

#30
char="0"
if(char=="a" or char=="0" or char=="u" or char=="i" or char=="e"):
    print(f"{char} character is vowel")

 #31
num=203
if(num<100 or num>200):
    print(f"{num} is not between 100 and 200")   

 #32
thoery="pass"
practical="fail"
if(thoery=="pass" and practical=="pass"):
   print("pass")

#33
order_amt=600
premium="no"
if(order_amt>=500 or premium=="yes"):
   print("free delivery")  

#Advance conditional statement    

 #34
a=45
b=65
c=87
d=100
if(a>b and a>c and a>d):
   print(f"{a}is greatest number")
elif(b>a and b>c and b>d):
   print(f"{b} is greatest number")
elif(c>a and c>b and c>d):
   print(f"{c} is greatest number")
else:
   print(f"{d}is greatest number")

#35
service=9
if(service>=10 and service<=20):
   print("15% bonus")
elif(service>=5 and service<=10):
   print("10% bonus")  
elif(service<5):
   print("5% bonus")
else:
   print("enter under 20 year experience")'''
   