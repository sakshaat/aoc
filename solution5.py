#!/usr/local/bin/python3 

from utils import get_input_lines
import numpy as np
from functools import reduce

lines = get_input_lines("input5.txt")

# setup
class LineSegment:
    def __init__(self, line):
        split1 = line.split("->")
        start, end = split1[0].strip(), split1[1].strip()

        self.x_start = int(start.split(",")[0])
        self.y_start = int(start.split(",")[1])

        self.x_end = int(end.split(",")[0])
        self.y_end = int(end.split(",")[1])
    
    def __repr__(self):
        return f"({self.x_start}, {self.y_start}) -> ({self.x_end}, {self.y_end})"
    
    def get_largest_coordinates(self):
        return (max(self.x_start, self.x_end), max(self.y_start, self.y_end))

segments = [LineSegment(x) for x in lines]

reduce_fcn = lambda r, a: (max(r[0], a.get_largest_coordinates()[0] + 1), max(r[1], a.get_largest_coordinates()[1] + 1))
board_size = reduce(reduce_fcn, segments, (0, 0))
print(f"board size={board_size}")

# pt1

board = np.full(board_size, 0)

def get_diagonal_indices(x1, y1, x2, y2):

    x_inc = 1 if x1 < x2 else -1
    y_inc = 1 if y1 < y2 else -1

    curr_coord = [x1, y1]
    return_list = [curr_coord]

    while(curr_coord != [x2, y2]):
        next_coord = [curr_coord[0] + x_inc, curr_coord[1] + y_inc]
        return_list.append(next_coord)
        curr_coord = next_coord

    return return_list
    

for segment in segments:
    if(segment.x_start != segment.x_end and segment.y_start != segment.y_end):
        indexes_to_increment = get_diagonal_indices(segment.x_start, segment.y_start, segment.x_end, segment.y_end)
        for idx in indexes_to_increment:
            board[idx[1], idx[0]] += 1
    else:
        x1, x2 = min(segment.x_start, segment.x_end), max(segment.x_start, segment.x_end)
        y1, y2 = min(segment.y_start, segment.y_end), max(segment.y_start, segment.y_end)
        board[y1:y2 + 1, x1:x2 + 1] += 1

result = (board >= 2).sum()
print(result)
