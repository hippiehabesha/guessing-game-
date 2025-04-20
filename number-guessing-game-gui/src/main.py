# File: /number-guessing-game-gui/number-guessing-game-gui/src/main.py

from gui.app import GuessingGameApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()