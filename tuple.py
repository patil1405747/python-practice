#creating tuple
tuple=(4,5,3,7,8)
print(tuple)

# creating tuple using ,
tuple=23,54,67,12,43,56
print(tuple)

#tuple is immutable(cannot be changed)
'''tuple=(20,40,30,45,10,15)
tuple[0]=6
print(tuple)'''

#tuple built in function
tuple=(20,40,30,45,10,15)
tuple=max(tuple)
print(tuple)

tuple=(20,40,30,45,10,15)
tuple=min(tuple)
print(tuple)

tuple=(20,40,30,45,10,15)
tuple=sum(tuple)
print(tuple)

#immutable and mutable
tuple=(24,50,[50,60,20],65,58)
tuple[2].append(56)
print(tuple)

#packing and unpacking
tuple=(1,"ram","pune")
id,name,city=tuple
print(id)
print(name)
print(city)

#tuple methods
#index()
tuple=(10,20,30,40,50,60,45,35)
tuple=tuple.index(30)
print(tuple)

#count()
tuple=(30,50,45,25,60,46,25)
tuple=tuple.count(25)
print(tuple)
