import sys
import time
from queue import Queue

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        grid, start = Helper.build_grid(lines)
        q = Queue()
        q.put((start, 0))
        dirs = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        lookup = {} # key: (row, col), value: steps
        while not q.empty():
            (row, col), steps = q.get()
            if steps <= num_steps:
                for dy, dx in dirs:
                    y = row + dy
                    x = col + dx
                    next = (y, x)
                    if grid[y][x] == 0 and not next in lookup:
                        lookup[next] = steps + 1
                        q.put((next, steps + 1))
        last_steps = set()
        for index, steps in lookup.items():
            if (index[0] + index[1]) % 2 == num_steps % 2:
                last_steps.add(index)
        reached = len(last_steps)
        Helper.update_grid(grid, last_steps)        
        Helper.print(grid)
        return reached

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return 0

class Helper:
    def pad_input(lines: list[str]) -> list[str]:
        width = len(lines[0]) + 2
        padded = []
        padded.append("#" * width)
        for line in iter(lines):
            padded.append("#" + line + "#")
        padded.append("#" * width)
        return padded

    def build_grid(lines: list[str]) -> [list[list[int]], tuple]:
        size = len(lines)
        grid = []
        start = (0, 0)
        for _ in range(size): grid.append([0] * size) # init
        for row in range(size):
            for col in range(size):
                if lines[row][col] == '#': grid[row][col] = 2
                elif lines[row][col] == 'S': start = (row, col)
        return grid, start

    def update_grid(grid: list[list[int]], last_steps: set[tuple]):
        for row, col in last_steps:
            grid[row][col] = 1
    
    def print(grid: list[list[int]]):
        size = len(grid)
        for row in range(1, size - 1):
            line = ""
            for col in range(1, size - 1):
                if grid[row][col] == 0: line += "."
                elif grid[row][col] == 1: line += "O"
                elif grid[row][col] == 2: line += "#"
            print(line)

num_steps = int(sys.argv[1]) if len(sys.argv) > 1 else 64
tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
padded = Helper.pad_input(f)
print(f"Part 1: {Part1.solution(padded)}")
print(f"Part 2: {Part2.solution(padded)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
# Part 1: 3532
# Part 2: 0
# Took 0.0161 seconds