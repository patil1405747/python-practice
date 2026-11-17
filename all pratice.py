a = 100
print("Before:", type(a))
a = "Python"
print("After:", type(a))


employee_id = 101
name = "Rahul"
salary = 25000.50
department = "HR"
status = True

print("Employee ID:", employee_id)
print("Name:", name)
print("Salary:", salary)
print("Department:", department)
print("Employment Status:", status)


'''length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of Rectangle:", area)


a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)



a = 10
b = 20.5
c = "30"
print(type(a + b))
print(type(str(a)))
print(type(float(c)))



a = "250"
num = int(a)
print("Integer:", num)
print("Square:", num ** 2)



a = 45
print(float(a))
print(str(a))
print(bool(a))



a = 99.99
b = int(a)
print(b)



num = input("Enter a number: ")
num = int(num)
print("Number:", num)
print("Data Type:", type(num))



marks = "450"
total = int(marks)
percentage = (total / 500) * 100
print("Marks:", total)
print("Percentage:", percentage)'''



a = 100
b = 20.5
print(str(a) + str(b))
print(int(b))
print(float(a))
print(bool(0))
print(bool(""))

#string data type
name = input("Enter your full name: ")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())



text = input("Enter a string: ")
count = len(text)
print("Total characters:", count)




text = input("Enter a string: ")
reverse = text[::-1]
print("Reverse:", reverse)





text = input("Enter a string: ")
count = text.count("a")
print("Letter a appears:", count, "times")




text = input("Enter a sentence: ")
result = text.replace(" ", "-")
print(result)

text = input("Enter a string: ")
count = text.count("a")
print("Letter a appears:", count, "times")



sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
if word in sentence:
    print("Word exists")
else:
    print("Word does not exist")






email = input("Enter email: ")
parts = email.split("@")
username = parts[0]
domain = parts[1]
print("Username:", username)
print("Domain:", domain)




name = "Rahul"
age = 22
city = "Bangalore"
print(f"My name is {name}. I am {age} years old. I live in {city}.")




numbers = [10, 25, 60, 45, 80, 90, 30, 55, 70, 20, 65, 40, 100, 15, 85]
print("Numbers greater than 50:")
for i in numbers:
    if i > 50:
        print(i)



numbers = [10, 50, 30, 80, 60, 90]
largest = numbers[0]
second = numbers[0]
for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("Second Largest:", second)    




numbers = [10, 20, 30, 10, 40, 20, 50]
result = []
for i in numbers:
    if i not in result:
        result.append(i)
print("Original List:", numbers)
print("After Removing Duplicates:", result)




list1 = [10, 20, 30]
list2 = [40, 50, 60]
result = list1 + list2
print("First List:", list1)
print("Second List:", list2)
print("Combined List:", result)




list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
result = []
for i in list1:
    if i in list2:
        result.append(i)
print("Common Elements:", result)




