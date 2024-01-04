import sys

def solve(lines: list[str]):
    sum = 0
    width = len(lines[0])
    for index in range(1, len(lines) - 2):
        line = lines[index]
        previous_line = lines[index - 1]
        next_line = lines[index + 1]
        for i in range(2, width - 4):
            if line[i] == '.': continue
            if line[i].isdigit(): continue
            #print(f'found symbol at [{index}, {i}]')
            if previous_line[i].isdigit():
                #print(f'found {previous_line[i]} N')
                previous_line, number = get_number(previous_line, i)
                sum += int(number)
            if next_line[i].isdigit():
                #print(f'found {next_line[i]} S')
                next_line, number = get_number(next_line, i)
                sum += int(number)
            if line[i + 1].isdigit():
                #print(f'found {line[i + 1]} W')
                line, number = get_number(line, i + 1)
                sum += int(number)
            if previous_line[i + 1].isdigit():
                #print(f'found {previous_line[i + 1]} NW')
                previous_line, number = get_number(previous_line, i + 1)
                sum += int(number)
            if next_line[i + 1].isdigit():
                #print(f'found {next_line[i + 1]} SW')
                next_line, number = get_number(next_line, i + 1)
                sum += int(number)
            if line[i - 1].isdigit():
                #print(f'found {line[i - 1]} E')
                line, number = get_number(line, i - 1)
                sum += int(number)
            if previous_line[i - 1].isdigit():
                #print(f'found {previous_line[i - 1]} NE')
                previous_line, number = get_number(previous_line, i - 1)
                sum += int(number)
            if next_line[i - 1].isdigit():
                #print(f'found {next_line[i - 1]} SE')
                next_line, number = get_number(next_line, i - 1)
                sum += int(number)
        lines[index] = line
        lines[index - 1] = previous_line
        lines[index + 1] = next_line
    print(sum)

def pad_input(lines: list[str]) -> list[str]:
    width = len(lines[0]) + 4
    padded = []
    padded.append("." * width)
    for line in iter(lines):
        padded.append(".." + line + "..")
    padded.append("." * width)
    return padded

def get_number(line: str, index: int) -> [str, str]:
    start = index
    end = index + 1
    while line[start - 1].isdigit(): start -= 1
    while line[end].isdigit(): end += 1
    number = line[start:end]
    #print(f'found number: {number} => {("." * (end - start))}')
    line = line[:start] + ("." * (end - start)) + line[end:]
    #print(line)
    return line, number

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(pad_input(f))