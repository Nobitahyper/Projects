'''This script implements the classic game of "Hangman" with a twist. Instead of just guessing a word,
players are provided with a clue to help them guess the word. The game uses a JSON file as its data source,
containing words paired with their respective clues. Players choose a difficulty level (easy, medium, or hard)
based on the word length, and then attempt to guess the word letter by letter. For every incorrect guess, a part
of a hangman figure is drawn. The game ends either when the player successfully guesses the word or when the hangman
figure is fully drawn, indicating that the player has run out of attempts.
'''

from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

import random
import json

# Load the JSON data
with open("data.json", "r") as file:
    data_json = json.load(file)

def choose_word_and_clue_by_difficulty(data_json, difficulty):
    """Randomly select a word and its clue based on the chosen difficulty."""
    if difficulty == "easy":
        suitable_words = [key for key in data_json.keys() if 3 <= len(key) <= 5]
    elif difficulty == "medium":
        suitable_words = [key for key in data_json.keys() if 6 <= len(key) <= 8]
    else:
        suitable_words = [key for key in data_json.keys() if len(key) >= 9]

    word = random.choice(suitable_words)
    clue = data_json[word][0]
    return word, clue

def hangman_state(turns):
    """Return the hangman drawing based on the remaining turns."""
    states = [
        ['  --------  ', '     O_|    ', '    /|\\      ', '    / \\     '],
        ['  --------  ', '   \\ O_|/   ', '     |      ', '    / \\     '],
        ['  --------  ', '   \\ O /|   ', '     |      ', '    / \\     '],
        ['  --------  ', '   \\ O /    ', '     |      ', '    / \\     '],
        ['  --------  ', '   \\ O      ', '     |      ', '    / \\     '],
        ['  --------  ', '     O      ', '     |      ', '    / \\     '],
        ['  --------  ', '     O      ', '     |      ', '    /       '],
        ['  --------  ', '     O      ', '     |      '],
        ['  --------  ', '     O      '],
        ['  --------  '],
        []
    ]
    return states[10 - turns]

def hangman(data_json):
    # Ask player for difficulty level
    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid choice. Please select from 'easy', 'medium', or 'hard'.")
        difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()

    word, clue = choose_word_and_clue_by_difficulty(data_json, difficulty)
    word = word.lower()

    validLetters = 'abcdefghijklmnopqrstuvwxyz '
    turns = 10
    guessed_letters = ''

    print(f"{Fore.CYAN}Clue: {clue}{Style.RESET_ALL}\n")

    while len(word) > 0:
        current_guess = "".join([letter if letter in guessed_letters or letter == " " else "_" for letter in word])

        if current_guess == word:
            print(f"{Fore.GREEN}{current_guess}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}You win!{Style.RESET_ALL}")
            return

        print("Guess the word:", current_guess)
        guess = input().lower()

        if guess == "hint":
            random_unrevealed_letter = random.choice([char for char in word if char not in guessed_letters])
            print(f"Hint: The word contains the letter '{random_unrevealed_letter}'.")
            turns -= 2  # Reduce turns by 2 for using a hint
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        if guess in validLetters:
            guessed_letters += guess
        else:
            print("Enter a valid character")
            continue

        if guess not in word:
            turns -= 1
            print(f"{Fore.RED}\n".join(hangman_state(turns)) + Style.RESET_ALL)
            if turns == 0:
                print(f"{Fore.RED}You lose!{Style.RESET_ALL}")
                print(f"The word was: {word}")
                return

# Start the hangman game and ask if the player wants to play again
while True:
    hangman(data_json)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
