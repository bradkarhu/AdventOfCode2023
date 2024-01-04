from functools import reduce
from math import gcd
from sys import argv

def solve(lines: list[str]):
    a_nodes = get_nodes(lines, ending_in="A")
    z_nodes = get_nodes(lines, ending_in="Z")
    steps = [get_num_steps(lines, a, z_nodes) for a in a_nodes]
    ans = lcm(steps)
    print(ans)

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
    return reduce(lambda a,b: a*b // gcd(a,b), numbers)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)