import time
from dijkstar import Graph, find_path

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:
        nj = len(lines)
        ni = len(lines[0])
        rg = range(1, 4)
        graph = Graph()        
        # add start node with zero loss edges to itself in each direction
        start = node(0,0,"")        
        graph.add_edge(start, node(0,0,"V"), (0, "V"))
        graph.add_edge(start, node(0,0,"H"), (0, "H"))
        for j in range(0, nj):
            for i in range(0, ni):
                loss = 0
                for x in rg: # left of current node
                    if i-x < 0: break
                    loss += int(lines[j][i-x])
                    graph.add_edge(node(j,i,"V"), node(j,i-x,"H"), (loss, "H"))
                    graph.add_edge(node(j,i,"H"), node(j,i-x,"H"), (loss, "H"))
                loss = 0
                for x in rg: # right of current node
                    if i+x >= ni: break
                    loss += int(lines[j][i+x])
                    graph.add_edge(node(j,i,"V"), node(j,i+x,"H"), (loss, "H"))
                    graph.add_edge(node(j,i,"H"), node(j,i+x,"H"), (loss, "H"))
                loss = 0
                for y in rg: # up from current node
                    if j-y < 0: break
                    loss += int(lines[j-y][i])
                    graph.add_edge(node(j,i,"V"), node(j-y,i,"V"), (loss, "V"))
                    graph.add_edge(node(j,i,"H"), node(j-y,i,"V"), (loss, "V"))
                loss = 0
                for y in rg: # down from current node
                    if j+y >= nj: break
                    loss += int(lines[j+y][i])
                    graph.add_edge(node(j,i,"V"), node(j+y,i,"V"), (loss, "V"))
                    graph.add_edge(node(j,i,"H"), node(j+y,i,"V"), (loss, "V"))
        #print(graph.node_count)
        #print(graph.edge_count)
        total_cost = None
        shortest_path = None
        for dir in ["H", "V"]:
            try:
                path = find_path(graph, start, node(nj-1,ni-1,dir), cost_func=Helper.cost_func)
                if total_cost is None or path.total_cost < total_cost:
                    shortest_path = path
                    total_cost = path.total_cost
            except:
                pass
        #print(shortest_path)
        return total_cost

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return 0

def node(j, i, dir):
    return f"{j}|{i}|{dir}"

class Helper:
    def cost_func(u, v, edge, prev_edge):
        loss, dir = edge
        if prev_edge:
            if prev_edge[1] == dir:
                return 1e7
        return loss

tic = time.perf_counter()
#with open("sample1.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 1099
#Part 2: 0
#Took 0.6561 seconds