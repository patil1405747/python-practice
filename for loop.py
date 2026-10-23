#print 1 to 100 
for i in range(1,101):
  print(i)

#print odd number with using if
for i in range(1,100):
  if(i%2==1):
   print("odd numbers",i) 

#print odd number without using is statement
for i in range(1,100,2):
 print(i) 

#print even number using if statement
for i in range(100):
  if(i%2==0) :
   print("even number")

#print 2 table 
for i in range(2,21,2):
 print(i)   

#print reverse numbers 200 to 1
for i in range(200,0,-1):
 print(i) 

#print numbers -100 to 100
for i in  range (-100,101):
 print(i)

#print 1 to 100 number with skipping 1 number
for i in range(1,101,2):
 print(i)  

#factorial
n=5
fact=1
for i in range(1,n+1):
  fact*=i
print(fact)  

numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print("Sum:", total)

#reverse the number
num=12345
for i in (str(num)[::-1]):
 print(i)

numbers = [15, 42, 7, 89, 23]
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print("Maximum:", max_val)

for i in range(3):
   print(i)
else:
   print("loop finished successfully")

for i in range(1,6):
    if i==3:
      print(i)

 #print 1 to 100 number with skipping 1 number
for i in range(1,100,-2):
 print(i)    

for char in "Python":
    print(char)

#print even number from 1 to 20
for i in range(0,21,22):
    print(i)

#print add number from 1 to 20
for i in range(1,21):
  print(i)

  for i in range(1, 6):
    print(i)

for i in range(2, 11, 2):
    print(i)

    total=0
    for num in[1,2,3,4,5,]:
      print(i)

for i in range(1, 5):
    print(i**2)


for i in range(1, 4):
    print(i**3)

    prod = 1
for n in [2, 3, 4]:
    prod *= n
print(prod)

for i in range(2):
    for j in range(3):
        if j == 1:
            break
        print(i, j)

count=0
for i in range(1,51):
   count+=1
   print(count)

for i in range(1,6):
   print(i**4)   

for i in range(1,11):
     if i % 2 == 0:   
         print("i even")
else:
   print("i odd")

for i in range(1, 6):
    print(str(i) * i)   

   