import copy
import re
import sys, getopt
import time
from queue import Queue

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        grid, start = Helper.build_grid(lines)
        #mask = Helper.build_mask(grid)
        #mask[start[0]][start[1]] = True
        q = Queue()
        q.put([start])
        dirs = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        last_steps = set()
        cycle_steps = set()
        while not q.empty():
            steps = q.get()
            current = steps[-1]
            if len(steps) > num_steps:
                last_steps.add(current)
            else:
                for dir in dirs:
                    next = tuple(sum(x) for x in zip(current, dir))
                    if grid[next[0]][next[1]] == 0:
                        if next in steps:                            
                            #print(f'skipping {next}')
                            first_index = steps.index(next)
                            last_index = len(steps)
                            diff = last_index - first_index
                            remaining = num_steps - last_index 
                            if remaining % diff == 0:
                                #print(f'cycle found at {next} from {first_index} to {last_index}')                
                                cycle_steps.add(next)
                            continue
                        #print(f'stepping from {current} to {next}')
                        #mask[next[0]][next[1]] = True
                        next_steps = steps.copy()
                        next_steps.append(next)
                        q.put(next_steps)
        
        last_steps |= cycle_steps # last_steps.union(cycle_steps)
        Helper.update_grid(grid, last_steps)
        reached = len(last_steps)
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
        for current in last_steps:
            grid[current[0]][current[1]] = 1
    
    def build_mask(grid: list[list[int]]) -> list[list[bool]]:
        mask = []
        for row in grid: 
            mask.append([val > 0 for val in row])
        return mask
    
    def apply_mask(grid: list[list[int]], mask: list[list[bool]]) -> int:
        size = len(grid)
        reached = 0
        for row in range(size):
            for col in range(size):
                if grid[row][col] == 0 and mask[row][col]:
                    grid[row][col] = 1
                    reached += 1
        return reached
    
    def print(grid: list[list[int]]):
        size = len(grid)
        for row in range(1, size - 1):
            line = ""
            for col in range(1, size - 1):
                if grid[row][col] == 0: line += "."
                elif grid[row][col] == 1: line += "O"
                elif grid[row][col] == 2: line += "#"
            print(line)
    
    def walk(grid: list[list[int]], mask: list[list[bool]], index: tuple, steps: list[tuple], stop_at: int):
        if len(steps) >= stop_at: return
        steps.copy()


num_steps = int(sys.argv[1]) if len(sys.argv) > 1 else 64
        
tic = time.perf_counter()
with open("sample.txt", "r") as file:
#with open("input.txt", "r") as file:
    f = file.read().splitlines()
padded = Helper.pad_input(f)
print(f"Part 1: {Part1.solution(padded)}")
print(f"Part 2: {Part2.solution(padded)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")

# sample.txt = 38