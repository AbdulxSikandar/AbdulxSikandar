
### Snake Water Gun Game

import random

Your_points = 0
Computers_points = 0

print( ''' "Welcome to The Game"
  "Snake - Water - Gun" ''')

for a in range(1,6):
   print("Round =", a)
   Userinput = int(input("Enter your Choice: "))
   i =0
   while i < 10:
    if Userinput >3:
        print("Please enter a Number between 1 to 3")
        Userinput = int(input("Enter your Choice: "))
    elif Userinput < 1:
        print("Please enter a Number between 1 to 3")
        Userinput = int(input("Enter your Choice: "))
    else: 
        if Userinput == 1 :
            print(f"Your Choice is : Water")
            break
        elif Userinput == 2 :
            print(f"Your Choice is : Gun")
            break
        elif Userinput == 3 :
            print(f"Your Choice is : Snake")
            break
   compinput = random.randint(1,3)
   print(f"Computer's Choice : {compinput}")

   if compinput == 1 :
    print(f"Choice of computer is : Water")
   elif compinput == 2 :
     print(f"Choice of computer is : Gun")
   elif compinput == 3 :
     print(f"Choice of computer is : Snake")




   if Userinput == compinput :
    print(f"Both Choose the Same ; So match Tie")
    Your_points = Your_points + 0
    Computers_points = Computers_points + 0
   elif Userinput == 1 and compinput == 2 :
    print(f"You won the Match")
    Your_points = Your_points + 1
    Computers_points = Computers_points + 0
   elif Userinput == 1 and compinput == 3 :
    print(f"You won the Match")
    Your_points = Your_points + 1
    Computers_points = Computers_points + 0
   elif Userinput == 2 and compinput == 3 :
    print(f"You won the Match")
    Your_points = Your_points + 1
    Computers_points = Computers_points + 0
   elif Userinput == 2 and compinput == 1 :
    print(f"Your Opponent won the Match")
    Your_points = Your_points + 0
    Computers_points = Computers_points + 1
   elif Userinput == 3 and compinput == 1 :
    print(f"Your Opponent won the Match")
    Your_points = Your_points + 0
    Computers_points = Computers_points + 1
   elif Userinput == 3 and compinput == 2 :
    print(f"Your Opponent won the Match")
    Your_points = Your_points + 0
    Computers_points = Computers_points + 1 
   print("-------------------------------------------------------")

print("Your_points :",Your_points)
print("Computers_points :",Computers_points)

if Your_points > Computers_points :
    print(''' Congratatulations!!!!! 
             "You Have Won the Tournament" ''')
elif Your_points < Computers_points :
    print(''' Sorry!!!!! 
             "You loss the Tournament" ''')
else:
    print(''' Well Played!!!!! 
             "You tie the Tournament" ''')