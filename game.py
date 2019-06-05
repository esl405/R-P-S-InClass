print("Welcome to R-P-S-InClass")

user_choice=input("Select: Rock, Paper, Scissors: ")

#if user_choice in ["rock", "paper","scissors"]:
#print ("Selection:")
#else:
#    print ("fuck off")
if user_choice not in ["rock","paper","scissor", "Rock", "Paper", "Scissor"]:
    print("")
    print ("Fuck Off")
else:
    print("")
    print ("Selection: ", user_choice)
