from utils import get_input_lines

lines = get_input_lines("input3.txt")

# pt 1

def most_common_bit(bits):
    return max(bits, key=bits.count)

def least_common_bit(bits):
    return min(bits, key=bits.count)


transposed_lines = list(map(list, zip(*[x for x in lines])))

most_common_bits = [most_common_bit(x) for x in transposed_lines]
least_common_bits = [least_common_bit(x) for x in transposed_lines]

gamma = int("".join(most_common_bits), 2)
epsilon = int("".join(least_common_bits), 2)

print(gamma*epsilon)

# pt 2

def get_oxygen_gen_rating_helper(lines, position):
    if(len(lines) == 1):
        return lines[0]
    else:
        bit_arr = list(map(list, zip(*[x for x in lines])))
        bits = bit_arr[position]
        filter_char = "1" if bits.count("1") >= bits.count("0") else "0"

        return get_oxygen_gen_rating_helper([x for x in lines if x[position] == filter_char], position+1)

def get_oxygen_gen_rating(lines):
    result = "".join(get_oxygen_gen_rating_helper(lines, 0))
    return int(result, 2)

def get_c02_scrub_rating_helper(lines, position):
    if(len(lines) == 1):
        return lines[0]
    else:
        bit_arr = list(map(list, zip(*[x for x in lines])))
        bits = bit_arr[position]
        filter_char = "1" if bits.count("1") < bits.count("0") else "0"

        return get_c02_scrub_rating_helper([x for x in lines if x[position] == filter_char], position+1)

def get_c02_scrub_rating(lines):
    result = "".join(get_c02_scrub_rating_helper(lines, 0))
    return int(result, 2)

oxygen_gen_rating = get_oxygen_gen_rating(lines)
c02_scrubber_rating = get_c02_scrub_rating(lines)

print(oxygen_gen_rating, c02_scrubber_rating, oxygen_gen_rating * c02_scrubber_rating)