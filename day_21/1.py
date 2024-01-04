from sys import argv
from queue import Queue
import numpy as np

num_steps = 64

def solve(lines: list[str]):
    grid, start = build_grid(lines)
    last_steps = solve_grid(grid, start, num_steps, can_grow=False)
    update_grid(grid, last_steps)
    #write_grid(grid, "output1.txt")
    #print_grid(grid)
    print(len(last_steps))

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

def solve_grid(grid: list[list[int]], start: tuple, num_steps: int, can_grow: bool) -> set:
    size = len(grid)
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
                if y < 0 or y >= size: 
                    if can_grow: raise ("increase size of the grid")
                    continue
                if x < 0 or x >= size: 
                    if can_grow: raise ("increase size of the grid")
                    continue
                next = (y, x)
                if grid[y][x] == 0 and not next in lookup:
                    lookup[next] = steps + 1
                    q.put((next, steps + 1))
    last_steps = set()
    for index, steps in lookup.items():
        if (index[0] + index[1]) % 2 == num_steps % 2:
            last_steps.add(index)
    return last_steps

def update_grid(grid: list[list[int]], last_steps: set[tuple]):
    for row, col in last_steps:
        grid[row][col] = 1

def print_grid(grid: list[list[int]]):
    size = len(grid)
    rg = range(size)
    for row in rg:
        line = ""
        for col in rg:
            if grid[row][col] == 0: line += "."
            elif grid[row][col] == 1: line += "O"
            elif grid[row][col] == 2: line += "#"
        print(line)

def write_grid(grid: list[list[int]], filename: str):
    size = len(grid)
    rg = range(size)
    with open(filename, "w") as file:
        for row in rg:
            line = ""
            for col in rg:
                if grid[row][col] == 0: line += "."
                elif grid[row][col] == 1: line += "O"
                elif grid[row][col] == 2: line += "#"
            file.write(line + "\r\n")

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)