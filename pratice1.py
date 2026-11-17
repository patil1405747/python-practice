#Remove Duplicates: Write a Python program to remove duplicate elements from a list without using set()
numbers = [10, 20, 10, 30, 20, 40, 50, 30]
list = []
for i in numbers:
    if i not in list:
        list.append(i)
print("Original List:", numbers)
print("List after removing duplicates:", list)

 #Second Largest: Write a program to find the second-largest element from a list without using sort(),
#sorted() or max()

numbers = [10, 25, 45, 30, 60, 50]
largest = numbers[0]
second = numbers[0]
for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("Largest element:", largest)
print("Second largest element:", second)

#. Separate Even and Odd: Write a program to separate even and odd numbers from a list into two different
#lists.
numbers = [10, 15, 20, 25, 30, 35, 40, 45]
even = []
odd = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:", even)
print("Odd numbers:", odd)

#Element Frequency: Write a program to count how many times each element occurs in a list.
numbers = [10, 20, 10, 30, 20, 10, 40]
for i in numbers:
    count = 0
    for j in numbers:
        if i == j:
            count += 1
            
if numbers.index(i) == numbers.index(i):
        print(i, "occurs", count, "times")

#tuple
#Tuple Reversal: Write a program to reverse a tuple without using slicing
numbers = (10, 20, 30, 40, 50)
reverse = numbers[::-1]
print("Reversed Tuple:", reverse)

# Maximum and Minimum: Write a program to find the maximum and minimum elements from a tuple without
#using built-in functions.
numbers = (10, 50, 20, 80, 30, 5)

maximum = numbers[0]
minimum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

print("Maximum element:", maximum)
print("Minimum element:", minimum)

#Tuple Element Frequency: Write a program to count the occurrence of a particular element in a tuple without
#using the count() method
numbers = (10, 20, 10, 30, 10, 40, 20)
element = 10
count = 0
for i in numbers:
    if i == element:
        count += 1

print("Element:", element)
print("Occurrence:", count)

#Convert Tuple: Write a program to convert a tuple into a list, remove duplicate elements, and convert it back
#into a tuple
'''numbers = (10, 20, 10, 30, 20, 40, 50)
list = list(numbers)
list = []
for i in list:
    if i not in list:
        list.append(i)
new_tuple = tuple(list)

print("Original Tuple:", numbers)
print("List:", list)
print("After Removing Duplicates:", new_tuple)'''

#Nested Tuple: Consider the following tuple and write a program to find the student who scored the highest
#marks.
students = (("Amit", 85), ("Rahul", 92), ("Sneha", 78), ("Priya", 95))
highest = students[0]
for i in students:
    if i[1] > highest[1]:
        highest = i

print("Highest Scoring Student:", highest[0])
print("Highest Marks:", highest[1])

# Common Elements: Write a program to find common elements between two lists using sets
list1 = [10, 20, 30, 40, 50]
list2 = [20, 40, 60, 80, 100]
set1 = set(list1)
set2 = set(list2)
common = set1 & set2
print("Common Elements:", common)

#Unique Elements: Write a program to find all unique elements from two lists combined
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
unique = set(list1) | set(list2)
print("Unique Elements:", unique)

#Subset Checking: Write a program to check whether one set is a subset of another set without using the
#issubset() method
set1 = {10, 20}
set2 = {10, 20, 30, 40, 50}
if set1 <= set2:
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")

    #Remove Common Elements: Write a program to remove all common elements between two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
common1 = set1 - set2
common2 = set2 - set1
print("Set1 after removing common:", common)
print("Set2 after removing common:", common2)   

#. Symmetric Difference: Write a program to find elements present in either of two sets but not in both, without
#using the symmetric_difference() method
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = (set1 - set2) | (set2 - set1)
print("Symmetric Difference:", result)

# DICTIONARY
#Character Frequency: Write a program to count the frequency of each character in a given string using a
#dictionary. Example: "programming".
text = "programming"
frequency = {}
for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print("Character Frequency:", frequency)

# Word Frequency: Write a program to count the frequency of every word in a sentence using a dictionary.
#Example: "python is easy and python is powerful".
text = "python is easy and python is powerful"

frequency = {}

words = text.split()

for i in words:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("Word Frequency:", frequency)

# Highest Marks: Consider the dictionary below and write a program to find the student with the highest marks
#without using max()
students = {
    "Amit": 85,
    "Rahul": 92,
    "Sneha": 78,
    "Priya": 95
}
highest = 0
name = ""
for i in students:
    if students[i] > highest:
        highest = students[i]
        name = i

print("Student Name:", name)
print("Highest Marks:", highest)

#Sort Dictionary by Values: Write a program to arrange dictionary elements in ascending order based on their
#values without using sorted()
'''d = {"a": 30, "b": 10, "c": 20}
values = list(d.values())
values.sort()
print("Ascending Order:", value'''