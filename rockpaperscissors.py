import random

prompt = input("Choose rock, paper, or scissors (r,p,s): ")

choices = ["r", "p", "s"]
comp_choice = random.choice(choices)

if (prompt == comp_choice):
    answer = "It's a tie!"

elif ((prompt == "r" and comp_choice == "p") or (prompt == "p" and comp_choice == "s") or (prompt == "s" and comp_choice == "r")):
    answer = "You lose"

elif ((prompt == "p" and comp_choice == "r") or (prompt == "s" and comp_choice == "p") or (prompt == "r" and comp_choice == "s")):
    answer = "You win"

else:
    answer = "You entered an invalid character. Try again. "

print("You chose " + prompt)
print("The computer chose " + comp_choice)
print(answer)