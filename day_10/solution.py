import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        s_index = Helper.get_s(lines)
        next1 = Helper.get_next(lines, s_index, [-1,-1])
        next2 = Helper.get_next(lines, s_index, next1)
        previous1 = s_index
        previous2 = s_index
        steps = 0
        while True:
            steps += 1
            a = Helper.get_next(lines, next1, previous1)
            Helper.set_char(lines, previous1, '*')
            b = Helper.get_next(lines, next2, previous2)
            Helper.set_char(lines, previous2, '*')
            if a == b: 
                Helper.set_char(lines, a, '*')
                Helper.set_char(lines, next1, '*')
                Helper.set_char(lines, next2, '*')
                break
            previous1 = next1
            previous2 = next2
            next1 = a
            next2 = b
        Helper.write_lines(lines, "progress.txt")
        return steps + 1

class Part2:
    @staticmethod
    def solution(lines: list[str], mask: list[str]) -> int:
        s_index = Helper.get_s(lines)  
        Helper.replace_s(lines, s_index)
        num_tiles = 0
        for j in range(len(lines)):
            line = lines[j]
            line_mask = mask[j]
            dir = -1
            for i in range(len(line)):
                if line_mask[i] == '%': continue
                elif line_mask[i] == '*': # rely on replacement in part 1
                    if line[i] in ('-', 'L', 'J'): continue
                    if line[i] in ('|', 'F', '7'): dir *= -1 # flip checking
                elif dir == 1: # found a tile
                    Helper.set_char(lines, [j,i], '#')
                    num_tiles += 1
        Helper.write_lines(lines, "progress2.txt")
        return num_tiles

class Helper:
    def pad_input(lines: list[str]) -> list[str]:
        width = len(lines[0]) + 4
        padded = []
        padded.append("%" * width)
        for line in iter(lines):
            padded.append("%." + line + ".%")
        padded.append("%" * width)
        return padded
    
    def print_lines(lines: list[str]):
        for line in iter(lines):
            print(line)
    
    def write_lines(lines: list[str], filename: str):      
        with open(filename, "w") as file:
            file.writelines("\r\n".join(lines))
    
    def get_s(lines: list[str]) -> [int, int]:
        for j in range(len(lines)):
            line = lines[j]
            for i in range(len(line)):
                if line[i] == 'S': return j,i
    
    def replace_s(lines: list[str], s: [int, int]) -> chr:
        a = Helper.get_next(lines, s, [-1,-1])
        b = Helper.get_next(lines, s, a)
        dy = b[0] - a[0]
        dx = b[1] - a[1]        
        c = 'S'
        if dy == 2: c = '|'
        elif dx == 2: c = '-'
        elif dy == -1 and dx == -1: c = 'L'
        elif dy == -1 and dx == 1: c = 'J'
        elif dy == 1 and dx == -1: c = 'F'
        elif dy == 1 and dx == 1: c = '7'
        Helper.set_char(lines, s, c)

    def get_char(lines: list[str], index: [int, int]) -> str:
        return lines[index[0]][index[1]]
    
    def set_char(lines: list[str], index: [int, int], value: chr):
        lines[index[0]] = lines[index[0]][:index[1]] + value + lines[index[0]][index[1]+1:]

    def get_next(lines: list[str], start: [int, int], skip: [int, int]) -> [int, int]:
        j = start[0]
        i = start[1]
        current = lines[j][i] # supports: - | F L J 7 S
        if current == '-' or current == 'S':
            if skip != (j,i-1) and lines[j][i-1] in ('-', 'F', 'L'): return j,i-1
            if skip != (j,i+1) and lines[j][i+1] in ('-', 'J', '7'): return j,i+1
        if current == '|' or current == 'S':
            if skip != (j-1,i) and lines[j-1][i] in ('|', 'F', '7'): return j-1,i
            if skip != (j+1,i) and lines[j+1][i] in ('|', 'J', 'L'): return j+1,i
        if current == 'F' or current == 'S':
            if skip != (j,i+1) and lines[j][i+1] in ('-', 'J', '7'): return j,i+1
            if skip != (j+1,i) and lines[j+1][i] in ('|', 'J', 'L'): return j+1,i
        if current == 'L' or current == 'S':
            if skip != (j,i+1) and lines[j][i+1] in ('-', 'J', '7'): return j,i+1
            if skip != (j-1,i) and lines[j-1][i] in ('|', 'F', '7'): return j-1,i
        if current == 'J' or current == 'S':
            if skip != (j,i-1) and lines[j][i-1] in ('-', 'F', 'L'): return j,i-1
            if skip != (j-1,i) and lines[j-1][i] in ('|', 'F', '7'): return j-1,i
        if current == '7' or current == 'S':
            if skip != (j,i-1) and lines[j][i-1] in ('-', 'F', 'L'): return j,i-1
            if skip != (j+1,i) and lines[j+1][i] in ('|', 'J', 'L'): return j+1,i
        else:
            raise Exception(f"[get_next] should not be able to get here: {current} {start}")

tic = time.perf_counter()
#with open("sample4.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
part1 = Helper.pad_input(f)
part2 = Helper.pad_input(f)
print(f"Part 1: {Part1.solution(part1)}")
print(f"Part 2: {Part2.solution(part2, part1)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 6717
#Part 2: 381
#Took 0.0099 seconds