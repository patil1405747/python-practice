class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    @property    
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        if amount >0:
            self.__balance+=amount
        else:
            print("invaild amount")
    
b1=bankaccount(1500) 
print(b1.balance)
b1.balance=600
print(b1.balance)

#public variable
class student:
    def __init__(self):
        self.name="gayatri"
        self.age=22
    def display(self):
        print("name",self.name)
        print("age",self.age)
c1=student()
c1.display()
print(c1.name)
print(c1.age)

#protected variable
class student:
    def __init__(self):
        self.name="gayatri"
        self.age=22
    def display(self):
         print("name",self.name)
         print("age",self.age)
c1=student()
c1.display()
print(c1.name)
print(c1.age) 

#private variable
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def display(self):
          print("Account Holder:", self.name)
          print("Balance:", self.__balance)
b1 = BankAccount("Rahul", 5000)
print("Name:", b1.name)
b1.display()
          