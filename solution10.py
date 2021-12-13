from utils import get_input_lines

lines = get_input_lines("input10.txt")


# pt 1
closing_symbol_dict = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}
opening_symbol_dict = dict((v,k) for k,v in closing_symbol_dict.items())

error_score_points_dict = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

ac_score_points_dict = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

from collections import deque

def check_syntax_error_score(line):

    stack = deque()

    for chr in line:
        if len(stack) == 0:
            stack.append(chr)
            continue

        elem = stack.pop()

        if(chr in closing_symbol_dict):
            if elem == closing_symbol_dict[chr]:
                continue
            else:
                # print(f"illegal char {chr} on line:{line}, points={closing_symbol_points_dict[chr]}")
                return error_score_points_dict[chr]
        else:
            stack.append(elem)
            stack.append(chr)
    
    return 0

print(sum([check_syntax_error_score(line) for line in lines]))

# pt 2
def check_autocomplete_score(line):
  
    stack = deque()

    for chr in line:
        if len(stack) == 0:
            stack.append(chr)
            continue

        elem = stack.pop()

        if(chr in closing_symbol_dict):
            if elem == closing_symbol_dict[chr]:
                continue
            else:
                return None
        else:
            stack.append(elem)
            stack.append(chr)
    score = 0

    while(stack):
        elem = stack.pop()
        op_sym = opening_symbol_dict[elem]
        score = (score * 5) + ac_score_points_dict[op_sym]
    
    return score

from statistics import median 
print(median(filter(None, [check_autocomplete_score(line) for line in lines])))
