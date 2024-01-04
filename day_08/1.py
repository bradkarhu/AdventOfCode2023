from sys import argv

def solve(lines: list[str]):
    ans = get_num_steps(lines, "AAA", ["ZZZ"])
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

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)