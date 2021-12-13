def get_input_lines(file_name):
    with open(f"./inputs/{file_name}") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
