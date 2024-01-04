import sys
from queue import Queue
import numpy as np

num_steps = 64
target_steps = 26501365

def solve(lines: list[str]):
    size = len(lines)
    mid = size // 2
    grid, _ = build_grid(lines)
    steps = [mid*1+0, mid*3+1, mid*5+2] # mid*7+3, etc... for higher degree polynomials
    target = (target_steps - mid) // size
    x = [i for i in range(len(steps))]
    y = []
    while len(y) < len(x):
        try:
            start = (len(grid) // 2, len(grid) // 2) # start in the middle of the grid
            for i in range(len(y), len(steps)):
                num_steps = steps[i]
                last_steps = solve_grid(grid, start, num_steps, can_grow=True)
                y.append(len(last_steps))
        except:          
            grid = expand_grid(grid, 3)
    update_grid(grid, last_steps)
    #write_grid(grid, "output2.txt")
    coeffs = np.polyfit(x, y, 2)
    result = np.polyval(coeffs, target)
    ans = int(np.round(result, 0))
    print(ans)

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

def expand_grid(grid: list[list[int]], repeat: int) -> list[list[int]]:
    new_grid = []
    for _ in range(repeat):
        for row in grid:
            new_row = row * repeat
            new_grid.append(new_row)
    return new_grid

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

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)