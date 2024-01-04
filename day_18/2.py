import sys

def solve(lines: list[str]):
    x = 0
    y = 0
    perimeter = 0
    vertices = []
    for line in lines:
        _, _, instructions = line.split()
        instructions = instructions[2:-1]
        steps = int(instructions[:-1], 16)
        perimeter += steps
        vertices.append((x, y))
        i = int(instructions[-1])
        #match i: # requires Python 3.10+
        #    case 0: dir = 'R'; x += steps
        #    case 1: dir = 'D'; y += steps
        #    case 2: dir = 'L'; x -= steps
        #    case 3: dir = 'U'; y -= steps
        if i == 0: dir = 'R'; x += steps
        elif i == 1: dir = 'D'; y += steps
        elif i == 2: dir = 'L'; x -= steps
        elif i == 3: dir = 'U'; y -= steps
        #print(f'#{instructions} = {dir} {steps}')
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

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)