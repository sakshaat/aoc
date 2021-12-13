#!/usr/local/bin/python3 

from utils import get_input_lines
from collections import defaultdict, Counter

lines = get_input_lines("input6.txt")

fishes = Counter([int(x) for x in lines[0].split(",")])

def sim(X, n):
    for _ in range(n):
        Y = defaultdict(int)
        for x, cnt in X.items():
            if not x:
                Y[6] += cnt
                Y[8] += cnt
            else:
                Y[x-1] += cnt
            X = Y
    return sum(X.values())

print(sim(fishes, 80))
print(sim(fishes, 256))
