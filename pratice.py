x=[10,20,30,40]
print(x[2])

x=[1,2,3]
x.append(4)
print(x)

x=[10,20,30]
x.insert(1,99)
print(x)

x=[1,2,3,4,5]
print(x[1:4])

x=[10,20,30]
print(x[-2])

x=[1,2,3]
x.append([4,5])
print(x)

x=[10,20,30]
print(x.pop())
print(x)

x=[10,20,30,20]
x.remove(20)
print(x)

x=[1,2,3,4]
x.reverse()
print(x)

x=[10,20,30]
y=x
y.append(40)
print(x)
print(y)

x=[10,20,30]
y=x.copy()
y.append(40)
print(x)
print(y)

x=[[1,2],[3,4],[5,6]]
print(x[::-1])


x=[1,2,3]
print(x*2)

#secotion b
x=(10,20,30)
print(x[1])

x=(1,2,3,4)
print(x[-1])

x=(10,20,30,40)
print(x[1:3])

x = (1, 2, 3) 
print(len(x))

x = (10,)
print(type(x))

x=(10)
print(type(x))

x=(10)
print(type(x))

x=(1,2)
print(x*3)

x=(10,20,30)
a,b,c=x
print(a)
print(b)

25.
x=(10,20,30,40)
a,*b=x
print(a)
print(b)

26.
x=(1,2,3,2,2)
print(x.count(2))

27.
x=(10,20,30)
print(x.index(20))

28.
x=(1,2,3)
print(2 in x)

29.
x=(1,2,3)
print(2 in x)

30.
x=(1,2,3,4,5)
print(x[::-2])

31.
x={1,2,3,4}
print(len(x))

32.
x={1,2,2,3,3,3}
print(len(x))

33.
x={1,2,3}
x.add(4)
print(x)

34.
x={1,2,3}
x.update([3,4,5])
print(x)

35.
x={1,2,3}
x.remove(2)
print(x)

36.
x={1,2,3}
x.discard(10)
print(x)

37.
a={1,2,3}
b={3,4,5}
print(a | b)

38.
a={1,2,3}
b={2,3,4}
print(a&b)

39.
a={1,2,3}
b={3,4}
print(a-b)

40.
a={1,2,3}
b={3,4,5}
print(a^b)

41.
a={1,2}
b={1,2,3,4}
print(a.issubset(b))

42.
a={1,2,3,4}
b={2,3}
print(a.issuperset(b))

43.
a={1,2}
b={3,4}
print(a.isdisjoint(b))

44.
x=set("banana")
print(type(x))

45.
d={"a":10,"b":20}
d["c"]=30
print(d)

46.
d={"name":"kiran","age":25}
print(d["name"])

47.
d={"a":10,"b":20}
d["c"]=30
print(d)

48.
d={"a":10,"b":20}
d["a"]=99
print(d)

49.
d={"a":10,"b":20}
print(d.get("c"))

50.
d={"a":10,"b":20}
print(d.get("c",100))

51.
d={"a":10,"b":20}
print(list(d.keys()))

52.
d={"a":10,"b":20}
print(list(d.values()))

53.
d={"a":10,"b":20}
print(list(d.items()))

54.
d={"a":10,"b":20}
x=d.pop("a")
print(x)
print(d)

55.
d={"a":10,"b":20}
d.update({"b":99,"c":30})
print(d)







