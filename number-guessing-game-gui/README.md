# Number Guessing Game GUI

This project is a graphical user interface (GUI) implementation of the classic number guessing game. Players have a limited number of attempts to guess a randomly generated number within a specified range.

## Project Structure

```
number-guessing-game-gui
├── src
│   ├── main.py          # Entry point of the application
│   ├── gui
│   │   └── app.py      # GUI logic for the number guessing game
├── requirements.txt     # Dependencies required for the project
└── README.md            # Documentation for the project
```

## Requirements

To run this project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Running the Application

To start the number guessing game, run the following command in your terminal:

```
python src/main.py
```

## How to Play

1. When the application starts, a window will appear prompting you to guess a number between 1 and 10.
2. You have 3 attempts to guess the correct number.
3. After each guess, you will receive feedback indicating whether your guess was too high, too low, or correct.
4. If you guess correctly, you will be congratulated. If you run out of attempts, the correct number will be revealed.

Enjoy the game!