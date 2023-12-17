import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        grid = Grid(lines)
        grid.travel_east(0, 0)
        #grid.print()
        return grid.get_energized()

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        nj = len(lines)
        ni = len(lines[0])
        nums = []
        for i in range(ni):
            grid = Grid(lines)
            grid.travel_south(i, 0)
            nums.append(grid.get_energized())
        for i in range(ni):
            grid = Grid(lines)
            grid.travel_south(i, nj - 1)
            nums.append(grid.get_energized())
        for j in range(nj):
            grid = Grid(lines)
            grid.travel_east(0, j)
            nums.append(grid.get_energized())
        for j in range(nj):
            grid = Grid(lines)
            grid.travel_west(ni - 1, j)
            nums.append(grid.get_energized())
        #print(nums)
        return max(nums)

class Grid:
    def __init__(self, lines: list[str]):
        self.lines = lines
        self.nj = len(lines)
        self.ni = len(lines[0])
        self.grid = [[0] * self.ni for _ in range(self.nj)]

        # use lookups to avoid infinite recursion
        self.dash_map = {}
        self.pipe_map = {}
        self.fslash_north_map = {}
        self.fslash_south_map = {}
        self.fslash_west_map = {}
        self.fslash_east_map = {}
        self.bslash_north_map = {}
        self.bslash_south_map = {}
        self.bslash_west_map = {}
        self.bslash_east_map = {}
    
    def print(self):
        for row in range(self.nj):
            line = ""
            for col in range(self.ni):
                if self.grid[row][col] == 0: line += "."
                else: line += "#"
            print(line)
    
    def get_energized(self):
        num = 0
        for row in range(self.nj):
            for col in range(self.ni):
                if self.grid[row][col] > 0: num += 1
        return num

    def travel_north(self, i: int, j: int):
        while j >= 0:
            self.grid[j][i] += 1
            if self.lines[j][i] == '/':
                if not (j,i) in self.fslash_north_map:
                    self.fslash_north_map[(j,i)] = True
                    self.travel_east(i + 1, j)
                break
            elif self.lines[j][i] == '\\':
                if not (j,i) in self.bslash_north_map:
                    self.bslash_north_map[(j,i)] = True
                    self.travel_west(i - 1, j)
                break
            elif self.lines[j][i] == '-':
                if not (j,i) in self.dash_map:
                    self.dash_map[(j,i)] = True
                    self.travel_east(i + 1, j)
                    self.travel_west(i - 1, j)
                break
            j -= 1

    def travel_south(self, i: int, j: int):
        while j < len(self.lines):
            self.grid[j][i] += 1
            if self.lines[j][i] == '\\':
                if not (j,i) in self.bslash_south_map:
                    self.bslash_south_map[(j,i)] = True
                    self.travel_east(i + 1, j)
                break
            elif self.lines[j][i] == '/':
                if not (j,i) in self.fslash_south_map:
                    self.fslash_south_map[(j,i)] = True
                    self.travel_west(i - 1, j)
                break
            elif self.lines[j][i] == '-':
                if not (j,i) in self.dash_map:
                    self.dash_map[(j,i)] = True
                    self.travel_east(i + 1, j)
                    self.travel_west(i - 1, j)
                break
            j += 1
    
    def travel_west(self, i: int, j: int):
        while i >= 0:
            self.grid[j][i] += 1
            if self.lines[j][i] == '/':
                if not (j,i) in self.fslash_west_map:
                    self.fslash_west_map[(j,i)] = True
                    self.travel_south(i, j + 1)
                break
            elif self.lines[j][i] == '\\':
                if not (j,i) in self.bslash_west_map:
                    self.bslash_west_map[(j,i)] = True
                    self.travel_north(i, j - 1)
                break
            elif self.lines[j][i] == '|':
                if not (j,i) in self.pipe_map:
                    self.pipe_map[(j,i)] = True
                    self.travel_south(i, j + 1)
                    self.travel_north(i, j - 1)
                break
            i -= 1

    def travel_east(self, i: int, j: int):
        while i < len(self.lines[0]):
            self.grid[j][i] += 1
            if self.lines[j][i] == '\\':
                if not (j,i) in self.bslash_east_map:
                    self.bslash_east_map[(j,i)] = True
                    self.travel_south(i, j + 1)
                break
            elif self.lines[j][i] == '/':
                if not (j,i) in self.fslash_east_map:
                    self.fslash_east_map[(j,i)] = True
                    self.travel_north(i, j - 1)
                break
            elif self.lines[j][i] == '|':
                if not (j,i) in self.pipe_map:
                    self.pipe_map[(j,i)] = True
                    self.travel_south(i, j + 1)
                    self.travel_north(i, j - 1)
                break
            i += 1

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 7415
#Part 2: 7943
#Took 0.4617 seconds