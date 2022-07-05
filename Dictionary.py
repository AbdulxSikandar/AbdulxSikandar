# -------------------------    DICTIONARY --------------------------- ##



# 1. Dictionary IS Key - Value Combination
# 1. Dictionary IS MUTABLE
# 2. Dictionary IS ORDERED
# 3. Dictionary IS INDEXDED
# 4. Key = Unique ( it caan not be duplicate)
#   value = Can be duplicate 
# 5. Any Datatype Values (string,tuple,int,float,bool,list) 

# ------------------------------------------------------------------------------------------------------------------
## Empty Dictionary
a = {}
print(type(a))     ##<class 'dict'>

a = { 1:12,2:23,3:78,4:54,5:46,6:455}
print(type(a))                           ## <class 'dict'>
print(a)                                 ## {1: 12, 2: 23, 3: 78, 4: 54, 5: 46, 6: 455}

# ------------------------------------------------------------------------------------------------------------------

aDict = { 
          'day1':'Mondaay',
          'List':[ 12,32.5,'Red',True],
          'tuple':( 12,3,5,6,12,45,78,2,45,6),
          'favcolor':'Black&white'
        }

print(aDict)
print(type(aDict))
print(aDict['List'])
print(aDict['favcolor'])


bDict ={ }
print(bDict)
print(type(bDict))

# ------------------------------------------------------------------------------------------------------------------

aDict = { 
          'day1':'Mondaay',
          'List':[ 12,32.5,'Red',True],
          'tuple':( 12,3,5,6,12,45,78,2,45,6),
          'favcolor':'Black&white'
        }

print(len(aDict))    ### 4  length = The Number of Keys available in Dictionary

# ------------------------------------------------------------------------------------------------------------------

aDict = { 
          'day1':'Mondaay',
          'List':[ 12,32.5,'Red',True],
          'tuple':( 12,3,5,6,12,45,78,2,45,6),
          'favcolor':'Black&white'
        }

a = { 1:12,2:23,3:78,4:54,5:46,6:455}

print(a[3])    ##78    ## index = Key in Dictionary

a = { 1:12,2:23,3:78,4:54,5:46,6:455}
a[2] = 1254                            ### mutable -  Value of 2nd key has changged by 1254
print(a)                      ##{1: 12, 2: 1254, 3: 78, 4: 54, 5: 46, 6: 455}

# ------------------------------------------------------------------------------------------------------------------

a = { 1:12,2:23,3:78,4:54,5:46,6:455}

print(a.items())  ###  a set-like object providing a view on D's items
## dict_items([(1, 12), (2, 23), (3, 78), (4, 54), (5, 46), (6, 455)])

print(a.keys())    ## a set-like object providing a view on D's keys
## dict_keys([1, 2, 3, 4, 5, 6])

print(a.values())  ### an object providing a view on D's values
## dict_values([12, 23, 78, 54, 46, 455])

print(a.get(2))   ## 23      value of key 2
print(a.get('2'))      ## None  

# Check if Key Exists

if 3 in a:                           ## we can check only for keys 
    print("Yes")

if 54 in a:                         ## Values can't be checked
    print("Yes")
else:
  print("No")

if 54 in a.values():                         ## Values be checked like this
    print("Yes")

# ------------------------------------------------------------------------------------------------------------------

# Update Dictionary 

a = { 1:12,2:23,3:78,4:54,5:46,6:455}

a.update({2 : "Shree"})
print(a)

## {1: 12, 2: 'Shree', 3: 78, 4: 54, 5: 46, 6: 455}

a[4] = 'Janam'
print(a)
## {1: 12, 2: 'Shree', 3: 78, 4: 'Janam', 5: 46, 6: 455}

a[7] = 'Anek'   # if key is available then it will update and if key is not available then it will create a key & value pair
print(a)
{1: 12, 2: 'Shree', 3: 78, 4: 'Janam', 5: 46, 6: 455, 7: 'Anek'}

a.update({8 : "kuch"})  # if key is available then it will update and if key is not available then it will create a key & value pair
print(a)


print(a[9])
## KeyError: 9   Because 9 is not a key

# ------------------------------------------------------------------------------------------------------------------

b = {1: 12, 2: 'Shree', 3: 78, 4: 'Janam', 5: 46, 6: 455, 7: 'Anek', 8: 'kuch'}

print(b.get(3))
print(b.get(7))

# ------------------------------------------------------------------------------------------------------------------

# pop() method removes the item with the specified key name

b = {1: 12, 2: 'Shree', 3: 78, 4: 'Janam', 5: 46, 6: 455, 7: 'Anek', 8: 'kuch'}

b.pop(3)
print(b)
## {1: 12, 2: 'Shree', 4: 'Janam', 5: 46, 6: 455, 7: 'Anek', 8: 'kuch'}
## pop removed the key and value from dictionary 

##popitem() method removes the last inserted item

b.popitem()
print(b)
### {1: 12, 2: 'Shree', 4: 'Janam', 5: 46, 6: 455, 7: 'Anek'}
## popitem() 


## del keyword can also delete the dictionary completely

c = {1: 12, 2: 'Shree', 4: 'Janam', 5: 46, 6: 455, 7: 'Anek'}
print(c)

del c
print(c)  ## NameError: name 'c' is not defined