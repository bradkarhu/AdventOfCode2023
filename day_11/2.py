from sys import argv

def solve(lines: list[str]):
    galaxies, per_row, per_col = find_galaxies(lines)
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
                if per_row[j] == 0: steps += 999999
                steps += 1
            for i in range(i1, i2):
                if per_col[i] == 0: steps += 999999
                steps += 1
            #print(f'- Between galaxy {a+1} and galaxy {b+1}: {steps}')
            sum += steps
    print(sum)

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

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)