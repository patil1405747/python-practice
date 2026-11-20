#constructor
class employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary

    def display(self):
        print("name-->",self.name)
        print("department-->",self.department)
        print("department-->",self.salary)

emp=employee("gayatri","full stack developer","10000")
emp.display()   

#class variable and instance variable
class student:
    college="GFGC SADALAGA"# class variable
    def __init__(self,name,age,course,marks):
        self.name=name #instance variable
        self.age=age
        self.course=course
        self.marks=marks
    def display(self):
        print("name-->",self.name)
        print("age-->",self.age)
        print("course-->",self.course)
        print("marks-->",self.marks)
        print("college-->",student.college)
s1=student("anuja",22,"data analyst",89)
s2=student("gyatri",22,"python",99)
s1.display()   
s2.display()   

#local variable and global variable
company="TCS" #global variable
class employee:
   def __init__(self, name, age,salary):
       self.name=name
       self.age=age 
       self.salary=salary
       department="HR" #local variable
       print("name:",name)
       print("age:",age)
       print("salary:",salary)
e1=employee("kiran",30,100000)   

#hospital
class hospital:
    name="kirshn hospital"
    def __init__(self,p_name,age):
        self.p_name=p_name
        self.age=age
    def display(self):
        print("Patient Name:",self.p_name)
        print("age:",self.age)
p1=hospital("sakshi",22)
p2=hospital("swati",25)
p1.display()
p2.display()
        

        

    
