from sys import argv

def solve(lines: list[str]):
    sum = 0
    for line in lines:
        sequence = [int(s) for s in line.split()]
        previous = previous_value(sequence)
        #print(f'{previous} => {sequence}')
        sum += previous
    print(sum)

def previous_value(sequence: list[int]) -> int:
    diffs = []
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        diffs.append(diff)
    if any(x != 0 for x in diffs):
        return sequence[0] - previous_value(diffs)
    return sequence[0]

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)