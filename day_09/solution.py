import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        sum = 0
        for line in iter(lines):
            sequence = [int(s) for s in line.split()]
            next = Helper.next_value(sequence)
            #print(f'{sequence} => {next}')
            sum += next
        return sum

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        sum = 0
        for line in iter(lines):
            sequence = [int(s) for s in line.split()]
            previous = Helper.previous_value(sequence)
            #print(f'{previous} => {sequence}')
            sum += previous
        return sum

class Helper:
    def next_value(sequence: list[int]) -> int:
        diffs = []
        for i in range(len(sequence) - 1):
            diff = sequence[i + 1] - sequence[i]
            diffs.append(diff)
        if any(x != 0 for x in diffs):
            return sequence[-1] + Helper.next_value(diffs)
        return sequence[-1]

    def previous_value(sequence: list[int]) -> int:
        diffs = []
        for i in range(len(sequence) - 1):
            diff = sequence[i + 1] - sequence[i]
            diffs.append(diff)
        if any(x != 0 for x in diffs):
            return sequence[0] - Helper.previous_value(diffs)
        return sequence[0]
    
tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
    
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 1980437560
#Part 2: 977
#Took 0.0067 seconds