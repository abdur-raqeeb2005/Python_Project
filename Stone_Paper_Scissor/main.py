import random

'''
1 is Stone
-1 is Paper
0 is Scissor
'''

computer = random.choice([1,-1,0])
player = input("Enter your choice: ")
playerdict = {"st": 1, "p": -1, "sc": 0}
choice = {1 : "Stone", -1 : "Paper", 0 : "Scissor"}

you = playerdict[player]

print(f"Your Chose {choice[you]}\nComputer Chose {choice[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == 1 and you == -1):
        print("You Win!")
    elif(computer == 1 and you == 0):
        print("You Lose!")
    elif(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 0 and you == -1):
        print("You Lose!")
    elif(computer == 0 and you == 1):
        print("You Win!")

    else:
        print("Something went wrong!")

        
    

