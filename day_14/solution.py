import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        size = len(lines)
        load = 0
        #Helper.print_lines(lines)
        for col in range(size):
            data = [0] * size
            for row in range(size):
                c = lines[row][col]
                if c == 'O': data[size - row - 1] = 1
                elif c == '#': data[size - row - 1] = 2
            #print(data)
            changed = True
            while changed: changed = Helper.swap(data)
            #print(data)
            load += Helper.get_load(data)
        return load

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        matrix = Helper.build_matrix(lines)
        lookup = {}
        cycles = 1000000000
        stop_at_index = -1
        for i in range(cycles):
            Helper.swap_matrix(matrix)
            if stop_at_index != -1:
                if stop_at_index == i:
                    break
            else:
                hash = Helper.hash_matrix(matrix)
                if hash in lookup:
                    diff = i - lookup.get(hash)
                    remaining = cycles - i - 1
                    offset = remaining % diff
                    stop_at_index = i + offset
            lookup[hash] = i
        #Helper.print_matrix(matrix)
        load = Helper.get_load_matrix(matrix)
        return load

class Helper:
    def print_lines(lines: list[str]):
        for line in iter(lines):
            print(line)
    
    def pad_input(lines: list[str]) -> list[str]:
        width = len(lines[0]) + 2
        padded = []
        padded.append("#" * width)
        for line in iter(lines):
            padded.append("#" + line + "#")
        padded.append("#" * width)
        return padded
    
    def swap(data: list[int]) -> bool:
        changed = False
        for i in range(len(data) - 1):
            if data[i] != 1: continue # look for Os 
            for j in range(i + 1, len(data)):
                if data[j] == 2: break # stop at #
                if data[j] == 0: # swap . with O
                    data[i] = 0
                    data[j] = 1
                    i += 1
                    changed = True
        return changed
    
    def get_load(data: list[int]) -> int:
        load = 0
        for i in range(len(data)):
            if data[i] == 1: load += i
        return load
    
    # PART 2 METHODS
    
    def build_matrix(lines: list[str]) -> list[list[int]]:
        size = len(lines)
        matrix = []
        for _ in range(size): matrix.append([0] * size) # init
        for row in range(size):
            for col in range(size):
                if lines[row][col] == 'O':   matrix[row][col] = 1
                elif lines[row][col] == '#': matrix[row][col] = 2
        return matrix

    def print_matrix(matrix: list[list[int]]):
        size = len(matrix)
        load = size - 2
        for row in range(1, size - 1):
            line = ""
            for col in range(1, size - 1):
                if matrix[row][col] == 0: line += "."
                elif matrix[row][col] == 1: line += "O"
                elif matrix[row][col] == 2: line += "#"
            line += f" {load}"
            print(line)
            load -= 1
        print("")
    
    def swap_matrix(matrix: list[list[int]]):
        Helper.swap_matrix_ns(matrix, -1) # north
        Helper.swap_matrix_we(matrix, -1) # west
        Helper.swap_matrix_ns(matrix, 1)  # south
        Helper.swap_matrix_we(matrix, 1)  # east
    
    def swap_matrix_ns(matrix: list[list[int]], dir: int):
        size = len(matrix)
        for col in range(size) if dir == 1 else range(size - 1, 0, -1):
            for row in range(size - 1) if dir == 1 else range(size - 1, 1, -1):
                if matrix[row][col] != 1: continue # look for Os
                for x in range(row + 1, size) if dir == 1 else range(row - 1, 0, -1):
                    if matrix[x][col] > 1: break # stop at #
                    if matrix[x][col] == 0: # swap . with O
                        matrix[row][col] = 0
                        matrix[x][col] = 1
                        row += dir
    
    def swap_matrix_we(matrix: list[list[int]], dir: int):
        size = len(matrix)
        for row in range(size) if dir == 1 else range(size - 1, 0, -1):
            for col in range(size - 1) if dir == 1 else range(size - 1, 1, -1):
                if matrix[row][col] != 1: continue # look for Os
                for x in range(col + 1, size) if dir == 1 else range(col - 1, 0, -1):
                    if matrix[row][x] > 1: break # stop at #
                    if matrix[row][x] == 0: # swap . with O
                        matrix[row][col] = 0
                        matrix[row][x] = 1
                        col += dir
    
    def copy_matrix(matrix: list[list[int]]) -> list[list[int]]:
        return [l.copy() for l in matrix]
    
    def hash_matrix(matrix: list[list[int]]) -> int:
        return hash(tuple(Helper.hash_list(i) for i in matrix))

    def hash_list(list: list[int]) -> int:
        return hash(tuple(list))
    
    def get_load_matrix(matrix: list[list[int]]) -> int:
        size = len(matrix)
        sum = 0
        load = size - 2 # remove padding
        for row in range(1, size - 1):
            sum += load * matrix[row].count(1)
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