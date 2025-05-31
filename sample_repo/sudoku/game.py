class SudokuGame:
    def __init__(self):
        # 0 means empty cell
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.solution = self.solve(self.board)
        self.user_board = [[0]*9 for _ in range(9)]

    def generate_new_board(self):
        # Logic to generate a new Sudoku board
        pass

    def solve(self, board):
        # Logic to solve the Sudoku board
        pass

    def is_valid_move(self, row, col, num):
        # Logic to check if a move is valid
        pass

    def make_move(self, row, col, num):
        # Logic to make a move on the board
        pass

    def check_win(self):
        # Logic to check if the user has won
        pass

    def reset_game(self):
        # Logic to reset the game
        pass