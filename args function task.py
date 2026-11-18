#create a functon to display student details using positional arguments
def student(name,age,course):
    print("student name:",name)
    print("student age:",age)
    print("student course:",course)
student("gayatri",20, "python")

#create an employee function to pass detail using keyword argument
def employee(name,id,salary,age):
    print("employee name:",name)
    print("employee id:",id)
    print("employee salary:",salary)
    print("employee age:",age)
employee(name="gayatri",id=101,salary=30000,age=20) 


#create a function to calculate the sum of any number of arguments *args
def total(*args):
    result=0
    for i in args:
        result=result+i
        print("total sum:",result)
total(10,20,30,40,50)

    