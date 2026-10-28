a=[]
b=[10,20,30]
c=["apple", "mango"]
d=[10,"hello", 5.5]
print(a,b,c,d)

a=[10,20,30,40]
print(a[0])
print(a[-1])
print(a[-2])



a=[10,20,30,40,50]
a[1]=25
print(a)
print(a[1:4])


a=[10,20]
a.append(30)
a.extend([40,50])
a.insert(1,15)
print(a)


a=[10,20,30,40]
a.remove(20)
print(a)
a.pop()
print(a)


a=[30,10,20]
a.append(40)
print(len(a))
print(max(a))
print(min(a))


a=[10,20,30]
for i in a:
    print(i)


a=[1,2]
b=[3,4]
print(a+b)
print(a*2)
print(2 in a)

a=[10,20,30]
x,y,z=a
print(x)
print(y)
print(z)


a=[10,20,30]
b=a
c=a.copy()
b[0]=99
print(a)
print(c)


a=[[10,20],[30,40]]
print(a[0])
print(a[1])
print(a[0][1])



a=[30,10,20]
a.sort()
print(a)
b=[50,40,60]
print(sorted(b))


a=[1,2,3,4,5]
b=[i*2 for i in a]
print(b)



a=[10,20,30,40]
for i in a[:]:
    if i==20:
      a.remove(i)
    print(a)





    