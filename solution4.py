#!/usr/local/bin/python3 

from utils import get_input_lines
import numpy as np

lines = get_input_lines("input4.txt")

# setup

numbers_called = lines[0]

class Board:

    def __init__(self, lines):
        assert(len(lines) == 5)
        self._board = np.asmatrix([[int(x) for x in line.split(" ") if x != ''] for line in lines])
        self._marked = np.full((5, 5), False)

    def __repr__(self):
        return self._board.__str__() + '\n' + self._marked.__str__()

    def mark_number(self, num):
        idx = np.where(self._board == num)

        if(idx[0].size == 0):
            return 
        
        self._marked[idx[0], idx[1]] = True

    def hasWon(self):
        return any(np.all((self._marked == True), axis=1)) or any(np.all((self._marked == True), axis=0))
    
    def unmarked_number_sum(self):
        return np.sum(self._board[self._marked != True])
    
boards = []
for i in range(2, len(lines), 6):
    boards.append(Board(lines[i:i+5]))

# pt1
def get_first_winning_board(boards, numbers_called):
    numbers = [int(n) for n in numbers_called.split(',') if n != '']
    for n in numbers:

        for board in boards:
            board.mark_number(n)

            if(board.hasWon()):
                return (board, n)

    raise ValueError("No one won")
        
def get_first_winning_board_score(boards, numbers_called):
    result = get_first_winning_board(boards, numbers_called)
    return result[0].unmarked_number_sum() * result[1]

print(get_first_winning_board_score(boards, numbers_called))

# pt2

boards = []
for i in range(2, len(lines), 6):
    boards.append(Board(lines[i:i+5]))

def get_last_winning_board(boards, numbers_called):
    numbers = [int(n) for n in numbers_called.split(',') if n != '']
    for n in numbers:

        for board in boards:
            board.mark_number(n)

        if len(boards) > 1:
            boards = [x for x in boards if not x.hasWon()]
        else:
            if(boards[0].hasWon()): return (boards[0], n)
  
    raise ValueError("No active boards left")


def get_last_winning_board_score(boards, numbers_called):
    result = get_last_winning_board(boards, numbers_called)
    return result[0].unmarked_number_sum() * result[1]

print(get_last_winning_board_score(boards, numbers_called))
