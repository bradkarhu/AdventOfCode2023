from sys import argv

def solve(lines: list[str]):
    sum = 0
    for line in lines:
        sum += 1
    print(sum)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)