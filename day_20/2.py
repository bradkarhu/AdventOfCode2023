import re
import sys
from queue import Queue
from math import gcd
from functools import reduce 

class Pulse:
    def __init__(self, source, destination, value):
        self.source = source
        self.destination = destination
        self.value = value

class Module:
    def __init__(self, name):
        self.name = name
        self.sources = []
        self.destinations = []
    
    def initialize(self):
        pass
    
    def send_pulse(self, source, value) -> list[Pulse]:        
        return [Pulse(self, destination, value) for destination in self.destinations]

class Button(Module): pass
class Broadcaster(Module): pass
class Output(Module): pass

class FlipFlop(Module):
    def initialize(self):
        self.memory = False

    def send_pulse(self, source, value) -> list[Pulse]:
        if value == True: return []
        value = self.memory = not self.memory
        return super().send_pulse(source, value)
    
class Conjunction(Module):
    def initialize(self):
        self.memory = {s.name: False for s in self.sources}

    def send_pulse(self, source, value) -> list[Pulse]:
        self.memory[source.name] = value
        value = any([v == False for _, v in self.memory.items()])
        return super().send_pulse(source, value)

def solve(lines: list[str]):
    modules = parse_modules(lines)
    # get starting modules
    broadcaster = modules["broadcaster"]
    button = Button("button")
    button.destinations.append(broadcaster)
    # get ending module
    rx = modules["rx"]
    # get parent
    parent = rx.sources[0] # &zg
    # get grandparents
    grandparents = parent.sources # &vm, &lm, &jd, &fv
    grandparent_lows = {}
    # initialize memory
    for _, m in modules.items(): m.initialize()
    q = Queue()
    i = 0
    while True:
        i += 1
        q.put(Pulse(button, broadcaster, False))
        while not q.empty():
            p = q.get()
            if not p.value and p.destination in grandparents:
                if not p.destination in grandparent_lows:
                    #print(f'{p.source.name} -{"high" if p.value else "low"}-> {p.destination.name} at {i}')
                    grandparent_lows[p.destination] = i
            for p2 in p.destination.send_pulse(p.source, p.value):
                q.put(p2)
        if len(grandparents) == len(grandparent_lows):
            numbers = [v for _, v in grandparent_lows.items()]
            break
    ans = lcm(numbers)
    print(ans)

def parse_modules(lines: list[str]) -> dict:
    modules = {}
    destinations = {}
    for line in iter(lines):
        kind = line[0]
        split = re.split('[\s,]+', line)
        name = split[0]
        if kind == '%':
            name = name[1:]
            modules[name] = FlipFlop(name)
        elif kind == '&':
            name = name[1:]
            modules[name] = Conjunction(name) 
        elif kind == "b":
            modules[name] = Broadcaster(name)
        destinations[name] = split[2:]
    for k,v in destinations.items():
        source = modules[k]
        for name in v:
            if not name in modules:
                modules[name] = Output(name)
            destination = modules[name]
            #print(f'adding {destination.name} to {source.name}')
            destination.sources.append(source)
            source.destinations.append(destination)
    return modules

def lcm(numbers):   
    return reduce(lambda a,b: a*b // gcd(a,b), numbers)

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)