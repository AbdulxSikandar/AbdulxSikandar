# 1 Write a program to display the first 10 natural numbers.

i =0
while i < 10:
    print(i)
    i = i+1

i =1
while i <= 10:
    print(i,end=" ")
    i = i+1

#-------------------------------------------------------------------------

# 2 Write a program to find the sum of first 10 natural number

# Manual way
print("Sum of first 10 Natural Numbers:",0+1+2+3+4+5+6+7+8+9+10)

# #loop method 
n = int(input("Enter a Number: "))
sum = 0
for i in range(1,n+1):
     sum =sum +i
print(f"The sum of first {n} Natural Numbers is:{sum}")


# Formula Base Method

n = int(input("How many Numbers you want to add : "))
a = n*(n+1)/2
print(f"The sum of first {n} Natural Numbers is:{a}")

# ----------------------------------------------------------------------------         

#3  Print item in the list is greater than 15  

list1 = [12,34,54,33,45,78,23]                                                                                                                                                                                                                                                                                        
for item in list1:  
    if item > 15 :
      print(item)

#----------------------------------------------------------------------------

# 4  Write a program to display n terms of natural number and their sum

#While loop
n =int(input("Enter a Value:"))
sum =0
i = 1
while i <= n :
    sum = sum +i
    i = i+1
print(f"The Sum of {n} Natural Numbers is : {sum}")

#For loop
n = int(input("Enter a number:"))
sum =0
for i in range (1,n+1):
   print (i)
   sum = sum +i
print(f"The sum of {n} Natural Numbers is:{sum}")

#------------------------------------------------------------------------------

# 5  #Write a program to display first n even numbers

n = int(input("Enter a number:"))
if n == 0 :
    print("Please Provide a Valid Number")
elif n <0 :
    print("Please Provide a Positive Number")
else: 
 for i in range (1,2*n+1):
    if i %2 == 0:
        print(i)
    else:
        pass


## -----------------------------------------------------------------------------

# 6    Write a program to display first n odd numbers

n = int(input("Enter a number:"))
if n == 0 :
    print("Please Provide a Valid Number")
elif n <0 :
    print("Please Provide a Positive Number")
else: 
 for i in range (1,2*n+1):
    if i %2 != 0:
        print(i)
    else:
        pass

#------------------------------------------------------------------------------------

# 7     Write a program to display triangle shape n of natural number 

n = int(input("Enter a number:"))
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print() 

# -----------------------------------------------------------------------------------

8     #Write a program to display n terms of natural number and their sum

n = int(input("Enter a number:"))
sum =0
for i in range (1,n+1):
    for j in range(1,i+1):
      pass  
    print(j,end=' ')
    sum = sum +i 
    if i == n :
     print(f"The sum ={sum}")


#------------------------------------------------------------------------------------

# 9   Write a program to display triangle shape of n *

n = int(input("Enter a number:"))
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

#------------------------------------------------------------------------------------

# 10  Write a program to read n numbers from keyboard and find their sum and average

list = []
i =0
n = int(input("How many digits you want to enter : "))
while i < n:
    m = int(input("Give a Random Number (0 to 50): "))
    if m >50 :
      print("Please ReEnter")
    elif m < 0:
      print("Please Give a Positive Number")
    else:   
        list.append(m)
        i = i+1 
print(list)   
print(f"Sum of Given Numbers is:{sum(list)}")
print(f"Maximum Number is:{max(list)}")
print(f"Minimum Number is: {min(list)}")
print(f"Average :{sum(list)/len(list)}")

# ------------------------------------------------------------------------------

# 11  Write a program to read n numbers from keyboard and find their sum and average

list = []
i =0
n = int(input("How many digits you want to enter : "))
while i < n:
    m = input("Give a Random Number : ")
    e =''
    if m == e :
       break
    else:
       m = int(float(m))
       i = i+1 
    list.append(m)
print(list)   
print(f"Sum of Given Numbers is:{sum(list)}")
print(f"Maximum Number is:{max(list)}")
print(f"Minimum Number is: {min(list)}")
print(f"Average :{sum(list)/len(list)}")

