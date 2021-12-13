#!/usr/local/bin/python3 

from utils import get_input_lines

lines = get_input_lines("input1.txt")

result = sum([1 if (lines[i-2] + lines[i-1] + lines[i]) > (lines[i-3] + lines[i-2] + lines[i-1]) else 0 for i in range(3, len(lines))])
print(result)
