import re
import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return 0

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return 0

#class Helper:

tic = time.perf_counter()
with open("sample.txt", "r") as file:
#with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")