#-------------------------------------------------------------------

# 12  Write a program to display the cube of the number upto given an integer

a = float(input("Enter Your Number to calculate Cube: "))
b = print(a*a*a )

#----------------------------------------------------------------------

# 13    Write a program to display the multiplication table vertically from 1 to n.

b = int(input("Please Enter a Number: "))
for a in range(1,11):
    print(f"{b} x {a} = {a*b}")


# Write a program to display the multiplication table Horizentally from 1 to n.

b = int(input("Please Enter a Number: "))
for a in range(1,11):
    for j in range(1,2):
          print(a*b,end=" ")


#--------------------------------------------------------------------------------------------


# 14   Write a program display the n terms of odd natural number and their sum 

sumofodds = 0
n = int(input("Please Enter a Number: "))
for a in range(1,2*n):
        if a % 2 != 0 :
                print(a)
                sumofodds = sumofodds+a
        else:
                pass
print(f"Sum of odd Numbers:{sumofodds}")           
            
             
#--------------------------------------------------------------------------------------------

# 15  Write a program to display Exam passing marks and minimum marks condition

a = int(input("Enter Marks of English:"))

b = int(input("Enter Marks of Hindi:"))

c = int(input("Enter Marks of Sanskrit:"))

d = a+b+c
print(d)

if d > 120 and (a and b and c )>33:
    print("Congarts ! You Have Cleared the Exam")
else:
    print("Sorry! You are not up to the marks")
    
             
#--------------------------------------------------------------------------------------------

# 16   rite a program to display the pattern like right angle triangle using an asterisk.

n = int(input("Enter Number of lines: ")) 
for i in range(0,n):
        for j in range(0,i+1):
           print('* ',end="")
        print("\r")


#----------------------------------------------------------------------------------------------

#  17  Write a program to display the pattern like right angle triangle with a number

n = int(input("Enter Number of lines: ")) 
for i in range(1,n+1):
        for j in range(1,i+1):
           print(j,end=" ")
        print()

n = int(input("Enter Number of lines: ")) 
for i in range(1,n+1):
        for j in range(1,i+1):
           print(i,end=" ")
        print()

#-----------------------------------------------------------------------------------------------

# 18  Write a program to make such a pattern like right angle triangle with number increased by 1.

n = int(input("Enter Number of lines: "))
a=1
for i in range(1,n+1):
        for j in range(1,i+1):
           print(a,end=" ")
           a= a+1
        print()

#--------------------------------------------------------------------------------------------------

# 19  Write a program to make such a pattern like a pyramid with an asterisk

n = int(input("Give a Number : "))
m = n - 1
for i in range (0,n):
    for j in range(0,m):
        print(end =" ")
    m = m - 1
    for j in range (0,i+1):
         print("* ",end="")
    print()



n = int(input("Give a Number : "))
for i in range (0,n):
   for j in range(0,n-i-1):
       print(end=" ")
   for j in range (0,i):
       print("*",end=" ")
   print()

#---------------------------------------------------------------------------------------------------

# 20  Write a program to calculate the factorial of a given number

n = int(input("Enter a Number: ")) 
a=1
if n == 0 or n == 1:
    print(f"Factorial of {n} is :1")
elif n < 0:
    print(f"Factorial of Negative Numbers is Undefined")
else:
 for i in range (1,n+1):
    a = a*i
 print(f"Factorial of {n} is :{a}")



def fact(n):
    if n == 1:
        return n
    else: 
      return  n * fact(n - 1)

n = int(input("Enter a Number: ")) 
result = fact(n)
print(f"Factorial of {n} is :{result}")

#---------------------------------------------------------------------------------------------------

# 21   Write a program to display the sum of the series [ 9 + 99 + 999 + 9999 ...].

n = int(input("How many Steps do you want to add: "))
list=[]
for i in range (1,n+1):
     power = pow(10,i)         ## pow() Power Function           ## power = 10**i   Power operator
     list.append(power- 1)
