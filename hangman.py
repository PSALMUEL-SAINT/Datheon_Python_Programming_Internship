
import random
from pathlib import Path

# Locate the words.txt file in the same folder as this script
WORDS_FILE = Path(__file__).parent / "words.txt"

# ASCII gallows art for 0 to 6 incorrect guesses
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """,
]


def load_words():
    """Load valid words from words.txt."""
    try:
        with open(WORDS_FILE, "r", encoding="utf-8") as file:
            words = [
                line.strip().lower()
                for line in file
                if line.strip().isalpha()
            ]

        if not words:
            raise ValueError("The words.txt file contains no valid words.")

        return words

    except FileNotFoundError:
        print("Error: words.txt was not found.")
        print("Make sure it is in the same folder as hangman.py.")
        return []


def play_hangman():
    """Run one round of the Hangman game."""
    words = load_words()

    if not words:
        return

    secret_word = random.choice(words)
    guessed_letters = set()
    attempts_left = 6

    print("=" * 35)
    print("       HANGMAN WORD GAME")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect guesses available.")

    while attempts_left > 0:
        mistakes = 6 - attempts_left

        print(HANGMAN_STAGES[mistakes])

        display_word = " ".join(
            letter.upper() if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("Word:", display_word)
        print(
            "Guessed letters:",
            " ".join(sorted(letter.upper() for letter in guessed_letters))
            or "None"
        )
        print(f"Incorrect attempts remaining: {attempts_left}")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print("The word was:", secret_word.upper())
            print("=" * 35)
            return

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter one letter.")
            continue

        if guess in guessed_letters:
            print(
                f"You already guessed '{guess.upper()}'. "
                "Try another letter."
            )
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Correct! '{guess.upper()}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess.upper()}' is not in the word.")

        print()

    print(HANGMAN_STAGES[6])
    print("GAME OVER! You have run out of attempts.")
    print("The correct word was:", secret_word.upper())
    print("=" * 35)


if __name__ == "__main__":
    play_hangman()
