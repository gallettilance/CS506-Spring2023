import os
import time

class Board():

    def __init__(self, N):
        self.queen = "Q"
        self.blank = "-"
        self.N = N
        self.board = [[self.blank for _ in range(self.N)] for _ in range(self.N)]
    
    def __repr__(self):
        return "\n".join([" ".join(x) for x in self.board])

    def is_queen(self, row, col):
        return self.board[row][col] == self.queen

    def set_queen_at(self, row, col):
        self.board[row][col] = self.queen
    
    def unset_queen_on(self, row):
        self.board[row] = [self.blank for _ in range(self.N)]

    def is_valid_row(self, row):
        for j in range(self.N):
            if self.is_queen(row, j):
                return False
        return True

    def is_valid_col(self, col):
        for i in range(self.N):
            if self.is_queen(i, col):
                return False
        return True

    def is_on_board(self, row, col):
        return row >=0 and row < self.N and col >= 0 and col <self.N

    def is_valid_diag(self, row, col):
        for i in range(self.N):
            if self.is_on_board(row - i, col - i) and self.is_queen(row - i, col - i):
                return False
            if self.is_on_board(row - i, col + i) and self.is_queen(row - i, col + i):
                return False
            if self.is_on_board(row + i, col - i) and self.is_queen(row + i, col - i):
                return False
            if self.is_on_board(row + i, col + i) and self.is_queen(row + i, col + i):
                return False
        return True

    def is_valid_move(self, row, col):
        if not self.is_valid_row(row):
            return False
        if not self.is_valid_col(col):
            return False
        if not self.is_valid_diag(row, col):
            return False
        return True

    def find_queen_on(self, row):
        for col in range(self.N):
            if self.is_queen(row, col):
                return col
        raise ValueError("programmer error")

    def search(self):
        row = 0
        col = 0
        nsols = 0

        while row >= 0:
            if row < self.N:
                # searching for solution
                if col == self.N:
                    # backtrack
                    row -= 1
                    if row >= 0:
                        # only backtrack if valid row
                        col = self.find_queen_on(row) + 1
                        self.unset_queen_on(row)
                else:
                    if self.is_valid_move(row, col):
                        self.set_queen_at(row, col)
                        row += 1
                        col = 0
                        # os.system("clear")
                        # print(self)
                        # time.sleep(.05)
                    else:
                        col += 1
                    
            else:
                # found a solution!
                nsols += 1
                os.system("clear")
                print("found solution ", nsols)
                print(self)
                input("Enter for next solution: ")

                # reset row and col to find next solution
                row -= 1
                col = self.find_queen_on(row) + 1
                self.unset_queen_on(row)
        
        if nsols > 0:
            print("no more solutions found")
        else:
            print("no solutions found")
    
        return


board = Board(8)
board.search()
