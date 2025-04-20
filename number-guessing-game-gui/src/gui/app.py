import random
from tkinter import DISABLED, Button, Entry, Label, Tk


class GuessingGameApp:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.secret_number = random.randint(1, 10)
        self.guess_count = 0
        self.guess_limit = 3

        self.label = Label(master, text="Welcome to the Number Guessing Game! You have 3 chances to guess correctly.")
        self.label.pack()

        self.guess_entry = Entry(master)
        self.guess_entry.pack()

        self.guess_button = Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        guess = int(self.guess_entry.get())
        self.guess_count += 1

        if guess == self.secret_number:
            self.result_label.config(text="Congratulations! You guessed the correct number.")
        elif guess > self.secret_number:
            self.result_label.config(text="Too high! Try again.")
        elif guess < self.secret_number:
            self.result_label.config(text="Too low! Try again.")

        if self.guess_count == self.guess_limit:
            self.result_label.config(text=f"Sorry, you've run out of guesses. The correct number was {self.secret_number}.")
            self.guess_button.config(state=DISABLED)

def main():
    root = Tk()
    app = GuessingGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()