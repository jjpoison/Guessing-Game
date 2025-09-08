import json
import random
from pathlib import Path

print("\n««« Number Guessing »»»")

# load highscores from file or create new if missing
SCORES_FILE = Path(__file__).parent/ "highscores.json"

if SCORES_FILE.exists():
    with open(SCORES_FILE, "r") as f:
        highscores = json.load(f)
else:
    highscores = {"easy": None, "medium": None, "hard": None, "extreme": None}
    with open(SCORES_FILE, "w") as f:
        json.dump(highscores, f, indent=4)

# print(f"Highscore file is at: {SCORES_FILE.resolve()}")

def play_game():
    is_running = True
    while is_running:
        lowest_num = 1
        difficulty = input("Select the dificulty (easy/medium/hard/extreme): ").lower()
        if difficulty == "easy":
            highest_num = 10
        elif difficulty == "medium":
            highest_num = 50
        elif difficulty == "hard":
            highest_num = 100
        elif difficulty == "extreme":
            highest_num = 1000
        else:
            print("Invalid input. Defaulting to easy.")
            difficulty = "easy"
            highest_num = 10

        answer = random.randint(lowest_num, highest_num)
        guesses = 0

        print(" >>> Select a number between", lowest_num, "and", highest_num)

        while True:
            guess = int(input("Enter your guess: "))    
            # guess = int(guess)
            guesses += 1

            if guess < lowest_num or guess > highest_num:
                print("Your guess is beyond the preset range")
                print("Please select a number between", lowest_num, "and", highest_num)
            elif guess < answer:
                print("Too low! Try again.")
            elif guess > answer:
                print("Too high! Try again.")
            else: # correct answer
                print("You got it! The answer was", answer)
                print("~ You guessed", guesses, "times.")

                # highscore updater
                if highscores[difficulty] is None: # no highscore yet
                    highscores[difficulty] = guesses
                    print("~ First highscore for", difficulty, "mode:", guesses, "guesses.")
                elif guesses < highscores[difficulty]: # beat the highscore
                    highscores[difficulty] = guesses
                    print("~ New highscore for", difficulty, "mode:", guesses, "guesses!")
                else:
                    print("~ Highscore for", difficulty, "is still", highscores[difficulty], "guesses.")

                # save highscores to json file
                with open(SCORES_FILE, "w") as f:
                    json.dump(highscores, f)
                
                break

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            is_running = False
            print("Okay. Thanks for playing!")
            break

def show_highscores():
    print("\n=== Highscores ===")
    for diff in ["easy", "medium", "hard", "extreme"]:
        score = highscores[diff]
        if score is None:
            print(f"{diff.title()}: None")
        else:
            print(f"{diff.title()}: {score} guesses")
    print("\n================")

def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Play Game")
        print("2. View Highscores")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_highscores()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main_menu()

# Leaderboards