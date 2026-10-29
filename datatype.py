#print every element of a list
numbers={10,20,30,40,50}
for num in numbers:
    print(num)

#find the sum without using
numbes=[10,20,30,40]
total=0
for num in numbers:
    total=total + num
    print("sum:",total)


#find the largest number without using max().
numbers=[15,45,25,60,10]
largest = numbers[0]

#find the largest number without using max()
for num in numbers:
    if num>largest:
        largest=num
        print(largest)

#count even and odd  numbers.
numbers=(1,2,3,4,5,6)
even=0
odd=0
for num in numbers:
    if num % 2==0:
        even +=1
else:
    odd+=1
    print(even)
    print(odd)


#sarch for a number without using.
numbers=[10,20,30,40]
target=30
found=False
for num in numbers:
    if num == target:
        found = True
        break
if found:
    print("number found")
else:
    print("number not found")   

#count how many times a value appears
numbers=[10,20,10,30,10,40]
target=3
count=0
for num in numbers: 
      if num == target:
         count+=1
print(count)   

#create a new list containg only positive numbers.
numbers=[10,0,-40,50,60,-80,-60]
positive=[]
for num in numbers:
    if num >0:
        positive.append(num)
        print(positive)

#reverse a list without using reverse() or slicing.
number=[10,20,30,40,50]
reversed_list=[]
for i in range(len(numbers) -1,-1,-1):
    reversed_list.append(numbers[i])
    print(reversed_list)


#separate even and odd numbers into two list
numbers= [ 1 ,2,3,4,5,6]
even=[]
odd=[]
for num in numbers:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)

#student average marks
marks=[80,50,60,30]
total=0
for marks in marks:
  total +=marks
average=total/(marks)
print(average)


#move all zeros to end of a list
numbers=[10,10,0,20,30,0,40]
result=[]
for num in numbers:
    if num!=0:
        result.append(num)
for num in numbers:
    if num==0:
        result.append(num)
        print(result)        

