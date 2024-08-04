#!/usr/bin/python3
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_invalid_number_and_exit():
    print("N must be a number")
    sys.exit(1)

def print_invalid_value_and_exit():
    print("N must be at least 4")
    sys.exit(1)

def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    def solve(board, row):
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * N
    solve(board, 0)
    return solutions

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_invalid_number_and_exit()

    if N < 4:
        print_invalid_value_and_exit()

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
