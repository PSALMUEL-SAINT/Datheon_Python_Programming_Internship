
import random

words = ["python", "computer", "programming", "developer", "keyboard"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("=== HANGMAN WORD GUESSING GAME ===")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Attempts remaining:", attempts)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

else:
    print("\nGame over! The word was:", word)
