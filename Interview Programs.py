# 1. Write a program to swap two numbers.

x = 10
y = 15

temp = x
x = y
y = temp

print(x)
print(y)

# 2. How to check number is prime or not.

n = int(input("Enter your Number : "))
def prime(n):
    for i in range(2,n):
        if n%i == 0:
            print("It is Not a Prime Number")
            break
        else:
            pass
    else:
        print("It's a prime Number")

prime(n)


# 3. How to find factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = 5
print(factorial(n))

# 4. Print Fibonacci series.

def febo(n):
    a = 0
    b = 1
    try:
       if n < 1:
           print("please provide a correct lenth for series")
       elif n == 1:
           print (a)
       elif n == 2:
           print(a,end=" ")
           print(b)
       elif n > 2 :
           print(a)
           for i in range (2,n+1):
                print(b)
                c = a+ b
                a = b
                b = c
    except Exception as e :
        print(e)

n = 12
febo(n)


# 5. How to find the sum of elements in an array?

alist = [10, 100, 150, 10000, 10, 120, 100, 1000, 10, 100, 150, 1000, 10]
print(sum(alist))

# 6. How to find maximum and minimum elements in an array?

alist = [10, 100, 150, 10000, 10, 120, 100, 1000, 10, 100, 150, 1000, 10]
print(max(alist))
print(min(alist))

# 7. How to find the length of the list?
alist = [10, 100, 150, 10000, 10, 120, 100, 1000, 10, 100, 150, 1000, 10]
print(len(alist))


# 8. How to swap first and last elements in the list
channels = ['netflix', 'hulu', 'disney+', 'appletv+']
## we want to swap netflix by appletv+

channels.insert(0,(channels[-1]))
channels.append(channels[1])
channels.pop(1)
channels.pop(-2)                   ### Pop delete elments by their index number
print(channels)


# 9. How to swap any two elements in the list?

channels = ['netflix', 'hulu', 'disney+', 'appletv+']

## lets suppose we want to swap disney+ by netflix
# first check for index number of both
disney_index = channels.index('disney+')
netflix_index = channels.index('netflix')

print(disney_index)
print(netflix_index)

## now we will insert netflix on disney index\
##and disney on netflix index

channels.insert(netflix_index,'disney+')

## we also remove the netflix from previous index
channels.remove('netflix')
channels.insert(disney_index,'netflix')

channels.pop(disney_index+1)

print(channels)


# 10. How to remove the Nth occurrence of a given word list?


def nth_occurence_element(alist,element,n):
    count = 0
    for i in range(0,len(alist)):
           if (alist[i] == element):
               count = count+1
               if (count == n):
                   del (alist[i])
                   return True
    return False

alist = [ 10, 100, 150, 10000, 10, 120, 100, 1000, 10, 100, 150, 1000, 10 ]
element = 150
n = 2
nth_occurence_element(alist,element,n)

print(alist)




# 11. How to search an element in the list ?

channels = ['netflix', 'hulu', 'disney+', 'appletv+']
my_fav = 'netflix'

if my_fav in channels:
    print(f"{my_fav} is found")
else:
    print(f"{my_fav} does not found")



# 12. How to clear the list?

alist = [10, 100, 150, 20, 10, 1000]
print(alist)
alist.clear()
print(alist)

alist = [1, 6, 5, 2, 10, 12]
print(alist)
del alist[:]
print(alist)



# 13. How to reverse a list?
alist = [10, 100, 150, 20, 10, 1000]
print(alist)
alist.reverse()
print(alist)



# 14. How to clone or copy a list?
alist = [10, 100, 150, 20, 10, 1000]
copy_list = alist
print(copy_list)


# 15. How to count occurrences of an element in a list?
alist = [10, 100, 150, 10000, 10, 120, 100, 1000, 10, 100, 150, 1000]
blist = []
for i in alist:
    if i not in blist:
        blist.append(i)
    else:
        continue
print(blist)
for i in blist:
    print(f" Count of {i} is : {alist.count(i)}")


# 16.Find the sum of the elements in list

alist = [10, 100, 1000, 10000]
print(sum(alist))


# 17. How to multiply all the numbers in the list?

alist = [12, 15, 21, 23, 18, 4, 27]
print(alist)
r = 1
for i in alist:
    r = r*i
print(r)


# 18. How to find the smallest and largest numbers on the list?

alist = [12, 15, 21, 23, 18, 4, 27]
print(max(alist))
print(min(alist))

print(sorted(alist))    # Sorted will rearrange list in asc order temporarily
print(alist)

# 19. How to find the second Max number in a list?

alist = [12, 15, 21, 23, 18, 4, 27]

# Max value from list
print(alist)
a = max(alist)
print(a)

# Second max value from list
b = alist.remove(max(alist))
print(alist)
secondMax = max(alist)
print(secondMax)
f = alist.sort()
print(alist)

# Max value from list
print(alist[len(alist)-1])

# 2nd Max value from list
print(alist[len(alist)-2])


# 20. How to check string is palindrome or not?

string = 'cake'

def palindrome(string):

    if string == string[::-1]:
        return print(f"{string} : It's a palindrome string")
    else:
        return print(f"{string} : It's not a palindrome string")

palindrome(string)

string = 'kanak'
palindrome(string)


# 21. How to reverse words in a string ?
a = 'welcome'
b = a[::-1]
print(b)


# 22. How to find a substring in a string?

b = a.find('co')
print(b)
#

f = 'wel'
if f in a:
    print('Yes')
else:
    print('no')


st = "How to find a substring in a string"
r = 'ring'
if r in st:
    print('Yes')
    print(a.find(r))
else:
    print('no')


# 23. How to find the length of a string?
a = 'welcome'
print(len(a))


# 24. How to check if the string contains any special character?
a = 'wel@c7o$me*gh0jk=wr-il^jk!k'
for i in a:
    if i.isalpha() or i.isdigit():
        pass
    else:
        print(i)

# 25. Check for URL in a string
