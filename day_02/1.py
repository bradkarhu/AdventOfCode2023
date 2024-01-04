import re
from sys import argv

def solve(lines: list[str]):
    sum = 0
    for line in lines:
        split = re.split(":", line)
        game = re.sub("Game ", "", split[0])
        possible = check_game(re.split(";", split[1]))
        #print(f'{game}: {possible}')
        if possible:
            sum += int(game)
    print(sum)

def check_game(pulls: list[str]) -> bool:    
    for pull in pulls:
        pairs = re.split(",", pull)
        for pair in pairs:                
            kvp = re.split(" ", pair)
            #print(f'color={kvp[2]}, number={kvp[1]}')
            if kvp[2] == "red" and int(kvp[1]) > 12:
                return False                
            if kvp[2] == "green" and int(kvp[1]) > 13:
                return False
            if kvp[2] == "blue" and int(kvp[1]) > 14:
                return False
    return True

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)