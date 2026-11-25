#polymorphism
class dog:
    def sound(self):
        print("dog is barking")

class cat:
    def sound(self):
        print("cat is mewo")

d=dog()
d.sound()
c=cat()
c.sound()     

#types of polymorphism
#method overloading
class calculation:
    def add(*args):
        total=0
        for i in args:
          total=i
        print(total)
c=calculation() 

c.add(20,20,30)
c.add(10,20)
c.add(10,20,30,40)

#shopping

class shopping:
    def bill(self,*args):
        total=0
        for i in args:
            total=i
            print("total bill:",total)
s=shopping()
s.bill(100,200)
s.bill(100,200,300)
s.bill(100,200,300,400) 

#student details
class student:
    def details(self,**kwargs):
        for key,value in kwargs.items():
            print(key, ":", value)
s=student()
s.details(name="gayatri",age=20)
s.details(name="gayatri",age=20,city="pune")  

#employee
class employee :
    def salary(self,basic,bonus=1):
        print("total salary-->",basic+bonus)
emp=employee()
emp.salary(10000,10000)
emp.salary(2000)  

#calculator
class calculator:
    def add(self,a=0,b=0):
        print(a+b)
c=calculator()
c.add(10,20)
c.add(10)
c.add()

#class employee using*args
class employee:
    def multify(self,*args):
        result=1
        for i in args[2:]:
            result*=1
            print("multiplication result:",result)
e=employee()
e.multify("rahul",2,3)

#display names
class person:
    def display(self,*args):
        for i in args:
            print(i)

p=person()
p. display("ram","sam")
p.display("ram","raj")



#method overiding
#Animal
class animal:
    def sound(self):
        print("animal marks sound")

class dog(animal):
    def sound(self):
        print("dog barking")

a=dog()
a.sound()

#vehicle
class vehicle:
    def start(self):
        print("vehicle starts")

class car:
    def start(self):
        print("car starts")

v=car()
v.start()  

#student details
class student:
    def study(self):
        print("student is studying")

class teacher(student):
    def study(self):
        print("teacher is teaching")

t=teacher()
t.study()        


#student details using *args
class student:
    def marks(self,*args):
        print("student marks:",sum)
    
class result(student):
    def marks(self,*args):
        print("total marks:",sum(args))
        print("avg:",sum(args)/len(args))
r=result()
r.marks(30,40)
r.marks(50,60,70) 

#bank
class Bank:
    def interest(self):
        print("Bank interest is 5%")

class SBI(Bank):
    def interest(self):
        print("SBI interest is 7%")

s = SBI()
s.interest()


