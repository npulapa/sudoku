# This is the entry point for the Sudoku game.
import tkinter as tk
from gui import SudokuGUI
from game import SudokuGame

def main():
    root = tk.Tk()
    root.title("Sudoku Game")
    
    game = SudokuGame()
    gui = SudokuGUI(root, game)
    
    gui.pack()
    root.mainloop()

if __name__ == "__main__":
    main()