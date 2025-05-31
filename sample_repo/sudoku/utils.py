def generate_sudoku_board(size=9):
    """Generates a new Sudoku board."""
    import random

    def fill_board(board):
        for i in range(size):
            for j in range(size):
                if board[i][j] == 0:
                    num = random.randint(1, size)
                    while not is_valid(board, i, j, num):
                        num = random.randint(1, size)
                    board[i][j] = num
                    if fill_board(board):
                        return True
                    board[i][j] = 0
        return False

    def is_valid(board, row, col, num):
        for x in range(size):
            if board[row][x] == num or board[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    board = [[0 for _ in range(size)] for _ in range(size)]
    fill_board(board)
    return board

def print_board(board):
    """Prints the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def check_solution(board):
    """Checks if the current board is a valid solution."""
    for row in board:
        if len(set(row) - {0}) != len([num for num in row if num != 0]):
            return False
    for col in range(len(board)):
        if len(set(board[row][col] for row in range(len(board))) - {0}) != len([board[row][col] for row in range(len(board)) if board[row][col] != 0]):
            return False
    for i in range(0, len(board), 3):
        for j in range(0, len(board), 3):
            if len(set(board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)) - {0}) != len([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3) if board[x][y] != 0]):
                return False
    return True