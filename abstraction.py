#class and dog
from abc import ABC, abstractmethod
class animal (ABC):
    @abstractmethod
    def eat(self):
        pass

class dog (animal):
    def eat(self):
        print("dog is met")

class cow(animal):
    def eat(self):
        print("cow eat grass")        

d=dog()
d.eat()

c=cow()
d.eat()

#vehicle car and bike
from abc import ABC,abstractmethod
class start(ABC):
    @abstractmethod
    def strat (self):
        pass

class stop(ABC):
    @abstractmethod
    def stop(self):
        pass

class Bike:

    def start(self):
        print("bike is start")


    def stop(self):
        print("bike is stop")

class car:

    def start(self):
        print("car is start")

    def stop(self):
        print("car is stop")  

b=Bike()
b.start()
b.stop()

c=car()
c.start()
c.stop()

#bank SBI and RBI
from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def calculate_interset(self):
        pass
class SBI(bank):
    def calculate_interset(self):
        print("invest SBI bank amount")

class RBI(bank): 
    def calculate_interset(self):
        print("invest RBI bank")  

s=SBI()
s.calculate_interset()
s=RBI()
s.calculate_interset()  


#rectangle and triggle
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class rectangle(shape):
    def calculate_area(self):
        length=10
        breadth=5
        print("rectangle area:",length*breadth)

class triangle(shape):
    def calculate_area(self):
        base=10
        height=0
        print("triangle area:",0.5*base*height)

r=rectangle()
r.calculate_area()
t=triangle()
t.calculate_area()  

#employee with  calculate salary developer with manager
from abc import ABC, abstractmethod
class employee(ABC):
    def calculate_salary(self):
        pass
class manager:
    def calculate_salary(self):
        print("managere calcualte_salary:", 50000)

class developer:
    def calculate_salary(self):
        print(" developer calculate_salary:",30000)

e=employee()
e.calculate_salary()

e=manager()
e.calculate_salary()

e=developer()
e.calculate_salary()

# card payment upi payment cash payment
from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def make_payment(self):
        pass

class cardpayment(payment):
    def make_payment(self):
        print("card payment successfully")

class UPI(payment):
    def make_payment(self):
        print("UPI payment succesfully")

class cash(payment):
    def make_payment(self):
        print("cash payment succesfully")

p=cardpayment()  
p.make_payment()
p=UPI()
p.make_payment()
p=cash()
p.make_payment() 

#hospital
from abc import ABC,abstractmethod
class hospital:
    @abstractmethod
    def tretment(self):
        pass

class doctor(hospital):
    def tretment(self):
        print("patient tretment")

class nurse(hospital):
    def tretment(self):
        print("check the patient")

h=doctor()
h.tretment() 
h=nurse()
h.tretment()  

#food
from abc import ABC, abstractmethod
class food:
    @abstractmethod
    def prepare_food(self):
        pass

class pizza:
    def prepare(self):
        print(" pizza food is ready")

class burger:
    def prepare(self):
        print("burger is ready")

f=pizza()
f.prepare()
f=burger()
f.prepare()

#mobile
from abc import ABC,abstractmethod
class mobile:
    @abstractmethod
    def make_call(self):
        pass

class vivo(mobile):
    def make_call():
        print("vivo is making call")

class redmi(mobile):
    def make_call(self):
        print("redmi is making call")

v=vivo
v.make_call()
r=redmi()
r.make_call()                









        





