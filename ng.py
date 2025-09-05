print("Number Guessing")
lowest_num = 1
dificulty = input("Select the dificulty (e/m/h): ")
if dificulty == "e":
    highest_num = 10
elif dificulty == "m":
    highest_num = 50
elif dificulty == "h":
    highest_num = 100
else:
    print("Invalid input.")
    print("Please select the dificulty (e/m/h): ")

import random

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Select a number between", lowest_num, "and", highest_num)

while is_running == True:
    guess = int(input("Enter your guess: "))
    
    guess = int(guess)
    guesses += 1

    if guess < lowest_num or guess > highest_num:
        print("Your guess is beyond the preset range")
        print("Please select a number between", lowest_num, "and", highest_num)
    elif guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print("You got it! The answer was", answer)
        print("You guessed", guesses, "times.")
        is_running == False
else:
    print("Invalid input")
    print("Please select a number between", lowest_num, "and", highest_num)