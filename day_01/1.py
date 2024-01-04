import re
import sys

def solve(lines: list[str]):
    sum = 0
    for line in lines:
        digits = re.findall("\d", line)
        #print(digits[0]+digits[-1])
        number = int(f'{digits[0]}{digits[-1]}')
        #print(number)
        sum += number
    print(sum)

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)