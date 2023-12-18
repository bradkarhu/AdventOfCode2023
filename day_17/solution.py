import time
from dijkstar import Graph, find_path

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        nj = len(lines)
        ni = len(lines[0])
        
        graph = Graph()
        for j in range(nj):
            for i in range(ni):
                loss = 0
                for ii in range(i - 1, i - 4, -1): # left of current node
                    if ii < 0: break
                    loss += int(lines[j][ii])
                    graph.add_edge((j,i), (j,ii), (loss, (0, -1)))
                loss = 0
                for ii in range(i + 1, i + 4): # right of current node
                    if ii >= ni: break
                    loss += int(lines[j][ii])
                    graph.add_edge((j,i), (j,ii), (loss, (0, 1)))
                loss = 0
                for jj in range(j - 1, j - 4, -1): # up from current node
                    if jj < 0: break
                    loss += int(lines[jj][i])
                    graph.add_edge((j,i), (jj,i), (loss, (-1, 0)))
                loss = 0
                for jj in range(j + 1, j + 4): # down from current node
                    if jj >= nj: break
                    loss += int(lines[jj][i])
                    graph.add_edge((j,i), (jj,i), (loss, (1, 0)))
        print(graph.node_count)
        print(graph.edge_count)
        
        path = find_path(graph, (0,0), (nj-1,ni-1), cost_func=Helper.cost_func)
        print(path)
        Helper.print(lines, path)
        return 0

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return 0

class Helper:
    def cost_func(u, v, edge, prev_edge):
        loss, dir = edge
        if prev_edge:
            if prev_edge[1] == dir:
                return 1e7
            # if prev_edge[1][0] == dir[0] and prev_edge[1][1] != dir[1]:
            #     return 1e7        
            # if prev_edge[1][0] != dir[0] and prev_edge[1][1] == dir[1]:
            #     return 1e7
        return loss
    
    def print(lines: list[str], path):
        nj = len(lines)
        ni = len(lines[0])
        grid = [['0'] * ni for _ in range(nj)]
        for j in range(nj):
            for i in range(ni):
                grid[j][i] = lines[j][i]
        for n in range(1, len(path.nodes)):
            prev_node = path.nodes[n-1]
            node = path.nodes[n]
            c = '#'
            dir = 1
            if prev_node[0] < node[0]: c = 'v'
            elif prev_node[0] > node[0]: c = '^'; dir = -1
            elif prev_node[1] < node[1]: c = '>'
            elif prev_node[1] > node[1]: c = '<'; dir = -1
            for j in range(prev_node[0]+dir, node[0]+dir, dir):
                grid[j][node[1]] = c            
            for i in range(prev_node[1]+dir, node[1]+dir, dir):
                grid[node[0]][i] = c
        for j in range(nj):
            print(''.join(grid[j]))

tic = time.perf_counter()
with open("sample1.txt", "r") as file:
#with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")

# 1163 too high