# Read a File

FilePath = 'C:\\Users\\SIKANDER\\RRR.txt'
content = open(FilePath)
y = content.read()
print(y)

#SyntaxError: invalid syntax

##-----------------------------------------------------------------------------------


FilePath = "K:\\T9\\Automation\\Python Practice\\RRR.txt"
content = open(FilePath)
y = content.read()
print(y)


##-----------------------------------------------------------------------------------

FilePath = "K:\\T9\\Automation\\Python Practice\\rrr.txt"
content = open(FilePath)
y = content.read()
print(y)

#File Name is not Case Sensetive


##-----------------------------------------------------------------------------------

FilePath = "D:\Element\\rrr.txt"
content = open(FilePath)
y = content.read()
print(y)

#we Can Read file from anywhere but path should be correct

##-----------------------------------------------------------------------------------

print(open("D:\Element\\rrr.txt").read())
try:
    FilePath = "D:\Element\\rrar.txt"
    content = open(FilePath)
    y = content.read()
    print(y)
except Exception as e:
    print(e)
    content.close()
    
# Name Error: name 'content, is not defined
# Here file name is wrong so how it can be closeed if it is not even openned 
# thats why it is showing NameError

# --------------------------------------------------------------------------------------

# to ignore this to happen (name error)we use Finally 
try:
    FilePath = "D:\Element\\rrr.txt"
    content = open(FilePath)
    y = content.read()
    print(y)
except Exception as e:
    print(e)
    content.close()
finally:
    try :
        print(open("D:\Element\\rrr.txt").read())
    except:
        print("No File Found")

    # Try -- Succesful    else -- Executed      Finally --- Executed
    # Try -- Failed    Except -- Executed      Finally --- Executed

##----------------------------------------------------------------------------------

## Second method of File Opening

try:
    FilePath = "D:\Element\\rrr.txt"
    with open(FilePath,'r') as Filevar:
        content = Filevar.readlines()
        print(content)
## by this with open (filepath) we can print file data in List Format
except Exception as e:
    print(e)
    content.close()
finally:
    try :
        print(open("D:\Element\\rrr.txt").read())
        ## tHis is printing excet same file content
    except:
        print("No File Found")

##--------------------------------------------------------------------------------------------

try:
    FilePath = "D:\Element\\rrr.txt"
    with open(FilePath,'w') as Filevar:
        content = Filevar.write("Jai ho Jai ho jai ho ")
        print(content)
except Exception as e:
    print(e)
    content.close()
    
    ## r = Read the file
    ## w - length of string which we are inserting
    
try:
    FilePath = "D:\Element\\rrr.txt"
    with open(FilePath,'a') as Filevar:
        content = Filevar.write("Jai ho Jai ho jai ho jai heeeeeeeee")
        print(content)
except Exception as e:
    print(e)
    content.close()
## a = a will also append the content in file