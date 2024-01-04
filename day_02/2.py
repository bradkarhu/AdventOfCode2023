import re
from sys import argv

def solve(lines: list[str]):
    sum = 0
    for line in lines:
        split = re.split(":", line)
        game = re.sub("Game ", "", split[0])
        power = get_power(re.split(";", split[1]))
        #print(f'{game}: {power}')
        sum += power
    print(sum)

def get_power(pulls: list[str]) -> int:
    min_red = 0
    min_green = 0
    min_blue = 0
    for pull in pulls:
        pairs = re.split(",", pull)
        for pair in pairs:
            kvp = re.split(" ", pair)
            #print(f'color={kvp[2]}, number={kvp[1]}')
            if kvp[2] == "red":
                min_red = max(min_red, int(kvp[1]))
            if kvp[2] == "green":
                min_green = max(min_green, int(kvp[1]))
            if kvp[2] == "blue":
                min_blue = max(min_blue, int(kvp[1]))
    #print(f'red={min_red}, green={min_green}, blue={min_blue}')
    return min_red * min_green * min_blue

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)