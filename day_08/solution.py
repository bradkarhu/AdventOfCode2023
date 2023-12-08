import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return Helper.get_num_steps(lines, "AAA", "ZZZ")

class Part2:    
    @staticmethod
    def solution(lines: list[str]) -> int:
        starting_nodes = Helper.get_nodes(lines, ending_in="A")
        stopping_nodes = Helper.get_nodes(lines, ending_in="Z")
        min_steps = []
        for i in range(len(starting_nodes)):
            steps = []            
            for j in range(len(stopping_nodes)):
                steps.append(Helper.get_num_steps(lines, starting_nodes[i], stopping_nodes[j], limit=100000))
            min_steps.append(min(steps))
        return Helper.lcm(min_steps)

class Helper:
    def get_num_steps(lines: list[str], start: str, stop: str, limit: int = -1) -> int:        
        dirs = lines[0]
        num_dirs = len(dirs)
        nodes = {}
        for i in range(2, len(lines)):
            key = lines[i][0:3]
            left = lines[i][7:10]
            right = lines[i][12:15]
            nodes[key] = (left, right)
        current_index = 0
        current_node = start
        num_steps = 0
        while current_node != stop:
            if dirs[current_index] == 'R':
                current_node = nodes[current_node][1]
            else:
                current_node = nodes[current_node][0]
            current_index += 1
            if current_index == num_dirs: current_index = 0
            num_steps += 1
            if num_steps == limit: break # needed for part 2, if A never reaches Z
        return num_steps
    
    def get_nodes(lines: list[str], ending_in: str) -> int:
        nodes = []
        for i in range(2, len(lines)):
            if lines[i][2] == ending_in:                
                nodes.append(lines[i][0:3])
        return nodes
    
    def lcm(numbers):
        from math import gcd
        from functools import reduce    
        return reduce(lambda a,b: a*b // gcd(a,b), numbers)

tic = time.perf_counter()
#with open("sample3.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 15871
#Part 2: 11283670395017
#Took 0.2383 seconds