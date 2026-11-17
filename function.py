#function
#type of function

#user define function
def add(a,b):
    print(a+b)
add(2,3)


def mul(a,b):
    print(a*b)
mul(5,8)

def mul(a,b):
    return a*b
print(mul(5,5))

#Args with return type
def sum(x,y):
    return x+y
print(sum(4,5))

#args without return type
def sub(a,b):
    print(a-b)
    sub(4,5)

#no args with return type
def sub():
    a=4
    b=2
    return a-b
print(sub())  

#no args with return type
def sub():
    x=8
    y=6
    return x-y
print(sub())

#no args without return type
def sub():
    x=5
    y=9
    return x-y
print(sub())


#student information
def studinfo(name,age,city,gender):
    print("name-->",name)
    print("age-->",age)
    print("city-->",city)
    print("gender-->",gender)
studinfo("gayatri",21,"pune","female")

def studinfo(name,age,city,gender):
    print("name-->",name)
    print("age-->",age)
    print("city-->",city)
    print("gender-->",gender)
studinfo(name="gayatri",age=21,city="pune",gender="female")   


#insert default value
def studinfo(name,age,city,gender="female"):
    print("name-->",name)
    print("age-->",age)
    print("city-->",city)
    print("gender-->",gender)
studinfo(name="gayatri",age=21,city="pune")  





    



    
    