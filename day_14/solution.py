import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        grid = Helper.build_grid(lines)
        Helper.tilt_north(grid)
        #Helper.print(grid)
        return Helper.get_load(grid)

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        grid = Helper.build_grid(lines)
        lookup = {}
        cycles = 1000000000
        stop_at_index = -1
        for i in range(cycles):
            Helper.cycle(grid)
            if stop_at_index != -1:
                if stop_at_index == i:
                    break
            else:
                hash = Helper.hash(grid)
                if hash in lookup:
                    diff = i - lookup.get(hash)
                    remaining = cycles - i - 1
                    offset = remaining % diff
                    stop_at_index = i + offset
            lookup[hash] = i
        #Helper.print(grid)
        return Helper.get_load(grid)

class Helper:
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

    def print(grid: list[list[int]]):
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

    def cycle(grid: list[list[int]]):
        Helper.tilt_north(grid)
        Helper.tilt_west(grid)
        Helper.tilt_south(grid)
        Helper.tilt_east(grid)

    def tilt_north(grid: list[list[int]]): Helper.tilt_north_south(grid, -1)
    def tilt_south(grid: list[list[int]]): Helper.tilt_north_south(grid, 1)
    def tilt_west(grid: list[list[int]]): Helper.tilt_east_west(grid, -1)
    def tilt_east(grid: list[list[int]]): Helper.tilt_east_west(grid, 1)

    def tilt_north_south(grid: list[list[int]], dir: int):
        size = len(grid)
        for col in range(size) if dir == 1 else range(size - 1, 0, -1):
            for row in range(size - 1) if dir == 1 else range(size - 1, 1, -1):
                if grid[row][col] != 1: continue # look for Os
                for x in range(row + 1, size) if dir == 1 else range(row - 1, 0, -1):
                    if grid[x][col] > 1: break # stop at #
                    if grid[x][col] == 0: # swap . with O
                        grid[row][col] = 0
                        grid[x][col] = 1
                        row += dir

    def tilt_east_west(grid: list[list[int]], dir: int):
        size = len(grid)
        for row in range(size) if dir == 1 else range(size - 1, 0, -1):
            for col in range(size - 1) if dir == 1 else range(size - 1, 1, -1):
                if grid[row][col] != 1: continue # look for Os
                for x in range(col + 1, size) if dir == 1 else range(col - 1, 0, -1):
                    if grid[row][x] > 1: break # stop at #
                    if grid[row][x] == 0: # swap . with O
                        grid[row][col] = 0
                        grid[row][x] = 1
                        col += dir

    def hash(grid: list[list[int]]) -> int:
        return hash( tuple( tuple(i) for i in grid ) )

    def get_load(grid: list[list[int]]) -> int:
        size = len(grid)
        sum = 0
        load = size - 2 # remove padding
        for row in range(1, size - 1):
            sum += load * grid[row].count(1)
            load -= 1
        return sum

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
padded = Helper.pad_input(f)
print(f"Part 1: {Part1.solution(padded)}")
print(f"Part 2: {Part2.solution(padded)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 112773
#Part 2: 98894
#Took 0.4148 seconds