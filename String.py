
# -------------------------    STRING --------------------------- ##

# 1. STRING IS IMMUTABLE
# 2. STRING IS ORDERED
# 3. STRING IS INDEXDED


a = 'welcome to Python World'
print(a)
print(type(a))
# -------------------------------------------------------------------------------------------------------------------
# print every elements of string
# every element in different line
for i in a:
    print(i)

#-------------------------------------------------------------------------------------------------------------------
## print every elements of string
# every element in single line
for i in a:
    print(i,end="")

for i in a:
    print(i,end=" ")
print()                    #### this print is used for printing in sperate line

for i in a:
    print(i,end="/")

#-------------------------------------------------------------------------------------------------------------------

zlist = []
print(type(zlist))

for i in a :
    zlist.append(i)

print(zlist)

## this list has a problem 
## list can contain dupplicate values 
#so if we want to store only unique values then we will use set
## because set dont allow duplicate values

zset=set()             ## we can not declare an empty set without set keyword
                       ## If we decare zset = {} like this then it will be considered as dictionary
for i in a :
    zset.add(i)
print(zset)

## but set is unordered and unindexed
# set elements are immutable but set is mutable
# because we cant not change values from a set but we can remove set elements
#-------------------------------------------------------------------------------------------------------------------

b = "good morning to everyone"

print(b)

## string is ordered & indexded 
## so we access any of charcter by their index number

print(b[2])  ## o
print(b[9])  ## i

## we can provide a range to print a perticuter
print(b[2:9])

print(b[0:9])

print(b[1:9:1]) # pike every nexxt element from string

print(b[1:9:2])  #pike every second element from string

print(b[:6])   ## starting from 0 index and till 6th index

print(b[::1]) ## starting from 0th index till last index pick every next element

print(b[: :2])  ## starting from 0th index till last index pick every second element

print(b[: :-1])  ## Reverse String Printing

#-------------------------------------------------------------------------------------------------------------------

c = b.capitalize()
print(b)                  ## String As it is
print(c)                  ## string's first character in capitalize form

# so we can say string is immutable that's why we saved this string's capitalizes form in a new variable

# -------------------------------------------------------------------------------------------------------------------

d = b.casefold()
print(b)
print(d)   ###casefold() method returns a string where all the characters are lower case.

# -------------------------------------------------------------------------------------------------------------------
e = b.count('e')
print(e)  ## Count() is a method which will return the count of a given charcter

print(b[10:20])
e = b.count('e',10,20) ##in Count()"e" is pattern which we want to search  #10 is starting index from where we will start
print(e)                  #20 is last index till we will search

# -------------------------------------------------------------------------------------------------------------------
f = b.endswith('e')  #Return True if given String ends with the given pattern, False otherwise. 
                  
print(f)   

f = b.endswith(('o','e','n'))  #Pattern can also be a tuple of strings to try.
print(f)  


f = b.endswith(('o','n'),10)  #Pattern can also be a tuple of strings to try.        ## 10 is starting index
print(f)  

# -------------------------------------------------------------------------------------------------------------------

g = b.find("e")  ## will return the first occurence of that char or element
print(g)

g = b.find("e",10,20) ## 10 starting Index ## 20 Last index
print(g)

# -------------------------------------------------------------------------------------------------------------------

h = b.index('r')   ## this will provide the index of given string or patteren
print(h)
#The index() method raises an exception if the value is not found. 
#The index() method is almost the same as the find() method,
#the only difference is that the find() method returns -1 if the value is not found.

h = b.find('k')
print(h)                 ###     -1        this is error when find method doest not find any match substring
#h = b.index('k')        ### ValueError:   substring not found

# -------------------------------------------------------------------------------------------------------------------

i = len(b)    ## this we provide the length of the string
print(i)

# -------------------------------------------------------------------------------------------------------------------

j = b.isdigit()   ##Check if all the characters in the text are digits:
print(j)          

j = b.isnumeric()  
print(j)

#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
#Exponents, like ² and ¾ are also considered to be numeric values.
#"-1" and "1.5" are NOT considered numeric values, because all the characters in the string
#must be numeric, and the - and the . are not.

p = '1.5'
print(p)
m = p.isnumeric
print(m)

