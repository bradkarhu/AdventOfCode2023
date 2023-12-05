import re
import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        sum = 0
        for line in iter(lines):
            digits = re.findall("\d", line)
            #print(digits[0]+digits[-1])
            number = int(f'{digits[0]}{digits[-1]}')
            #print(number)
            sum += number
        return sum

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        sum = 0
        for line in iter(lines):
            digits = re.findall("\d", Helper.replace_words(line))
            #print(digits[0]+digits[-1])
            number = int(f'{digits[0]}{digits[-1]}')
            #print(number)
            sum += number
        return sum

class Helper:    
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

tic = time.perf_counter()
# with open("sample1.txt", "r") as file:
# with open("sample2.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 54951
#Part 2: 55218
#Took 0.0027 seconds