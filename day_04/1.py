from sys import argv

def solve(lines: list[str]):
    sum = 0
    for line in iter(lines):
        data = line.split(":")[1].strip()
        index = data.find("|")
        winners = data[:index].strip().split()
        numbers = data[index+1:].strip().split()
        #print(f'winners = {winners}')
        #print(f'numbers = {numbers}')
        matches = set(winners) & set(numbers)
        if len(matches) > 0:
            points = pow(2, len(matches) - 1)
            #print(f'{matches} = {points} points')
            sum += points
    print(sum)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)