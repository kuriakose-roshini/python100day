import random

def f_easy():
    print("You've 10 attempts")
    i = 10
    while i != 0:
        guess = int(input("Make a guess:"))
        i = i - 1
        if num < guess:
            print("Too high")
        elif num > guess:
            print("Too low")
        else:
            print(f"You got it. The answer was{num}")

def f_diff():
    print("You've 5 attempts")
    i = 5
    while i != 0:
        guess = int(input("Make a guess:"))
        i = i - 1
        if num < guess:
            print("Too high")
        elif num > guess:
            print("Too low")
        else:
            print(f"You got it. The answer was{num}")

print("Welcome to the Guessing game!\n I'm thinking of a number between 1 & 100")
num = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type easy or hard:")
if difficulty == 'easy':
    f_easy()
else:
    f_diff()
