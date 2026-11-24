#types of inheritance
#single inheritance
class Father:
    def house(self):
        print("Father has a house")
class son(Father):
    def bike(self):
        print("son has a bike")
s=son()
s.house()
s.bike()

#Animal
class animal:
    def eat(self):
        print("animal is eating")

class dog(animal):
    def bark(self):
        print("dog is barking")
a=dog()
a.eat()
a.bark()

#student
class person:
    def name(self):
        print("name:","gayatri")

class student(person):
    def marks(self):
        print("marks:",80)

s=student()  
s.name()
s.marks()  

#Bank
class bank:
    def bank_name(self):
        print("SBI bank")

class account(bank):
    def bank_details(self):
        print("account number:",1234)

b=account()
b.bank_name()
b.bank_details()  

#multiple  inheritance
class father:
    def house(self):
        print("father has house")

class mother:
    def gold(self):
        print("mother has gold")

class son(father,mother):
    def bike(self):
        print("son has bike")
s=son()
s.house()
s.gold() 
s.bike()

#music player and camera
class music_player:
    def play_music(self):
        print("playing music")

class camera:
    def take_photo(self):
        print("taking photo")

class smartdevice(music_player,camera):
    pass

obj=smartdevice()
obj.play_music()
obj.take_photo()

#Bank
class bank:
    def bank_name(self):
        print("bank name:SBI")

class customer:
    def customer_name(self):
        print("customer_name:gayatri")

class account(bank,customer):
    def account_no(self):
        print("account_no:12345")

a=account()
a.bank_name()
a.customer_name()
a.account_no()

#Animal
class animal:
    def eat(self):
        print("animal has eating")

class bird:
    def fly(self):
        print(" bird is flying")

class parrot(animal,bird):
    def speak(self):
        print("parrot is spek")

a=parrot()
a.eat()
a.fly() 
a.speak 

#multilevel inheritance
#grandfather father child
class grandfather:
    def house(self):
        print("grandfather has house")

class father(grandfather):
    def car(self):
        print("father has car")        

class child(father):
    def bike(self):
        print("child has bike")

c1=child()
c1.house()
c1.car()
c1.bike()  

# company-->employee-->manager
class company:
    def company_name(self):
        print("company:TCS")

class employee(company):
    def employee_name(self):
        print("employee_name:gayatri")

class manager(employee):
    def manager_work(self):
        print("manager work:HR")

c1=manager()
c1.company_name()
c1.employee_name()
c1.manager_work()

#college--> class-->student
class college:
    def college_name(self):
        print("GFGC college")

class Class(college):  
    def class_name(self):
        print("class_name degree")

class student(Class):  
    def student_name(self):
        print("student_name:anuja")  


c1=student()
c1.college_name()
c1.class_name()
c1.student_name()

#Hierarchical Inheritance
class father:
    def property(self):
        print("father has property")

class son(father):
    def bike (self):
        print("son has bike")

class dauagther(father):
    def gold(self):
        print("daughter has gold")

f1=son()
f1.property()
f1.bike()

'''class vehicle:
 def __init__(self,brand):
    self.brand=brand

class car(vehicle):
 def __init(self,brand,price): 
    super().__init__(brand)
    self.price=price 

 def display(self):
     print("bike:",self.brand)
     print("price:",self.price)

class bike(vehicle):
  def __init__(self,brand, price):
        super().__init__(brand)
        self.price=self.price

  def display(self):
    print("bike:",self.brand)
    print("price:",self.price)

  def display(self):
      print("bike:",self.brand)
      print("pratice:",self.price)
c=car("toyota",15000)
c.display()
b=bike("honda",30000)
b.display()'''

#school-->teacher-->student
class School:
    def __init__(self, school_name):
        self.school_name = school_name

class Teacher(School):
    def __init__(self, school_name, subject):
        super().__init__(school_name)
        self.subject = subject

    def display(self):
        print("School:", self.school_name)
        print("Subject:", self.subject)

class Student(School):
    def __init__(self, school_name, marks):
        super().__init__(school_name)
        self.marks = marks

    def display(self):
        print("School:", self.school_name)
        print("Marks:", self.marks)


t = Teacher("ABC School", "Python")
t.display()

s = Student("ABC School", 90)
s.display()

#hybrid inheritance

'''class a:
    def student(self):
        print("student name:gayatri")

class b(a):
    def marks(self):
        print("python:90")

class c(a):
    def city(self):
        print ("city:karnataka")

class d(b,c):
    def result(self):
        print("student result")

c=d()
c1.student()
c1.marks()
c1.city()
c1.result()'''

#employee details
class a:
    def company(self):
        print("company:wipro")
class b(a):
    def salary(self):
        print("salary:20000")
class c(a):
    def experience(self):
        print("experience:fresher")        
class d(b,c):
    def details(self):
        print("employee details")
e1=d()
e1.company()
e1.salary()
e1.experience()
e1.details()        
                    

   


