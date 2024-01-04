from sys import argv

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

def solve(lines: list[str]):
    grid = Grid(lines)
    grid.travel_east(0, 0)
    #grid.print()
    total = grid.get_energized()
    print(total)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)