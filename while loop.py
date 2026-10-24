i=1
while i<=10:
    print(i)
    i+=1

i=10
while i>=1:
   print(i)
   i-=1    

i=2
while i<=10:
    print(i)
    i+=2

i=1
sum=0
while i<=5:
 sum+=i
 i+=1
print(sum)

'''password=" "
while password !="screct123":
   password=input("enter your password")
   print("access gentred")

   number = 12345
reversed_num = 0'''

'''while number > 0:
    digit = number % 10
    reversed_num = (reversed_num * 10) + digit
    number = number // 10
    print("Reversed Number:", reversed_num)'''

word = "PYTHON"
i = 0
while i < len(word):
    print(word[i])
    i += 1

i = 0
while i <= 5:
    i += 1
    if i == 3:
        continue
    print(i)

    a = 48
    b = 18
while b != 0:
    a, b = b, a % b
print("GCD is:", a)

i=8652653
count=0
while i>0:
   count+=1
   i=i//10
print(count)   

i=1
while i<=10:
   square=i*i
   print("square of ",i,"is",square)
   i+=1

   #print negative number a list
numbers = [10, -5, 3, -2, 0, -8, 7]
i = 0
print("Negative numbers are:")
while i < len(numbers):
  if numbers[i] < 0:
    print(numbers[i])
  i += 1 

#print positive numbers from a list
numbers = [10, -5, 3, -2, 0, -8, 7]
i = 0
while i<len(numbers):
    if numbers[i]>0:
     print(numbers[i])
    i+=1  

#reverse tha number
num=54321
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print("reversed:",rev)

#print the multiples of 3 up to 30
num = 3
while num <= 30:
    print(num)
    num += 3

for num in range(3, 31, 3):
    print(num)

# count from 1 to 5
    i=1
    while i<=5:
      print(i)
      i +=1

total = 0
i = 1
while i <= 5:
    total += i
    i += 1
print("Total sum:", total)

num = 1
while num <= 10:
    if num == 4:
        break
    print(num)
    num += 1

#print cube from 2 to 20
i=2
while i<=20:
   cube=i*i*i
   print("cube of",i,"is",cube)
   i+=1 