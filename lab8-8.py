import random
compThrow = random.randint(1, 3)
print("Start Game")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
# assuming no input validation
userThrow = int(input("What do you want to throw? "))
uChoice = " "
cChoice = " "
if userThrow == 1:
    uChoice = "Rock"
elif userThrow == 2:
    uChoice = "Paper"
else:
    uChoice = "Scissors"
if compThrow == 1:
    cChoice = "Rock"
elif compThrow == 2:
    cChoice = "Paper"
else:
    cChoice = "Scissors"
# Computer = rock, User = paper
if compThrow == 1 and userThrow == 2:
    print(f"Computer:{cChoice} vs You:{uChoice}")
    print("You win!")
# Computer = rock, User = scissors
elif compThrow == 1 and userThrow == 3:
    print(f"Computer:{cChoice} vs You:{uChoice}")
    print("You lose!")
# tie case
elif compThrow == userThrow:
    print(f"Computer:{cChoice} vs You:{uChoice}")
    print("It's a tie!")
# Comptuer = paper, User = rock
elif compThrow == 2 and userThrow == 1:
    print(f"Computer:{cChoice} vs You:{uChoice}")
    print("You lose!")
# Computer = paper, user = scissors
elif compThrow == 2 and userThrow == 3:
    print(f"Computer:{cChoice} vs You:{uChoice}")
    print("You win!")
# Computer = scissors, user = rock
elif compThrow == 3 and userThrow == 1:
    print(f"Computer:{cChoice} vs You:{uChoice}")
    print("You win!")
# Computer = scissors, user = paper
else:
    print(f"Computer:{cChoice} vs You:{uChoice}")
    print("You lose!")

