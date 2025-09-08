import json
import random
from pathlib import Path

print("\n««« Number Guessing »»»")

SCORES_FILE = Path(__file__).parent/ "highscores.json"
difficulties = ["easy", "medium", "hard", "extreme"]
### highscores = {"easy": [], "medium": [], "hard": [], "extreme": []}

# load highscores from file or create new if missing
if SCORES_FILE.exists():
    with open(SCORES_FILE, "r") as f:
        highscores = json.load(f)
    # make sure all difficulties exist
    for diff in difficulties:
        if diff not in highscores:
            highscores[diff] = []

else:
    highscores = {diff: [] for diff in difficulties}
    with open(SCORES_FILE, "w") as f:
        json.dump(highscores, f, indent=4)

### print(f"Highscore file is at: {SCORES_FILE.resolve()}")

def play_game():
    player_name = input("Enter your name: ").strip()
    if not player_name:
        player_name = "Anonymous"

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
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")  
            ### guess = int(guess)

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

                # add to leaderboard
                new_entry = {"name": player_name, "guesses": guesses}

                if not highscores[difficulty]:
                    highscores[difficulty].append(new_entry)
                    print("~ First highscore for", difficulty, "mode:", guesses, "guesses.")
                else:
                    highscores[difficulty].append(new_entry)            
                    # sort leaderboard (lowest guess = best)
                    highscores[difficulty] = sorted(highscores[difficulty], key=lambda x: x["guesses"])
                    # max top 10 people
                    highscores[difficulty] = highscores[difficulty][:10]

                # show result
                best = highscores[difficulty][0]
                if new_entry == best:
                    print("~ New highscore for", difficulty, "mode:", guesses, "guesses!")
                else:
                    print("~ Highscore for", difficulty, "is still", best["name"], "with", best["guesses"], "guesses.")

                # save highscores to json file
                with open(SCORES_FILE, "w") as f:
                    json.dump(highscores, f)
                
                break

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            is_running = False
            print("Okay. Thanks for playing!")
            break

def show_leaderboard():
    print("\n=== Leaderboard (Best Player Per Difficulty) ===")
    for diff in difficulties:
        if highscores[diff]:
            best = highscores[diff][0]
            print(f"{diff.title()}: {best["name"]} - {best["guesses"]} guesses")
        else:
            print(f"{diff.title()}: None")
    print("================================================")

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
        print("3. View Leaderboards")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_highscores()
        elif choice == "3":
            show_leaderboard()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main_menu()

# Edit difficulty selection
# Add "Erase Game Data" fuction