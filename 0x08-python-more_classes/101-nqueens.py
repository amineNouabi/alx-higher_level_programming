#!/usr/bin/python3
"""

Module defining NQueens Class

"""


class NQueens:
    """
        Class that solves NQueens Problem.
    """

    def __init__(self, N):
        self.__N = N
        self.solutions = []

    def safe_position(self, position):
        [x, y] = position

        # Filter outside the board case
        if x >= self.__N or y >= self.__N or x <= 0 or y <= 0:
            return False

        # Filter Queen Attacked by previously played queens.
        for queen in self.__queens:
            [queen_x, queen_y] = queen

            # Attaking queen straight
            if queen_x == x or queen_y == y:
                return False

            # Attacking in diagonal or taken position
            if abs(queen_x - queen_y) == abs(x - y):
                return False

        # Safe Position
        return True

    def backtrack(self, board, column):

        if len(board) == self.__N:
            self.solutions.append(board.copy())
            return True

        if column > self.__N:
            return False

        for i in range(self.__N):

            if self.safe_position([i, column]):
                board.append([i, column])
                if self.backtrack(board, [i, column + 1]):
                    return True
                board.pop()

        return False

    def solve(self):
        board = []
        self.backtrack(board, 0)
        print(self.solutions)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = NQueens(N).solve()
