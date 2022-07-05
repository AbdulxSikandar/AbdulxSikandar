
# -------------------------    SET --------------------------- ##



# 1. Set IS Unindexed
# 2. Set items are unchangeable, but you can remove items and add new items.      Set - mutable // set items - immutable
# 3. Set IS UnORDERED
# 4. doesn't accept duplicate 
# 5. Any Datatype Values (string,tuple,int,float,bool,list) 

# ------------------------------------------------------------------------------------------------------------------

# Empty Set

aSet = {}
print(type(aSet))    ## <class 'dict'>

aSet = set()
print(type(aSet))    ##<class 'set'>

# ------------------------------------------------------------------------------------------------------------------

aSet = {'Red','Green','Black'}

print(aSet)

#{1:'King',2:'Queen',3:'commander',4:'army'}
#['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

for i in aSet:
    print(i)

if 'Yellow' in aSet:
    print("Yes,It is there")
else:
    print("No! Try Again")

# ------------------------------------------------------------------------------------------------------------------

aSet = {'Red','Green','Black'}

aSet.add('Black')
aSet.add('Yellow')
aSet.add('Pink')
aSet.add('Gray')
aSet.add('Purple')
aSet.add('Orange')
aSet.add('White')

print(aSet)

# ------------------------------------------------------------------------------------------------------------------

z = {'Gray', 'Green', 'Red', 'Pink', 'Purple', 'White', 'Orange', 'Black', 'Yellow'}

z.update('Brown')   ## it will update every letter seprately in set
print(z)

x = ('Peace','War','Love')  #for itration update prepare a list or tuple then it will add elements in iteration
z.update(x)
print(z)

# ------------------------------------------------------------------------------------------------------------------

z = {'Gray', 'Green', 'Red', 'Pink', 'Purple', 'White', 'Orange', 'Black', 'Yellow'}
z.remove('Black')
z.remove('Yellow')
# If the item to remove does not exist, remove() will raise an error.
# we can use discard # it will not give any error if element is not available in set
z.discard('Brown')
print(z)
## {'Red', 'Green', 'Pink', 'Purple', 'Gray', 'White', 'Orange'}

x = z.pop()   ## pop remove random elements and provide the value of removed element 
print(x)
print(z)

x = z.pop()
print(x)
print(z)

x = z.pop()
print(x)
print(z)
# ------------------------------------------------------------------------------------------------------------------

p = {'Gray', 'Green', 'Pink', 'Red', 'White', 'Purple'}

p.clear()   ## remove all the elements
print(p)

del p      ## Delete the structure and all elements
print(p)   ## NameError: name 'p' is not defined  

# ------------------------------------------------------------------------------------------------------------------

p = {'Gray', 'Green', 'Pink', 'Red', 'White', 'Purple'}
x = ('Peace','War','Love')

v = p.union(x)
print(v)
## {'Peace', 'Pink', 'War', 'Gray', 'Red', 'Love', 'Green', 'White', 'Purple'}