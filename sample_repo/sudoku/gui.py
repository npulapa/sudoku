from tkinter import Tk, Frame, Button, Label, StringVar, Entry

class SudokuGUI(Frame):
    def __init__(self, master, game):
        super().__init__(master)
        self.game = game
        self.master = master
        master.title("Sudoku Game")

        self.grid_frame = Frame(master)
        self.grid_frame.pack()

        self.cells = [[StringVar() for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]

        self.create_grid()
        self.fill_initial_board()

        self.solve_button = Button(master, text="Solve", command=self.solve)
        self.solve_button.pack()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = Entry(self.grid_frame, textvariable=self.cells[i][j], width=2, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.entries[i][j] = entry

    def fill_initial_board(self):
        for i in range(9):
            for j in range(9):
                value = self.game.board[i][j]
                if value != 0:
                    self.cells[i][j].set(str(value))
                    self.entries[i][j].config(state='disabled')

    def solve(self):
        # Placeholder for solve functionality
        pass

if __name__ == "__main__":
    root = Tk()
    sudoku_gui = SudokuGUI(root)
    root.mainloop()