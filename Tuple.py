# -------------------------   Tuples  --------------------------- ##

## Round Brackets and comma        where Comma is mandatory

# 1. Tuples IS IMMUTABLE
# 2. Tuples IS ORDERED  
# 3. Tuples IS INDEXDED
# 4. Duplicate allowed 
# 5. Any Datatype Values

# ------------------------------------------------------------------------------------------------------------------

a =()                    ## Empty Tuple
print(type(a))   


a = 4,5,6,7,8,9,7,10,11,'Slice'     ### tuple without round brackets
print(type(a))
print(a)

# ---------------------------------------------------------------------------------------------------------------------------------------

atuple = (1,2,3,4.5,6.77,8.999,3,'R','Pink','Pink','Love',2,3)

print(atuple)

print(type(atuple))

print(atuple[len(atuple)-1])

b = atuple.index(8.999)
print(b)

b = atuple.index(2,2)                  # staring index = 2
print(b)

b = atuple.index('Pink')
print(b)

b = atuple.index('Pink',9,11)          # Starting Index = 9 and Stopping Index = 11
print(b)

# ----------------------------------------------------------------------------------------------------------------------------------------

atuple = (1,2,3,4.5,6.77,8.999,3,'R','Pink','Pink','Love',2,3,2,2,2,2,2,2,2,2)
c = atuple.count(2)
print(c)

# -----------------------------------------------------------------------------------------------------------------------------------------

atuple = (1,2,3,4.5,6.77,8.999,3,'R','Pink','Pink','Love',2,3,2,2,2,2,2,2,2,2)

print(atuple.index('R'))       #7

print(atuple.index('Pink'))    #8

print(atuple.index(2))       #1

print(atuple.index('2'))       #ValueError: tuple.index(x): x not in tuple

# -------------------------------------------------------------------------------------------------------------------------------------------

## Tuple Length

atuple = (1,2,3,4.5,6.77,8.999,3,'R','Pink','Pink','Love',2,3,2,2,2,2,2,2,2,2)

print(len(atuple))

# -------------------------------------------------------------------------------------------------------------------------------------------

atuple = (1,2,3,4.5,6.77,8.999,3,'R','Pink','Pink','Love',2,3,'Gold',4,'True',5,True,False,6.7,8.999)

print(atuple[1])              #2
print(atuple[-1])             #8.999
print(atuple[: :-1])          # Reverse Tuple
print(atuple[: : 3])          # skip 3 - 3 elements
print(atuple[ :7])            # elements till index 6
print(atuple[ 5:11])          # elements from index 5 till index 10
print(atuple[ :])             # print tuple

# -------------------------------------------------------------------------------------------------------------------------------------------

atuple = (1,2,3,4.5,6.77,8.999,3,'R','Pink','Pink','Love',2,3,'Gold',4,'True',5,True,False,6.7,8.999)

print ( 3 in atuple)       # true

if "Love" in atuple:
  print("Yes, 'Love' is in tuple")

# -------------------------------------------------------------------------------------------------------------------------------------------

atuple = (1,2,3,4.5,6.77,8.999,3,'R','Pink','Pink','Love',2,3,'Gold',4,'True',5,True,False,6.7,8.999)

atuple[2] = 122     ## TypeError: 'tuple' object does not support item assignment

print(atuple)      ### tuple is immutable 


# Tuples are unchangeable, so you cannot add or remove items from it

# We can add two tuples to makke a new tuple

a = (1,2,3,4,5)
b = (6,7,8,9,10)

atup = a+b
print(atup)

# -------------------------------------------------------------------------------------------------------------------------------------------


atuple = (1,2,3,4.5,6.77,8.999,3,'R','Pink','Pink','Love',2,3,'Gold',4,'True',5,True,False,6.7,8.999)

for x in atuple:
  print(x, end=" ")


i = 0
while i < len(atuple):
  print(atuple[i])
  i = i + 1
# -------------------------------------------------------------------------------------------------------------------------------------------