print(list)
print(f"The Sum of Numbers is:{sum(list)}")
    


n = int(input("How many Steps do you want to add: "))
list=[]
for i in range(1,n+1):
  list.append(int('9'*i))
print(list)
print(f"The Sum of Numbers is:{sum(list)}")


# ----------------------------------------------------------------------------------------------------------

# 22    Write a program to find the sum of the series 1 +11 + 111 + 1111 + .. n terms.

#1

n = int(input("How many Steps do you want to add: "))
list=[]
for i in range(1,n+1):
 list.append(int('1'*i))
print(list)
print(f"The Sum of Numbers is:{sum(list)}")

#2 

n = int(input("How many Steps do you want to add: "))
sum = 0
j = 1
for i in range(1,n+1):
        sum = sum + j
        j = (j * 10) + 1
print(f"The Sum of Numbers is:{sum}")

#3

n = int(input("How many Steps do you want to add: "))
sum = int((pow(10, n + 1) -10 - (9 * n)) / 81)
print(f"The Sum of Numbers is:{sum}")

#4

n = int(input("How many Steps do you want to add: "))
def recSum(n):
    if n<=0:
        return 0
    else:
        return (n + 10 * recSum(n-1))
series_sum = recSum(n)
print("\nSum of series is: ", series_sum)



# ----------------------------------------------------------------------------------------------------------

# 23  Find sum of the series 1+22+333+4444+…… upto n terms

def solve_sum(n): 

    return (pow(10, n + 1)*(9 * n - 1)+10)/pow(9, 3)-n*(n + 1)/18
 
n = 3
print(int(solve_sum(n)))

# ----------------------------------------------------------------------------------------------------------

# 24   Write a program to display the pattern like a diamond   

n=6

for i in range(n):
       print(" "*(n-i-1)+"* "*(i+1))
for j in range(n-1,0,-1):
       print(" "*(n-j)+"* "*(j))


# ----------------------------------------------------------------------------------------------------------

# 25  Write a program to print the Floyd's Triangle.


# 1
# 2	3
# 4	5 6
# 7	8 9	10
# 11 12	13 14 15


n=int(input("Number of Rows: "))
count = 1
for i in range(1,n+1):
    for j in range(1,i+1):
         print(count,end=" ") 
         count = count+ 1
    print()


# ----------------------------------------------------------------------------------------------------------

# 26  Write a program to display Pascal's triangle
#                  1
#               1     1
#             1    2     1 
#          1    3     3     1
#        1    4    6     4     1
#      1    5   10    10    5     1

a ={ 
    1:1,2:'l',3:'p'
}
print(a)
a['pw']=12
print(a.get(2))
print(a.keys())
print(a.items())
for i in a:
  print(i)
print(type(a))


# ----------------------------------------------------------------------------------------------------------

# 27  Write a program to check whether a given number is a perfect number or not. 

def perfect_number(n) :
     sum = 0
     for i in range (1,n):
          if n%i == 0:
               sum = sum + i
          else :
               pass
     if sum == n:
        return print(f"{n} is a perfect number")
     else:
        return print(f"{n} is not a perfect number")

n= int(input("Please enter a number to check it is perfect or not: "))

perfect_number(n)

# ----------------------------------------------------------------------------------------------------------

# 28  Write a program to check whether a given number is an armstrong number or not.

def armstrong_num(n):
    import math
    sum = 0
    strng = str(n)
    power = len(strng)
    for i in range (power):
        i = int(i)
        sum = sum + pow(int(strng[i]),power)

    if sum == n :
        return print("It's an Armstrong Number")
    else:
        return print("It's not an Armstrong Number")


n = 8208
armstrong_num(n)

## Armstrong Number : 153/370/371/407/1634/8208
# ----------------------------------------------------------------------------------------------------------

# 29  Write a program to display the first n terms of Fibonacci series. 
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

# ----------------------------------------------------------------------------------------------------------

# 30  Write a program to display the number in reverse order
  

