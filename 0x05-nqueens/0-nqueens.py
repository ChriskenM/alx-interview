#!/usr/bin/python3
"""
Solving the nqueens problem
"""
import sys


def is_valid(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    This is a utility function to check if a queen can be placed,
    on board[row][col].
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, board, row, solutions):
    """
    Solve the N-Queens problem using backtracking.
    """
    if row == N:
        solution = []
        for i in range(N):
            solution.append([i, board[i]])
        solutions.append(solution)
    else:
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve_nqueens(N, board, row + 1, solutions)
                board[row] = -1


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
