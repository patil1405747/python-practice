#creating sets
a={10,20,30,40}
print(a)

#using sets
a=set((10,20,30))
print(a)

#create an empty set
num=set()
print(num)

#{} creates an empty dict,not a seta={}
a={}
print(a)
print(type(a))

num={10,20,30,40,50}
print(num)

#sets methods
#add
fruits={'apple','banana','cherry'}
fruits.add('mango')
print(fruits)

fruits.add('kiwi')
print(fruits)

fruits.add('apple')
print(fruits)

#remove
fruits.remove('apple')
print(fruits)

#remove one element
a={10,20,30,40,50}
a.remove(20)
print(a)

#remove first value
num={1,2,3,4,9}
num.remove(1)
print(num)


#sets opeartion
1.#union sets
a={1,2,3}
b={3,4,5}
union_set=a.union(b)
print(union_set)

union_set=a|b
print(union_set)

#comman values
a={10,20,30}
b={40,50,60}
print(a.union(b))

#string values
a={"apple","banana"}
b={"kiwi","orange"}
print(a.union(b))

#theree sets
a={1,2}
b={3,4}
c={5,6}
print(a.union(b,c))

#duplicates values
a={10,20,30}
b={10,20,40}
print(a.union(b))

2.#intersection(&)
a={10,20,30}
b={20,30,40}
print(a&b)

3.#difference(-)
a={10,20,30}
b={40,20,50}
print(a-b)

4.#symmetric difference(^)
fruits={'mango','banana', 'orange'}
b={'mango', 'paneapple','apple'}
print(fruits^b)

#type of sets

#sets
a={10,40,30,20,60}
print(a)

a.add(50)
print(a)

a.remove(20)
print(a)

#frozenset
a=frozenset([10,20,30,40])
print(a)
print(20 in a)
print(len(a))












