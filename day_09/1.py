import sys

def solve(lines: list[str]):
    sum = 0
    for line in lines:
        sequence = [int(s) for s in line.split()]
        next = next_value(sequence)
        #print(f'{sequence} => {next}')
        sum += next
    print(sum)

def next_value(sequence: list[int]) -> int:
    diffs = []
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        diffs.append(diff)
    if any(x != 0 for x in diffs):
        return sequence[-1] + next_value(diffs)
    return sequence[-1]

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)