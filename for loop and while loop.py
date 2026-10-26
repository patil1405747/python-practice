# for loop
#print factorial 5
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")


#Fibonacci
n = 10
a, b = 0, 1
print("Fibonacci Series using For Loop:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b





#while loop
# print factorial 5
num = 5
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"The factorial of {num} is {factorial}")


#Fibonacci
n = 10
a=0
b=1
count = 0

print("Fibonacci Series using While Loop:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

    

    #prime number
    #for loop
numbers = [2, 3, 4, 5, 6, 7, 8]
prime_numbers = []
for num in numbers:
    if num > 1:
        is_prime = True
    
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break 
        
        if is_prime:
            prime_numbers.append(num)

print("Original List:", numbers)
print("Prime Numbers:", prime_numbers)


#while loop
numbers = [2, 3, 4, 5, 6, 7, 8]
prime_numbers = []

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  
        
        if is_prime:
            prime_numbers.append(num)

print("Original List:", numbers)
print("Prime Numbers:", prime_numbers)