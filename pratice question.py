#Remove Duplicate Elements: Write a Python program to remove duplicate elements from a list without using set().
numbers=[10,20,10,30,20,40]
result=[]
for i in numbers:
    if i not in result:
        result.append(i)
        print(result)

#Find Second Largest Element: Write a program to find the second-largest element from a list without using the sort() method.
a=[10,50,20,80,40]  
a.sort()
print("second largest:",a[-2])

 #Separate Even and Odd Numbers: Write a program to separate even and odd numbers from a list and store them in two different lists.
'''a = [10, 15, 20, 25, 30, 35]
even=[]
odd=[]
for i in a:
    if i % 2==0:   
         even.append[i]
    else:
        odd.append[i]
print("even numbers:",even)
print("odd numbers:",odd)'''

#Find Common Elements: Write a program to find common elements between two lists without using set operations.
'''list=[10,20,30,40]
list=[30,40,50,60]
print("comman elements:",comman)'''

# Move Zeros to the End: Write a program to move all zeros to the end of a l
a = [0, 10, 0, 20, 30, 0, 40]

for i in a:
    if i != 0:
        print(i, end=" ")

for i in a:
    if i == 0:
        print(i, end=" ")

#Find Unique Elements: Write a program to remove duplicate values from a list using a set and display only unique elements.
a = [10, 20, 10, 30, 20, 40]
b = set(a)
print(b)

#Find Union and Intersection: Write a program to find the union and intersection of two sets.
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))

#Find Difference: Write a program to display elements that are present in the first set but not in the second set.
A = {10, 20, 30, 40}
B = {30, 40, 50}
print("Difference:", A.difference(B))

#Find Common Students: Two sets contain the names of students enrolled in Java and Python courses. Write a program to display students enrolled in both courses.
Java = {"Amit", "Rahul", "Sneha", "Priya"}
Python = {"Sneha", "Priya", "Raj", "Kiran"}
common = Java.intersection(Python)
print("Common Students:", common)   

#Check Subset: Write a program to check whether all elements of one set are present in another set.
A = {10, 20}
B = {10, 20, 30, 40, 50}
if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")