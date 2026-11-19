#student details
class student:
  def details(self,name,age,course,marks):
    self.name=name
    self.age=age
    self.course=course
    self.marks=marks
  def display(self):
      print("name:",self.name)
      print("age:",self.age)
      print("course:",self.course)
      print("marks:",self.marks)
s1=student()
s1.details("gay",20,"python",90)
s1.display()    

#car details
class car():
  def details(self,brand,color,model,price):
    self.brand=brand
    self.color=color
    self.model=model
    self.price=price
  def display(self): 
   print("brand:",self.brand)
   print("color:",self.color)
   print("model:",self.model)
   print("price:",self.price)
swift=car()
swift.details("swift", "white", "2026", 200000)
swift.display()

#mobile details
class mobile():
  def details(self,brand, model, ram, price):
    self.brand=brand
    self.model=model
    self.ram=ram
    self.price=price
  def display(self):
   print("brand:",self.brand)
   print("model:",self.model)
   print("ram:",self.model)
   print("price:",self.price)
m1=mobile()
m1.details("vivo","s24","8GB",20000)
m1.display()  
      
#bank detais
class bank():
  def details(self,name,accountno,balance):
    self.name=name
    self.accountno=accountno
    self.balance=balance
  def display(self):
   print("name:",self.name)
   print("accountno:", self.accountno)
   print("balance:", self.balance)
b1= bank()
b1.details("kiran",12345,50000)
b1.display()   

#movie
class Movie:
    def details(self, name, hero, language, rating):
        self.name = name
        self.hero = hero
        self.language = language
        self.rating = rating
    def display(self):
        print("Movie:", self.name)
        print("Hero:", self.hero)
        print("Language:", self.language)
        print("Rating:", self.rating)
m1 = Movie()
m1.details("KGF", "Yash", "Kannada", 9)
m1.display()

#addition of numbers
class addition:
  def details(self,a,b):
    self.a=a
    self.b=b
  def display(self):
      print(" first number:",self.a)
      print("second number:",self.b)
      print("addition:",self.a+self.b)
a1=addition()
a1.details(10,20)  
a1.display()   

#fruit
class fruit():
  def details(self, name,color,price):
    self.name=name
    self.color=color
    self.price=price
  def display(self):
   print("name:",self.name)
   print("color:",self.color)
   print("price:",self.price) 
f1=fruit()
f1.details("apple","pink",20)
f1.display()

#ATM details
class ATM:

    def details(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdraw Success")
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")


a1 = ATM()

a1.details("Rahul", 10000)
a1.display()
a1.withdraw(2000)




#polidrome

class Palindrome:
    def details(self, text):
        self.text = text

    def check(self):
        if self.text == self.text[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")

p1 = Palindrome()
p1.details("madam")
p1.check()

#factorial
class Factorial:
    def details(self, num):
        self.num = num
    def calculate(self):
        fact = 1
        for i in range(1, self.num + 1):
            fact = fact * i
            print("Factorial:", fact)

f1 = Factorial()
f1.details(5)
f1.calculate()