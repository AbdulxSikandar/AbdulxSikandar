# -------------------------    List  --------------------------- ##

# 1. List IS MUTABLE
# 2. List IS ORDERED
# 3. List IS INDEXDED
# 4. Duplicate allowed
# 4. Any datatype value allowed



# -----List is mutable So we can replace any element by another one 

alist = [10,6,3,9,11,0]

alist[4]= 'Pink'

print (alist)

#---------------------------------------------------------------------------------------------------------------------- 

print (len(alist))

#---------------------------------------------------------------------------------------------------------------------- 
temp = alist.sort()

print (alist)

temp = alist.sort(reverse= True)

print (alist)

#---------------------------------------------------------------------------------------------------------------------- 
temp = alist.reverse()

print (alist)
#---------------------------------------------------------------------------------------------------------------------- 
temp = alist.remove(35)

print (alist)
#---------------------------------------------------------------------------------------------------------------------- 
temp = alist.append(15)

print (alist)

temp = alist.append(27)

print (alist)
#---------------------------------------------------------------------------------------------------------------------- 
temp = alist.insert(1,22)

print (alist)

temp = alist.insert(3,41)

print (alist)
#---------------------------------------------------------------------------------------------------------------------- 
temp = alist.remove(3)    ### Deleting given Value 

print (alist)

temp = alist.pop(1)    ### Deleting given Index Value 

print (alist)
print(temp)
#---------------------------------------------------------------------------------------------------------------------- 
temp = alist.insert(1,22)       ## Insert Value at 1st index 22

print (alist)

temp = alist.append(32)        ## Insert Value at last of list

print (alist)

temp = alist.sort()            ## arrange list in ascending order

print (alist)
#---------------------------------------------------------------------------------------------------------------------- 
print(alist[6])        ## ## Insert Value at last of list

print(alist[2:5])        ### List slicing

print(alist[2:5:2])

print(alist)


