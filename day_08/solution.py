import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return Helper.get_num_steps(lines, "AAA", ["ZZZ"])

class Part2:    
    @staticmethod
    def solution(lines: list[str]) -> int:
        a_nodes = Helper.get_nodes(lines, ending_in="A")
        z_nodes = Helper.get_nodes(lines, ending_in="Z")
        steps = [Helper.get_num_steps(lines, a, z_nodes) for a in a_nodes]
        return Helper.lcm(steps)

class Helper:
    def get_num_steps(lines: list[str], start: str, stop_nodes: list[str]) -> int:        
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
        while not any([current_node == x for x in stop_nodes]):
            if dirs[current_index] == 'R':
                current_node = nodes[current_node][1]
            else:
                current_node = nodes[current_node][0]
            current_index += 1
            if current_index == num_dirs: current_index = 0
            num_steps += 1
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
#Took 0.0387 seconds