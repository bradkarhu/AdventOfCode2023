import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        grid = []
        grid.append([0])
        x = 0
        y = 0
        for line in iter(lines):
            dir, steps_s, _ = line.split()
            steps = int(steps_s)
            if dir == 'U':
                for j in range(1, steps + 1):
                    if y - j < 0: 
                        Helper.grow_up(grid)
                    else: y -= 1
                    grid[y][x] = 1
            if dir == 'D':
                for j in range(1, steps + 1):
                    if y + j >= len(grid): 
                        Helper.grow_down(grid)
                    y += 1
                    grid[y][x] = 1
            elif dir == 'L':
                for i in range(1, steps + 1):
                    if x - i < 0: 
                        Helper.grow_left(grid)
                    else: x -= 1
                    grid[y][x] = 1
            elif dir == 'R':
                for i in range(1, steps + 1):
                    if x + i >= len(grid[0]):
                        Helper.grow_right(grid)
                    x += 1
                    grid[y][x] = 1
        # pad to avoid boundary checks while digging
        Helper.grow_up(grid)
        Helper.grow_down(grid)
        Helper.grow_left(grid)
        Helper.grow_right(grid)
        #Helper.print(grid)
        vol = Helper.dig(grid)
        return vol

    # Can't brute force. Python gobbles > 100GB memory just for the sample.
    @staticmethod
    def optimized(lines: list[str]) -> int:
        x = 0
        y = 0
        perimeter = 0
        vertices = []
        for line in iter(lines):
            dir, steps_s, _ = line.split()
            steps = int(steps_s)
            perimeter += steps
            vertices.append((x, y))
            match dir:
                case 'R': x += steps
                case 'D': y += steps
                case 'L': x -= steps
                case 'U': y -= steps
        #print(f'perimeter: {perimeter}')
        area = Helper.area(vertices)
        #print(f'area: {area}')
        vol = (area + perimeter) // 2 + 1
        return vol
    
class Part2:
    # Can't brute force. Python gobbles > 100GB memory just for the sample.
    @staticmethod
    def solution(lines: list[str]) -> int:
        x = 0
        y = 0
        perimeter = 0
        vertices = []
        for line in iter(lines):
            _, _, instructions = line.split()
            instructions = instructions[2:-1]
            steps = int(instructions[:-1], 16)
            perimeter += steps
            vertices.append((x, y))
            match int(instructions[-1]):
                case 0: dir = 'R'; x += steps
                case 1: dir = 'D'; y += steps
                case 2: dir = 'L'; x -= steps
                case 3: dir = 'U'; y -= steps
            #print(f'#{instructions} = {dir} {steps}')            
        #print(f'perimeter: {perimeter}')
        area = Helper.area(vertices)
        #print(f'area: {area}')
        vol = (area + perimeter) // 2 + 1
        return vol

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

    # shoelace formula
    def area(vertices) -> int:
        area = 0
        for i in range(len(vertices) - 1):
            area += vertices[i][0] * vertices[i + 1][1]
            area -= vertices[i][1] * vertices[i + 1][0]
        return area

#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
tic = time.perf_counter()
print(f"Part 1: {Part1.solution(f)} (brute force)")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
# Part 1: 50603 (brute force)
# Took 0.0086 seconds
tic = time.perf_counter()
print(f"Part 1: {Part1.optimized(f)} (optimized)")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
# Part 1: 50603 (optimized)
# Part 2: 96556251590677
# Took 0.0006 seconds