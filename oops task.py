#student management
class student:
    def __init__ (self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course
    def display(self):
        print("name:",self.name)
        print("roll_no:",self.roll_no)
        print("course:",self.course)
s1=student("gayatri",1,"python")
s1.display()   

#employee salary details
class employee:
    def __init__(self,emp_name,emp_id,emp_salary):
        self.name=emp_name
        self.id=emp_id
        self.salary=emp_salary
    def calculate_salary(self):
        annual_salary=self.salary*12
        print("annual_salary:",annual_salary)   
emp=employee("anuja",1,50000)
emp.calculate_salary()  

#mobile phone details
class mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("model:",self.brand)
        print("price:",self.price)
    def apply_discount(self):
        final_price=self.price=self.apply_discount
        print("final_price:",final_price)
m1=mobile("vivo", "v20",10000)
m1.display()
m1.apply_discount()


#Laptop information
class laptop:
    def __init__(self):
        self.brand="dell"
        self.RAM= "18gb"
        self.price=20000
    def display(self):
        print("brand:",self.brand)
        print("RAM:",self.RAM)
        print("price:",self.price)
l1=laptop()
l1.display()

#Book information
class book:
    def __init__(self,book_name,author_name,price):
        self.book_name=book_name
        self.author_name=author_name
        self.price=price
    def display(self):
        print("bookname:",self.book_name)
        print("authorname:",self.author_name)
        print("price:",self.price)
b1=book("python", "kiran sir",20)
b2=book("java","kiran",30)
b1.display()
b2.display()   

#Rectangle area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        area = self.length * self.width
        print("Area:", area)
r1 = Rectangle(10, 5)
r1.calculate_area()

#Electricitybill

class ElectricityBill:
    def __init__(self, customer_name, units):
        self.customer_name = customer_name
        self.units = units
    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5
        elif self.units <= 200:
            bill = (100 * 5) + (self.units - 100) * 7
        else:
            bill = (100 * 5) + (100 * 7) + (self.units - 200) * 10

        print("Customer Name:", self.customer_name)
        print("Units Consumed:", self.units)
        print("Total Electricity Bill: ₹", bill)
b1 = ElectricityBill("Gayatri", 250)
b1.calculate_bill()

 #product inventroy
class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display_product(self):
            print("name:",self.name)
            print("price:",self.price)
            print("quantity:",self.quantity)
    def calculate_total_price(self):
        total = self.price*self.quantity
        print("Total Price:",total)

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Updated Quantity:", self.quantity)
p1 = product("Laptop", 50000, 2)
p1.display_product()
p1.calculate_total_price()
p1.update_quantity(5)
p1.calculate_total_price()

 #employee counter
class employee:
    #class variable
    company_name="infosys"
    employee_count=0
    def __init__(self,employee_name,employee_id):
        #instance variable
        self.employee_name=employee_name
        self.employee_id=employee_id
        #increase employee count
        employee.employee=+1
    def display_employee (self):
        print("company name:",employee.company_name)  
        print("employee_name:",self.employee_name)
        print("employee_id:",self.employee_id)
       #creating object
e1=employee("gayatri",1)  
e2=employee("shilpa",2)
e3=employee("poornima",3)
#display details
e1.display_employee()
e2.display_employee()
e3.display_employee()
# Total employees
print("Total Employees:", employee.employee_count)

#school student information
class variable: 
    school_name="govt high school"
    def __init__(self, student_name, roll_no):
    #instance variable
       self.student_name=student_name
       self.roll_number=roll_no

    def display_student(self):
    #local variable
     percentage=80.10
     print("student_name:",self.student_name)   
     print("roll_no:",self.roll_number)
     print("school name:",variable.school_name)
     print("percentage:",percentage)

s1=variable("Swati",10)
s2=variable("Sakshi",12)

s1.display_student()
s2.display_student()   

#shopping cart
class shoppingcart:
    discount_percentage=0
    def __init__(self,customer_name,total_amount):
        self.customer_name=customer_name
        self.total_amount=total_amount
    def calculate_discount(self):
       discount=self.total_amount*shoppingcart.discount_percentage/100
       final_amount=self.total_amount-discount
       print("customer name:",self.customer_name)
       print("total amount:",self.total_amount)
s1=shoppingcart("gayatri",2000)
s1.calculate_discount()

#hospital patient
'''class hospital:
    hospital_name="city hospital"
    def __init__(self,patient_name,patient_age,disease):
      self.patient_name=patient_name
      self.patient_age=patient_name
      self.disease=disease
    def display_patient(self):
       print("patient_name:", self.patient_name)
       print("patient_age:",self.patient_age)
       print("city:",self.city)
p1=hospital("gayatri",20, "pune")  
p2=hospital("anuja",21,"nsk") 
p3=hospital("sneha",22,"noida")     
p1.display_patient()
p2.display_patient()
p3.display_patient()'''

#online course management
class course:
    insinstance_name="abc institute"
    def __init__(self,course_name,course_fee):
        self.course_name=course_name
        self.course_fee=course_fee
    def calculate_fee(self):
        discount=self.course_fee*10/100
        final_fee=self.course_fee-discount
        print("course name:",self.course_name)
        print("course fee:",self.course_fee)
        print("discount:",discount)
        print("final fee:",final_fee)
        
c1=course("python",2000) 
c1.calculate_fee()     

#Temperature converter
class temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    def celsius_to_fahrenheit(self):
        return(self.celsius*9/5)+32
    def fahrenheit_to_celsius(self,fahrenheit):
        return(fahrenheit-32)*5/9
t1=temperature(30)
print("celsium to fahrenheit:",t1.celsius_to_fahrenheit())
print("fahrenheit to celsius:",t1.fahrenheit_to_celsius(98.6))

#student marks management
class student:
    def __init__(self,student_name,python_marks,sql_marks,excel_marks):
        self.student_name=student_name
        self.python_marks=python_marks
        self.sql_marks=sql_marks
        self.excel_marks=excel_marks
    def calculate_total(self):
            total_marks=self.python_marks+self.sql_marks+self.excel_marks
            return total_marks
    def calculate_percentage(self):
            total_marks=self.calculate_total()
            percentage=(total_marks/300)*100
            return percentage
    def display_result(self):
            print("student_name:",self.student_name)
            print("python_marks:",self.python_marks)
            print("sql_marks:",self.sql_marks)
            print("excel_marks:",self.excel_marks)
s1=student("gayatri",80,85,90)
s2=student("anuja",90,95,85)
s3=student("shubhanggi",80,85,70)
s1.display_result()
s2.display_result()
s3.display_result()

#food order
class foodorder:
  def __init__(self,customer_name,food_item,food_price,quantity):
    self.customer_name=customer_name
    self.food_item=food_item
    self.food_price=food_price
    self.quantity=quantity
  def calculate_bill(self):
    return self.food_price*self.quantity
    
  def apply_coupon(self,discount):
    total=self.calculate_bill()
    return total-(total*discount/100)
  def display_order(self):
    print("customer name:",self.customer_name)
    print("food:",self.food_item)
    print("total:",self.quantity)
    print("total_bill:",self.calculate_bill)
    print("final bill:",self.apply_coupon)
f1=foodorder("gayatri","piza",200,2)
f1.display_order()


    



                   
        


       
            




