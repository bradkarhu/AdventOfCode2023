import copy
import re
from sys import argv
from queue import Queue
from math import prod

class Part:
    def __init__(self, xmas):
        self.xmas = xmas

    def to_string(self) -> str:
        return f'{{x={self.xmas[0]},m={self.xmas[1]},a={self.xmas[2]},s={self.xmas[3]}}}'

    def sum(self) -> int:
        return sum(self.xmas)

    def is_less_than(self, letter: chr, value: int) -> bool:
        index = order.index(letter)
        return self.xmas[index] < value

    def is_greater_than(self, letter: chr, value: int) -> bool:
        index = order.index(letter)
        return self.xmas[index] > value

order = ['x', 'm', 'a', 's']

def solve(lines: list[str]):
    workflows, parts = parse(lines)
    total = 0
    for p in parts:
        #output = f"{p.to_string()}: "
        name = "in"
        while name in workflows:
            #output += f"{name} -> "
            conditions = workflows[name]
            for condition in conditions:
                if "<" in condition:
                    c, v, w = re.split('[<:]', condition)
                    if p.is_less_than(c, int(v)):
                        name = w
                        break
                elif ">" in condition:
                    c, v, w = re.split('[>:]', condition)
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
    print(total)

def parse(lines: list[str], break_at_empty_line: bool = False) -> [dict, list[Part]]:
    workflows = {}
    parts = []
    for line in iter(lines):
        if line == "":
            if break_at_empty_line: break
            continue
        if line[0] == '{':
            part = Part([int(p[2:]) for p in line[1:-1].split(',')])
            #print(part.to_string())
            parts.append(part)
        else:
            name, second = line[:-1].split('{')
            conditions = second.split(',')
            #print(f'{name}: {", ".join(conditions)}')
            workflows[name] = conditions
    return workflows, parts

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)