from utils import get_input_lines

lines = get_input_lines("input9.txt")

# pt 1
total_risk = 0
low_points = []

n, m = len(lines), len(lines[0])

def get_valid_neighbors(x, y):
    neighbors = [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]
    return list(filter(lambda t: min(t) >= 0 and t[0] < n and t[1] < m, neighbors))

for y in range(n):
    for x in range(m):
        if all(lines[y1][x1] > lines[y][x] for y1,x1 in get_valid_neighbors(x,y)):
            total_risk += int(lines[y][x]) + 1
            low_points.append((y,x))

print(total_risk)

# pt 2
all_basin_sizes = []
for lp in low_points:

    seen = set()
    search = [lp]
    size = 0

    while search:

        curr = search.pop()
        if curr in seen:
            continue

        seen.add(curr)
        size += 1
        y,x = curr

        for y1, x1 in get_valid_neighbors(x,y):
            if(lines[y1][x1] != '9' and lines[y1][x1] > lines[y][x]):
                search.append((y1, x1))
        
    all_basin_sizes.append(size)

from functools import reduce
print(reduce(lambda x, y: x * y, sorted(all_basin_sizes, reverse=True)[:3]))

