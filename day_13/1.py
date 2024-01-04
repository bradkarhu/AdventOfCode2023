from sys import argv

def solve(lines: list[str]):
    lineset = []
    total = 0
    setcount = 0
    for r in range(len(lines)):
        if lines[r] == "": 
            setcount += 1
            rows_above = find_horizontal_reflection(lineset)
            cols_left = find_vertical_reflection(lineset)
            sum = 100 * rows_above + cols_left
            #print(f'set {setcount} = {sum} ({cols_left} cols, {rows_above} rows)')
            total += sum
            lineset.clear()
        else:
            lineset.append(lines[r])
    print(total)

def find_horizontal_reflection(lines: list[str]) -> int:
    for i in range(len(lines) - 1):
        if lines[i] == lines[i+1]:
            if is_reflection(lines, i, i + 1):
                return i + 1
    return 0

def find_vertical_reflection(lines: list[str]) -> int:
    rotated = []
    cols = len(lines[0])
    for i in range(cols):
        rotated.append("")
    for j in range(len(lines)):
        line = lines[j]
        for i in range(cols):
            rotated[i] = rotated[i] + line[i]
    return find_horizontal_reflection(rotated)

def is_reflection(lines: list[str], a: int, b: int) -> bool:
    if a < 0 or b >= len(lines): return True
    if lines[a] != lines[b]: return False
    return is_reflection(lines, a - 1, b + 1)

with open(argv[1], "r") as file:
    f = file.read().splitlines()
    f.append("") # pad end with a blank line

solve(f)