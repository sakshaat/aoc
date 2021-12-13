from utils import get_input_lines
from numpy import median
from collections import Counter

lines = get_input_lines("input7.txt")
input_list = [int(x) for x  in lines[0].split(",")]

# pt1
print(sum(abs(x - median(input_list)) for x in input_list))

# pt2
mi, mx = min(input_list), max(input_list)
fuel_required = Counter({ elem:0 for elem in range(mi, mx+1) })

sum_one_to_n = lambda n: (n * (n + 1)) // 2

for i in range(mi, mx+1):
    for e in input_list:
        fuel_required[i] += sum_one_to_n(abs(e - i))

print(fuel_required.most_common()[-1])