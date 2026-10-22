# Hangman Word Guessing Game

A terminal-based Hangman game developed with Python as part of the Datheon Python Programming Internship. The player attempts to guess a randomly selected hidden word, one letter at a time, with a maximum of six incorrect guesses.

## Features

- Random word selection from an external `words.txt` file.
- ASCII gallows art that updates with each incorrect guess.
- Displays correctly guessed letters while hiding unguessed letters.
- Tracks previously guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Validates user input.
- Displays clear victory and defeat messages.
- Handles missing or empty word-list files.

## Technologies Used

- **Python 3**
- **Random module** for selecting words.
- **Pathlib** for locating the word-list file.
- **Sets** for tracking guessed letters.
- **Text files** for storing game words.

## Project Structure

```text
Datheon Hangman/
├── hangman.py
├── words.txt
└── README.md
```

### File Descriptions

- `hangman.py` — Contains the game logic, input validation, word selection, and ASCII gallows art.
- `words.txt` — Contains the words used by the game, with one word per line.
- `README.md` — Provides project information and instructions for running the game.

## Requirements

- Python 3 installed on your computer.
- A terminal or command prompt.

No additional Python packages are required.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/PSALMUEL-SAINT/Datheon_Python_Programming_Internship.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Datheon_Python_Programming_Internship
   ```

3. Ensure that `hangman.py` and `words.txt` are in the same directory.

4. Run the game:

   ```bash
   python hangman.py
   ```

If your system uses the `python3` command, you can run `python3 hangman.py` instead.

## How to Play

1. Start the game using the command above.
2. A random word is selected from `words.txt`.
3. Enter one letter at a time to guess the hidden word.
4. Correct guesses reveal the matching letters.
5. Incorrect guesses reduce your remaining attempts and update the gallows art.
6. Repeated guesses do not cost an attempt.
7. Guess the entire word before using all six incorrect guesses to win.

## Managing the Word List

To add more words, open `words.txt` and add one alphabetic word per line.

Example:

```text
python
computer
developer
programming
```

Save the file before starting the game. The program loads the word list when a new game starts.

## Learning Objectives

This project demonstrates the practical use of:

- Python functions and loops.
- Conditional statements.
- User input and input validation.
- Sets and string manipulation.
- Random selection.
- File handling and reading text files.
- Error handling.
- Basic game development.

## Future Improvements

- Add difficulty levels.
- Allow players to replay without restarting the program.
- Introduce word categories.
- Track player scores and wins.
- Add hints for difficult words.

## Author

**PSALMUEL-SAINT**

Developed as a Python programming practice project during the Datheon Python Programming Internship.

---

*This project is intended for learning and demonstrating foundational Python programming skills.*