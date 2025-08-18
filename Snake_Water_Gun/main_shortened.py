import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youdict = {"s" : 1, "w" : -1, "g" : 0}
reversedict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youdict[youstr]

# By know we have 2 numbers (variables), You and Computer

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")


if(computer == you):
    print("Its a draw")

# else:
#     if(computer == -1 and you == 1): (computer - you)= -2
#         print("You Win!")

#     elif(computer == -1 and you == 0): (computer - you) = -1
#         print("You Loss!")  

#     if(computer == 1 and you == -1): (computer - you) =  2
#         print("You Loss!")

#     elif(computer == 1 and you == 0): (computer - you) = 1
#         print("You Win!") 

#     if(computer == 0 and you == 1): (computer - you) = -1
#         print("You Loss!")

#     elif(computer == 0 and you == -1): (computer - you) = 1
#         print("You Win!")  

#     else:
#         print("Something went wrong!")      

# The below logic is written on the basis of the value of computer - you


if ((computer - you) == -1 or (computer - you) == 2):
    print("You Loss!")

else:
    print("You Win!")