def reverse(A):
    a = str(A)
    A = a[ : :-1]
    A = int(A)
    return print(A)

A = 78965421
reverse(A)


num = 65421
print(int(str(num)[ : :-1]))

# ----------------------------------------------------------------------------------------------------------


# 31  Write a program to find the number and sum of all integer between 100 and 200 which are divisible by 9.

sum = 0
for num in range(100,200):
            if num % 9 ==0:
              print(num,end=" ")
              sum = sum + num 
print()             
print(f"Sum of all numbers which are divisible by 9 between 100 and 200 :{sum}")

# ----------------------------------------------------------------------------------------------------------


# 32  Write a program to find HCF (Highest Common Factor) of two numbers

a = int(input("a = "))
b = int(input("b = "))
if a > b:
        r = (a%b)
        while r !=0 :
         x= int(a/b)
         a = b*x + r
         a = b;b = r
         r =(a%b)
         if r == 0:
             break
         else:
             pass
        print(f"This is hcf: {b}")
else:
       r = (b%a)
       while r !=0 :
         y= int(b/a)
         b = a*y + r
         b = a; a = r
         r =(b%a)
         if r == 0:
             break
         else:
             pass
       print(f"This is hcf: {a}")

# ----------------------------------------------------------------------------------------------------------

# 33  Write a program to find LCM of any two numbers using HCF

a = int(input("a = "))
b = int(input("b = "))

def hcf(a,b):
 if a > b:
        r = (a%b)
        while r !=0 :
         x= int(a/b)
         a = b*x + r
         a = b;b = r
         r =(a%b)
         if r == 0:
             break
         else:
             pass
        hcf = b
 else:
       r = (b%a)
       while r !=0 :
         y= int(b/a)
         b = a*y + r
         b = a; a = r
         r =(b%a)
         if r == 0:
             break
         else:
             pass
       hcf = a
 return hcf
h = hcf(a,b)
print(h)
def lcm(a,b):
    l = (a*b)/hcf(a,b)
    return l
print(int(lcm(a,b))) 
# ----------------------------------------------------------------------------------------------------------

# 34  Write a program to find LCM of any two numbers

# Python Program to find the L.C.M. of two input number

def lcm(a, b):
   if a > b:
       greater = a
   else:
       greater = b

   while(True):
       if((greater % a == 0) and (greater % b == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
a = int(input("a = "))
b = int(input("b = "))

print("The L.C.M. is", lcm(a, b))



# ----------------------------------------------------------------------------------------------------------

# 35  Write a program to Check Whether a Number can be Express as Sum of Two Prime Numbers.

from math import ceil

n=n=int(input("Give me a Number : "))
for a in range(2,ceil(n/2)+1): 
     for i in range(2,a+1):
                if a%i != 0 :
                  pass
                elif a%i ==0 and i<a :
                    break
                elif True :
                      for b in range(2,n):
                        if a + b ==n :
                            for j in range(2,b+1):
                              if b%j != 0 :
                                pass
                              elif b%j ==0 and j<b :
                                break
                              elif b%j ==0:
                                 print(f"This is the Pair of Prime Numbers : {a} + {b} = {n}") 
                              else:
                                 pass
                        else:
                            pass  
                else:
                    print(f"Provide a New Number")
   


# ----------------------------------------------------------------------------------------------------------

#36 Write a program to check the Given Number is the prime numbers or Not

n=int(input("Check this Number: "))
for i in range(2,n):
    if n%i == 0  :
        print(f"{n} is Not a Prime Number")
        break
    else:
        pass
else :
        print(f"{n} is a Prime Number")


# ----------------------------------------------------------------------------------------------------------

# 37 Write a program to find the prime numbers within a range of numbers

a = int(input("Starting Point: "))
b = int(input("Ending Point: "))
list=[]
for i in range(a,b+1):
    for j in range(2,i+1):
        if i%j != 0 :
               continue
        elif i%j == 0 and j<i :
                break
        else :
                list.append(i)
print(f"Prime Numbers between {a} and {b} : {list}")
