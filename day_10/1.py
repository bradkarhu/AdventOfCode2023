from sys import argv

def solve(lines: list[str]):
    s_index = get_s(lines)
    next1 = get_next(lines, s_index, [-1,-1])
    next2 = get_next(lines, s_index, next1)
    previous1 = s_index
    previous2 = s_index
    steps = 0
    while True:
        steps += 1
        a = get_next(lines, next1, previous1)
        set_char(lines, previous1, '*')
        b = get_next(lines, next2, previous2)
        set_char(lines, previous2, '*')
        if a == b: 
            set_char(lines, a, '*')
            set_char(lines, next1, '*')
            set_char(lines, next2, '*')
            break
        previous1 = next1
        previous2 = next2
        next1 = a
        next2 = b
    #write_lines(lines, "progress.txt")
    print(steps + 1)

def pad_input(lines: list[str]) -> list[str]:
    width = len(lines[0]) + 4
    padded = []
    padded.append("%" * width)
    for line in iter(lines):
        padded.append("%." + line + ".%")
    padded.append("%" * width)
    return padded

def write_lines(lines: list[str], filename: str):      
    with open(filename, "w") as file:
        file.writelines("\r\n".join(lines))

def get_s(lines: list[str]) -> [int, int]:
    for j in range(len(lines)):
        line = lines[j]
        for i in range(len(line)):
            if line[i] == 'S': return j,i

def set_char(lines: list[str], index: [int, int], value: chr):
    lines[index[0]] = lines[index[0]][:index[1]] + value + lines[index[0]][index[1]+1:]

def get_next(lines: list[str], start: [int, int], skip: [int, int]) -> [int, int]:
    j = start[0]
    i = start[1]
    current = lines[j][i] # supports: - | F L J 7 S
    if current == '-' or current == 'S':
        if skip != (j,i-1) and lines[j][i-1] in ('-', 'F', 'L'): return j,i-1
        if skip != (j,i+1) and lines[j][i+1] in ('-', 'J', '7'): return j,i+1
    if current == '|' or current == 'S':
        if skip != (j-1,i) and lines[j-1][i] in ('|', 'F', '7'): return j-1,i
        if skip != (j+1,i) and lines[j+1][i] in ('|', 'J', 'L'): return j+1,i
    if current == 'F' or current == 'S':
        if skip != (j,i+1) and lines[j][i+1] in ('-', 'J', '7'): return j,i+1
        if skip != (j+1,i) and lines[j+1][i] in ('|', 'J', 'L'): return j+1,i
    if current == 'L' or current == 'S':
        if skip != (j,i+1) and lines[j][i+1] in ('-', 'J', '7'): return j,i+1
        if skip != (j-1,i) and lines[j-1][i] in ('|', 'F', '7'): return j-1,i
    if current == 'J' or current == 'S':
        if skip != (j,i-1) and lines[j][i-1] in ('-', 'F', 'L'): return j,i-1
        if skip != (j-1,i) and lines[j-1][i] in ('|', 'F', '7'): return j-1,i
    if current == '7' or current == 'S':
        if skip != (j,i-1) and lines[j][i-1] in ('-', 'F', 'L'): return j,i-1
        if skip != (j+1,i) and lines[j+1][i] in ('|', 'J', 'L'): return j+1,i
    else:
        raise Exception(f"[get_next] should not be able to get here: {current} {start}")

with open(argv[1], "r") as file:
    f = file.read().splitlines()

part1 = pad_input(f)

solve(part1)