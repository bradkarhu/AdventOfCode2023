import re
import time
from queue import Queue

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        modules = Helper.parse_modules(lines)
        # get starting modules
        broadcaster = modules["broadcaster"]
        button = Button("button")
        button.destinations.append(broadcaster)
        # initialize memory
        for _, m in modules.items(): m.initialize()
        num_low = 0
        num_high = 0
        q = Queue()
        for _ in range(1000):
            q.put(Pulse(button, broadcaster, False))
            while not q.empty():
                p = q.get()
                #print(f'{p.source.name} -{"high" if p.value else "low"}-> {p.destination.name}')
                if p.value: num_high += 1
                else: num_low += 1
                for p2 in p.destination.send_pulse(p.source, p.value):
                    q.put(p2)
        #print(f'{num_low} low pulses and {num_high} high pulses are sent')
        return num_low * num_high

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return 0

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
class Generic(Module): pass

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

class Helper:
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
                destination = modules[name] if name in modules else Generic(name)
                #print(f'adding {destination.name} to {source.name}')
                destination.sources.append(source)
                source.destinations.append(destination)
        return modules

tic = time.perf_counter()
#with open("sample1.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
# Part 1: 825896364
# Part 2: 0
# Took 0.0928 seconds