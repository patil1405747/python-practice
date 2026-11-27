#student management system

class student:
    def __init__(self,name,roll_no,marks):
       self.name=name
       self.roll_no=roll_no
       self.marks=marks

    def display_details(self):
        print("student name:",self.name)
        print("roll_no:",self.roll_no)
        print("marks:",self.marks)
s=student("gayatri",1,80)
s=student("anuja",2,70)
s=student("swati",3,85)

s.display_details()
s.display_details()
s.display_details()   

#Bank account
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"deposite balance {amount} total balance {self.__balance}")
        else:
            print("invalid amount")
    def withdraw (self,amount):
        if amount>0:
            self.__balance-=amount
            print(f"withdraw balance {amount} total balance {self.__balance}")
        else:
            print("amount is not available")
    def display_balance(self):
        print(f"account holder name {self.name}")
        print(f"total balance {self.__balance}")
b=BankAccount("anuja",50000)
b.display_balance()
b.deposite(25000)
b.withdraw(10000)
b.display_balance()

#employee account 
class employee:
 def emp(self,name,emp_id,salary):
    self.name=name
    self.emp_id=emp_id
    self.salary=salary

 def dis_emp(self):
   print("name:",self.name)  
   print("emp_id:",self.emp_id) 
   print("salary:",self.salary)

class manager(employee):
 def man(self,department):
         self.department=department

 def dis_manager(self):
    self.dis_emp()
    print("department:",self.department)        

m=manager()
m.emp("gayatri",1,2000)
m.man("python")

#payment system
class creditcard:
   def payment(self):
      print("payment using creditcard")

class UPI:
   def payment(self):
      print("using UPI")

class netbanking:
   def payment(self):
      print("using netbanking")

p=creditcard()
u=UPI()
n=netbanking()

p.payment()
u.payment()
n.payment()

#vehicle management
class vehicle:
   def start(self):
      print("car is start")

class bike(vehicle):
   def start(self):
      print("bike is start")

class bus(vehicle):
   def start(self):
      print("bus is start")

class car(vehicle):
   def start(self):
      print("car is start")


b=bike()
bus=bus()
c=car()

b.start()
bus.start()
c.start()

#calculate area
from abc import ABC,abstractmethod
import math
class shape(ABC):
    @abstractmethod
    def cal_area(self):
        pass
class rectangle(shape):
    def __init__(self,height,widht):
        self.heght=height
        self.widht=widht
    def cal_area(self):
        print(f"area of a rectangle {self.heght * self.widht} " )

class circle(shape):
    def __init__(self,redius):
        self.redius=redius 

    def cal_area(self):
        print(f"area of a circle {math.pi * self.redius**2}")

rect=rectangle(54,87)
rect.cal_area()
c=circle(7) 
c.cal_area()           

#Book
class book:
   def __init__(self,book_name,author,price):
      self.book_name=book_name
      self.author=author
      self.price=price
   def display_book(self):
      print("book_name:",self.book_name)
      print("author:",self.author)
      print("price:",self.price)
   def apply_discount(self,discount):
      self.price=self.price-discount
      print("discount price:",self.price)
b1=book("python","kiran",100) 
b2=book("sql","david",200)
b3=book("java","john",300)
b1.display_book 
b1.apply_discount(20)

b2.display_book
b2.apply_discount(30)

b3.display_book()
b3.apply_discount(40)

#hospital management
class person:
   def __init__(self,name,age):
      self.name=name
      self.age=age
   def display_person(self):
      print("name:",self.name)
      print("age:",self.age)

class doctor(person):
   def __init__(self,name,age,specialization):
      super().__init__(name,age)
      self.specialization=specialization

      def display_doctor(self):
         print("specialization:",self.specialization)

class surgeon(doctor):
      def __init__(self,name,age,specialization,experience):
         super().__init__ (name,age,specialization)
         self.experience=experience

      def display_surgeon(self):
         self.display_person()
         print("operation experiance:",self.experience,"years")

s=surgeon("gayatri",30,"heart surgeon",10)          
s.display_surgeon()

#employee
class employee:
   def __init__(self,name,age,salary):
      self.name=name
      self.age=age
      self.__salary=salary
   def get_salary(self):
      return self.__salary
   def set_salary(self,salary):
      if salary>0:
         self.__salary=salary
         print("salary update sucessfully")
      else:  
         print("invaild salary")
class developer(employee):
   def __init__(self,name,age,salary,language):
      super().__init__(name, age, salary)
      self.language = language
   def display_developer(self):
        print("employee Name:", self.name)
        print("Age:", self.age)
        print("programming language:", self.language)
        print("salary:", self.get_salary())
d=developer("rahul",20,4000,2000)
d.display_developer  
d.set_salary(5000)
print("update salary:",d.get_salary()) 



#food order system
from abc import ABC,abstractmethod
class food():
    def __init__(self,price,quantity):
      self.price=price
      self.__quantity=quantity

    def get(self):
        return self.__quantity  
    def set(self,quantity):
        if quantity>0:
            self.__quantity+=quantity
        else:
            print("quantity must be greater than zero")
    @abstractmethod
    def cal_bill(self):
        pass


class pizza_order(food):
    def __init__(self, price, quantity,crust_type):
        super().__init__(price, quantity)
        self.crust_type=crust_type
    def cal_bill(self):
        base_total=self.price*self.get() 
        delivery_fee=5.00
        return base_total+delivery_fee
    def dis_bill(self):
        print("crust type-->",self.crust_type)  
        print("quantity-->",self.get())
        print("price-->",self.price)
        print("total bill-->",self.cal_bill())

class  burger(food):
    def __init__(self, price, quantity,meal_cambo):
        super().__init__(price, quantity) 
        self.meal_cambo=meal_cambo
    def cal_bill(self):
        base_total=self.price*self.get()
        if self.meal_cambo:
            base_total*=1.20
        return base_total
    def dis_bill(self):
        print(f"is mael cambo-->{"yes" if self.meal_cambo else 'NO'}")   
        print(f"quantity-->{self.get()}")
        print(f"price {self.price}")
        print(f"total bill{self.cal_bill()}")
pizza=pizza_order(100,1,"stuffed  crust")
burger=burger(50,2,meal_cambo=True)

pizza.dis_bill()
burger.dis_bill()
        
        
        