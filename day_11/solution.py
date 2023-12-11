import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return Helper.solve(lines)

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return Helper.solve(lines, extra_space=1000000-1)

class Helper:
    def print_lines(lines: list[str]):
        for line in iter(lines):
            print(line)
    
    def write_lines(lines: list[str], filename: str):      
        with open(filename, "w") as file:
            file.writelines("\r\n".join(lines))

    def find_galaxies(lines: list[str]) -> [list[tuple], list[bool], list[bool]]:
        galaxies = []
        rows = [0] * len(lines)
        columns = [0] * len(lines[0])
        for j in range(len(rows)):
            line = lines[j]
            for i in range(len(columns)):
                if line[i] == '#':
                    galaxies.append((j,i))
                    rows[j] += 1
                    columns[i] += 1
        return galaxies, rows, columns
    
    def solve(lines: list[str], extra_space: int = 1):
        galaxies, per_row, per_col = Helper.find_galaxies(lines)
        #print(galaxies)
        #print(per_row)
        #print(per_col)
        sum = 0
        for a in range(len(galaxies)):
            for b in range(a + 1, len(galaxies)):
                g1 = galaxies[a]
                g2 = galaxies[b]
                j1 = min(g1[0], g2[0])
                j2 = max(g1[0], g2[0])
                i1 = min(g1[1], g2[1])
                i2 = max(g1[1], g2[1])
                steps = 0
                for j in range(j1, j2):
                    if per_row[j] == 0: steps += extra_space
                    steps += 1
                for i in range(i1, i2):
                    if per_col[i] == 0: steps += extra_space
                    steps += 1
                #print(f'- Between galaxy {a+1} and galaxy {b+1}: {steps}')
                sum += steps
        return sum

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 10077850
#Part 2: 504715068438
#Took 0.5415 seconds