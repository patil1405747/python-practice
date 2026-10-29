x = 10
y = 3 
print(x // y) 
print(x % y)
print(x ** y)

a=5
b=2
a+=b*3
print(a)

x=10
print(x>5 and x<20)
print(x<5 or x==10)

a=5
b=3
print(a&b)
print(a | b)
print(a^b)


x="python"
print("py" in x)
print("z" not in x)

a=[10,20]
b=[10,20]
print(a==b)
print(a is b)

s="kiranacademy"
print(s[1:8:2])
print(s[::-1])

s="python"
print(s[-1:-6:-2])

x=15
if x%3==0:
    print("A")
elif x% 5==0:
    print("B")
else:
    print("C")

x=2
match x:
    case 1:
        print("One")
    case 2:
        print("two")
    case _:
        print("other")    

s="python programming"
print(s.upper()[2:8])
print(s.title())

s="     kiran academy     "
print(len(s))
print(len(s.strip()))

s="banana"
print(s.find("a"))
print(s.rfind("a"))
print(s.count("an"))

x=10
if x >5:
  if x < 15:
     print("A")
  else:
     print("B")
else:
     print("C")

x=1
for i in range(1,5):
  x*=2
print(x)

for i in range(1,6):
    if i==3:
        continue 
    print(i,end= " ")

for i in range(1,6):
    if i==4:
        break
    print(i,end=" ")


sum=0
for i in range(1,7):
    if i % 2==0:
        sum+=i
        print(sum)

i=1
while i<=5:
    print(i,end=" ")
    i+=2


i=1
while i<=5:
    if i==3:
        i+=1
        continue
    print(i,end="  ")
    i+=1

#Reverse slicing
s="kiranacademy"
print(s[-2:1:-2])

s="abcdefghij"
print(s[8:2:-2])

x=5
print(x > 2 and x < 10 or x==100)

a=5
b=3
print(a&b==1)
print(a|b==7)


x=2
match x:
    case 1|2:
        print("A")
    case 3:
        print("B")
    case _:
        print("C")

for i in range(1,4):
    for j in range(1,3):
        print(i,j,end=" |")     


for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=" ")
        print()

total=0
for i in range(1,5):
    for j in range(1,i+1):
        if(i+j) %2==0:
            total +=j
            print(total)  

i=1
count=0
while i<=10:
    if i% 2==0:
        count +=1
        i+=3
        print(count)


x=1
for i in range(1,4):
    x*=2
    if x==4:
        continue
    print(x,end=" ")
    print("|",x)                                   




