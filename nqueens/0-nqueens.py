#!/usr/bin/python3
"""N queens puzzle solver using backtracking"""
import sys
 
 
def is_safe(row, col, queens):
    """Check if a queen at (row, col) is attacked by the placed queens"""
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True
 
 
def solve(row, n, queens):
    """Place queens row by row and print every solution"""
    if row == n:
        print(queens)
        return
    for col in range(n):
        if is_safe(row, col, queens):
            queens.append([row, col])
            solve(row + 1, n, queens)
            queens.pop()
 
 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(0, n, [])
