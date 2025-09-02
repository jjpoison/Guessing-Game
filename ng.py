import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Number Guessing")
print("Select a number between", lowest_num, "and", highest_num)

while is_running == True:
    guess = input("Enter your guess: ")

    if guess.isdigit():
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