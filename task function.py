#1.without arguments and without return value
#add two numbers
def add():
    a=10
    b=20
    print(a+b)
add()

#even 
def check():
    n=10 
    if n%2==0:
        print("even")
check()

#factorial
def factorial():
    n=5
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)
factorial()

#prime number
def prime():
    n=7
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count +=1
    if count ==2:
       print("prime")
    else:
     print("not prime")      
prime()  

#reverse
def reverse():
    s="python"
    print(s[::-1])
    reverse()

#palindrome
def palindrome():
    s="madam"
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not paindrome")
palindrome()

    



#2.with argument and without return value
#add two number
def add(a,b):
    print(a+b)
add(10,20)

#even 
def check(n):
    if n%2==0:
        print("even")
check(7) 

#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
        print(fact)
        factorial(5)

#prime number
def prime(n):
    count=0
    for i in range(1,n+1):
        if n %i==0:
            count +=1
    if count==2:
        print("prime")
    else:
        print("not prime")
        prime(7)   

#reverse
def reverse(s):
 print(s[::-1])
reverse("python")   


#palindrome
def palindrome(s):
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
palindrome("madam")        

#3.without argument with return value
#add two number
def add():
    a=10
    b=20
    return a+b
result=add()
print(result)

# palindrome
def palindrome():
    s="madam"
    if s==s[::-1]:
        return "not palindrome"
print(palindrome())    


#even 
def check():
    n=4
    if n % 2==0:
        return "even"
print (check()) 

#factorial
def factorial():
    n=5
    fact=1
    for i in range(1,n+1):
        fact*=i
        return fact
    print(factorial())

#prime number
def prime():
    n=7
    count=7
    for i in range(1,n+1):
        if n%i==0:
            count+=1

    if count==2:
        return "prime"    
    else:
        return "not prime"     

#reverse   
def reverse ():
    s="python"
    return s[::-1]
print(reverse())    

#4.with arguments and with return value
# add two numbers
def add(a,b):
    return a+b
result=add(10,20)
print(result)   


#even 
def check(n):
    if n % 2==0:
        return "even"
print(check(10))  

#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        return fact
print(factorial(5))

#prime number
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
                return "prime"
    else:
                return "not prime"
print(prime(7))


#reverse
def reverse(s):
    return s[::-1]
print(reverse("python"))    

#palindrome
def palindrome(s):
    if s==s[::-1]:
     return "palindrome"
    else:
      return "not palindrome"
print(palindrome("madam"))    

    


        

