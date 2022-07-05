# Function to print triangle pattern

def triangle(n):
    for i in range(0,n+1):
        for j in range (0,i+1):
            print("* ",end="")
        print(" ")  
n = 5
triangle(n)

#-----------------------------------------------------------------------------------------

# Write a program to make such a pattern like right angle triangle with number increased by 1.

def contnum(n):
     
    num = 1
    for i in range(0, n):     
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
n = 5 
contnum(n)

#-----------------------------------------------------------------------------------------

# Write a program to calculate the factorial of a given number

def fact(n):
    if n == 1:
        return n
    else: 
      return  n * fact(n - 1)

n = int(input("Enter a Number: ")) 
result = fact(n)
print(f"Factorial of {n} is :{result}")

#-----------------------------------------------------------------------------------------

#  Write a program to display the first n terms of Fibonacci series. 
 # 0 1 1 2 3 5 8 13 21 34 55 89 144

def febo(n):
        a = 0
        b = 1
        count = 0
        if n <= 1 :
         print("Enter a Positive Number")
        elif n == 1:
            print("Fibonacci sequence upto",n,":")
            print(a)
        else:
         while count < n:
            print(a)
            c = a+b
            a = b
            b =c
            count = count +1
n = 5
febo(5)

#----------------------------------------------------------------------------------------

n=3
for a in range(2,ceil(n/2)+1):
    print(a)

print(f"This Number Can't be Expressed as Sum of two Prime Numbers") 

#----------------------------------------------------------------------------------------

## Lambda Function
x = lambda a,b,c : a+b+c
print(x(12,15,23))





