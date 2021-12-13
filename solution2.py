from utils import get_input_lines

lines = get_input_lines("input2.txt")


# pt1
commands = [(x.split(' ')[0], int(x.split(' ')[1])) for x in lines]

x_val = sum([x[1] for x in commands if x[0] == "forward"])
y_val = sum([-x[1] if x[0] == "up" else x[1] for x in commands if x[0] == "up" or x[0] == "down"])

print(x_val * y_val)


# pt2
aim = 0
x = 0
depth = 0

for command in commands:
    a = command[0]
    v = command[1]

    if(a == "down"):
        aim += v
    elif(a == "up"):
        aim -= v
    elif(a == "forward"):
        x += v
        depth += v * aim
    else:
        raise ValueError

print(x * depth)
    