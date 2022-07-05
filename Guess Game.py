import random

print('''     "Welcome to Guessing Game"
   Please choose a Range to play''')

Round = 1
a = int(input(f"Start from here: "))
b = int(input(f"End here: "))
if a==b:
   while a==b:
    print(f"Please choose a correct Range")
    a = int(input(f"Start from here: "))
    b = int(input(f"End here: "))
else:
    pass
for i in range(b):
 print("_ "*10)
 print(f"Round Number :{Round}")
 print("_ "*10)
 n = int(input("Your Number is: "))
 if n > b:
      while n >b:
       print("You Choose a number which is out of your range")
       n = int(input("Please choose Your Number again : "))
 comp_choice = random.randint(a,b)
 print(f"Opponent's Choice is :{comp_choice}")
 if n == comp_choice:
   print("Congratulations!!!! You Guess the Right")
   break
 elif n > comp_choice:
   print("Opps!! You Guess higher than opponent")
   pass
 else:
   print("Opps!! You Guess lower than opponent")
   pass
 if Round == b or n == comp_choice :
     print(f"Total Number of Rounds : {Round}")
 Round = Round+1



### Some Random Function

# print(random.randrange(2, 20, 2))
# print(random.randrange(100, 1000, 3))
# print(random.randrange(-50, -5))
# print(random.sample(range(0, 1000), 10))
