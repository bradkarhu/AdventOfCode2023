import re
import sys

def solve(lines: list[str]):
    sum = 0
    for line in lines:
        digits = re.findall("\d", replace_words(line))
        #print(digits[0]+digits[-1])
        number = int(f'{digits[0]}{digits[-1]}')
        #print(number)
        sum += number
    print(sum)

def replace_words(line: str) -> str:
    cal = line
    cal = cal.replace("one", "o1e")
    cal = cal.replace("two", "t2o")
    cal = cal.replace("three", "t3e")
    cal = cal.replace("four", "f4r")
    cal = cal.replace("five", "f5e")
    cal = cal.replace("six", "s6x")
    cal = cal.replace("seven", "s7n")
    cal = cal.replace("eight", "e8t")
    cal = cal.replace("nine", "n9e")
    return cal

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)