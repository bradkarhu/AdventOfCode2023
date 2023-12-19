import re
import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        workflows, parts = Helper.parse(lines)
        total = 0
        for p in parts:
            #output = f"{p.to_string()}: "
            name = "in"
            while name in workflows:
                #output += f"{name} -> "
                conditions = workflows[name]
                for condition in conditions:
                    if "<" in condition:
                        c, v, w = re.split('[<>:]', condition)
                        if p.is_less_than(c, int(v)):
                            name = w
                            break
                    elif ">" in condition:
                        c, v, w = re.split('[<>:]', condition)
                        if p.is_greater_than(c, int(v)):
                            name = w
                            break
                    else:
                        name = condition
                        break
            if name == "A":
                total += p.sum()
            #    print(f"{output} -> A = {p.sum()}")
            #else:
            #    print(f"{output} -> R")
        return total

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return 0

class Part:
    def __init__(self, x: int, m: int, a: int, s: int):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def to_string(self) -> str:
        return f'{{x={self.x},m={self.m},a={self.a},s={self.s}}}'
    
    def sum(self) -> int:
        return self.x + self.m + self.a + self.s
    
    def is_less_than(self, letter: chr, value: int) -> bool:
        match letter:
            case 'x': return self.x < value
            case 'm': return self.m < value
            case 'a': return self.a < value
            case 's': return self.s < value

    def is_greater_than(self, letter: chr, value: int) -> bool:
        match letter:
            case 'x': return self.x > value
            case 'm': return self.m > value
            case 'a': return self.a > value
            case 's': return self.s > value

class Helper:
    def parse(lines: list[str]) -> [dict, list[Part]]:
        workflows = {}
        parts = []
        for line in iter(lines):
            if line == "": 
                print("")
                continue
            if line[0] == '{':
                x, m, a, s = [int(p[2:]) for p in line[1:-1].split(',')]
                #print(f'x={x},m={m},a={a},s={s}')
                parts.append(Part(x, m, a, s))
            else:
                name, second = line[:-1].split('{')
                conditions = second.split(',')
                #print(f'{name}: {", ".join(conditions)}')
                workflows[name] = conditions
        return workflows, parts

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
# Part 1: 418498
# Part 2: 0
# Took 0.0020 seconds