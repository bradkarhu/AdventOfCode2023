import time

class Part1:
    @staticmethod
    def solution(line: str) -> int:        
        return sum(Helper.hash(s) for s in line.split(','))

class Part2:
    @staticmethod
    def solution(line: str) -> int:
        boxes = [{} for _ in range(256)] # init
        for s in line.split(','):
            if s[-1] == '-':
                a = s[:-1]
                box = boxes[Helper.hash(a)]
                if a in box: del box[a]
            else:
                a, lens = s.split('=')
                box = boxes[Helper.hash(a)]
                box[a] = int(lens) # python dict is ordered!
        #print(boxes)
        total = 0
        for i in range(len(boxes)):
            j = 1
            for _,v in boxes[i].items():
                total += (i+1) * j * v
                j += 1
        return total

class Helper:
    def hash(s: str) -> int:
        value = 0        
        for c in iter(s):
            value += ord(c)
            value *= 17
            value %= 256
        return value

tic = time.perf_counter()
#with open("sample.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()[0] # all on the first line
print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
#Part 1: 513158
#Part 2: 200277
#Took 0.0047 seconds