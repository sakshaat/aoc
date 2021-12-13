from utils import get_input_lines

lines = get_input_lines("input8.txt")

# pt1
result = 0
for line in lines:
    output_list = [x.strip().split(" ") for x in line.split("|")][1]
    result += sum([1 for x in output_list if len(x) in {2, 3, 4, 7}])
# print(result)

# pt2

m = {2: 1, 3: 7, 4: 4, 7: 8}

result = 0
for line in lines:
    mapping_dict = {chr(ord('a') + i) : None for i in range(7)}
    input_list, output_list = [x.strip().split(" ") for x in line.split("|")]
    s = {}
    
    for input in input_list:
        if(len(input) in m):
            s[m[len(input)]] = input
    
    lst = []
    for output in output_list:
        if(len(output) in m):
            lst.append(m[len(output)])
        elif(all([ch in output for ch in s[4]])):
            lst.append(9)
        elif(all([ch in output for ch in s[7]])):
            if(len(output) == 6):
                lst.append(0)
            else:
                lst.append(3)
        elif len(output) == 5:
            if sum([ch in output for ch in s[4]]) == 3:
                lst.append(5)
            else:
                lst.append(2)
        else:
            lst.append(6)
    
    result += int("".join(map(str, lst)))

print(result)