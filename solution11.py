from utils import get_input_lines

lines = get_input_lines("input11.txt")

# pt 1
n, m = len(lines), len(lines[0])

def get_valid_neighbors(x, y):
    neighbors = [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x), (y + 1, x + 1), (y + 1, x - 1), (y - 1, x - 1), (y - 1, x + 1)]
    return list(filter(lambda t: min(t) >= 0 and t[0] < n and t[1] < m, neighbors))

def get_flashes_sum(lines, steps=2):

    flashes = 0

    import numpy as np 
    power_mat = np.full((n, m), -1)

    # init
    for y in range(n):
        for x in range(m):
            power_mat[y][x] = int(lines[y][x])

    for _ in range(steps):
        # increase energy by 1 and find all the nines
        nines = set()
        for y in range(n):
            for x in range(m):
                power_mat[y][x] += 1

                if(power_mat[y][x] > 9):
                    nines.add((y, x))
        
        flashed = set()

        while nines:
            elem = nines.pop()
            x, y = elem[1], elem[0]
            neighs = get_valid_neighbors(x,y)
            
            # increment neighbors
            for neigh in neighs:
                if (neigh[0], neigh[1]) not in flashed:
                    power_mat[neigh[0]][neigh[1]] += 1
                    if power_mat[neigh[0]][neigh[1]] > 9:
                        nines.add((neigh[0], neigh[1]))

            if (y,x) not in flashed:
                power_mat[y][x] = 0
                flashes += 1
                flashed.add((y,x))
    
    return flashes

print(get_flashes_sum(lines, 100))

#pt 2

def get_first_sync(lines):

    import numpy as np 
    power_mat = np.full((n, m), -1)

    # init
    for y in range(n):
        for x in range(m):
            power_mat[y][x] = int(lines[y][x])

    count = 0
    
    while power_mat.any():
        count += 1

        # increase energy by 1 and find all the nines
        nines = set()
        for y in range(n):
            for x in range(m):
                power_mat[y][x] += 1
                if(power_mat[y][x] > 9):
                    nines.add((y, x))
        
        flashed = set()
        while nines:
            elem = nines.pop()
            x, y = elem[1], elem[0]
            neighs = get_valid_neighbors(x,y)
            
            # increment neighbors
            for neigh in neighs:
                if (neigh[0], neigh[1]) not in flashed:
                    power_mat[neigh[0]][neigh[1]] += 1
                    if power_mat[neigh[0]][neigh[1]] > 9:
                        nines.add((neigh[0], neigh[1]))

            if (y,x) not in flashed:
                power_mat[y][x] = 0
                flashed.add((y,x))

    return count
        
print(get_first_sync(lines))