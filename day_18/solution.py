import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        grid = []
        grid.append([0])
        x = 0
        y = 0
        for line in iter(lines):
            dir, steps_s, color_s = line.split()
            steps = int(steps_s)
            color = color_s[2:-1]
            color_hash = hash(color)
            if not color_hash in colors:
                colors[color_hash] = color
            if dir == 'U':
                for j in range(1, steps + 1):
                    if y - j < 0: 
                        Helper.grow_up(grid)
                    else: y -= 1
                    grid[y][x] = color_hash
            if dir == 'D':
                for j in range(1, steps + 1):
                    if y + j >= len(grid): 
                        Helper.grow_down(grid)
                    y += 1
                    grid[y][x] = color_hash
            elif dir == 'L':
                for i in range(1, steps + 1):
                    if x - i < 0: 
                        Helper.grow_left(grid)
                    else: x -= 1
                    grid[y][x] = color_hash
            elif dir == 'R':
                for i in range(1, steps + 1):
                    if x + i >= len(grid[0]):
                        Helper.grow_right(grid)
                    x += 1
                    grid[y][x] = color_hash
        # pad to avoid boundary checks while digging
        Helper.grow_up(grid)
        Helper.grow_down(grid)
        Helper.grow_left(grid)
        Helper.grow_right(grid)
        #Helper.print(grid)
        vol = Helper.dig(grid)
        return vol

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return 0

colors = {}

class Helper:
    def grow_up(grid: list[list[int]]):
        grid.insert(0, [0] * len(grid[0]))

    def grow_down(grid: list[list[int]]):
        grid.append([0] * len(grid[0]))

    def grow_left(grid: list[list[int]]):
        for l in grid: l.insert(0, 0)

    def grow_right(grid: list[list[int]]):
        for l in grid: l.append(0)
        
    def dig(grid: list[list[int]]) -> int:
        vol = 0
        ni = len(grid[0])
        for j in range(len(grid)):
            dir = -1
            # from day 10: if line[i] in ('|', 'F', '7'): dir *= -1 # flip checking
            for i in range(ni):
                if grid[j][i] != 0:
                    vol += 1
                    if grid[j][i-1] == 0 and grid[j][i+1] == 0:
                        dir *= -1 # flip checking if |
                    elif grid[j+1][i] != 0:
                        if grid[j][i-1] != 0 or grid[j][i+1] != 0:
                            dir *= -1 # flip checking if F or 7
                elif dir == 1:
                    vol += 1 # inside the loop
        return vol

    def print(grid: list[list[int]]):
        for j in range(len(grid)):
            line = ""
            for i in range(len(grid[0])):
                if grid[j][i] == 0: line += '.'
                else: line += '#'
            print(line)
        
tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
# Part 1: 50603
# Part 2: 0
# Took 0.0088 seconds