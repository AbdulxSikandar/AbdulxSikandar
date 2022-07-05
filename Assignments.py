# Write program to find sum or addition of the numbers in below string:-
# abc = "cre34de90n1ce"


abc = "cre34de90n1ce"
sum =0
for i in abc:
    if i.isnumeric() == True:
           i = int(i)
           sum = sum + i
print(sum)

#------------------------------------------------------------------------------------------------------------------

str = 'cre34de90n1ce is the best place to learn'
a= len(str)
for i in range(len(str)):
     print(f" Value of count of {str[i]} : {str.count(str[i])}")


abc = "cre34de90n1ce"
x = {}
for y in abc:
    if y in x:  
            x[y]= x[y]+1
    else:
        x[y] = 1
print(f"Ouccrence of char : {x}")

#-----------------------------------------------------------------------------------------------------------------

#  Read all values from excel

import pandas as pd

file = 'sampledata.xlsx'

# df = pd.read_excel(file)
# print(df)
#---------------------------------------------------------------------------------------------------------------------

import openpyxl

file = "sampledata.xlsx"

worksheet = openpyxl.load_workbook(file)