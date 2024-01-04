import sys

def solve(lines: list[str]):
    grid = build_grid(lines)
    tilt_north(grid)
    #print_grid(grid)
    load = get_load(grid)
    print(load)

def pad_input(lines: list[str]) -> list[str]:
    width = len(lines[0]) + 2
    padded = []
    padded.append("#" * width)
    for line in iter(lines):
        padded.append("#" + line + "#")
    padded.append("#" * width)
    return padded

def build_grid(lines: list[str]) -> list[list[int]]:
    size = len(lines)
    grid = []
    for _ in range(size): grid.append([0] * size) # init
    for row in range(size):
        for col in range(size):
            if lines[row][col] == 'O':   grid[row][col] = 1
            elif lines[row][col] == '#': grid[row][col] = 2
    return grid

def print_grid(grid: list[list[int]]):
    size = len(grid)
    load = size - 2
    for row in range(1, size - 1):
        line = ""
        for col in range(1, size - 1):
            if grid[row][col] == 0: line += "."
            elif grid[row][col] == 1: line += "O"
            elif grid[row][col] == 2: line += "#"
        line += f" {load}"
        print(line)
        load -= 1

def tilt_north(grid: list[list[int]]):
    size = len(grid)
    for col in range(size - 1, 0, -1):
        for row in range(size - 1, 1, -1):
            if grid[row][col] != 1: continue # look for Os
            for x in range(row - 1, 0, -1):
                if grid[x][col] > 1: break # stop at #
                if grid[x][col] == 0: # swap . with O
                    grid[row][col] = 0
                    grid[x][col] = 1
                    row += -1

def get_load(grid: list[list[int]]) -> int:
    size = len(grid)
    sum = 0
    load = size - 2 # remove padding
    for row in range(1, size - 1):
        sum += load * grid[row].count(1)
        load -= 1
    return sum

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(pad_input(f))