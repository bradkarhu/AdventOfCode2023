from dijkstar import Graph, find_path
import sys

def solve(lines: list[str]):
    rg = range(1, 4)
    min_steps = 1
    nj = len(lines)
    ni = len(lines[0])
    graph = Graph()
    for j in range(0, nj):
        for i in range(0, ni):
            loss = 0
            for x in rg:  # left of current node
                if i-x < 0: break
                loss += int(lines[j][i-x])
                if x < min_steps: continue
                graph.add_edge((j, i, "V"), (j, i-x, "H"), (loss, "H"))
                graph.add_edge((j, i, "H"), (j, i-x, "H"), (loss, "H"))
            loss = 0
            for x in rg:  # right of current node
                if i+x >= ni: break
                loss += int(lines[j][i+x])
                if x < min_steps: continue
                graph.add_edge((j, i, "V"), (j, i+x, "H"), (loss, "H"))
                graph.add_edge((j, i, "H"), (j, i+x, "H"), (loss, "H"))
            loss = 0
            for y in rg:  # up from current node
                if j-y < 0: break
                loss += int(lines[j-y][i])
                if y < min_steps: continue
                graph.add_edge((j, i, "V"), (j-y, i, "V"), (loss, "V"))
                graph.add_edge((j, i, "H"), (j-y, i, "V"), (loss, "V"))
            loss = 0
            for y in rg:  # down from current node
                if j+y >= nj: break
                loss += int(lines[j+y][i])
                if y < min_steps: continue
                graph.add_edge((j, i, "V"), (j+y, i, "V"), (loss, "V"))
                graph.add_edge((j, i, "H"), (j+y, i, "V"), (loss, "V"))
    #print(graph.node_count)
    #print(graph.edge_count)        
    # add start and end nodes with zero-loss edges to themselves in each direction
    start = (0, 0, "#")
    graph.add_edge(start, (0, 0, "V"), (0, "V"))
    graph.add_edge(start, (0, 0, "H"), (0, "H"))
    end = (nj-1, ni-1, "#")
    graph.add_edge((nj-1, ni-1, "V"), end, (0, "#"))
    graph.add_edge((nj-1, ni-1, "H"), end, (0, "#"))
    # find path with lowest heat loss from start to end
    path = find_path(graph, start, end, cost_func=cost)
    #print(path)
    print(path.total_cost)

def cost(u, v, edge, prev_edge):
    loss, dir = edge
    if prev_edge:
        # must flip direction from previous run
        if prev_edge[1] == dir:
            return 1e7
    return loss

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)