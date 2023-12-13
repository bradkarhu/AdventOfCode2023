import time

class Part1:
    @staticmethod
    def solution(lines: list[str]) -> int:        
        return Helper.solve(lines)

class Part2:
    @staticmethod
    def solution(lines: list[str]) -> int:
        return Helper.solve(lines, is_smudge_ok=True)

class Helper:
    def solve(lines: list[str], is_smudge_ok: bool = False) -> int:
        lineset = []
        total = 0
        setcount = 0
        for r in range(len(lines)):
            if lines[r] == "": 
                setcount += 1
                rows_above = Helper.find_horizontal_reflection(lineset)
                cols_left = Helper.find_vertical_reflection(lineset)
                if is_smudge_ok:
                    rows_above = Helper.find_horizontal_reflection(lineset, ignore=rows_above)
                    cols_left = Helper.find_vertical_reflection(lineset, ignore=cols_left)
                sum = 100 * rows_above + cols_left
                #print(f'set {setcount} = {sum} ({cols_left} cols, {rows_above} rows)')
                total += sum
                lineset.clear()
            else:
                lineset.append(lines[r])
        return total
    
    def find_horizontal_reflection(lines: list[str], ignore: int = -1) -> int:
        for i in range(len(lines) - 1):
            if ignore != -1: # part 2
                if ignore == i + 1: continue
                if Helper.is_smudgy_reflection(lines, i, i + 1):
                    return i + 1
            elif lines[i] == lines[i+1]:
                if Helper.is_reflection(lines, i, i + 1):
                    return i + 1
        return 0

    def find_vertical_reflection(lines: list[str], ignore: int = -1) -> int:
        rotated = []
        cols = len(lines[0])
        for i in range(cols):
            rotated.append("")
        for j in range(len(lines)):
            line = lines[j]
            for i in range(cols):
                rotated[i] = rotated[i] + line[i]
        return Helper.find_horizontal_reflection(rotated, ignore)
    
    def is_reflection(lines: list[str], a: int, b: int) -> bool:
        if a < 0 or b >= len(lines): return True
        if lines[a] != lines[b]: return False
        return Helper.is_reflection(lines, a - 1, b + 1)
    
    def is_smudgy_reflection(lines: list[str], a: int, b: int, smudge_line: int = -1) -> bool:
        if a < 0 or b >= len(lines): return True
        if smudge_line == -1 and Helper.has_smudge(lines[a], lines[b]):
            return Helper.is_smudgy_reflection(lines, a - 1, b + 1, a)
        if lines[a] != lines[b]: return False
        return Helper.is_smudgy_reflection(lines, a - 1, b + 1, smudge_line)
    
    def has_smudge(a: str, b: str) -> bool:
        has_smudge = False
        for i in range(len(a)):
            if a[i] != b[i]:
                if has_smudge: return False # too many differences
                else: has_smudge = True
        return has_smudge

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()
    f.append("") # pad end with a blank line
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 31956
#Part 2: 37617
#Took 0.0043 seconds