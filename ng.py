import os
import msvcrt
import json
import random
from pathlib import Path

print("\n««« Number Guessing »»»")

SCORES_FILE = Path(__file__).parent / "highscores.json"
difficulties = ["easy", "medium", "hard", "extreme", "custom"]

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
    #with open(SCORES_FILE, "w") as f:
    #    json.dump(highscores, f, indent=4)

def choose_custom_range():
    while True:
        try:
            max_num = int(input("Enter the highest number (minimum 2): "))
            if max_num < 2:
                print("The highest number must be at least 2.")
                continue
            return "custom", max_num
        except ValueError:
            print("Please enter a valid number.")

def choose_difficulty():
    while True:
        os.system("cls")
        print("Select the difficulty (1-4):\n")
        print("1. Easy (1-10)")
        print("2. Medium (1-50)")
        print("3. Hard (1-100)")
        print("4. Extreme (1-1000)")
        print("5. Custom (1-?)\n")

        key = msvcrt.getch()

        if key == b'1':
            return "easy", 10
        elif key == b'2':
            return "medium", 50
        elif key == b'3':
            return "hard", 100
        elif key == b'4':
            return "extreme", 1000
        elif key == b'5':
            return choose_custom_range()
        else:
            print("Invalid key. Please press 1, 2, 3, 4 or 5.")

def play_game():
    player_name = input("Enter your name (Skip if Anonymous): ").strip()
    if not player_name:
        player_name = "Anonymous"

    is_running = True
    while is_running:
        os.system("cls")
        lowest_num = 1
        result = choose_difficulty()

        if len(result) == 2:
            difficulty, highest_num = result
        else:
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
                continue

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
                    json.dump(highscores, f, indent=4)
                
                break

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            is_running = False
            print("Okay. Thanks for playing!")
            os.system("cls")
            break

def show_highscores():
    os.system("cls")
    print("\n=== Highscores ===")
    for diff in difficulties:
        if highscores[diff]:
            best = highscores[diff][0]
            print(f"{diff.title()}: {best['name']} - {best['guesses']} guesses")
        else:
            print(f"{diff.title()}: None")
    print("===================")

def show_leaderboard():
    os.system("cls")
    print("\n=== Leaderboard (Best Player Per Difficulty) ===")
    for diff in difficulties:
        if diff == "custom":
            continue
        scores = highscores[diff]
        if not scores:
            print(f"{diff.title()}: None yet")
        else:
            seen_guesses = set()
            print(f"{diff.title()}")
            for entry in scores:
                if entry["guesses"] not in seen_guesses:
                    print(f"   {entry["name"]} - {entry["guesses"]} guesses")
                    seen_guesses.add(entry["guesses"])
    print("\n================================================")

def clear_game_data():
    comfirm = input("Reset all of your highscores? (y/n): ").strip().lower()
    if comfirm == "y":
        if SCORES_FILE.exists():
            os.remove(SCORES_FILE)

            for diff in difficulties:
                highscores[diff].clear()
            print("All game data cleared! Highscores reset.")
        else:
            print("No saved highscores found.")
    elif comfirm == "n":
        print("Highscores still saved.")
    else:
        print("Invalid input.")

def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Play Game")
        print("2. View Highscores")
        print("3. View Leaderboards")
        print("4. Clear Game Data")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_highscores()
        elif choice == "3":
            show_leaderboard()
        elif choice == "4":
            clear_game_data()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main_menu()

# Streaks
# Timer (chosen)
# Achievements !!!