m = p.isdigit()
print(m)


# -------------------------------------------------------------------------------------------------------------------

b = "GOOD MORNING TO EVERYONE"
k = b.lower()        ## Return a copy of the string converted to lowercase.
print(k)

b = 'good morning to everyone'
k = b.upper()       ##Return a copy of the string converted to uppercase.
print(k)

# -------------------------------------------------------------------------------------------------------------------

b = 'good morning to everyone'

# Search for the word "morning", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

k = b.partition("morning")       ##a tuple
print(k)


# -------------------------------------------------------------------------------------------------------------------

k = b.replace("morning","evening")   ##string.replace(oldvalue, newvalue, count)
# replace will replace old string will with new string value

print(k)

# -------------------------------------------------------------------------------------------------------------------

l = b.title()   ## title will return string where first charcter of every letter will be capital

print(l)

# -------------------------------------------------------------------------------------------------------------------

b = 'good morning to everyone'
# to check a pattern is available in string or not
print('good'in b)     #Flase
print('Good'in b)     ##True

print('afternoon' not in b)  #true


# -------------------------------------------------------------------------------------------------------------------

###  check count of every char of the string

l = "mujjiburrahman"

print('j' in l)
print(l.count('n'))

for i in l :
    print(f" count of {i} :{l.count(i)}")

x={}
for i in l :
    if i in x:
        x[i] = x[i]+1
    else:
        x[i] = 1
print(x)

# -------------------------------------------------------------------------------------------------------------------

h = "King of the kings"

for i in h :
    print(i)


#------------------------------------------------------------------------------------------------------------------

str = 'good morning'
a= len(str)
print(a)

for i in range(len(str)):
     print(f" Value of count of {str[i]} : {str.count(str[i])}")


abc = "cre34de90n1ce"
sum =0
for i in abc:
    if i.isnumeric() == True:
           i = int(i)
           sum = sum + i
print(sum)


# ------------------------------------------------------------------------------------------------------------------

# a = input("Enter a Value : ")
# b = input("Enter a Value : ")

# if a == b:
#    print("A is equal to B")
# else:
#     print( "A is not equal to B" )

# ------------------------------------------------------------------------------------------------------------------

a = "aryabhatta institute of mathematics"

print(a)
print(a[12])
print(a[11])
print(a[34]) 
print(a[-1])

print(len(a))

print(a[0:len(a)-1])
print(a[0:len(a)+1])
print(a[:11])
print(a[11:20])

print(a[:34:1])
print(a[0:34:2])
print(a[0:25:3])

print(a[ : :-1])

b = a.capitalize()
print(b)

c= a.upper()
print(c)

d=a.lower()
print(d)


print(
      "The Sum of two Variables:",
        int ( float(input ("Enter 1st Variable value:")))+
         int(input("Enter 2nd Variable value:"))
)

#-----------------------------------------------------------------------

print(
       "The Sum of two Variables:",
       eval(input ("Enter 1st Variable value:"))+
          int(input("Enter 2nd Variable value:"))
 )

#--------------------------------------------------------------------------

print(
       int(input("The value 1 is :"))+
        bool(input("The Value 2 is :"))                     #output of bool will be one always #True
)


#-----------------------------------------------------------------------------

print(
       int(input("The value 1 is :"))+
        bool(input("The Value 2 is :"))               #output of empty input bool will be Zero #False
)

#-----------------------------------------------------------------------------

print(
       int(input("The value 1 is :"))+
        float((input("The Value 2 is :")))                     #output of bool will be One always #True
)

#------------------------------------------------------------------------------

a= "welcome"

print(len(a))

print(a)                #welcome
print(a[0:7])           #welcome
print(a[:7])            #welcome
print(a[0:])            #welcome

print(a[0:7:1])         #welcome
print(a[0:7:2])         #wloe
print(a[0:7:3])         #wce
print(a[0:7:4])         #wo
print(a[::-1])            #emoclew

#------------------------------------------------------------------------------


str = 'good morning'
a= len(str)
print(a)

for i in range(len(str)):
     print(f" Value of count of {str[i]} : {str.count(str[i])}")

#------------------------------------------------------------------------------

