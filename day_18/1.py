from sys import argv

def solve(lines: list[str]):
    x = 0
    y = 0
    perimeter = 0
    vertices = []
    for line in lines:
        dir, steps_s, _ = line.split()
        steps = int(steps_s)
        perimeter += steps
        vertices.append((x, y))
        #match dir: # requires Python 3.10+
        #    case 'R': x += steps
        #    case 'D': y += steps
        #    case 'L': x -= steps
        #    case 'U': y -= steps
        if dir == 'R': x += steps
        elif dir == 'D': y += steps
        elif dir == 'L': x -= steps
        elif dir == 'U': y -= steps
    #print(f'perimeter: {perimeter}')
    area = get_area(vertices)
    #print(f'area: {area}')
    vol = (area + perimeter) // 2 + 1
    print(vol)

# shoelace formula
def get_area(vertices) -> int:
    area = 0
    for i in range(len(vertices) - 1):
        area += vertices[i][0] * vertices[i + 1][1]
        area -= vertices[i][1] * vertices[i + 1][0]
    return area

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)