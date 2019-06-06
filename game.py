import random

print("Welcome to R-P-S-InClass")

user_choice=input("Select: Rock, Paper, Scissors: ")

#if user_choice in ["rock", "paper","scissors"]:
#print ("Selection:")
#else:
#    print ("fuck off")
options = ["Rock", "Paper", "Scissor"]

if user_choice not in options:
    print("")
    print ("Fuck Off")
else:
    print("")
    print ("Selection: ", user_choice)

Comp_choice = random.choice(options)
print("Comp_choice: ", Comp_choice)

if user_choice == Comp_choice:
    print ("Tie")
elif user_choice == "Rock" and Comp_choice == "Paper":
    print (user_choice)
elif user_choice == "Rock" and Comp_choice == "Scissor":
    print (Comp_choice)
elif user_choice == "Paper" and Comp_choice== "Rock":
    print (user_choice)
elif user_choice == "Paper" and Comp_choice == "Scissor":
    print (Comp_choice)
elif user_choice == "Scissor" and Comp_choice== "Paper":
    print (user_choice)
elif user_choice == "Scissor" and Comp_choice == "Rock":
    print (Comp_choice)