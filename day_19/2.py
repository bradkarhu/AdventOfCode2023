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

class Ranges:
    def __init__(self, name: str, start: int, end: int):
        self.name = name
        self.ranges = [range(start, end) for _ in order]

    def fork_off_less_than(self, letter: chr, value: int):
        index = order.index(letter)
        r = self.ranges[index]
        fork = copy.deepcopy(self)
        r1 = range(r.start, value)
        r2 = range(value, r.stop)
        self.ranges[index] = r2
        fork.ranges[index] = r1
        return fork

    def fork_off_greater_than(self, letter: chr, value: int):
        index = order.index(letter)
        r = self.ranges[index]
        fork = copy.deepcopy(self)
        r1 = range(r.start, value + 1)
        r2 = range(value + 1, r.stop)
        self.ranges[index] = r1
        fork.ranges[index] = r2
        return fork

    def product(self) -> int:
        return prod([r.stop - r.start for r in self.ranges])

order = ['x', 'm', 'a', 's']

def solve(lines: list[str]):
    workflows, _ = parse(lines, break_at_empty_line=True)
    accepted = 0
    rejected = 0
    q = Queue()
    q.put(Ranges("in", 1, 4001))
    while not q.empty():
        r = q.get()
        name = r.name
        while name in workflows:
            #print(f'{name}: {r.product():,}')
            conditions = workflows[name]
            for condition in conditions:
                if "<" in condition:
                    c, v, w = re.split('[<:]', condition)
                    f = r.fork_off_less_than(c, int(v))
                    f.name = w
                    q.put(f)
                elif ">" in condition:
                    c, v, w = re.split('[>:]', condition)
                    f = r.fork_off_greater_than(c, int(v))
                    f.name = w
                    q.put(f)
                else:
                    name = condition
                    break
        if name == "A":
            accepted += r.product()
        elif name == "R":
            rejected += r.product()
        else:
            raise Exception(f'unknown workflow: {name}')
    #print(f'R: {rejected:,}')
    #print(f'A: {accepted:,}')
    print(accepted)

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