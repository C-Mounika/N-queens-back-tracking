def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].
    This function checks the column and both diagonals to the queen.
    """
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row, n):
    # If all queens are placed
    if row == n:
        return True

    # Try placing the queen in each column one by one
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen on board[row][col]
            board[row][col] = 1

            # Recur to place the next queen
            if solve_nqueens(board, row + 1, n):
                return True

            # If placing queen in board[row][col] leads to no solution, backtrack
            board[row][col] = 0

    # If no place can be found for the queen in this row
    return False

def print_board(board, n):
    for row in range(0, n):
        for col in range(0, n):
            if board[row][col] == 1:
                print('Q', end=" ")
            else:
                print('.', end=" ")
        print("\n")

def n_queens(n):
    board = [[0 for i in range(n)] for j in range(n)]  # Initialize the empty board

    if solve_nqueens(board, 0, n):
        print_board(board, n)
    else:
        print("Solution does not exist.")

n = 4
# You can change this value to try different board sizes
n_queens(n)
